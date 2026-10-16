# T19, phase 1 : relevé des mesures chiffrées (PLF 2027, PLFSS 2027, loi 2026-534)

Date d'accès : 2026-10-16. Fichiers produits :

- `mesures.csv` : 143 lignes, dont 92 pour 2027 et 51 pour 2028 (id suffixé `_2028`). Six lignes 2028 n'ont pas de jumelle 2027, parce que la source chiffre l'effet 2027 à zéro ou ne le détermine pas.
- `sources.csv` : 3 documents téléchargés dans `sources/T19/`, plus 5 documents de `sources/T1/` relus (chemins `../T1/`).

## 1. Sources et méthode

| Texte | Source des chiffrages | Remarque |
|---|---|---|
| PLF 2027 (AN n° 3210) | Évaluations préalables des articles (`sources/T1/PLF2027_evaluations_prealables.pdf`, 743 p.), section 4.2 de chaque article | 74 articles évalués, tous lus. Page = page du PDF (identique à la pagination imprimée). |
| PLFSS 2027 (AN n° 3211) | Annexe 9, « Fiches d'évaluation préalable des articles » (`sources/T19/PLFSS2027_annexe9_evaluations_prealables.pdf`, 324 p., securite-sociale.fr) | Ni le dossier AN ni le texte n° 3211 ne la contiennent ; l'URL a été trouvée par WebSearch. 32 fiches (articles 4 à 14, 18, 20 à 39), toutes lues (rubrique « 1. Impact financier global » et tableau en droits constatés). |
| Loi n° 2026-534 | Étude d'impact du projet de loi (Sénat n° 24, 13/10/2025, `sources/T19/PJL_fraudes_etude_impact_senat_pjl25-024.pdf`) et copie du JO du 26/06/2026 (`sources/T19/Loi_2026-534_JO_copie_afg.pdf`) | La loi promulguée compte 115 articles, le projet 27. Les chiffrages sont ceux du projet de loi. Le numéro d'article du CSV est celui de la loi : il a été retrouvé en cherchant le dispositif dans le texte du JO. |

Règles appliquées :
- Les montants exprimés en M€ sont convertis en Md€ (division par 1 000, simple changement d'unité). Aucun autre calcul, sauf trois cas signalés dans `note` : les sommes que la source écrit elle-même, et la ligne 2028 de l'art. 39 du PLFSS.
- Dans les tableaux de l'annexe 9, l'en-tête annonce souvent une colonne « 2026 (rectificatif) » qui reste vide, ou des années décalées (2025-2029). J'ai attribué chaque valeur à une année d'après sa position dans la mise en page (`pdftotext -layout`) et d'après le texte. Les cas ambigus sont signalés dans `note` (PLFSS art. 4, 21, 22, 26, 28).
- Le PLFSS chiffre en droits constatés et l'évaluation préalable du PLF en recettes ou dépenses budgétaires. La comptabilité nationale n'est retenue que lorsque la source la donne (CICE Mayotte, art. 11 du PLF).

## 2. Résultats

Effectifs et totaux 2027 : sommes brutes de la colonne `chiffrage_md`, à ne pas utiliser telles quelles (voir § 4).

| Texte | Lignes 2027 | Économies 2027 (Md€) | Coûts 2027 (Md€) | Lignes 2028 |
|---|---|---|---|---|
| PLF 2027 | 55 | 19,83 | 4,80 (dont 4,2 d'indexation du barème de l'IR) | 29 |
| PLFSS 2027 | 26 | 10,19 | 0,10 | 22 |
| Loi 2026-534 | 11 | 0,14 (montants annuels, année non précisée) | 0 | 0 |

Principales mesures (2027) :
- **PLF 2027**
  - Contribution exceptionnelle des grandes entreprises : 5,0 Md€.
  - CPEB (contribution des collectivités) : 2,5 Md€.
  - FCTVA : 2,092 Md€.
  - Abattement des retraités : 1,4 Md€.
  - Avoirs en déshérence de la CDC : 1,4 Md€.
  - Fiscalisation des IJ : 0,965 Md€.
  - Indemnités de rupture : 0,82 Md€.
  - TEITLD : 0,8 Md€.
  - TVA sur les collectivités : 0,6 Md€.
  - CSG sur les IJ : 0,54 Md€.
  - Apport-cession : 0,5 Md€.
  - CPF : 0,35 Md€.
  - Prime d'activité : 0,332 Md€.
  - France compétences : 0,317 Md€.
  - TVA sur la télévision : 0,304 Md€.
  - Côté coûts : indexation du barème de l'IR, 4,2 Md€ (par rapport à un gel).
- **PLFSS 2027**
  - Assiette des allègements généraux : 3,7 Md€.
  - Pensions (art. 35) : 3,0 Md€ pour les ROBSS et 1,1 Md€ pour l'État. La source donne aussi un total de 4,0 Md€ pour l'ensemble des régimes de base.
  - Contribution des organismes complémentaires : 1,117 Md€.
  - Indemnités de rupture : 0,44 Md€, doublon partiel avec le PLF (voir § 4).
  - Taxe soda étendue : 0,303 Md€.
  - Dispositifs médicaux : 0,15 Md€.
  - Distribution du médicament : 0,12 Md€.
- **Loi 2026-534**
  - Solidarité du maître d'ouvrage : 47 M€.
  - Géolocalisation des transports sanitaires : 32 M€.
  - Flagrance sociale : 17 M€.
  - Mise sous objectifs (MSO) : deux fois 10 M€.
  - Opposition à contrainte : 8 M€.
  - Les autres mesures pèsent moins de 5 M€ chacune.

Comportements : la source indique le plus souvent un chiffrage statique (« à comportements constants / inchangés ») ou n'en dit rien (`inconnu`). Elle intègre explicitement des comportements pour l'APL étudiante (art. 78 du PLF), le CPF (art. 89 du PLF, renoncement de 23 à 30 %) et la distribution du médicament (art. 10 du PLFSS). Elle les intègre aussi pour plusieurs mesures de santé dont le coût dépend du recours (vaccination, dépistage, intéressement des EHPAD).

## 3. Mesures sans chiffrage 2027 exploitable (hors CSV)

**PLF 2027 (évaluations préalables)**
- **Chiffrage absent ou « non chiffrable »** :
  - art. 4, allègement des donations (« coût non chiffrable en 2027 ») ;
  - art. 8, volet Pilier 2 HLM ;
  - art. 14, taxe foncière des sinistrés ;
  - art. 17, réductions de capital ;
  - art. 18, provisions assurantielles ;
  - art. 24, taxe incitative EnR (« non chiffrable compte tenu de l'effet comportemental ») ;
  - art. 25, déduction poids lourds (« gain non chiffrable ») et TVA ;
  - art. 28, SIEG (« coût non chiffrable ») ;
  - **art. 30, lutte contre la fraude fiscale et anti-contournement (« incidence non chiffrable », p. 351)** ;
  - art. 44, TAC (« sans incidence APU ») ;
  - art. 69, garantie du nouveau nucléaire (« incertaines ») ;
  - art. 29, 32, 33, 40, 46 à 48, 52, 75 et 83 (sans objet ou sans incidence).
- **Chiffrés, mais pas pour 2027, ou par une fourchette ou un plafond** :
  - art. 8, TFPB des logements sociaux : effet à partir de 2043 ;
  - art. 14, CFE des sinistrés : 21 M€, placé dans la colonne « 2025 » d'un tableau à l'en-tête douteux, donc écarté ;
  - art. 24, carburants de synthèse : environ 650 M€ sur 10 ans, à partir de 2030 ;
  - art. 26, zones BUD et ZDP : moins de 0,5 M€ à partir de 2028 ;
  - art. 28, NZIA : « gain non chiffrable (majorant 32 M€) » ;
  - art. 31 : quelques M€, non datés ;
  - art. 71 : 20 à 30 M€ de subventionnement, inchangé ;
  - art. 73 : 0,2 à 0,3 M€ ;
  - art. 80, harkis (CNIH) : économie de 1,9 à 2,9 M€ en 2027, fourchette sans valeur centrale.
- **Transferts sans effet sur le solde APU selon la source** :
  - art. 38, compensations aux régions : −173,8 M€ pour l'État, +173,8 M€ pour les collectivités, total APU 0 ;
  - art. 45 : versement du CAS au budget général, interne à l'État ;
  - art. 49 : TVA affectée à la sécurité sociale, −1,7 Md€ net au profit de l'État ;
  - art. 51 : transfert entre ODAC ;
  - art. 53 : +2,6 / −2,6 M€ entre l'État et les collectivités.
- **Articles sans évaluation préalable** : art. 1, 41, 43, 55 et 57 à 67 (articles d'équilibre, de crédits ou sans évaluation dans l'annexe).

**PLFSS 2027 (annexe 9)**
- **Transferts internes sans effet sur le solde APU** :
  - art. 13, financement APA/PCH : neutre ;
  - art. 14, transferts entre branches ;
  - art. 34, majoration de pension pour enfants : −1,4 M€ pour la vieillesse, +1,4 M€ pour l'État en 2027.
- **Chiffrage conditionnel, en fourchette, ou incohérent** :
  - art. 18 : environ 15 M€ pour 10 Md€ d'émissions de moyen terme, conditionnel ;
  - art. 20 : le tableau (+0,18 M€ en 2027) contredit le texte (0,45 M€ d'économies, 0,02 M€ de coût), écarté ;
  - art. 23 : fourchette de −0,6 à −1,3 M€ ;
  - art. 33, suppression de l'ANDPC : 1,5 à 3 M€ à partir de 2028.
- **Coût 2027 non déterminé** : art. 26, complémentaire FPH (2027 « À déterminer », seule la ligne 2028 a été relevée).
- **Articles sans fiche** : art. 1 à 3, 15 à 17, 19, 40 à 48 (rectifications, tableaux, objectifs de dépenses).
- **Mesures réglementaires hors articles** (franchises, transports en ALD, prescription des arrêts de travail, plafond des IJ AT-MP, etc.) : citées dans l'annexe A et l'exposé, avec par exemple 0,1 Md€ chacune pour deux mesures sur les arrêts de travail et transports. Non relevées, car la consigne porte sur les articles.

**Loi 2026-534 (étude d'impact du projet)**
- **Aucun chiffrage** : articles 1, 2, 3, 4, 8, 9, 11, 13, 14 (IV), 15, 16, 18 à 20 et 23 à 26 du projet (impact « positif » mais non quantifié, ou sans objet).
- **Art. 6 du projet (MDPH)** : environ 20 M€ « potentiellement recouvrable annuellement » pour les départements. Chiffré au § 4.3 (collectivités), « avec beaucoup de précaution » ; écarté.
- **Art. 10 du projet** : droit de communication des agents des CPAM, +5 M€. **Écarté**, faute d'avoir retrouvé avec certitude l'article correspondant de la loi.
- **Art. 14 (I-III) du projet** : CSG majorée sur les revenus illicites, +13,7 M€ en 2026, +14,2 M€ en 2027, +14,7 M€ en 2028. **Écarté** : le dispositif est absent du texte promulgué (aucune occurrence de « contribution sociale généralisée » ; la seule mention des revenus illicites porte sur les allocations chômage). Il a sans doute été retiré ou censuré, mais la décision 2026-904 DC n'a pas été lue.
- **Rendement global** : il n'est donné ni par la loi ni par son étude d'impact. Le HCFP (avis 2026-5, tableau 7, p. 23) compte **1,0 Md€** de « Lutte contre la fraude (y c. facturation électronique) » parmi les mesures nouvelles 2027 et note (§ 78) que ces mesures « n'ont, semble-t-il, pas porté leurs fruits en 2026 ». Ce montant agrège plusieurs leviers et n'est pas attribuable à la loi 2026-534. Il n'est pas dans le CSV.

## 4. Points de vigilance pour l'intégrateur

1. **Doublons** :
   - `plfss27_art6_indemnites_rupture` (0,44) est la part sociale déjà comprise dans `plf27_art2_ruptures` (0,82) ;
   - `plfss27_art35_*` : 3,0 (ROBSS) et 1,1 (État) sont deux lignes séparées ; la source donne 4,0 tous régimes de base, sans écrire la somme 4,1 ;
   - la CSG sur les IJ (`plf27_art2_csg_ij`, 0,54 en droits constatés) figure dans le PLF ; l'exposé du PLFSS (art. 16) l'évalue à « + 0,4 milliard d'euros ».
2. **Transferts entre administrations** : FCTVA (art. 35), TVA des collectivités (art. 36), accises régionales (art. 39), DGF et dotations (art. 34, 77, 85 à 87), DILICO (art. 84) et ONF (art. 13). Ce sont des gains ou des coûts pour l'État dont l'effet sur le solde APU dépend de la réaction des collectivités. Seule la CPEB (art. 37) est explicitement chiffrée sur le solde APU par la source. Le DILICO améliore le solde APUL selon la source, sans montant écrit.
3. **Mesures dont la référence n'est pas une politique inchangée** :
   - indexation du barème de l'IR (coût par rapport à un gel) ;
   - prorogations (CICE Mayotte, dépenses fiscales culturelles et carburants aéronautiques, contribution des complémentaires à 2,05 %) ;
   - audiovisuel public (amélioration « par rapport à 2026 ») ;
   - malus masse (par rapport à un droit en vigueur « inopérant »).
4. **Recettes ponctuelles** : déshérence CDC (1,4 Md€), prélèvement ANCV (0,12), FCAC (0,003) et contribution exceptionnelle des grandes entreprises (« au titre des acomptes »).
5. **Plafonds, planchers, objectifs** :
   - valeurs maximales : INB, TTAP sûreté, recharge des poids lourds, MSO (« jusqu'à ») ;
   - valeurs plancher (« plus de », « au moins ») : pénalités, AT-MP ;
   - objectifs plutôt qu'estimations : dispositifs médicaux (taux calibré), fraude à la facturation (art. 32 du PLFSS).
6. **Incohérences internes à la source** :
   - PLFSS art. 24 : le texte dit 19 M€ en 2027 « puis 2028 », le tableau donne 38 M€ en 2028 ;
   - PLFSS art. 39 : 59 + 160 ≠ 154,8 M€ ;
   - PLF art. 74, prime d'activité : 995 M€ en 2028 contre 332 M€ en 2027, un rapport supérieur à 3 que le texte n'explique pas ;
   - PLF art. 88 : 317 M€ en 2027 et en 2028 malgré une clé de décaissement de 40 %.
7. **Périmètre APU incertain** :
   - taxe de sûreté des aérodromes (affectée aux exploitants, effet sur le solde public douteux) ;
   - ANCV et audiovisuel public (classement en APU non vérifié) ;
   - ACI publics (employeurs publics).
8. **Loi 2026-534** :
   - les chiffrages portent sur le projet de loi d'octobre 2025, et plusieurs dispositifs ont été modifiés (exemple : l'opposition à contrainte, art. 93 de la loi, garde une demande d'arrêt de l'exécution provisoire) ;
   - les montants sont annuels sans année ; ils sont rattachés à 2027 par convention (voir `note`) ;
   - la correspondance entre articles du projet et articles de la loi a été établie par recherche de mots-clés dans la copie du JO hébergée par l'AFG, non par Legifrance.
9. **Contrôle croisé** : le tableau 7 du HCFP (p. 23) recoupe les montants pour les allègements (3,7), l'abattement (1,4), la déshérence (1,4), la TEITLD (0,8) et les ruptures (0,8). Il donne 1,4 pour les IJ (IR + CSG ; le relevé a 0,965 + 0,54). Pour la TVA sur la télévision, il donne 0,4 contre 0,304 Md€ dans l'évaluation préalable.

## 5. Tentatives et lacunes

- **Annexe 9 du PLFSS** : absente du dossier AN (pages `dyn/17/dossiers/PLFSS_2027` et `l17b3211_projet-loi`) et de `l17b3211_etude-impact.pdf` (404). Trouvée sur securite-sociale.fr par WebSearch.
- **Évaluations préalables de la loi fraude** : celles du texte final ou des amendements gouvernementaux n'ont pas été cherchées. Seule l'étude d'impact initiale a été lue.
- **Décision CC 2026-904 DC** : non lue. L'absence de la CSG majorée n'est donc pas expliquée.
- **Mesures du PLFSS hors articles** : non relevées (consigne).
