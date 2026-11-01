# T29, LR : programme 2027 à partir du programme présidentiel 2022 (V. Pécresse)

Notes du 01/11/2026. Consigne : `recherche/T29/CONSIGNE.md`. Aucun fichier de `data/`, `scripts/` ni `web/` n'a été modifié. Les CSV sont produits par deux scripts de travail gardés dans le dossier temporaire de la session (`gen.py`, `gen2.py`).

## 1. Ce qui a été lu

- Consignes : `AGENTS.md`, `CONTRIBUTING.md`, `recherche/CONSIGNES.md`, `recherche/T1/convention_application_2024.md`, `recherche/T1/rapport.md`, gabarits de `modeles/`, `scripts/garde_fous.py`, `recherche/T29/RN/` (exemple intégré), `recherche/T22/rapport.md` § 1, `recherche/T17/rapport.md` § 8 (LR 2024).
- Lignes `rn27_*`, `nfp_*`, `ens_*` de `data/raw/application_lignes.csv` et leur registre 2027 (familles et statuts repris).
- Textes de la référence archivés par T1 (`sources/T1/` : LFI 2026, LFSS 2026, PLF et PLFSS 2027, évaluations préalables, avis HCFP 2026-5) et par T29 RN (Sénat n° 736 Justice, Légifiscal, LCP).
- Sources nouvelles : `sources.csv` (40 fichiers dans `sources/T29/LR/`, dont 21 fiches Montaigne).

## 2. Programme retenu et pourquoi

| Candidat | Chiffrage indépendant mesure par mesure | Décision |
|---|---|---|
| Législatives 2024 (LR, « pacte législatif » de L. Wauquiez) | Aucun. T17 § 8 : pas de programme officiel (LR « privé de leader »), Montaigne n'a chiffré que trois listes, l'iFRAP n'a pas de fiche « vrai coût », l'OFCE et Asterès rien ; le pacte législatif date de juillet 2024, après le scrutin, et n'est pas chiffré. | Écarté |
| Plan de B. Retailleau, candidat LR (12/10/2026) | Aucun. Public Sénat (12/10/2026) : « 197 milliards d’euros d’économies, dont 56 milliards redirigés » en baisses d'impôts, chiffrage du candidat. Le comparateur 2027 de l'iFRAP reprend les montants du candidat sans chiffrage propre ; Montaigne annonce le chiffrage des candidats « au premier trimestre 2027 » (communiqué du 06/10/2026). | Écarté (point d'attention : voir § 8) |
| Présidentielle 2022 (V. Pécresse, candidate LR) | Oui : Institut Montaigne (synthèse + 21 fiches lues) et Fondation iFRAP (tableau « mesures chiffrables »). | **Retenu** |

Le libellé suit la règle 2 : « LR 2027 (programme 2022) ». La consigne T29 part d'un constat (« aucun parti n'a encore publié de programme pour 2027 ») qui n'est plus tout à fait vrai pour LR : le plan de B. Retailleau existe, mais il n'a pas de chiffrage indépendant mesure par mesure. Sous la règle 1, toutes ses mesures iraient dans une ligne « non chiffrée » à 0. Le programme 2022 reste donc le dernier programme chiffrable au sens de la consigne.

**Synthèse Montaigne** : la page en ligne et l'archive du 15/08/2022 donnent le même texte. Totaux : dépenses 51,6, économies 16,5, solde −35,1 « par an ». Selon la candidate, le solde serait de +42. Totaux de l'iFRAP : +30,5 en 2027 (dépenses −30,3, recettes +0,2). Ces totaux sont dans `totaux.csv`, au format de `totaux_instituts.csv`.

**Horizon des montants** (colonne `horizon` de `chiffrages.csv` et fin de chaque justification). Montaigne chiffre « par an » sur le quinquennat 2022-2027, par rapport au droit de 2022. Selon les fiches, l'horizon diffère :

- « en année pleine » : cotisations, fonctionnaires (17,8 cumulés, soit 5,9 en année pleine) ;
- « à horizon 2027 » : retraites (4,6 ; 13,3 à partir de 2030), EPR, prisons (fonctionnement 2027), allocations familiales au premier enfant ;
- coût annuel dès 2023 : allocations familiales des 2e et 3e enfants, consultation ;
- moyenne d'un cumul sur le quinquennat : tribunaux (9,3), forces de l'ordre (5).

L'iFRAP chiffre un solde pour 2027, « dans le cas d'une application complète des mesures », par rapport à un solde tendanciel de −84,7 Md€.

## 3. Lignes (41) et méthode

- **Montaigne, chiffreur de départ** (25 lignes).
  - 19 mesures de dépenses ou de baisses d'impôts de 1 Md€ ou plus, et 4 mesures d'économies.
  - Deux restes au sens de T22 § 1 :
    - `lr27_autres_dep_reste` (−6,8) : les 17 postes sous 1 Md€, dont la somme est égale à 26,3 − 19,5 ;
    - `lr27_autres_eco_reste` (+0,7) : l'AME.
  - Contrôle : la somme des lignes Montaigne vaut −35,1, le solde de la synthèse.
- **iFRAP seul** (13 lignes), comme `rn27_fraude`, `rn27_ue`, `rn27_iff` : mesures que Montaigne ne chiffre pas ou exclut. Ce sont fraude 15, niches et prestations 5, aides aux entreprises 15, collectivités 3,5, organismes 1,5, dispositifs immobiliers 2,5, État actionnaire 3, défense −6, handicap −1,7, audiovisuel −2,5, CVAE −2,0, forfait social −2,0 et un reste de −0,2 (IFI).
  - Pour la CVAE et le forfait social : l'iFRAP compte à part un « retour d'IS » de +2 pour −10 de baisses d'impôts de production. La famille `impots_production` suppose un montant net, comme la C3S de Montaigne. Ces deux lignes retiennent donc −2,5 × 0,8 = −2,0 (calcul).
  - L'iFRAP ne détaille pas son écart de −0,9 dans le bloc des impôts de production. Il n'est pas repris.
- **Annulations** (2 lignes) et **charge d'intérêts** (1 ligne) : § 5 et § 6.
- **Autres estimations** : celles de l'iFRAP, quand elles correspondent à une ligne Montaigne, sont dans `autres_estimations`. `chiffrages.csv` contient 69 lignes au format de `chiffrages_instituts.csv` :
  - 28 de Montaigne ;
  - 34 de l'iFRAP (usages `ligne`, `composante`, `dans_residu`, ou `hors_lignes` pour ses agrégats « Éducation et santé », « Politique familiale », « Environnement ») ;
  - 7 de la candidate (`partisan`).
- **Colonnes** : celles de `data/raw/application_lignes.csv` (avec `facteur_reference_bas`, `_haut`, `_loi_votee`), pour pouvoir ajouter les lignes telles quelles.

### Familles nouvelles pour une mesure de même nature (règle 5)

Chaque famille est reprise d'une ligne d'un autre parti ; la ligne de référence est citée dans la justification. Cinq choix sont à relire :

- `lr27_emploi_domicile` et `lr27_audiovisuel` → `impot_revenu_large` : crédit d'impôt et taxe qui touchent une large part des foyers. Aucune famille propre à ce cas n'existe. La règle « Aucune » est la même que celle de `residu`.
- `lr27_af_premier` → `revalorisation_prestation` plutôt que `prestation_nouvelle` : c'est l'extension d'une prestation existante versée par les CAF. La règle « Taux de recours » ne s'applique pas.
- `lr27_collectivites` → `reforme_structurelle_etat` : il n'existe pas de famille propre aux collectivités.
- `lr27_immobilier` → `residu` : le poste de l'iFRAP n'est pas détaillé.
- `lr27_forfait_social` → `impots_production` : c'est le classement de l'iFRAP.

## 4. Statut par rapport à la référence 2027

| Ligne | Statut, facteur [bornes] ; loi votée | Raison (source) |
|---|---|---|
| `lr27_retraites` | partielle 0,41 [0 ; 0,83] ; 0,41 | La réforme 2023 est dans la référence (suspendue). Borne haute : (4,6 − 0,8) / 4,6, rendement 2027 de 0,8 selon le PLFSS 2027, annexe A. Borne basse : Montaigne compte 8,2 pour la réforme 2023 en 2027 (registre `rn24_retraites`), soit 7,2 après la suspension, plus que 4,6. Milieu. |
| `lr27_prisons` | partielle 0,76 [0,53 ; 1] ; 0,76 | Le reste du plan 15 000 (63 % non réalisé fin 2025, Sénat n° 736) représente ≈9 450 des 20 000 places. Même source que `rn27_prisons`. |
| `lr27_tribunaux` | partielle 0,5 [0 ; 1] | LOPJ 2023-2027 votée (Sénat n° 736) ; part des tribunaux non isolée |
| `lr27_forces_ordre` | partielle 0,5 [0 ; 1] | LOPMI 2023-2027 votée : +15 Md€ cumulés (Sénat n° 115) |
| `lr27_chomage` | partielle 0,5 [0 ; 1] ; 0,5 | Réformes réglementaires de l'assurance chômage dans la référence, montant non isolé (T1, `ens_chomage`) |
| `lr27_fraude` | partielle 0,933 ; 1 | Comme `rn27_fraude` : (15 − 1) / 15 |
| `lr27_aides_entreprises` | partielle 0,73 [0,46 ; 1] ; 0,98 | Baisses d'aides dans la référence : gel des allègements 2,9, assiette 3,7, apprentissage 0,46, France compétences 1,0 |
| `lr27_collectivites` | partielle 0,5 [0 ; 1] ; 1 | PLF 2027 : contribution des collectivités de 4,1 Md€ (HCFP § 90) |
| `lr27_organismes` | partielle 1 | Comme `rn27_agences` |
| `lr27_handicap` | partielle 0,59 | Déconjugalisation de l'AAH (0,7 selon l'iFRAP) en vigueur depuis le 1/10/2023 (Sénat, avis n° 131) |
| `lr27_cvae` | partielle 0,5 [0 ; 1] ; 0,5 | CVAE baissée depuis 2022, encore 4,11 Md€ en 2027 (PLF, état A) ; rendement 2022 non lu |
| `lr27_consultation` | votée 0 | G = 30 € depuis le 22/12/2024 (source secondaire : syndicat Les Médecins libres) |
| `lr27_defense` | votée 0 | LPM 2024-2030 : 51 → 63 Md€ de 2025 à 2027 (HCFP, tableau 10) |
| `lr27_audiovisuel` | votée 0 | Contribution supprimée, audiovisuel financé par une fraction de TVA (LFI 2026, PLF 2027) |
| `lr27_epr` | proposée 0 ; 0 | Six EPR2 dans la PPE3 (février 2026) et financés par le PLF 2027. Le montant de Montaigne est d'ailleurs un surcoût du mix, pas une dépense budgétaire. |
| autres lignes | absente 1 | Mêmes statuts que les lignes de même nature (`rn27_production`, `rn27_donations`, `ens_succession`, `rn27_tva_elec_gaz`, `rn27_preference_nationale`, `nfp_niches`…). Points de vigilance dans `note_reference`. |

`facteur_reference_loi_votee` est rempli pour chaque ligne partielle dont la source cite le PLF ou le PLFSS 2027 (garde-fou LOI VOTÉE), et pour les deux annulations (0). Plusieurs facteurs sont des milieux d'intervalle de confiance faible, selon la convention de T1 : ce ne sont pas des valeurs mesurées.

## 5. Annulations de la référence (règle 4)

| Ligne | Économie annulée | Montant | Engagement (groupe Droite républicaine) |
|---|---|---|---|
| `lr27_annul_pensions` | Sous-indexation des pensions (PLFSS 2027, art. 35) | −4,0 | Amendement n° **AS359**, « M. Wauquiez, Mme Gruet, M. Bazin… », commission des affaires sociales, 07/10/2026, « Adopté ». Exposé : « Cet amendement des députés Droite Républicaine vise à supprimer l’article 35, qui sous-indexe ou désindexe certaines pensions de retraite en 2027 ». LCP (16/10/2026) confirme l'adoption, avec des amendements de suppression de plusieurs groupes, dont la Droite républicaine. |
| `lr27_annul_abattement` | Plafond de l'abattement de 10 % des retraités abaissé à 3 000 € (PLF 2027, art. 3) | −1,4 | Amendement n° **I-1**, « M. Wauquiez, M. Ray… », séance, 02/10/2026, « Adopté ». Exposé : « Cet amendement du groupe Droite républicaine vise à faire obstacle à une hausse d’impôt sur les retraités ». C'est l'un des sept amendements identiques qui ont supprimé l'article en séance le 15/10/2026 (Légifiscal). |

Montants et traitement : ceux de `rn27_annul_*`. Dans la variante loi votée, ces lignes valent 0.

**Groupe ou ministres.** Seules des positions du groupe parlementaire ont servi : amendements de suppression contre le texte du Gouvernement Lecornu. Aucune déclaration ministérielle n'est utilisée. La composition du gouvernement au 01/11/2026 et la présence éventuelle de ministres LR n'ont pas été vérifiées.

Économies de la référence sans ligne :

- **Gels de prestations** (prime d'activité et APL, PLF art. 74 ; prestations familiales gelées en 2027, 0,5 Md€, PLFSS annexe A) et **point d'indice** : aucun amendement ni aucune déclaration de LR n'a été trouvé. L'exposé de l'amendement I-1 plaide plutôt pour des économies sur « les dérives de l’assistanat », et celui de l'AS359 pour 20 Md€ d'économies sur l'État, la fraude et l'immigration.
- **Jours fériés** : la mesure est absente de la référence (T1).
- En 2022, la candidate promettait déjà de réindexer les pensions sur l'inflation. Montaigne l'exclut de son chiffrage (« application de la loi en vigueur »). La ligne d'annulation repose sur l'amendement de 2026, pas sur cette promesse.

## 6. Charge d'intérêts et montée en charge

- **`lr27_taux` = −0,1.** Même règle que `rn27_taux`. On prend la somme des lignes multipliées par leur facteur de référence : −5,8 Md€/an. Cela donne +0,47 point de dette, puis +1,2 pb, et −0,96 × 5,8 / 49,8 = −0,11. Avec les montants bruts (−9,4), la charge serait de −0,18. Le calcul est symétrique : un solde excédentaire réduirait la charge.
- **`lr27_retraites`** : la famille `retraites_age` est profilée, donc un profil est obligatoire (garde-fou PROFIL).
  - Coefficient central : 4,6 en 2027, puis 13,3 à partir de 2030 (fiche Montaigne), 2028-2029 interpolés, soit 1,63, 2,26, puis 2,89. Les Md€ ne sont pas rapportés au PIB, car la base de prix de Montaigne n'est pas dite.
  - Coefficient bas : 1. La réforme 2023 reprend sa montée en charge en 2028 (PLFSS 2027 : 1,9 en 2028, 3,7 en 2030).
  - Le facteur de référence (0,41) reste le même toutes les années, ce qui surestime sans doute l'écart après 2028 : décision laissée à l'intégrateur (§ 8).
- Annulations : pas de profil, comme `rn27_annul_*`.

## 7. Vérification

Dans une copie du dépôt (`…/scratchpad/copie_lr/`), avec les lignes ajoutées à `data/raw/` (`application_lignes`, `statut_reference_2027`, `application_programmes`, `montee_en_charge`, `chiffrages_instituts`, `totaux_instituts`) :

- `build.py`, `calc.py`, `moteur.py`, `sensibilite.py`, `validation.py`, `projection.py`, `build_web.py` et `check_regression.py` passent ;
- `garde_fous.py` : **0 erreur, 0 alerte** ;
- `test_web.py` et `distributif.sh` n'ont pas été lancés.

Résultats :

- **Solde de départ** (somme des montants) : **−9,4 Md€/an**. Il se décompose ainsi : Montaigne −35,1 ; iFRAP seul +31,1 ; annulations −5,4 ; intérêts −0,1.
- **Solde corrigé par le moteur** : **−20,2** (P10 −28,5 ; P50 −18,1 ; P90 −7,0) ; variante loi votée −9,3. Dans la même sortie, RN 2027 : −59,8.
- Le solde corrigé est plus bas que le solde de départ parce que les économies de l'iFRAP sont décotées :
  - fraude : 15 → 4,1 (effet promis et recoupement) ;
  - aides aux entreprises : 15 → 11,0 ;
  - collectivités : 3,5 → 1,5 ;
  - fonctionnaires : 5,9 → 5,0 ;
  - retraites : 4,6 → 1,5.
- Projection 2027 : déficit 6,2 % du PIB, dette 122,9 % ; en 2032 : 5,9 % et 134,1 %.

## 8. Décisions laissées à l'intégrateur

1. **Programme retenu.** Faut-il prendre le programme 2022 alors qu'un plan LR pour 2027 existe (B. Retailleau, 12/10/2026), mais sans chiffrage indépendant ? Montaigne doit chiffrer les candidats au premier trimestre 2027 : il faudra alors remplacer ces lignes. `position_parti` le dit.
2. **Lignes « iFRAP seul » (+31,1 au départ).** Montaigne écarte explicitement fraude, niches, fonctionnement et privatisations, qu'il juge « insuffisamment détaillées ou dont la matérialisation est trop incertaine ». Elles sont gardées par symétrie avec le RN (`rn27_fraude`, `rn27_ue`…), avec leurs règles (effet promis, réforme structurelle). Leur poids est bien plus grand ici que pour le RN.
3. **Facteurs de confiance faible** (milieux d'intervalle) : `lr27_retraites`, `lr27_tribunaux`, `lr27_forces_ordre`, `lr27_chomage`, `lr27_aides_entreprises`, `lr27_collectivites`, `lr27_cvae`. `lr27_prisons` suit `rn27_prisons`.
4. **`lr27_retraites` au-delà de 2027** : faut-il un `facteur_reference_2028` qui tienne compte de la reprise de la réforme 2023 en 2028 ?
5. **Familles des 5 lignes** listées au § 3 (choix à relire).
6. **`lr27_epr`** : le montant de Montaigne n'est pas une dépense publique. Il est compté 0 par le statut « proposée », mais il reste dans le solde de départ (−1,2).
7. `solde_annonce` et `solde_montaigne` sont vides dans `entete.csv`, comme pour le RN : +42 (candidate) et −35,1 (Montaigne) se mesurent par rapport au droit de 2022.

## 9. Lacunes

- Plan Retailleau 2027 : programme détaillé non lu ; seule la presse (Public Sénat) et le comparateur de l'iFRAP l'ont été.
- Fiches Montaigne absentes de l'index du candidat : prévention (3,7), emploi à domicile, forces de l'ordre, recherche. Pour ces mesures, seule la synthèse a été lue.
- Le tableau de l'iFRAP est une image sans date ; le poste « dispositifs immobiliers » (2,5) n'est pas identifié.
- Statut 2027 non vérifié en détail :
  - exécution de la LOPMI et de la LOPJ ;
  - rendement 2022 de la CVAE ;
  - texte de la convention médicale (source secondaire) ;
  - loi de suppression de la contribution à l'audiovisuel public (déduite du financement par la TVA) ;
  - montant 2027 des réformes de l'assurance chômage.
- Aucun amendement Droite républicaine en séance sur l'art. 35 du PLFSS : la partie dépenses n'a pas été examinée avant le rejet du 23/10/2026.
- Positions de LR sur les gels de prestations et le point d'indice : rien trouvé.
