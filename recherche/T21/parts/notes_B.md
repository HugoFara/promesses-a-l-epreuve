# T21, groupe B : Effet emploi du SMIC, Taux d'intérêt (notes)

Date d'accès : 2026-10-20. Règles gelées au commit `686902b`. Fichiers : `cout_B.csv` (6 cas), `parametres_B.csv` (8 tests de paramètre), `sources_B.csv` (25 fichiers dans `sources/T21/B/`).

## 1. Ce que testent les règles

- **Effet emploi du SMIC** (`emploi_smic`) : montant = |eps_smic| × hausse_moy_smic × n_smic_tranche × cout_emploi_perdu. Paramètres gelés : eps_smic −0,6 (bas −0,17, haut −0,9) ; hausse_moy_smic 0,069 (haut 0,1439) ; n_smic_tranche 2,5 M (2,2-3,0) ; cout_emploi_perdu 16 175 € (15 131-17 219).
- **Taux d'intérêt** (facteur 1) : la ligne « spread × dette » est déjà calculée. Paramètres : spread_dette ≈3 pb par point de dette (jusqu'à 6) ; taux_100pb +3,2 Md€ à 1 an (19,1 à 5 ans, 32,6 à 9 ans).

Aucune hausse du SMIC n'a de chiffrage budgétaire avant adoption suivi d'un réalisé budgétaire. La règle ne peut donc être testée sur une mesure qu'en unités d'emplois (le montant est proportionnel aux emplois perdus). Ces cas sont à l'étranger et leur réalisé est une évaluation économétrique : `type_ex_post = reestimation`, aucun cas `observe`.

## 2. Cas de mesure (`cout_B.csv`)

| id | pays | type_ex_post | ex ante | ex post (central) | écart | réalisé publié |
|---|---|---|---|---|---|---|
| es_smi_2019_emploi | ES | reestimation | 40 000 emplois (AIReF, oct. 2018) | 49 500 (45 000-54 000, AIReF mai 2026) | +24 % | 2026-05-29 |
| de_mindestlohn_2015_emploi | DE | reestimation | 910 717 emplois (Knabe-Schöb-Thum, févr. 2014) | ≈76 500 (+11 000 à −200 000, synthèse IAB) | −92 % | 2019-12 |
| p117_2020 | FR | observe | 38,149 Md€ (LFI) | 35,8 | −6,2 % | 2021-04 |
| p117_2023 | FR | observe | 50,83 | 53,874 | +6,0 % | 2024-04 |
| p117_2024 | FR | observe | 51,37 | 49,268 | −4,1 % | 2025-04 |
| p117_2025 | FR | observe | 54,207 | 50,90 | −6,1 % | 2026-04 |

Par `type_ex_post` : 4 `observe` (FR, Taux d'intérêt, proxy) et 2 `reestimation` (ES, DE, Effet emploi du SMIC). Par pays : FR 4, ES 1, DE 1.

**Comparabilité.**
- Les cas `p117_*` sont un **proxy** (drapeau `proxy_charge_dette`) : prévision de la charge de la dette en LFI contre exécution. Ils ne contiennent pas d'effet « spread × dette ». Les écarts viennent des taux courts et de l'inflation (OATi), d'après la Cour. Ils disent seulement si un chiffrage d'intérêts pris tel quel (facteur 1) se réalise à quelques pourcents près. L'intégrateur peut les écarter s'il juge le périmètre trop éloigné de la règle.
- Les deux cas SMIC sont des prévisions d'effet emploi, pas des chiffrages statiques : `comportement_inclus_ex_ante = oui`. La question pour la règle est de savoir si l'élasticité appliquée était la bonne.
  - Espagne 2019 : la Banco de España (DO 1902, févr. 2019, après l'adoption du décret) projetait ≈125 000 emplois perdus avec une élasticité de −0,6 sur ≈1 million d'affectés. C'est exactement la valeur centrale gelée, appliquée sur le même périmètre (les affectés).
  - Contre l'ex post AIReF 2026, cette projection surestime de 60 %. Dans le même cadre, l'ex post correspond à une élasticité d'environ −0,22 à −0,27 (dérivation de l'agent : 0,625 × 45/125 et 0,625 × 54/125 ; confiance faible).
- Ex post espagnol : trois millésimes AIReF (19 000-33 000 en 2020 ; 40 000-65 000 en 2025 ; 45 000-54 000 en 2026). Le cas retient le dernier. Le choix du millésime change le signe de l'écart.
- Ex ante allemand : chiffrage universitaire (auteurs CESifo et ifo Dresde), pas administratif. Les mêmes auteurs simulaient un déficit public de 4,3 Md€/an (modèle standard). C'est le seul chiffrage budgétaire d'un effet emploi du salaire minimum trouvé, et il n'a pas de réalisé budgétaire.

## 3. Tests de paramètre (`parametres_B.csv`)

| paramètre gelé | valeur gelée | valeur trouvée | nature | pays | confiance |
|---|---|---|---|---|---|
| eps_smic | −0,6 (−0,17 ; −0,9) | −0,18, non significatif (hausse à 12 €, bunching) | ex post | DE 2022 | medium |
| eps_smic | idem | −0,17 own-wage, non significatif | ex post | UK 2016-2019 | high |
| eps_smic | idem | +0,476 own-wage | ex post | UK (LPC 2023) | high |
| eps_smic | idem | −0,3 à −0,5 sur les affectés (borne supérieure) | ex post | ES 2019 | high |
| eps_smic | idem | ≈ −1 (zéro charges 2009, baisse de coût) | ex post | FR | medium |
| cout_emploi_perdu | 16 175 € | ≈23 000 € (dérivé du Groupe d'experts 2025) | modèle | FR | low |
| spread_dette | 3 pb (jusqu'à 6) | ≈2 pb (1,2 à 7,7 dans la littérature citée) | économétrie 2000-2023 | zone euro | high |
| taux_100pb | 3,2 Md€ à 1 an | 3,2 Md€ à 1 an (23,5 à 5 ans ; 33,5 à 9 ans) | réestimation (même modèle AFT) | FR, PLF 2026 | medium |

**Lecture.**
- **eps_smic** : les estimations ex post de hausses du salaire minimum (DE, UK, ES) vont de +0,48 à −0,5, la plupart entre 0 et −0,2. Elles sont toutes moins fortes en valeur absolue que la valeur centrale gelée (−0,6), et proches de la borne basse (−0,17). La seule estimation à −1 est française, mais elle porte sur une baisse ciblée du coût du travail, pas sur une hausse du SMIC.
  - Le paramètre gelé est une élasticité au coût du travail. Les estimations étrangères sont des élasticités au salaire (own-wage), proches mais pas identiques, et à d'autres niveaux du salaire minimum par rapport au médian.
  - Le cas espagnol est le plus probant : une projection faite avec −0,6 sur les affectés a surestimé les pertes d'emplois d'environ 60 % (cout_B).
- **cout_emploi_perdu** : la simulation du Groupe d'experts implique ≈23 000 € par emploi, au-dessus de la valeur gelée. Elle porte sur des emplois jusqu'à plus de 1,2 SMIC et retient une allocation de 1 000 €/mois pendant un an. Ce n'est ni une observation ni un chiffre publié (dérivation de l'agent).
- **spread_dette** : estimation plus récente un peu plus basse (≈2 contre ≈3 pb), dans la fourchette de la littérature.
- **taux_100pb** : seulement une réestimation par le même modèle. **Aucun test ex post trouvé** (voir § 4).

## 4. Non trouvé (endroits cherchés)

- **Taux d'intérêt, test ex post de taux_100pb** : aucune publication qui confronte la sensibilité annoncée (+100 pb → +3,2 Md€ à 1 an) au surcoût constaté après la hausse des taux de 2022-2023. Endroits lus :
  - Cour des comptes, NEB Engagements financiers 2020, 2023, 2024, 2025 et NEB Gestion de la dette 2023, 2024 ;
  - Sénat, rapports PLF 2021, 2022, 2023, 2026 et loi de règlement 2022.
  - Ce qui existe seulement : une décomposition « effet volume / effet taux / effet inflation » de la variation annuelle. Pour 2023, effet taux +3,3 Md€, dont +4,6 Md€ via les BTF (NEB 2023 Gestion de la dette, p. 37). Pour 2024, effet taux −0,8 Md€. Ces chiffres ne sont pas rapportés à un choc de taux mesuré ; une dérivation serait fragile et n'a pas été faite.
- **spread_dette, test ex post propre à la France** : non trouvé.
  - Cherché : Banque de France, DG Trésor, FMI (Fiscal Monitor), BCE. Le document DG Trésor trouvé est la présentation de Pamies-Carnot-Patarau, c'est-à-dire la source du paramètre gelé : écarté.
  - Repère : spread OAT-Bund de 38 pb en moyenne en 2021, 56 pb en 2022 et 2023 (NEB 2023 Gestion de la dette, PDF p. 14). Non attribuable à la seule dette.
- **LFI du programme 117 en 2019, 2021 et 2022** : non retenues.
  - 2021-2022 : les rapports du Sénat donnent le PLF (38,66 Md€ pour 2022), un amendement de +1,1 Md€ et une hausse de « 31,5 % par rapport à la LFI 2022 » pour le PLF 2023 (50,83). Les deux dérivations de la LFI 2022 (38,65 ou ≈39,8) se contredisent.
  - Les NEB 2019, 2021 et 2022 sont introuvables (ccomptes.fr et web.archive.org).
- **SMIC, cas français** :
  - Le coup de pouce de juillet 2012 a un ex ante OFCE (≈1 400 emplois, vu seulement dans le résumé d'une recherche, non lu) mais aucune évaluation ex post trouvée.
  - Aucune évaluation ex post de l'effet emploi d'une revalorisation du SMIC trouvée (Insee, Dares, Groupe d'experts 2025).
  - Groupe d'experts 2025 : seulement des simulations et des évaluations d'allègements.
- **Allemagne, hausse à 12 € (2022)** : aucun chiffrage ex ante quantifié lu.
  - La présentation Knabe-Schöb (INSM) est inaccessible : DNS `preview.insm.de` en échec.
  - L'étude ZEW sur les effets budgétaires suppose un emploi constant.
  - Les ex post existent : 152 000-220 000 emplois (Georgieva-Hohendanner, via le rapport MLK p. 121) contre aucun effet significatif (Bossler et al.).
- **Royaume-Uni, NLW 2016** :
  - Ex ante OBR : chômage +60 000 en 2020 (EFO nov. 2015, encadré 3.2, lu via web.archive.org).
  - Ex post IFS : −0,1 % de l'emploi par hausse dans les régions à bas salaires, non significatif. Aucun effectif national publié : cas non construit.
- **Espagne 2023-2024** : ex post AIReF lus (50 000-61 000 et 78 000-90 000 emplois) ; ex ante non cherchés faute de temps, donc pas de cas.
- **n_smic_tranche, hausse_moy_smic** : aucune publication nouvelle trouvée. Pas de chiffre Dares pour les bénéficiaires de la revalorisation de janvier 2026 ; les médias reprennent 2,2 M (données 2024).
- **Caliendo et al. (2025), Georgieva-Hohendanner (2025)** : études primaires non lues (mindestlohn-kommission.de : 403). Lues via le 5e rapport de la commission.
- **Cahuc-Carcillo-Le Barbanchon (2019)** : article primaire non lu (REStud, accès payant).
- **Espagne, Casanova et al. (2025)** : élasticité propre citée par le Groupe d'experts, mais un chiffre manque à l'extraction du texte (« −0, ») : non retenue.

## 5. Sites inaccessibles

- ccomptes.fr et program-evaluation.ccomptes.fr : connexion réinitialisée (curl 35) après les premiers téléchargements. Suite via web.archive.org (`/web/2025id_/` ou `/web/2026id_/`).
- obr.uk : 403 (curl et WebFetch) ; encadré lu via web.archive.org.
- mindestlohn-kommission.de : 403 ; rapport lu sur la copie sozialpolitik-aktuell.de.
- airef.es : chaîne de certificats incomplète. Téléchargement avec `curl -k`, documents publics archivés avec sha256.
- preview.insm.de : nom de domaine non résolu.
- TU Dresde (bilan « fünf Jahre Mindestlohn ») : ECONNRESET.

## 6. Décisions laissées à l'intégrateur

1. **Cas SMIC en unités d'emplois.** Les accepter dans le test de la règle « Effet emploi du SMIC » (montant proportionnel aux emplois) ou les reverser en lignes d'effets (format `mesures_effets.csv`).
2. **Sous-échantillon étranger** (ES, DE), à garder séparé des cas français.
3. **Cas `p117_*` (proxy)** : les garder comme test « facteur 1 » d'une charge d'intérêts, ou les exclure faute de lien avec le spread.
4. **eps_smic** : toutes les estimations ex post de hausses du salaire minimum lues sont plus faibles que −0,6 en valeur absolue, et la projection espagnole faite avec −0,6 a surestimé les pertes d'environ 60 %.
   - À discuter, sans modification pendant la tâche : abaisser la valeur centrale vers la borne basse, ou dire que −0,6 vient d'élasticités au coût mesurées sur des baisses de cotisations.
   - Point de vigilance : les élasticités sont asymétriques (baisse de coût −1 contre hausse de salaire ≈ −0,2).
5. **cout_emploi_perdu** : la dérivation à ≈23 000 € suggère une sous-estimation de la valeur gelée. Elle est fragile (périmètre jusqu'au-delà de 1,2 SMIC) et doit être confirmée par une source qui publie le chiffre.
6. **Règles non testables par construction** : Règle d'or et Déjà dans la référence (consigne § 2). Ce groupe ne les a pas cherchées.
