# T10a, groupe D : notes de recherche

Date d'accès de toutes les sources : 2026-10-14. Les sources archivées sont dans `sources/T10a/D_*` et listées dans `sources_D.csv`.

**Limite d'outillage.** Le budget WebSearch de la session a été épuisé en cours de tâche. senat.fr est resté inaccessible (TLS reset, curl rc=35, WebFetch ECONNRESET). assemblee-nationale.fr a renvoyé plusieurs erreurs 503 (annexe 8 du PLFSS 2026, PLFR 1 2022). Certaines pistes n'ont donc pas pu être creusées ; elles sont signalées plus bas.

## Synthèse

| id | ex ante | ex post (central) | ratio | statut |
|---|---|---|---|---|
| ac_2021 (assurance chômage 2019-2021, année 2022) | 1,93 Md€ (Unédic, avril 2021, borne haute) | 1,9 Md€ (Unédic, fév. 2023) | 0,98 | retenu, confiance low |
| apl_contemp_2021 | 0,75 Md€ (PLF 2021) | 1,11 Md€ (Cour des comptes 2025) | 1,48 | retenu, medium |
| cheque_energie_exc_2021 | 0,6 Md€ (gouvernement, oct. 2021) | 0,493 Md€ (Cour 2024) | 0,82 | retenu, high |
| cheque_energie_exc_2022 | 1,8 Md€ (évaluation préalable PLFR 2 2022) | 1,53 Md€ (Cour 2024) | 0,85 | retenu, medium |
| cheque_fioul_2022 | 0,23 Md€ (LFR 1 2022) | 0,048 Md€ (réponse ministérielle, déc. 2023) | 0,21 | retenu, medium |
| bouclier_gaz_2023 | 6,8 Md€ (PLF 2023, cité par la Cour) | 1,35 Md€ (CRE juil. 2023, cité par la Cour) | 0,20 | retenu, medium |
| Réforme assurance chômage 2019 (horizon 2019-2021) | n/a | n/a | n/a | exclu |
| Réforme assurance chômage 2023 (contracyclicité) | n/a | n/a | n/a | exclu |
| RSA 2009 | n/a | n/a | n/a | exclu |
| Remise carburant 2022 | n/a | n/a | n/a | exclu |

Effet retenu : `cheque_fioul_benef` (≈1,6 M ménages éligibles annoncés contre ≈306 000 chèques émis, ratio 0,19, « Surestimé »).

## (1) Réforme de l'assurance chômage 2019 (décret de juillet 2019) : EXCLUE

- Ex ante : les résultats de recherche citent l'étude d'impact Unédic de 2019 (« en cumul sur 2019-2021, les dépenses d'indemnisation diminueront au total de 3,4 Md€ »). Je n'ai pas lu le PDF lui-même (page https://www.unedic.org/publications/etude-dimpact-de-la-reforme-de-lassurance-chomage-2019 repérée, non archivée).
- Motif d'exclusion : l'horizon 2019-2021 a été rompu. La réforme a été suspendue par la crise Covid et par les recours en Conseil d'État, puis remaniée par le décret de mars 2021. Elle n'est entrée en vigueur qu'entre juillet et décembre 2021 (synthèse Unédic mars 2025, p. 3 : « la dernière en date étant la règle concernant l'ouverture de droits, entrée en vigueur au 1er décembre 2021 »). Aucun ex post ne porte sur le même périmètre et la même période. La version 2021 de la réforme est traitée en (2).

## (2) Réforme 2021 (règles 2019-2021 effectivement appliquées) : RETENUE (`ac_2021`, confiance low)

- **Ex ante** (primaire, lu) : Unédic, « Impact de l'évolution des règles d'assurance chômage au 1er juillet 2021 », avril 2021, p. 7. Moindres dépenses de 1 190 à 1 930 M€ en 2022 selon la date de retour à meilleure fortune, et de 2 260 M€ en régime de croisière. La borne haute suppose que la condition d'affiliation de 6 mois et la dégressivité au 7e mois s'appliquent dès le 1er janvier 2022. Elles sont en fait entrées en vigueur le 1er décembre 2021, donc la borne haute (1,93) est la bonne référence. C'est une hypothèse de lecture de ma part.
- **Ex post** : Unédic, prévisions financières du 21 février 2023, tableau A p. 11 : réforme 2021 = 1,9 Md€ en 2022 et 2,2 Md€ en 2023 et en régime de croisière. La synthèse d'évaluation de mars 2025 (p. 4) indique : « Les observations de la montée en charge de la réforme confirment ces estimations ex ante », sans donner de chiffre.
- **Vigilance** :
  - L'ex post est une estimation par modèle de la même institution qui a produit l'ex ante, faite après l'observation de 2022. Ce n'est pas une évaluation indépendante.
  - Je n'ai trouvé aucun chiffrage ex post de la Cour des comptes, de la Dares ou de l'Unédic donnant des économies constatées en Md€ (rapport financier Unédic 2022 et situation financière de juin 2026 consultés : qualitatif seulement).
  - D'où la confiance low.
  - L'ex ante gouvernemental « ≈2,3 Md€/an » correspond aux 2 260 M€ de l'Unédic.
  - Bonus-malus : neutre ex ante. Démission-reconversion (+0,3 Md€) et financement de Pôle emploi (+0,5 Md€) sont hors périmètre des deux côtés.
- **Effets sur l'emploi** : l'étude Unédic 2025 sur le nouveau calcul du SJR conclut à un « accès plus rapide à l'emploi » (document d'étude, conclusions de l'analyse économétrique), sans chiffre comparable à une annonce ex ante lue. Pas de ligne effet.

## (3) Réforme 2023 (contracyclicité, −25 % de durée) : EXCLUE

- Ex ante lu : Unédic, février 2023, p. 10. La réforme réduirait les dépenses de 4,5 Md€ en régime de croisière (dont 4,2 Md€ d'allocations et 0,3 Md€ pour les retraites complémentaires) et de 3,0 Md€ en 2025 (tableau A p. 11). Le décret date du 26 janvier 2023 : ce chiffrage est donc postérieur de quelques jours à l'adoption. L'annonce gouvernementale « ≈4 Md€ » n'a pas été lue.
- Ex post : non trouvé. Lieux consultés :
  - Unédic, situation financière de juin 2026 : effets qualifiés de « toujours puissants », régime de croisière attendu en 2027, sans chiffre isolé ;
  - Unédic, synthèse du CA de juin 2023 (non retenue) ;
  - annexe 8 du PLFSS 2026 (erreur 503) ;
  - recherches web.

  Le régime de croisière n'est pas atteint (montée en charge sur 5 ans). Le chiffre « 2,8 Md€ en 2025 » apparu dans un résumé de recherche n'a pas été confirmé et n'est pas utilisé.

## (4) RSA 2009 (RSA activité) : EXCLU

- Pistes trouvées, uniquement dans des sources secondaires non lues en primaire :
  - prévision de dépense FNSA 2010 de 1,548 Md€ (Localtis, citant le rapport du Sénat sur le PLF 2011) contre ≈1,3 Md€ dans un autre document du Sénat ;
  - recette de la taxe FNSA de 0,833 Md€ en 2009 contre 1,432 Md€ prévus (compte rendu de la commission des finances de l'AN, 2010) ;
  - non-recours au RSA activité de 68 % (rapport final du Comité national d'évaluation, déc. 2011, via OFCE et Localtis).
- Motif d'exclusion : je n'ai pu lire ni l'ex ante (étude d'impact du projet de loi de 2008, PAP 2010 programme 304) ni l'ex post (RAP 2010, rapport du comité). senat.fr est inaccessible et le budget de recherche épuisé. Je n'ai pas non plus pu établir de couple de chiffres sur le même périmètre et la même année. C'est une piste prioritaire pour une reprise : RAP 2010 du programme 304 sur performance-publique et rapport final du CNE RSA (DARES).

## (5) Contemporanéisation des APL (2021) : RETENUE (`apl_contemp_2021`, medium)

- **Ex ante** : PLF 2021, économie de 0,75 Md€ en 2021. Lue dans le rapport spécial AN PLF 2021, p. 11 : « La réforme des aides au logement devrait générer 750 millions d'euros d'économies ». La Cour (p. 55) donne 0,746 Md€. Le PAP 2021 du programme 109 n'a pas été lu, d'où la confiance medium.
- **Ex post** (primaire, lu) : Cour des comptes, observations définitives S2024-1417 (janv. 2025), p. 7 et p. 55 : « L'économie réalisée sur le versement des prestations s'est élevée à 1,11 Md€ en 2021 ».
- **Vigilance** :
  - Autres ex ante : PLF 2019, 0,9 Md€ pour 2019 (année partielle, réforme reportée) ; PLF 2020, 1,25 Md€ (réforme non appliquée en 2020) ; Cnaf mai-juin 2020, 1,16 Md€ en année pleine hors Covid et 0,924 Md€ avec Covid. Seul le PLF 2021 porte sur la même année d'application. Ratio 1,48 : économie sous-estimée.
  - Coûts de mise en œuvre (≈100 M€) non déduits.
  - La dépense totale d'aides au logement a baissé de 963 M€ en 2021 (comptes du Fnal) ; ce chiffre mesure autre chose (variation brute, pas un contrefactuel).

## (6) Remise carburant 2022 : EXCLUE

- Ex post lu (Cour des comptes, mars 2024, p. 58) : « remise carburant », coût total de 7,6 Md€ pour l'État (avril-décembre 2022) ; l'annexe 5 donne une exécution budgétaire de 7 854 M€.
- Ex ante : seulement des enveloppes successives pour des phases différentes :
  - 3 Md€ par décret au printemps pour avril-juillet à 15 c HT et 4,6 Md€ en LFR 1 d'août (Public Sénat, 17/10/2022, non primaire) ;
  - extension à mi-novembre évaluée à 0,4 Md€ (PLFR 2 2022, exposé des motifs p. 7-8, lu).
- Motif d'exclusion :
  - le dispositif a changé quatre fois (18 c, puis 30 c, puis 10 c) ;
  - aucun ex post n'est ventilé par phase ;
  - les montants ex ante pour le dispositif final sont des crédits ouverts et non des chiffrages, et ne sont pas lus en primaire ;
  - une comparaison « initial 4 mois » est impossible sans coût réalisé avril-juillet (le rapport Husson du Sénat du 28/07/2022 citant 4,4 Md€ engagés est inaccessible).

## (7) Bouclier tarifaire gaz 2023 : RETENU (`bouclier_gaz_2023`, medium)

- Ce cas est distinct de la note de `bouclier_elec`, qui porte sur le gel du gaz 2022.
- **Ex ante** : « Le PLF 2023 tablait initialement sur un coût 6,8 Md€ au titre de 2023 sur le bouclier individuel ». Lu dans la Cour des comptes (mars 2024), fiche annexe, p. 217 (p. 220 du PDF). Le PLF 2023 n'a pas été lu directement.
- **Ex post** : CRE, délibérations de juillet 2023, citées par la même fiche de la Cour : « Pour 2023, l'estimation est de seulement 1 350 M€ ». Estimation non définitive ; les délibérations CRE n'ont pas été lues (recherche impossible).
- **Vigilance** :
  - Le bouclier a pris fin au 30 juin 2023 au lieu d'une prolongation possible au S2. Cette décision est elle-même due au reflux des prix, d'où la cause « Prix de l'énergie ».
  - Les volumes déclarés étaient inférieurs à l'hypothèse de la DGEC (66 TWh annualisés contre 74 TWh).
  - Le périmètre exclut l'aide à l'habitat collectif.

## (8) Chèques énergie exceptionnels : RETENUS (3 lignes)

- **2021 (100 €, 5,8 M ménages)**
  - Ex ante : annonce d'O. Dussopt à l'AN (QAG n° 4365, JO 6 oct. 2021) : « soit 600 millions d'euros ». C'est une annonce gouvernementale ; le chiffrage du PLFR de fin de gestion 2021 n'a pas été lu.
  - Ex post : Cour 2024, annexe 4 : 493 M€, « montant correspondant à un taux de recours à 85 % » ; exécution 363 + 125 = 488 M€ (somme calculée, annexe 5).
- **2022 (100/200 €, 12 M ménages)**
  - Ex ante : évaluation préalable de l'art. 9 du PLFR 2 2022, p. 113 : budget de 1,8 Md€. Le tableau d'impact (p. 115) donne 2 030 M€, soit 1,8 Md€ plus les 230 M€ du chèque fioul (décomposition calculée).
  - Ex post : Cour, annexe 4 : 1 530 M€ ; annexe 5 : 868 M€ exécutés en 2022 et 660 M€ en « prévision d'exécution » 2023 (somme calculée 1 528).
  - L'évaluation préalable ne fait pas d'hypothèse explicite de non-recours : l'écart s'explique vraisemblablement par le non-usage des chèques. C'est mon interprétation ; la Cour ne chiffre pas de taux de recours pour ce chèque.
- **Chèque fioul**
  - Ex ante : 230 M€ (LFR 1 2022, rappelé dans l'exposé des motifs du PLFR 2, p. 28), pour ≈1,6 M ménages éligibles (évaluation préalable p. 115).
  - Ex post : réponse ministérielle à la QE n° 9837 (JO 12/12/2023) : ≈306 000 chèques émis pour ≈48 M€, taux d'usage provisoire de 75,8 %. La Cour indique une exécution de 52 M€ en 2022. Bas = 48 × 0,758 ≈ 36 M€ (calculé).
  - Le PDF a été récupéré sur un miroir (greenunivers.com) car le site de l'AN renvoyait une erreur 503. Le document est le PDF officiel de l'AN (en-tête et URL AN).
- **Chèque bois** (non retenu) : l'annexe 4 de la Cour donne 225 M€ et l'annexe 5 une exécution de 50 M€ en 2022 (2023 n.d.). Je n'ai trouvé ni ex ante lu en primaire ni ex post complet.
- Montant prévisionnel cumulé des chèques exceptionnels selon la Cour (p. 61) : 2,86 Md€. Ce total agrégé n'est pas utilisé.

## Conversions et valeurs calculées

- 488 M€ = 363 + 125 (chèque 2021, exécution).
- 1 528 M€ = 868 + 660 (chèque 2022).
- 36 M€ ≈ 48 × 0,758 (chèque fioul).
- Ratio de l'effet fioul : 306 000 / 1 600 000 ≈ 0,19.
- Le choix de la borne haute 1,93 pour `ac_2021` est une hypothèse de lecture (date du retour à meilleure fortune).
- Tous les montants sont convertis en Md€ ; toutes les valeurs sont des grandeurs positives, le sens étant porté par la colonne `sens`.
