"""Contrôle du site public (web/index.html) dans un vrai navigateur.

Ouvre chaque vue, sur écran large puis sur téléphone, et échoue si :
  - une erreur JavaScript survient, ou si les données ne se chargent pas ;
  - une vue à graphiques n'en trace aucun ;
  - la page déborde horizontalement ;
  - un chiffre clé affiché ne correspond pas aux CSV de data/ (statistique principale, solde corrigé de chaque
    programme, date des données).

Nécessite Playwright (`pip install playwright && playwright install chromium`). Sans lui, le contrôle est sauté,
sauf si TEST_WEB_STRICT=1 (cas de la CI), où son absence est une erreur.
"""
import csv
import functools
import os
import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DATA = RACINE / "data"
VUES = ["accueil", "hier", "programmes", "equilibre", "foyer", "demain", "methode", "lexique"]
AVEC_GRAPHIQUES = {"hier", "programmes", "equilibre", "demain"}
ECRANS = {"large": (1280, 900), "téléphone": (390, 844)}


def lire(nom):
    with open(DATA / f"{nom}.csv", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fr(v, dec=0):
    """Format d'affichage du site : virgule décimale, signe moins typographique."""
    return f"{v:.{dec}f}".replace(".", ",").replace("-", "−")


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
    return {"mes_n": st["n"], "mes_mediane": fr(float(st["erreur_abs_mediane_pct"])) + " %", "soldes": soldes, "date": date}


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
                deb = page.evaluate("document.documentElement.scrollWidth - innerWidth")
                if deb > 1:
                    echecs.append(f"[{ecran}] vue {v} : débordement horizontal de {deb} px")
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
                annee, mois, jour = att["date"].split("-")
                if annee not in k("maj") or str(int(jour)) not in k("maj"):
                    echecs.append(f"pied de page : date « {k('maj')} », attendu {att['date']}")
            page.close()
        nav.close()
    serveur.shutdown()

    if echecs:
        print("\n".join("ÉCHEC  " + e for e in echecs), file=sys.stderr)
        sys.exit(f"test web : {len(echecs)} échec(s)")
    print(f"test web : OK ({len(VUES)} vues × {len(ECRANS)} écrans, chiffres clés conformes aux CSV)")


if __name__ == "__main__":
    main()
