"""T27 G3.4 : biais des programmes de stabilité mesuré sur la première publication (EFB Forecast Tracker).

Usage (depuis la racine du dépôt) :
    python3 recherche/T27/G3/efb.py [sources/T2b/EFB_Forecast_Tracker.xlsx]

Lit l'onglet Forecast_Data du classeur archivé (France, variable nom_BB_pc_GDP, solde en % du PIB).
Définition EFB (onglet Information) : réalisé de l'année T = estimation du printemps T+1 de la Commission
(millésime « SPR T+1 », horizon T) ; prévision = programme de stabilité (millésimes « SCP »).
Erreur = réalisé − prévision (négatif = programme optimiste).

Règle d'exclusion des crises : celle de la couche 2 (scripts/calc.py, scripts/check_regression.py) :
années cibles 2009 et 2020 à 1 an ; 2009, 2010, 2020 et 2021 à 3 ans.

Trois échantillons :
  A. les millésimes de la couche 2 (data/raw/programmes_stabilite_fr.csv), prévision et réalisé lus dans le classeur :
     seule la mesure du réalisé change (première publication au lieu de la série actuelle d'Eurostat) ;
  A'. idem, mais avec les prévisions de la couche 2 (data/raw/programmes_stabilite_fr.csv) : même échantillon que le
     biais actuel (prévisions recoupées avec l'EFB par T2b § 1.3), seul le réalisé vient du classeur ;
  B. tous les programmes du classeur (calcul de T2b § 1.3), sans la ligne « SCP 2010 » qui ne correspond à aucun
     programme déposé (T2b § 1.3).
"""
import csv
import statistics
import sys
from pathlib import Path

import openpyxl

RACINE = Path(__file__).resolve().parents[3]
XLSX = Path(sys.argv[1]) if len(sys.argv) > 1 else RACINE / "sources/T2b/EFB_Forecast_Tracker.xlsx"
CRISE = {1: {2009, 2020}, 3: {2009, 2010, 2020, 2021}}

wb = openpyxl.load_workbook(XLSX, read_only=True, data_only=True)
lignes = wb["Forecast_Data"].iter_rows(values_only=True)
entete = next(lignes)
i_v, i_h, i_c, i_bb = (entete.index(c) for c in ("Vintage", "Horizon", "Country", "nom_BB_pc_GDP"))
D = {}  # (millésime EFB, année cible) -> solde
for r in lignes:
    if r[i_c] == "FR" and r[i_bb] is not None:
        D[(r[i_v], int(r[i_h]))] = float(r[i_bb])


def realise(t):
    return D.get((f"SPR {t + 1}", t))


def scp(v, t):
    return D.get((f"SCP {v}", t))


def stats(erreurs, h):
    tout = [e for _, t, e in erreurs]
    hc = [e for _, t, e in erreurs if t not in CRISE[h]]
    return {"n_tout": len(tout), "moy_tout": statistics.mean(tout), "n_hc": len(hc), "moy_hc": statistics.mean(hc),
            "med_hc": statistics.median(hc), "part_optimiste_hc": sum(e < 0 for e in hc) / len(hc)}


# A. millésimes de la couche 2 ; millésime EFB = année cible à 1 an − 1, sauf SP 2010-02 = « SCP 2009 » (T2b § 1.3)
with open(RACINE / "data/raw/programmes_stabilite_fr.csv", encoding="utf-8") as fh:
    c2 = list(csv.DictReader(fh))
A = {1: [], 3: []}
A2 = {1: [], 3: []}  # A' : prévision de la couche 2 (CSV), réalisé EFB : même échantillon que le biais actuel
print("A. millésimes de la couche 2 (prévision EFB / réalisé EFB, première publication ; réalisé actuel de la couche 2)")
for r in c2:
    v = 2009 if r["millesime"] == "SP 2010-02" else int(r["annee_t1"]) - 1
    for h in (1, 3):
        t = int(r[f"annee_t{h}"])
        p, re_ = scp(v, t), realise(t)
        print(f"  {r['millesime']:<11} SCP {v} t{h} {t} : prévision EFB {p} (couche 2 {r[f'prev_t{h}']}), "
              f"réalisé EFB {re_} (couche 2 {r[f'real_t{h}'] or '-'})"
              + ("" if p is not None and re_ is not None else "  -> écarté (valeur absente du classeur)"))
        if p is not None and re_ is not None:
            A[h].append((r["millesime"], t, re_ - p))
        if r[f"real_t{h}"] and re_ is not None:
            A2[h].append((r["millesime"], t, re_ - float(r[f"prev_t{h}"])))

# B. tous les programmes du classeur, sauf « SCP 2010 »
B = {1: [], 3: []}
for v in sorted({int(k[0].split()[1]) for k in D if k[0].startswith("SCP ")}):
    if v == 2010:
        continue
    for h in (1, 3):
        p, re_ = scp(v, v + h), realise(v + h)
        if p is not None and re_ is not None:
            B[h].append((f"SCP {v}", v + h, re_ - p))

print()
for nom, ech in (("A (millésimes de la couche 2)", A), ("A' (prévisions de la couche 2, réalisé EFB)", A2),
                 ("B (tous les programmes du classeur, sans SCP 2010)", B)):
    for h in (1, 3):
        s = stats(ech[h], h)
        print(f"{nom:<52} {h} an(s) : toutes années {s['moy_tout']:+.3f} (n = {s['n_tout']}) ; "
              f"hors crises {s['moy_hc']:+.3f} (n = {s['n_hc']}), médiane {s['med_hc']:+.2f}, "
              f"part optimiste {s['part_optimiste_hc']:.0%}")
# Contrôle : calcul de T2b (B avec SCP 2010, années 2009, 2010, 2020, 2021 exclues à 1 an aussi)
t2b = [D[(f"SCP {v}", v + 1)] for v in range(2000, 2024) if (f"SCP {v}", v + 1) in D and realise(v + 1) is not None]
e = [realise(v + 1) - D[(f"SCP {v}", v + 1)] for v in range(2000, 2024)
     if (f"SCP {v}", v + 1) in D and realise(v + 1) is not None and v + 1 not in CRISE[3]]
print(f"\ncontrôle T2b (1 an, SCP 2010 inclus, 2009-2010-2020-2021 exclues) : {statistics.mean(e):+.3f} (n = {len(e)})")
