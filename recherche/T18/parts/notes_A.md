# T18, phase 1, groupe A : notes

Règles du groupe : Élasticité capital, Élasticité patrimoine, Élasticité revenus, Élasticité succession. Date d'accès des sources : 2026-10-16. Les sources sont archivées dans `sources/T18/A/` (22 fichiers, sha256 dans `sources_A.csv`) ; toutes ont été contrôlées avec `pdftotext` (pas de PDF tronqué).

## 1. Résultat par règle (cible : 8 cas `observe`)

| Règle | `observe` | Tous types | Cible atteinte |
|---|---|---|---|
| Élasticité patrimoine | 7 | 7 | non (7/8) |
| Élasticité revenus | 4 (dont 2 de champ discutable) | 6 | non |
| Élasticité capital | 2 | 4 | non |
| Élasticité succession | 2 | 3 | non |

Lignes de `cout_A.csv` (Md€, montants positifs, sens donné par `sens`). L'écart vaut (ex post central − ex ante) / ex ante ; c'est une valeur calculée.

| id | Règle pressentie | Ex ante | Ex post central | Écart | Type | Confiance |
|---|---|---|---|---|---|---|
| cef_2012 | patrimoine | 2,325 | 2,33 | +0 % | observe | high |
| bouclier_60_2007 | patrimoine | 0,401 | 0,246 | −39 % | observe | medium |
| bouclier_50_2008 | patrimoine | 0,81 | 0,578 | −29 % | observe | medium |
| bouclier_suppr_2012 | patrimoine | 0,72 | 0,4 | −44 % | observe | high |
| isf_plafonnement_2013 | patrimoine | 0,667 | 0,709 | +6 % | observe | medium |
| isf_pme_tepa | patrimoine | 0,38 (2009) | 0,80 (2010) | +111 % | observe | medium |
| isf_reforme_2013 | patrimoine | 1,0 | 1,39 (calculé) | +39 % | observe | low |
| cehr_2012 | revenus | 0,4 | 0,63 | +58 % | observe | medium |
| tranche45_2013 | revenus | 0,32 | 0,344 | +8 % | observe | medium |
| qf_2013 | revenus (champ discutable) | 0,49 | 0,554 | +13 % | observe | medium |
| frais_pro_2013 | revenus (champ discutable) | 0,075 | 0,09 | +20 % | observe | medium |
| contrib_1pt_2011 | revenus (mixte capital) | 0,405 (calculé) | 0,4 | −1 % | reestimation | medium |
| qf_2014 | revenus (champ discutable) | 1,0 | 1,03 | +3 % | administratif | medium |
| bareme_capital_2013 | capital | 1,96 | 1,16 (calculé) | −41 % | observe | medium |
| ps_nonresidents_2012 | capital | 0,3 | 0,275 (calculé) | −8 % | observe | medium |
| ci_dividendes_2011 | capital | 0,645 | 0,6 | −7 % | reestimation | medium |
| pv_immo_2012 | capital | 1,212 (calculé) | 0,79 | −35 % | reestimation | medium |
| dmtg_tepa_2008 | succession | 1,821 (calculé) | 1,6 | −12 % | reestimation | medium |
| rappel_donations_2011 | succession | 0,018 | 0,006 | −67 % | observe | medium |
| successions_delais_2015 | succession | 0,5 | 1,0 | +100 % | observe | low |

Sens de l'écart pour la lecture : pour une recette (`economie`), un écart négatif veut dire moins de recette que prévu ; pour un coût, moins de coût que prévu. Je n'ai pas choisi les mesures selon le sens de l'écart : j'ai retenu tous les couples ex ante / réalisé trouvés dans les documents lus, sauf les exclusions du § 4.

`effets_A.csv` : une ligne (bouclier 2006 : plus de 93 000 bénéficiaires potentiels annoncés, 14 426 effectifs, ratio 0,155).

## 2. Conventions de classement

- **`observe`** : recette ou coût constaté, soit sur une ligne de recette distincte (contribution exceptionnelle sur la fortune, CEHR, restitutions du bouclier, montant de réduction ISF-PME, acompte sur dividendes), soit sous forme de **supplément d'impôt calculé par la DLF sur les déclarations effectives** (tranche à 45 %, quotient familial 2013, frais professionnels). Ce second cas est un « observe au sens large » : l'intégrateur peut vouloir le séparer (il ne mesure pas le contrefactuel sans réforme, seulement l'effet de la mesure sur les revenus effectivement déclarés).
- **`reestimation`** : rendement de « mesures nouvelles » imputé par l'administration dans l'exécution sans détail (Cour, RBDE 2011 et 2008), ou chiffre au conditionnel (plus-values immobilières 2012 : « ne serait que »).
- **`administratif`** : montant affecté à la sécurité sociale par une fraction de TVA (qf_2014).
- **`comportement_inclus_ex_ante`** : presque toujours `inconnu`. Aucun des chiffrages lus ne dit explicitement inclure une réaction des contribuables. Plusieurs reposent sur des revenus anciens (revenus 2008 pour la tranche à 41 %, 2009 pour la CEHR, 2011 pour la tranche à 45 %), ce qui suggère des chiffrages statiques, sans le dire. Seule exception : `frais_pro_2013` (`non`, l'ex ante signalait un effet de report sans le chiffrer). Pour les dons en numéraire de TEPA, le Sénat écrit que les estimations « ne tiennent pas compte de l'effet incitatif ».
- **Citations** : chaque citation a été recherchée dans le texte extrait des archives et s'y retrouve, au moins pour son début. Font exception les lignes de tableau reconstituées (séparateurs « / » ajoutés) : `ps_nonresidents_2012` (ex ante), `bouclier_suppr_2012`, `pv_immo_2012` et `bareme_capital_2013` (ex ante, annexes de la Cour). Pour ces lignes, les chiffres ont été vérifiés dans le bon document.
- **Déflateur** : 1 partout (comparaisons sur la même année, sauf `isf_pme_tepa`, 2009 contre 2010, non déflaté).

## 3. Détail par cas (pages, calculs, réserves)

### Élasticité patrimoine

- **cef_2012** : ex ante 2,325 Md€ (rapport AN n° 79, p. 117, et Cour RBDE 2012, annexe 6, p. 259). Réalisé 2,33 Md€ (Cour RBDE 2013, p. 82) ; le ministre annonçait 2,26 Md€ contre 2,25 « espérés » (AN, CR n° 59 du 23/01/2013, p. 4). Recette d'une seule année : la règle « Recette ponctuelle » (groupe D) pourrait aussi s'appliquer.
- **bouclier_60_2007** : coût prévu 401 M€, réalisé 246 M€ (restitutions 2007, vision exhaustive, rapport AN n° 1794, p. 33 ; 222 M€ à fin février 2008, rapport n° 1012, p. 24). L'écart vient du non-recours : il touche donc aussi la règle « Taux de recours ». Chiffrage du PLF 2006 non lu directement.
- **bouclier_50_2008** : 810 M€ (Sénat, rapport n° 404, art. 5, « L'impact de la mesure ») contre 578 M€ restitués au 31/05/2009 (rapport AN n° 1794, p. 30 ; « un peu moins de 600 millions », p. 266). Le rapporteur AN dit que le bouclier « coûte un peu moins des deux tiers de la dépense prévue ». Ambiguïté : coût total ou supplément du renforcement ? La Cour (RBDE 2008, p. 23) compte 0,4 Md€ pour le bouclier dans le coût de TEPA en 2008. Le réalisé est inférieur à l'ex ante dans les deux lectures.
- **bouclier_suppr_2012** : +720 M€ attendus en 2012 (Cour RBDE 2012, annexe 6, p. 258), +0,4 Md€ obtenus (p. 77). L'autoliquidation obligatoire du droit à restitution (−420 M€ prévus) interfère sans être isolée.
- **isf_plafonnement_2013** : 667 M€ prévus en LFI 2013, 709 M€ constatés (rapport AN n° 2172, p. 66). On y ajoute éventuellement 75,6 à 107 M€ de dégrèvements consécutifs à la censure des revenus capitalisés (haut 0,816, calculé).
- **isf_pme_tepa** : 190 M€ (2008) et 380 M€ (2009) prévus (Sénat, art. 6) ; 800 M€ en 2010 (Cour, référé du 26/11/2015, p. 1), puis 528 M€ en 2014 après le passage du taux de 75 % à 50 % (LFI 2011). L'année ex post diffère de l'année ex ante.
- **isf_reforme_2013** : 1 Md€ attendu (Cour RBDE 2013, p. 83 et annexe 7). Réalisé calculé à partir du tableau DLF (rapport AN n° 2172, p. 62) : ISF déclaré 2013 (3 634 M€) − ISF 2012 hors CEF (2 248 M€) = 1 386 M€ ; corrigé de la hausse de 7,9 % du patrimoine net taxable (777 990 → 839 566 M€), ≈1 208 M€. Contrefactuel grossier, d'où la confiance `low`.

### Élasticité revenus

- **cehr_2012** : 0,2 Md€ dans la version du PLF, 0,4 Md€ dans le texte voté, 0,63 Md€ constatés (rapport AN n° 1328, p. 96). La Cour (RBDE 2012, p. 262) écrit « conforme à la prévision, a été de 0,6 Md€ » : sa prévision de référence n'est pas précisée (révisée en cours d'année ?). Le rendement baisse ensuite à 0,522 Md€ en 2013 (revenus 2012), car la base taxable recule de 2,7 Md€ (rapport n° 2172, p. 50).
- **tranche45_2013** : 320 M€ prévus, 344 M€ effectifs (rapport n° 2172, p. 51), 57 659 foyers contre 50 000 attendus.
- **qf_2013** : 490 M€ prévus, 554 M€ effectifs (p. 53). **frais_pro_2013** : 75 M€ prévus, 90 M€ effectifs (p. 55). Ces deux mesures touchent le haut de la distribution sans viser les tranches supérieures du barème : leur rattachement à la règle est discutable. Elles sont gardées pour ne pas trier selon le résultat ; l'agent d'attribution tranchera.
- **contrib_1pt_2011** : ex ante calculé 0,405 Md€ en 2011 (230 M€ pour la tranche à 41 %, 130 M€ pour les PFL, 45 M€ pour les plus-values immobilières ; rapport général AN n° 2857, t. II, p. 58). Réalisé 0,4 Md€ (Cour RBDE 2011, p. 70). On ignore si la Cour vise l'article entier ou seulement la tranche ; dans le second cas, l'écart serait de +74 %.
- **qf_2014** : 1,0 prévu, 1,03 affecté (Cour RBDE 2014, p. 71 et p. 139).

### Élasticité capital

- **bareme_capital_2013** : 1,96 Md€ prévus pour l'ensemble barème + acompte (Cour RBDE 2013, annexe 7, p. 246). Réalisé calculé : 1,96 − 1,4 + 0,5 + 0,1 = 1,16 Md€ (p. 88 et note 57 ; l'acompte a rapporté 3,2 Md€ au lieu de 4,6, annexe 8, p. 248). France Stratégie (2020, p. 87-88, archivé dans `sources/T2a/fs_fiscalite_capital_2020.pdf`) estime pour les seuls dividendes un gain statique d'environ 0,4 Md€, mais un effet net de −0,7 à −1,7 Md€ (CRED) ou de −0,9 Md€ (IPP) en 2013, à cause de la baisse des dividendes versés. Il n'existe pas de chiffrage gouvernemental avant adoption pour les dividendes seuls, donc pas de ligne séparée ; c'est pourtant le cas le plus proche d'une élasticité du capital observée.
- **ps_nonresidents_2012** : 0,3 Md€ en année pleine (rapport AN n° 79, p. 22). Réalisé calculé : 126 M€ sur les revenus fonciers et 149 M€ sur les plus-values, soit 0,275 Md€ (rapport n° 2172, p. 68).
- **ci_dividendes_2011** : 645 M€ prévus (rapport général AN n° 2857, p. 90), 0,6 Md€ (Cour RBDE 2011, p. 70). Mesure presque mécanique.
- **pv_immo_2012** : 1 030 + 182 M€ prévus pour 2012 (Cour RBDE 2012, annexe 6) ; 1,3 Md€ en année pleine annoncés ; 790 M€ en 2012 selon la DGFiP (rapport AN n° 1328, p. 101), qui cite la baisse des transactions et l'anticipation des cessions. La Cour (RBDE 2012, p. 77) note seulement un moindre rendement de 0,2 Md€ sur l'IR.

### Élasticité succession

- **dmtg_tepa_2008** : somme des chiffrages 2008 par mesure du Sénat (rapport n° 404, art. 4) = 1 821 M€ (calculé). Le rapporteur AN cite 1,7 Md€ de baisse attendue (rapport n° 1012, p. 30). La Cour (RBDE 2008, p. 23, note 16) retient 1,6 Md€ en 2008, puis 3 Md€ en 2010 (RBDE 2010, p. 80). Ce sont des chiffrages de l'administration, pas des observations.
- **rappel_donations_2011** : 18 M€ prévus, 6 M€ constatés sur les donations de 2011 ; l'écart est attribué explicitement au comportement (anticipation des donations ; rapport AN n° 79, p. 135).
- **successions_delais_2015** : 0,5 prévu, 1,0 réalisé (Cour RBDE 2015, p. 62). Le texte législatif n'a pas été identifié ni lu. C'est une mesure de trésorerie : elle relève peut-être de la « Recette ponctuelle ».

## 4. Pistes non retenues (motif) et endroits cherchés

| Piste | Motif | Où j'ai cherché |
|---|---|---|
| Réforme de l'ISF de la LFR I 2011 (allègement de 1,857 Md€ en 2012) | Pas de réalisé pour la mesure elle-même. La seule comparaison disponible (ISF 2012 prévu à 3,1 Md€ en LFI 2012, 2,7 Md€ réalisés, rapport AN n° 2172, p. 62-63) porte sur un rendement total prévu après l'adoption. | RBDE 2011-2013, rapports AN n° 1328 et 2172 |
| Autoliquidation du droit à restitution sur l'ISF (−420 M€ en 2012) | Pas de réalisé isolé | RBDE 2012 |
| Volet ISF de TEPA en 2008 (≈0,41-0,42 Md€ prévus, calculé ; 0,7 Md€ selon la Cour, RBDE 2008, p. 23) | Doublon partiel avec `isf_pme_tepa` ; réalisé de type `reestimation`. À ajouter si l'intégrateur préfère la même année. | Sénat n° 404 ; RBDE 2008 |
| Abattement de 30 % sur la résidence principale à l'ISF (TEPA, 110-120 M€) ; réduction d'ISF pour dons (110 M€ en 2008, 160 M€ en 2009) | Pas de réalisé lu | Sénat n° 404 ; rapports AN n° 1012 et 1794 |
| IFI 2018 (rendement) | Recoupe la ligne existante `isf_ifi` | Non repris |
| Taxe à 75 % (taxe exceptionnelle de solidarité sur les hautes rémunérations, 2014-2015) | Ex ante seulement de seconde main (310 M€ brut, 210 M€ net, amendement du rapporteur général) ; aucun réalisé trouvé | 2 recherches web ; RBDE 2014 et 2015 |
| Contribution de 18 % sur les très hauts revenus (2013) | Censurée | RBDE 2013, annexe 7 |
| Tranche à 41 % de 2006, plafonnement global des niches (2009) | Pas de couple ex ante / réalisé trouvé ; le rapport AN n° 3631 traite du plafonnement sans chiffres de rendement comparables | AN n° 3631 |
| Hausse du PFL de 19 à 24 % (LFR IV 2011, +600 M€) | Pas de réalisé isolé | RBDE 2012 |
| Fin du seuil de cession des plus-values mobilières (180 M€ en 2012) ; plus-values mobilières au barème en 2013 (0,25 Md€) | Pas de réalisé | AN n° 2857 ; RBDE 2013 et 2014 |
| Prélèvement social sur le capital porté de 2,2 à 3,4 % (LFR II 2011, 1,33 Md€ en 2012) ; +2 points en 2012 (2,6 Md€) | Réalisé à chercher dans les rapports de la CCSS, non trouvés (1 recherche) | Web |
| Exit tax 2011 (53 M€ en 2012, 115 M€ en 2013) | « Les estimations de rendement ... n'ont pas fait l'objet d'une actualisation » (rapport AN n° 1328, p. 106). L'élargissement des dégrèvements en LFI 2024 n'a pas de chiffrage ex ante lu. | AN n° 1328 ; Cour, NEB recettes fiscales 2025 |
| Prélèvement social sur les stock-options (LFR II 2012, 75 / 317 M€, « hypothèse de comportement inchangé ») | Pas de réalisé ; rattachement à une règle du groupe A douteux | AN n° 79 |
| Aménagements des DMTG de la LFR II 2012 (abattement ramené à 100 000 €, rappel à 15 ans : 1,2 Md€ en 2013, 1,4 Md€ en croisière) | **Réalisé non trouvé**. La Cour signale seulement des droits de donation et de succession inférieurs à la LFI en 2013 (−0,9 et −0,4 Md€, RBDE 2013, p. 255), sans les isoler par mesure. | RBDE 2013 et 2014 ; AN n° 1328 et 2172 ; 2 recherches web |
| Volet successions du rappel de 6 à 10 ans (410 M€ en année pleine) ; suppression des réductions de droits liées à l'âge (130 / 290 M€) ; +5 points sur les tranches supérieures des DMTG (LFR I 2011) | Pas de réalisé | AN n° 79 et 127 ; RBDE 2011-2012 |
| Pacte Dutreil | Pas de chiffrage avant adoption (2003) ; le rapport de la Cour de novembre 2025 compare à des évaluations budgétaires postérieures | 1 recherche web |
| Hausse de la CSG de 1,7 point sur le capital (2018) | Partie de la bascule CSG, déjà écartée par T10a ; pas de réalisé isolé | Non repris |

## 5. Accès aux sources

- **budget.gouv.fr** : la page des documents du PLF 2014 renvoie une page vide, à curl comme à WebFetch, et **performance-publique** ne répond pas (DNS). Ni les Voies et moyens tome I ou II, ni les évaluations préalables n'ont pu être lus directement. Les ex ante viennent donc des rapports parlementaires et des tableaux de la Cour qui les citent.
- **vie-publique.fr** : les PDF passent par une redirection JavaScript, contournée en suivant l'URL `/redirect_…/` avec un fichier de cookies (RBDE 2012) ou par le chemin `/files/rapport/pdf/…`.
- **ccomptes.fr** : les pages `/fr/documents/NNN` renvoient du HTML ; le PDF est lié en `/sites/default/files/EzPublish/…`. Le RBDE 2013 a été tronqué au premier essai, puis retéléchargé en entier.
- **senat.fr** : la page HTML du rapport n° 404 s'est téléchargée sans difficulté.
- Un PDF téléchargé par erreur (CPO, rapport de 2025 sur l'industrie, sans rapport avec la tâche) a été supprimé.

## 6. Pour l'intégrateur

1. Les cas « observe au sens large » (supplément calculé par la DLF : `tranche45_2013`, `qf_2013`, `frais_pro_2013`) mesurent l'effet de la mesure sur les revenus effectivement déclarés, pas un contrefactuel. Faut-il les traiter comme `observe` ?
2. `qf_2013`, `qf_2014` et `frais_pro_2013` sont hors du champ strict de « Élasticité revenus » (tranches supérieures).
3. `bouclier_60_2007` et `bouclier_50_2008` relèvent autant du non-recours que de l'élasticité : la règle « Taux de recours » pourrait s'appliquer.
4. `cef_2012` et `successions_delais_2015` pourraient relever de la « Recette ponctuelle ».
5. **Sens des écarts** : les recettes sur hauts revenus (CEHR, 45 %, QF) dépassent leur prévision, alors que les mesures sur le capital et le patrimoine qui comportent un choix du contribuable (acompte 2013, plus-values immobilières, rappel des donations) rapportent moins. Pour les règles qui réduisent un rendement attendu, les cas « hauts revenus » vont contre la règle. Ce constat est à vérifier par la statistique de la phase 2 avec les facteurs gelés ; je ne l'ai pas calculée.
6. Toutes les dates de publication du réalisé vont de 2009 à 2016 : aucun cas du sous-échantillon « publié en 2026 », et un agent d'attribution peut connaître l'issue des plus médiatisés (bouclier, CEHR, ISF 2012).
