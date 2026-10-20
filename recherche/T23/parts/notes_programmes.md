# T23, étape 2 : état du droit des lignes de programme et de panier

Agent « programmes », 20/10/2026. Gel vérifié : `application_lignes.csv` (sha256 `07dc5bd7…`, 89 lignes) et `paniers.csv` (`60f922ad…`, 33 lignes), identiques à la consigne § 0. Le champ du § 1 est appliqué tel quel.

Fichiers :

- `lignes_programmes.csv` : 122 lignes, une par ligne de `application_lignes.csv` et de `paniers.csv`. Colonnes : `id, fichier, programme, ligne, montant, critere, critere_secondaire, reference, url, citation, page, confiance, recherches_faites, date_jugement, note, date_acces`.
- `sources_programmes.csv` : sources archivées dans `sources/T23/programmes/` (20 fichiers) et sources réutilisées de T17, T20 et T22, avec leur sha256.

## 1. Résultat

| Fichier | J1 | J2 seul | aucun |
|---|---|---|---|
| application_lignes.csv (89) | 6 (dont 1 aussi J2) | 0 | 83 |
| paniers.csv (33) | 1 | 0 | 32 |

Lignes dans le champ, avec leur montant et la confiance :

| id | Programme | Montant (Md€) | Critère | Confiance | Décision ou texte |
|---|---|---|---|---|---|
| rn24_preference_nationale | RN 2024 | +6,4 | J1 et J2 | high | 89-269 DC (1990), 2024-6 RIP (11/04/2024), CEDH Koua Poirrez (2003), CJUE C-449/16 (2017) ; programme : « (si nécessaire par référendum constitutionnel) » |
| rn24_asile | RN 2024 | +1,2 | J1 | medium | 93-325 DC (1993), droit d'asile |
| rn24_tva_carburants | RN 2024 | −7,53 | J1 | medium | CJUE C-479/13 (2015), taux réduit hors annexe III ; directive 2022/542 |
| nfp_blocage_prix | NFP 2024 | −9 | J1 | low | 2019-774 QPC (2019), liberté d'entreprendre ; CE ANODE (2017) pour l'énergie |
| nfp_taxe_kilometrique | NFP 2024 | +1 | J1 | medium | CJCE 2/69 et 3/69 (1969), taxe d'effet équivalent |
| nfp_ir | NFP 2024 | +4,7 | J1 (part CSG) | low | 2000-437 DC (2000), CSG modulée selon le revenu |
| l_gel (panier LFI) | LFI 2027 | −9 | J1 | low | comme nfp_blocage_prix |

Par programme, en sommant les montants des lignes dans le champ, sans en déduire de correction :

- RN 2024 : +6,4 et +1,2 (économies), −7,53 (baisse de recette). Les deux lignes les plus solides, préférence nationale et TVA carburants, ont des signes opposés.
- NFP 2024 : −9 (dépense), +1 et +4,7 (recettes). Deux des trois lignes ont la confiance `low`.
- Ensemble 2024 : aucune.
- Paniers : l_gel (−9, LFI) ; aucune ligne Ensemble.

La règle multiplie le montant quel que soit son signe (§ 7 de la consigne). Elle réduirait donc à la fois des économies du RN et une perte de recettes du RN, ainsi qu'une dépense et des recettes du NFP. Le sens net dépend du facteur.

## 2. Cas limites du § 2 B

- **rn24_preference_nationale.** Les deux critères sont remplis. J2 : le programme du 24/06/2024 (PDF p. 6) dit « Mettre en place la priorité nationale (si nécessaire par référendum constitutionnel) » et « Réserver les aides sociales aux Français et conditionner à 5 années de travail en France l'accès aux prestations sociales non-contributives comme le RSA (si nécessaire par référendum constitutionnel) ». J1 : condition de nationalité (89-269 DC, Koua Poirrez, Martinez Silva) et condition de durée (2024-6 RIP, rendue deux mois avant l'annonce). Il existe une décision antérieure en sens contraire, à mentionner : 2011-137 QPC a validé la condition de 5 ans de titre de séjour pour le RSA. Le volet RSA (2,6) est donc moins nettement dans le champ que le volet familial (3,8). Une décision postérieure (2026-901 DC, APL des étudiants étrangers, conforme avec réserve) est notée sans changer le critère.
- **rn24_asile (J1, medium).** Le programme place le dépôt des demandes dans les ambassades parmi les mesures prises « en attendant la réforme constitutionnelle » : il ne la fait pas dépendre de la révision, donc pas de J2. Pour J1, 93-325 DC protège le droit de demeurer sur le territoire le temps de l'examen. La révision de 1993 (art. 53-1) n'a levé l'obstacle que pour les accords européens. Le cas est discutable : à confirmer par l'agent à l'aveugle.
- **nfp_asile (aucun).** L'abrogation ne porte pas de risque de censure. Un point est signalé à l'intégrateur, hors règle : le coût de 1,3 est calculé sur l'art. 19 de la loi de 2024, déjà censuré le 25/01/2024 (2023-863 DC, procédure) et jugé contraire sur le fond le 11/04/2024 (2024-6 RIP). La mesure chiffrée n'était pas en vigueur en juin 2024 : c'est une question de référence (montant peut-être nul).
- **rn24_ame et e_ame (aucun).** 2010-622 DC valide des restrictions d'accès à l'AME. 2024-6 RIP ne statue pas sur l'article AME de la proposition LR. L'inconstitutionnalité d'une suppression pure n'est qu'un avis de Montaigne.
- **nfp_blocage_prix et l_gel (J1, low).** 2019-774 QPC censure un mécanisme de fixation des prix dans tout secteur, sans limite de durée, mais elle valide l'encadrement des marges limité aux produits de première nécessité. Le NFP vise la première nécessité, mais par un blocage et sans durée annoncée : il est entre les deux. L'intégrateur peut juger que le « même mécanisme » n'est pas atteint.
- **rn24_ue (aucun).** Le cas est hors champ par le § 1 : il dépend d'une négociation sans changement de traité.
- **Baisses de TVA.** Les carburants sont en J1, parce qu'aucun point de l'annexe III ne les couvre et que la CJUE a condamné la France pour un taux réduit hors annexe (C-479/13). L'électricité et le gaz (annexe III, point 22), les transports en commun (point 5) et le taux zéro sur les produits de première nécessité (art. 98 § 2, sept points) sont en « aucun » : la directive les autorise. La « révision de la directive » évoquée par Montaigne pour les carburants est du droit dérivé, pas un traité : ce n'est pas J2.
- **ens_retention (aucun).** La mesure de niveau européen repose sur le pacte asile et migration, sans changement de traité ni décision de même nature. Montaigne la chiffre comme rn24_asile, mais leur mécanisme juridique diffère. C'est l'asymétrie à regarder si l'agent à l'aveugle juge autrement.
- **l_zucman (aucun, medium).** Aucune décision n'a déclaré contraire un impôt sur la fortune de même mécanisme avant juin 2026. 2012-662 DC est une décision de conformité. Ses censures portent sur le calcul du plafonnement et sur les biens de société non disponibles. 2026-901 DC ne statue pas sur le fond de la taxe sur les holdings. La ligne garde sa règle « Nouvelle assiette » (avis, pas décision). Même lecture pour nfp_isf, l_isf et rn24_iff.
- **nfp_taxe_kilometrique (J1).** Elle est déjà en « Nouvelle assiette : risque juridique ». Une seule règle par ligne : c'est à l'intégrateur de décider (§ 5.5).

Autres cas limites relevés :

- **nfp_ir (J1, low).** Seule la part « CSG progressive » est visée (2000-437 DC). Le montant de 4,7 repose surtout sur l'IR à 14 tranches. Le panier l_ir (IR seul) est en « aucun ».
- **nfp_flat et l_pfu (aucun).** La part « exit tax » (≤ 0,067) relève de l'arrêt de Lasteyrie (2004), mais la version supposée (2011) a été conçue après cet arrêt.
- **rn24_ir_jeunes et rn24_medecins (aucun).** 2023-862 DC censure une exonération d'IR liée à l'employeur, ce qui n'est pas le même mécanisme.

## 3. Dates

- Programmes 2024 : jugés à juin 2024.
- Paniers : `date_jugement` reprend la source de `paniers.csv`, qui ne donne pas toujours de date précise (Acteurs publics, CAE note 69, iFRAP).
- Pour les lignes en « aucun », aucune décision de même nature n'a été trouvée jusqu'au 20/10/2026. La date exacte ne change donc pas le résultat.
- Pour l_gel, la source est Montaigne 2024, donc la date est juin 2024 (2019-774 QPC est antérieure).

## 4. Lacunes et réserves

- Pour la plupart des lignes « aucun » (dépenses budgétaires, cotisations, retraites, crédits), aucune recherche web propre n'a été faite. Le jugement repose sur la lecture du libellé, de la fiche du chiffreur quand elle est archivée, et des dispositifs des décisions sur les lois de finances 2013, 2024, 2025 et 2026. La colonne `recherches_faites` le dit.
- Décisions citées par une source secondaire mais non lues, et non utilisées pour le critère : CE n° 375887 (2015, RSA et CEDH) ; CJUE du 19/12/2024 sur les prestations familiales en France ; CC 2022-842 DC et 86-217 DC (audiovisuel) ; CE sur les blocages de prix de 2020.
- Sources indirectes :
  - Koua Poirrez : texte anglais de l'arrêt, copie de l'université de Galway (HUDOC non atteint).
  - Martinez Silva et C-479/13 : communiqués de presse de la CJUE (EUR-Lex refuse curl ; la copie Wayback de l'arrêt C-302/19 était vide).
  - Décisions récentes du Conseil constitutionnel : copies Wayback, le site refusant curl après quelques requêtes.
  - 2019-774 QPC : copie juridoc.gouv.nc.
- Le programme NFP n'a pas été relu dans son texte original : ses mesures sont citées d'après les fiches et micro-chiffrages Montaigne, qui le citent entre guillemets.
