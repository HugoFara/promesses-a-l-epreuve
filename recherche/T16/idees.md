# T16 — « Les idées qui reviennent : combien ça rapporte vraiment ? »

Projet, version 0.1 du 14 octobre 2026, à valider.

## 0. Le produit

Une page en langage courant. Chaque carte part d'une idée formulée comme les gens la formulent (« rétablir l'ISF », « réduire le train de vie de l'État », « supprimer les aides aux entreprises sans contrepartie »). Elle répond à trois questions :

1. **Combien ça rapporte ou coûte**, en milliards par an, avec un repère : « soit environ X % du déficit », ou « soit Y € par habitant et par an ».
2. **Peut-on s'y fier ?** Ce que le backtest dit des chiffrages de ce type de mesure : les coûts sont souvent justes, les rendements des impôts sur les très hautes assiettes et les « effets retour » souvent surestimés. Le niveau est donné en mots (« chiffrage fiable », « très incertain »), avec la fourchette.
3. **Qui paie, ou qui y perd**, en une phrase.

Pas de verdict sur l'opportunité de l'idée. Pas d'étiquette de parti sur la carte : l'idée vient des citoyens, pas d'un programme.

## 1. Règle de sélection des idées

La sélection ne vient pas de nous. Une idée entre si elle remplit **(A ou B) et C** :

- **A. Elle revient souvent dans les cahiers citoyens de 2019** : la synthèse officielle des contributions libres (Roland Berger, Bluenove, Cognito, rapport final du 14/6/2019, sur granddebat.fr) compte la proposition au moins 5 000 fois dans les contributions individuelles (cahiers citoyens et courriers ; les cahiers en font environ 93 %). *Révisé le 15/10/2026* : la première version s'appuyait sur les comptes provisoires et non publiés de l'association (seuil de 20 % des cahiers) ; la source publique les remplace (`D_rapport.md`). Effet : la taxe sur les transactions financières (1 052 mentions, que le repérage provisoire par mots-clés surestimait nettement) et la taxe Zucman (aucune proposition comptée ; présentée comme variante dans la carte de l'ISF) sortent ; la fraude sociale (3 594) reste exclue.
- **B. Elle a été testée dans un sondage national publié en 2026**, avec la question et les résultats en ligne. Point de départ : les 12 mesures d'Elabe pour Les Echos du 3 septembre 2026.
- **C. Elle a un effet sur le solde public** qu'une source publique permet de chiffrer, ou d'expliquer quand le chiffrage est impossible.

Une idée qui remplit A ou B mais pas C (par exemple la règle d'or, le RIC, le vote blanc) n'a pas de carte chiffrée. Elle va dans une liste « Idées sans effet direct sur le budget ».

*À décider par l'utilisateur* : le seuil de 20 %, et l'ajout d'autres sondages 2026 (Ifop, Ipsos, Odoxa) si leurs listes de mesures sont publiées.

## 2. Idées candidates et ce que les données couvrent déjà

> **Comptes des cahiers ci-dessous : provisoires et non publiés.** Ils viennent du travail en cours de l'association « Des cahiers pour décider et agir » et de Data For Good, et ne sont ni affichés ni recopiés dans `data/`. Depuis le 15/10/2026, la règle A s'appuie sur la synthèse officielle de 2019 (section 1) ; cette colonne n'est gardée que pour l'historique de la conception.

« Cahiers » : sujet repéré dans les cahiers citoyens de 2019 (comptes provisoires de l'association, non publiés : retirés du dépôt). « Elabe » : mesure testée le 3/9/2026.

| Idée | Origine | Déjà dans nos données | À chercher |
|---|---|---|---|
| Rétablir l'ISF | Cahiers | ISF rétabli, gain net par rapport à l'IFI (`paniers`) ; coût de la suppression de 2018 (`mesures_cout` `isf_ifi`) | — |
| Taxer les très grandes fortunes (Zucman) | Cahiers (même sous-thème) | Taxe Zucman (`paniers`), avec décote d'interaction | — |
| Taxer davantage les « méga-héritages » | Elabe | Successions LFI (`paniers`) | Rendement d'une mesure ciblée sur les très grosses successions |
| Supprimer les aides aux entreprises sans contrepartie | Elabe | Bandeaux d'allègements (`paniers`) | Montant total des aides aux entreprises (définitions très variables) et part « sans contrepartie » |
| Reconduire la surtaxe d'IS des grandes entreprises | Elabe | Surtaxe d'IS (`paniers`, `statut_reference_2027`) | — |
| Lutter contre l'évasion et la fraude fiscales | Cahiers | Ligne Ensemble `ens_fraude` (fraude sociale et fiscale) | Estimations publiques de la fraude ; montants réellement recouvrés et leur progression |
| Taxer les transactions financières | Cahiers | Relèvement de la TTF (`rendements_leviers`) | — |
| Réduire le train de vie de l'État | Cahiers, premier levier Elabe | Fusion d'opérateurs, un départ sur deux (`paniers`) | Définition et montant (fonctionnement de l'État hors personnel ?) : carte surtout pédagogique |
| Réduire les privilèges et la rémunération des élus, le nombre de parlementaires | Cahiers | — | Dotations des assemblées et de la présidence (mission « Pouvoirs publics » du PLF), avantages des anciens présidents |
| Supprimer 250 000 à 300 000 postes de fonctionnaires | Elabe | Un départ sur deux (`paniers`) | Coût moyen d'un poste, calendrier réaliste |
| Désindexer les pensions les plus élevées | Elabe ; cahiers (retraites, sens à vérifier) | Gel des pensions (`paniers`, simulateur « Mon foyer ») | — |
| Année blanche sur les prestations, sauf petites retraites | Elabe | — | Rendement (le PLF ou une étude d'impact l'a-t-il chiffrée ?) |
| Limiter l'indemnisation chômage à 12 mois avant 50 ans | Elabe | Réforme de l'assurance chômage `ens_chomage` | Chiffrage de cette variante précise (Unédic) |
| Réduire les prestations non contributives des étrangers | Elabe | AME recentrée (`paniers`) | Montants par prestation ; contraintes juridiques (Conseil constitutionnel) |
| Réduire la contribution française au budget de l'UE | Elabe ; cahiers (Europe, sens à vérifier) | — | Prélèvement sur recettes au profit de l'UE (PLF) ; carte surtout explicative (traités) |
| Annuler la dette détenue par la BCE | Elabe | — | Carte explicative : intérêts versés et ce qui revient déjà à l'État par la Banque de France ; ce que disent les traités (à sourcer). Pas de chiffre de « gain » sans source |
| Porter la franchise médicale de 100 à 140 € | Elabe | — | Rendement (PLFSS 2027 ?) |
| Baisser les taxes sur les carburants | Cahiers | Taxe carbone +10 €/t (`rendements_leviers`), dans l'autre sens | Rendement de l'accise sur les carburants, par centime |
| Baisser la TVA sur les produits de première nécessité | Cahiers (impôts, TVA, CSG, sens à vérifier) | Gel des prix LFI (`paniers`) ; élasticités TVA | Coût d'un taux réduit élargi |

Côté idées « de gauche » comme « de droite », la liste est déjà équilibrée. C'est l'avantage d'une sélection faite par les citoyens et un institut, et non par nous.

## 3. Conventions

- **Montant central et fourchette** : ceux du moteur quand l'idée y correspond à une ligne ; sinon la source primaire, avec la règle de correction du backtest qui s'applique au type de mesure (`regles.csv`), et `confiance` comme ailleurs.
- **Repère** : en part du déficit public de la dernière année connue, et en euros par habitant, avec des sources lues (`projection_reference.csv` pour le déficit).
- **Formulation de l'idée** : la plus proche des mots des cahiers ou du sondage, sans en reprendre de citation.
- **Une idée floue** (« train de vie de l'État ») : la carte dit ce que l'expression peut recouvrir, et chiffre chaque lecture séparément.
- **Juridique** : une mention courte et sourcée (« interdit par les traités européens », « censuré en 20XX ») seulement quand une décision ou un texte le dit.

## 4. Étapes

1. Valider la règle (section 1) et la liste (section 2).
2. Recherche sourcée des cases « À chercher », par un agent selon `recherche/CONSIGNES.md`.
3. Fichier `data/raw/idees.csv` : une ligne par idée, qui renvoie aux lignes du moteur ou aux sources, plus les comptes des cahiers et les résultats des sondages.
4. Vue `#/idees` sur le site, liée depuis l'accueil (« Les idées qui reviennent : combien ça rapporte ? »).
5. Accord de l'association pour citer ses comptes de sous-thèmes, avec la mention de la source.
