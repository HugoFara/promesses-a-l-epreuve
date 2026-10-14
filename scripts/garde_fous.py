"""Garde-fous automatiques (T8) : symétrie des règles, traçabilité, double compte avec la référence.

Mode strict (STRICT_REFERENCE=1, par défaut une fois T1 intégré) : une ligne sans statut de référence est une erreur.
"""
import csv
import os

STRICT = os.environ.get("STRICT_REFERENCE", "1") == "1"


def rows(f):
    with open(f, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


erreurs, alertes = [], []
regles = {r["regle"]: r for r in rows("regles.csv")}

for nom in ("application_lignes", "paniers"):
    for r in rows(f"{nom}.csv"):
        lid = f"{nom} {r['id']}"
        facteur = float(r["facteur"])
        montant = float(r["independant"] if nom == "application_lignes" else r["statique"])
        regle = regles[r["regle"]]

        # Symétrie : une règle fixe a le même facteur partout, sauf exception justifiée
        if regle["variable"] == "0" and abs(facteur - float(regle["facteur"])) > 1e-9:
            if not r.get("exception_symetrie"):
                erreurs.append(f"SYMÉTRIE {lid} : règle « {r['regle']} » = {regle['facteur']}, ligne = {facteur}")
            else:
                alertes.append(f"exception de symétrie {lid} : {r['exception_symetrie']}")
        if regle["variable"] == "1" and not (r.get("source_reference") or r.get("justification")):
            erreurs.append(f"SYMÉTRIE {lid} : facteur variable sans justification")

        # Taux de recours : seulement si le chiffrage de départ suppose un recours complet (validation du 14/10/2026)
        if r["regle"] == "Taux de recours" and not (r.get("recours_complet_suppose") == "oui" and r.get("source_recours")):
            erreurs.append(f"RECOURS {lid} : règle « Taux de recours » sans preuve que le chiffrage suppose un recours complet")

        # Traçabilité : toute ligne chiffrée a une URL et une confiance
        if montant != 0 and not (r["url"].startswith("http") and r["confiance"]):
            erreurs.append(f"TRAÇABILITÉ {lid} : URL ou confiance manquante")

        # Double compte avec la référence (T1). Référence 2027 = loi votée + budgets 2027 déposés :
        # une mesure « proposée » y est donc incluse, comme une mesure votée.
        statut = r.get("statut_reference") or ""
        f_ref = float(r.get("facteur_reference") or 1)
        total = facteur * f_ref
        if statut in ("votée", "proposée") and total != 0 and f_ref >= 1:
            erreurs.append(f"DOUBLE COMPTE {lid} : mesure {statut} comptée au facteur total {total:g}")
        if statut == "partielle" and f_ref >= 1 and not r.get("note_reference"):
            erreurs.append(f"DOUBLE COMPTE {lid} : mesure partielle sans décote ni explication")
        if statut in ("votée", "proposée", "partielle") and not r.get("source_reference"):
            erreurs.append(f"DOUBLE COMPTE {lid} : statut {statut} sans source")
        if not statut:
            (erreurs if STRICT else alertes).append(f"RÉFÉRENCE {lid} : statut inconnu")

# Audit n° 19 : une ligne « absente » ne devrait pas avoir de montant de référence 2027 non nul (statut_reference_2027.csv)
actuel = {(f, r["id"]): r for f in ("application_lignes", "paniers") for r in rows(f"{f}.csv")}
for r in rows("statut_reference_2027.csv"):
    ligne = actuel.get((r["fichier"], r["id_ligne"]), {})
    deja_traitee = ligne.get("statut_reference") != "absente" or float(ligne.get("facteur_reference") or 1) < 1
    if r["fichier"] == "application_lignes":
        deja_traitee = True  # l'application 2024 est jugée par rapport au PStab 2024, pas à la référence 2027
    if not deja_traitee and r["statut_reference"] == "absente" and r["montant_reference_2027"] not in ("", "0", "0.0"):
        alertes.append(f"RÉFÉRENCE {r['fichier']} {r['id_ligne']} : statut absente mais montant de référence {r['montant_reference_2027']}")
    # Synchronisation : un statut ou un facteur des paniers différent de celui proposé par T1 doit être expliqué
    if r["fichier"] == "paniers" and ligne:
        ecart = (ligne.get("statut_reference") != r["statut_reference"]
                 or abs(float(ligne.get("facteur_reference") or 1) - float(r["facteur_suggere"] or 1)) > 1e-9)
        if ecart and not r.get("raison_ecart"):
            erreurs.append(f"RÉFÉRENCE {r['id_ligne']} : statut ou facteur différent de T1 sans raison_ecart")

for nom, url_cols in (("mesures_cout", ("source_ex_ante", "source_ex_post")), ("elasticites", ("url",)),
                      ("programmes_stabilite_fr", ("source",))):
    for r in rows(f"{nom}.csv"):
        if not all(r[c].startswith("http") for c in url_cols) or not r["confiance"]:
            erreurs.append(f"TRAÇABILITÉ {nom} {r.get('id') or r.get('millesime')} : URL ou confiance manquante")

for a in alertes:
    print("alerte ", a)
for e in erreurs:
    print("ÉCHEC  ", e)
print(f"garde-fous : {len(erreurs)} erreur(s), {len(alertes)} alerte(s)")
raise SystemExit(1 if erreurs else 0)
