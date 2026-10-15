"""Moteur de correction (T4) : facteur calculé par formule à partir de paramètres sourcés, avec Monte-Carlo.

Entrées (data/) : moteur_regles.csv, moteur_parametres.csv, application_lignes.csv, paniers.csv.
Sorties (data/) : moteur_lignes.csv (facteur forfaitaire vs moteur, P10/P90 par ligne),
                  moteur_totaux.csv (P10/P50/P90 par programme et par variante de panier),
                  moteur_variantes.csv (variantes de sensibilité : solde central et P10/P50/P90).

Montant corrigé d'une ligne = statique × facteur de la règle × facteur de référence × facteur d'interaction.
- Facteur de la règle : formule de moteur_regles.csv ; si un paramètre manque, facteur forfaitaire (mode = forfait).
- Facteur de référence (part hors référence 2027) et d'interaction (recoupement avec d'autres lignes du même
  programme) : tirés dans leur intervalle documenté (colonnes *_bas, *_haut) quand il existe.
Incertitude :
- chaque paramètre est tiré une fois par simulation et partagé par tous les partis ;
- erreur de chiffrage par ligne : bruit normal de médiane absolue erreur_ligne (T10b), dont une part
  (part_commune_erreur) est commune à toutes les lignes d'un même chiffreur, tronqué à ±90 % ;
- une même mesure reçoit le même tirage dans toutes les variantes de panier.
Les lignes « Investissement (règle d'or) » sont comptées à part (composante investissement), hors solde.
Variante « loi votée seule » : les lignes au statut « proposée » ne sont plus décotées (facteur de référence 1).
"""
import csv
import math
import os

import numpy as np

N_SIM = 20_000
GRAINE = 2027
LARGE = os.environ.get("INCERTITUDE_LARGE") == "1"
MEDIANE_ABS_NORMALE = 0.6745


def lire(f):
    with open(f, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def num(x):
    return float(x) if x not in ("", None) else None


# --- Formules : scalaires ou tableaux numpy (une valeur par simulation)
FORMULES = {
    "fixe": lambda p: p["valeur"],
    "complement": lambda p: 1 - p["valeur"],
    # Hausse de taux t0→t1 sur une base d'élasticité eps au taux net : recette réelle / recette statique
    "taxe_elasticite": lambda p: (p["t1"] * ((1 - p["t1"]) / (1 - p["t0"])) ** p["eps"] - p["t0"]) / (p["t1"] - p["t0"]),
    # Base réduite de s par point, effet atteint à la fraction h (sans perte sur un impôt existant)
    "semi_elasticite": lambda p: 1 - p["s"] * p["delta"] * p["h"],
    # Hausse de delta points sur un impôt existant de t0 points : la base perdue fait aussi perdre l'impôt existant
    "semi_elasticite_taux": lambda p: 1 - p["s"] * (p["t0"] + p["delta"]) * p["h"],
    # Hausse d'accise répercutée : prix +dp ; quantité × (1 + eps·dp) ; perte de l'accise existante a (en part de la hausse)
    "accise": lambda p: (1 + p["eps"] * p["dp"]) + p["a"] * p["eps"] * p["dp"],
    "smic": lambda p: 1 + abs(p["eps"]) * p["hausse"] * p["n"] * p["c"] / 1e9 / p["statique"],
    # Montant en Md€ (ligne de statique −1) : emplois perdus × coût par emploi
    "montant": lambda p: p["emplois"] * p["c"] / 1e9,
    # Montant en Md€ : emplois perdus = |élasticité au coût| × hausse moyenne du coût × effectif concerné, × coût par emploi
    # Taxe dont l'assiette fuit : assiette relative b × (1 − part perdue s) − recette existante remplacée r (en part du statique)
    "assiette_reduite_nette": lambda p: (1 - p["s"]) * p["b"] - p["r"],
    "emploi_smic": lambda p: abs(p["eps"]) * p["h"] * p["n"] * p["c"] / 1e9,
}


def tri(rng, lo, c, hi, n):
    """Loi triangulaire (bas, central, haut) ; un côté manquant = central."""
    lo = c if lo is None else lo
    hi = c if hi is None else hi
    lo, hi = min(lo, hi), max(lo, hi)
    return np.full(n, c) if hi == lo else rng.triangular(lo, min(max(c, lo), hi), hi, n)


def noms_parametres(mr):
    if mr["formule"] in ("fixe", "complement"):
        return {"valeur": mr["parametres"]}
    return dict(kv.split("=") for kv in mr["parametres"].split(";"))


def chiffreur(r):
    """Source du chiffrage de départ, pour l'erreur commune : nom repéré dans la colonne source."""
    s = (r.get("source_independant") or r.get("source") or "").lower()
    for nom in ("montaigne", "ifrap", "grande conversation", "asterès", "ofce", "cae", "france stratégie", "plfss", "plf",
                "bozio", "nfp", "calcul", "médiane"):
        if nom in s:
            return nom
    return s[:20]


def main():
    rng = np.random.default_rng(GRAINE)
    mregles = {r["regle"]: r for r in lire("moteur_regles.csv")}
    params = {r["id"]: {"lo": num(r["val_bas"]), "c": num(r["val_central"]), "hi": num(r["val_haut"])}
              for r in lire("moteur_parametres.csv")}
    tirages = {k: tri(rng, v["lo"], v["c"], v["hi"], N_SIM) for k, v in params.items()}

    fact = {}
    for nom, mr in mregles.items():
        if mr["formule"] == "ligne":
            continue
        noms = noms_parametres(mr)
        manquants = [v for v in noms.values() if v not in params]
        if manquants:
            fact[nom] = {"mode": "forfait", "manquants": manquants}
            continue
        f = FORMULES[mr["formule"]]
        fact[nom] = {"mode": "moteur", "central": float(f({k: params[v]["c"] for k, v in noms.items()})),
                     "dist": np.broadcast_to(f({k: tirages[v] for k, v in noms.items()}), (N_SIM,))}

    # Erreur de ligne : composante commune par chiffreur + composante propre, même médiane absolue au total
    sigma = params["erreur_ligne"]["hi" if LARGE else "c"] / MEDIANE_ABS_NORMALE
    rho = params["part_commune_erreur"]["c"]
    communs, propres, refs = {}, {}, {}

    def bruit(cle_mesure, cle_chiffreur):
        if cle_chiffreur not in communs:
            communs[cle_chiffreur] = rng.normal(0, sigma * math.sqrt(rho), N_SIM)
        if cle_mesure not in propres:
            propres[cle_mesure] = rng.normal(0, sigma * math.sqrt(1 - rho), N_SIM)
        return 1 + np.clip(communs[cle_chiffreur] + propres[cle_mesure], -0.9, 0.9)

    def facteur_tire(cle, lo, c, hi):
        """Même tirage pour une même mesure dans toutes les variantes."""
        if cle not in refs:
            refs[cle] = tri(rng, lo, c, hi, N_SIM)
        return refs[cle]

    lignes, totaux, tirs = [], {}, {}
    for fichier, groupe_col, montant_col in (("application_lignes", "programme", "independant"), ("paniers", "variante", "statique")):
        for r in lire(f"{fichier}.csv"):
            m = float(r[montant_col])
            base_id = r["id"].rsplit("_", 1)[0] if fichier == "paniers" else r["id"]
            f_ref = num(r.get("facteur_reference"))
            f_ref = 1.0 if f_ref is None else f_ref
            f_ref_dist = facteur_tire((fichier, base_id, "ref"), num(r.get("facteur_reference_bas")), f_ref,
                                      num(r.get("facteur_reference_haut")))
            f_int = num(r.get("facteur_interaction"))
            f_int = 1.0 if f_int is None else f_int
            f_int_dist = facteur_tire((fichier, base_id, "int"), num(r.get("facteur_interaction_bas")), f_int,
                                      num(r.get("facteur_interaction_haut")))
            f_ref_vote = 1.0 if r.get("statut_reference") == "proposée" else f_ref
            f_ref_2028 = num(r.get("facteur_reference_2028"))
            f_ref_2028 = f_ref if f_ref_2028 is None else f_ref_2028
            f_forfait = float(r["facteur"])
            info = fact.get(r["regle"])
            if info and info["mode"] == "moteur":
                f_c, dist, mode = info["central"], info["dist"], "moteur"
            else:
                f_c, dist = f_forfait, np.full(N_SIM, f_forfait)
                mode = "ligne" if info is None else "forfait"
            role = r.get("role", "")
            # Montant choisi par le parti (investissement) : pas d'erreur d'estimation
            err = 1.0 if role.startswith("Investissement") else bruit((fichier, base_id), chiffreur(r))
            sim = m * dist * f_ref_dist * f_int_dist * err
            tirs[(fichier, r["id"])] = (dist, f_ref_dist, f_int_dist, err)
            central = m * f_c * f_ref * f_int
            ecart = (f_c - f_forfait) / f_forfait * 100 if f_forfait else (0.0 if f_c == 0 else math.inf)
            composante = "investissement" if role.startswith("Investissement") else (role or "total")
            lignes.append({
                "fichier": fichier, "id": r["id"], "groupe": r[groupe_col], "composante": composante, "regle": r["regle"],
                "mode": mode, "montant": m, "facteur_forfait": f_forfait, "facteur_moteur": round(f_c, 4),
                "facteur_reference": f_ref, "facteur_interaction": f_int, "ecart_facteur_pct": round(ecart, 1),
                "dans_tolerance": abs(ecart) <= 10 or bool(mregles[r["regle"]]["justification_ecart"]),
                "corrige_central": round(central, 2), "corrige_loi_votee": round(m * f_c * f_ref_vote * f_int, 2),
                "corrige_2028": round(m * f_c * f_ref_2028 * f_int, 2),
                "p10": round(float(np.percentile(sim, 10)), 2), "p90": round(float(np.percentile(sim, 90)), 2),
                "parametres_manquants": " ".join(info.get("manquants", [])) if info else "",
            })
            t = totaux.setdefault((fichier, r[groupe_col]), {})
            c = t.setdefault(composante, [0.0, 0.0, np.zeros(N_SIM)])
            c[0] += central
            c[1] += m * f_c * f_ref_vote * f_int
            c[2] = c[2] + sim

    with open("moteur_lignes.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(lignes[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(lignes)

    out = []
    for (fichier, groupe), comps in totaux.items():
        solde = [0.0, 0.0, np.zeros(N_SIM)]
        for comp, (c, cv, s) in comps.items():
            if comp != "investissement":
                solde = [solde[0] + c, solde[1] + cv, solde[2] + s]
        items = {**comps, "solde": solde} if fichier == "paniers" else {"solde": solde}
        for comp, (c, cv, s) in items.items():
            p10, p50, p90 = np.percentile(s, [10, 50, 90])
            out.append({"fichier": fichier, "groupe": groupe, "composante": comp, "central": round(c, 1),
                        "loi_votee_seule": round(cv, 1), "p10": round(p10, 1), "p50": round(p50, 1), "p90": round(p90, 1)})
    with open("moteur_totaux.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(out[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    # Variantes de sensibilité : surcharge de colonnes de lignes de panier. Les tirages (règle, erreur, référence,
    # interaction) sont ceux du scénario central ; un facteur dont l'intervalle est surchargé est retiré dans son
    # nouvel intervalle (générateur dédié, pour ne pas décaler les tirages du central).
    rng_var = np.random.default_rng(GRAINE + 1)
    variantes = {}
    for v in lire("variantes_sensibilite.csv"):
        variantes.setdefault((v["variante"], v["libelle"]), []).append(v)
    sorties_var = []
    for (vid, lib), surcharges in variantes.items():
        for fichier, groupe_col, montant_col in (("paniers", "variante", "statique"),):
            soldes, sims_var = {}, {}
            for r in lire(f"{fichier}.csv"):
                if r.get("role", "").startswith("Investissement"):
                    continue
                base_id = r["id"].rsplit("_", 1)[0]
                cols = set()
                for s_ in surcharges:
                    if s_["id"] == base_id:
                        r[s_["colonne"]] = s_["valeur"]
                        cols.add(s_["colonne"])
                l = next(x for x in lignes if x["fichier"] == fichier and x["id"] == r["id"])
                dist, f_ref_dist, f_int_dist, err = tirs[(fichier, r["id"])]
                f_ref = num(r.get("facteur_reference"))
                f_ref = 1.0 if f_ref is None else f_ref
                if cols & {"facteur_reference", "facteur_reference_bas", "facteur_reference_haut"}:
                    f_ref_dist = tri(rng_var, num(r.get("facteur_reference_bas")), f_ref, num(r.get("facteur_reference_haut")), N_SIM)
                m = float(r[montant_col])
                g = r[groupe_col]
                soldes[g] = soldes.get(g, 0.0) + m * l["facteur_moteur"] * f_ref * l["facteur_interaction"]
                sims_var[g] = sims_var.get(g, 0.0) + m * dist * f_ref_dist * f_int_dist * err
            for g, v in soldes.items():
                p10, p50, p90 = np.percentile(sims_var[g], [10, 50, 90])
                sorties_var.append({"variante": vid, "libelle": lib, "groupe": g, "solde_central": round(v, 1),
                                    "p10": round(p10, 1), "p50": round(p50, 1), "p90": round(p90, 1)})
    if sorties_var:
        with open("moteur_variantes.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, list(sorties_var[0]), lineterminator="\n")
            w.writeheader()
            w.writerows(sorties_var)
        for s_ in sorties_var:
            print(f"variante {s_['variante']:<8} {s_['groupe']:<16} solde central {s_['solde_central']:>7}  "
                  f"P10 {s_['p10']:>7}  P50 {s_['p50']:>7}  P90 {s_['p90']:>7}")
    for o in out:
        print(f"{o['groupe']:<16} {o['composante']:<15} central {o['central']:>7}  loi votée {o['loi_votee_seule']:>7}  "
              f"P10 {o['p10']:>7}  P50 {o['p50']:>7}  P90 {o['p90']:>7}")
    for l in lignes:
        if not l["dans_tolerance"]:
            print(f"hors tolérance ±10 % sans justification : {l['id']} ({l['regle']}) {l['ecart_facteur_pct']} %")
    print("règles encore au forfait :", "; ".join(sorted({l["regle"] for l in lignes if l["mode"] == "forfait"})) or "aucune")


if __name__ == "__main__":
    main()
