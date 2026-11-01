# T28 : les plans contre la fraude rapportent-ils ce qu'annonçait leur chiffrage ?

*État au 01/11/2026. Fichiers : `cas.csv` (5 cas nouveaux), `sources.csv` (21 fichiers archivés dans `sources/T28/`).*

## 1. Question et méthode

Le site divise par 3 les recettes annoncées des plans contre la fraude (`ens_fraude`, `rn24_fraude` : règle « Effet promis », facteur 0,333). Cette règle a été calibrée sur des promesses d'emploi (CICE, heures supplémentaires de 2007). On cherche ici des cas passés qui ont à la fois un chiffrage ex ante officiel des recettes et un réalisé de même périmètre.

`cas.csv` suit les colonnes de `data/raw/mesures_cout.csv`, sans colonne de règle. Il ajoute cinq colonnes en fin de ligne : `url`, `citation`, `page` (demandées par `recherche/CONSIGNES.md`, elles reprennent le réalisé), `ratio_realise_annonce` et `ecart_pct`. **Ces deux dernières colonnes, ainsi que `cause_principale`, `note` et les colonnes ex post, sont à retirer de la copie remise à l'agent qui attribuera les règles à l'aveugle.**

Déjà dans l'échantillon, donc non repris : la cellule de régularisation (`cellule_regul_2010`) et le STDR (`stdr_2014` à `stdr_2017`), dans `mesures_cout.csv`. Il y a aussi deux lignes de `mesures_effets.csv` sur la fraude, que la consigne ne citait pas :
- `fraude_lfi2013` : mesures contre la fraude de la LFI 2013, 1 Md€ annoncé, rendement nul selon la Cour (RBDE 2013, p. 88) ;
- `fraude_is_lfi2014` : volet IS de la lutte contre la fraude de la LFI 2014, 0,4 Md€ annoncé, rendement nul (RBDE 2014, p. 77).

Je les ai relues dans les RBDE déjà archivés (`sources/T18/A/`) et les compte dans le bilan ci-dessous.

## 2. Cas trouvés

| id | Annoncé | Réalisé | Nature du réalisé | Ratio réalisé / annoncé |
|---|---|---|---|---|
| `fraude_plan_2026` (FR) : « Lutte contre la fraude », PLF et LFI 2026 | 1,5 Md€ (PLF 2026, HCFP 2025-5 p. 17) | 0 : la mesure a « disparu » de la prévision 2026 révisée (HCFP 2026-5 p. 21) | reestimation (prévision révisée, année non close) | **0** |
| `urssaf_travail_dissimule_2023` (FR) : objectif de redressements de mai 2023 | 5 Md€ sur 2023-2027, soit 1,0 Md€/an | 4,3 Md€ fin 2025, soit 1,43 Md€/an (1,2 ; 1,6 ; 1,5) | observe (redressements constatés, **pas des encaissements**) | **1,43** (≈ 3,2 en écart à 2022) |
| `uk_accord_suisse_2013` (GB) : accord fiscal Royaume-Uni - Suisse | 3,45 Md£ cumulés à mars 2014 (prévision certifiée par l'OBR) | 1,074 Md£ (NAO, 2014), dont 0,808 de prélèvement encaissé | observe | **0,31** |
| `uk_mtd_tva_2019` (GB) : Making Tax Digital pour la TVA | 115 M£ en 2019-20 | 185 M£ (IC 95 % : -80 à 455) ; 195 M£ avec une autre méthode | reestimation (évaluation en doubles différences de HMRC) | **1,61** (1,70) |
| `uk_hmrc_conformite_sr2010` (GB) : réinvestissement de 917 M£ dans le contrôle (Spending Review 2010), année 2012-13 | +4 Md£/an de « compliance yield » | cible atteinte « almost exactly » une fois la base corrigée (NAO, 2014) | reestimation (indicateur estimé par HMRC) | **≈ 1,0** |
| *déjà dans l'échantillon* `fraude_lfi2013` (FR) | 1 Md€ | 0 | constat d'exécution (Cour) | **0** |
| *déjà dans l'échantillon* `fraude_is_lfi2014` (FR) | 0,4 Md€ | 0 | constat d'exécution (Cour) | **0** |

Pour mémoire, les régularisations déjà comptées ont rapporté plus que prévu : cellule de 2010, 0,9 / 0,7 = 1,29 ; STDR 2014, 1,7 / 1,0 = 1,7.

**Médianes** (calculées) :
- les 5 cas nouveaux : 0 ; 0,31 ; 1,0 ; 1,43 ; 1,61, médiane **1,0** ;
- les 7 cas (nouveaux et lignes `fraude_*` existantes) : médiane **0,31** ;
- les cas « observe » seuls : 2 nouveaux (0,31 et 1,43), 4 si l'on ajoute les deux constats d'exécution de la Cour (0 ; 0 ; 0,31 ; 1,43), médiane **0,16**.

Le facteur de la règle est de 0,333.

## 3. Ce que cela suggère, sans proposer de changement

On a **moins de 5 cas observés**. Cela ne suffit pas pour changer la règle, et ce rapport n'en propose pas.

1. **La médiane d'ensemble (0,31) tombe près de 1/3, mais par compensation.** Les ratios ne se regroupent pas autour de 1/3 : ils se partagent entre 0 et environ 1 ou plus. Un seul cas est proche de 1/3 (l'accord suisse).
2. **Deux groupes semblent se dessiner. C'est une piste, pas une conclusion.**
   - *Le montant global « lutte contre la fraude » inscrit en loi de finances*, sans mesure identifiée ni ventilation : 2013 (1 Md€), 2014 IS (0,4 Md€) et 2026 (1,5 Md€) ont un rendement nul ou retiré, soit 3 cas sur 3. La Cour (2013, 2014) et le HCFP (2025 : « ne paraît pas crédible » ; 2026 : « optimiste voire hypothétique ») l'avaient signalé. Pour ces lignes, la règle de 1/3 serait trop généreuse.
   - *Un dispositif précis, avec moyens ou outil identifiés et évalué à part* : MTD-TVA (1,6), réinvestissement de HMRC (1,0), objectif de redressements de l'Urssaf (1,4). Le réalisé atteint ou dépasse l'annonce. Pour ces cas, la règle de 1/3 serait trop sévère. Mais deux de ces réalisés sont des estimations de l'administration qui avait fait la prévision (`meme_auteur_ex_ante_ex_post`, `indicateur_administration`). Le troisième compte des redressements, pas des recettes.
   - Les lignes `ens_fraude` et `rn24_fraude` (3 Md€, sans ventilation par mesure) ressemblent au premier groupe. Je le signale à l'intégrateur sans en tirer de proposition.
3. **Redressé n'est pas encaissé.** En 2025, l'Urssaf a redressé 1,5 Md€ pour travail dissimulé, mais n'a recouvré que « près de 150 millions d'euros » au titre de la fraude. La DGFiP a notifié 17,1 Md€ et encaissé 11,4 Md€ (`idees_chiffres.csv`, `fraude_fiscale` lignes 1 et 2). Une promesse exprimée en montants détectés ou redressés n'a pas le même périmètre qu'une recette. Le ratio de 1,43 de l'Urssaf deviendrait bien plus faible en encaissements. Je n'ai pas trouvé d'objectif exprimé en encaissements pour faire la comparaison.
4. **Un réalisé de nature peu sûre.** Sur les 7 cas, seul l'accord suisse a un réalisé observé, encaissé et de même périmètre que l'annonce.

## 4. Pistes cherchées sans résultat utilisable

- **Loi n° 2018-898** : aucun chiffrage de recettes trouvé (recherche sur l'étude d'impact et les débats). Non retenue.
- **Plan de lutte contre toutes les fraudes de 2023, volet fiscal** : pas d'objectif de recettes chiffré trouvé (le bilan de mars 2024 donne des mises en recouvrement : 15,2 Md€ en 2023). Volet social : objectif CNAF et CNAV de 3 Md€ cumulés de préjudice détecté et évité sur 2022-2027 (discours du 20/03/2024, p. 4), et objectif de l'Assurance maladie de 2,4 Md€ sur 2024-2027. Ces cibles portent sur des montants détectés ; elles ne sont ni exploitées ni terminées.
- **LFSS 2023 à 2025** : aucune mesure de fraude n'apparaît avec un chiffrage dans les avis du HCFP de 2022 à 2025 (le mot « fraude » est absent des avis sur les PLF et PLFSS 2023, 2024 et 2025). L'Ondam intègre chaque année une ligne « maîtrise médicalisée et lutte contre la fraude » (0,9 Md€ en 2026, CCSS mai 2026), qui mélange les deux. Non exploitée.
- **LFR 1 de 2012** : « renforcement des actions de lutte contre la fraude (pour 0,3 Md€) » (RBDE 2012, `sources/T18/A/ccomptes_rbde_2012.pdf`). Réalisé non trouvé dans les RBDE 2012 et 2013.
- **LFR 1 de 2011**, « Lutte contre la fraude - Accords internationaux » : prévision de 254 M€ pour 2012 (annexe du RBDE 2011). Réalisé non trouvé.
- **LFI 2014, ensemble des impôts** (1,4 Md€ annoncés, 1,7 réalisés) : non repris, parce que le réalisé repose sur le seul STDR, déjà compté.
- **Data mining (CFVR)** : pas de chiffrage de recettes trouvé. Le seul écart publié (environ 20 M€ d'économies contre 46,6 M€ attendus, rapporté par la presse d'après la Cour) porte sur des gains de productivité, pas sur des recettes.
- **TVA du commerce électronique (2021)** : la Commission publie les montants collectés par les guichets OSS et IOSS, pas un supplément de recette. Seul chiffre de supplément : 1,4 Md€ par an pour l'UE, au titre de la suppression de la franchise de 22 €. Pas de chiffrage ex ante français ni européen de même périmètre trouvé.
- **Facturation électronique** : pas encore de réalisé. Le Gouvernement justifie par sa « mise en place » le 1,0 Md€ attendu pour 2027 (HCFP 2026-5, § 78) ; le calendrier de déploiement n'a pas été vérifié ici.
- **Italie, facture électronique de 2019** : la presse cite une prévision d'environ 2 Md€. Le réalisé du ministère italien (rapport sur l'évasion) n'isole pas l'effet de la mesure. Non retenue.
- **Royaume-Uni, OBR** : les encadrés qui évaluent les chiffrages anti-évasion et l'accord suisse (obr.uk) sont bloqués (Cloudflare, erreur 403). Ces encadrés pourraient fournir d'autres cas.

## 5. Points de vigilance et décisions laissées à l'intégrateur

- `fraude_plan_2026` : `inclus_stats` = 0 proposé, parce que l'année n'est pas close. À revoir au RBDE 2026 (vers avril 2027).
- `urssaf_travail_dissimule_2023` : il faut choisir entre l'objectif total (ratio 1,43) et l'écart à 2022 (ratio ≈ 3,2). Autre question : faut-il accepter un objectif de redressements comme chiffrage de départ ? Les chiffres de 2024 et 2025 viennent d'une source secondaire (Legisocial) ; urssaf.org n'a pas pu être téléchargé.
- `uk_accord_suisse_2013` : c'est une forme de régularisation, comme le STDR. L'intégrateur doit dire s'il relève de la même famille. L'ex ante a été lu dans le rapport du NAO, pas dans le document de l'OBR.
- `uk_mtd_tva_2019` : il vise l'erreur et la négligence plus que la fraude. Le chiffre de 115 M£ est peut-être un chiffrage révisé (non vérifié).
- `uk_hmrc_conformite_sr2010` : le réalisé est une phrase qualitative du NAO, convertie en 4,0. En 2014-15, la comparaison n'est pas possible sans retraitement, parce que la cible a été relevée et le périmètre élargi.
- Confiance : `high` pour l'accord suisse ; `medium` pour les quatre autres (motif dans `note_confiance`).
- Aucun fichier de `data/` ni de `scripts/` n'a été modifié. Rien n'a été commité.
