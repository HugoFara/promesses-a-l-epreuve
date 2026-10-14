# T1 : référence 2027 (loi en vigueur + budget 2027 proposé)

Date d'accès de toutes les sources : 2026-10-14. Fichiers produits :

- `statut_reference.csv` : 68 lignes (23 `application_lignes` + 45 `paniers`), une par `id`. On y trouve 39 lignes absentes, 24 partielles, 4 proposées et 1 votée. Aucune ligne n'a de statut inconnu. J'ai ajouté une colonne `ligne` (libellé) pour la lisibilité.
- `parametres_plf2027.csv` : 82 paramètres, avec une colonne `note` ajoutée.
- `sources.csv` : 14 fichiers archivés dans `sources/T1/`, avec leur sha256.

## 1. Textes lus

| Texte | Source lue | Remarque |
|---|---|---|
| LFI 2026 (loi n° 2026-103 du 19/02/2026) | Texte définitif AN, TA n° 227 (PDF, 448 p.) | Legifrance refuse `curl` (403). La numérotation des articles 7, 8 et 12 a été vérifiée sur Legifrance via WebFetch : elle est identique au TA. Le texte promulgué peut différer du TA par les censures du Conseil constitutionnel (quelques cavaliers selon la presse, aucun sur les articles utilisés ici, selon Legifrance). |
| LFSS 2026 (loi n° 2025-1403 du 30/12/2025) | JORF du 31/12/2025 (copie PDF hébergée par l'AFPA) | Décision CC 2025-899 DC. Articles censurés : 51, 57, 60, 69, 72, 83, 85, 91 et 92, dont aucun n'est utilisé ici. |
| PLF 2027 (AN n° 3210, déposé le 1/10/2026) | Texte complet AN (exposé général, articles, états A et B), évaluations préalables (743 p.), PAP Travail et Santé, rapport général AN tome I | Le dossier de presse et le RESF de budget.gouv.fr sont **inaccessibles** (Incapsula bloque `curl` et WebFetch) ; economie.gouv.fr renvoie une 403. |
| PLFSS 2027 (AN n° 3211) | Texte complet AN (articles, exposés, annexe A pluriannuelle) | L'étude d'impact du PLFSS n'a pas été trouvée sur le dossier AN. |
| Avis HCFP 2026-5 (25/09/2026) et 2026-3 (RAA) | hcfp.fr | |
| Insee IP 2105 et 2106 | insee.fr | |

## 2. Résultats principaux (mesures)

**Votées (loi en vigueur)**
- **Surtaxe d'IS** : la LFI 2026 (art. 12) la proroge pour un seul exercice (exercice 2026), avec un seuil de 1,5 Md€ de chiffre d'affaires. Rendement 2026 : 7,3 Md€ en LFI, révisé à environ 7,0.
- **Taxe sur les holdings patrimoniales** : LFI 2026, art. 7 (art. 235 ter C du CGI). Taux de 20 % sur les actifs non professionnels, pour les exercices clos à compter du 31/12/2026. Rendement 2027 de 0,1 Md€, à condition que la ligne 1439 de l'état A, « Taxe sur le patrimoine financier », soit bien cette taxe.
- **Dutreil** : restreint par la LFI 2026 (art. 8) : actifs non professionnels exclus, engagements de conservation portés de 4 à 6 ans. Rendement non trouvé.
- **Taxe sur les rachats d'actions** : **inchangée**, 0,2 Md€ en 2026 comme en 2027. L'amendement du PLF 2026 qui sert de base aux 8,4 Md€ n'a pas été retenu.
- **CSG sur le capital** : LFSS 2026, art. 12. Le taux passe de 9,2 % à 10,6 % sur les revenus du patrimoine et la plupart des produits de placement, ce qui porte le PFU à 31,4 % de fait. Rendement 2026 : +1,2 Md€ selon le HCFP. Le PFU lui-même est maintenu.
- **Suspension de la réforme des retraites** : LFSS 2026, art. 105, pour les pensions prenant effet à compter du 1/9/2026 et jusqu'au 1/1/2028. Le PLFSS 2027 (annexe A) en chiffre le coût : la suspension réduit de **1,0 Md€** le rendement attendu de la réforme 2023 en 2027, qui était de 1,8 Md€ (champ des régimes de base). Les paniers utilisent 1,4 (lettre rectificative citée par la presse, non lue).
- **Gel des allègements généraux** : décret n° 2026-509 du 12/06/2026 (SMIC de référence figé à sa valeur du 1/1/2026). Rendement : +2,8 Md€ en 2026 et +2,9 Md€ supplémentaires en 2027 selon le HCFP. Le PLF art. 49 transfère à l'État 5,6 Md€ en 2027.
- **Loi contre les fraudes** : loi n° 2026-534 du 25/06/2026 (source secondaire). La référence 2027 compte 1,0 Md€ de recettes « lutte contre la fraude » (HCFP, tableau 7).
- **Aides à l'apprentissage** : réduites par les décrets 2025-174 et 2026-168. Le PLF 2027 reconduit l'aide exceptionnelle, avec 2,00 Md€ de CP contre 2,46 en LFI 2026.
- **AME** : les décrets 2026-66 et 2026-67 renforcent les contrôles, sans chiffrage. Aucun recentrage du panier de soins n'a été voté.
- **Assurance chômage** : réformes réglementaires dont la montée en charge est comptée dans le solde 2027. Le montant n'est pas isolé.

**Proposées (PLF/PLFSS 2027)**
- **Surtaxe d'IS, 3e exercice** à taux réduits (15,7 % / 31,4 %) : **5,0 Md€** en 2027 (PLF art. 15, évaluation préalable). Elle n'est pas pérennisée.
- **Abattement de 10 % des retraités** plafonné à 3 000 € : **1,4 Md€** en 2027, 1,8 en 2028, 1,1 ensuite (PLF art. 3).
- **Sous-indexation des pensions** au-dessus de 1 281 € : **4,0 Md€** si les pensions concernées sont gelées, dont 3,0 pour la branche vieillesse (PLFSS art. 35).
- **Assiette des allègements** élargie à l'intéressement, à la participation et à la PPV : **3,7 Md€** (PLFSS art. 7). Le même article pérennise le régime social de la PPV.
- **Indemnités journalières** : 1 Md€ d'économies inscrites dans l'ONDAM, sans instrument précisé. Les jours de carence ne sont pas mentionnés.
- **Gels de prestations** : prime d'activité −0,33 Md€ et APL −0,10 Md€ en 2027 (PLF art. 74).
- **Donations** : allègement temporaire jusqu'au 30/06/2027 (PLF art. 4), coût jugé « non chiffrable ».
- **Pacte « Papin »** (reprises par les salariés). Le gouvernement s'engage à préserver le Dutreil.
- Point d'indice gelé ; opérateurs à −2 209 ETP ; France compétences −1 Md€.

**Absentes** : jours fériés (abandonnés en septembre 2025), 7 jours de carence, ISF, taxe Zucman (seule existe la taxe sur les holdings), barème IR à 14 tranches, suppression du PFU, frais de notaire pour les primo-accédants, accise réduite sur l'électricité (le taux normal est rétabli), niches brunes, versement automatique des prestations (seul le préremplissage existe), non-remplacement d'un fonctionnaire sur deux (l'État crée des postes nets).

## 3. Facteurs suggérés : convention et points clés

`facteur_suggere` mesure **uniquement le recoupement avec la référence**. Il s'applique en plus du facteur comportemental existant (colonne `facteur` des CSV de `data/`). Convention retenue : la référence = loi votée + PLF/PLFSS 2027 tels que déposés, comme le demande la consigne. Si l'intégrateur préfère une référence « loi votée seulement », les lignes `proposée` repassent au facteur 1.

| Ligne | Facteur | Calcul |
|---|---|---|
| l_surtaxe_* | 0,17 | (6 − 5,0) / 6 ; vaut 1 si le PLF 2027 n'est pas adopté |
| e_pens_e, e_abat_e | 0 | mesures proposées quasi identiques (4,0 contre 4,1 ; 1,4 contre 1,4) |
| ens_fraude | 0,67 | (3 − 1,0) / 3, avant la règle ÷3 |
| nfp_retraites, l_ret60_i | 0,98 | (58 − 1,0) / 58 |
| l_bandeaux_* | 0,5 | milieu de [0,09 ; 0,87], confiance faible (voir la note de la ligne) |
| e_carence_e | 0,5 | milieu entre un recoupement total et nul avec l'enveloppe IJ de 1 Md€ |
| l_succ, nfp_succession, l_ir, nfp_ir | 0,91 à 0,94 | milieu d'intervalles bornés par la composante qui recoupe la référence (Dutreil ; CDHR 0,6) |
| isf, zucman, multinationales | 0,94 à 0,98 | taxe holdings 0,1 ; Pilier 2 0,5 |
| e_appr_e | 0,5 (maintenu) | borne haute calculée à 0,84 ; économies 2025-2026 non chiffrées |
| ens_chomage | 0 | votée (maintenu) |

Plusieurs facteurs sont des **milieux d'intervalles** : le calcul est donné dans `note` et la confiance est marquée `low`. Ce ne sont pas des valeurs mesurées.

## 4. Mesures dont le statut a changé récemment ou reste instable

1. **PLF 2027 en commission** (source secondaire, Légifiscal ; le rapport AN n° 3291 lu ne relate pas les votes). Le 9/10/2026, la partie recettes a été **rejetée** par 31 voix contre 3. Parmi plus de 200 amendements adoptés :
   - suppression de l'**art. 3** (abattement des retraités) ;
   - suppression de la fiscalisation des IJ ;
   - taxe de 2 % sur les titres de placement des holdings ;
   - taxe sur les services numériques portée à 15 % ;
   - relèvement de la CEHR et de la CDHR ;
   - suppression de la cible de 5 % ;
   - perte nette d'environ 9,6 Md€.

   La séance (depuis le 13/10) repart du texte du Gouvernement, avec un vote sur la première partie prévu le 20/10.
2. **Abattement des retraités et IJ des ALD** : déjà abandonnés lors du PLF 2026 (le Sénat avait voté l'abattement, la mesure a été retirée ensuite), reproposés en 2027, puis supprimés de nouveau en commission.
3. **Gel des allègements** : pris par décret en cours d'année (juin 2026). Il ne figure ni dans la LFI ni dans la LFSS 2026. Sa prolongation en 2027 dépend du PLFSS.
4. **Surtaxe d'IS** : le « temporaire » devient une troisième année, à taux réduits. Le rendement 2026 a été révisé à la baisse de 0,3 Md€.
5. **Fraude** : la loi a été promulguée le 25/06/2026 après la décision CC 2026-904 DC. Le HCFP note que le rendement de 1,5 Md€ prévu en 2026 « a disparu ».
6. **Retraites** : la suspension a été réintroduite par l'Assemblée en nouvelle lecture. Elle n'a pas été censurée (art. 105 promulgué).
7. **LFI 2026** : adoptée tardivement (loi spéciale le 27/12/2025, 49.3, promulgation le 19/02/2026).

## 5. Paramètres macro et finances publiques (résumé)

| | 2025 | 2026 | 2027 |
|---|---|---|---|
| Solde public (% PIB) | −5,1 (Insee) | −5,4 (LFI : −5,0) | −5,0 |
| Dette (% PIB) | 115,7 (Insee) | 119,3 | 121,7 |
| PIB en valeur (Md€) | 2 991,1 (Insee) | ≈3 051 (calcul) | ≈3 134 (calcul) |
| Croissance en volume | 0,8 (Insee, brut) | 0,5 | 1,0 |
| Déflateur du PIB / IPC | | 1,5 / 2,1 | 1,7 / 1,8 |
| Charge d'intérêts APU (Md€) | 66 | 79,2 | 91 (2,9 % du PIB) |
| Programme 117, charge de la dette de l'État (Md€) | | 58,6 (LFI) ; ≈62,7 révisé | 72,4 |
| OAT 10 ans | | 3,9 en moyenne ; 4,2 en fin d'année | 4,3 en moyenne |
| Solde structurel (% PIB potentiel) | −5,2 | −5,1 | −4,6 |

Trajectoire au-delà de 2027 :
- Déficit de 3,9 % en 2028 et 2,8 % en 2029. Cette trajectoire a été **communiquée au HCFP, mais pas publiée** : « Le Gouvernement n'a pas fourni de scénario pluriannuel de finances publiques ».
- Croissance de 1,1 % en 2028 et 2029, puis 1,2 % en 2030 ; croissance potentielle de 1,2 % jusqu'en 2028, puis 1,0 %.
- **Dette 2028-2030 et solde structurel 2028-2029 : non trouvés.**

Avis du HCFP :
- croissance 2027 « optimiste » ;
- solde 2026 « plausible » ;
- effort structurel de 0,9 point (≈28 Md€, dont 17 en recettes) ;
- 43 Md€ de mesures par rapport à la politique inchangée ;
- dépenses nettes à +0,7 % pour un plafond de 1,2 % ;
- retour sous 3 % en 2029 « très peu vraisemblable ».

**Critère d'acceptation de T5** : le déficit 2027 de 5,0 % et la dette de 121,7 % sont confirmés dans le texte primaire (article liminaire).

## 6. Ce qui n'a pas été trouvé

- Le dossier de presse PLF 2027, le RESF et le PSMT/RAA sur budget.gouv.fr (bloqués par Incapsula). Les paramètres ont été repris de l'article liminaire, de l'exposé général et de l'avis du HCFP. Le PIB 2026-2027 en valeur est donc calculé.
- Le rendement de l'art. 8 de la LFI 2026 (Dutreil) et celui de la taxe holdings hors état A.
- La lettre rectificative du PLFSS 2026 et son évaluation : le chiffre de 1,4 Md€ en 2027 n'est pas lu.
- Le montant 2027 des réformes de l'assurance chômage.
- Les économies votées sur les aides à l'apprentissage en 2025-2026.
- Le chiffrage de l'effet de la RGDU 2026 sur les salaires au-dessus de 1,6 SMIC.
- Les textes primaires sur la trajectoire GNR du BTP et la hausse de la TSBA (niches brunes).
- L'étude d'impact de la loi fraude.

## 7. Décisions laissées à l'intégrateur

1. Choisir la référence : loi votée seule, ou loi votée + PLF/PLFSS 2027. Ce choix change 5 lignes (surtaxe, pensions, abattement et, en partie, fraude et bandeaux). Vu le rejet en commission, une variante « loi votée seule » paraît utile.
2. l_ret62_a : statique de −6,9 (suspension à 1,4, presse) ou de −7,3 (suspension à 1,0, PLFSS 2027, champ des régimes de base).
3. l_smic : le gel du SMIC de référence des allègements réduit le coût budgétaire d'une hausse du SMIC tant qu'il dure. Le statique de −19 (base 2024) est probablement surestimé par rapport à la référence 2027.
4. Les lignes de dépense qui promettent des indexations complètes (nfp_autres_dep) coûtent davantage si la référence inclut les gels et sous-indexations du PLF/PLFSS 2027.
5. l_bandeaux et e_carence : facteurs à 0,5 de confiance faible, à remplacer par un chiffrage (T2 ou T4).
6. T8 (double compte) : aucune ligne n'est `votée` avec un facteur 1. La seule ligne votée (ens_chomage) est à 0. Les lignes `proposée` sont à 0, sauf la surtaxe (0,17).
