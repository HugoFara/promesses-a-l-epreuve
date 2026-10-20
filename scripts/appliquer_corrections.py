"""Applique un fichier de corrections (format des agents T2) à data/raw/, avec traçabilité.

Usage (depuis la racine du projet) :  python3 scripts/appliquer_corrections.py recherche/T2b/corrections.csv
Colonnes attendues : fichier,id,colonne,valeur_precedente,valeur_nouvelle,confiance_precedente,confiance_nouvelle,
                     url,citation,page,note

Règles :
- la valeur actuelle doit être égale à valeur_precedente, sinon la ligne est refusée (rien n'est écrasé à l'aveugle) ;
- chaque changement ou confirmation est inscrit dans data/raw/historique.csv (ancienne valeur, nouvelle, raison, source) ;
- si la ligne reste en confiance medium, la note est écrite dans la colonne note_confiance (critère T2).
"""
import csv
import sys
from datetime import date
from pathlib import Path

RAW = Path("data/raw")
CLES = {"programmes_stabilite_fr": "millesime", "regles": "regle"}


def norm(v):
    return (v or "").strip().replace("−", "-")


def main(chemin):
    corr = list(csv.DictReader(open(chemin, encoding="utf-8")))
    fichiers = {}
    hist = []
    refus = []
    for c in corr:
        nom = c["fichier"].removesuffix(".csv")
        if nom not in fichiers:
            rows = list(csv.DictReader(open(RAW / f"{nom}.csv", encoding="utf-8")))
            fichiers[nom] = rows
        rows = fichiers[nom]
        cle = CLES.get(nom, "id")
        ligne = next((r for r in rows if r[cle] == c["id"]), None)
        if ligne is None:
            refus.append(f"{nom} {c['id']} : identifiant introuvable")
            continue
        col = c["colonne"]
        if col not in ligne:
            refus.append(f"{nom} {c['id']} : colonne inconnue {col}")
            continue
        if norm(ligne[col]) != norm(c["valeur_precedente"]) and norm(ligne[col]) != norm(c["valeur_nouvelle"]):
            refus.append(f"{nom} {c['id']}.{col} : valeur actuelle « {ligne[col][:40]} » ≠ précédente « {c['valeur_precedente'][:40]} »")
            continue
        ancienne = ligne[col]
        ligne[col] = c["valeur_nouvelle"]
        if c.get("confiance_nouvelle") and "confiance" in ligne:
            ligne["confiance"] = c["confiance_nouvelle"]
            if c["confiance_nouvelle"] == "medium":
                ligne["note_confiance"] = c["note"]
        source = " ; ".join(x for x in (c["url"], c.get("page"), c.get("citation")) if x)
        nature = "confirmée" if norm(ancienne) == norm(c["valeur_nouvelle"]) else "corrigée"
        hist.append([date.today().isoformat(), nom, c["id"], col, ancienne, c["valeur_nouvelle"],
                     f"Valeur {nature} ({Path(chemin).parent.name}) : {c['note']}", source])
    for nom, rows in fichiers.items():
        cols = list(rows[0])
        if any("note_confiance" in r for r in rows) and "note_confiance" not in cols:
            cols.append("note_confiance")
        with open(RAW / f"{nom}.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, cols, lineterminator="\n", restval="")
            w.writeheader()
            w.writerows(rows)
    with open(RAW / "historique.csv", "a", newline="", encoding="utf-8") as fh:
        csv.writer(fh, lineterminator="\n").writerows(hist)
    print(f"{len(hist)} correction(s) appliquée(s), {len(refus)} refusée(s)")
    for r in refus:
        print("REFUS", r)


if __name__ == "__main__":
    main(sys.argv[1])
