# T4p, partie D : Smic, non-recours, retraites (notes)

Date d'accès : 2026-10-14. Toutes les valeurs, avec leur citation et leur page, sont dans `D_smic_recours_retraites.csv`. Les sources sont dans `D_sources.csv`.

## Trouvé

- **Smic** (Insee, service-public, info.gouv) :
  - 2024 : 1 766,92 € brut et 1 398,70 € net au 1er janvier ; 1 801,80 € brut et 1 426,30 € net au 1er novembre.
  - 2026 : 1 823,03 € brut et 1 443,11 € net au 1er janvier ; **nouvelle revalorisation au 1er juin 2026** (arrêté du 22/05/2026), à 1 867,02 € brut et 1 477,93 € net.
- **Bénéficiaires des revalorisations** (Dares, publication du 29/10/2025) : 2,2 M de salariés (12,4 %) au 1er novembre 2024. Avant : 2,7 M (14,6 %) au 1er janvier 2024 et 3,1 M (17,3 %) au 1er janvier 2023. Aucune publication trouvée pour janvier 2026.
- **ARE** (Unédic, T1 2026) : 1 055 € nets par mois en moyenne ; 881 € pour les allocataires de niveau inférieur au bac.
- **Smic à 1 600 € (Montaigne, 24/06/2024)** : 19 Md€ (fourchette 17-21). Décomposition : −21,5 d'allègements, −3,7 de masse salariale publique, +6 de prélèvements, soit −19,2.
  - Les effets emploi (300 000 emplois perdus, fourchette 230-380 k) et l'assurance chômage sont **exclus** du chiffrage.
  - La prime d'activité n'est pas isolée.
  - Premier chiffrage du 20/06/2024 : 3,5 Md€.
- **Non-recours au RSA** : 33-37 % au T4 2021 (DREES, ER 1370, mai 2026) ; 34 % en 2018 (Dossiers de la DREES n° 92).
- **Réforme 2023, en 2027** (rapport annexé au PLFRSS, janvier 2023) :
  - brut : 10,3 Md€ (système de retraite) ;
  - net des mesures d'accompagnement : 6,2 ;
  - avec les recettes nouvelles : 7,7.
- **Suspension (art. 105 LFSS 2026)** :
  - lettre rectificative : 0,1 Md€ en 2026 et 1,4 Md€ en 2027 ;
  - amendement gouvernemental n° 2686 (adopté) : +0,2 et +0,5 ;
  - **total dérivé : 0,3 et 1,9 Md€**.
  - PLFSS 2027 (n° 3211, 01/10/2026) : la suspension ajoute 1,0 Md€ aux prestations vieillesse des régimes de base en 2027.

## Non trouvé (tentatives)

- **Coût budgétaire d'un emploi perdu au Smic** : aucun chiffre direct.
  - Dérivation `cout_emploi_perdu` : ARE + (brut − net) × 12, soit 15,1 à 17,2 k€ par an. Confiance basse.
  - Non inclus : cotisations patronales résiduelles, effets RSA et prime d'activité, non-indemnisation d'une partie des chômeurs.
  - Pistes non lues : modèle DG Trésor, Cour des comptes.
- **Non-recours à la prime d'activité** : la DREES (2022) dit qu'il n'est pas estimable avec les données disponibles. Le taux de recours « ~50 % » souvent cité n'a pas été vérifié.
- **Couverture CEJ / Garantie jeunes** : non trouvée.
  - Le site Dares bloque curl et WebFetch (WAF) ; les PDF Dreets PACA ne sont plus servis.
  - Le quota de recherches web partagé a été épuisé en cours de tâche.
- **Rendement de la réforme 2023 en 2027 net des autres prestations** : non publié. Le val_bas 4,1 est dérivé avec le ratio de 20 % cité par la Cour des comptes (2025, p. 67).
- **Coût global officiel de la suspension après amendements** : la loi n'en donne pas, et le PLFSS 2027 ne donne pas de total explicite.

## Vigilance

- **Signe** : les colonnes budgétaires sont en impact sur le solde (négatif = creuse le déficit). Les montants Smic et ARE sont en niveau.
- **Smic 2026** : deux valeurs dans l'année. La moyenne annuelle dérivée est de 1 848,7 € brut et 1 463,4 € net. L'intégrateur choisit la valeur à retenir.
- **Champs différents pour la réforme 2023** :
  - système de retraite (base et complémentaires) ou ROBSS seuls (6,7 Md€ en 2027 avant accompagnement) ;
  - l'étude d'impact du PLFRSS s'arrête en 2026 ;
  - les 9,7 et 11,8 Md€ de la Cour des comptes portent sur 2030 en € 2024.
- **PLFSS 2027** : les « 0,8 Md€ en 2027 / 1,9 en 2028 » de rendement net de la suspension semblent être des **gains supplémentaires d'une année sur l'autre** (champ ROBSS), pas des niveaux. Ne pas les additionner aux autres valeurs.
- **Montaigne** : site derrière un captcha, page lue via Wayback (20240710). Le chiffrage de 19 Md€ suppose une hausse en euros constants, en plus de l'indexation.
- **Sources secondaires** : le ratio du groupe d'experts Smic 2017 (−240 M€ par point de Smic) a été lu chez Montaigne, pas dans le rapport.
