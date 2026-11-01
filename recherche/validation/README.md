# Validation de la méthode : protocole

**Question.** Notre chiffrage corrigé (chiffrage de départ × facteur de la règle) est-il plus proche du coût réalisé que le chiffrage de départ ? C'est l'indicateur de confiance de la méthode, règle par règle.

**Échantillon.** 25 chiffrages officiels avant adoption (couche 1), 10 effets annoncés chiffrables, 22 chiffrages d'instituts sur les programmes Macron 2017 et 2022 (T10b).

**Attribution à l'aveugle.** Un agent séparé a reçu une copie isolée de `aveugle/` (libellé de la mesure, année, sens, chiffrage annoncé, auteur ; liste des règles et de leur champ), sans le réalisé ni la cause de l'écart, avec consigne de choisir la règle d'après la seule nature de la mesure. Son fichier est conservé tel quel (`attribution_agent.csv`, copié dans `data/raw/validation_attribution.csv`) ; aucune attribution n'a été retouchée après coup, y compris les cas limites qu'il signale (CIR et CITE en « Taux de recours », boucliers énergie en « Aucune »…).

**Limite principale.** L'agent reconnaissait l'issue de 60 cas sur 83 (colonne `issue_connue`). Le test n'est donc aveugle qu'en intention. Les 23 cas « issue inconnue » sont presque tous des coûts mécaniques (facteur 1) : ils ne testent pas la méthode.

**Circularité.** Deux paramètres sont calibrés sur des mesures de l'échantillon : `facteur_reforme` (retraites 2010 et 2023) et `ratio_effet_promis` (CICE, TEPA, ISF, PFU). Pour ces mesures, le facteur est recalculé sans elles (leave-one-out). L'élasticité du capital (0,77) a été estimée sur 2008-2017 : le PFU de 2018 est hors échantillon.

**Nature du réalisé** (`type_ex_post`, convention du 20/10/2026, après T20) :

- `observe` : montant constaté pour la mesure elle-même, isolable dans les comptes : recette d'un prélèvement propre (contribution, majoration déclarée à part), dépense d'un dispositif identifié, montants versés aux bénéficiaires ;
- `reestimation` : la mesure est fondue dans un impôt ou une dépense existante (changement de taux ou d'assiette, dépense fiscale), et son coût après coup est un nouveau chiffrage de l'administration ou d'un évaluateur ; un coût de dépense fiscale lu dans les Voies et moyens en fait partie ;
- `administratif` : montant budgétaire ou enveloppe qui reprend la prévision.

Seuls les cas `observe` jugent une règle (statut ci-dessous). Les autres restent dans l'erreur des chiffrages de départ (couche 1), où ils sont signalés.

**Statuts** (`data/validation_regles.csv`) : confirmée (plus d'améliorations que de dégradations et erreur médiane réduite), contredite (l'inverse), mitigée, non concluante (réalisés qui ne sont pas des observations), non testée.

## Critères de l'échantillon et choix de la fusion (T27, 01/11/2026)

**Indépendance des cas.** Un cas par mesure. Deux réformes distinctes d'un même dispositif comptent séparément : la création du bouclier fiscal (2007) et sa suppression (2012) sont deux cas. Une année suivante de la même mesure ne compte pas : pour le STDR, seule l'année 2014 est comptée, pas 2015 à 2017. Une ligne qui porte l'année suivante sur tout le dispositif, extension comprise, est une année suivante : le chèque énergie de 2019 n'est pas compté à côté de celui de 2018. Deux aides distinctes d'un même plan comptent séparément, même quand leurs chiffrages viennent du même tableau (aide à l'embauche des jeunes et aide aux contrats de professionnalisation, plan #1jeune1solution) ; leurs erreurs ne sont donc pas tout à fait indépendantes. Une même mesure peut avoir une ligne de coût et une ligne d'effet. Mais si les deux lignes mesurent le même recours et relèvent de la même règle, seule la ligne de coût est comptée (Pass'Sport, chèque énergie de 2018). Les cas étrangers suivent le même critère : la première année de chaque taxe, dans chaque territoire où elle s'applique. Les lignes écartées restent dans `mesures_cout.csv` et `mesures_effets.csv` (`inclus_stats` = 0, motif dans la note), avec le drapeau `meme_dispositif` ou `meme_plan`.

**Rattachements alternatifs.** L'attribution à l'aveugle fait foi. Les groupes de recherche ont proposé d'autres règles pour quelques cas (drapeau `autre_regle_possible`) : « Taux de recours » pour le bouclier fiscal de 2007 et de 2008, et pour les effets sur l'emploi du contrat de génération et des emplois d'avenir. Ces propositions ont été faites en connaissant le réalisé. Les adopter enlèverait au test son intérêt. Elles ne changent donc ni le statut des règles, ni la part des corrections qui repose sur une règle confirmée. Simulée sur une copie, la variante qui les adopte ne change aucun statut (`recherche/T27/G2/readme_ajouts.md`, § B2) ; elle n'est pas publiée.

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

Code : `scripts/validation.py`. Sorties : `data/validation_mesures.csv`, `validation_resume.csv`, `validation_regles.csv`, `confiance_programmes.csv`.
