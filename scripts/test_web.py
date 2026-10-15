"""Contrôle du site public (web/index.html) dans un vrai navigateur.

Ouvre chaque vue, sur écran large puis sur téléphone, et échoue si :
  - une erreur JavaScript survient, ou si les données ne se chargent pas ;
  - une vue à graphiques n'en trace aucun ;
  - la page déborde horizontalement ;
  - un chiffre clé affiché ne correspond pas aux CSV de data/ (statistique principale, solde corrigé de chaque
    programme, date des données) ;
  - une explication « Pourquoi ce chiffre ? » est vide ou ne s'ouvre pas ;
  - le simulateur « Mon foyer » n'affiche pas le revenu et les effets de la situation choisie
    (distributif_grille.csv) ;
  - un lien partageable (#/vue?choix=…) ne rétablit pas les choix, ou l'adresse ne suit pas les choix ;
  - axe-core (scripts/vendor/, règles WCAG 2.2 A et AA et bonnes pratiques) trouve un défaut d'accessibilité,
    dans une vue (accordéons ouverts), en thème clair et sombre, ou dans la fenêtre « Pourquoi ce chiffre ? ».

Nécessite Playwright (`pip install playwright && playwright install chromium`). Sans lui, le contrôle est sauté,
sauf si TEST_WEB_STRICT=1 (cas de la CI), où son absence est une erreur.
"""
import csv
import functools
import os
import re
import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DATA = RACINE / "data"
AXE = RACINE / "scripts" / "vendor" / "axe-core-4.10.3.min.js"
AXE_REGLES = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa", "best-practice"]
VUES = ["accueil", "idees", "hier", "programmes", "equilibre", "foyer", "demain", "methode", "journal", "lexique"]
AVEC_GRAPHIQUES = {"hier", "programmes", "equilibre", "demain"}
ECRANS = {"large": (1280, 900), "téléphone": (390, 844)}


def lire(nom):
    with open(DATA / f"{nom}.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fr(v, dec=0):
    """Format d'affichage du site : virgule décimale, signe moins typographique. Arrondi comme d3-format (toFixed sur la
    valeur absolue : demi éloigné de zéro, sur la valeur binaire exacte), et non au pair comme le format de Python."""
    q = Decimal(abs(v)).quantize(Decimal(1).scaleb(-dec), rounding=ROUND_HALF_UP)
    return ("−" if v < 0 and q else "") + f"{q:f}".replace(".", ",")


def accessibilite(page, lieu):
    """Défauts relevés par axe-core sur la page telle qu'elle est affichée."""
    if not page.evaluate("!!window.axe"):
        page.add_script_tag(path=str(AXE))
    v = page.evaluate("""async regles => (await axe.run(document, {runOnly: {type: "tag", values: regles}})).violations
        .map(v => `${v.id} (${v.impact}) : ${v.help} → ${v.nodes.slice(0, 3).map(n => n.target.join(" ")).join(" ; ")}`)""", AXE_REGLES)
    return [f"{lieu} : accessibilité, {x}" for x in v]


class Silencieux(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def attendus():
    """Valeurs que le site doit afficher, recalculées depuis les CSV."""
    st = next(r for r in lire("couche1_stats") if r["echantillon"].startswith("principal"))
    progs = lire("application_programmes")
    annee = lambda sc: int("".join(c for c in sc if c.isdigit())[:4] or 0)
    dernier = max({p["scrutin"] for p in progs}, key=annee)
    totaux = {r["groupe"]: float(r["central"]) for r in lire("moteur_totaux")
              if r["fichier"] == "application_lignes" and r["composante"] == "solde"}
    soldes = {p["programme"]: totaux[p["programme"]] for p in progs if p["scrutin"] == dernier}
    date = next(r["valeur"] for r in lire("meta") if r["cle"] == "date_donnees")
    return {"mes_n": st["n"], "mes_mediane": fr(float(st["erreur_abs_mediane_pct"])) + " %", "soldes": soldes, "date": date,
            "foyer": [r for r in lire("distributif_grille") if r["id"] == "retraite_couple_2_0_2000_0"],
            "idees": lire("idees"), "journal": len(lire("historique")), "isf": next(r for r in lire("moteur_lignes") if r["fichier"] == "paniers" and r["id"] == "l_isf_i")}


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        if os.environ.get("TEST_WEB_STRICT") == "1":
            sys.exit("test web : Playwright absent (requis par TEST_WEB_STRICT=1)")
        print("test web : sauté (Playwright absent)")
        return

    serveur = ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Silencieux, directory=str(RACINE)))
    threading.Thread(target=serveur.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{serveur.server_address[1]}/web/"
    att = attendus()
    echecs = []

    with sync_playwright() as p:
        nav = p.chromium.launch()
        for ecran, (w, h) in ECRANS.items():
            page = nav.new_page(viewport={"width": w, "height": h})
            sombre = nav.new_page(viewport={"width": w, "height": h}, color_scheme="dark")
            sombre.goto(base + "#/accueil")
            sombre.wait_for_selector("#chargement", state="detached", timeout=15000)
            erreurs = []
            page.on("pageerror", lambda e: erreurs.append(str(e)))
            page.on("console", lambda m: erreurs.append(m.text) if m.type == "error" else None)
            page.goto(base + "#/accueil")
            page.wait_for_selector("#chargement", state="detached", timeout=15000)
            for v in VUES:
                page.evaluate(f"location.hash = '#/{v}'")
                page.wait_for_selector(f"#v-{v}:not([hidden])")
                page.wait_for_timeout(150)
                if v in AVEC_GRAPHIQUES and page.locator(f"#v-{v} svg").count() == 0:
                    echecs.append(f"[{ecran}] vue {v} : aucun graphique tracé")
                if "[object " in page.locator(f"#v-{v}").text_content():
                    echecs.append(f"[{ecran}] vue {v} : un élément affiché comme « [object …] » (tableau imbriqué non aplati)")
                deb = page.evaluate("document.documentElement.scrollWidth - innerWidth")
                if deb > 1:
                    echecs.append(f"[{ecran}] vue {v} : débordement horizontal de {deb} px")
                for pg, theme in ((page, "clair"), (sombre, "sombre")):
                    if pg is sombre:
                        pg.evaluate(f"location.hash = '#/{v}'")
                        pg.wait_for_selector(f"#v-{v}:not([hidden])")
                    pg.evaluate("document.querySelectorAll('details').forEach(d => d.open = true)")
                    pg.wait_for_timeout(100)
                    echecs += accessibilite(pg, f"[{ecran}, {theme}] vue {v}")
            echecs += [f"[{ecran}] erreur JavaScript : {e}" for e in erreurs]

            if ecran == "large":
                k = lambda c: page.locator(f"[data-k={c}]").first.inner_text()
                page.evaluate("location.hash = '#/accueil'")
                for c in ("mes_n", "mes_mediane"):
                    if k(c) != att[c]:
                        echecs.append(f"accueil : {c} affiché « {k(c)} », attendu « {att[c]} »")
                page.evaluate("location.hash = '#/programmes'")
                cartes = page.locator("#cards-programmes .card")
                if cartes.count() != len(att["soldes"]):
                    echecs.append(f"programmes : {cartes.count()} cartes, {len(att['soldes'])} programmes attendus")
                for i in range(cartes.count()):
                    nom = cartes.nth(i).locator("h3").inner_text()
                    txt = cartes.nth(i).inner_text()
                    v = att["soldes"].get(nom)
                    lu = ("+" if v and v > 0 else "") + fr(v) + " Md€" if v is not None else None
                    if lu is None or lu not in txt:
                        echecs.append(f"programmes : solde corrigé de « {nom} » absent ou faux (attendu {lu})")
                # « Pourquoi ce chiffre ? » : chaque ligne corrigée s'explique sans erreur, et la fenêtre s'ouvre au clic
                vides = page.evaluate("""() => D.moteur.filter(m => { pourquoi(m.fichier, m.id);
                    const ok = $("#pq-corps").innerText.includes("Après correction"); $("#pq").close(); return !ok; }).map(m => m.id)""")
                if vides:
                    echecs.append(f"pourquoi : explication vide pour {', '.join(vides)}")
                page.locator("#cards-programmes .btn-pq").first.click()
                if not page.locator("#pq[open]").count() or "Après correction" not in page.locator("#pq-corps").inner_text():
                    echecs.append("pourquoi : la fenêtre du total ne s'ouvre pas")
                echecs += accessibilite(page, "fenêtre « Pourquoi ce chiffre ? »")
                page.keyboard.press("Escape")
                # Idées qui reviennent : une carte par idée, montants lus dans les CSV (moteur compris), lien vers une carte
                page.evaluate("location.hash = '#/idees'")
                page.wait_for_selector("#v-idees:not([hidden])")
                if page.locator(".card.idee").count() != len(att["idees"]):
                    echecs.append(f"idées : {page.locator('.card.idee').count()} cartes, {len(att['idees'])} idées attendues")
                isf = re.sub(r"\s", "", page.locator("#idee-isf").inner_text())
                for c in ("montant", "corrige_central"):
                    if fr(float(att["isf"][c]), 1) + "milliards" not in isf:
                        echecs.append(f"idées : ISF, {c} du moteur absent ({att['isf'][c]})")
                if "1,2milliard" not in re.sub(r"\s", "", page.locator("#idee-elus").inner_text()):
                    echecs.append("idées : coût des pouvoirs publics absent de la carte des élus")
                page.goto(base + "#/idees/elus")
                page.wait_for_timeout(200)
                if page.evaluate("document.activeElement.id") != "idee-elus":
                    echecs.append("idées : le lien #/idees/elus ne mène pas à la carte")
                # Simulateur de l'accueil (même situation, en euros par mois) et son lien vers « Mon foyer »
                serre = lambda t: re.sub(r"\s", "", t)  # sans espaces (le site sépare les milliers par une espace fine)
                page.evaluate("location.hash = '#/accueil'")
                for v in ("retraite", "couple_2"):
                    page.locator(f"#sim-accueil input[value={v}]").check(force=True)
                page.select_option("#acc-niveau", "2000")
                res = serre(page.locator("#acc-resultat").inner_text())
                for r in att["foyer"]:
                    v = round(int(r["gain_annuel"]) / 12)
                    if v and ("+" if v > 0 else "") + fr(v) + "€parmois" not in res:
                        echecs.append(f"accueil : effet mensuel de {r['reforme']} absent ou faux (attendu {v} € par mois)")
                if page.locator("#acc-enfants").is_visible():
                    echecs.append("accueil : le choix des enfants reste affiché pour un retraité")
                page.locator("#acc-affiner").click()
                page.wait_for_selector("#v-foyer:not([hidden])")
                if not page.locator("#sim-foyer input[value=couple_2]").is_checked() or page.locator("#sim-niveau").input_value() != "2000":
                    echecs.append("accueil : « Affiner mon calcul » ne reprend pas la situation choisie")
                # Simulateur « Mon foyer » : couple de retraités, deux pensions de 2 000 € bruts, sans dividendes
                page.evaluate("location.hash = '#/foyer'")
                for v in ("retraite", "couple_2"):
                    page.locator(f"#sim-foyer input[value={v}]").check(force=True)
                page.select_option("#sim-niveau", "2000")
                page.select_option("#sim-capital", "0")
                intro, res = page.locator("#foyer-intro").inner_text(), page.locator("#foyer-result").inner_text()
                serre = lambda t: re.sub(r"\s", "", t)  # sans espaces (le site sépare les milliers par une espace fine)
                g = att["foyer"]
                if not g or str(int(g[0]["revenu_disponible_avant"])) + "€" not in serre(intro):
                    echecs.append(f"foyer : revenu disponible absent ou faux (lu « {intro} »)")
                for r in g:
                    v = int(r["gain_annuel"])
                    if v and ("+" if v > 0 else "") + fr(v) + "€" not in serre(res):
                        echecs.append(f"foyer : effet de {r['reforme']} absent ou faux (attendu {v} €)")
                if page.locator("#sim-enfants").is_visible():
                    echecs.append("foyer : le choix des enfants reste affiché pour un retraité")
                # Liens partageables : l'adresse suit les choix, et un lien ouvert ailleurs les rétablit
                if "statut=retraite" not in page.evaluate("location.hash"):
                    echecs.append(f"partage : l'adresse ne reprend pas les choix (« {page.evaluate('location.hash')} »)")
                autre = nav.new_page(viewport={"width": w, "height": h})
                autre.goto(base + "#/foyer?statut=retraite&composition=couple_2&niveau=2000")
                autre.wait_for_selector("#chargement", state="detached", timeout=15000)
                if g and str(int(g[0]["revenu_disponible_avant"])) + "€" not in serre(autre.locator("#foyer-intro").inner_text()):
                    echecs.append("partage : le lien ne rétablit pas la situation du simulateur")
                autre.goto(base + "#/demain?ind=deficit_pct&stress=1")
                autre.wait_for_timeout(200)
                if not autre.locator("#f-stress").is_checked() or "Déficit" not in autre.locator("#titre-proj").inner_text():
                    echecs.append("partage : le lien ne rétablit pas les choix de la vue Dette et déficit")
                # Lien permanent d'un chiffre (« Citer ce chiffre ») : rouvre son explication, avec la citation
                autre.goto(base + "#/equilibre?pq=" + "paniers:l_isf_i")
                autre.wait_for_selector("#pq[open]", timeout=5000)
                if "Citer ou contester ce chiffre" not in autre.locator("#pq-corps").inner_text():
                    echecs.append("citer : le lien permanent n'ouvre pas l'explication avec sa citation")
                autre.close()
                # Ordre neutre (alphabétique) des programmes et des scénarios
                for sel in ("#cards-programmes .card h3", "#cards-paniers .card h3"):
                    noms = page.locator(sel).all_inner_texts()
                    if noms != sorted(noms, key=str.casefold):
                        echecs.append(f"ordre : {sel} n'est pas alphabétique ({noms})")
                # « Non calculé pour vous » et journal des corrections
                page.evaluate("location.hash = '#/accueil'")
                nc = page.locator("#acc-nonchiffre").inner_text() + page.locator("#acc-nonchiffre details").text_content()
                if "Ce n'est pas l'effet total" not in nc or "[object" in nc:
                    echecs.append("accueil : la liste des mesures non calculées manque")
                page.evaluate("location.hash = '#/journal'")
                page.wait_for_selector("#v-journal:not([hidden])")
                n_j = page.locator("#tb-journal tbody tr").count()
                if n_j != att["journal"]:
                    echecs.append(f"journal : {n_j} lignes affichées, {att['journal']} attendues")
                annee, mois, jour = att["date"].split("-")
                if annee not in k("maj") or str(int(jour)) not in k("maj"):
                    echecs.append(f"pied de page : date « {k('maj')} », attendu {att['date']}")
            page.close()
            sombre.close()
        nav.close()
    serveur.shutdown()

    if echecs:
        print("\n".join("ÉCHEC  " + e for e in echecs), file=sys.stderr)
        sys.exit(f"test web : {len(echecs)} échec(s)")
    print(f"test web : OK ({len(VUES)} vues × {len(ECRANS)} écrans, chiffres clés conformes aux CSV, aucun défaut d'accessibilité relevé par axe-core)")


if __name__ == "__main__":
    main()
