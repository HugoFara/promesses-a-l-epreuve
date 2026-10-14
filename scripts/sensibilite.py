"""Sensibilité au chiffreur de départ (T6).

Pour chaque programme et chaque chiffreur, deux lectures :
  - « propre » : les seules lignes chiffrées par l'institut (plus ses postes hors lignes) ; reproduit son solde publié ;
  - « complété » : les lignes qu'il ne chiffre pas sont remplies par la médiane des autres chiffreurs indépendants.
Chaque ligne reçoit le facteur de sa règle (application_lignes.csv), quel que soit le chiffreur : la correction
ne dépend que de la nature de la mesure.

Exclus du point de départ : chiffrages partisans ; composantes partielles (OFCE).
Asterès reprend les recettes du parti : il figure comme scénario « recettes du parti », pas comme chiffreur indépendant.
Sortie : data/sensibilite_chiffreurs.csv.
"""
import csv
import statistics


def lire(f):
    with open(f, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


lignes = {r["id"]: r for r in lire("application_lignes.csv")}
facteur = {k: float(r["facteur"]) for k, r in lignes.items()}
ch = [r for r in lire("chiffrages_instituts.csv") if r["usage"] not in ("partisan", "composante")]
publies = {(r["programme"], r["chiffreur"]): r["solde_total"] for r in lire("totaux_instituts.csv")}
INDEPENDANTS = {"ligne", "hors_lignes"}

out = []
for prog in dict.fromkeys(r["programme"] for r in lignes.values()):
    ids = [k for k, r in lignes.items() if r["programme"] == prog]
    val = {}  # (chiffreur, id) -> valeur
    for r in ch:
        if r["programme"] == prog:
            val[(r["chiffreur"], r["id_ligne"])] = (float(r["valeur"]), r["usage"])
    chiffreurs = sorted({c for c, _ in val})
    for c in chiffreurs:
        propre_s = propre_c = 0.0
        compl_s = compl_c = 0.0
        n_propres = 0
        for k, (v, usage) in ((k, x) for (cc, k), x in val.items() if cc == c):
            f = facteur.get(k, 1.0)  # postes hors lignes : facteur 1 (règle « Aucune »)
            propre_s += v
            propre_c += v * f
            compl_s += v
            compl_c += v * f
            n_propres += k in ids
        for k in ids:
            if (c, k) in val:
                continue
            autres = [v for (cc, kk), (v, u) in val.items() if kk == k and cc != c and u in INDEPENDANTS]
            if k.endswith("_taux"):
                autres = [float(lignes[k]["independant"])]  # charge d'intérêts : calcul propre au projet
            if autres:
                m = statistics.median(autres)
                compl_s += m
                compl_c += m * facteur[k]
        statut = "indépendant" if any(u in INDEPENDANTS for (cc, _), (_, u) in val.items() if cc == c) else ""
        if any(u == "recettes_du_parti" for (cc, _), (_, u) in val.items() if cc == c):
            statut = "recettes du parti"
        # Solde publié : premier total de l'institut (Asterès en a deux : on prend la note ligne à ligne)
        pub = next((v for (p, cc), v in publies.items() if p == prog and c.split(" ")[0] in cc), "")
        out.append({"programme": prog, "chiffreur": c, "statut": statut, "lignes_chiffrees": n_propres,
                    "lignes_programme": len(ids), "solde_publie": pub,
                    "propre_statique": round(propre_s, 1), "propre_corrige": round(propre_c, 1),
                    "complete_statique": round(compl_s, 1), "complete_corrige": round(compl_c, 1)})

# Dispersion entre chiffreurs indépendants, avant et après correction (lecture « complété »)
resume = []
for prog in dict.fromkeys(o["programme"] for o in out):
    ind = [o for o in out if o["programme"] == prog and o["statut"] == "indépendant"]
    if len(ind) >= 2:
        e_s = max(o["complete_statique"] for o in ind) - min(o["complete_statique"] for o in ind)
        e_c = max(o["complete_corrige"] for o in ind) - min(o["complete_corrige"] for o in ind)
        resume.append((prog, len(ind), e_s, e_c))

with open("sensibilite_chiffreurs.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, list(out[0]), lineterminator="\n")
    w.writeheader()
    w.writerows(out)
for o in out:
    print(f"{o['programme']:<15} {o['chiffreur']:<23} {o['statut']:<18} {o['lignes_chiffrees']:>2}/{o['lignes_programme']}"
          f"  publié {o['solde_publie']:>6}  propre {o['propre_statique']:>7} → {o['propre_corrige']:>7}"
          f"  complété {o['complete_statique']:>7} → {o['complete_corrige']:>7}")
for prog, n, e_s, e_c in resume:
    print(f"{prog} : écart entre {n} chiffreurs indépendants {e_s:.1f} Md€ avant correction, {e_c:.1f} après "
          f"({(1 - e_c / e_s) * 100 if e_s else 0:.0f} % de réduction)")
