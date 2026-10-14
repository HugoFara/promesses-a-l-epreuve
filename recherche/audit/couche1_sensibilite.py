"""Audit : sensibilité de l'erreur absolue médiane (couche 1) aux exclusions. Lecture seule de data/mesures_cout_calc.csv."""
import csv, statistics, sys
base = sys.argv[1] if len(sys.argv) > 1 else "data/mesures_cout_calc.csv"
rows = {r["id"]: abs(float(r["ecart_pct"])) for r in csv.DictReader(open(base, encoding="utf-8"))}
energie = {"bouclier_elec", "bouclier_gaz_2023", "cheque_energie_exc_2021", "cheque_energie_exc_2022", "cheque_fioul_2022"}
admin = {"is_25", "th_20", "ip_2021", "hs_ir_2019", "pacte_2015"}  # « ex post » = chiffrage administratif à comportement constant
def stat(nom, ids):
    v = [rows[i] for i in ids]
    print(f"{nom:<45} n={len(v):>2}  médiane={statistics.median(v):5.1f} %  à ±15 % : {sum(x<=15 for x in v)}/{len(v)}")
tous = set(rows)
stat("25 mesures", tous)
stat("hors énergie (prix exogènes)", tous - energie)
stat("hors ex post administratifs", tous - admin)
stat("hors énergie et administratifs", tous - energie - admin)
# retraites 2023 à prix constants (ex ante 13,5 € courants 2030 → € 2024, déflateur ≈1,75 %/an)
r23 = 13.5 / 1.0175**6
print(f"retraites_2023 à prix 2024 : ex ante ≈{r23:.1f} ; écart {(10 - r23) / r23 * 100:.0f} % (au lieu de −26 %)")
w = 20.2 * 1.08
print(f"woerth_2010 en € 2016 : ex ante ≈{w:.1f} ; écart {(18.8 - w) / w * 100:.0f} % (au lieu de −7 %)")
print("facteur_reforme recalculé (valeurs actuelles) : bas", round(10 / 13.5, 3), "haut", round(18.8 / 20.2, 3),
      "moyenne", round((10 / 13.5 + 18.8 / 20.2) / 2, 3), "; à prix constants :", round(10 / r23, 3), round(18.8 / w, 3))
