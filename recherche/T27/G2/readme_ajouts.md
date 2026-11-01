# T27, groupe 2 : ajouts au README de la validation (G2.5, G2.6, G2.7, G2.10)

État du dépôt : commit `0ff7a16` et modifications non commitées du 01/11/2026. Ce fichier a deux parties :

- **partie A**, le texte à coller dans `recherche/validation/README.md`, après le paragraphe « Statuts » ;
- **partie B**, les vérifications qui le fondent et les corrections proposées (`corrections_paires.csv`, 17 lignes au format de `scripts/appliquer_corrections.py`, non appliquées). Cette partie n'est pas à coller.

Le texte de la partie A décrit l'échantillon une fois `corrections_paires.csv` appliqué. Sans ces corrections, les paragraphes « Indépendance des cas » et « Enveloppes de crédits » ne sont pas encore vrais.

---

## Partie A : texte à coller

**Indépendance des cas.** Un cas par mesure. Deux réformes distinctes d'un même dispositif comptent séparément : la création du bouclier fiscal (2007) et sa suppression (2012) sont deux cas. Une année suivante de la même mesure ne compte pas : pour le STDR, seule l'année 2014 est comptée, pas 2015 à 2017. Une ligne qui porte l'année suivante sur tout le dispositif, extension comprise, est une année suivante : le chèque énergie de 2019 n'est pas compté à côté de celui de 2018. Deux aides distinctes d'un même plan comptent séparément, même quand leurs chiffrages viennent du même tableau (aide à l'embauche des jeunes et aide aux contrats de professionnalisation, plan #1jeune1solution) ; leurs erreurs ne sont donc pas tout à fait indépendantes. Une même mesure peut avoir une ligne de coût et une ligne d'effet. Mais si les deux lignes mesurent le même recours et relèvent de la même règle, seule la ligne de coût est comptée (Pass'Sport, chèque énergie de 2018). Les cas étrangers suivent le même critère : la première année de chaque taxe, dans chaque territoire où elle s'applique. Les lignes écartées restent dans `mesures_cout.csv` et `mesures_effets.csv` (`inclus_stats` = 0, motif dans la note), avec le drapeau `meme_dispositif` ou `meme_plan`.

**Rattachements alternatifs.** L'attribution à l'aveugle fait foi. Les groupes de recherche ont proposé d'autres règles pour quelques cas (drapeau `autre_regle_possible`) : « Taux de recours » pour le bouclier fiscal de 2007 et de 2008, et pour les effets sur l'emploi du contrat de génération et des emplois d'avenir. Ces propositions ont été faites en connaissant le réalisé. Les adopter enlèverait au test son intérêt. Elles ne changent donc ni le statut des règles, ni la part des corrections qui repose sur une règle confirmée. Elles sont publiées à part, en variante.

**Enveloppes de crédits.** Pour une aide nouvelle, souvent décidée en urgence, le seul chiffre connu avant le vote est parfois l'enveloppe de crédits ouverte par la loi de finances. Elle compte comme chiffrage de départ si le texte qui l'ouvre, ou l'annonce du Gouvernement juste avant le vote, donne le montant par bénéficiaire et le nombre de bénéficiaires visés : l'enveloppe est alors le produit d'une prévision. Sinon, c'est un plafond de dépense, pas un chiffrage. Toute ligne dont le départ est un crédit voté porte le drapeau `credit_vote`, qu'elle soit comptée ou non. La ligne « sans les crédits votés » de `validation_resume.csv` donne le résultat sans elles. Les chèques énergie exceptionnels de 2021 (100 € pour 5,8 millions de ménages) et de 2022 (100 ou 200 € pour 12 millions de ménages) remplissent le critère et restent comptés. Le chèque fioul de 2022 le remplit aussi, mais il reste hors statistique depuis l'extension de l'échantillon (T10a). Le bouclier tarifaire sur le gaz de 2023 n'est pas une enveloppe : son départ est un chiffrage du PLF 2023, qui part d'un volume de gaz.

**Choix de la fusion.** Les choix ci-dessous ont été faits en intégrant les recherches, sans texte à ce moment-là. Le motif vient des rapports de recherche et du journal (`data/raw/historique.csv`). Quand il n'est écrit nulle part, on le dit.

*Mesures de T18* (`recherche/T18/rapport_fusion.md`, § 4 et § 6) :

- `cehr_2012` : départ de 0,4 Md€ (groupe A, dispositif voté), et non de 0,6 (groupe D). Le chiffre de A est lu (rapport AN n° 1328, p. 96). Celui de D est calculé (0,2 au PLF, plus 0,4 ajoutés en LFI). Drapeau `ex_ante_conteste`.
- `cri_2023` : réalisé central de 1,7 Md€ (total dû au titre de 2022 et 2023), et non de 0,6 (recette budgétaire de 2023, gardée comme borne basse). La Cour des comptes juge ce total « plus juste » à comparer aux 12,3 Md€ attendus en LFI 2023. Drapeau `ex_post_central_conteste`.
- `contrib_stocks_petroliers_2012` : réalisé central de 0,6 Md€, et non de 0,55. La ligne du groupe B repose sur deux sources primaires lues. Le 0,55 du groupe D est le contrecoup de 2013, peut-être une prévision. Les bornes (0,55 et 0,65) viennent de l'arrondi au dixième de la Cour.
- Taxe de 3 % sur les dividendes (`taxe_dividendes_3pct_2012`) : réalisé net (0), et non brut (environ 1,8 Md€ par an, soit un écart de +64 %). Motif non écrit à la fusion. Le groupe B a retenu le net et mis le brut en note (drapeau `ex_post_net_vs_brut`).
- `ticfe_baisse_2022` : départ de 6,4 Md€ (chiffrage révisé de janvier 2022). Les autres chiffres étaient 5,1 Md€ (débats parlementaires) et 8 Md€ « pour un an » (réponse ministérielle d'avril 2022). Le 6,4 est retenu parce qu'il porte sur le même périmètre que le réalisé, la baisse jusqu'au plancher (groupe B, `recherche/T18/parts/notes_B.md`).
- `indemnite_carburant_2023` : réalisé central de 433 M€, borne basse de 277 M€. Le groupe C a retenu 433 M€ parce que ce montant compte les 156 M€ rendus par l'ASP puis réutilisés (note 47 de la Cour). Il correspond aussi aux 4,3 millions de bénéficiaires × 100 €. Motif de la confirmation non écrit à la fusion.
- « Réforme structurelle » (T18, point 22) : la réforme de l'assurance chômage de 2019-2021 (`ac_2021`, T10a) n'est pas dans l'échantillon. Elle a été écartée à l'intégration de T10a, avec les trois autres candidates en confiance `low` (journal, 14/10/2026, ligne C1). Le motif pour ne pas la reprendre en T18 n'a pas été écrit à la fusion. Elle serait de toute façon hors statistique : confiance `low`, et départ et réalisé tirés du même modèle de l'Unédic. `carte_judiciaire_2008` et `am_2004_transferts` sont dans le fichier, hors statistique. Pour la première, le réalisé est une estimation de la Cour, pas une observation. Pour la seconde, la ligne est `low` et son départ a été reconstitué (journal, 16/10/2026).

*Chiffrages d'instituts de T10b* (`recherche/T10b/rapport.md`, § 8) :

- Les chiffrages de l'OFCE sont gardés, alors qu'ils datent de juin et juillet 2017, après l'élection. Motif non écrit à la fusion. Leur note dit seulement qu'ils sont parus « après l'élection mais avant le PLF 2018 (ex ante) ». Leurs résultats sont publiés à part, chiffreur par chiffreur (groupe « institut : OFCE »).
- Les deux lignes dont le réalisé est dérivé sont gardées : 50 000 postes d'État et suppression de la redevance. Motif non écrit à la fusion. Le PFU est exclu, avec le motif écrit dans `inclus_stats` : « périmètre et réalisé incertains » (réalisé entre 0 et 1,4 Md€). La ligne de la Fondation Concorde sur le PFU est exclue parce que son chiffrage est nul.

*Paramètres testés en T21* (`recherche/T21/rapport.md`, § 6) :

- Les deux estimations de l'élasticité des successions (France et Allemagne) gardent la confiance `medium`, alors que seuls leurs résumés ont été lus. Motif non écrit à la fusion. Le choix ne change aucun chiffre : la règle de T21 corrige un paramètre avec les seules estimations `high`.

---

## Partie B : vérifications et propositions (ne pas coller)

### B1. G2.5 : paires `meme_dispositif` et `meme_plan` dont une ligne au moins a `inclus_stats` = 1

« Règle » = règle attribuée à l'aveugle. « Effets » = `mesures_effets.csv`. Verdicts de `data/validation_mesures.csv`.

| Paire | Lignes comptées (`inclus_stats`) | Lecture | Conforme ? | Changement |
|---|---|---|---|---|
| `bouclier_60_2007` et `bouclier_suppr_2012` (Élasticité patrimoine) | 1 et 1 | création, puis suppression : deux réformes | oui | aucun |
| `bouclier_60_2007` et `bouclier_50_2008` | 1 et 0 | renforcement de 2008 : réforme distincte, déjà exclue pour une autre raison (périmètre de l'ex ante douteux, hist. 316) | oui | aucun |
| `bouclier_60_2007` (Élasticité patrimoine) et `bouclier_60_benef` (effets, Taux de recours) | 1 et 1 | même mesure, coût et effet, mais deux règles différentes : jamais dans la même statistique | oui (voir B2 : non dans la variante) | aucun |
| `bouclier_50_2008` et `bouclier_suppr_2012` | 0 et 1 | réformes distinctes | oui | aucun |
| `cheque_energie_gen_2018` et `cheque_energie_elarg_2019` (Taux de recours) | 1 et 1 | la ligne de 2019 porte sur tout le dispositif élargi, pas sur la seule extension (sa note) ; même cause d'écart (taux d'usage de 79-80 % contre 90 % prévu) | **non** : c'est une année suivante | `cheque_energie_elarg_2019` : `inclus_stats` 1 → 0, note complétée |
| `cheque_energie_gen_2018` et `cheque_energie_usage_2018` (effets ; les deux en Taux de recours) | 1 et 1 | le taux d'usage est la cause de l'écart de coût ; les deux entrent dans le test de « Taux de recours » | **non** | `cheque_energie_usage_2018` : `inclus_stats` 1 → 0, note complétée |
| `pass_sport_2021` et `pass_sport_benef` (effets ; les deux en Taux de recours) | 1 et 1 | coût = bénéficiaires × 50 € : même recours, même règle | **non** | `pass_sport_benef` : `inclus_stats` 1 → 0, note complétée |
| `aej_2020`, `aide_contrat_pro_2020`, `aide_apprentissage_2020` (#1jeune1solution) | 1, 1 et 0 | trois aides distinctes ; même tableau de la DGEFP, erreurs corrélées (−13 % et −12,5 %) ; l'aide à l'apprentissage est exclue (`low`, périmètre changé) | oui | aucun ; corrélation dite dans le README |
| `qf_2013` et `qf_2014` | 1 et 0 | deux abaissements successifs du plafond : réformes distinctes ; 2014 exclue parce que réalisé `administratif` | oui | aucun |
| `ticfe_baisse_2022` et `ticfe_prolongation_2023` | 1 et 0 | 2023 exclue (`low`, ex ante calculé, `administratif`) | oui | aucun |
| `stdr_2014` et `stdr_2015` à `stdr_2017` | 1 et 0 | années suivantes ; un seul cas compté (hist. 316) | oui | aucun |
| `bc_carbon_tax_2008_09`, `_2009_10`, `_2010_11` (étranger) | 1, 1, 1 | trajectoire de taux fixée par la loi de 2008 : années suivantes | **non** | `_2009_10` et `_2010_11` : `inclus_stats` 1 → 0 |
| `ca_fuel_charge_2019_20` et `ca_fuel_charge_2020_21` (étranger) | 1 et 1 | même redevance, mêmes provinces, hausse de taux prévue par la loi | **non** | `_2020_21` : 1 → 0 |
| `ca_fuel_charge_ab_2019_20` et `ca_fuel_charge_ab_2020_21` (étranger) | 1 et 1 | année suivante en Alberta | **non** | `_ab_2020_21` : 1 → 0 |
| `ca_fuel_charge_2019_20` et `ca_fuel_charge_ab_2019_20` | 1 et 1 | extension de la redevance à une province de plus au 1er janvier 2020 : décision distincte, ligne propre à l'Alberta | oui, **douteux** | aucun (T21 comptait 1 cas fédéral ; ici 2) |

Hors champ (autres drapeaux), pour mémoire : `isf_plafonnement_2013` et `isf_reforme_2013` (`chevauchement`, la seconde exclue) ; `taxe_dividendes_3pct_2012` et `ce_is_2017` (`lie_a`, deux règles différentes).

**Effet des 14 lignes G2.5 de `corrections_paires.csv`** (calculé sur une copie du dépôt : `appliquer_corrections.py`, `build.py`, `validation.py`, `check_regression.py`, tous OK) :

- aucun effet sur un solde, sur un statut de règle ni sur `confiance_programmes.csv` (part confirmée inchangée) ;
- chiffrages officiels, statistique principale : 49 → 48 cas, erreur médiane 18,2 % → 16,8 % devient 18,0 % → 17,1 %, 20 / 14 / 15 devient 19 / 14 / 15 ;
- effets annoncés : 18 → 16 cas, 76,0 % → 29,0 % devient 81,5 % → 29,0 % ;
- « Taux de recours » (version d'origine, non publiée comme statut) : 10 améliorés et 8 dégradés deviennent 8 et 7 ; erreur médiane 29,7 % → 28,1 % devient 34,4 % → 38,8 % ;
- cas étrangers de « Élasticité carburants » (note de la règle) : 7 cas, 3 améliorés et 4 dégradés, 13 % → 18 %, deviennent 3 cas, tous dégradés, 10 % → 29 %. « Mesures étrangères » : 8 → 4 cas.

### B2. G2.6 : la variante n'existe pas dans `scripts/validation.py`

`validation.py` ne lit pas le drapeau `autre_regle_possible` : la variante n'est pas calculée. Changement de code nécessaire (non fait) :

1. Lire dans `mesures_cout.csv` et `mesures_effets.csv` les drapeaux `autre_regle_possible:<règle>` (dictionnaire `(fichier, id) → règle`), en ignorant ceux qui répètent la règle à l'aveugle.
2. Sortir de `ajouter` une fonction `evaluer(idm, depart, realise, regle, base)` qui rend facteur (leave-one-out compris), prévision, erreurs et verdict, puis construire `lignes_variante` : copie de `lignes` avec la règle alternative et les valeurs recalculées.
3. Sortir la boucle des statuts (`for regle in sorted(f)`) dans une fonction `statuts_de(lignes)`, appelée sur `lignes` puis sur `lignes_variante`.
4. Écrire `validation_regles_variante.csv` (statut et note de la variante, à côté du statut publié) et ajouter à `validation_resume.csv` une ligne « Variante : rattachements alternatifs » ; déclarer le fichier dans `build_web.py` et les schémas si le site doit l'afficher.
5. Ne pas brancher la variante sur `confiance_programmes.csv` : la part confirmée reste calculée sur l'attribution à l'aveugle.

Résultat attendu, simulé sur une copie (attribution remplacée pour les 8 lignes à drapeau, avant les corrections G2.5) : aucun statut ne change. « Élasticité patrimoine » reste mitigée (5 / 4 → 4 / 4). « Effet promis » reste confirmée (10 / 3 → 9 / 2). « Taux de recours » passe, en version d'origine, de 10 / 8 à 12 / 9. L'erreur médiane corrigée de la statistique principale passe de 16,8 % à 15,0 %, à cause du seul `bouclier_60_2007`.

À noter : dans la variante, `bouclier_60_2007` et `bouclier_60_benef` relèvent tous deux de « Taux de recours » ; par le critère de G2.5, seule la ligne de coût devrait y compter. Les drapeaux de `bouclier_60_benef`, `ati_2019`, `demission_reconversion_2019` et `successions_delais_2015` répètent la règle déjà attribuée à l'aveugle : ils sont sans objet.

### B3. G2.7 : cas candidats au drapeau `credit_vote`

Le drapeau est un élément de la colonne `drapeaux` (liste séparée par des `;`), lu par `validation.py:102`. Pour une ligne sans drapeau, la correction remplace la valeur vide par `credit_vote` : le format de `appliquer_corrections.py` le permet.

| Ligne | Départ | Montant et bénéficiaires lus | Critère | Correction |
|---|---|---|---|---|
| `cheque_energie_exc_2021` (comptée) | 600 M€, crédits à voter en PLFR de fin de gestion 2021 | 100 € × 5,8 M ménages (QG n° 4365, archivé) | rempli | `drapeaux` : vide → `credit_vote` |
| `cheque_energie_exc_2022` (comptée) | 1,8 Md€ ouverts au PLFR 2 2022 | 100 ou 200 € ; 12 M ménages (PLFR 2, art. 9, p. 28 et 115, archivé) | rempli | `drapeaux` : vide → `credit_vote` |
| `cheque_fioul_2022` (hors statistique) | 230 M€ votés en LFR 1 2022 | 100 ou 200 € ; ≈1,6 M ménages (même source, p. 115) | rempli | `drapeaux` : vide → `credit_vote` |
| `bouclier_gaz_2023` (hors statistique) | 6,8 Md€, « coût » prévu au PLF 2023 | volume de 74 TWh (Cour, 2024, p. 217) ; pas d'enveloppe | sans objet | aucune |
| `bouclier_elec` (hors statistique) | estimation de la CRE en juillet 2023 | pas d'enveloppe | sans objet | aucune |
| `p117_2020` à `p117_2025` (hors statistique) | crédits évaluatifs de la charge de la dette | pas une aide | sans objet | aucune |

Effet des 3 lignes : aucun sur la statistique principale ni sur un statut. La ligne « sans les crédits votés » passe de 41 à 39 cas ; son erreur médiane ne bouge pas (17,8 % → 17,5 %), puisque les deux chèques suivent la règle « Aucune » (facteur 1). Les autres lignes de la couche 1 (prime d'activité, APL…) partent d'un chiffrage et non d'une enveloppe.

### B4. Restent douteux

- **Critère des enveloppes appliqué aux lignes de T18 déjà marquées `credit_vote`.** Il n'a pas été vérifié ligne par ligne. D'après les notes, `pass_sport_2021`, `indemnite_carburant_2023` et `aide_contrat_pro_2020` donnent montant et bénéficiaires. Ce n'est pas le cas d'`embauche_pme_2017` : la Cour parle d'« absence de prévision possible du nombre de dossiers ». Pour `emplois_francs_2018`, `aej_2020`, `cheque_energie_gen_2018` et `cheque_energie_elarg_2019`, les notes ne disent rien. Si le critère sert aussi à exclure (« sinon, c'est un plafond »), il peut changer la statistique principale : décision à prendre avant de coller la phrase.
- **`cheque_fioul_2022`** remplit le critère mais reste exclu (« enveloppe de crédits, recours », note de la ligne, depuis le commit initial). Avec le critère, ce motif ne tient plus. Le réintégrer ajouterait un cas « Taux de recours » amélioré (−79 % avant correction). Ce n'est pas proposé ici.
- **Alberta 2019-20** compté comme mesure distincte : c'est une lecture. T21 (§ 3.1) ne gardait qu'un cas fédéral.
- **`cheque_energie_elarg_2019`** : le suivi (G2.5) le voyait comme une mesure distincte (élargissement). La note de la ligne dit le contraire (dispositif entier, cas corrélé). C'est la note qui est suivie ici.
- **Phrase « Elles sont publiées à part, en variante »** (partie A) : elle n'est vraie qu'après le changement de code de B2.
