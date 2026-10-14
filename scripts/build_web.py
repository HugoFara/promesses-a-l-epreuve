"""Génère web/complet.html : version autonome du tableau de bord complet, qui lit directement les CSV de data/.

Le site public (web/index.html, site.css, site.js) n'est pas généré : il est écrit à la main et lit lui-même les CSV.
complet.html en reste la version « spécialistes », toutes sections sur une page, liée depuis la vue Méthode.

La page d'origine (web/dashboard_page.html) attend l'environnement d'un artifact claude.ai (objet `dash`,
variables CSS du système de design). Ce script l'enveloppe dans une page complète : variables CSS (clair/sombre),
d3 v7 (copie locale web/vendor/, sans dépendance réseau) et une cale qui recrée dash.data / dash.calc / dash.onData / dash.colors à partir des CSV.

Affichage : depuis la racine du projet, `python3 -m http.server 8000` puis http://localhost:8000/web/
(les navigateurs bloquent la lecture de fichiers locaux par fetch en file://).
"""
from pathlib import Path

ICI = Path(__file__).resolve().parent.parent / "web"
SOURCES = {"mesures": "mesures_cout", "effets": "mesures_effets", "ps": "programmes_stabilite_fr",
           "pairs": "pairs_frankel_schreger", "regles": "regles_calibration", "elasticites": "elasticites",
           "hypotheses": "hypotheses_defaut", "application": "application_lignes",
           "programmes": "application_programmes", "parametres": "application_parametres", "paniers": "paniers",
           "moteur": "moteur_lignes", "moteur_totaux": "moteur_totaux", "moteur_variantes": "moteur_variantes",
           "sensibilite": "sensibilite_chiffreurs", "projection": "projection", "projection_controle": "projection_controle",
           "validation_resume": "validation_resume", "validation_regles": "validation_regles",
           "distributif": "distributif_menages"}

TETE = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tableau de bord complet</title>
<script src="vendor/d3-7.9.0.min.js"></script>
<style>
/* Palette : instance de référence validée (skill dataviz, references/palette.md) */
:root {
  --font-anthropic-sans: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-anthropic-serif: Georgia, "Times New Roman", serif;
  --color-bg: #f9f9f7; --color-panel: #fcfcfb; --color-fg: #0b0b0b; --color-fg-muted: #52514e;
  --color-border-line: #e1e0d9; --color-ok: #006300; --color-bad: #d03b3b;
  --cds-surface-popover: #fcfcfb; --cds-border: #c3c2b7; --cds-text-secondary: #52514e;
  --cds-shadow-popover: 0 4px 16px rgba(0,0,0,.12);
  --cds-chart-muted: #898781; --cds-chart-reference: #898781; --cds-chart-grid: #e1e0d9;
  --cds-chart-status-critical: #d03b3b;
  --cds-pad-xs: 4px; --cds-pad-sm: 8px; --cds-pad-lg: 16px;
  --cds-gap-xs: 4px; --cds-gap-sm: 8px; --cds-gap-md: 12px; --cds-gap-lg: 20px; --cds-gap-xl: 32px;
  --cds-radius: 8px; --cds-font-size-title: 1.75rem; --cds-font-size-heading: 1.1rem;
  --cds-font-size-body: 0.95rem; --cds-font-size-caption: 0.8rem; --cds-font-weight-medium: 600;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --color-bg: #0d0d0d; --color-panel: #1a1a19; --color-fg: #f0efec; --color-fg-muted: #c3c2b7;
    --color-border-line: #2c2c2a; --color-ok: #0ca30c; --color-bad: #e66767;
    --cds-surface-popover: #1a1a19; --cds-border: #383835; --cds-text-secondary: #c3c2b7;
    --cds-chart-grid: #2c2c2a;
  }
}
:root[data-theme="dark"] {
  --color-bg: #0d0d0d; --color-panel: #1a1a19; --color-fg: #f0efec; --color-fg-muted: #c3c2b7;
  --color-border-line: #2c2c2a; --color-ok: #0ca30c; --color-bad: #e66767;
  --cds-surface-popover: #1a1a19; --cds-border: #383835; --cds-text-secondary: #c3c2b7; --cds-chart-grid: #2c2c2a;
}
body { margin: 0; padding: 24px 16px; background: var(--color-bg); color: var(--color-fg); }
.dash-skeleton { color: transparent; background: var(--color-border-line); border-radius: 4px; }
select { font: inherit; }
</style>
<script>
(() => {
  const SOURCES = %SOURCES%;
  const sombre = matchMedia("(prefers-color-scheme: dark)").matches;
  const store = {}, calcs = [], rappels = [];
  window.dash = {
    colors: sombre ? ["#3987e5", "#d95926", "#199e70", "#c98500", "#d55181"]
                   : ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"],
    data: nom => store[nom] || {status: "loading", data: null},
    calc: (nom, def) => calcs.push([nom, def]),
    onData: cb => rappels.push(cb),
  };
  addEventListener("DOMContentLoaded", () => {
    Promise.all(Object.entries(SOURCES).map(([k, f]) =>
      d3.csv(`../data/${f}.csv`).then(rows => { store[k] = {status: "ok", data: rows}; },
                                     err => { store[k] = {status: "error", error: err}; })))
    .then(() => {
      for (const [nom, def] of calcs) {
        try { store[nom] = {status: "ok", data: def.fn(...def.inputs.map(i => store[i].data))}; }
        catch (e) { store[nom] = {status: "error", error: e}; console.error(nom, e); }
      }
      rappels.forEach(cb => cb());
    });
  });
})();
</script>
</head>
<body>
"""


def main():
    page = (ICI / "dashboard_page.html").read_text(encoding="utf-8")
    sources = "{" + ", ".join(f'"{k}": "{v}"' for k, v in SOURCES.items()) + "}"
    (ICI / "complet.html").write_text(TETE.replace("%SOURCES%", sources) + page + "\n</body>\n</html>\n", encoding="utf-8")
    print("web/complet.html écrit")


if __name__ == "__main__":
    main()
