# T20 : TVA et taxes sur la consommation, effet sur les foyers et sur le solde

Brouillon au 20/10/2026, après la fusion (étape 2 de la consigne). L'attribution à l'aveugle (étape 3) reste à faire. Consigne : `CONSIGNE.md`. Détail de la collecte : `parts/notes_A.md`, `notes_B.md`, `notes_C.md`. Rien n'est intégré à `data/`.

Règles gelées (§ 0) : les sha256 de `data/raw/regles.csv` et `data/raw/moteur_regles.csv` sont toujours ceux de la consigne. La règle T15 (version 0.1) n'est pas modifiée.

## 1. Fichiers produits par la fusion

| Fichier | Contenu | Origine |
|---|---|---|
| `repercussion.csv` | 36 lignes, colonnes et ordre de `data/raw/elasticites.csv` | `parts/repercussion_A.csv`, copié sans changement |
| `consommation.csv` | 5 755 lignes, colonnes du § 1 groupe B | `parts/consommation_B.csv`, copié sans changement |
| `mesures_cout_nouvelles.csv` | 7 lignes, colonnes de `recherche/T18/mesures_cout_nouvelles.csv` | `parts/cout_C.csv`, copié sans changement |
| `sources.csv` | 90 sources (A 24, B 40, C 26), colonnes `fichier,url,titre,date_acces,sha256` | fusion des trois `parts/sources_<G>.csv` |
| `aveugle/mesures_officielles.csv` | 7 lignes, colonnes exactes de `recherche/T18/aveugle/mesures_officielles.csv` | construit depuis `mesures_cout_nouvelles.csv` |
| `aveugle/regles_disponibles.csv` | copie identique de `recherche/T18/aveugle/regles_disponibles.csv` (vérifiée avec `cmp`) | |

Pas de `mesures_effets_nouvelles.csv` ni de fichier d'effets aveugle : le groupe C n'a trouvé aucune paire « effet annoncé chiffré / effet constaté » (`notes_C.md` § 1).

## 2. Contrôles de la fusion

### 2.1 Format et identifiants

- **En-têtes** : identiques aux formats demandés pour les trois fichiers.
- **Lignes** : aucune ligne de longueur incorrecte.
- **Identifiants** : tous uniques. Aucun ne figure déjà dans `data/raw/mesures_cout.csv`, `data/raw/mesures_effets.csv`, `data/raw/elasticites.csv`, `recherche/T18/mesures_cout_nouvelles.csv` ni `recherche/T18/mesures_effets_nouvelles.csv`.
- **Champs obligatoires** (`url`, `citation`, `page`, `confiance`, et les valeurs) : tous remplis. Une exception de fond, voir 2.3.
- **URL** : chaque URL citée dans les trois fichiers (y compris `source_ex_ante` et `source_ex_post` du groupe C) a son document archivé dans `sources.csv`.
- **Valeurs BdF 2017** : les 5 356 lignes `B_bdf17_TF10x_*` ont été comparées aux CSV archivés (`sources/T20/B/insee_bdf2017_TF10x.csv`), ligne par ligne. Toutes sont conformes (citation et valeur).

### 2.2 Sources

- 90 fichiers listés, 90 présents. Les 90 sha256 sont conformes à `sha256sum`. Aucun fichier manquant, aucun fichier archivé non listé.
- Toutes les dates d'accès sont le 2026-10-20.
- Format : `sources_A.csv` avait une sixième colonne `groupe`. Elle n'est pas reprise, pour s'en tenir aux cinq colonnes demandées ; le groupe se lit dans le chemin (`sources/T20/<G>/`).

### 2.3 Anomalies signalées (valeurs non corrigées)

1. **`rep_be_elec_hausse`** : `citation` vaut « Idem » (et `note_num` aussi). Le champ est rempli, mais ce n'est pas une citation. La phrase est celle de la ligne `rep_be_elec_baisse` (« both the tax cut and the tax hike were entirely shifted to the electricity price (i.e., 100%) »), qui couvre les deux sens. À recopier à l'intégration.
2. **Valeurs supérieures à 1** dans `repercussion.csv`, alors que la consigne demande une valeur entre 0 et 1 : `rep_biens_capital_baisse` (1,3 partout), `rep_imf_normal_lt` (haut 1,39), `rep_fr_carb_remise_2022` (haut 1,11), `rep_pt_alim_hausse` (haut 1,07), `rep_de_carb_essence_2022` (haut 1,05). Le groupe A les garde volontairement (sur-répercussion publiée). À l'intégrateur de dire s'il plafonne.
3. **Même étude déjà présente dans `data/raw/elasticites.csv`** (pas de doublon d'identifiant, mais un doublon de fond) :
   - `tva_asym` (Benzarti, Carloni, Harju, Kosonen, version 2020 : ≈ 13 % pour les baisses, ≈ 55 % pour les hausses) et `rep_ue_hausse_1m` / `rep_ue_baisse_1m` (même équipe, version NBER 2017 : 33 % et 6,3 % au premier mois). **Les chiffres diffèrent** selon la version et peut-être l'horizon. Le groupe A n'a pas lu la version publiée.
   - `tva_resto` (Benzarti-Carloni, ≈ 12 %) et `rep_resto_baisse_lt` (bas 0,135 tiré de la même étude, central 0,2 de l'Insee).
   - `tva_de` (Fuest et al., ≈ 70 %) et `rep_de_alim_baisse` (même étude, 0,7).
4. **`rep_fr_2014_prevision`** : c'est une prévision de l'Insee (type `hypothese_prevision`), pas une observation. Elle ne doit pas être comptée comme une mesure de répercussion.
5. **Écarts du groupe C** : recalculés comme (ex post central − ex ante) / ex ante. Ils sont tous conformes aux notes du groupe :

| id | ex ante | ex post central | écart recalculé | `type_ex_post` |
|---|---|---|---|---|
| `tva_7pct_2012` | 1,8 | 2,0 | +11,1 % | reestimation |
| `tva_resto_7pct_2012` | 0,34 | 0,3 | −11,8 % | reestimation |
| `tva_hausse_2014` | 5,2 | 4,9 | −5,8 % | reestimation |
| `tva_logement_social_10_2018` | 0,7 | 0,8 | +14,3 % | reestimation |
| `tva_presse_en_ligne_2018` | 0,15 | 0,15 | 0 % | administratif |
| `tva_zoos_2018` | 0,01 | 0,01 | 0 % | administratif |
| `tva_equitation_2024` | 0,065 | 0,049 | −24,6 % | reestimation |

6. **Dépendance** : `tva_resto_7pct_2012` est une composante de `tva_7pct_2012`. Les deux lignes ne sont pas deux cas indépendants. `tva_resto_7pct_2012` est aussi le même dispositif que `tva_resto_2009` (`data/raw/`), à une autre étape.
7. **Quatre chiffres cités par B ne sont pas cohérents entre eux** : taux d'épargne de Q5 dans le CPO 2015 (40,2 % dans le texte, 42,0 % dans le graphique) ; part de l'énergie de D1 et D10 (12,7 % et 9,5 % selon le CPO 2023, sans source ; 9,9 % et 6,8 % selon le calcul du groupe B sur TF106). Les deux versions sont dans le fichier, avec la confiance `medium`.

### 2.4 Fichier aveugle

- Colonnes : `id,mesure,annee,sens,indicateur,chiffrage_avant_adoption_md,auteur_du_chiffrage`. Ni réalisé, ni cause, ni note, ni citation de l'ex post.
- `mesure`, `annee`, `sens`, `indicateur` et le chiffrage sont repris tels quels. `auteur_du_chiffrage` est raccourci, comme dans T18 : les mentions « cité par la Cour des comptes » et « récapitulatif des mesures de TVA, Cour des comptes » sont retirées, car elles désignent le document qui contient aussi le réalisé.
- Contrôle automatique sur tous les champs, libellés compris : aucune valeur d'ex post qui diffère de l'ex ante, aucun mot qui renvoie au réalisé (« réalisé », « exécuté », « constaté », « écart », « moins-value », « reconduit », « Cour des comptes », « NEB », « RBDE », « au lieu de » sauf pour un taux). Seule occurrence : « au lieu de 20 % » dans `tva_equitation_2024`, qui décrit le taux, pas le résultat.
- Limite : pour `tva_presse_en_ligne_2018` et `tva_zoos_2018`, le réalisé est égal à la prévision. Le fichier aveugle n'en dit rien, mais l'agent d'attribution ne peut de toute façon rien en tirer.

## 3. Résultats par groupe

### Groupe A : répercussion sur les prix

36 lignes : 21 `high`, 15 `medium`. Restauration, services à forte main-d'œuvre, travaux, voitures, coiffure, électricité, énergie du logement, carburants, alimentation, toutes TVA confondues.

Valeurs françaises principales :

- **Restauration, baisse de 2009** : 0,21 à 2-5 mois, 0,20 à 1-2,5 ans (Insee F1404, `high`). Benzarti-Carloni : 13,6 % du gain aux consommateurs à 30 mois.
- **Électricité au tarif réglementé, 2025** : 1,0 (CRE, délibération 2025-155, `high`). C'est mécanique : la CRE fixe le tarif hors taxes, et les taxes s'ajoutent.
- **Carburants, remise de 2022** : 1,0 (0,999 à 1,11) en deux semaines environ (Drolsbach et al., `high`).
- **Services, 1995 et 2000** : 0,91 pour la hausse, 0,22 pour la baisse (Carbonnier, lu via l'Insee, `medium`).

Pas de chiffre français pour l'alimentation : les valeurs viennent du Portugal (0,998 à la baisse, 1,0 à la hausse), d'Espagne (0,90), d'Allemagne (0,70 / 0,35) et de l'ensemble de l'Europe (0,23 / 0,65).

**Deux familles de résultats ne disent pas la même chose** (`notes_A.md` § 2.1) :

- Les études qui portent sur **toutes les réformes ordinaires** de TVA en Europe trouvent une répercussion faible et asymétrique à court terme. Benzarti et al. (2017) : 33 % pour les hausses et 6,3 % pour les baisses au premier mois ; énergie du logement 92 % / 12 % ; essence 91 % / 16 %. Le FMI (2015) : 40 % / 24 % en cumul sur deux ans, sans asymétrie significative, mais environ 100 % pour le taux normal et 30 % pour les taux réduits.
- Les études récentes sur des **baisses ciblées, visibles et surveillées** trouvent une répercussion proche de 1 : carburants en France en 2022, alimentation au Portugal et en Espagne en 2023, électricité en Belgique. Le cadre y est particulier : obligation légale de répercuter en Espagne, remise versée aux distributeurs en France, forte inflation, attention politique.

Les deux mesurent des situations différentes. Le choix d'une valeur pour une promesse revient à décider à laquelle des deux situations la promesse ressemble. Ce choix n'est pas fait ici (§ 6).

Le sens de l'asymétrie n'est pas stable : plus forte pour les hausses selon Benzarti et al. et Carbonnier ; dans l'autre sens en Allemagne en 2021 ; absente selon le FMI et au Portugal.

### Groupe B : ce que consomment les foyers

5 755 lignes, recopiées des tableaux publiés, sans interpolation.

- **Dernière édition de Budget de famille : 2017** (collecte 2016-2017, résultats du 15/09/2020). L'édition 2026 est en cours de collecte depuis le 2 janvier 2026 et n'a aucun résultat.
- BdF 2017 : dépense par ménage en 180 postes, par décile de niveau de vie (TF106), par statut d'occupation × quintile (TF107), par type de ménage (TF105), par âge de la personne de référence (TF102). En euros 2017, TTC.
- Comptes nationaux distribués 2022 et 2023 (Insee) : consommation par unité de consommation, taux d'épargne, revenu par décile ; taxes sur les produits par vingtième (2023).
- Parts par taux de TVA : par décile seulement dans le CPO 2015 (BdF 2011, législation 2014), de façon indirecte ; pour l'ensemble dans André et Biotteau (Ines 2016) : taux normal 52,2 %, intermédiaire 13,3 %, réduit 15,4 %, 2,1 % 0,6 %, exonéré 18,5 %.
- Charge de TVA en part du revenu disponible : 12,5 % pour D1, 4,7 % pour D10 (CPO 2015). C'est la seule valeur de contrôle par décile.
- Énergie : dépense moyenne de 2 071 € pour le logement et 1 673 € de carburants par ménage en 2024 (SDES), avec la part des taxes. Pas de volumes.

### Groupe C : coût des changements de TVA passés

7 lignes : 6 changements distincts, plus une composante. **Aucun réalisé `observe`** : 5 `reestimation`, 2 `administratif`. La recette de TVA n'est jamais encaissée par taux. Écarts de −25 % à +14 %, de signe variable.

Exclus avec motif (`notes_C.md` § 2) : TVA « sociale » 2012 (abrogée avant d'entrer en vigueur), abonnements d'électricité et de gaz 2025 (réalisé lu, +0,5 Md€, mais ex ante non isolé), restauration 7 → 10 % en 2014 (réalisé non isolé), cinéma 2014, logement social et rénovation 2014 (dépense fiscale mesurée par rapport au mauvais taux), livres 2013, équidés 2013 (« non chiffrable »).

## 4. Ce qui n'a pas été trouvé

**Groupe A** (`notes_A.md` § 3) :

- hausse de TVA dans la restauration (2012, 2014) ;
- bilan ex post de la hausse de 2014 : seule la prévision de l'Insee a été lue ;
- gaz naturel seul ; électricité en offre de marché ;
- composante carbone de la TICPE (2014-2018) ;
- bouclier tarifaire 2022-2023 (hors mécanisme réglementaire) ;
- billetterie et services culturels ;
- évaluation CPO ou IPP de la TVA restauration.

Sites bloqués : HAL (anti-robot), fiscalcouncil.ie (403), PDF de Fuest et al. et de Hindriks-Serse. Plusieurs valeurs `medium` ne reposent que sur un résumé.

**Groupe B** (`notes_B.md` § 3) :

- part de la dépense par taux de TVA et par décile sur une enquête récente ;
- table de correspondance entre postes BdF et taux de TVA (non publiée) ;
- charge de TVA et d'accises par décile sur données récentes ;
- volumes d'énergie (kWh, litres) par décile ou type de ménage ;
- tableau croisé niveau de vie × composition × âge ;
- accises détaillées par décile ;
- taux d'épargne par décile récent ;
- publications IPP (TAXIPP) récentes.

**Groupe C** (`notes_C.md` § 2 et 3) :

- baisse du taux normal en 2000 et travaux à 5,5 % (PDF non extractible, OCR non fait) ;
- masques et gels (2020), protections hygiéniques (2016), billetterie (2012), livres numériques (2012), œuvres d'art (2015) ;
- tomes II des voies et moyens antérieurs au PLF 2025 : non obtenus. C'est la principale limite ; ils permettraient d'autres réestimations ;
- évaluations préalables du PLF 2014 (annexe séparée non trouvée).

## 5. Points de vigilance

1. **Répercussion** : deux familles de résultats en désaccord (§ 3, groupe A). Une valeur unique ne peut pas être présentée comme établie.
2. **Horizons courts** : la plupart des mesures valent pour 1 à 3 mois. Au-delà d'un an, seulement la restauration française, le FMI et la coiffure finlandaise.
3. **Études étrangères** : admises pour A, mais aucune donnée française sur l'alimentation.
4. **Versions** : Benzarti et al. lus dans la version 2017, alors que `data/raw/elasticites.csv` cite la version 2020 avec d'autres chiffres (§ 2.3, point 3).
5. **Concepts de consommation non comparables** : BdF compte par ménage, sans loyers imputés ; les comptes nationaux distribués comptent par unité de consommation, loyers imputés compris. Le taux d'épargne des plus modestes va de −29 % à +2,7 % selon la source.
6. **Données datées** : BdF 2017 a neuf ans. La structure des taux a changé depuis (abonnements d'énergie en 2025, par exemple).
7. **Retraités de 71 ans** : les tranches publiées sont 65-74 ans, 70 ans ou plus, ou 65 ans ou plus.
8. **Grille « sans loyer »** : le tableau BdF le plus proche est TF107 (propriétaires par quintile). Le poste loyers des propriétaires n'y est pas nul.
9. **Nature du réalisé de C** : aucun cas `observe`. Le classement n'est pas cohérent avec T18 et `data/raw/` (§ 6.5).
10. **`scripts/validation.py`** compte comme « réalisé observé » tout ce qui n'est pas `administratif` (`observe=r["type_ex_post"] != "administratif"`). Une ligne `reestimation` avec `inclus_stats = 1` y serait donc traitée comme une observation, alors que la consigne T18 (§ 1) dit que seuls les cas `observe` comptent. Les 7 lignes de C ont `inclus_stats = 0`. Le point compte si elles sont intégrées.

## 6. Décisions laissées à l'intégrateur et à l'utilisateur (§ 3 de la consigne)

Les éléments sont présentés. Rien n'est tranché.

### 6.1 Calcul par foyer

Ce serait un nouveau type de réforme dans `scripts/distributif.py`, écrit pour tous les partis. Il y a aujourd'hui quatre types (`parametre`, `option_bareme_capital`, `smic_net_cible`, `gel_pensions`), tous calculés par OpenFisca.

Ce qui manque pour passer de `consommation.csv` à la grille :

1. **Une table postes BdF → taux de TVA 2026**, à construire depuis le code général des impôts. Elle n'est pas publiée. L'annexe 5 du CPO 2015 n'a pas été trouvée, et le module « taxes indirectes » d'Ines n'est pas publié en table.
2. **Les seuils des déciles de niveau de vie BdF 2017**, pour situer chaque foyer de la grille. Ils n'ont pas été trouvés dans les fichiers archivés (`cad01_fe.xlsx` ne donne que des effectifs). Il faut aussi ramener le niveau de vie OpenFisca en euros 2017.
3. **Une convention pour combiner niveau de vie, composition et âge.** BdF ne publie que des tableaux séparés (TF106 ou TF107, TF105, TF102). Aucun tableau croisé n'existe.
4. **Les volumes d'énergie** (kWh, litres), pour appliquer une accise. Il n'y a que des montants TTC. Il faudrait des prix unitaires, non collectés.
5. **Des indices de prix 2017-2026 par poste**, pour ramener les montants en euros 2026. Non collectés.

Éléments pour la répercussion retenue (centrale et fourchette) : voir § 3, groupe A. Les valeurs vont de 0,06 (toutes baisses, Europe, premier mois) à 1,0 (baisses ciblées récentes, tarif réglementé). Pour l'électricité au tarif réglementé, la répercussion est mécanique (1,0). Pour la restauration française, la seule mesure est d'environ 0,2.

Contrôle disponible : la charge de TVA par décile du CPO 2015 (12,5 % pour D1, 4,7 % pour D10), et les taxes sur les produits par vingtième des comptes nationaux distribués 2023, qui sont une borne haute (notion plus large).

Le résultat peut être qu'un calcul par foyer n'est pas assez fiable pour être publié (consigne, § « Pourquoi cette tâche »). Les cinq manques ci-dessus pèsent dans ce sens.

### 6.2 Présentation

Trois options : afficher l'effet par les prix à côté de l'effet OpenFisca ; ne montrer qu'une fourchette ; continuer à classer ces mesures « non calculées ». L'écart entre les deux familles de répercussion (de 0,06 à 1) donnerait une fourchette très large pour une baisse de TVA ordinaire. Un effet par les prix serait moins précis que celui d'OpenFisca : il ne peut pas lui être additionné sans le dire.

### 6.3 Règle T15

Une version 0.2 pourrait rendre calculables tout ou partie des mesures `canal_prix` : `rn24_tva_carburants`, `rn24_tva_elec_gaz`, `rn24_tva_pn`, `l_gel`, `ens_elec`, `e_elec`, et l'idée `tva_alimentation`. Les candidats les mieux couverts sont l'électricité au tarif réglementé (répercussion mécanique, mais pas de volumes par foyer) et les carburants (répercussion de 2022 proche de 1, mais pas de volumes non plus). L'alimentation n'a pas de valeur française. Aucune proposition de texte n'est faite ici : elle demande d'abord les décisions 6.1 et 6.2. Si elle est faite, il faudra l'entrée de journal et la liste des programmes à refaire.

### 6.4 Solde : règle propre à `tva_produits`

Aucun cas `observe` dans le groupe C. Le seuil de 5 cas de `scripts/validation.py` (`MIN_CAS = 5`) n'est pas atteint, même avec `tva_resto_2009`. Avec les `reestimation`, on aurait 5 lignes, dont deux liées (`tva_7pct_2012` et sa composante) et une dont l'ex ante est postérieur au vote (`tva_equitation_2024`). Les écarts ne séparent pas la répercussion, les volumes et l'évolution spontanée de l'assiette. Ils ne disent rien d'une règle de comportement.

### 6.5 Classement `observe` / `reestimation` : incohérence avec T18 et `data/raw/`

Le groupe C classe `reestimation` (ou `administratif`) les montants « exécutés » de la Cour des comptes, parce que la recette n'est pas isolée par taux. Des chiffres de même nature sont classés `observe` ailleurs. Vérifié dans `data/raw/mesures_cout.csv` et `recherche/T18/mesures_cout_nouvelles.csv` (non modifiés) :

| Ligne | Fichier | Réalisé | Source du réalisé | Classement |
|---|---|---|---|---|
| `tva_resto_2009` | `data/raw/` | 3,3 Md€ | Rapport Thévenoud (2012) : « Le coût brut de cette dépense fiscale a atteint 3,3 milliards d'euros en 2010 et 2011 » | `observe`, `inclus_stats` = 1 |
| `tva_resto_7pct_2012` | T20 | 0,3 Md€ (différence de deux montants) | CPO 2015 reprenant Thévenoud : « Le coût brut de la dépense fiscale a été de 3,3 Md€ en 2010 et 2011 et de 3 Md€ […] en 2012 » | `reestimation` |
| `maj_is_5pct_2012` | `data/raw/` et T18 | 0,9 Md€ | Cour, NEB « Les recettes de l'État » 2012, tableau p. 32 (« 1,4 \| 0,9 \| -0,5 ») | `observe` (`inclus_stats` = 0 dans `data/raw/`, 1 dans T18) |
| `report_deficits_is_2012` | `data/raw/` et T18 | 1,2 Md€ | **même tableau**, même page (« 1,0 \| 1,2 \| 0,2 ») ; note : « chiffrage de la DGFiP, pas une recette isolée » | `reestimation` |
| `cef_2012` | `data/raw/` et T18 | 2,33 Md€ | Cour, budget de l'État 2013, p. 82 | `observe`, `inclus_stats` = 1 |
| `tva_7pct_2012` | T20 | 2,0 Md€ | Cour, NEB 2012 p. 33 et RBDE 2012 : « a procuré une recette supplémentaire de 2,0 Md€ » | `reestimation` |
| `tva_hausse_2014`, `tva_logement_social_10_2018` | T20 | 4,9 et 0,8 Md€ | Cour, NEB 2014 et 2018, montants exécutés d'après la direction du budget | `reestimation` |

Ce que montre le tableau :

- **Même phrase, deux classements.** Le réalisé de `tva_resto_2009` (`observe`) et celui de `tva_resto_7pct_2012` (`reestimation`) viennent de la même phrase de Thévenoud sur le coût de la dépense fiscale. Un chiffrage de dépense fiscale est une estimation, pas une recette constatée. Le classement `observe` de `tva_resto_2009` est donc celui qui s'écarte de la définition de T18 (§ 1 : « recette ou dépense effectivement constatée »).
- **Même tableau, deux classements, déjà dans T18.** `maj_is_5pct_2012` (`observe`) et `report_deficits_is_2012` (`reestimation`) sont deux lignes du même tableau de la NEB 2012. L'incohérence ne vient donc pas seulement du groupe C.
- **Une distinction possible, non écrite.** `cef_2012` et `maj_is_5pct_2012` sont des contributions déclarées et payées à part. Leur recette peut être isolée, au moins en principe. Une mesure de taux de TVA, une limite de report de déficits ou un taux réduit ne le sont pas. Ce critère (« recette isolable ou non ») expliquerait la plupart des classements, mais pas celui de `tva_resto_2009`. Il n'est écrit nulle part.
- **Conséquence.** Si l'on suivait le critère de T18 et `data/raw/` pour la Cour, `tva_7pct_2012`, `tva_hausse_2014` et `tva_logement_social_10_2018` pourraient passer `observe`, et peut-être `tva_resto_7pct_2012` par analogie avec `tva_resto_2009`. Le compte de cas `observe` de la famille `tva_produits` passerait de 0 à 3 ou 4 (5 avec `tva_resto_2009`, mais avec deux lignes liées). Si l'on suivait le critère du groupe C, `tva_resto_2009` et peut-être `maj_is_5pct_2012` devraient passer `reestimation`, ce qui changerait la statistique publiée.
- S'y ajoute le point de vigilance 10 (§ 5) : `scripts/validation.py` traite `reestimation` comme une observation.

Une règle de classement commune est à fixer par l'utilisateur. Rien n'a été modifié dans `data/raw/` ni dans T18.

## 7. Critères de réussite (§ 4 de la consigne)

| Critère | Atteint ? | Détail |
|---|---|---|
| Au moins une répercussion `high` ou `medium` pour l'énergie | **Oui** | `high` : CRE 2025 (électricité, tarif réglementé), Drolsbach et al. (carburants France 2022), Benzarti et al. (énergie du logement, essence), Montag et al. ; `medium` : Belgique, Allemagne 2022, États-Unis. Pas de valeur pour le gaz seul. |
| Au moins une répercussion `high` ou `medium` pour l'alimentation | **Oui** | `high` : Portugal 2023-2024, Benzarti et al. (COICOP 01) ; `medium` : Espagne 2023, Allemagne 2020-2021. Aucune valeur française. |
| Une structure de consommation par décile et par type de ménage, d'une enquête datée | **Oui** | BdF 2017 (collecte 2016-2017) : TF106 par décile, TF105 par type de ménage. Tableaux séparés, non croisés, et sans répartition par taux de TVA. |
| Au moins 5 changements de TVA avec chiffrage et réalisé | **Oui, de justesse** | 6 changements distincts (7 lignes). 0 `observe`. 4 seulement si l'on exige un ex ante antérieur au vote et un réalisé distinct de la prévision. |

Les trois critères sont atteints au sens littéral. Ils ne suffisent pas, à eux seuls, à rendre un calcul par foyer publiable (§ 6.1), ni à juger une règle `tva_produits` (§ 6.4).

## 8. Attribution à l'aveugle

Faite le 20/10/2026 par un agent neuf, sans web, sur une copie de `aveugle/` placée hors du dépôt. Sortie : `attribution_agent.csv`, conservé tel quel.

- **Les 7 lignes reçoivent la règle `Aucune`** : changements de taux ou d'assiette de TVA sur des assiettes existantes, chiffrés sans effet de comportement annoncé. C'est aussi la `regle_pressentie` du groupe C.
- **`issue_connue` = `non` pour les 7 lignes.** Pour `tva_hausse_2014`, l'agent signale un vague souvenir de recettes de TVA 2014 plus faibles que prévu dans l'ensemble, sans souvenir du rendement de la mesure elle-même.
- **Hésitation** : pour les hausses de 2012 et de 2014, l'agent a hésité avec `Effet promis` (baisse possible de la consommation). Il a gardé `Aucune`, faute de règle propre à la TVA dans `regles_disponibles.csv`.

Conséquence : ces cas ne testent aucune règle de correction. Avec la règle `Aucune`, la prédiction est le chiffrage lui-même. Ils mesurent seulement l'erreur des chiffrages mécaniques de TVA : de −25 % à +14 % sur 6 changements distincts, et 0 % pour les deux réalisés `administratif`, qui reprennent la prévision.

## 9. Intégration (20/10/2026)

Décisions prises par l'utilisateur le 20/10/2026 : intégrer les données, corriger la convention `observe` / `reestimation`, calculer l'effet par les prix.

**Données** (`data/raw/`, journal dans `historique.csv`) :

- `elasticites.csv` : les 36 répercussions (`rep_*`), domaine « Entreprises et consommation ». Les mentions « Idem » de la méthode, de la citation et de la note sont remplacées par le texte de la ligne précédente ; la méthode d'origine est gardée dans `note_num`.
- `mesures_cout.csv` : les 7 changements de TVA, avec `selection` = `test_regles` et `inclus_stats` = 0 (aucun réalisé observé), `deflateur_ex_ante` = 1 (montants de la même année).
- `validation_attribution.csv` : `attribution_agent.csv` copié tel quel.
- `consommation_menages.csv` (nouveau) : extrait de `consommation.csv` (énergie : postes 045, 0450 à 0453, 0722 du BdF 2017 par décile et par type de ménage ; dépenses moyennes SDES 2024).
- `parametres_bareme.csv` : seuils de déciles de niveau de vie 2024 (`nv_d1` à `nv_d9`, Insee).
- `parametres_bareme.csv` (et non `moteur_parametres.csv`, dont le moteur tire tous les paramètres au sort : y ajouter une ligne décale ses tirages) : `rep_energie_logement_baisse` (0,12 / 1 / 1) et `rep_carburants_baisse` (0,16 / 1 / 1). Règle, la même pour tous : central = estimation française `high` pour le même produit et le même sens ; bas et haut = plus basse et plus haute estimation `high` du même groupe de produits et du même sens, plafonnées à 1.
- `distributif_reformes.csv` : type `prix` et colonne `repercussion` ; trois mesures (RN 2024 : TVA à 5,5 % sur les carburants et le fioul, sur l'électricité et le gaz ; Ensemble 2024 : accise sur l'électricité maintenue au tarif réduit, avec la même variation de prix `dp_elec` que le chiffrage du solde).

**Convention `type_ex_post`** : définie dans `recherche/validation/README.md`. `scripts/validation.py` ne juge plus une règle que sur les cas `observe` (avant : tout sauf `administratif`). `tva_resto_2009` passe en `reestimation` (`recherche/T20/corrections_convention.csv`). Les autres lignes signalées au § 6.5 respectent la convention : `maj_is_5pct_2012` et `cef_2012` sont des prélèvements déclarés à part (`observe`), `report_deficits_is_2012` est fondu dans l'IS (`reestimation`). Effet sur les statuts : « Substitution retraites » passe de 2 cas à 1 (`retraites_2023`, réestimation, écartée). La statistique principale de la couche 1 n'est pas modifiée : elle mesure l'erreur des chiffrages de départ et garde, comme avant, les réalisés administratifs signalés.

**Calcul par les prix** (`scripts/distributif.py`, type `prix`) : gain = − dépense du poste × variation du prix TTC × répercussion (bas, central, haut). Dépense = BdF 2017 (décile de niveau de vie) × rapport du type de ménage à la moyenne (TF105) × dépense moyenne SDES 2024 / dépense moyenne BdF 2017. Le décile vient du revenu disponible OpenFisca divisé par les unités de consommation (`unites_consommation`, échelle Insee), comparé aux seuils 2024. Électricité et gaz non dissociables (0450) : comptés en entier si les deux énergies sont visées, au prorata sinon. Le résultat est affiché à part du revenu disponible, comme une baisse de dépenses, avec sa fourchette.

Limites : séparabilité décile × type (les deux se recoupent), pas d'effet propre de l'âge (les retraités de 65 à 74 ans dépensent moins en carburants : 932 € contre 1 108 € en moyenne, TF102), seuils 2024 appliqués à des revenus de 2026, structure de 2017. Contrôle d'ordre de grandeur : environ 450 € par ménage moyen pour les deux mesures RN, soit ≈ 13 Md€ pour l'ensemble des ménages, à comparer aux 16,7 Md€ bruts de l'iFRAP qui couvrent aussi les autres consommateurs (`chiffrages_instituts.csv`).

**Règle T15** : version 0.2 (exception « prix »), voir le journal de `recherche/T15/regle_selection.md`.

**Inventaire des mesures ménages (T15 § 8)** : les trois programmes 2024 sont inventoriés de la même façon, à partir des synthèses et fiches de l'Institut Montaigne lues sur web.archive.org (le site renvoie 403) : RN 23 mesures, Ensemble 18, NFP 42 (`recherche/T20/integration/inventaire_*.csv`). Un second codeur, sans les verdicts du premier ni accès au web, a recodé les 83 mesures : accord 74/83 (RN 22/23, Ensemble 15/18, NFP 37/42). Les 9 désaccords sont arbitrés, avec leur motif, dans `codage_final.csv` ; aucun ne fait passer une mesure de « non calculée » à « calculée ». Cas sensible : la « taxe Macron » du NFP (accise sur l'électricité) reste non calculée (`imprecise` : ni tarif ni énergies visées), alors que l'accise réduite d'Ensemble est calculée (variation de prix fixée) ; les deux codeurs ont fait ce choix séparément. `non_chiffre_foyer.csv` passe de 7 lignes NFP à 79 lignes pour les trois partis (plus les 5 lignes du gouvernement, inchangées). En attente d'une décision de l'utilisateur : la part fiscale entière dès le 2e enfant (RN), calculable si l'on garde le plafond actuel du quotient familial, sinon `imprecise` ; affichée pour l'instant « Pas encore simulé ».
