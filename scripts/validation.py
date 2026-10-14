"""Validation de la méthode (indicateur de confiance) : notre chiffrage corrigé est-il plus proche du réalisé que
le chiffrage de départ ?

Pour chaque mesure passée : chiffrage de départ (officiel ou d'institut) × facteur de la règle = notre prévision,
comparée au réalisé. La règle de chaque mesure a été attribuée À L'AVEUGLE par un agent qui ne voyait ni le réalisé
ni la cause de l'écart (data/raw/validation_attribution.csv ; protocole : recherche/validation/).

Circularité : les facteurs calibrés sur des mesures du backtest (facteur_reforme, ratio_effet_promis) sont
recalculés sans la mesure testée (« leave-one-out ») avec la même règle de construction. Les autres facteurs viennent
d'élasticités publiées ou de barèmes : ces mesures sont hors échantillon de calibration.

Entrées (data/) : validation_attribution.csv, mesures_cout.csv, mesures_effets.csv, calibration_instituts.csv,
                  moteur_regles.csv, moteur_parametres.csv, regles.csv.
Sorties (data/) : validation_mesures.csv (une ligne par mesure), validation_resume.csv,
                  validation_regles.csv (statut de chaque règle), confiance_programmes.csv (part des corrections de
                  chaque programme qui repose sur une règle confirmée, contredite, non concluante ou non testée).
"""
import csv
import statistics

from moteur import FORMULES, lire, noms_parametres, num

# Règles dont le « réalisé » n'est pas une observation : un chiffrage administratif à comportement constant ne peut
# ni confirmer ni contredire une règle de comportement (IS : mesures_cout.type_ex_post = administratif ; chiffrages
# d'instituts : réalisé = chiffrage officiel de la mesure votée, recherche/T10b/rapport.md).
NON_CONCLUANTES = {"Élasticité IS": "réalisés = chiffrages administratifs à comportement constant (is_25 ; T10b)"}

# Mesures du backtest qui ont servi à calibrer un paramètre, et valeur du paramètre recalculée sans elles.
# facteur_reforme = moyenne des ratios à prix constants (retraites 2023 : 0,822 ; Woerth 2010 : 0,862)
# ratio_effet_promis = mode = seul effet promis non nul de l'échantillon de calibration (CICE 0,29) ; sans le CICE : 0
CALIBRATION = {
    "retraites_2023": ("Réforme structurelle", 0.862),
    "woerth_2010": ("Réforme structurelle", 0.822),
    "cice_emploi": ("Effet promis", 0.0),
    "tepa_heures": ("Effet promis", 0.29),
    "isf_invest": ("Effet promis", 0.29),
    "pfu_invest": ("Effet promis", 0.29),
    "cice_emploi_ofce": ("Effet promis", 0.29),
}


def facteurs_centraux():
    """Facteur central de chaque règle : formule du moteur si ses paramètres existent, sinon forfait."""
    params = {r["id"]: num(r["val_central"]) for r in lire("moteur_parametres.csv")}
    forfaits = {r["regle"]: num(r["facteur"]) for r in lire("regles.csv")}
    out = {}
    for r in lire("moteur_regles.csv"):
        if r["formule"] in ("ligne", "montant"):
            continue
        noms = noms_parametres(r)
        if all(v in params for v in noms.values()):
            out[r["regle"]] = float(FORMULES[r["formule"]]({k: params[v] for k, v in noms.items()}))
        else:
            out[r["regle"]] = forfaits[r["regle"]]
    return out


def main():
    f = facteurs_centraux()
    attrib = {(r["fichier"], r["id"]): r for r in lire("validation_attribution.csv")}
    lignes = []

    def ajouter(source, idm, libelle, depart, realise, regle, issue_connue, base=None):
        base = abs(depart) if base is None else base
        fac = f[regle]
        echantillon = "test"
        if idm in CALIBRATION:
            regle_cal, fac_loo = CALIBRATION[idm]
            if regle_cal == regle:
                fac, echantillon = fac_loo, "calibration (leave-one-out)"
        prev = depart * fac
        e_dep, e_nous = (realise - depart) / base, (realise - prev) / base
        verdict = "inchangé" if abs(fac - 1) < 1e-9 else ("amélioré" if abs(e_nous) < abs(e_dep) - 1e-9 else
                                                          "dégradé" if abs(e_nous) > abs(e_dep) + 1e-9 else "inchangé")
        lignes.append({"source": source, "id": idm, "mesure": libelle, "regle": regle, "facteur": round(fac, 3),
                       "echantillon": echantillon, "issue_connue": issue_connue, "depart": depart,
                       "prevision": round(prev, 3), "realise": realise,
                       "erreur_depart_pct": round(e_dep * 100, 1), "erreur_nous_pct": round(e_nous * 100, 1),
                       "verdict": verdict})

    # 1. Chiffrages officiels (couche 1), à base de prix comparable
    for r in lire("mesures_cout.csv"):
        a = attrib[("mesures_officielles", r["id"])]
        depart = float(r["ex_ante"]) * float(r["deflateur_ex_ante"])
        source = "officiel" if r["inclus_stats"] == "1" else "officiel (hors statistique principale)"
        ajouter(source, r["id"], r["mesure"], depart, float(r["ex_post_central"]), a["regle"], a["issue_connue"])
    # 2. Effets promis : départ = 1 (l'annonce), réalisé = ratio réalisé / annoncé
    for r in lire("mesures_effets.csv"):
        if not r["ratio_central"]:
            continue
        a = attrib[("effets_annonces", r["id"])]
        ajouter("effet annoncé", r["id"], f"{r['mesure']} — {r['effet']}", 1.0, float(r["ratio_central"]), a["regle"], a["issue_connue"])
    # 3. Chiffrages d'instituts (programmes Macron 2017 et 2022), comparaisons retenues par T10b
    for i, r in enumerate(lire("calibration_instituts.csv")):
        if not r["inclus_stats"].lower().startswith("oui") or not r["cout_realise"] or not r["chiffrage_campagne"]:
            continue
        a = attrib[("chiffrages_campagne", f"inst_{i:02d}")]
        ajouter(f"institut : {r['chiffreur']}", f"inst_{i:02d}", f"{r['campagne']} — {r['mesure']}",
                float(r["chiffrage_campagne"]), float(r["cout_realise"]), a["regle"], a["issue_connue"])

    with open("validation_mesures.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(lignes[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(lignes)

    def resume(nom, sel):
        if not sel:
            return None
        e0 = [abs(l["erreur_depart_pct"]) for l in sel]
        e1 = [abs(l["erreur_nous_pct"]) for l in sel]
        return {"groupe": nom, "n": len(sel), "erreur_mediane_depart_pct": round(statistics.median(e0), 1),
                "erreur_mediane_nous_pct": round(statistics.median(e1), 1),
                "erreur_moyenne_depart_pct": round(statistics.mean(e0), 1), "erreur_moyenne_nous_pct": round(statistics.mean(e1), 1),
                "ameliores": sum(l["verdict"] == "amélioré" for l in sel), "degrades": sum(l["verdict"] == "dégradé" for l in sel),
                "inchanges": sum(l["verdict"] == "inchangé" for l in sel)}

    officiel = [l for l in lignes if l["source"] == "officiel"]
    groupes = [
        ("Chiffrages officiels, statistique principale", officiel),
        ("  dont hors calibration (test)", [l for l in officiel if l["echantillon"] == "test"]),
        ("  dont mesures où la règle change le chiffre (facteur ≠ 1)", [l for l in officiel if abs(l["facteur"] - 1) > 1e-9]),
        ("  dont issue inconnue de l'agent d'attribution", [l for l in officiel if l["issue_connue"] == "non"]),
        ("Chiffrages officiels, toutes mesures", [l for l in lignes if l["source"].startswith("officiel")]),
        ("Effets annoncés", [l for l in lignes if l["source"] == "effet annoncé"]),
        ("Chiffrages d'instituts (tous)", [l for l in lignes if l["source"].startswith("institut")]),
    ]
    for ch in sorted({l["source"] for l in lignes if l["source"].startswith("institut")}):
        groupes.append((f"  {ch}", [l for l in lignes if l["source"] == ch]))
    for regle in sorted({l["regle"] for l in lignes} - {"Aucune"}):
        groupes.append((f"Règle : {regle}", [l for l in lignes if l["regle"] == regle]))
    out = [x for x in (resume(n, s) for n, s in groupes) if x]
    with open("validation_resume.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(out[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(out)
    # Statut de chaque règle : confirmée si elle rapproche plus souvent du réalisé qu'elle n'en éloigne ET réduit
    # l'erreur médiane ; contredite dans le cas inverse ; non concluante si les réalisés ne sont pas des observations
    statuts = []
    for regle in sorted(f):
        sel = [l for l in lignes if l["regle"] == regle and abs(l["facteur"] - 1) > 1e-9]
        if regle in ("Aucune",):
            continue
        if not sel:
            st, note = "non testée", "aucune mesure passée de ce type dans le backtest"
        elif regle in NON_CONCLUANTES:
            st, note = "non concluante", NON_CONCLUANTES[regle]
        else:
            a, d = sum(l["verdict"] == "amélioré" for l in sel), sum(l["verdict"] == "dégradé" for l in sel)
            m0 = statistics.median(abs(l["erreur_depart_pct"]) for l in sel)
            m1 = statistics.median(abs(l["erreur_nous_pct"]) for l in sel)
            st = "confirmée" if a > d and m1 < m0 else "contredite" if d > a and m1 > m0 else "mitigée"
            note = f"{a} améliorée(s), {d} dégradée(s) ; erreur médiane {m0:.0f} % → {m1:.0f} %"
        statuts.append({"regle": regle, "statut": st, "n": len(sel), "note": note})
    with open("validation_regles.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(statuts[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(statuts)
    statut = {s_["regle"]: s_["statut"] for s_ in statuts}

    # Indicateur par programme : correction totale (corrigé − statique, hors référence) ventilée par statut de règle
    conf = {}
    for l in lire("moteur_lignes.csv"):
        if l["composante"] == "investissement":
            continue
        base = float(l["montant"]) * float(l["facteur_reference"]) * float(l["facteur_interaction"])
        corr = float(l["corrige_central"]) - base
        st = "sans correction" if l["regle"] in ("Aucune", "Médiane des estimations", "Taux d'intérêt", "Règle d'or",
                                                   "Déjà dans la référence", "Recette ponctuelle", "Effet emploi du SMIC") \
            else statut.get(l["regle"], "non testée")
        d = conf.setdefault((l["fichier"], l["groupe"]), {})
        d[st] = d.get(st, 0.0) + corr
    sorties = []
    for (fichier, groupe), d in conf.items():
        tot = sum(abs(v) for k, v in d.items() if k != "sans correction")
        sorties.append({"fichier": fichier, "groupe": groupe,
                        **{f"correction_{k.replace(' ', '_')}": round(d.get(k, 0.0), 1)
                           for k in ("confirmée", "mitigée", "contredite", "non concluante", "non testée")},
                        "part_confirmee_pct": round(abs(d.get("confirmée", 0.0)) / tot * 100) if tot else 0})
    with open("confiance_programmes.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, list(sorties[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(sorties)

    for s_ in statuts:
        print(f"règle {s_['regle']:<46} {s_['statut']:<15} {s_['note']}")
    for o in sorties:
        print(f"{o['groupe']:<16} " + "  ".join(f"{k[11:]} {v:+.1f}" for k, v in o.items() if k.startswith("correction_"))
              + f"  | part confirmée {o['part_confirmee_pct']} %")
    print(f"{'groupe':<58} {'n':>3}  {'départ':>7}  {'nous':>7}   + / − / =")
    for o in out:
        print(f"{o['groupe']:<58} {o['n']:>3}  {o['erreur_mediane_depart_pct']:>6} %  {o['erreur_mediane_nous_pct']:>6} %   "
              f"{o['ameliores']} / {o['degrades']} / {o['inchanges']}")


if __name__ == "__main__":
    main()
