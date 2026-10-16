"""T18 : statistique provisoire « avant et après la règle » sur les nouvelles mesures (consigne § 5, point 2).

Même calcul que scripts/validation.py (prévision = chiffrage de départ × facteur central de la règle attribuée à
l'aveugle), sur les fichiers de recherche/T18, sans rien écrire dans data/. Facteurs gelés : état du commit 0b4175f.

Lancer depuis data/ :  python3 ../recherche/T18/stats_provisoires.py
Sortie : recherche/T18/stats_provisoires.csv
"""
import csv
import statistics
import sys

sys.path.insert(0, "../scripts")
from validation import facteurs_centraux  # noqa: E402

T18 = "../recherche/T18/"


def lire(f):
    with open(f, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


fac = facteurs_centraux()
attrib = {(r["fichier"], r["id"]): r for r in lire(T18 + "attribution_agent.csv")}
lignes = []
for r in lire(T18 + "mesures_cout_nouvelles.csv"):
    a = attrib[("mesures_officielles", r["id"])]
    depart = float(r["ex_ante"]) * float(r["deflateur_ex_ante"] or 1)
    lignes.append(dict(source="officiel", id=r["id"], regle=a["regle"], issue_connue=a["issue_connue"], depart=depart,
                       realise=float(r["ex_post_central"]), type_ex_post=r["type_ex_post"],
                       comportement=r["comportement_inclus_ex_ante"], publie_2026=r["realise_publie_le"].startswith("2026"),
                       drapeaux=r["drapeaux"]))
for r in lire(T18 + "mesures_effets_nouvelles.csv"):
    if not r["ratio_central"]:
        continue
    a = attrib[("effets_annonces", r["id"])]
    lignes.append(dict(source="effet annoncé", id=r["id"], regle=a["regle"], issue_connue=a["issue_connue"], depart=1.0,
                       realise=float(r["ratio_central"]), type_ex_post="observe", comportement="",
                       publie_2026=r["realise_publie_le"].startswith("2026"), drapeaux=r["drapeaux"]))

for l in lignes:
    f = fac[l["regle"]]
    prev = l["depart"] * f
    l["facteur"] = round(f, 3)
    l["e0"] = abs(l["realise"] - l["depart"]) / abs(l["depart"]) * 100
    l["e1"] = abs(l["realise"] - prev) / abs(l["depart"]) * 100
    l["verdict"] = ("inchangé" if abs(f - 1) < 1e-9 else "amélioré" if l["e1"] < l["e0"] - 1e-9
                    else "dégradé" if l["e1"] > l["e0"] + 1e-9 else "inchangé")


def resume(nom, sel):
    sel = [l for l in sel if abs(l["facteur"] - 1) > 1e-9]  # seules les lignes où la règle change le chiffre testent
    if not sel:
        return {"groupe": nom, "n": 0}
    return {"groupe": nom, "n": len(sel),
            "erreur_mediane_depart_pct": round(statistics.median(l["e0"] for l in sel), 1),
            "erreur_mediane_regle_pct": round(statistics.median(l["e1"] for l in sel), 1),
            "ameliores": sum(l["verdict"] == "amélioré" for l in sel),
            "degrades": sum(l["verdict"] == "dégradé" for l in sel)}


obs = [l for l in lignes if l["type_ex_post"] == "observe"]
groupes = [("Tout, réalisés observés (facteur ≠ 1)", obs),
           ("Tout, convention de validation.py (administratif exclu seulement)", [l for l in lignes if l["type_ex_post"] != "administratif"]),
           ("  observés, issue inconnue de l'agent", [l for l in obs if l["issue_connue"] == "non"]),
           ("  observés, issue connue de l'agent", [l for l in obs if l["issue_connue"] == "oui"]),
           ("  observés, réalisé publié en 2026", [l for l in obs if l["publie_2026"]]),
           ("  observés, comportement inclus ex ante = oui", [l for l in obs if l["comportement"] == "oui"]),
           ("  observés, comportement inclus ex ante = non", [l for l in obs if l["comportement"] == "non"]),
           ("  observés, sans drapeau low", [l for l in obs if "low" not in l["drapeaux"]])]
for regle in sorted({l["regle"] for l in lignes} - {"Aucune"}):
    groupes.append((f"Règle : {regle}", [l for l in obs if l["regle"] == regle]))
    groupes.append((f"  dont issue inconnue", [l for l in obs if l["regle"] == regle and l["issue_connue"] == "non"]))

out = [resume(n, s) for n, s in groupes]
champs = ["groupe", "n", "erreur_mediane_depart_pct", "erreur_mediane_regle_pct", "ameliores", "degrades"]
with open(T18 + "stats_provisoires.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, champs, lineterminator="\n")
    w.writeheader()
    w.writerows(out)
with open(T18 + "stats_provisoires_mesures.csv", "w", newline="", encoding="utf-8") as fh:
    ch = ["source", "id", "regle", "facteur", "issue_connue", "type_ex_post", "depart", "realise", "e0", "e1", "verdict", "drapeaux"]
    w = csv.DictWriter(fh, ch, extrasaction="ignore", lineterminator="\n")
    w.writeheader()
    w.writerows({**l, "e0": round(l["e0"], 1), "e1": round(l["e1"], 1)} for l in lignes)
for o in out:
    print(o)
