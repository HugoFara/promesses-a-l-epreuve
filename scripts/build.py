"""Valide les CSV sources de data/raw/ et écrit les CSV publiés dans data/.

Les fichiers de data/raw/ sont la seule source de vérité. Ceux de data/ sont régénérés à chaque exécution :
ne pas les éditer à la main.
"""
import csv
import datetime
import subprocess
import sys
from pathlib import Path

from pydantic import ValidationError

from schemas import SCHEMAS

RAW = Path("raw")
# variantes vide : mesure sourcée gardée hors scénario (non publiée), par exemple les mesures de l'ancien « LFI ajusté »
VARIANTE_SUFFIXE = {"LFI intégral": "i", "Ensemble": "e"}


def lire(nom):
    with open(RAW / f"{nom}.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ecrire(nom, rows, cols):
    with open(f"{nom}.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, cols, extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


erreurs = []
donnees = {}
for nom, schema in SCHEMAS.items():
    rows = lire(nom)
    cle = next(iter(schema.model_fields))
    vus = set()
    for i, r in enumerate(rows, start=2):
        try:
            schema.model_validate(r)
        except ValidationError as e:
            for err in e.errors():
                erreurs.append(f"{nom}.csv l.{i} ({r.get(cle)}) {'.'.join(map(str, err['loc']))} : {err['msg']}")
        if nom not in ("historique", "chiffrages_instituts", "totaux_instituts", "statut_reference_2027", "ifrap_nfp_2024", "calibration_instituts", "variantes_sensibilite", "validation_attribution", "montee_en_charge", "idees_chiffres", "non_chiffre_foyer"):
            if r[cle] in vus:
                erreurs.append(f"{nom}.csv : clé en double {r[cle]}")
            vus.add(r[cle])
    donnees[nom] = rows

# Références croisées
ids_idees = {r["id"] for r in donnees["idees"]}
for r in donnees["idees_chiffres"]:
    if r["idee"] not in ids_idees:
        erreurs.append(f"idees_chiffres : idée inconnue {r['idee']}")
    if r["ligne_moteur"]:
        f, _, lid = r["ligne_moteur"].partition("/")
        # les paniers publiés déclinent chaque ligne par variante (l_isf → l_isf_i ; e_oper → e_oper_e)
        brut = lid.rsplit("_", 1)[0] if f == "paniers" else lid
        if f not in ("paniers", "application_lignes") or brut not in {x["id"] for x in donnees[f]}:
            erreurs.append(f"idees_chiffres {r['idee']} : ligne du moteur inconnue {r['ligne_moteur']}")
for i in ids_idees - {r["idee"] for r in donnees["idees_chiffres"] if r["principal"] == "oui"}:
    erreurs.append(f"idees {i} : aucun chiffre principal")
ids_elast = {r["id"] for r in donnees["elasticites"]}
ids_backtest = {r["id"] for r in donnees["mesures_cout"]} | {r["id"] for r in donnees["mesures_effets"]} | {"calibration_instituts", "mesures_cout"}
for r in donnees["hypotheses_defaut"]:
    for x in r["references"].split():
        if x not in ids_elast:
            erreurs.append(f"hypotheses_defaut {r['id']} : référence inconnue {x}")
regles = {r["regle"]: r for r in donnees["regles"]}
for r in donnees["regles"]:
    for x in (r["references"] or "").split():
        if x not in ids_elast | ids_backtest:
            erreurs.append(f"regles « {r['regle']} » : référence inconnue {x}")
familles = {r["famille"] for r in donnees["familles"]}
for r in donnees["familles"]:
    if r["regle"] not in regles:
        erreurs.append(f"familles {r['famille']} : règle absente de regles.csv « {r['regle']} »")
for nom in ("application_lignes", "paniers"):
    for r in donnees[nom]:
        if r["regle"] not in regles:
            erreurs.append(f"{nom} {r['id']} : règle absente de regles.csv « {r['regle']} »")
        if r["famille"] and r["famille"] not in familles:
            erreurs.append(f"{nom} {r['id']} : famille absente de familles.csv « {r['famille']} »")
ids_param = {r["id"] for r in donnees["application_parametres"]}
progs = {r["programme"] for r in donnees["application_programmes"]}
for r in donnees["application_programmes"]:
    for c in ("deficit_reference", "biais_reference"):
        if r[c] not in ids_param:
            erreurs.append(f"application_programmes {r['id']} : {c} inconnu de application_parametres « {r[c]} »")
for x in progs ^ {r["programme"] for r in donnees["application_lignes"]}:
    erreurs.append(f"programme « {x} » présent dans un seul des fichiers application_programmes / application_lignes")
ids_app = {r["id"] for r in donnees["application_lignes"]}
for r in donnees["chiffrages_instituts"]:
    if r["usage"] != "hors_lignes" and r["id_ligne"] not in ids_app:
        erreurs.append(f"chiffrages_instituts : ligne inconnue {r['id_ligne']} ({r['chiffreur']})")
for r in donnees["validation_attribution"]:
    if r["regle"] not in regles:
        erreurs.append(f"validation_attribution {r['id']} : règle inconnue « {r['regle']} »")
mregles = {r["regle"] for r in donnees["moteur_regles"]}
for x in set(regles) ^ mregles:
    erreurs.append(f"règle « {x} » présente dans un seul des fichiers regles.csv / moteur_regles.csv")
ids_bareme = {r["id"] for r in donnees["parametres_bareme"]}
for r in donnees["moteur_parametres"]:
    if r["source_type"] in ("elasticite", "backtest", "bareme", "calcul"):
        for x in (r["source_ref"] or "").split():
            if x not in ids_elast | ids_backtest | ids_bareme:
                erreurs.append(f"moteur_parametres {r['id']} : référence inconnue {x}")
    elif r["source_type"] == "url" and not (r["source_ref"] or "").startswith("http"):
        erreurs.append(f"moteur_parametres {r['id']} : URL manquante")
porteurs = {r["porteur"] for r in donnees["distributif_reformes"]}
for r in donnees["non_chiffre_foyer"]:
    if r["porteur"] not in porteurs:
        erreurs.append(f"non_chiffre_foyer : porteur sans mesure simulée « {r['porteur']} » (distributif_reformes.csv)")
postes_conso = {r["poste"] for r in donnees["consommation_menages"] if r["decoupage"] == "decile_niveau_vie"}
for r in donnees["non_chiffre_foyer"]:
    for p in filter(None, (r["postes"] or "").split(";")):
        if p not in postes_conso:
            erreurs.append(f"non_chiffre_foyer : poste inconnu {p} ({r['mesure']}, consommation_menages.csv)")
ids_paniers = {r["id"] for r in donnees["paniers"]}
for r in donnees["montee_en_charge"]:
    if r["id"] not in ids_paniers | ids_app:
        erreurs.append(f"montee_en_charge : ligne inconnue {r['id']} (ni panier ni ligne de programme)")
for r in donnees["paniers"]:
    for v in filter(None, r["variantes"].split(";")):
        if v not in VARIANTE_SUFFIXE:
            erreurs.append(f"paniers {r['id']} : variante inconnue « {v} »")

if erreurs:
    print("\n".join(erreurs), file=sys.stderr)
    sys.exit(f"{len(erreurs)} erreur(s) de validation dans data/raw/")

# Publication : copie à l'identique, sauf paniers (une ligne par variante) ; historique publié pour le journal
# des corrections du site, du plus récent au plus ancien
for nom, rows in donnees.items():
    if nom == "historique":
        ecrire(nom, sorted(rows, key=lambda r: r["date"], reverse=True), list(rows[0]))
    if nom in ("paniers", "historique"):
        continue
    ecrire(nom, rows, list(rows[0]))
paniers = []
for r in donnees["paniers"]:
    for v in filter(None, r["variantes"].split(";")):
        paniers.append({**r, "id": f"{r['id']}_{VARIANTE_SUFFIXE[v]}", "variante": v})
cols = ["id", "variante"] + [c for c in donnees["paniers"][0] if c not in ("id", "variantes")]
ecrire("paniers", paniers, cols)


def date_des_donnees():
    """Date de la dernière modification de data/raw/ : aujourd'hui si des fichiers ne sont pas encore commités,
    sinon la date du dernier commit qui les touche (hors dépôt git : aujourd'hui)."""
    try:
        sale = subprocess.run(["git", "status", "--porcelain", "--", "raw"], capture_output=True, text=True, check=True).stdout.strip()
        if not sale:
            d = subprocess.run(["git", "log", "-1", "--format=%cs", "--", "raw"], capture_output=True, text=True, check=True).stdout.strip()
            if d:
                return d
    except (OSError, subprocess.CalledProcessError):
        pass
    return datetime.date.today().isoformat()


# Métadonnées lues par le site (date affichée en pied de page)
ecrire("meta", [{"cle": "date_donnees", "valeur": date_des_donnees()}], ["cle", "valeur"])
print(f"build : {len(SCHEMAS)} fichiers validés, {sum(map(len, donnees.values()))} lignes")
