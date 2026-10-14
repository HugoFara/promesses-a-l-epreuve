"""Effets distributifs sur des ménages types (T7), avec OpenFisca-France.

Lancer avec l'environnement OpenFisca du clone local (../openfisca-france, installé en mode éditable) :
    bash ../scripts/distributif.sh   (depuis data/, ou via run_all.sh)
Entrées : data/raw/distributif_reformes.csv (paramètres des réformes, sourcés).
Sorties : data/distributif_menages.csv (gain ou perte de revenu disponible, €/an, par ménage type et réforme) ;
          data/distributif_grille.csv (même calcul sur une grille de situations, lue par le simulateur du site).

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
# Situation stable : mêmes revenus les deux années précédentes. Plusieurs calculs de 2026 lisent les revenus de
# l'année N-2 (taux de CSG des pensions selon le revenu fiscal de référence de 2024, ressources des prestations
# familiales) ; sans eux, ces revenus valent 0 et tous les retraités seraient exonérés de CSG. Les réformes sont
# appliquées sur les trois années : effet en régime permanent, pas la seule première année.
ANNEES = [str(int(ANNEE) - 2), str(int(ANNEE) - 1), ANNEE]
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
                d[var] = {m: a[var] for an in ANNEES for m in mois(an)}
        ind[f"a{i}"] = d
    for j, n in enumerate(enfants):
        ind[f"e{j}"] = {"date_naissance": {"ETERNITY": n}}
    adultes_ids = [k for k in ind if k.startswith("a")]
    enfants_ids = [k for k in ind if k.startswith("e")]
    foyer = {"declarants": adultes_ids, "personnes_a_charge": enfants_ids}
    for var, val in (revenus_foyer or {}).items():
        foyer[var] = {an: val for an in ANNEES}
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


# Grille du simulateur : conventions, comme les ménages types. Revenus d'activité en multiples du SMIC brut,
# pensions en montants ronds encadrant le seuil du gel (1 281 € bruts), dividendes annuels du foyer.
GRILLE_SALAIRES = [0.5, 1, 1.25, 1.5, 2, 3, 4, 6]
GRILLE_PENSIONS = [900, 1250, 1500, 2000, 2500, 3500, 5000]
GRILLE_CAPITAL = [0, 2000, 10000, 50000]
GRILLE_ENFANTS = ["2016-01-01", "2019-01-01", "2022-01-01"]  # 10, 7 et 4 ans en 2026
COMPOSITIONS = {"seul": 1, "couple_2": 2, "couple_1": 2}  # couple_1 : le conjoint n'a pas de revenu


def grille():
    """Situations du simulateur : (attributs, adultes, enfants, revenus du foyer)."""
    out = []
    for statut, niveaux, naiss in (("actif", GRILLE_SALAIRES, ("1985-01-01", "1987-01-01")),
                                   ("retraite", GRILLE_PENSIONS, ("1955-01-01", "1957-01-01"))):
        var = "salaire_de_base" if statut == "actif" else "retraite_brute"
        for compo, nb in COMPOSITIONS.items():
            for ne in range(4 if statut == "actif" else 1):
                for niv in niveaux:
                    mensuel = round(niv * S, 2) if statut == "actif" else niv
                    adultes = [{"naissance": naiss[0], var: mensuel}]
                    if nb == 2:
                        adultes.append({"naissance": naiss[1], **({var: mensuel} if compo == "couple_2" else {})})
                    for cap in GRILLE_CAPITAL:
                        out.append(({"statut": statut, "composition": compo, "enfants": ne, "niveau": niv,
                                     "capital": cap}, adultes, GRILLE_ENFANTS[:ne], {"f2dc": cap} if cap else {}))
    return out


def fusionner(cas_liste):
    """Une seule situation OpenFisca contenant tous les foyers (une simulation au lieu d'une par foyer)."""
    tout = {"individus": {}, "foyers_fiscaux": {}, "menages": {}, "familles": {}}
    for k, (_, cas) in enumerate(cas_liste):
        ren = {i: f"m{k}_{i}" for i in cas["individus"]}
        tout["individus"].update({ren[i]: v for i, v in cas["individus"].items()})
        for ent, d in cas.items():
            if ent == "individus":
                continue
            (_, v), = d.items()
            tout[ent][f"{ent[0]}{k}"] = {r: ([ren[i] for i in x] if isinstance(x, list) else x) for r, x in v.items()}
    return tout


def option_optimale(cas):
    """Situation de référence : chaque foyer qui a des revenus du capital choisit déjà, comme la loi le permet
    (case 2OP), le plus avantageux du PFU et du barème. Sans cela, supprimer le PFU ferait gagner les foyers
    pour qui le barème est plus favorable, alors qu'ils peuvent déjà l'obtenir. Le choix reste ensuite figé
    pour les autres réformes (effet de second ordre négligé)."""
    import copy
    if not any("f2dc" in f for f in cas["foyers_fiscaux"].values()):
        return cas
    sans = SimulationBuilder().build_from_entities(TBS, cas).calculate_add("revenu_disponible", ANNEE)
    avec_cas = copy.deepcopy(cas)
    for f in avec_cas["foyers_fiscaux"].values():
        f["f2op"] = {an: True for an in ANNEES}
    avec = SimulationBuilder().build_from_entities(TBS, avec_cas).calculate_add("revenu_disponible", ANNEE)
    # Un foyer fiscal par ménage, dans le même ordre (voir menage et fusionner)
    for k, f in enumerate(cas["foyers_fiscaux"].values()):
        if "f2dc" in f and avec[k] > sans[k]:
            f["f2op"] = {an: True for an in ANNEES}
    return cas


def simuler_grille(reformes):
    situations = grille()
    cas = option_optimale(fusionner([menage("", ad, en, rf) for _, ad, en, rf in situations]))
    sim = SimulationBuilder().build_from_entities(TBS, cas)
    avant = sim.calculate_add("revenu_disponible", ANNEE)
    # Revenu mensuel net de la personne de référence, pour décrire la situation en euros nets sur le site
    ids = list(cas["individus"])
    net = sim.calculate_add("salaire_net", ANNEE) + sim.calculate_add("retraite_nette", ANNEE)
    net_ref = {i: net[ids.index(i)] / 12 for i in ids}
    apres = {}
    for r in reformes:
        tbs, cas_r = appliquer(r, cas)
        apres[r["id"]] = SimulationBuilder().build_from_entities(tbs, cas_r).calculate_add("revenu_disponible", ANNEE)
    out = []
    for k, (attr, *_) in enumerate(situations):
        base = {**attr, "net_mensuel_reference": round(float(net_ref[f"m{k}_a0"])),
                "revenu_disponible_avant": round(float(avant[k]))}
        base["id"] = "_".join(str(attr[c]) for c in ("statut", "composition", "enfants", "niveau", "capital"))
        for r in reformes:
            g = float(apres[r["id"]][k] - avant[k])
            out.append({**base, "reforme": r["id"], "gain_annuel": round(g), "gain_pct": round(g / float(avant[k]) * 100, 2)})
    return out


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
                noeud.update(start=f"{ANNEES[0]}-01-01", value=valeur)
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
        for f in cas["foyers_fiscaux"].values():
            f["f2op"] = {an: True for an in ANNEES}
        return TBS, cas
    if r["type"] == "smic_net_cible":
        # Salariés payés au SMIC horaire (temps plein, ou temps partiel s'ils gagnent moins d'un SMIC mensuel) :
        # brut relevé dans le rapport (SMIC net cible / SMIC net actuel), approximation valable au voisinage du
        # SMIC où les cotisations salariales sont proportionnelles. Les salaires au-dessus ne bougent pas
        # (pas d'effet de diffusion modélisé).
        ratio = float(r["valeur"]) / smic_net_mensuel()
        for ind in cas["individus"].values():
            sal = ind.get("salaire_de_base")
            if sal and next(iter(sal.values())) <= S + 1:
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
        cas = option_optimale(cas)
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
    g = simuler_grille(reformes)
    cols = ["id", "statut", "composition", "enfants", "niveau", "capital", "net_mensuel_reference",
            "revenu_disponible_avant", "reforme", "gain_annuel", "gain_pct"]
    with open("distributif_grille.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, cols, lineterminator="\n")
        w.writeheader()
        w.writerows(g)
    print(f"grille : {len(g) // len(reformes)} situations × {len(reformes)} réformes")
    for o in out:
        print(f"{o['menage'][:45]:<46} {o['reforme']:<14} {o['gain_annuel']:>7} €/an ({o['gain_pct']:+.1f} %)")


if __name__ == "__main__":
    main()
