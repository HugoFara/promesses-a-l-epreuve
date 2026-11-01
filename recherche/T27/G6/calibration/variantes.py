# Variantes de erreur_ligne (G6.3). Usage : python3 -I recherche/T27/G6/calibration/variantes.py data/raw/calibration_instituts.csv
# Même filtre et même formule que scripts/validation.py (inclus_stats commençant par « oui », écart = (réalisé − chiffré) / |chiffré|).
import csv, statistics, sys
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
def e(ch, re_): return (re_ - ch) / abs(ch) * 100
def stat(lst): 
    a = [abs(x) for x in lst]; return len(a), round(statistics.median(a), 1)
# même filtre que scripts/validation.py
base = [e(float(r["chiffrage_campagne"]), float(r["cout_realise"])) for r in rows
        if r["inclus_stats"].lower().startswith("oui") and r["cout_realise"] and r["chiffrage_campagne"]]
aspa = round(592 * 3530 / 2780 / 1000, 3)  # 0,752 Md€ (calcul, voir notes.md)
print("ASPA extrapolé", round(aspa, 4))
hs = 1.686 + 3.4 - 0.6
new_1722 = [e(-0.5, -aspa), e(-0.6, -aspa), e(-0.9, -1.1)]
new_1722_rg = [e(-0.5, -0.592), e(-0.6, -0.592), e(-0.9, -1.1)]
new_2012 = [e(4.6, hs), e(4.6, hs), e(-2.0, -1.32)]  # candidat HS, Terra Nova HS, candidat emplois d avenir
# lignes 2012/2007 existantes dont le verdict interne est « oui »
inner = []
for r in rows:
    s = r["inclus_stats"]
    if s.startswith("non (T21") and "; oui" in s and r["cout_realise"]:
        inner.append((r["campagne"], r["mesure"][:30], r["chiffreur"], e(float(r["chiffrage_campagne"]), float(r["cout_realise"]))))
for x in inner: print("interne oui:", x[0], x[1], x[2], round(x[3], 1))
i2012 = [x[3] for x in inner if x[0].endswith("2012")]
i2012_sans_cg = [x[3] for x in inner if x[0].endswith("2012") and "génération" not in x[1]]
i2007 = [x[3] for x in inner if x[0].endswith("2007")]
print("nouveaux écarts 2017/2022:", [round(x, 1) for x in new_1722], "RG seul:", [round(x, 1) for x in new_1722_rg])
print("nouveaux écarts 2012:", [round(x, 1) for x in new_2012], "HS réalisé", round(hs, 3))
V = {
 "V0 actuel": base,
 "V1 + ASPA (extrapolé) + ASF": base + new_1722,
 "V1b + ASPA (RG seul) + ASF": base + new_1722_rg,
 "V1c + ASF seul": base + new_1722[2:],
 "V2 V1 + 2012 (existantes oui + nouvelles)": base + new_1722 + i2012 + new_2012,
 "V2b V2 sans contrat de génération": base + new_1722 + i2012_sans_cg + new_2012,
 "V3 V2 + 2007": base + new_1722 + i2012 + new_2012 + i2007,
 "V4 V0 + 2012 nouvelles seules": base + new_2012,
}
for k, v in V.items(): print(k, stat(v))
