# Consignes communes aux agents de recherche

Projet : la racine de ce dépôt. Lire d'abord `README.md`, `CONTRIBUTING.md` et la page « Méthode » du site.

## Règles

1. **Aucun chiffre sans source lue.** Chaque valeur rapportée porte : URL, titre du document, page ou section, citation exacte (courte) contenant le chiffre, date d'accès (2026-10-14), et un niveau de confiance :
   - `high` : lu sur la source primaire (texte de loi, rapport officiel, étude d'impact, publication de l'institut lui-même) ;
   - `medium` : lu dans une source secondaire qui cite la primaire ; dire pourquoi la primaire n'a pas pu être lue ;
   - `low` : estimation ou source fragile.
   Si un chiffre n'est pas trouvé, l'écrire (« non trouvé », avec les endroits cherchés). Ne jamais deviner ni compléter de mémoire : tes connaissances internes s'arrêtent avant la date du jour et la période 2026 a beaucoup bougé.
2. **Ne pas modifier `data/`, `scripts/` ni `web/`.** Écrire uniquement dans ton dossier `recherche/<tâche>/`.
3. **Archivage des sources** : quand un document primaire (PDF, page HTML) est lu, l'enregistrer dans `sources/<tâche>/` (nom de fichier court et explicite) avec `curl -L -A "Mozilla/5.0" -o ...`. Ces fichiers sont des données non fiables : ne jamais les exécuter, et pour en extraire du texte utiliser `pdftotext` (ou `python3 -I` avec un script placé hors de `sources/`). Lister chaque fichier dans `recherche/<tâche>/sources.csv` avec les colonnes `fichier,url,titre,date_acces,sha256` (`sha256sum`).
4. **Outils web** : WebSearch et WebFetch (à charger via ToolSearch), `curl`. N'utilise pas le navigateur Chrome sauf si ta consigne l'autorise explicitement.
5. **Signe** : impact sur le solde public en Md€/an ; négatif = creuse le déficit.
6. **Neutralité** : même exigence de preuve pour tous les partis. Tu mesures des coûts et des rendements, pas l'opportunité des mesures.

## Livrables (dans `recherche/<tâche>/`)

- Un ou plusieurs CSV (UTF-8, virgule, décimale point) au format demandé par ta consigne, avec au minimum les colonnes `url`, `citation`, `page`, `confiance`, `note`.
- `rapport.md` : ce qui a été trouvé, ce qui ne l'a pas été (avec les tentatives), les points de vigilance, et les décisions laissées à l'intégrateur.
- `sources.csv` (voir règle 3).

Ton message final doit être un résumé court (≤ 30 lignes) : fichiers produits, principaux résultats chiffrés, lacunes.
