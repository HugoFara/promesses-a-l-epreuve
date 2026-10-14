# T10a, groupe C : notes

Date d'accès de toutes les sources : 2026-10-14. Les valeurs calculées sont marquées « calculé ». Sources archivées dans `sources/T10a/C_*` (voir `sources_C.csv`).

## Conditions d'accès (à lire d'abord)

- **senat.fr** : erreur 500, puis plus de réponse du tout (curl comme WebFetch) pendant toute la session. Aucun rapport du Sénat n'a pu être lu.
- **budget.gouv.fr** (Incapsula), **legifrance.gouv.fr** (défi JavaScript), **economie.gouv.fr** (403) : bloqués pour les robots. Les **évaluations préalables primaires** des PLF 2018, 2020, 2021 et 2023 n'ont donc pas pu être lues. Leurs chiffres sont repris des rapports généraux de l'Assemblée nationale, qui les citent avec « Source : évaluation préalable » (confiance medium).
- **assemblee-nationale.fr** : erreur 503 avec curl, mais accessible avec WebFetch. Les PDF ont été récupérés par WebFetch puis copiés dans `sources/T10a/` ; l'URL d'origine est notée dans `sources_C.csv`.
- **Quota WebSearch épuisé** en cours de tâche. La suite s'est faite en consultant directement les sites officiels : moteur de recherche interne de ccomptes.fr, strategie-plan.gouv.fr, insee.fr, securite-sociale.fr.

## 1. Redevance / contribution à l'audiovisuel public (CAP), 2022 : retenue, confiance low (`cap_2022`)

- **Ex ante** (lu sur la source primaire, évaluation préalable de l'art. 1 du PLFR 2022, projet de loi n° 17, p. 135-137 du PDF) : −3,1 Md€ sur le solde budgétaire 2022 (encaissements nets de CAP prévus en LFI). La perte de prélèvements obligatoires est de 3,2 Md€. Rendement 2021 : 3,1 Md€ pour les particuliers (nets des dégrèvements de 627 M€) et 0,1 Md€ pour les professionnels.
- **Ex post** : la Cour des comptes (Budget de l'État 2022, tableau 11, p. 82) indique un « transfert de TVA pour financer l'audiovisuel public − 3,6 » et une « suppression du versement de subvention … + 0,6 » (dégrèvements que l'État ne compense plus). Net calculé : 3,0 Md€.
- **Vigilance** : l'ex post mesure le **financement de compensation**, dont le montant relève d'une décision budgétaire (dotation maintenue). Ce n'est pas une perte de recette observée, car le contrefactuel de CAP 2022 n'est pas observable. Le montant 2023 (3,815 Md€, LF 2023 art. 120) a été vu uniquement dans un résumé de recherche et n'a **pas** été lu sur source primaire, donc pas utilisé. À exclure si l'intégrateur exige un ex post contrefactuel.

## 2. Taxe d'habitation, 20 % restants (2021-2023) : retenue, étapes 2022-2023 seulement (`th_20`)

- **Ex ante** (rapport général AN n° 2301, t. II, p. 195, citant l'évaluation préalable de l'art. 5 du PLF 2020) : 2,3 Md€ en 2021, 5,1 Md€ en 2022 et 7,8 Md€ à partir de 2023.
- **Ex post** : mesures nouvelles en exécution publiées par la Cour (Budget de l'État 2022, p. 82 : « Suppression de la TH − 2,8 » ; Budget de l'État 2023, p. 76 : « Extinction progressive de la taxe d'habitation − 2,8 »). Le chiffrage vient du MEF ; c'est une estimation actualisée en exécution, pas une évaluation contrefactuelle.
- **Périmètre retenu** : coût incrémental des étapes 2022 et 2023. Ex ante 7,8 − 2,3 = 5,5 (calculé) ; ex post 2,8 + 2,8 = 5,6 (calculé). L'étape 2021 n'est pas isolable dans le tableau 2021 de la Cour, où elle se mêle à la rebudgétisation du reliquat de TH (+4,9) et aux transferts de TVA.
- Recoupement fragile, non mis dans le CSV : si le −2,8 de 2023 correspond au reliquat perçu en 2022 (35 % de l'impôt des 20 %), le coût total vaut environ 2,8 / 0,35 = 8,0 (calculé), contre 7,8 ex ante.
- Pas de doublon avec `th_80`.

## 3. Baisse des impôts de production 2021 : retenue (`ip_2021`)

- **Ex ante** (rapport général AN n° 3399, t. II, citant les évaluations préalables des art. 3 et 4 du PLF 2021) :
  - CVAE : coût brut de 7,2 Md€ (p. 101) ;
  - valeurs locatives industrielles : CFE 1,54 + TFPB 1,75 = 3,29 Md€ (p. 208) ;
  - gain croisé pour l'État de 0,4 Md€ ;
  - total : « gain global … de 10 milliards d'euros par an » (p. 102).
  - Coût net pour l'État en 2021 après effet retour d'IS : 5,9 (CVAE) + 2,9 (foncier) = 8,8 (calculé).
- **Ex post** :
  - Cour des comptes, Budget de l'État 2021, p. 35, note 21 : coût total pour l'État de 10,3 Md€ (6,8 de recettes fiscales et 3,5 de PSR). L'effet retour d'IS de +1,4 Md€ (tableau 12, p. 77) donne un net de 8,9 (calculé), proche des 8,8 ex ante.
  - France Stratégie (rapport final France Relance, vol. II ch. 13, janvier 2024), d'après la DG Trésor : coût brut de 10,6 Md€ en 2021 (CVAE 6,8, CFE 1,8, TFPB 2,0) et 11,7 Md€ en 2022. Retenu comme borne haute.
- **Vigilance** : le CSV compare un coût brut avant effet retour d'IS (ex ante 10 ; 10,5 calculé avant le gain croisé de 0,4).
- **Effets** : France Stratégie juge l'évaluation causale (emploi, investissement) « pas encore possible ». Le gouvernement n'a pas annoncé d'effet chiffré dans les documents lus. Aucune ligne d'effet.
- Corroboration non utilisée dans le CSV : Insee IR n° 81 (comptes 2021), « diminution des impôts sur la production (−8,9 Md€) ». C'est une variation d'agrégat qui inclut l'évolution spontanée.

## 4. Suppression de la CVAE 2023-2024 : exclue

- Ex ante lu (rapport général AN n° 292, t. II, p. 225-226, citant l'évaluation préalable) :
  - allègement d'environ 4 Md€ en 2023 et 7,61 Md€ en 2024 avant effet retour ;
  - coût pour l'État de −3,5 (2023), −7,0 (2024) et −7,2 en régime pérenne ;
  - coût brut pour l'État de 8,9 Md€ à partir de 2024.
- Raisons de l'exclusion :
  1. L'horizon 2024 n'a pas été réalisé : la deuxième étape a été étalée jusqu'en 2027 par la LF 2024. La Cour (Budget de l'État 2024) chiffre « la suppression de la CVAE à horizon 2027 (− 1,1 Md€) » pour 2024.
  2. Pour 2023, la Cour ne publie que des lignes de transfert et de périmètre : TVA aux collectivités −10,5, reliquats de CVAE affectés à l'État +9,9, effet retour IS +0,6, extinction de la CVAE régionale −4,2 (Budget de l'État 2023, tableau 13). Elles ne donnent pas un coût de la mesure comparable aux 3,5 ex ante : le net calculé vaut ≈ 0 ou −4,2 selon le traitement retenu, et il est dominé par des effets de calendrier.
- Non trouvé : une évaluation ex post du coût de l'étape 2023 (DGE, France Stratégie, Sénat inaccessible).

## 5. Baisse de l'IS de 33⅓ % à 25 % : retenue, confiance medium (`is_25`)

- **Ex ante** (rapport général AN n° 273, t. III, art. 41, p. 167-168) :
  - surcoût de la trajectoire du PLF 2018 par rapport à celle de la LFI 2017 : 4,1 Md€/an à terme ;
  - impact consolidé 33⅓ → 25 %, calculé par le rapporteur général à partir des évaluations préalables des PLF 2017 et 2018 : 0,33 / 1,45 / 3,5 / 6,5 / 8,76 / 10,85 / 11,2 Md€ de 2017 à 2023. Il s'agit de 11,2 Md€ à partir de 2023 ; l'évaluation préalable ne fournit pas elle-même ce consolidé.
- **Ex post** : somme calculée des mesures nouvelles « baisse du taux d'IS » en exécution, d'après les rapports Budget de l'État de la Cour, qui reprennent des chiffrages MEF/DB : 2017 : 0,3 ; 2018 : 1,2 ; 2019 : 0,8 ; 2020 : 2,5 ; 2021 : 3,7 ; 2022 : 2,9 ; 2023 : 0,3. Total : **11,7**. Écart de +4 %.
- **Vigilance** :
  - ce sont des chiffrages « à comportement constant » actualisés, pas une évaluation contrefactuelle ; la Cour (rapport de déc. 2024 sur la prévision des recettes 2014-2023, archivé) rappelle que la décomposition après LFI n'est pas publique ;
  - trajectoire intermédiaire modifiée : 2019 (grandes entreprises) et LFI 2020, d'où des incréments annuels différents ; le point d'arrivée (25 % en 2022) est le même ;
  - les effets du 5e acompte déplacent des montants entre années ;
  - aucune évaluation ex post du coût de la baisse du taux n'a été trouvée dans le rapport de la Cour sur la prévision des recettes, dans les pages ccomptes.fr du CPO (« Adapter l'IS… », « Quel taux pour l'IS en France ? », 2021, sans PDF exploitable) ni ailleurs. Le Sénat était inaccessible.
- Pas de nouvelle ligne d'effet (`is_pib` existe déjà).

## 6. Pacte de responsabilité et de solidarité : composante « allègements de cotisations 2015 » retenue (`pacte_2015`)

- **Ex ante** (étude d'impact du PLFRSS 2014, art. 2, lue sur la source primaire, assemblee-nationale.fr) :
  - baisse de la cotisation famille entre 1 et 1,6 Smic : −3 000 M€ (2015) ;
  - renforcement des allègements généraux : −400 et −1 000 M€ ;
  - famille des travailleurs indépendants : −1 000 M€ ;
  - « Coût total sécurité sociale avant compensation » : −5 400 M€ en 2015 (−5 550 en 2016, −5 850 en 2017).
- **Ex post** (PLFSS 2017, annexe 5, coûts 2015) :
  - baisse famille < 1,6 Smic : 3 589 M€ ;
  - famille des indépendants : 992 M€ ;
  - « hausse des allégements généraux d'environ 0,76 Md€ en 2015 ».
  - Total calculé : 5,34 Md€.
- **Vigilance** : la répartition interne diffère (famille 3,0 ex ante contre 3,59 ex post ; allègements 1,4 contre 0,76) en raison de l'interaction entre baisse famille et réduction générale. Seul le total est comparable. La colonne 2015 de l'annexe du PLFSS 2017 (oct. 2016) correspond à l'exécution, mais le tableau est présenté comme « évolution attendue entre 2015 et 2016 ».
- **Hors périmètre** : CICE (déjà dans le jeu de données), C3S (abattements 2015-2016, suppression 2017 abandonnée ; non trouvé ex post), surtaxe IS, étape 2016 de la baisse famille (1,6-3,5 Smic, pas d'ex ante primaire lu ; seul le PLFSS 2017 l'annonce à 2,9 Md€ en 2016 et 4,0 Md€ à partir de 2017). Le total famille 2017 en exécution (7,046 Md€, PLFSS 2019 annexe 5) a été vu mais non archivé ni utilisé.
- **Effet emploi du pacte** : non trouvé. Le rapport 2017 du COSAPE (France Stratégie) déclare ne pas produire de nouvelle évaluation quantitative. Pas de ligne d'effet.

## Fichier effets

`effets_C.csv` ne contient que l'en-tête : aucun effet n'a été à la fois annoncé et évalué parmi les candidats C. Les impôts de production n'ont pas d'évaluation causale ; le pacte n'a pas d'évaluation emploi trouvée.
