# T19 : registre des prédictions sur les mesures du budget 2027

Consigne préparée le 16/10/2026. Lire d'abord `recherche/CONSIGNES.md`, puis `recherche/T18/rapport.md` (§ 6) et `recherche/T1/rapport.md`.

## Pourquoi

Le test de la méthode sur le passé n'est pas aveugle : l'agent qui choisit les règles connaît souvent le coût réel (T18). Le seul test vraiment aveugle consiste à prédire **avant** que le coût réel existe. Les mesures du PLF et du PLFSS 2027 ont un chiffrage officiel, mais aucun réalisé : on enregistre maintenant, à date certaine (commit), ce que donnent les règles gelées. On comparera au réalisé quand il paraîtra (exécution 2027, publiée en 2028).

## Phase 1 : relevé des mesures chiffrées (un agent)

Relever toutes les mesures du PLF 2027 (AN n° 3210) et du PLFSS 2027 (AN n° 3211) qui ont un **chiffrage officiel de leur effet sur le solde en 2027** (et en 2028 s'il est donné), ainsi que les mesures chiffrées de la loi n° 2026-534 relative à la lutte contre les fraudes sociales et fiscales.

Sources, déjà archivées dans `sources/T1/` : `PLF2027_evaluations_prealables.pdf`, `PLF2027_projet_AN3210.html`, `PLFSS2027_projet_AN3211.html` (annexe 9 ou équivalent pour les évaluations préalables du PLFSS ; la télécharger dans `sources/T19/` si elle n'est pas dans le projet), `HCFP_avis_2026-5_PLF-PLFSS_2027.pdf`. Compléter sur le web seulement si nécessaire.

Pour chaque mesure, une ligne de `recherche/T19/mesures.csv` :

| Colonne | Contenu |
|---|---|
| `id` | identifiant court, unique, sans accent (`plf27_art4_dons`, `plfss27_art35_gel`) |
| `texte`, `article` | PLF 2027, PLFSS 2027 ou loi 2026-534 ; numéro d'article du texte déposé |
| `mesure` | libellé neutre de la mesure |
| `sens` | `cout` ou `economie` (effet sur le solde public) |
| `indicateur` | ce que mesure le chiffrage (par exemple « Rendement Md€ 2027, État ») |
| `annee` | 2027 (une seconde ligne si 2028 est chiffré, id suffixé `_2028`) |
| `chiffrage_md` | montant positif en Md€, tel qu'écrit par la source |
| `auteur` | Gouvernement (évaluation préalable), annexe du PLFSS… |
| `comportement_inclus` | `oui`, `non` ou `inconnu`, avec la phrase dans `citation_comportement` |
| `perimetre` | État, Sécurité sociale, collectivités, APU |
| `url`, `citation`, `page`, `confiance`, `note` | comme le demande `recherche/CONSIGNES.md` |

Ne relever que des montants écrits dans la source (pas de calcul, sauf somme explicite signalée dans `note`). Les mesures sans chiffrage vont dans le rapport, pas dans le CSV. Ne pas chercher à savoir si la mesure sera votée.

## Phase 2 : attribution à l'aveugle (un autre agent)

Fichier `aveugle/mesures.csv` (`id, mesure, annee, sens, indicateur, chiffrage_md, auteur`) et `aveugle/regles_disponibles.csv` (copie de `recherche/T18/aveugle/regles_disponibles.csv`), même protocole que T18 phase 3 : une règle par ligne d'après la seule nature de la mesure, justification d'une phrase. Ici, `issue_connue` vaut `non` par construction ; l'agent le confirme.

## Phase 3 : registre (intégrateur)

Dans `predictions/plf2027/`, à la racine du dépôt : les mesures, l'attribution, et la prédiction de chaque ligne (chiffrage × facteur central de la règle, avec les facteurs gelés au commit du registre), plus un `README.md` qui dit comment et quand comparer au réalisé, et quelles lignes ne seront pas comparables (mesure non votée ou modifiée). Le registre est publié tel quel par un commit ; toute modification ultérieure passe par un nouveau fichier daté, jamais par la réécriture du premier.
