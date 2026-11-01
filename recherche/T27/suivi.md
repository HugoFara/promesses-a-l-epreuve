# T27 : suivi des décisions non tranchées, groupes 2 à 6

Plan de travail du 01/11/2026, état du dépôt au commit `0ff7a16`. Il part du croisement des décisions non tranchées (trois relevés, environ 85 points pour les rapports T1 à T25 et l'audit du 14/10/2026). Le groupe 1, celui des points qui peuvent changer un chiffre publié, est traité dans `recherche/T26/rapport_integrateur.md` (commits `c668865` et `0ff7a16`) et n'est pas repris ici, sauf ses reliquats (§ 7).

Chaque point a été revérifié dans les fichiers actuels, dans `data/raw/historique.csv` (« hist. ») et dans le journal git. Les points réglés depuis le croisement sont écartés en une ligne (§ 8).

Légende :
- **Nature** : règle (décision de règle), recherche (recherche documentaire), texte (correction de texte), code ;
- **Effet** : effet possible sur un chiffre publié (solde, fourchette, « part confirmée », carte, « Mon foyer ») ;
- **Exécution** : *direct* (faisable avec le dépôt et les sources déjà archivées) ou *sous-agent* (source externe à lire, selon `recherche/CONSIGNES.md`) ;
- **[Utilisateur]** : le point demande un choix de l'utilisateur (politique, de périmètre ou de présentation), pas seulement un choix technique. Les autres points peuvent être tranchés par l'intégrateur, mais ceux qui changent un chiffre publié sont soumis à l'utilisateur avant d'être appliqués, comme en T26.

Dans chaque groupe, les points sont classés par priorité, en commençant par ceux qui ont un effet sur un chiffre publié.

## Synthèse

| Groupe | Points ouverts | Avec effet possible sur un chiffre publié | Décision de l'utilisateur |
|---|---|---|---|
| 2. Validation sur le passé | 10 | 4 (G2.1 à G2.4) | aucune |
| 3. Paramètres | 5 | 3 (G3.1 à G3.3) ; G3.4 seulement si l'indicateur remplace l'actuel | aucune |
| 4. Cartes « idées qui reviennent » | 6 | 5 (cartes seulement) | G4.1, G4.6 |
| 5. Notes périmées | 9 | aucun montant ; textes publiés | aucune |
| 6. Pistes jamais explorées | 10 | 7 (G6.1 à G6.5, G6.7, G6.8 : variantes, statuts ou nouveaux montants) | G6.1, G6.2 |
| Reliquats du groupe 1 (§ 7) | 5 | 5 (R1 sur les fourchettes seulement) | aucune |

---

## 2. Règles de validation sur le passé

Fichiers communs : `scripts/validation.py`, `data/raw/mesures_cout.csv`, `data/raw/mesures_effets.csv`, `data/raw/calibration_instituts.csv`, `data/raw/validation_attribution.csv`, `recherche/validation/README.md`, sortie `data/validation_regles.csv`.

Rappel utile : le statut d'une règle n'entre pas dans le solde, mais il entre dans l'indicateur publié « part des corrections reposant sur une règle confirmée » (`data/confiance_programmes.csv`, `validation.py:246-265`). Les règles « Recette ponctuelle » et « Médiane des estimations » y sont classées « sans correction » (`validation.py:253-254`).

### G2.1 Champ de la règle « Élasticité revenus » (T18 point 17, T17 § 6-1)

- **Constat.** La règle (facteur 0,9, `eps_top` 0,15 à 0,2) est calibrée sur le top 0,1 % (`regles.csv`, base « Élasticité 0,15-0,2 pour le top 0,1 % »). La famille `impot_revenu` (`familles.csv:22`) la donne aussi à deux baisses larges du RN : `rn24_part_fiscale` (−3,4, part fiscale entière dès le 2e enfant) et `rn24_ir_jeunes` (−3,7, exonération des moins de 30 ans). Sa justification dit encore « Règle discutable pour une baisse ciblée sur les familles : voir rapport » (`application_lignes.csv:64`). Le dépôt contient déjà l'élasticité moyenne : `eti_fr`, 0,05 pour tous les foyers, « correction négligeable (<5 %) » (`elasticites.csv:2`). Sur le passé, la règle a 3 cas (« trop peu de cas »), dont 2 dégradés ; `qf_2013` et `frais_pro_2013` sont déjà hors de son champ (règle « Aucune »).
- **Fichiers.** `data/raw/familles.csv`, `data/raw/application_lignes.csv` (lignes 64 et `rn24_ir_jeunes`), `data/raw/regles.csv`, `data/raw/moteur_regles.csv`, `data/raw/moteur_parametres.csv` (`eps_top`), `data/raw/elasticites.csv` (`eti_fr`).
- **Nature.** Règle, avec symétrie. **Effet : oui.** Facteur 1 sur les deux lignes : RN 2024 −0,7 Md€ ((3,4 + 3,7) × 0,1). Avec `eti_fr` (0,05), à peu près −0,5. `nfp_ir` (4,7) et `l_ir` (4,7) visent les hauts revenus et ne changent pas.
- **Action.** Écrire le champ de la règle (« hausse ou baisse du barème concentrée sur les hauts revenus »). Créer une famille « barème large » (baisse ou hausse qui touche la plupart des foyers) avec une règle à `eti_fr` ou « Aucune », appliquée à tous les partis. Reclasser les deux lignes du RN, puis réécrire la justification (G5.2). Faire relire l'attribution par quelqu'un qui n'a pas fait le chiffrage (CONTRIBUTING, règle 2).
- **Exécution.** Direct.

### G2.2 « Taux de recours » : version restreinte non testée, décote plus faible non examinée (T18 point 21)

- **Constat.** Depuis le 14/10/2026, la règle (0,65) ne vaut que si le chiffrage suppose un recours complet. Le statut reste « non testée (restreinte) » : aucun cas passé ne remplit la condition. Le groupe C de T18 relevait que 9 cas sur 10 dépensent moins que prévu même quand l'ex ante intégrait un recours partiel (chèque énergie, Pass'Sport). Il suggérait une décote plus faible, applicable aussi aux crédits votés d'une aide nouvelle à la demande. Deux lignes portent la règle : `nfp_autonomie` et `l_autonomie` (−12,3 chacune, facteur 0,65, `recours_complet_suppose` = oui).
- **Fichiers.** `data/raw/regles.csv:13`, `data/raw/moteur_parametres.csv` (`taux_recours`), `scripts/validation.py:52-54` (`RESTREINTES`), `data/raw/familles.csv:34`.
- **Nature.** Règle et recherche. **Effet : oui.** Chaque 0,1 de facteur vaut 1,2 Md€ sur NFP 2024 et sur le panier LFI. Si la version restreinte devenait « confirmée », la part confirmée de NFP 2024 passerait d'environ 36 % à environ 57 % (4,3 Md€ de correction aujourd'hui « non testée (restreinte) », `confiance_programmes.csv`).
- **Action.** (1) Chercher des chiffrages passés qui supposaient un recours complet (prestation nouvelle chiffrée sur la population éligible). (2) Tester sur les cas existants une décote « recours partiel déjà compté » et la présenter à part, sans changer la règle avant d'avoir 5 cas (`MIN_CAS`).
- **Exécution.** Sous-agent pour (1) ; direct pour (2).

### G2.3 Règle « Médiane des estimations » : indépendance des chiffreurs, prise en compte du candidat (T21 point 8)

- **Constat.** Non tranché. Le test sur le passé est « non jugeable » : 2 mesures seulement, à chiffreurs non indépendants (Terra Nova reprend le candidat, Montaigne révise après Terra Nova ; T21 § 3.5). Les campagnes 2007 et 2012 sont hors statistique. La règle porte sur `nfp_zucman` (8 = médiane de 0 pour l'iFRAP et 16 pour LGC) et `nfp_niches` (14). Les chiffrages partisans sont déjà exclus de la fourchette (`scripts/sensibilite.py:9`).
- **Fichiers.** `data/raw/regles.csv`, `data/raw/application_lignes.csv` (`nfp_zucman`, `nfp_niches`), `data/raw/calibration_instituts.csv` (lignes « T21 : test de la médiane »), `recherche/T21/rapport.md` § 3.5.
- **Nature.** Règle. **Effet : possible**, de plusieurs Md€ sur NFP 2024 si un chiffreur est écarté (`nfp_zucman` passerait à 0 ou à 16). Aucun si la règle actuelle est confirmée.
- **Action.** Écrire la règle : médiane des seuls chiffreurs indépendants du parti, candidat exclu (ce qui est cohérent avec `sensibilite.py:9`), et dépendance entre chiffreurs signalée dans la fiche. Vérifier que les deux lignes la respectent déjà. Clore le test sur le passé comme « non testable à ce jour ».
- **Exécution.** Direct.

### G2.4 Champ de la règle « Élasticité IS » (T18 point 18)

- **Constat.** Inchangé. Les mesures d'assiette (`report_deficits_is_2012`, `bmc_suppression_2012`) sont des réestimations et sortent de la statistique ; il reste 2 cas observés, de sens opposés (« trop peu de cas »). On ne sait pas si les ex ante d'IS intègrent déjà un comportement (risque de double compte). Dans les programmes, `rn24_armateurs` (1,1) est une mesure d'assiette qui reçoit le facteur 0,94.
- **Fichiers.** `data/raw/regles.csv`, `data/raw/moteur_parametres.csv` (`facteur_is`), `data/raw/familles.csv`, `data/raw/application_lignes.csv` (`rn24_armateurs`).
- **Nature.** Règle. **Effet : faible**, moins de 0,1 Md€ (1,1 × 0,06 sur RN 2024).
- **Action.** Écrire le champ (taux ou assiette). Garder la règle pour une mesure d'assiette qui ramène des bénéfices à l'IS, avec la raison dans `exception_symetrie` ou dans la base de la règle.
- **Exécution.** Direct.

### G2.5 Indépendance des cas : plusieurs lignes du même dispositif dans la statistique (T18 point 7)

- **Constat.** Toujours vrai (`mesures_cout.csv`, `inclus_stats` = 1 et drapeau `meme_dispositif` ou `meme_plan`) : `cheque_energie_gen_2018` et `cheque_energie_elarg_2019` (« Taux de recours ») ; `bouclier_60_2007` et `bouclier_suppr_2012` (« Élasticité patrimoine », 9 cas, « mitigée ») ; `aej_2020` et `aide_contrat_pro_2020` (même plan #1jeune1solution). La décision du 16/10/2026 sort de la statistique les « années suivantes d'un même dispositif » (`recherche/T18/rapport.md` § 6). Or ces paires sont des mesures distinctes (généralisation puis élargissement ; création puis suppression ; deux aides). Aucun texte ne le dit.
- **Fichiers.** `data/raw/mesures_cout.csv`, `recherche/validation/README.md`.
- **Nature.** Règle (critère) et texte. **Effet : aucun sur le solde.** L'effet sur la statistique publiée est faible. Sans `bouclier_suppr_2012`, « Élasticité patrimoine » aurait 4 cas améliorés et 4 dégradés : elle reste non confirmée.
- **Action.** Écrire le critère dans le README (« un cas par mesure ; deux réformes distinctes d'un même dispositif comptent séparément ; une année suivante de la même mesure ne compte pas »), puis vérifier chaque paire.
- **Exécution.** Direct.

### G2.6 Rattachements alternatifs non tranchés (T18 point 24)

- **Constat.** L'attribution à l'aveugle a été copiée telle quelle (`bouclier_60_2007` en « Élasticité patrimoine », effets de volume, `bouclier_60_benef`). Les rattachements à « Taux de recours » proposés par les groupes n'ont été ni adoptés ni écartés par écrit.
- **Fichiers.** `data/raw/validation_attribution.csv`, `data/raw/mesures_cout.csv` (drapeaux `autre_regle_possible`), `recherche/validation/README.md`.
- **Nature.** Règle. **Effet : aucun sur le solde.** Les statuts d'« Élasticité patrimoine » et de « Taux de recours » pourraient changer.
- **Action.** Écarter par écrit : l'attribution à l'aveugle fait foi, faute de quoi le test perd son intérêt. Publier, à côté, la variante avec les rattachements alternatifs (les drapeaux `autre_regle_possible` existent déjà).
- **Exécution.** Direct.

### G2.7 Enveloppes des dispositifs d'urgence prises comme chiffrage (T10a point 2)

- **Constat.** Partiel. `bouclier_gaz_2023` et `cheque_fioul_2022` sont hors statistique. Les chèques énergie exceptionnels de 2021 et 2022 y sont (règle « Aucune », inchangés). La variante « sans les crédits votés » (`validation.py:179`) ne couvre que le drapeau `credit_vote`, posé seulement sur les cas de T18. Aucun texte ne dit si une enveloppe ouverte en urgence est un « chiffrage ».
- **Fichiers.** `data/raw/mesures_cout.csv` (drapeaux), `scripts/validation.py:179`, `recherche/validation/README.md`.
- **Nature.** Règle et texte. **Effet : aucun sur le solde** ; un effet faible sur l'erreur médiane publiée de la couche 1.
- **Action.** Écrire le critère (une enveloppe est un chiffrage si elle est votée avec un coût unitaire et un nombre de bénéficiaires). Poser `credit_vote` sur les cas plus anciens qui le remplissent, pour que la variante couvre tout l'échantillon.
- **Exécution.** Direct.

### G2.8 Cas de la DLF classés `observe` malgré la convention (T18 point 9)

- **Constat.** `tranche45_2013`, `qf_2013` et `frais_pro_2013` restent `observe` et dans la statistique. Le README (l. 16) classe pourtant en `reestimation` une mesure « fondue dans un impôt existant », dont le coût après coup est un nouveau chiffrage.
- **Fichiers.** `data/raw/mesures_cout.csv`, `recherche/validation/README.md`.
- **Nature.** Règle (classement). **Effet : aucun sur le solde.** « Élasticité revenus » passerait de 3 à 2 cas et resterait « trop peu de cas ».
- **Action.** Relire la source DLF de chaque cas et appliquer la convention. Passer les lignes en `reestimation` par `appliquer_corrections.py` si le réalisé est bien un rechiffrage.
- **Exécution.** Direct (sources archivées en T18).

### G2.9 Indicateur du test « Recette ponctuelle » (T18 point 23 et § 5)

- **Constat.** Toujours « Indicateur à définir » (`validation.py:58-60`), statut « non concluante », 6 cas. La durée réelle des recettes est déjà notée (restée ponctuelle : CEF, stocks pétroliers, surtaxe d'IS 2017 ; prolongée : STDR, contribution de 5 % sur l'IS, CRI…). Celle de la CEHR n'est pas vérifiée.
- **Fichiers.** `scripts/validation.py` (`NON_CONCLUANTES`), `data/raw/mesures_cout.csv` (notes de durée).
- **Nature.** Code et règle. **Effet : aucun** (règle hors de l'indicateur « part confirmée » et facteur 0 inchangé).
- **Action.** Définir l'indicateur « recette encore perçue à N+2 » (oui ou non) et compter les cas où la règle (recette nulle à terme) a raison. Vérifier la durée de la CEHR, perçue sans interruption depuis 2012.
- **Exécution.** Direct ; la date de fin de la CEHR se lit au BOFiP (même lecture que G3.2).

### G2.10 Écrire les choix faits sans trace (T18, T10b, T21)

- **Constat.** Plusieurs valeurs de la fusion sont en place sans texte ni entrée du journal :
  - T18 points 3, 4, 5, 12, 13 et 14 (`cehr_2012`, `cri_2023`, `contrib_stocks_petroliers_2012`, taxe de 3 % nette, `ticfe_baisse_2022` 6,4, `indemnite_carburant_2023` 0,433) ;
  - T10b points 2 et 3 (OFCE gardé ; lignes à réalisé dérivé : fonction publique et redevance incluses, PFU exclu) ;
  - T21 point 13 (succession en `medium`) ;
  - `ac_2021` (T18 point 22), sans objet de fait : ligne `low` et `reestimation`, deux motifs d'exclusion actuels.
- **Fichiers.** `recherche/validation/README.md` (une section « Choix de la fusion »), notes des lignes dans `mesures_cout.csv` (voir G5.5).
- **Nature.** Texte. **Effet : aucun.**
- **Action.** Une phrase par choix, avec le motif. Pas de changement de valeur.
- **Exécution.** Direct.

---

## 3. Paramètres

Fichiers communs : `data/raw/moteur_parametres.csv`, `data/raw/hypotheses_defaut.csv`, `data/raw/elasticites.csv`, `data/raw/parametres_bareme.csv`, `data/raw/projection_parametres.csv`, `scripts/distributif.py`.

### G3.1 Smic 2026 dans « Mon foyer » (T4p point 2)

- **Constat.** Aucune décision n'est écrite. `scripts/distributif.py:35-37` prend le Smic d'OpenFisca au 1er janvier 2026 (1 823,03 € brut). Le Smic a été revalorisé au 1er juin 2026 : 1 867,02 € brut, 1 477,93 € net (`parametres_bareme.csv:107-108`). La réforme `smic_1600` (type `smic_net_cible`) relève les salaires du rapport 1 600 / Smic net actuel (`distributif.py:287-292`). D'après `parametres_bareme.csv`, la hausse simulée serait d'environ 10,9 % sur la base de janvier (1 443,11 € net), contre 8,3 % sur celle de juin. Le moteur garde, lui, la base 2024 du chiffrage Montaigne (`hausse_smic`, `hausse_moy_smic`), ce qui est cohérent avec le chiffreur.
- **Fichiers.** `scripts/distributif.py`, `data/raw/distributif_reformes.csv` (`smic_1600`), sortie `data/distributif_menages.csv`.
- **Nature.** Code et décision technique. **Effet : oui.** Pour le « salarié au SMIC, célibataire », la réforme rapporte aujourd'hui +1 293 €/an ; la part salariale de ce gain baisserait d'environ un quart, montant exact à recalculer. Les autres cas-types payés au Smic bougent un peu.
- **Action.** Choisir la valeur en vigueur à la date du calcul (juin 2026) ou la moyenne annuelle (1 463,4 € net, dérivée en T4p). Vérifier que la version d'OpenFisca installée connaît la valeur de juin, sinon la fixer depuis `parametres_bareme.csv`. Écrire le choix dans la section « Méthode » de « Mon foyer ».
- **Exécution.** Direct.

### G3.2 Assiette de la CEHR sur les dividendes (T4p point 4)

- **Constat.** Le central de `t1_capital` (46,27 %) assied la CEHR sur 100 % du dividende ; la borne basse suit France Stratégie (60 %, 44,78 %). La vérification au BOFiP demandée par T4p n'est pas attestée : T4p écrit « Le RFR réintègre l'abattement de 40 % (BOFiP) » sans source CEHR archivée. Seule la fiche service-public F31130 l'est. `parametres_bareme.csv:132` dit encore « Écart à trancher ».
- **Fichiers.** `data/raw/moteur_parametres.csv` (`t1_capital`), `data/raw/parametres_bareme.csv:132`, `recherche/T4p/sources.csv`.
- **Nature.** Recherche. **Effet : oui, faible.** Le facteur « Élasticité capital » passerait de 0,437 à 0,457 (formule de `moteur.py:47`) : +0,07 Md€ sur `l_pfu_i` (panier LFI) et +0,06 sur `nfp_flat` (NFP 2024).
- **Action.** Lire la fiche BOFiP de la CEHR (BOI-IR-CHR), section sur l'assiette (revenu fiscal de référence), l'archiver, puis figer le central et corriger la note de la ligne 132.
- **Exécution.** Sous-agent (Légifrance est bloqué ; le BOFiP s'ouvre, voir `recherche/T4p/parts/B_notes.md:19`).

### G3.3 Hypothèse de « Mon foyer » pour la part fiscale entière dès le 2e enfant (T20 § 9)

- **Constat.** Toujours « Pas encore simulé : le programme ne précise pas le plafond du quotient familial » (`non_chiffre_foyer.csv:8`). C'est la mesure `rn24_part_fiscale`, liée à G2.1.
- **Fichiers.** `data/raw/distributif_reformes.csv`, `data/raw/non_chiffre_foyer.csv`, `scripts/distributif.py`.
- **Nature.** Décision technique (hypothèse) et code. **Effet : oui**, un nouveau montant par foyer pour les familles de deux enfants ou plus. Le solde ne change pas.
- **Action.** Simuler avec le plafond actuel par demi-part, lu dans OpenFisca, et le dire sur la fiche. Donner en variante le cas sans plafond.
- **Exécution.** Direct.

### G3.4 Second indicateur du biais des programmes de stabilité, l'EFB (T2b point 2)

- **Constat.** Ouvert. `biais_pstab_efb` n'existe nulle part ; seuls `biais_t1` (−0,60) et `biais_t3` (−1,93) servent (`projection_parametres.csv:3-4`, `projection.py:62`). T2b a calculé, sur la première publication, −0,40 à −0,54 à 1 an et −1,85 à 3 ans, hors crises. Le classeur est archivé (`sources/T2b/EFB_Forecast_Tracker.xlsx`).
- **Fichiers.** `data/raw/projection_parametres.csv`, `scripts/projection.py`, `recherche/T2b/rapport.md` § 1.3.
- **Nature.** Décision technique (méthode). **Effet : aucun** si l'indicateur est affiché comme variante. S'il remplaçait la valeur actuelle, la trajectoire publiée bougerait de 0,1 à 0,2 point de PIB à 1 an.
- **Action.** L'ajouter en variante (« biais mesuré sur la première publication »), à côté de l'actuel, sans changer le central. Le rapporter dans la page « Méthode ».
- **Exécution.** Direct.

### G3.5 Texte de `h_charges` fondé sur Crépon-Desplatz (T2b point 6)

- **Constat.** Partiel. `charges_bw_1216` comble l'interpolation de 1,3 à 1,6 SMIC (hist. 56). `charges_smic` (+1,6 à +1,8 % d'emploi par point de coût, `elasticites.csv:18`) n'a pas été réexaminé. Bozio-Wasmer jugent −0,6 au SMIC plus plausible (`charges_bw_smic`, `elasticites.csv:70`). `charges_smic` n'entre dans aucune formule : seul le texte publié de `h_charges` le cite (`hypotheses_defaut.csv:6`).
- **Nature.** Texte. **Effet : aucun montant**, mais un texte publié.
- **Action.** Ajouter `charges_bw_smic` aux références de `h_charges` et dater Crépon-Desplatz (années 1990) dans le texte.
- **Exécution.** Direct.

---

## 4. Cartes « idées qui reviennent » (T16)

Fichiers communs : `data/raw/idees.csv`, `data/raw/idees_chiffres.csv`, `recherche/T16/idees.md`, `web/site.js` (repères, l. 925-932). Ces points changent les cartes, pas les soldes des programmes.

### G4.1 [Utilisateur] Appliquer ou non les règles du backtest aux estimations des cartes

- **Constat.** Les cartes affichent les chiffres bruts de leurs sources. Une règle n'est appliquée qu'aux lignes du moteur citées par une carte (par exemple `paniers/l_succ_i`, `paniers/e_fp_e`). Deux points du croisement en dépendent : G4.2 et G4.3.
- **Nature.** Décision de présentation. **Effet : oui** sur les cartes concernées.
- **Action proposée.** Garder le chiffre de la source comme valeur principale et ajouter, sous la carte, « avec la règle du site : … » quand une famille et sa règle s'appliquent. Même traitement pour toutes les cartes.
- **Exécution.** Direct, après la décision.

### G4.2 Fonctionnaires : aucune règle appliquée au coût des 250 000 postes (T16 A point 2)

- **Constat.** Les deux calculs (7,75 et 13,6 Md€, confiance `low`) sont affichés. Seul un rappel de 2017 figure dans « peut-on s'y fier ? ».
- **Nature.** Règle (« Réforme structurelle », facteur 0,842). **Effet : oui** sur la carte (environ 6,5 à 11,5 avec la règle), selon G4.1.
- **Action et exécution.** Selon G4.1 ; direct.

### G4.3 Héritages : la règle « Élasticité succession » n'est pas appliquée au chiffre du CAE (T16 C point 4)

- **Constat.** La carte affiche « plus de 10 Md€ en état stationnaire » (CAE, note n° 69), sans règle. La règle (0,9) ne s'applique qu'à `l_succ`.
- **Nature.** Règle. **Effet : oui** sur la carte (« plus de 9 »), selon G4.1.
- **Action et exécution.** Selon G4.1 ; direct.

### G4.4 Solde net de la France avec l'UE : donnée 2024 (T16 A point 5)

- **Constat.** Le versement 2027 vient du PLF 2027, art. 55 (`ue`, ordre 1). Le solde net (−7,9 Md€, `ue`, ordre 2) vient encore du rapport AN sur le PLF 2026 (données 2024), en confiance `medium` : le jaune n'a pas été lu.
- **Nature.** Recherche. **Effet : oui** sur la carte.
- **Action.** Lire le jaune « Relations financières avec l'Union européenne » annexé au PLF 2027 et prendre le dernier solde net exécuté (hors plan de relance), en `high`.
- **Exécution.** Sous-agent.

### G4.5 Carburants : coût d'un centime calculé, pas lu (T16 C point 3)

- **Constat.** Toujours 0,475 Md€/an, calculé (47,5 Mm³ × 0,01 €, Ufip), confiance `medium` (`carburants`, ordre 1).
- **Nature.** Recherche. **Effet : oui** sur la carte.
- **Action.** Chercher un chiffrage officiel du coût d'un centime d'accise (DGEC, Sénat, rapport sur la fiscalité des énergies), ou à défaut garder le calcul et le recouper avec l'accise brute (`carburants`, ordre 3).
- **Exécution.** Sous-agent.

### G4.6 [Utilisateur] Repère « € par habitant » (T16 B point 5, C point 5)

- **Constat.** Seul le « % du déficit » est calculé (`web/site.js:925-932`). `recherche/T16/idees.md:9` demande l'un « ou » l'autre.
- **Nature.** Décision de présentation. **Effet : aucun montant.**
- **Action proposée.** Clore : le « % du déficit » remplit la consigne. Un « € par habitant » côtoierait l'indicateur par foyer, que la décision du 15/10/2026 réserve aux programmes (« jamais déduit du gain personnel »).
- **Exécution.** Direct.

---

## 5. Notes périmées

Toutes ces corrections passent par `scripts/appliquer_corrections.py` (`data/raw/`) ou par une simple édition (`recherche/`). Aucune ne change un montant, mais G5.1 à G5.6 corrigent des textes publiés (fiches « Pourquoi ce chiffre ? », registre 2027, notes du backtest).

### G5.1 `rn24_preference_nationale` : justification d'avant T23

- `application_lignes.csv:77` dit « application de la règle discutable, voir rapport ». T23 a tranché (règle « Aucune », risque affiché sans correction ; hist. 596-597, `2c0948c`). Réécrire la justification. Direct.

### G5.2 `rn24_part_fiscale` : « Règle discutable… voir rapport »

- `application_lignes.csv:64`. À réécrire après G2.1, avec la règle retenue. Direct.

### G5.3 `e_oper` : « à arbitrer » alors que T26 a confirmé le facteur 1

- `paniers.csv:32`, `note_reference` : « facteur 1 par défaut, à arbitrer ». T26 (§ 6) a confirmé 1 (le PLF 2027 ne chiffre aucune fusion ni suppression d'opérateur), mais la note n'a pas été mise à jour. Direct.

### G5.4 Registre 2027 (`statut_reference_2027.csv`) : notes d'avant les décisions

- `l_ret62_a` (l. 26) : « décision laissée à l'intégrateur (−6,9 ou −7,3) » ;
- `l_smic_i` (l. 27) : « à réexaminer par l'intégrateur » ;
- `l_isf_i` (l. 35) : facteur 0,96 et « déjà net de l'IFI (3,08) » ;
- `rn24_production` (l. 61) : « Non compté ici : à arbitrer » (CVAE), alors que la convention du droit de juin 2024 rend la question sans objet (T25, `rapport.md:36`) ; pas de `raison_ecart`.

Les trois premières ont une `raison_ecart` juste, mais la `note` contredit la décision. Réécrire les quatre notes et ajouter la `raison_ecart` de `rn24_production`. Direct.

### G5.5 Notes du backtest qui attendent un « choix de l'intégrateur »

- `mesures_cout.csv` : `indemnite_carburant_2023` (« choix de l'intégrateur entre 277 et 433 », 0,433 retenu), `ticfe_prolongation_2023` (« à exclure si… », exclue), `isf_reforme_2013` (exclue), `stdr_2014` (« sans décision de l'intégrateur », un seul cas compté, hist. 316), `us_rachats_1pct_fy2024` (« À l'intégrateur de dire… », sous-échantillon étranger). Écrire la décision prise dans chaque note. À faire avec G2.10. Direct.

### G5.6 `calibration_instituts.csv` : « test de la médiane, pas encore calculé »

- La colonne `inclus_stats` des chiffrages de 2007 et 2012 dit « pas encore calculé ». T21 § 8 dit « non jugeable ». Aligner le texte (après G2.3). Direct.

### G5.7 Lignes d'état des rapports T18 et T20, et sections « Décisions laissées » des autres rapports

- `recherche/T18/rapport.md:3` (« Rien n'est intégré à `data/` ; la phase 4 reste à décider ») et l. 24 (« les 27 décisions … ne sont pas tranchées »). Le § 6 décrit pourtant l'intégration (`f32e017`).
- `recherche/T18/rapport_fusion.md` § 6 : 27 points sans statut.
- `recherche/T20/rapport.md:3` (« Brouillon … L'attribution à l'aveugle reste à faire … Rien n'est intégré à `data/` »), l. 156 (« Rien n'est tranché ») et § 5 point 10, qui décrit un `validation.py` dépassé (il ne juge plus que sur `observe` depuis `e17e777`). Le § 9 décrit l'intégration.
- Sections « Décisions laissées à l'intégrateur » sans statut : T2b § 5, T4p, T10a § 6, T10b § 8, T16 A à D, T17 § 6 et § 9, T21 § 6, T22 § 5.

Action : ajouter en tête de chaque rapport une ligne datée (« État au 01/11/2026 : intégré le …, voir § … ; points restants : `recherche/T27/suivi.md` »), sans réécrire le rapport, qui garde sa valeur d'archive. Direct.

### G5.8 Textes 2027 en cours d'examen

- Le PLFSS 2027 a été rejeté par l'Assemblée le 23/10/2026 (T.A. n° 358) ; le Sénat examine le texte initial à partir du 09/11 (`recherche/T26/rapport_integrateur.md` § 3). Les cartes et les lignes qui en dépendent disent « proposé », ce qui reste exact : `idees.csv` (`annee_blanche`, `desindexation_pensions`), `paniers.csv` (`e_pens`, `e_abat`, `e_carence`), le registre 2027.
- Action : dater l'état de la procédure là où il compte (« projet ; rejeté en première lecture à l'Assemblée le 23/10/2026 »), et prévoir une revue complète du statut de référence après l'adoption des textes 2027 (fin décembre). `e_carence` est à revoir après le 19/12/2026. Direct, avec une lecture du texte adopté le moment venu (sous-agent).

### G5.9 Fragilités non dites dans les justifications

- `nfp_indexation_salaires` (10,5) et `nfp_point_indice` (20) : deux hausses du point que Montaigne additionne (T22 § 5.3, gardées de fait). Le cas est le même que celui de `nfp_cotis_vieillesse` (T26 n° 8) : les deux lignes ont la règle « Aucune » et un facteur 1, donc le total NFP ne bouge pas. Écrire la fragilité dans la justification, comme en T26.
- `rn24_heritage` (reliquat T26 § 8) : 1 Md€ sans méthode publiée par Montaigne. **En cours** : justification réécrite dans `data/raw/application_lignes.csv`, non commitée. Reste à faire : les deux lignes NFP.

---

## 6. Pistes de recherche jamais explorées

### G6.1 [Utilisateur] Effet des programmes sur l'économie (ticket #3)

- **Constat.** Ouvert. Seuls « Effet promis » et les lignes `*_taux` bouclent sur l'économie. Le ticket propose une variante à multiplicateurs publiés, la même pour tous les programmes, avec relecture par un économiste extérieur. `hypotheses_defaut.csv` (`h_macro` : `mult_dep`, `mult_imp`, `semi_elast`) contient déjà des valeurs sourcées (T2b point 5).
- **Nature.** Décision de périmètre, puis recherche et code. **Effet : oui**, une nouvelle variante publiée, qui peut dépasser l'ensemble des corrections ligne à ligne.
- **Décision demandée.** Lancer ou non ce chantier, accepter ou non la dépendance à un relecteur extérieur, et dire si la variante est publiée avant 2027.
- **Exécution.** Sous-agent (multiplicateurs par type de dépense et de recette, à court et moyen terme), puis direct.

### G6.2 [Utilisateur] Couverture : partis absents, présidentielle 2027, horizon au-delà de 2032 (ticket #7)

- **Constat.** Ouvert. Les paniers 2027 ne couvrent que LFI et Ensemble ; `modeles/programme_2027.csv` est vide ; la projection s'arrête en 2032.
- **Nature.** Décision de périmètre et de calendrier (quels partis, quel délai, même protocole), puis recherche. **Effet : nouveaux chiffres publiés.**
- **Décision demandée.** Protocole et date d'intégration communs, et liste des partis sans programme chiffrable.
- **Exécution.** Sous-agent par programme, au moment de sa publication.

### G6.3 Calibration des instituts : élargir l'échantillon (T10b point 4, T21 § 4)

- **Constat.** Partiel. Les campagnes 2007 et 2012 sont hors statistique. Plusieurs réalisés manquent : ASPA, ASF, PPV, CVAE (T10b) ; pour 2012, heures supplémentaires, abattement de succession, emplois d'avenir, carrières longues, TTF (T21 § 4). C'est cet échantillon qui fixe `erreur_ligne` (central 14,9 %, n = 22).
- **Fichiers.** `data/raw/calibration_instituts.csv`, `data/raw/moteur_parametres.csv` (`erreur_ligne`).
- **Nature.** Recherche. **Effet : possible** sur les fourchettes de tous les programmes (P10-P90), par `erreur_ligne`.
- **Exécution.** Sous-agent.

### G6.4 Nouveaux cas pour les règles à moins de 5 cas (T18 point 27)

- **Constat.** Non explorées : CSPE, ex post de la complémentaire santé solidaire, NEB du CAS « véhicules propres », assurance chômage 2019 et 2023, garantie jeunes, fiscalité du tabac 2018-2020, suramortissement 2019, objectif Duflot. T21 a déjà cherché sans succès la contribution d'IS de 10,7 %, la taxe à 75 %, les prélèvements sociaux et les DMTG de 2012.
- **Nature.** Recherche. **Effet : possible** sur les statuts, donc sur la « part confirmée ». Il faut viser d'abord les règles qui pèsent dans cet indicateur : « Élasticité revenus », « Élasticité IS », « Élasticité succession », « Réforme structurelle », « Substitution retraites » (`validation_regles.csv`).
- **Exécution.** Sous-agent, avec le protocole de T18 (attribution à l'aveugle).

### G6.5 Backtest : sous-indexation des pensions 2019 et bascule CSG 2018 (T10a point 5)

- **Constat.** Toujours absentes de `mesures_cout.csv`. Ce sont deux grandes mesures, proches de lignes des paniers (indexations, CSG).
- **Nature.** Recherche. **Effet : possible** sur la statistique de la couche 1 ; ces mesures relèvent surtout de règles à facteur 1 (« Aucune »).
- **Exécution.** Sous-agent.

### G6.6 Recherches de T2b interrompues (budget épuisé)

- Non-recours aux APL et à l'AAH ; non-recours à la CSS après 2021 (`nr_css` date de 2022) ; rapports annuels de l'EFB (`recherche/T2b/rapport.md` § 4). Pour le document de Lefebvre, Lehmann et Sicsic, voir R1. **Effet : aucun direct** (`h_recours` est un texte ; l'AAH est en règle « Aucune »). Sous-agent.

### G6.7 « Mon foyer » : TVA hors énergie (T20 § 6.1)

- La table « poste de consommation → taux de TVA » n'est pas construite ; l'alimentation reste non calculée (`non_chiffre_foyer.csv`, « Liste des produits non publiée »). **Effet : nouveaux montants par foyer** pour les mesures de TVA. Recherche (taux par poste COICOP) puis code. Sous-agent.

### G6.8 « Mon foyer » : autres mesures « Pas encore simulé »

- `non_chiffre_foyer.csv` : APL non revalorisées en 2027, point d'indice gelé ou relevé, revalorisation des enseignants et des agents publics, garantie d'autonomie des jeunes, métiers du soin, travail de nuit à l'hôpital, dons familiaux. **Effet : nouveaux montants par foyer.** Il faut d'abord décider quels cas-types ajouter (agent public, jeune adulte). Code, avec une recherche ponctuelle pour certains barèmes. Direct pour la plupart.

### G6.9 TTF : paramètre du relèvement de 2025

- `rendements_leviers.csv` (`ttf_relevement_2025`) : « à vérifier dans la LFI 2025 avant de l'extrapoler ». **Effet : aucun** aujourd'hui (rendement réalisé cité seulement). Sous-agent, en passant.

### G6.10 Cas SMIC espagnol : millésime de l'AIReF (T21 point 6)

- Le cas n'est pas utilisé. Proposition : clore sans action, avec une phrase dans `recherche/T21/` (fait par G5.7).

---

## 7. Reliquats du groupe 1 (pour mémoire)

Laissés ouverts par `recherche/T26/rapport_integrateur.md` § 8 et § 9, ou relevés en T26 comme questions distinctes. Au moment de la rédaction, R1, R2 et R5 sont en cours de traitement : modifications non commitées dans `data/raw/`, plus `recherche/T26/parts/*_C.*` et `recherche/T26/relecture/`. Ils peuvent changer un chiffre publié et sont à traiter avec le groupe 1, pas dans ce plan.

| Id | Point | Effet | Exécution |
|---|---|---|---|
| R1 | `eps_capital` (0,77) sans intervalle : lire l'intervalle de Lefebvre, Lehmann et Sicsic (2024). **En cours** : bornes 0,5 et 1,17 écrites dans `data/raw/moteur_parametres.csv`, non commitées (`recherche/T26/parts/notes_C.md`). Leur note dit « seule nfp_flat utilise ce paramètre », alors que `l_pfu_i` (panier LFI) passe aussi par le moteur (`data/moteur_lignes.csv:100`) : à corriger | fourchettes de NFP 2024 et du panier LFI | en cours |
| R2 | Relecture du modèle de l'agent A pour `l_bandeaux` (0,4, confiance `low`) par quelqu'un d'autre que son auteur (CONTRIBUTING, règle 2) | panier LFI, 1,1 Md€ par 0,1 de facteur | en cours (`recherche/T26/relecture/`) |
| R3 | `l_brunes` : le même périmètre coûte 6,6 Md€ au PLF 2027, contre 6,05 au PLF 2025 (T26 § 6, « question distincte ») | panier LFI, environ +0,5 Md€ en statique si la ligne était rechiffrée ; contraire à la règle du montant du chiffreur, donc probablement à écarter avec motif | direct |
| R4 | `e_carence` (0,5) : à revoir après la négociation des partenaires sociaux (au plus tard le 19/12/2026) | panier Ensemble, jusqu'à 0,5 Md€ | sous-agent, après le 19/12 |
| R5 | Médecins en formation (0,1 dans `ens_autres_dep_reste`) : part déjà dans la référence. **En cours** : facteur 0,863 → 0,853, non commité | Ensemble 2024, 0,1 au plus | en cours |

---

## 8. Points écartés : réglés depuis le croisement ou sans objet

- **T2b point 3, `h_cir`** : corrigé le 01/11/2026 (« ≈1 € de R&D par € en moyenne… », `recherche/audit/corrections_notes.csv`, `0ff7a16`).
- **T2b point 7, `h_recours`** : la CSS (0,56, `nr_css`) est ajoutée (même commit). Le 61 % de l'AAH n'est pas utilisé, comme T2b le recommandait.
- **Audit n° 5, source et notes de `l_ret62` et `l_ret60`** : corrigées (`paniers.csv:2-3`, `0ff7a16`). L'asymétrie de la décote des retraites est écartée avec motif (T26 n° 2).
- **Audit n° 8, `a_sur_da_niches`** : écarté avec motif (T26 § 5). `hausse_smic` ne sert plus qu'à une règle conservée pour l'historique (`moteur_regles.csv`). Pour `eps_capital`, voir R1.
- **Audit n° 9, variante `l_rachats` à 0,5 Md€** : écartée avec motif (T26 § 5).
- **Audit n° 13, `l_brunes` et `e_oper`** : traités (T26 n° 6 ; `e_oper` confirmé). Seule la note de `e_oper` reste à corriger (G5.3).
- **Audit n° 14, note de `l_bandeaux` calculée sur 12,1** : note réécrite par T26 (n° 5).
- **Audit n° 17** : l'écart est expliqué par `raison_ecart` ; les notes périmées du registre sont en G5.4.
- **Audit n° 21 et T1 point 5, variante « loi votée seule »** : colonne `facteur_reference_loi_votee` (T26 n° 3).
- **T17 § 6-3, `rn24_audiovisuel`** : l'horizon « 3 à 5 ans » est désormais affiché dans la fiche (T26 n° 4).
- **T22 § 5.4 à 5.7 (`rn24_asile`, `ens_agents_publics`, `ens_leasing`, `nfp_niches` contre exemptions, horizons)** : traités en T26 (§ 4, 5 et 7). `rn24_heritage` est en G5.9.
- **T22 § 5.3, PTZ RN et `rn24_taux`** : traité (T26 n° 1).
- **T18 point 22, `ac_2021`** : sans objet (ligne `low` et `reestimation`) ; à écrire en G2.10.
- **T4p points 1, 3, 5, 6 et 7 ; T21 points 1 à 5, 7, 9 à 12 et 14 ; T20 § 6.2 à 6.5 ; T23 ; T24 ; T25 § 4 et 7** : tranchés, d'après les relevés du croisement, revérifiés dans les fichiers cités.

## 9. Bilan du groupe 2 (01/11/2026)

| Point | Fait | Effet |
|---|---|---|
| G2.1 | Famille `impot_revenu_large` (règle « Aucune », élasticité moyenne 0,05) pour `rn24_part_fiscale` et `rn24_ir_jeunes` ; champ de « Élasticité revenus » écrit (`G2/corrections_regles.csv`) | RN 2024 −52,86 → −53,57. Rattachement à faire relire par une autre personne |
| G2.2 | 2 cas à recours complet seulement (ACS 2005, ATI 2020) : version restreinte toujours non testée, note mise à jour. Décote « recours partiel déjà compté » : 0,81 sur 3 dispositifs, présentée dans `G2/notes.md`, règle inchangée | aucun |
| G2.3, G2.4 | Règles « Médiane des estimations » et « Élasticité IS » écrites dans leur base | aucun |
| G2.5, G2.6, G2.7, G2.10 | Critères et choix de la fusion dans `recherche/validation/README.md` ; 7 doublons hors statistique, 3 drapeaux `credit_vote` (`G2/corrections_paires.csv`). Variante des rattachements alternatifs simulée, non publiée | statistique sur le passé seulement |
| G2.8 | `tranche45_2013`, `qf_2013`, `frais_pro_2013` en `reestimation` (`G2/corrections_dlf.csv`) | « Élasticité revenus » : 2 cas observés |
| G2.9 | Indicateur « recette encore perçue à N+2 » dans `validation.py` : « Recette ponctuelle » confirmée (5 cas sur 6). CEHR perçue sans interruption depuis 2012 (BOFiP) | aucun sur le solde |
| G3.2 (fait en passant) | CEHR sur 100 % du dividende (RFR) : central de `t1_capital` conforme ; la borne basse France Stratégie ne correspond pas au droit (à traiter au groupe 3) | — |

Reste ouvert : 3 cas de plus à recours complet (RSA jeunes, chèque bois, aide aux étudiants : hypothèse de recours à confirmer), coût réalisé de la CMU-C 2000.

## 10. Bilan du groupe 3 (01/11/2026)

| Point | Fait | Effet |
|---|---|---|
| G3.1 | « Mon foyer » prend le Smic en vigueur depuis le 1/6/2026 (OpenFisca 176.1.4, contrôlé contre `parametres_bareme.csv`) ; dit dans « Limites de ce calcul » | `smic_1600` : salarié au Smic 1 293 → 982 €/an ; monoparental 1 403 → 1 092 |
| G3.2 | CEHR sur 100 % du dividende (RFR, BOFiP) : central de `t1_capital` confirmé, borne basse 42,54 % → 45,34 % (CEHR 3 %) | fourchettes de `nfp_flat` et `l_pfu_i` seulement |
| G3.3 | `rn24_part_fiscale` simulée (2e enfant à une part, plafond de 1 807 € par demi-part) ; retirée de `non_chiffre_foyer.csv` | couple, 2 enfants : 0 à 1 807 €/an. À vérifier : gain non croissant avec le revenu entre 1,5 et 2 Smic (883 € puis 850 €), probablement un effet de seuil |
| G3.4 | Variante du biais mesuré sur la première publication (EFB) : −0,43 à 1 an, −1,72 à 3 ans ; `data/projection_variantes.csv` ; phrase dans « Méthode » | central inchangé ; dette 2032 corrigée 129,1 % au lieu de 130,3 % dans la variante |
| G3.5 | `h_charges` : Crépon-Desplatz daté, `charges_bw_smic` ajouté | texte seulement |

Corrections : `G3/corrections_parametres.csv` ; scripts `distributif.py`, `projection.py` ; historique tenu à la main pour les fichiers hors `appliquer_corrections.py`.

## 11. Bilan du groupe 4 (01/11/2026)

| Point | Fait | Effet |
|---|---|---|
| G4.1 (décision de l'utilisateur, 01/11/2026) | Colonne `famille` dans `idees_chiffres.csv`, pour les seuls chiffres qui prévoient le rendement ou le coût d'une mesure ; sous chaque carte, « Avec la règle du site (« règle », × facteur) : … », même facteur que dans les programmes ; contrôle dans `garde_fous.py` | 5 chiffres corrigés à l'affichage, chiffre de la source gardé en principal |
| G4.2, G4.3 | Fonctionnaires (« Réforme structurelle », 7,8 → 6,5 et 14 → 11) ; héritages CAE (« Élasticité succession », plus de 9) | cartes |
| G4.4 | Solde net avec l'UE : −7,9 (2024, medium) → −9,5 Md€ (2025, jaune PLF 2027, méthode comptable, high) ; méthode de la Commission (−6,4) dans la note ; dépenses de l'UE en France 16,391 (2025) ; textes de la carte mis à jour | carte |
| G4.5 | Coût d'un centime : 0,475 gardé (calcul), recoupé par les volumes DGEC 2024 (0,477) ; aucun chiffrage officiel récent | carte (note) |
| G4.6 | En attente de l'utilisateur ; proposition : clore, le « % du déficit » suffit | — |

Choix de l'intégrateur à signaler : « recettes attendues du plan contre la fraude » (1 Md€) dans la famille `effet_promis`, comme `ens_fraude` (× 0,33).

## 12. Bilan du groupe 5 (01/11/2026)

- G5.1, G5.3, G5.4, G5.5, G5.8, G5.9 : 20 corrections de textes publiés (`G5/corrections_notes.csv`), aucune valeur chiffrée ne change ; `nfp_indexation_salaires` et `nfp_point_indice` passent en confiance medium (fragilité dite). G5.2 était déjà fait (G2.1).
- G5.4 : note de `l_bandeaux_i` au registre alignée sur celle du panier (`G5/corrections_registre.csv`).
- G5.6 : 32 lignes de `calibration_instituts.csv`, « non jugeable » (journal écrit à la main).
- G5.7 : ligne d'état datée en tête de 14 rapports ; T21 point 6 (G6.10) clos sans action. 10 points de `T18/rapport_fusion.md` § 6 hors de ce suivi renvoient au journal du 16/10.
- Reste à vérifier : la prolongation du gel du SMIC de référence est dite « proposée par le PLFSS 2027 » dans plusieurs fichiers, mais la citation lue vient du PLF 2027 (art. 49). Si elle passe par le PLFSS, le rejet à l'Assemblée la touche aussi. La date d'examen au Sénat (09/11) ne vient que d'une source secondaire. Carte `etrangers_prestations` : proposition dans `G5/notes.md`, non appliquée.
