# Promesses à l'épreuve

Les promesses budgétaires sont-elles crédibles ? Ce projet compare le coût annoncé de mesures passées à ce qu'elles ont réellement coûté, en tire des règles de correction, puis les applique de la même façon aux programmes des partis. Un site public en langage courant présente les résultats.

Projet d'étude indépendant, sans lien avec l'État, une administration ou un parti politique. Il ne donne aucune consigne de vote et ne juge pas si une mesure est souhaitable.

## Le site

En ligne : **https://hugofara.github.io/promesses-a-l-epreuve/web/**, publié par GitHub Pages après chaque passage réussi des contrôles sur `main` (`.github/workflows/ci.yml`).

En local, depuis la racine du dépôt :

```bash
python3 -m http.server 8000
```

puis ouvrir http://localhost:8000/web/. Les pages :

- **Accueil** : ce que les mesures en débat changent pour votre foyer, en euros par mois ;
- **Les idées qui reviennent** : combien rapportent vraiment les idées des cahiers citoyens de 2019 et des sondages de 2026 ;
- **Les promesses d'hier**, **Les programmes**, **Financer les promesses**, **Mon foyer**, **Dette et déficit**, **Méthode**, **Journal des corrections**, **Lexique**.

Tous les chiffres affichés viennent des CSV de `data/` ; chaque montant corrigé a un bouton « Pourquoi ce chiffre ? ».

## Les données et le calcul

- `data/raw/` : la source de vérité, seuls fichiers à éditer. Chaque valeur porte son URL, une citation et un niveau de confiance.
- `data/*.csv` : fichiers publiés et dérivés, régénérés par le pipeline.
- `scripts/` : validation (`build.py`, schémas dans `schemas.py`), calculs (`calc.py`, `moteur.py`, `projection.py`…), contrôles (`garde_fous.py`, `test_web.py`).
- `recherche/` : les rapports de recherche documentaire, avec l'index des sources consultées (`sources.csv` : URL, date, sha256). Les documents eux-mêmes ne sont pas versionnés.

Lancer tout le pipeline :

```bash
pip install -r requirements.txt -r requirements-web.txt
playwright install chromium
bash scripts/run_all.sh
```

L'étape distributive (simulateur « Mon foyer ») demande un clone d'[OpenFisca-France](https://github.com/openfisca/openfisca-france) à côté du projet (voir `scripts/distributif.sh`) ; sans lui, elle est sautée et les fichiers déjà publiés sont gardés.

La méthode, ses résultats et ses limites sont expliqués sur le site (page « Méthode », boutons « Pourquoi ce chiffre ? ») ; le détail des recherches est dans `recherche/`, et chaque valeur modifiée est inscrite dans `data/raw/historique.csv` (page « Journal des corrections »).

## Contribuer

Les règles du projet (aucun chiffre sans source lue, traitement identique pour tous les partis, historique de chaque correction, présentation neutre) et la façon de contester un chiffre sont dans `CONTRIBUTING.md`. Les agents d'IA suivent en plus `AGENTS.md`.

## Méthode de travail

Le projet a été réalisé avec l'assistance d'une IA (Claude, d'Anthropic) : recherche documentaire par des agents qui suivent `recherche/CONSIGNES.md` (aucun chiffre sans source lue et archivée), écriture du code et des textes, relus et validés par l'auteur. Les contrôles automatiques (`scripts/garde_fous.py`, `scripts/test_web.py`) vérifient la cohérence des chiffres et l'accessibilité du site.

## Licence

- Code (`scripts/`, `web/`) : licence MIT, voir `LICENSE`.
- Données et textes (`data/`, `recherche/`) : [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr). Les chiffres viennent de sources publiques citées ligne par ligne ; les courtes citations restent la propriété de leurs auteurs.
- Bibliothèques incluses : d3 (`web/vendor/d3-LICENSE`) et axe-core (`scripts/vendor/axe-core-LICENSE.txt`).
