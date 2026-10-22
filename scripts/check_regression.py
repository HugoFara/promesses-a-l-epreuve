"""Valeurs de référence au 12/10/2026, mises à jour le 14/10/2026 ; mesures de T18 (selection = test_regles) exclues de la couche 1 le 16/10/2026 (voir data/raw/historique.csv). Toute modification volontaire des données doit mettre à jour ce fichier."""
import csv, statistics
def rows(f): return list(csv.DictReader(open(f, encoding="utf-8")))
ok = True
def check(name, got, exp, tol=0.05):
    global ok
    good = abs(got - exp) <= tol
    ok &= good
    print(f"{'OK ' if good else 'ÉCHEC'} {name}: {got:.2f} (attendu {exp})")

# Couche 1
c = [r for r in rows("mesures_cout.csv") if r["inclus_stats"] == "1" and r["selection"] == "generale"]  # T18 hors couche 1
def ecart(r):
    a = float(r["ex_ante"]) * float(r["deflateur_ex_ante"])
    return ((a - float(r["ex_post_central"])) if r["sens"] == "cout" else (float(r["ex_post_central"]) - a)) / a * 100
err = [ecart(r) for r in c]
check("C1 erreur absolue médiane (%)", statistics.median(abs(e) for e in err), 11.2)
check("C1 nombre de mesures (statistique principale)", len(c), 26, 0)
check("C1 mesures à ±15 %", sum(abs(e) <= 15 for e in err), 16)
# Couche 2
p = rows("programmes_stabilite_fr.csv")
e1 = [float(r["real_t1"]) - float(r["prev_t1"]) for r in p if int(r["annee_t1"]) not in (2009, 2020)]
e3 = [float(r["real_t3"]) - float(r["prev_t3"]) for r in p if r["real_t3"] and int(r["annee_t3"]) not in (2009, 2010, 2020, 2021)]
check("C2 erreur moyenne t+1 hors crises (pt PIB)", statistics.mean(e1), -0.60)
check("C2 erreur moyenne t+3 hors crises (pt PIB)", statistics.mean(e3), -1.93)
check("C2 n t+3 hors crises", len(e3), 15)
# Couche 3
check("C3 nb estimations", len(rows("elasticites.csv")), 140)  # 78 + 36 répercussions (T20) + 26 tests de paramètres (T21), 20/10/2026
# Application 2024
a = rows("application_lignes.csv")
# Lignes dont le moteur calcule le montant (statique conventionnel −1) : hors total « indépendant »
calc = {r["regle"] for r in rows("moteur_regles.csv") if r["formule"] in ("emploi_smic", "montant")}
# Spread 3 → 2,5 pb par point de dette (T21, 20/10/2026) : lignes nfp_taux, ens_taux, rn24_taux
# Lignes « Autres » découpées (T22, 20/10/2026) : indépendant inchangé ; RN corrigé −60,0 → −59,0 (IR des jeunes, transmissions,
# héritage : élasticités) ; NFP inchangé à 0,1 près (taxe Macron, taxe kilométrique, effet emploi du SMIC se compensent)
# Référence de juin 2024 (T24, 22/10/2026) : nfp_asile (article censuré) et rn24_chomage (réforme non prise) à 0, ens_chomage
# compté : NFP −158,9 → −157,6, Ensemble −25,3 → −20,7, RN −59,0 → −54,5
for prog, exp_i, exp_c in [("NFP 2024 (LFI)", -149.9, -157.6), ("Ensemble 2024", -18.0, -20.7), ("RN 2024", -63.6, -54.5)]:
    l = [r for r in a if r["programme"] == prog]
    check(f"App {prog} indépendant", sum(float(r["independant"]) for r in l if r["regle"] not in calc), exp_i, 0.1)
    check(f"App {prog} corrigé", sum(float(r["independant"]) * float(r["facteur"]) * float(r["facteur_reference"]) for r in l), exp_c, 0.1)
# Paniers
k = rows("paniers.csv")
# Effet emploi du SMIC 1,67 → 0,47 (eps_smic −0,17, T21, 20/10/2026)
for v, em, ef in [("LFI intégral", -110.0, 38.9), ("Ensemble", -14.7, 7.5)]:
    l = [r for r in k if r["variante"] == v]
    s = lambda role: sum(float(r["statique"]) * float(r["facteur"]) * float(r["facteur_reference"]) * float(r["facteur_interaction"] or 1) for r in l if r["role"].startswith(role))
    check(f"Panier {v} mesures", s("Mesure"), em, 0.1)
    check(f"Panier {v} financement", s("Financement"), ef, 0.1)
raise SystemExit(0 if ok else 1)
