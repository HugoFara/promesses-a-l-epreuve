"""Vérifie l'archive locale des sources (sources/, non versionnée) contre les index versionnés recherche/*/sources.csv.

Usage (depuis la racine) : python3 scripts/verifier_sources.py
Pour chaque document indexé : présent et intact (sha256 identique), modifié, ou absent. Un document absent peut être
retéléchargé depuis l'URL de l'index ; un document lu dans le navigateur a pour trace une fiche d'extraits.
"""
import csv
import hashlib
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

intacts, modifies, absents = 0, [], []
for index in sorted(RACINE.glob("recherche/*/sources.csv")):
    with open(index, encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            fichier = (r.get("fichier") or "").strip()
            attendu = (r.get("sha256") or "").strip()
            if not fichier or not attendu:
                continue
            p = RACINE / fichier if fichier.startswith("sources/") else index.parent.parent.parent / "sources" / index.parent.name / fichier
            if not p.exists():
                absents.append((fichier, r.get("url", "")))
            elif hashlib.sha256(p.read_bytes()).hexdigest() != attendu:
                modifies.append(fichier)
            else:
                intacts += 1
print(f"{intacts} intact(s), {len(modifies)} modifié(s), {len(absents)} absent(s)")
for f in modifies:
    print("MODIFIÉ ", f)
for f, u in absents:
    print("ABSENT  ", f, u)
