# T18, phase 2 : fusion, contrôles et fichiers aveugles

Fusion faite le 16/10/2026, à partir de `parts/` (non modifié). Règles gelées au commit `0b4175f`. Cette phase ne fait **pas** l'attribution des règles (phase 3). Elle ne calcule pas non plus la statistique « avant et après la règle », qui dépend de cette attribution.

## 1. Fichiers produits

| Fichier | Contenu |
|---|---|
| `mesures_cout_nouvelles.csv` | 55 lignes. Colonnes de `cout_<G>.csv` (celles de `data/raw/mesures_cout.csv` puis celles du § 4 de la consigne), plus `groupe` et `drapeaux` |
| `mesures_effets_nouvelles.csv` | 15 lignes. Colonnes de `effets_<G>.csv`, plus `groupe` et `drapeaux` |
| `sources.csv` | 83 sources : fusion des quatre `sources_<G>.csv`, plus `groupe` |
| `aveugle/mesures_officielles.csv` | 55 lignes, aux colonnes exactes de `recherche/validation/aveugle/mesures_officielles.csv` |
| `aveugle/effets_annonces.csv` | 15 lignes, aux colonnes exactes de `recherche/validation/aveugle/effets_annonces.csv` |
| `aveugle/regles_disponibles.csv` | Copie identique de `recherche/validation/aveugle/regles_disponibles.csv` (vérifiée avec `cmp`) |

**Colonne `groupe`** : `A`, `B`, `C` ou `D`. Une ligne fusionnée porte les deux groupes (`A;D`, `B;D`).

**Colonne `regle_pressentie`** : pour une ligne fusionnée, elle porte les règles pressenties des deux groupes, séparées par « ; ». La première est celle de la ligne gardée.

**Colonne `drapeaux`** : liste séparée par « ; ». Elle signale des réserves de fond. Aucune ligne n'a été supprimée pour un motif de fond : c'est à l'utilisateur de décider (§ 6).

| Drapeau | Sens |
|---|---|
| `low` | Confiance `low` |
| `credit_vote` | Ex ante = crédits votés, enveloppe ou trajectoire budgétaire, pas un chiffrage de la mesure |
| `ex_ante_secondaire` | Ex ante lu chez un tiers (Cour, rapporteur, CPO), pas dans le document de son auteur |
| `ex_ante_presse` | Ex ante lu seulement dans la presse spécialisée |
| `ex_ante_reconstitue` | Ex ante reconstitué a posteriori par la Cour |
| `ex_ante_tardif` | Ex ante fixé en cours de réforme (CMPP 6 de décembre 2011 pour la RGPP) |
| `ex_ante_calcule`, `ex_post_calcule` | Valeur obtenue par calcul (somme, différence) |
| `ex_post_lecture` | Central qui dépend d'une lecture de la source (indemnité carburant : 277 ou 433 M€) |
| `ex_post_net_vs_brut` | Choix entre net et brut (taxe de 3 % : 0 net, ≈1,8 brut) |
| `ex_ante_conteste`, `ex_post_central_conteste` | Les deux groupes ont retenu des valeurs différentes (§ 4) |
| `annee_differente` | L'ex ante et l'ex post ne portent pas sur la même année ou la même période |
| `hors_champ_strict` | Hors du champ littéral de la règle pressentie |
| `champ_mixte` | Mesure à cheval sur deux règles |
| `regle_absente_aveugle` | La règle pressentie n'existe pas dans `regles_disponibles.csv` (§ 5.4) |
| `autre_regle_possible:<règle>` | Une autre règle est suggérée par l'agent de collecte |
| `meme_dispositif:<id>` | Même dispositif qu'une autre ligne, y compris de `data/raw/` |
| `meme_plan:<plan>` | Même plan et même tableau source |
| `chevauchement:<id>` | Ex post qui inclut peut-être l'effet d'une autre ligne |
| `lie_a:<id>` | Mesures liées sans être le même dispositif |
| `tresorerie` | Avance de trésorerie |
| `recette_perenne_ensuite` | Recette « exceptionnelle » rendue pérenne ensuite |
| `exclu_T10a_motif_leve` | Piste écartée par T10a ; le groupe C juge le motif levé |
| `effet_volume` | Effet qui compte des recours plutôt qu'un effet économique |
| `stock_vs_flux` | Ex ante en flux, ex post en stock |
| `ratio_indicatif` | Ratio donné à titre indicatif |
| `ex_post_simule` | Ex post obtenu par simulation |
| `ex_post_execution` | Ex post = constat d'exécution |
| `annonce_post_adoption` | Annonce publiée après le vote |
| `annonce_non_chiffree` | Annonce sans chiffre |
| `annonce_implicite` | Annonce implicite |

## 2. Lignes avant et après fusion

| | Avant | Après | Écart |
|---|---|---|---|
| Coûts (`cout_A` 20, `cout_B` 15, `cout_C` 13, `cout_D` 12) | 60 | 55 | −5 (fusions) |
| Effets (`effets_A` 1, `effets_C` 2, `effets_D` 12) | 15 | 15 | 0 |
| Sources | 83 | 83 | 0 (aucune n'est dédoublonnée : les copies entre groupes gardent chacune leur ligne) |

Nature des 55 lignes de coût :

- `type_ex_post` : 43 `observe`, 8 `reestimation`, 4 `administratif` ;
- confiance : 8 lignes `low` ;
- date de publication du réalisé : **une seule** en 2026 (`accise_elec_2025`, avril 2026), aucune parmi les effets. Le sous-échantillon « réalisé publié en 2026 » de la consigne ne comptera donc qu'un cas.

## 3. Cas par règle pressentie (après fusion)

Les comptes portent sur les **nouvelles** lignes de T18.

- **Règles multiples.** Une ligne fusionnée qui porte deux règles compte pour chacune. La colonne « dont 1re règle » ne compte que la règle de la ligne gardée.
- **Dispositifs distincts.** Un dispositif sur plusieurs années ou sous plusieurs paramètres compte pour un :
  - STDR 2014 à 2017 : 1 ;
  - bouclier fiscal à 60 % (2007), renforcé à 50 % (2008), supprimé (2012) : 1 ;
  - quotient familial 2013 et 2014 : 1 ;
  - TICFE 2022 et 2023 : 1 ;
  - chèque énergie 2018 et 2019 : 1.

  Les trois aides de #1jeune1solution, et l'ISF 2013 (réforme et plafonnement), restent comptés comme des mesures distinctes, mais ils sont liés (§ 6).

| Règle pressentie | `observe` (lignes) | `observe` (dispositifs) | Tous types (lignes) | Tous types (dispositifs) | Cible 8 `observe` | Cas déjà présents (consigne, § 2) |
|---|---|---|---|---|---|---|
| Élasticité patrimoine | 7 | 5 | 7 | 5 | non | 5 |
| Élasticité revenus | 4 (dont 2 `hors_champ_strict`) | 4 | 6 | 5 | non | 1 |
| Élasticité capital | 2 | 2 | 4 | 4 | non | 1 |
| Élasticité succession | 2 (dont 1 `hors_champ_strict`) | 2 | 3 | 3 | non | 0 |
| Élasticité IS | 2 | 2 | 4 (dont 2 `hors_champ_strict`) | 4 | non | 1 |
| Nouvelle assiette : risque juridique | 6 | 6 | 6 | 6 | non | 1 |
| Élasticité carburants | 0 | 0 | 2 | 2 | non | 0 |
| Élasticité électricité | 2 | 1 | 3 | 1 | non | 0 |
| Taux de recours | 10 | 9 | 10 | 9 | **oui** | 8 (restreinte) |
| Réforme structurelle | 1 | 1 | 3 | 3 | non | 2 |
| Recette ponctuelle | 12 (dont 1re règle : 7) | 9 (dont 1re règle : 4) | 12 | 9 | oui en lignes et en dispositifs si l'on compte les 5 lignes fusionnées ; non sur la 1re règle seule | 0 |

**Effets (`mesures_effets_nouvelles.csv`)** : 15 lignes.

- **Effet promis** : 12 lignes, dont 4 marquées `effet_volume` et 3 `low`. Elles portent sur 9 dispositifs (CIR, CICE et PreParE ont chacun 2 lignes).
- **Taux de recours** : 2 lignes.
- **Élasticité patrimoine** : 1 ligne.

**Critère de réussite de la consigne.**

- *8 cas `observe` pour au moins 6 des 10 règles A-C* : **non atteint**. Une seule règle sur 10 l'atteint (Taux de recours, 10 lignes, 9 dispositifs).
  - Si l'on ajoute les 5 cas déjà présents donnés par la consigne, Élasticité patrimoine passe à 12 lignes, ou 10 en dispositifs distincts. Recette ponctuelle, qui n'avait aucun cas, n'atteint 8 que si l'on compte les lignes fusionnées.
  - Ce cumul n'a pas été vérifié ligne à ligne contre `data/raw/` : il est laissé à l'intégration.
- *Au moins 15 nouvelles lignes d'effets* : **atteint de justesse**, avec 15 lignes tous groupes confondus. Le groupe D seul en apporte 12, et 4 lignes sont des effets de volume.

**Non testables** (consigne, § 2), aucun cas cherché : Effet emploi du SMIC, Taxe sur les rachats d'actions, Règle d'or, Taux d'intérêt, Médiane des estimations, Déjà dans la référence. Aucun cas étranger n'a été signalé : il n'y a aucun fichier `parts/<G>_etranger.md`.

## 4. Fusions, suppressions et doublons gardés

### 4.1 Fusions (5 lignes supprimées, les informations utiles sont reportées en `note`)

| Ligne gardée | Ligne supprimée | Motif |
|---|---|---|
| `cef_2012` (A) | `ce_fortune_2012` (D) | Même mesure, même indicateur, même ex ante (2,325). Central A de 2,33 (RBDE 2013) ; le central D de 2,3 est arrondi. La durée réelle (une seule année) est reportée en note |
| `cehr_2012` (A) | `cehr_2012` (D) | Même mesure, même indicateur, **même id**. **Ex ante divergent** : A lit 0,4 Md€ pour le dispositif voté (AN n° 1328, p. 96) ; D calcule 0,6 (0,2 au PLF + 0,4 en LFI, d'après la Cour). Le réalisé est de 0,63 pour A et de 0,6 pour D (« conforme à la prévision », Cour). La ligne A est gardée parce que son ex ante est lu et non calculé. Écart : +58 % (A) ou 0 % (D). Drapeau `ex_ante_conteste` |
| `ce_is_2017` (D) | `ce_is_15pct_2017` (B) | Mêmes valeurs (4,7 et 4,9). La ligne D est gardée parce que son ex ante est lu dans le rapport AN n° 376, alors que B le lit de seconde main dans la Cour. Les remarques de B (reliquat de 0,4 Md€ en 2018, fin de la contribution, compensation de la censure de la taxe de 3 %) sont reportées en note |
| `cri_2023` (B) | `cri_2023` (D) | Même mesure, même ex ante (12,3), **même id**. Les deux lignes ne diffèrent que par le central : 1,7 (total dû au titre de 2022-2023, que la Cour juge « plus juste ») ou 0,6 (rendement budgétaire 2023). Chacune avait l'autre valeur en borne. Ce ne sont pas deux indicateurs distincts, mais deux lectures d'une même comparaison : une seule ligne est gardée, avec le drapeau `ex_post_central_conteste`. Écart : −86 % (B) ou −95 % (D) |
| `contrib_stocks_petroliers_2012` (B) | `ce_petrolier_2012` (D) | Même mesure, même indicateur, même ex ante (0,55). La ligne B est gardée (deux primaires lues, `high`). Le central D de 0,55 (contrecoup 2013) est reporté en note. Écart : +9 % (B) ou 0 % (D) |

### 4.2 Doublons apparents gardés (indicateurs ou mesures réellement différents)

- **`maj_is_5pct_2012` (B) et `ce_is_anticipe_2012` (D)** : ce sont deux mesures distinctes.
  - La première est le rendement 2012 de la contribution de 5 % (1re année) : 1,4 → 0,9.
  - La seconde est le versement anticipé en 2012 de la contribution due en 2013, voté en LFR 2 2012 : 0,8 → 1,0.
  - Les deux sont gardées, avec des drapeaux `meme_dispositif` croisés. Elles visent aussi `ce_is_5pct_2013` de `data/raw/` (2e année : 0,8 → 1,2).
  - **Risque de double compte à vérifier** : les 1,2 Md€ de 2013 s'entendent-ils avant ou après l'imputation de l'avance de 0,8 versée en 2012 ? La source n'a pas été relue sur ce point.
- **`ticfe_prolongation_2023` (B) et `bouclier_elec` (`data/raw/`)** : même bouclier tarifaire 2023, mais deux instruments différents.
  - La ligne T18 porte sur l'accise (TICFE).
  - La ligne existante porte sur les charges de service public compensées aux fournisseurs (CRE).
  - Pas de doublon. Drapeau `meme_dispositif:bouclier_elec`.
- **Lignes de coût et d'effet sur un même dispositif** : indicateurs différents, toutes gardées.
  - `bouclier_60_2007` et `bouclier_60_benef` ;
  - `pass_sport_2021` et `pass_sport_benef` ;
  - `cheque_energie_gen_2018` et `cheque_energie_usage_2018` ;
  - `cir2008_levier` et `cir2008_pib`, liés à `cir_2008` (`data/raw/`) ;
  - `cice_invest` et `cice_export`, liés à `cice` et `cice_emploi` (`data/raw/`).
- **Autres rapprochements avec `data/raw/`, sans doublon** :
  - `cheque_energie_gen_2018` et `cheque_energie_elarg_2019` sont des chèques de droit commun ; `cheque_energie_exc_2021` et `cheque_energie_exc_2022` sont des chèques exceptionnels ;
  - `dmtg_tepa_2008`, `isf_pme_tepa` et `bouclier_50_2008` relèvent de la loi TEPA, mais sont distincts de `tepa_hs` ;
  - `cehr_2012` est distinct de `cdhr_2025` ;
  - `ce_is_2017` est distinct de `cebge_2025`.
- **Avec T10a** : aucune ligne commune.
  - `rsa_activite_2009` reprend une piste que T10a avait exclue, faute de sources primaires. Le groupe C la juge levée : ex ante lu dans le rapport AN n° 1198, ex post tiré d'une déclaration ministérielle (drapeau `exclu_T10a_motif_leve`).
  - `ac_2021` (T10a) ne figure pas dans `data/raw/mesures_cout.csv` et n'est pas repris ici.

## 5. Contrôles

### 5.1 Écarts recalculés

L'écart vaut (ex post central − ex ante) / ex ante. Il a été recalculé pour les 60 lignes de coût d'origine et comparé aux valeurs données par les agents (tableaux de `notes_<G>.md`, mention « Écart » dans `note`).

**Aucune différence au-delà de l'arrondi.**

- Écarts arrondis par les agents : `aide_contrat_pro_2020` (−12,5 % calculé, −13 % donné), `ticfe_baisse_2022` (−12,5 % / −13 %), `cef_2012` (+0,2 % / 0 %), `tranche45_2013` (+7,5 % / +8 %), `cehr_2012` (+57,5 % / +58 %).
- Trois signalements automatiques étaient de faux positifs : un autre pourcentage figurait dans la même ligne de note (taux de recours de 37 % du Pass'Sport, recours implicite de 70 % de l'indemnité carburant, taux de 5 % de la contribution).

Les ratios des 15 lignes d'effets ont aussi été recalculés (par exemple 14 426 / 93 000 = 0,155 ; 40 300 / 220 000 = 0,18 ; 25 500 / 23 500 = 1,09). Ils sont conformes.

Écarts après fusion, pour mémoire (Md€) :

| id | Ex ante | Ex post central | Écart | Type | Règle(s) pressentie(s) |
|---|---|---|---|---|---|
| cef_2012 | 2,325 | 2,33 | +0 % | observe | patrimoine ; ponctuelle |
| bouclier_60_2007 | 0,401 | 0,246 | −39 % | observe | patrimoine |
| bouclier_50_2008 | 0,81 | 0,578 | −29 % | observe | patrimoine |
| bouclier_suppr_2012 | 0,72 | 0,4 | −44 % | observe | patrimoine |
| isf_plafonnement_2013 | 0,667 | 0,709 | +6 % | observe | patrimoine |
| isf_pme_tepa | 0,38 | 0,8 | +111 % | observe | patrimoine |
| isf_reforme_2013 | 1,0 | 1,39 | +39 % | observe | patrimoine |
| cehr_2012 | 0,4 | 0,63 | +58 % | observe | revenus ; ponctuelle |
| tranche45_2013 | 0,32 | 0,344 | +8 % | observe | revenus |
| qf_2013 | 0,49 | 0,554 | +13 % | observe | revenus |
| frais_pro_2013 | 0,075 | 0,09 | +20 % | observe | revenus |
| contrib_1pt_2011 | 0,405 | 0,4 | −1 % | reestimation | revenus |
| qf_2014 | 1,0 | 1,03 | +3 % | administratif | revenus |
| bareme_capital_2013 | 1,96 | 1,16 | −41 % | observe | capital |
| ci_dividendes_2011 | 0,645 | 0,6 | −7 % | reestimation | capital |
| pv_immo_2012 | 1,212 | 0,79 | −35 % | reestimation | capital |
| ps_nonresidents_2012 | 0,3 | 0,275 | −8 % | observe | capital |
| dmtg_tepa_2008 | 1,821 | 1,6 | −12 % | reestimation | succession |
| rappel_donations_2011 | 0,018 | 0,006 | −67 % | observe | succession |
| successions_delais_2015 | 0,5 | 1,0 | +100 % | observe | succession |
| maj_is_5pct_2012 | 1,4 | 0,9 | −36 % | observe | IS |
| report_deficits_is_2012 | 1,0 | 1,2 | +20 % | reestimation | IS |
| bmc_suppression_2012 | 0,05 | 0,5 | +900 % | reestimation | IS |
| ce_is_2017 | 4,7 | 4,9 | +4 % | observe | IS ; ponctuelle |
| ttf_2012 | 0,53 | 0,2 | −62 % | observe | nouvelle assiette |
| taxe_dividendes_3pct_2012 | 1,1 | 0 | −100 % | observe | nouvelle assiette |
| tsn_2019 | 0,4 | 0,3 | −25 % | observe | nouvelle assiette |
| cri_2023 | 12,3 | 1,7 | −86 % | observe | nouvelle assiette ; ponctuelle |
| ecotaxe_pl_2014 | 0,89 | 0 | −100 % | observe | nouvelle assiette |
| contrib_stocks_petroliers_2012 | 0,55 | 0,6 | +9 % | observe | nouvelle assiette ; ponctuelle |
| carbone_convergence_2018 | 3,6 | 3,8 | +6 % | administratif | carburants |
| accise_gaz_bouclier_2024 | 1,9 | 1,3 | −32 % | administratif | carburants |
| ticfe_baisse_2022 | 6,4 | 5,6 | −13 % | observe | électricité |
| ticfe_prolongation_2023 | 2,8 | 4,7 | +68 % | administratif | électricité |
| accise_elec_2025 | 3,4 | 4,2 | +24 % | observe | électricité |
| embauche_pme_2017 | 1,932 | 1,581 | −18 % | observe | recours |
| emplois_francs_2018 | 0,012 | 0,0038 | −68 % | observe | recours |
| aej_2020 | 0,200 | 0,174 | −13 % | observe | recours |
| aide_apprentissage_2020 | 0,404 | 0,630 | +56 % | observe | recours |
| aide_contrat_pro_2020 | 0,160 | 0,140 | −13 % | observe | recours |
| cheque_energie_gen_2018 | 0,563 | 0,422 | −25 % | observe | recours |
| cheque_energie_elarg_2019 | 0,857 | 0,686 | −20 % | observe | recours |
| rsa_activite_2009 | 1,45 | 0,744 | −49 % | observe | recours |
| pass_sport_2021 | 0,100 | 0,066 | −34 % | observe | recours |
| indemnite_carburant_2023 | 0,700 | 0,433 | −38 % | observe | recours |
| am_2004_transferts | 1,5 | 0,5 | −67 % | observe | réforme structurelle |
| rgpp_2012 | 12,3 | 11,9 | −3 % | reestimation | réforme structurelle |
| carte_judiciaire_2008 | 0,457 | 0,413 | −10 % | reestimation | réforme structurelle |
| stdr_2014 | 1,0 | 1,7 | +70 % | observe | ponctuelle |
| stdr_2015 | 1,7 | 2,654 | +56 % | observe | ponctuelle |
| stdr_2016 | 2,4 | 2,476 | +3 % | observe | ponctuelle |
| stdr_2017 | 2,1 | 1,1 | −48 % | observe | ponctuelle |
| cellule_regul_2010 | 0,7 | 0,9 | +29 % | observe | ponctuelle |
| ce_trs_2012 | 0,55 | 0,5 | −9 % | observe | ponctuelle |
| ce_is_anticipe_2012 | 0,8 | 1,0 | +25 % | observe | ponctuelle |

### 5.2 Citations

Les 150 citations ex ante et ex post des 75 lignes d'origine (60 coûts, 15 effets) ont été recherchées dans le texte des sources archivées. Le texte a été extrait avec `pdftotext`, ou tiré du HTML débarrassé de ses balises. Avant la recherche, il a été normalisé : NFKC, apostrophes et tirets unifiés, espaces réduits. Le script, lancé avec `python3 -I`, se trouve hors de `sources/`.

| Résultat | Nombre |
|---|---|
| Retrouvées mot pour mot dans le fichier de l'URL citée | 97 |
| Retrouvées sans tenir compte des espaces (mise en page) | 1 |
| Retrouvées par fragments : citation coupée par « […] », « | » ou « ; » ; chaque fragment est dans le document | 24 |
| Non retrouvées automatiquement, puis vérifiées à la main | 28 |
| **Non retrouvées après vérification** | **0** |

Les 28 vérifications manuelles se répartissent ainsi :

- **22 lignes de tableau reconstituées** par les agents (séparateurs « / » ou « | », années entre crochets). Les chiffres et les intitulés ont été retrouvés sur la page indiquée avec `pdftotext -layout`.
  - `bouclier_suppr_2012`, `pv_immo_2012` : RBDE 2012, p. 258 : 0 / +720 / +720 ; +1030 / +1076 ; +182 / +190.
  - `ps_nonresidents_2012` : AN n° 79, p. 22 : 0,05 / 0,25 / 0,3.
  - `maj_is_5pct_2012`, `report_deficits_is_2012` : NEB 2012, p. 32 : 1,4 / 0,9 / −0,5 ; 1,0 / 1,2 / 0,2.
  - `carbone_convergence_2018` : CPO 2019, p. 59, graphique : 2,7 et 0,9. Leur somme donne l'ex ante de 3,6 (drapeau `ex_ante_calcule`).
  - `accise_elec_2025` : NEB 2025, p. 24 : 4,0 / 7,4 / 8,2.
  - `embauche_pme_2017` : NEB 2018 TE, p. 67 : 1 932,0 / 1 581,1.
  - `emplois_francs_2018` : NEB 2019 TE, p. 46 : 12 / 4 / 51 / 23.
  - `aej_2020` : RPA 2022, p. 17 : 200,00 / 174,01.
  - `cheque_energie_*` : Cour 2022, p. 44 : 563,4 / 422,3 / 857,3 / 685,7 ; p. 33 : 78,8 % / 80,4 %.
  - `rsa_activite_2009` : AN n° 1198, annexe 43, p. 23 : 1 450.
  - `rgpp_2012` : IGA-IGF-IGAS, p. 50 : 12,3.
  - `stdr_2016` : RBDE 2016, p. 82 : 1,9 / 2,7 / 2,5 et 1,7 / 2,1 / 1,8.
  - `ce_fortune_2012`, `ce_trs_2012`, `ce_is_anticipe_2012` : PLFR 2 2012, p. 166, 185-188 et 195 : 2 325 ; + 550 ; 800 / −800.
  - `isf_reforme_2013` : AN n° 2172, p. 62. La note ** donne 2 248 et le tableau donne 4 570 (2012) et 3 634 (2013). Le calcul de A (3 634 − 2 248) correspond bien au tableau.
- **6 phrases** dont l'écart est purement typographique :
  - appel de note collé au chiffre : `tsn_2019` (« 20196 »), `ticfe_baisse_2022` ex post (« 2021153 »), `indemnite_carburant_2023` (« CP47 ») ;
  - trait d'union perdu : `ticfe_baisse_2022` ex ante (« comptetenu ») ;
  - citation composée de deux passages et de leurs étiquettes de source, chaque passage étant retrouvé : `taxe_dividendes_3pct_2012`, `ticfe_baisse_2022` ex post ;
  - phrase et ligne de tableau mêlées : `isf_reforme_2013`.

**Remarques.**

- Certaines citations ex post se trouvent dans un fichier archivé par un autre groupe. C'est le cas de `stdr_2015` (RBDE 2019, archivé par B) et de `ce_petrolier_2012` (RBDE 2013, archivé par A). Les deux copies ont le même sha256.
- La citation de `ticfe_baisse_2022` ex ante (NEB 2022, p. 54) est fidèle. La même note donne aussi, à un autre endroit, une formulation voisine : « initialement chiffré à -5,1 Md€, a été revu à -6,4 Md€ ».

### 5.3 Sources et sha256

- Les 83 fichiers de `sources/T18/{A,B,C,D}/` existent et leur sha256 correspond à `sources_<G>.csv`.
- Aucun fichier de `sources/T18/` ne manque à la liste.
- Toutes les dates d'accès sont le 2026-10-16.
- Aucun retéléchargement n'a été nécessaire.
- Plusieurs fichiers sont des copies de sources archivées par d'autres tâches ou d'autres groupes (signalées dans leur titre) : RBDE 2010, 2012, 2013, 2017 et 2019, PLFR 2 2012, compte rendu AN n° 59, prévision des recettes 2014-2023.

### 5.4 Unicité des id et autres anomalies

- **Id en double entre groupes avant fusion** : `cehr_2012` (A et D) et `cri_2023` (B et D). Les deux cas sont résolus par la fusion (§ 4.1). Après fusion, les 55 id de coût et les 15 id d'effet sont uniques.
- **Collisions avec l'existant** : aucune collision entre coûts et effets. Aucune non plus avec `data/raw/mesures_cout.csv`, `data/raw/mesures_effets.csv`, `data/raw/validation_attribution.csv`, ni avec les fichiers de T10a.
- **« Élasticité électricité » est absente de `regles_disponibles.csv`**, alors qu'elle existe dans `data/raw/regles.csv` (facteur 0,92, `elec_menages`).
  - Le fichier a été copié tel quel, comme le demande la consigne.
  - L'agent de phase 3 ne pourra donc pas attribuer cette règle aux 3 lignes concernées (`ticfe_baisse_2022`, `ticfe_prolongation_2023`, `accise_elec_2025`, drapeau `regle_absente_aveugle`). Il choisira probablement « Élasticité carburants » ou « Aucune ».
  - À trancher **avant** la phase 3 (§ 6, point 1).
- **« Taux de recours »** : `regles_disponibles.csv` décrit la règle d'origine (« prestation versée à la demande »). `data/raw/regles.csv` la restreint aux chiffrages qui supposent un recours complet. D'après le groupe C, aucun des 10 cas ne remplit cette condition : la version restreinte n'est pas testée.
- **Format de `realise_publie_le`** : 27 lignes (18 coûts, 9 effets) sont au format `AAAA-MM`, que la consigne ne prévoit pas (elle demande `AAAA-MM-JJ` ou `AAAA`). Ce format n'a pas été modifié : il reste exploitable pour le sous-échantillon 2026.
- **Valeurs différentes entre groupes pour la même mesure** : `cehr_2012` (ex ante 0,4 ou 0,6), `cri_2023` (central 1,7 ou 0,6), `contrib_stocks_petroliers_2012` (central 0,6 ou 0,55), `cef_2012` (central 2,33 ou 2,3).
- **Libellé de B pour la surtaxe IS 2017** : il contenait « créées pour compenser la censure de la taxe de 3 % ». Ce libellé n'est pas repris, car la ligne D est celle qui a été gardée ; l'information figure en note.

### 5.5 Construction des fichiers aveugles

- **Contenu** : id, libellé, année (`annee`), sens, indicateur, chiffrage avant adoption (`ex_ante`) et auteur. On n'y trouve ni réalisé, ni cause, ni note, ni citation, ni URL, ni règle pressentie, ni drapeau.
- **Ordre** : alphabétique par id, pour ne pas laisser voir le regroupement par règle des parts.
- **Auteur** : réécrit sous une forme courte. Les mentions qui renvoient à l'exécution ont été retirées, par exemple « calculé : exécution − écart publié par la Cour » ou « reprise par la Cour ».
- **Libellés neutralisés** (texte qui trahissait l'issue ou portait sur le réalisé) :
  - `taxe_dividendes_3pct_2012` : retrait de « censurée en 2017 … intégralement restituée » ; indicateur ramené à « Rendement Md€/an », au lieu de « net, après restitution » ;
  - `ecotaxe_pl_2014` : retrait de « suspendue en 2013 puis abandonnée en 2014 avant toute perception » ;
  - `stdr_2017` : retrait de « dernière année du guichet » ;
  - `stdr_2015`, `stdr_2016` : retrait de « périmètre de la prévision incertain » dans l'indicateur ;
  - `cheque_energie_elarg_2019` : retrait de « 5,7 M de bénéficiaires » ;
  - `successions_delais_2015` : « prévue en LFI 2015 » devient « mesure de la LFI 2015 » ;
  - `cri_2023` : indicateur « au titre de juillet 2022-décembre 2023 », sans « y c. solde versé en juillet 2024 » ;
  - `ticfe_prolongation_2023` : retrait de « (mesure nouvelle) ».
- **Termes restants** : une recherche de « annul », « restitu », « abandon », « censur », « suspend », « prorog », « conforme », « réalis », « constat » et « exécution » ne trouve plus que des termes qui décrivent le mécanisme de la mesure ou sa base de comparaison, pas son issue :
  - les « restitutions » du bouclier fiscal ;
  - « vs exécution 2024 », qui désigne la base, antérieure à la mesure, de `accise_elec_2025`.
- **Effets** : les annonces sont reprises telles quelles. Aucune ne contient de réalisé.
- **Limite** : plusieurs mesures sont très médiatisées (taxe de 3 % sur les dividendes, écotaxe, bouclier fiscal, CRI, CEHR). L'agent de phase 3 pourra en connaître l'issue même avec un libellé neutre. La colonne `issue_connue` est faite pour le dire.

## 6. Décisions laissées à l'utilisateur (non tranchées)

Elles sont tirées des notes des quatre groupes et des contrôles ci-dessus.

**Avant la phase 3**

1. **Ajouter « Élasticité électricité » à `aveugle/regles_disponibles.csv`**, ou la laisser absente, comme dans le protocole de validation actuel (§ 5.4). La consigne demande une copie à l'identique, que j'ai faite.
2. Garder ou non dans le fichier aveugle les lignes que l'on compte écarter de toute façon (crédits votés, `low`, hors champ). Toutes y sont aujourd'hui.

**Doublons et valeurs divergentes**

3. **`cehr_2012`** : ex ante de 0,4 (A, lu) ou de 0,6 (D, calculé d'après la Cour). Réalisé de 0,63 ou de 0,6. L'écart passe de +58 % à 0 %.
4. **`cri_2023`** : central de 1,7 (total au titre de 2022-2023, B) ou de 0,6 (rendement budgétaire 2023, D).
5. **`contrib_stocks_petroliers_2012`** : central de 0,6 (B) ou de 0,55 (D).
6. **`ce_is_anticipe_2012` et `ce_is_5pct_2013`** (`data/raw/`) : vérifier qu'il n'y a pas de double compte de l'avance de 0,8 Md€.
7. **Indépendance des cas** :
   - STDR 2014 à 2017 : 1 ou 4 cas ;
   - bouclier fiscal 2007, 2008 et 2012 ;
   - chèque énergie 2018 et 2019 ;
   - les trois aides #1jeune1solution, tirées du même tableau ;
   - quotient familial 2013 et 2014 ;
   - TICFE 2022 et 2023 ;
   - `isf_reforme_2013` et `isf_plafonnement_2013` : l'ex post calculé du premier inclut peut-être l'effet du second.

**Nature des chiffrages**

8. **Crédits votés comme ex ante** (`credit_vote`) : faut-il les accepter comme « chiffrages avant adoption » ? Cela concerne 11 lignes : les 10 cas de « Taux de recours », RSA activité compris, et la carte judiciaire. Pour Embauche PME (LFI 2017), la mesure existait déjà.
9. **« Observe au sens large »** (A) : supplément d'impôt calculé par la DLF sur les déclarations effectives (`tranche45_2013`, `qf_2013`, `frais_pro_2013`). Il ne mesure pas un contrefactuel. Faut-il le garder en `observe` ?
10. **Ex post administratifs ou réestimés** : `carbone_convergence_2018`, `accise_gaz_bouclier_2024`, `ticfe_prolongation_2023`, `qf_2014`, les réestimations A et B, `rgpp_2012` et `carte_judiciaire_2008`. Ils sont exclus de la statistique principale par construction (`inclus_stats` = 0 pour toutes ces lignes).
11. **Ex ante calculés ou secondaires** : faut-il écarter `ticfe_prolongation_2023` (low) et `accise_elec_2025` (prévision de ligne, pas chiffrage de mesure) ? Que faire de `stdr_2015` et `stdr_2016` (ex ante tiré de la presse) et de `am_2004_transferts` (ex ante reconstitué par la Cour) ?
12. **Taxe de 3 % sur les dividendes** : comparer le net (0, retenu) ou le brut (≈1,8 Md€/an, écart de +64 %) ?
13. **`ticfe_baisse_2022`** : quel ex ante retenir ? 5,1 (débats), 6,4 (janvier 2022, retenu) ou 8 « pour un an » (réponse ministérielle d'avril 2022).
14. **`indemnite_carburant_2023`** : central de 433 M€ (avec les 156 M€ restitués par l'ASP) ou de 277 M€.
15. **`contrib_1pt_2011`** : si la Cour ne vise que la tranche à 41 %, l'écart passe de −1 % à +74 %.
16. **`bouclier_50_2008`** : l'ex ante de 810 M€ porte-t-il sur le coût total ou sur le seul renforcement ?

**Champ des règles** (à noter, sans modifier les règles pendant T18)

17. **Élasticité revenus** : `qf_2013`, `qf_2014` et `frais_pro_2013` sont hors du champ « tranches supérieures ».
    - A note que les recettes sur les hauts revenus (CEHR, tranche à 45 %, QF) dépassent leur prévision : ces cas vont contre une règle qui réduit le rendement attendu.
    - À l'inverse, les mesures sur le capital et le patrimoine qui laissent un choix au contribuable rapportent moins que prévu.
18. **Élasticité IS** :
    - les mesures d'assiette (`report_deficits_is_2012`, `bmc_suppression_2012`) sont hors du champ « taux » ;
    - aucun ex ante d'IS ne dit s'il intègre un comportement : l'hypothèse du « double compte » ne peut être ni confirmée ni écartée ;
    - les deux cas `observe` vont en sens opposés (−36 % et +4 %).
19. **Nouvelle assiette : risque juridique** : les 6 cas mêlent des causes que la règle ne vise pas :
    - risque juridique réalisé (dividendes) ;
    - abandon politique (écotaxe) ;
    - prix de l'énergie (CRI) ;
    - assiette surestimée malgré une élasticité incluse (TTF, seul cas `comportement_inclus_ex_ante = oui`) ;
    - décalage d'encaissement (TSN) ;
    - aucune cause (stocks pétroliers).

    Faut-il restreindre la règle au risque juridique ?
20. **Élasticité carburants** : la recette d'une hausse d'accise n'est jamais isolée : il n'existe que des chiffrages administratifs. La règle reste non testable sur des cas `observe`, sauf à comparer la ligne budgétaire (prévision contre exécution), ce qui mêle la mesure et la conjoncture. Par ailleurs, l'accise sur le gaz n'est couverte par aucune règle (`accise_gaz_bouclier_2024`).
21. **Taux de recours** :
    - la version restreinte (recours complet supposé) n'est testée par aucun cas ;
    - 9 cas sur 10 dépensent moins que prévu, de −13 % à −68 %, y compris quand l'ex ante intégrait déjà un recours partiel (chèque énergie à 90 %, Pass'Sport à 37 %) ;
    - C suggère une décote plus faible, applicable aussi aux crédits votés pour une aide nouvelle à la demande.
22. **Réforme structurelle** :
    - la cible paraît inatteignable sur des réalisés `observe`, car les économies sont réestimées par l'administration qui les a prévues ;
    - le seul cas `observe` (`am_2004_transferts`) repose sur un ex ante reconstitué ;
    - `carte_judiciaire_2008` est un coût de mise en œuvre et non une économie : à exclure si la règle ne vise que les économies ;
    - faut-il réintégrer `ac_2021` (T10a) sous cette règle ?
23. **Recette ponctuelle** :
    - **choisir l'indicateur du test** : écart de la première année (celui des lignes actuelles) ou recette encore perçue à N+2 ? La durée réelle est donnée en note :
      - restée ponctuelle : CEF, stocks pétroliers, surtaxe IS 2017 ;
      - prolongée ou renouvelée : STDR, cellule de 2010, contribution de 5 % sur l'IS, TRS, CRI ;
      - durée de la CEHR **non vérifiée** ;
    - autres rattachements possibles à cette règle : `cef_2012`, `successions_delais_2015` (mesure de trésorerie, plutôt que succession) et `contrib_stocks_petroliers_2012`.
24. **Rattachements alternatifs suggérés par les groupes** :
    - `bouclier_60_2007` et `bouclier_50_2008` (non-recours) : « Taux de recours » ;
    - effets de volume (`contrat_generation`, `emplois_avenir_2013`, `ati_2019`, `demission_reconversion_2019`) : « Taux de recours » ;
    - `bouclier_60_benef` : « Taux de recours ».
25. **Effets** : garder ou non :
    - les lignes `low` (`cir2008_pib`, ex post simulé ; `ati_2019` et `demission_reconversion_2019`, stock contre flux) ;
    - les annonces non chiffrées (CICE investissement et exportations, PreParE emploi des mères), dont le ratio de 0 est conventionnel ;
    - les annonces publiées après le vote (CIR, Trésor-Éco de janvier 2009).
26. **`rsa_activite_2009`** : le groupe C juge levé le motif d'exclusion de T10a. L'ex post reste une déclaration ministérielle, et le RAP 2009 n'a pas été lu.
27. **Pistes de reprise** citées par les groupes :
    - A : DMTG de la LFR 2 2012 ; prélèvements sociaux sur le capital (CCSS) ; taxe à 75 % ;
    - B : contribution d'IS à 10,7 % ; CSPE ; Voies et moyens, tome I (TSN, TICFE) ;
    - C : complémentaire santé solidaire, ex post du surcoût ; NEB du CAS « véhicules propres » ; assurance chômage 2023 ; garantie jeunes ;
    - D : fiscalité du tabac 2018-2020 (OFDT) ; évaluation préalable du suramortissement 2019 ; objectif Duflot ; emplois de la réforme de l'assurance chômage 2019.

## Ajout avant la phase 3 (16/10/2026)

La règle « Élasticité électricité », présente dans `data/raw/regles.csv` mais absente de `recherche/validation/aveugle/regles_disponibles.csv` (fichier antérieur à la règle), a été ajoutée à la seule copie `aveugle/regles_disponibles.csv` de T18, avec le champ « Accise sur l'électricité (hausse ou baisse du tarif) ». Les fichiers gelés au § 0 de la consigne (`regles.csv`, `moteur_regles.csv`) ne sont pas modifiés.
