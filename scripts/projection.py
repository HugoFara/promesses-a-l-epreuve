"""Projection pluriannuelle du déficit et de la dette, 2026-2032 (T5).

Entrées (data/) : projection_reference.csv (trajectoire du gouvernement : croissance, déflateur, solde ; dette publiée
                  pour contrôle ; ajustements stock-flux), projection_parametres.csv, moteur_lignes.csv, montee_en_charge.csv.
Sorties (data/) : projection.csv (scénario × année), projection_controle.csv.

Mécanique, par année t (Md€ ; ratios en % du PIB) :
  PIB_t      = PIB publié (PLF 2027 pour 2026-2027), sinon PIB_{t-1} × (1 + croissance réelle) × (1 + déflateur)
  déficit_t  = déficit de référence_t + biais_t + impact du programme_t + intérêts supplémentaires_t
  dette_t    = dette_{t-1} + déficit_t + ajustement stock-flux_t
  biais_t    : couche 2, selon l'horizon h = t − année du PLF (h = 1 : biais à 1 an ; interpolé jusqu'à 3 ans ; constant ensuite)
  impact_t   = Σ lignes (montant corrigé de l'année, moteur_lignes.csv) × PIB_t / PIB_2027 :
               2027 = corrige_central ; 2028 et après = corrige_2028 (facteur de référence propre à 2028+,
               ex. surtaxe d'IS temporaire dans la référence), × coefficient de montée en charge de l'année
               (montee_en_charge.csv, central ; 1 par défaut, soit constant en % du PIB).
  investissement_t = emprunt « règle d'or » (lignes Investissement), compté dans le déficit et la dette, publié à part
  intérêts supplémentaires_t = dette supplémentaire_{t-1} × taux OAT
                             + Σ_u spread_u × (part refinancée(u) − part refinancée(u−1)) × dette de référence_{t-1}
                               (chaque tranche refinancée l'année u garde le spread de u) + choc × part refinancée
  spread_u   = 3 pb × écart de dette au scénario de référence (points de PIB)
  part refinancée(k) : profil AFT/Sénat (+100 pb = 3,2 Md€ à 1 an, 19,1 à 5 ans, 32,6 à 9 ans, rapportés à 32,6).
La dette publiée par le gouvernement n'entre pas dans le calcul : elle sert de contrôle (critère T5).
"""
import csv

import numpy as np


def lire(f):
    with open(f, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def num(x):
    return float(x) if x not in ("", None) else None


P = {r["id"]: float(r["valeur"]) for r in lire("projection_parametres.csv")}
REF = {int(r["annee"]): r for r in lire("projection_reference.csv")}
ANNEES = sorted(REF)
A0 = ANNEES[0]
PLF = int(P["annee_plf"])

# PIB publié quand il existe, sinon prolongé par la croissance réelle et le déflateur
PIB = {A0: float(REF[A0]["pib"])}
for t in ANNEES[1:]:
    PIB[t] = float(REF[t]["pib"]) if REF[t]["pib"] else \
        PIB[t - 1] * (1 + float(REF[t]["croissance_reelle"]) / 100) * (1 + float(REF[t]["deflateur"]) / 100)

_k, _v = [0, 1, 5, 9], [0, P["aft_1an"] / P["aft_9ans"], P["aft_5ans"] / P["aft_9ans"], 1.0]


def part_refinancee(k):
    return float(np.interp(k, _k, _v))


def biais(t):
    h = t - PLF
    if h <= 0:
        return 0.0
    return float(np.interp(h, [1, 3], [P["biais_t1"], P["biais_t3"]]))  # constant au-delà de 3 ans (np.interp borne)


def reference():
    """Dette de référence calculée à partir des déficits et ajustements stock-flux du gouvernement."""
    dette = {A0: float(REF[A0]["dette_pct"]) / 100 * PIB[A0]}
    for t in ANNEES[1:]:
        dette[t] = dette[t - 1] - float(REF[t]["solde_pct"]) / 100 * PIB[t] + float(REF[t]["sfa_pct"] or 0) / 100 * PIB[t]
    return dette


DETTE_REF = reference()


def trajectoire(impact, choc_pb=0.0, avec_biais=True, invest=None):
    """impact : dict année -> Md€ (négatif = creuse le déficit), aux prix de 2027 ; invest : idem (emprunt)."""
    out, dette, spreads = [], DETTE_REF[A0], {}
    for t in ANNEES[1:]:
        def_ref = -float(REF[t]["solde_pct"]) / 100 * PIB[t]
        sfa = float(REF[t]["sfa_pct"] or 0) / 100 * PIB[t]
        b = -biais(t) / 100 * PIB[t] if avec_biais else 0.0
        ech = PIB[t] / PIB[2027]
        imp = -(impact.get(t, impact.get(2028, 0.0)) if t >= 2027 else 0.0) * ech
        inv = -((invest or {}).get(min(t, 2028), 0.0) if t >= 2027 else 0.0) * ech
        dette_sup = dette - DETTE_REF[t - 1]
        spreads[t] = P["spread_pb_par_pt"] * (dette_sup / PIB[t - 1] * 100) / 1e4
        sp = sum(spreads[u] * (part_refinancee(u - PLF) - part_refinancee(u - 1 - PLF)) for u in spreads)
        interets = dette_sup * P["taux_oat"] / 100 + (sp + choc_pb / 1e4 * part_refinancee(t - PLF)) * DETTE_REF[t - 1]
        deficit = def_ref + b + imp + inv + interets
        dette = dette + deficit + sfa
        out.append({"annee": t, "extrapole": REF[t]["extrapole"], "deficit_pct": round(deficit / PIB[t] * 100, 2),
                    "dont_investissement_pct": round(inv / PIB[t] * 100, 2), "dette_pct": round(dette / PIB[t] * 100, 1),
                    "biais_pct": round(b / PIB[t] * 100, 2), "impact_md": round(-imp, 1), "investissement_md": round(-inv, 1),
                    "interets_sup_md": round(interets, 1), "pib_md": round(PIB[t])})
    return out


def main():
    ml = [r for r in lire("moteur_lignes.csv") if r["fichier"] == "paniers"]
    # Montée en charge (montee_en_charge.csv) : coefficient central par année, relatif au montant 2027 en % du PIB
    mec = {}
    for r in lire("montee_en_charge.csv"):
        mec.setdefault(r["id"], {})[int(r["annee"])] = float(r["coef_central"])
    impacts, invests = {}, {}
    for r in ml:
        cible = invests if r["composante"] == "investissement" else impacts
        d = cible.setdefault(r["groupe"], {t: 0.0 for t in ANNEES if t >= 2027})
        coef = mec.get(r["id"].rsplit("_", 1)[0], {})
        for t in d:
            d[t] += float(r["corrige_central" if t == 2027 else "corrige_2028"]) * coef.get(t, 1.0)
    choc = P["choc_stress_pb"]
    scenarios = [("Référence du gouvernement", {}, 0.0, False, None),
                 ("Référence corrigée du biais", {}, 0.0, True, None),
                 ("Référence corrigée, stress +25 pb", {}, choc, True, None)]
    for g, imp in impacts.items():
        inv = invests.get(g)
        scenarios += [(f"Panier {g}", imp, 0.0, True, inv), (f"Panier {g}, stress +25 pb", imp, choc, True, inv)]
    lignes = [{"scenario": nom, **r} for nom, imp, ch, ab, inv in scenarios for r in trajectoire(imp, ch, ab, inv)]
    with open("projection.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(lignes[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(lignes)

    # Contrôle T5 : sans biais ni programme, la dette calculée reproduit la dette publiée du PLF
    ref = {r["annee"]: r for r in trajectoire({}, avec_biais=False)}
    controle = [{"annee": t, "indicateur": ind, "calcule": ref[t][ind], "plf": v,
                 "ecart": round(ref[t][ind] - v, 2)}
                for t in ANNEES[1:]
                for ind, v in (("deficit_pct", -num(REF[t]["solde_pct"])), ("dette_pct", num(REF[t]["dette_pct"])))
                if v is not None and REF[t]["extrapole"] == "0"]
    with open("projection_controle.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(controle[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(controle)
    for c in controle:
        print(f"contrôle {c['annee']} {c['indicateur']:<12} calculé {c['calcule']:>6}  PLF {c['plf']:>6}  écart {c['ecart']:+.2f}")
    for nom in dict.fromkeys(l["scenario"] for l in lignes):
        traj = [l for l in lignes if l["scenario"] == nom]
        print(f"{nom:<40}" + " ".join(f"{l['annee']}:{l['deficit_pct']:>5.1f}/{l['dette_pct']:>5.1f}" for l in traj))


if __name__ == "__main__":
    main()
