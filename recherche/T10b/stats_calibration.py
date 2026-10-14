"""Biais des chiffreurs : statistiques par institut à partir de calibration_instituts.csv.

Convention : les montants sont des impacts sur le solde public (Md€/an, négatif = dégrade
le solde). ecart_pct = (réalisé - chiffré) / |chiffré| * 100. Un écart négatif signifie
que la mesure a coûté plus (ou rapporté moins) que prévu : le chiffrage était trop optimiste
pour le solde.

Seules les lignes dont inclus_stats == "oui" entrent dans les statistiques.
IC à 95 % : t de Student (moyenne) et bootstrap percentile (10 000 tirages, graine fixe).
Usage : python3 -I stats_calibration.py [chemin_csv]
"""
import csv
import math
import random
import statistics
import sys
from pathlib import Path

CSV = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("calibration_instituts.csv")

# Quantiles bilatéraux à 97,5 % de la loi de Student, ddl 1 à 30.
T975 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306,
        9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145, 15: 2.131,
        16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086, 25: 2.060, 30: 2.042}


def t975(df):
    if df in T975:
        return T975[df]
    keys = sorted(k for k in T975 if k <= df)
    return T975[keys[-1]] if keys else float("nan")


def boot_ci(x, n_boot=10000, seed=20261014):
    rng = random.Random(seed)
    n = len(x)
    means = sorted(statistics.fmean(rng.choices(x, k=n)) for _ in range(n_boot))
    return means[int(0.025 * n_boot)], means[int(0.975 * n_boot) - 1]


def summarize(label, x):
    n = len(x)
    if n == 0:
        return None
    mean = statistics.fmean(x)
    med = statistics.median(x)
    mae = statistics.median([abs(v) for v in x])
    if n >= 2:
        sd = statistics.stdev(x)
        half = t975(n - 1) * sd / math.sqrt(n)
        t_lo, t_hi = mean - half, mean + half
        b_lo, b_hi = boot_ci(x)
    else:
        sd = t_lo = t_hi = b_lo = b_hi = float("nan")
    if n < 3:
        verdict = "n trop petit : aucune conclusion"
    elif t_lo > 0 or t_hi < 0:
        verdict = "biais significatif à 5 % (fragile vu n)" if n < 10 else "biais significatif à 5 %"
    else:
        verdict = "biais non significatif (IC contient 0)"
    return dict(label=label, n=n, mean=mean, median=med, mae=mae, sd=sd,
                t_lo=t_lo, t_hi=t_hi, b_lo=b_lo, b_hi=b_hi, verdict=verdict)


def fmt(v):
    return "n.d." if v != v else f"{v:+.1f}"


def table(rows, title):
    print(f"\n### {title}\n")
    print("| Chiffreur | n | Biais moyen (%) | Médiane (%) | Écart-type (pts) | IC 95 % t | IC 95 % bootstrap | Erreur abs. médiane (%) | Lecture |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        if r is None:
            continue
        sd = "n.d." if r["sd"] != r["sd"] else f"{r['sd']:.1f}"
        print(f"| {r['label']} | {r['n']} | {fmt(r['mean'])} | {fmt(r['median'])} | {sd} | "
              f"[{fmt(r['t_lo'])} ; {fmt(r['t_hi'])}] | [{fmt(r['b_lo'])} ; {fmt(r['b_hi'])}] | "
              f"{r['mae']:.1f} | {r['verdict']} |")


def main():
    with open(CSV, encoding="utf-8") as f:
        data = [r for r in csv.DictReader(f)]
    inc = [r for r in data if r["inclus_stats"].strip() == "oui" and r["ecart_pct"] != ""]
    print(f"Lignes du CSV : {len(data)} ; lignes retenues pour les statistiques : {len(inc)}")

    by = {}
    for r in inc:
        by.setdefault(r["chiffreur"], []).append(float(r["ecart_pct"]))
    order = sorted(by, key=lambda k: (-len(by[k]), k))
    table([summarize(k, by[k]) for k in order] +
          [summarize("Tous chiffreurs (lignes non indépendantes)", [v for k in order for v in by[k]])],
          "Écart (réalisé − chiffré) / |chiffré|, toutes lignes retenues")

    # Sensibilité 1 : écarts plafonnés à ±100 % (limite l'effet des petites mesures).
    cap = {k: [max(-100.0, min(100.0, v)) for v in by[k]] for k in by}
    table([summarize(k, cap[k]) for k in order], "Sensibilité : écarts plafonnés à ±100 %")

    # Sensibilité 2 : Montaigne sans les mesures où le chiffrage repose sur une hypothèse de volume
    # du candidat (emplois francs) ou sur un réalisé dérivé fragile (fonction publique).
    m = [float(r["ecart_pct"]) for r in inc if r["chiffreur"] == "Institut Montaigne"
         and not r["mesure"].startswith(("Emplois francs", "Suppression de 50 000"))]
    table([summarize("Institut Montaigne, hors emplois francs et fonction publique", m)],
          "Sensibilité : Montaigne, mesures fiscales et prestations seulement")

    # Sensibilité 3 : uniquement les lignes de confiance high ou medium.
    hm = {}
    for r in inc:
        if r["confiance"] in ("high", "medium"):
            hm.setdefault(r["chiffreur"], []).append(float(r["ecart_pct"]))
    table([summarize(k, hm[k]) for k in sorted(hm, key=lambda k: (-len(hm[k]), k))],
          "Sensibilité : lignes de confiance high ou medium seulement")

    # Mesures communes à plusieurs chiffreurs (comparaison appariée).
    print("\n### Mesures chiffrées par plusieurs chiffreurs (écart en %)\n")
    mes = {}
    for r in inc:
        mes.setdefault(r["mesure"], {})[r["chiffreur"]] = float(r["ecart_pct"])
    chiffreurs = order
    print("| Mesure | " + " | ".join(chiffreurs) + " |")
    print("|---|" + "---|" * len(chiffreurs))
    for k, d in mes.items():
        if len(d) >= 2:
            print(f"| {k} | " + " | ".join(fmt(d[c]) if c in d else "" for c in chiffreurs) + " |")


if __name__ == "__main__":
    main()
