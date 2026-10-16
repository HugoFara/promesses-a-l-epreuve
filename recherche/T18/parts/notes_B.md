# T18, phase 1, groupe B : notes

Date d'accès des sources : 2026-10-16. Règles gelées au commit `0b4175f` (non modifiées). Fichiers : `cout_B.csv` (15 lignes), `sources_B.csv` (18 sources archivées dans `sources/T18/B/`). Pas d'`effets_B.csv` : aucun effet annoncé puis mesuré n'a été trouvé dans le groupe.

## 1. Bilan par règle

| Règle | `observe` | Tous types | Cible | Atteinte |
|---|---|---|---|---|
| Élasticité IS | 2 | 4 | 8 | non |
| Nouvelle assiette : risque juridique | 6 | 6 | 8 | non |
| Élasticité carburants | 0 | 2 | 8 | non |
| Élasticité électricité | 2 | 3 | 8 | non |

Aucune des quatre règles n'atteint 8 cas `observe`. Pour les accises (carburants, électricité), la raison est structurelle : la recette d'une hausse d'accise n'est jamais isolée de la ligne budgétaire ; la Cour publie seulement le chiffrage administratif des « mesures nouvelles » (calculé sur les volumes constatés, sans contrefactuel), alors que l'effet volume que la règle veut corriger se retrouve dans l'« évolution spontanée ». Les cas `observe` d'électricité ne sont possibles que lorsque la mesure domine la ligne (baisse de 2022, relèvement de 2025).

## 2. Cas retenus

Écart = (ex post central − ex ante) / ex ante, calculé.

| id | Règle pressentie | Ex ante | Ex post (bas-central-haut) | Écart | Type | Comportement ex ante | Réalisé publié |
|---|---|---|---|---|---|---|---|
| maj_is_5pct_2012 | IS | 1,4 | 0,9 | −36 % | observe | inconnu | 2013-05 |
| ce_is_15pct_2017 | IS | 4,7 | 4,9 | +4 % | observe | inconnu | 2018-05-23 |
| report_deficits_is_2012 | IS (assiette) | 1,0 | 1,2 | +20 % | reestimation | inconnu | 2013-05 |
| bmc_suppression_2012 | IS (assiette) | 0,05 | 0,5 | ×10 | reestimation | inconnu | 2013-05 |
| ttf_2012 | Nouvelle assiette | 0,53 | 0,2 | −62 % | observe | **oui** (élasticité −0,7) | 2013-05 |
| taxe_dividendes_3pct_2012 | Nouvelle assiette | 1,1 | 0 (net) | −100 % | observe | inconnu | 2020-04-28 |
| tsn_2019 | Nouvelle assiette | 0,4 | 0,3 | −25 % | observe | inconnu | 2020-04 |
| cri_2023 | Nouvelle assiette | 12,3 | 0,6-1,7-1,7 | −86 % | observe | inconnu | 2024-12-23 |
| ecotaxe_pl_2014 | Nouvelle assiette | 0,89 | 0 | −100 % | observe | inconnu | 2017-02-08 |
| contrib_stocks_petroliers_2012 | Nouvelle assiette | 0,55 | 0,55-0,6-0,65 | +9 % | observe | inconnu | 2013-05 |
| carbone_convergence_2018 | Carburants | 3,6 | 3,8 | +6 % | administratif | **non** (« consommation énergétique inchangée ») | 2019-05-15 |
| accise_gaz_bouclier_2024 | Carburants (gaz) | 1,9 | 1,3 | −32 % | administratif | inconnu | 2025-04 |
| ticfe_baisse_2022 | Électricité | 6,4 | 4,9-5,6-5,6 | −13 % | observe | inconnu | 2024-03-15 |
| ticfe_prolongation_2023 | Électricité | 2,8 (calculé) | 4,7 | +68 % | administratif | inconnu | 2024-04 |
| accise_elec_2025 | Électricité | 3,4 (calculé) | 4,2 (calculé) | +24 % | observe | inconnu | 2026-04 |

### Points de lecture

- **Élasticité IS et comportement inclus.** Aucun des chiffrages d'IS lus ne dit s'il intègre un effet de comportement : tous sont `inconnu`. L'étude d'impact de 2019 (trajectoire de l'IS, non retenue faute d'ex post) décrit une simulation sur les déclarations de 2017 avec une croissance du bénéfice de 5,3 % et 12 %, sans réaction des entreprises : c'est un chiffrage statique de fait, mais sans phrase qui le dise. L'hypothèse « double compte » de la consigne ne peut donc être ni confirmée ni écartée sur ces cas.
- **Sur les deux cas IS `observe`, les écarts vont dans des sens opposés** (−36 % en 2012, +4 % en 2017), comme pour les deux cas déjà présents (+50 % en 2013, −6 % en 2025). Le −36 % de 2012 coïncide avec une évolution spontanée de l'IS très inférieure à la prévision (−4,5 Md€, même page) : conjoncture plus que comportement.
- **Nouvelle assiette.** Les six cas `observe` ont des causes différentes : risque juridique réalisé (dividendes, rendement net nul), abandon politique (écotaxe), prix de l'énergie (CRI), assiette surestimée malgré une élasticité incluse (TTF), décalage d'encaissement (TSN), aucune (stocks pétroliers). La règle (décote de 0,8) les mélange ; à signaler à l'intégrateur.
- **TTF 2012** est le seul cas du groupe où le chiffrage avant adoption dit explicitement intégrer une réaction (élasticité −0,7 de l'assiette) ; le réalisé reste 62 % en dessous.
- **Taxe de 3 % sur les dividendes.** Le rendement brut a dépassé l'ex ante (≈ 1,8 Md€/an selon la Cour, contre 1,1), mais tout a été restitué (9,5 Md€ en 2017-2019). L'ex post retenu (0) est le net ; le brut est en note. Si l'intégrateur préfère le brut, l'écart devient +64 %.

## 3. Pistes suivies sans résultat retenu (non trouvé ou exclu)

| Piste | Statut | Où l'on a cherché |
|---|---|---|
| Hausse de la contribution exceptionnelle d'IS à 10,7 % (2014-2015) | ex ante seulement (+2,5 Md€, déjà relevé par `recherche/IS`) ; aucun réalisé isolé | Cour, RBDE 2014 et 2015 (archives `sources/IS`) |
| Inflexion de la trajectoire de l'IS pour les entreprises > 250 M€ (2019) | ex ante lu : 1,67 Md€ en 2019 (étude d’impact TSN, p. 26) ; aucun réalisé isolé | RBDE 2019 (tableau des mesures), NEB 2019 |
| Limitation de la déductibilité des charges financières (LFI 2013) | ex ante lu : 4 Md€ au PLF, 3,7 après amendement (NEB 2013 p. 19-20) ; pas de réalisé isolé | NEB 2013, RBDE 2013 |
| Réforme des acomptes d'IS des grandes entreprises (2013) | exclue : mesure de trésorerie (calendrier), pas de taux ni d'assiette | NEB 2013 (ex ante 1,0, moins-value 0,6) |
| Baisse des taux d'IS (PME 2017-2019, 33⅓ → 25 %) | exclue : déjà `is_25`, et seuls existent des chiffrages administratifs | — |
| Taxe de risque systémique (création 2011, doublement 2012) | doublement : 0,5 Md€ « rendement prévu » en 2012, mais pas une assiette nouvelle ; création 2011 : RBDE 2011 non lu | NEB 2012, NEB 2013 (« absence de montée en charge », −0,5 / −0,7 Md€, sans niveaux) |
| TTF 2013 (1re année pleine) | exclue : la Cour donne des écarts (−0,4 à −0,8 Md€ selon les pages) sans niveau prévu cohérent ; même mesure que `ttf_2012` | NEB 2013 p. 17-18, 25-26, 37, RBDE 2013 |
| CRI prolongée en 2024 | exclue : la recette 2024 (1,1 Md€) est surtout le solde de 2023 ; la Cour signale une erreur de prévision sur ce solde | NEB 2024 p. 33-40 |
| Taxe sur l'exploitation des infrastructures de transport de longue distance (2024) | non trouvée dans les NEB 2024 et 2025 | NEB recettes 2024 et 2025 |
| Taxe de 3 % sur les dividendes, rendement de la 1re année 2013 | « supérieur de 0,2 Md€ à la prévision », sans le niveau prévu | NEB 2013 p. 25 |
| Composante carbone 2014-2016, gazole +2 c€ (2015), convergence 2016 | réalisés seulement administratifs (RBDE 2015 : « gain total en 2015 de 2,0 Md€ » ; RBDE 2016 : 1,2 + 0,3) ; ex ante annuels du PLF 2014 non lus | RBDE 2015, 2016 ; CPO 2019 |
| Compensation de l'écotaxe par la TICPE gazole (2015) | ex ante lu : 1 139 M€/an « à législation constante et consommation constante » (RPA 2017 p. 214) ; aucun réalisé isolé | RPA 2017, RBDE 2015 |
| GNR : hausse non agricole 2024, hausse agricole 2024 non appliquée | réalisés administratifs (+0,1 ; mesure non appliquée) ; ex ante de l'évaluation préalable du PLF 2024 non lus | NEB 2024 p. 26-29 |
| Annulation de la hausse carbone 2019 | exclue : mesure annulée avant application (3,8 Md€ avec le GNR, RBDE 2019) | RBDE 2019 |
| Remise carburant 2022 | exclue par T10a (dispositif modifié quatre fois) ; pas de source nouvelle | — |
| Relèvement de la TICFE au 1er février 2024 | exclu : ex ante nul, « aucune hypothèse de hausse n'avait été intégrée » en LFI 2024 (NEB 2024 p. 40) ; recettes estimées à 3,5 Md€ en 2024 | NEB 2024 |
| CSPE (hausses 2011-2015) | non cherchée faute de quota ; c'était une contribution hors budget de l'État, chiffrée par la CRE | — |
| Bouclier électricité 2023 (CRE) | déjà `bouclier_elec` dans data/raw | — |

## 4. Accès aux sources

- **ccomptes.fr** : accessible avec curl. Les URL des notes d'exécution changent selon l'année (`sites/default/files/2023-10/…`, `system/files/2022-06/…`, `2025-04/…`) ; plusieurs essais renvoient une page HTML de 140 Ko au lieu du PDF (supprimés). Le rapport public annuel 2017 (9 Mo) a dû être téléchargé deux fois (première copie tronquée).
- **assemblee-nationale.fr** : accessible avec curl (PLFR2 2012, étude d'impact TSN, QE 44551). Le projet de LFR1 2017 n'a pas été trouvé (numéros 0234-0236, 0270, 0336-0342 et 0383-0385 essayés : autres textes ou 404).
- **budget.gouv.fr / performance-publique** (Voies et moyens tome I) : pas essayé, bloqué selon T10a ; cela empêche de lire l'exécution par ligne de la TSN (2020-2022) et de la TICFE.
- **senat.fr** : pas utilisé.
- Quota de recherche : 4 WebSearch utilisés.
- Huit fichiers déjà archivés par d’autres tâches (`sources/T10a`, `T10b`, `T2a`, `IS`) ont été copiés dans `sources/T18/B/` (sha256 recalculé).

## 5. Décisions laissées à l'intégrateur

1. **Accises** : seul le chiffrage administratif existe pour les hausses d'accise sur les carburants. Il faut soit accepter qu'« Élasticité carburants » reste non testable sur des cas `observe`, soit la tester sur la ligne budgétaire (prévision LFI de la TICPE contre exécution), ce qui mêle la mesure et la conjoncture.
2. **Nouvelle assiette** : la règle reçoit des cas dont l'écart vient d'une cause qu'elle ne vise pas (prix de l'énergie pour la CRI, abandon politique pour l'écotaxe). Faut-il restreindre son champ au risque juridique, ou garder « assiette nouvelle » quelle que soit la cause ?
3. **Taxe de 3 % sur les dividendes** : comparer le net (0, retenu) ou le brut (≈ 1,8) ?
4. **`ticfe_baisse_2022`** : quel ex ante retenir (5,1 pendant les débats, 6,4 en janvier 2022 pour la baisse au plancher, ou 8 « pour un an » selon la réponse ministérielle d'avril 2022) ? Le 6,4 a été retenu (même périmètre que le réalisé).
5. **`ticfe_prolongation_2023`** et **`accise_elec_2025`** : ex ante reconstitués par calcul (confiance low et medium). À écarter si l'on exige un ex ante lu.
6. **Mesures d'assiette d'IS** (`report_deficits_is_2012`, `bmc_suppression_2012`) : hors du champ strict de la règle (« taux de l'IS »). Gardées pour information, en `reestimation`.
7. **`contrib_stocks_petroliers_2012`** relève aussi de « Recette ponctuelle » (groupe D).
8. **Accise sur le gaz** : aucune règle ne la couvre. `accise_gaz_bouclier_2024` est classée sous « Élasticité carburants » par défaut.
