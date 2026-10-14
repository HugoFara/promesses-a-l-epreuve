"""Audit T5 : variantes de projection (lecture seule de data/). Lancer depuis data/ :
   cd data && python3 ../recherche/audit/projection_variantes.py
(a) LFI ajusté avec l'emprunt « règle d'or » (−30 Md€/an) dans la dette et les intérêts ;
(b) spread appliqué par millésime de refinancement (la dette refinancée en t garde le spread de t)."""
import csv
import numpy as np

P = {r["id"]: float(r["valeur"]) for r in csv.DictReader(open("projection_parametres.csv", encoding="utf-8"))}
REF = {int(r["annee"]): r for r in csv.DictReader(open("projection_reference.csv", encoding="utf-8"))}
AN = sorted(REF); A0 = AN[0]; PLF = int(P["annee_plf"])
PIB = {A0: float(REF[A0]["pib"])}
for t in AN[1:]:
    PIB[t] = PIB[t-1] * (1 + float(REF[t]["croissance_reelle"]) / 100) * (1 + float(REF[t]["deflateur"]) / 100)
K, V = [0, 1, 5, 9], [0, P["aft_1an"] / P["aft_9ans"], P["aft_5ans"] / P["aft_9ans"], 1.0]
part = lambda k: float(np.interp(k, K, V))
biais = lambda t: 0.0 if t - PLF <= 0 else float(np.interp(t - PLF, [1, 3], [P["biais_t1"], P["biais_t3"]]))
DREF = {A0: float(REF[A0]["dette_pct"]) / 100 * PIB[A0]}
for t in AN[1:]:
    DREF[t] = DREF[t-1] - float(REF[t]["solde_pct"]) / 100 * PIB[t] + float(REF[t]["sfa_pct"] or 0) / 100 * PIB[t]

def traj(imp, millesime=False):
    dette, hist, out = DREF[A0], {}, []
    for t in AN[1:]:
        ds = dette - DREF[t-1]
        spread = P["spread_pb_par_pt"] * ds / PIB[t-1] * 100 / 1e4
        hist[t] = spread
        if millesime:  # chaque tranche refinancée en u garde le spread de u
            sp = sum(hist[u] * (part(u - PLF) - part(u - 1 - PLF)) for u in hist)
        else:
            sp = spread * part(t - PLF)
        it = ds * P["taux_oat"] / 100 + sp * DREF[t-1]
        d = -float(REF[t]["solde_pct"]) / 100 * PIB[t] - biais(t) / 100 * PIB[t] + (-imp * PIB[t] / PIB[2027] if t >= 2027 else 0) + it
        dette += d + float(REF[t]["sfa_pct"] or 0) / 100 * PIB[t]
        out.append((t, round(d / PIB[t] * 100, 2), round(dette / PIB[t] * 100, 1), round(it, 1)))
    return out

tot = {r["groupe"]: float(r["central"]) for r in csv.DictReader(open("moteur_totaux.csv", encoding="utf-8"))
       if r["fichier"] == "paniers" and r["composante"] == "solde"}
for nom, imp in [("LFI ajusté (publié)", tot["LFI ajusté"]), ("LFI ajusté + emprunt 30 Md€", tot["LFI ajusté"] - 30),
                 ("Ensemble", tot["Ensemble"]), ("LFI intégral", tot["LFI intégral"])]:
    for m in (False, True):
        r = traj(imp, m)[-1]
        print(f"{nom:<30} spread {'millésime' if m else 'publié  '} : 2032 déficit {r[1]:5.2f} %  dette {r[2]:6.1f} %  intérêts sup {r[3]:6.1f} Md€")
