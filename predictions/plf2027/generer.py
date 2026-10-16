"""Registre des prédictions sur les mesures du budget 2027 (T19). Lancé une fois, depuis data/ :

    python3 ../predictions/plf2027/generer.py

Prédiction = chiffrage officiel × facteur central de la règle attribuée à l'aveugle (recherche/T19/attribution_agent.csv),
avec les facteurs de data/ au moment du commit qui publie ce registre. Le registre ne doit plus être régénéré ensuite :
une mise à jour passe par un nouveau fichier daté (voir README.md).
"""
import csv
import sys

sys.path.insert(0, "../scripts")
from validation import facteurs_centraux  # noqa: E402

T19, OUT = "../recherche/T19/", "../predictions/plf2027/"

# Lignes dont le réalisé ne pourra pas être comparé tel quel (recherche/T19/rapport.md, § 4)
TRANSFERTS = {"plf27_art13_onf_frais_garderie", "plf27_art34_dgf", "plf27_art35_fctva", "plf27_art36_tva_collectivites",
              "plf27_art39_accises_regions", "plf27_art77_dotation_feader_regions", "plf27_art84_dilico",
              "plf27_art84_dilico_2028", "plf27_art85_dotation_communes_rurales",
              "plf27_art86_aides_exceptionnelles_departements", "plf27_art87_fonds_soutien_cpeb"}
DOUBLONS = {"plfss27_art6_indemnites_rupture": "part sociale déjà comprise dans plf27_art2_ruptures",
            "plfss27_art6_indemnites_rupture_2028": "part sociale déjà comprise dans plf27_art2_ruptures_2028"}
NON_TESTABLES = {"Recette ponctuelle": "règle au test non concluant : facteur 0 (hors solde durable), pas une prévision du rendement"}


def lire(f):
    with open(f, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


fac = facteurs_centraux()
att = {r["id"]: r for r in lire(T19 + "attribution_agent.csv")}
sortie = []
for m in lire(T19 + "mesures.csv"):
    a = att[m["id"]]
    f = fac[a["regle"]]
    raison = ("transfert entre administrations : effet sur le solde public non chiffré par la source" if m["id"] in TRANSFERTS
              else DOUBLONS.get(m["id"]) or NON_TESTABLES.get(a["regle"], ""))
    sortie.append({"id": m["id"], "texte": m["texte"], "article": m["article"], "mesure": m["mesure"], "sens": m["sens"],
                   "annee": m["annee"], "indicateur": m["indicateur"], "chiffrage_md": m["chiffrage_md"],
                   "regle": a["regle"], "facteur": round(f, 4),
                   "prediction_md": round(float(m["chiffrage_md"]) * f, 4),
                   "comparable": "non" if raison else "oui", "raison_non_comparable": raison,
                   "comportement_inclus": m["comportement_inclus"], "source": m["url"], "page": m["page"]})
with open(OUT + "predictions.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, list(sortie[0]), lineterminator="\n")
    w.writeheader()
    w.writerows(sortie)
n = sum(r["comparable"] == "oui" for r in sortie)
print(f"{len(sortie)} lignes, {n} comparables ; facteur ≠ 1 : {sum(r['comparable'] == 'oui' and r['facteur'] != 1 for r in sortie)}")
