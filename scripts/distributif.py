"""Effets distributifs sur des ménages types (T7), avec OpenFisca-France.

Lancer avec l'environnement OpenFisca du clone local (../openfisca-france, installé en mode éditable) :
    bash ../scripts/distributif.sh   (depuis data/, ou via run_all.sh)
Entrées : data/raw/distributif_reformes.csv (paramètres des réformes, sourcés).
Sortie  : data/distributif_menages.csv (gain ou perte de revenu disponible, €/an, par ménage et réforme).

Les ménages types sont des conventions (multiples du SMIC, montants ronds), pas des données : ils servent à
montrer qui gagne et qui perd, pas à chiffrer un coût agrégé. Les effets par décile demandent une
microsimulation sur données d'enquête (ERFS, accessible via le CASD) : hors de portée ici (voir HANDOFF).
"""
import csv
import warnings

warnings.filterwarnings("ignore")

from openfisca_core.reforms import Reform  # noqa: E402
from openfisca_core.simulation_builder import SimulationBuilder  # noqa: E402
from openfisca_france import FranceTaxBenefitSystem  # noqa: E402

ANNEE = "2026"  # législation de référence disponible dans OpenFisca (fin 2026)
TBS = FranceTaxBenefitSystem()
_P = TBS.parameters(f"{ANNEE}-01-01")
SMIC_BRUT_MENSUEL = round(_P.marche_travail.salaire_minimum.smic.smic_b_horaire * 151.67, 2)


def mois(an):
    return [f"{an}-{m:02d}" for m in range(1, 13)]


def menage(nom, adultes, enfants=(), revenus_foyer=None):
    """adultes : liste de dicts {date_naissance, salaire_de_base (mensuel brut) | retraite_brute (mensuelle)}."""
    ind = {}
    for i, a in enumerate(adultes):
        d = {"date_naissance": {"ETERNITY": a["naissance"]}}
        for var in ("salaire_de_base", "retraite_brute"):
            if var in a:
                d[var] = {m: a[var] for m in mois(ANNEE)}
        ind[f"a{i}"] = d
    for j, n in enumerate(enfants):
        ind[f"e{j}"] = {"date_naissance": {"ETERNITY": n}}
    adultes_ids = [k for k in ind if k.startswith("a")]
    enfants_ids = [k for k in ind if k.startswith("e")]
    foyer = {"declarants": adultes_ids, "personnes_a_charge": enfants_ids}
    for var, val in (revenus_foyer or {}).items():
        foyer[var] = {ANNEE: val}
    return nom, {
        "individus": ind,
        "foyers_fiscaux": {"f": foyer},
        "menages": {"m": {"personne_de_reference": adultes_ids[:1], "conjoint": adultes_ids[1:2],
                          "enfants": enfants_ids}},
        "familles": {"fa": {"parents": adultes_ids, "enfants": enfants_ids}},
    }


S = SMIC_BRUT_MENSUEL
MENAGES = [
    menage("Salarié au SMIC, célibataire", [{"naissance": "1990-01-01", "salaire_de_base": S}]),
    menage("Couple de retraités (pensions 2 000 + 1 300 € bruts/mois)",
           [{"naissance": "1955-01-01", "retraite_brute": 2000}, {"naissance": "1957-01-01", "retraite_brute": 1300}]),
    menage("Cadre célibataire (4 SMIC, 5 000 € de dividendes)", [{"naissance": "1980-01-01", "salaire_de_base": 4 * S}],
           revenus_foyer={"f2dc": 5000}),
    menage("Famille monoparentale, 1 enfant, SMIC", [{"naissance": "1988-01-01", "salaire_de_base": S}],
           enfants=["2018-01-01"]),
]


def simuler(tbs, cas):
    sim = SimulationBuilder().build_from_entities(tbs, cas)
    return float(sim.calculate_add("revenu_disponible", ANNEE).sum())


def reforme_parametre(chemin, valeur):
    class R(Reform):
        def apply(self):
            def modif(params):
                noeud = params
                for k in chemin.split("."):
                    noeud = getattr(noeud, k) if hasattr(noeud, k) else noeud.children[k]
                noeud.update(start=f"{ANNEE}-01-01", value=valeur)
                return params
            self.modify_parameters(modifier_function=modif)
    return R(TBS)


def smic_net_mensuel():
    _, cas = MENAGES[0]
    sim = SimulationBuilder().build_from_entities(TBS, cas)
    return float(sim.calculate_add("salaire_net", ANNEE).sum()) / 12


def lire_reformes():
    with open("raw/distributif_reformes.csv", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def appliquer(r, cas):
    """Retourne (système, cas modifié) pour la réforme r."""
    import copy
    cas = copy.deepcopy(cas)
    if r["type"] == "parametre":
        return reforme_parametre(r["cible"], float(r["valeur"])), cas
    if r["type"] == "option_bareme_capital":
        cas["foyers_fiscaux"]["f"]["f2op"] = {ANNEE: True}
        return TBS, cas
    if r["type"] == "smic_net_cible":
        # Salariés au SMIC : brut relevé dans le rapport (SMIC net cible / SMIC net actuel), approximation
        # valable au voisinage du SMIC où les cotisations salariales sont proportionnelles
        ratio = float(r["valeur"]) / smic_net_mensuel()
        for ind in cas["individus"].values():
            sal = ind.get("salaire_de_base")
            if sal and abs(next(iter(sal.values())) - S) < 1:
                for m in sal:
                    sal[m] = round(sal[m] * ratio, 2)
        return TBS, cas
    if r["type"] == "gel_pensions":
        # Pensions brutes mensuelles au-dessus du seuil : revalorisation (inflation) non versée.
        # La situation de référence suppose la pension revalorisée ; le gel la réduit de 1 / (1 + inflation).
        seuil, inflation = (float(x) for x in r["valeur"].split(";"))
        for ind in cas["individus"].values():
            pen = ind.get("retraite_brute")
            if pen and next(iter(pen.values())) > seuil:
                for m in pen:
                    pen[m] = round(pen[m] / (1 + inflation), 2)
        return TBS, cas
    raise ValueError(r["type"])


def main():
    reformes = lire_reformes()
    out = []
    for nom, cas in MENAGES:
        avant = simuler(TBS, cas)
        for r in reformes:
            tbs, cas_r = appliquer(r, cas)
            apres = simuler(tbs, cas_r)
            out.append({"menage": nom, "reforme": r["id"], "libelle": r["libelle"], "annee_legislation": ANNEE,
                        "revenu_disponible_avant": round(avant), "revenu_disponible_apres": round(apres),
                        "gain_annuel": round(apres - avant), "gain_pct": round((apres - avant) / avant * 100, 2)})
    with open("distributif_menages.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(out[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    for o in out:
        print(f"{o['menage'][:45]:<46} {o['reforme']:<14} {o['gain_annuel']:>7} €/an ({o['gain_pct']:+.1f} %)")


if __name__ == "__main__":
    main()
