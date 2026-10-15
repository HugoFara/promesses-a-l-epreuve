# T17 – Programmes RN 2024 et LR 2024 : mesures, revirements et chiffrages par institut

Date d'accès de toutes les sources : 2026-10-15. Fichiers produits :

- `application_lignes_proposees.csv` : 22 lignes `rn24_*`, en-tête actuel de `data/raw/application_lignes.csv` (avec `famille` et `exception_symetrie`) ;
- `application_programmes_propose.csv` : 1 ligne (`rn24`) ;
- `chiffrages_par_institut.csv` : 41 lignes (id_ligne × chiffreur) ;
- `totaux_par_institut.csv` : 9 soldes ou constats (dont 1 pour LR) ;
- `statut_reference.csv` : 22 lignes, une par `rn24_*` (référence 2027, d'après les textes de `sources/T1/`) ;
- `sources.csv` : 40 fichiers archivés dans `sources/T17/`, avec leur sha256.

Signe : impact sur le solde public en Md€/an. Une valeur négative creuse le déficit.

**LR 2024 : aucun programme chiffrable ni chiffrage indépendant trouvé** (section 8). Aucune ligne `lr24_*` n'est donc proposée.

## 1. Principe de saisie

Même méthode qu'en T6 :

- une ligne par couple (ligne cible, chiffreur) ;
- les lignes « autres » de Montaigne et de l'iFRAP sont des résidus, de sorte que la somme des lignes retombe sur le solde publié ;
- les lignes qu'un institut n'a pas chiffrées sont absentes.

| Chiffreur | Somme des lignes | Solde publié | Origine de l'écart |
|---|---|---|---|
| Institut Montaigne | −71,0 | −71 | aucun (résidus `rn24_autres_dep` −21,05 et `rn24_autres_eco` +1,3) |
| Fondation iFRAP (26/06) | −14,525 | −14,5 | arrondi |

Pour `application_lignes_proposees.csv`, la valeur de départ (`independant`) est celle de Montaigne quand Montaigne chiffre la mesure. Sinon, c'est celle de l'iFRAP, comme pour `ens_fraude`, `nfp_zucman` ou `nfp_niches`. Six lignes sont dans ce cas : fraude, armateurs, rentes inframarginales, contribution à l'UE, retour de TVA et IFF. Elles font +19,78 brut, ce qui pèse lourd (section 7).

## 2. Le programme du RN et ses versions successives

**Document de référence** : « L'union fait la France. Un projet, une méthode », PDF publié le 24/06/2024 (`rn_programme_20240624.pdf`). Une seconde version du même jour (`rn_programme_20240625.pdf`, créée à 17:47) ajoute seulement un « Ministère d'État de la Mer et de l'Outre-mer ». **Ce programme ne contient aucun montant de coût ni de solde.** Le seul chiffre est une estimation de la fraude attribuée à la Cour des comptes. Public Sénat (24/06) : Bardella « n'a toutefois livré aucun chiffrage sur le projet dans son ensemble ».

Le programme est découpé en deux phases :

1. **« Temps de l'urgence », de juillet à l'automne 2024**, par un PLFR, des décrets et des circulaires :
   - baisse de la TVA « sur l'ensemble des produits énergétiques » (sans taux écrit) ;
   - annulation de la réforme de l'assurance chômage de juillet 2024 ;
   - exonération d'IR des médecins et infirmiers retraités qui reprennent une activité ;
   - suspension des allocations familiales des parents de mineurs récidivistes ;
   - suppression du droit du sol ;
   - remplacement de l'AME par une aide d'urgence vitale.
2. **« Temps des réformes », à partir de l'automne 2024**, dont les politiques « découleront en partie des conclusions » d'une commission d'évaluation des comptes publics :
   - abrogation de la réforme des retraites et retraite « progressive » ;
   - TVA supprimée sur une centaine de produits « en cas de forte inflation » ;
   - exonération de cotisations patronales sur les hausses de salaire de 10 % jusqu'à 3 SMIC, pendant 3 à 5 ans ;
   - poursuite de la baisse de la CVAE ;
   - part fiscale pleine dès le 2e enfant, PTZ transformé en subvention au 3e enfant, demi-part des veufs ;
   - privatisation de l'audiovisuel public, rationalisation des agences (ARS), « priorité nationale » sur les prestations (« si nécessaire par référendum constitutionnel ») ;
   - IR supprimé pour les moins de 30 ans, IS supprimé pendant 5 ans pour leurs entreprises, transmissions d'entreprises défiscalisées, héritage direct exonéré pour les classes modestes et moyennes, donations de 100 000 € tous les 10 ans, IFI remplacé par un IFF.

**Revirements datés pendant la campagne** (sources : Public Sénat, franceinfo, Montaigne, iFRAP) :

| Date | Mesure | Changement | Source |
|---|---|---|---|
| 12/06/2024 | Retraites | Bardella lie l'engagement à la situation budgétaire (« nous serons […] amenés à faire des choix », RTL) | Public Sénat, « réajuste son programme » |
| 17/06/2024 | Retraites | Abrogation promise « à partir de l'automne » (Le Parisien) | idem |
| 17/06/2024 | Médecins | Selon la fiche Montaigne, Bardella a dit que « cette réforme ne se fera que dans un second temps ». La mesure est pourtant dans la phase 1 du programme du 24/06. | fiche Montaigne médecins |
| 24/06/2024 | Retraites | 60 ans avec 40 annuités pour les carrières commencées avant 20 ans « à compter des textes budgétaires de l'automne ». Pour les autres, la « progressivité » (62 ans, jusqu'à 42 annuités) sera « déterminée après l'audit budgétaire » | Public Sénat, 24/06 |
| 24/06/2024 | TVA énergie | Taux de 5,5 % non confirmé (« réalignement » sur la moyenne européenne). Coût annoncé : 7 Md€ pour la fin de 2024, 12 en année pleine. Financement : niche des armateurs 1,2, taxe sur les énergéticiens 3, ristourne UE 2 | Public Sénat, 24/06 |
| 24/06/2024 | TVA sur 100 produits | Seulement « en cas de forte inflation » (contre une suppression temporaire en 2022) | programme ; Public Sénat |
| 24-25/06/2024 | Retraites (coût) | Un porte-parole avance 1,6 Md€ (F. Leggeri), puis J.-P. Tanguy 9 Md€ « à terme » (Reuters) | franceinfo, 25/06 |
| juin 2024 | Autoroutes | Nationalisation abandonnée | iFRAP |
| 26/06/2024 | IR des moins de 30 ans | Plafonnement évoqué après le débat (« tout cela peut se moduler », S. Chenu) | Public Sénat, « réajuste » |

**Ce qui est compté** : toutes les mesures du programme écrit du 24/06, phase 2 comprise. Montaigne (synthèse du 5/07) et l'iFRAP (26/06) font de même : les deux comptent l'abrogation de la réforme des retraites et la TVA sur les produits de première nécessité. Le NFP est traité de la même façon : ses mesures de phases 2 et 3 sont comptées. Les deux mesures conditionnelles posent des décisions à l'intégrateur (section 9, points 1 et 2).

## 3. Résultats par chiffreur

### Institut Montaigne (RN −71), confiance high

Le site renvoie un défi Cloudflare. Les pages ont été lues sur web.archive.org : synthèse du 17/07/2024, identique à tous les snapshots jusqu'en 2026, et toutes les fiches. Le PDF des micro-chiffrages, créé le 12/07/2024, a aussi été lu. Le communiqué date la synthèse de « quarante-huit heures » avant le second tour, soit le 5/07. Le total vaut −71, pour 85 de dépenses et 14 d'économies.

Points de vigilance :

- **Le total des dépenses ne correspond pas aux postes listés.** Les 8 postes principaux font 63,95 et les « autres mesures » 33,46, soit 97,4 au lieu de 85. L'écart de 12,4 est proche du PTZ du 3e enfant (12,6), sans explication. Le résidu `rn24_autres_dep` retient donc 85 − 63,95 = 21,05, sur le même principe qu'en T6 (le bandeau fait foi).
- **IR des moins de 30 ans** : 3,7 dans la synthèse, 0,7 dans le PDF des micro-chiffrages (vérifié sur l'image de la page 2).
- **Exonération sur les hausses de salaire** : la synthèse retient 0,8, le coût de 2025. La fiche donne 4,8 en 2027 et 12 en 2029. C'est une différence d'horizon avec les autres lignes, qui sont à 3 ans : à l'horizon 2027, Montaigne vaudrait −4,8 et le solde −75.
- **Audiovisuel** : 2 dans le tableau de la synthèse, 1,6 dans son texte. L'économie n'arrive qu'« à horizon de 3 à 5 ans ».
- **Impôts de production** : la synthèse retient 5,1, le rendement de la C3S, alors que la fiche chiffre 7,3 cumulés sur 2024-2027, retour d'IS compris. La CVAE est supposée déjà supprimée dans la trajectoire.
- **TVA sur les produits de première nécessité** : 6,7, milieu de 4,7 et 8,8. Le chiffrage ne tient pas compte de la condition « forte inflation ».
- **Mesures neutres ou absentes** :
  - indexation des pensions (27,4 sur trois ans) : jugée déjà dans le droit, donc neutre ;
  - annulation de la réforme de l'assurance chômage : 0 ;
  - IFF : « imprécis », non chiffré ;
  - fraude, armateurs, rentes inframarginales, ristourne UE : absents de la synthèse.
- **Révisions** : aucun montant n'a changé entre les versions archivées (TVA énergie : 21/06 et 25/07 ; salaires : 20/06 et 25/07). Les versions de juillet ajoutent seulement les « commentaires de l'équipe de campagne ».

### Fondation iFRAP (RN −14,5 ; versions antérieures −10,9 et −8,5), confiance high

Les tableaux sont des images, lues après agrandissement. Il y a trois versions :

| Version | Dépenses | Recettes | Solde | Principaux changements |
|---|---|---|---|---|
| 20/06 (archive du 21/06) | −9,2 | −17,6 | −8,5 | abrogation 8 ; salaires −10 ; armateurs 2 ; retour TVA 9,5 |
| 24/06 (archive du 25/06) | −9,2 | −20,1 | −10,9 | ajoute IFF +4, rentes +0,6, UE +2, armateurs 1,1, DMTG |
| 26/06 (page en ligne) | −6,0 | −20,5 | −14,5 | abrogation 10 ; salaires −8 ; rentes 3 ; retour TVA 6,68 ; ajoute uniforme 1,2, C3S 0, PTZ −2, transmissions −0,7 |

Constats :

1. **Retour de TVA de +6,68** (9,5 dans les versions antérieures) : un effet induit de la baisse de TVA, compté en recette. Montaigne exclut ce type d'effet. Pour le NFP, l'iFRAP n'a pas compté les « retours macro » revendiqués par le parti (≈30,8, voir T6). C'est une **asymétrie interne à l'iFRAP**. Sans cette ligne, le solde iFRAP vaut −21,2.
2. **Abrogation des retraites comptée (10)**, alors que le texte juge qu'elle « ne verrait probablement jamais le jour car infinançable ».
3. **TVA énergie à −16,7 brut** : c'est l'ensemble des recettes de TVA sur l'énergie selon Montaigne, et le chiffre de Bercy (16,8). Net du retour de TVA : −10,0.
4. **Priorité nationale +13,3**, « pas constitutionnelle en l'état » selon le même texte, mais comptée.
5. **Montants du parti repris** : armateurs 1,1, rentes 3, UE 2. Ils ne sont pas réestimés.
6. L'iFRAP chiffre à 0 la CVAE (trajectoire) et la C3S (« sans doute en 2028 »).

franceinfo (25/06) cite un « 5,5 milliards » de l'iFRAP qui ne correspond à aucune version archivée : non retenu.

### Asterès : pas de chiffrage propre

Trois notes de juin 2024, toutes lues :

- `ASTERES_RN_NFP.pdf` (T6) : « Asterès n'a pas réalisé de chiffrage détaillé » ; les dépenses représentent « au bas mot » des dizaines de milliards.
- `ASTERES_RN.pdf` : « le flou entourant un certain nombre de mesures rend tout chiffrage […] difficile ». Elle rappelle le gain de 16 Md€ attendu de l'immigration (Marine Le Pen, Les Échos, 2024), non détaillé.
- `RN-2-1.pdf` : déficit « d'environ 3,9 % du PIB par an ». C'est le **chiffre de Montaigne pour le programme présidentiel 2022 (101,8 Md€)**, repris faute de programme 2024.

Le −101,8 figure dans `totaux_par_institut.csv` par symétrie avec T6, où le « crédible » d'Asterès pour le NFP est saisi. Il porte sur un autre programme et n'est pas un chiffrage d'Asterès : il faut l'exclure de la sensibilité (section 9, point 6).

### OFCE : pas de chiffrage

La page `programmes/rn.html` (Paetzold, Plane, Saumtally) compile les « montants calculés par le RN », surtout en 2022, et ceux de Montaigne. Elle ne donne aucun solde. Elle signale que la baisse de la contribution à l'UE « n'est pas crédible » (budgets 2021-2027 déjà votés).

### Chiffrages partisans ou administratifs (confiance medium)

- **RN** : TVA énergie −12 en année pleine ; armateurs +1,2 ; énergéticiens +3 ; UE +2 (Bardella, 24/06, via Public Sénat). AME +1 (fiche Montaigne). Retraites −9 « à terme » (Tanguy, via franceinfo).
- **Bercy** : TVA énergie ≈16,8 (Public Sénat), « communiqué à des journalistes » mi-juin (franceinfo). Ce chiffrage émane d'un gouvernement en campagne. Il est saisi comme `Bercy (via presse)` et doit être traité comme le « camp présidentiel » de T6.

### Non trouvés

- **Terra Nova, La Grande Conversation, Fondation Jean-Jaurès, IPP, Rexecode, Fipeco** : aucun chiffrage du programme RN 2024 trouvé. Recherches menées :
  - WebSearch : une recherche étendue combinant les six noms, une sur Rexecode, une sur Terra Nova et Jean-Jaurès ;
  - liste des PDF de juin-juillet 2024 d'asteres.fr via l'index Wayback (seules les notes NFP et RN ci-dessus existent).

  franceinfo cite la Fondation Jean-Jaurès (« intenable d'un point de vue budgétaire ») sans montant.
- **Cette et Chaney (Telos)** : 50 à 120 Md€ pour le seul retour à 60 ans, effets sur les recettes compris. Le chiffre est cité par la fiche retraites de Montaigne ; l'article n'a pas été trouvé (une recherche). Il n'est pas saisi.

## 4. Lignes où les chiffreurs divergent le plus

| Ligne | Montaigne | iFRAP | Autres | Raison |
|---|---|---|---|---|
| rn24_retraites | −34,7 | −14 | parti −9 | **Périmètre** : Montaigne défait aussi les réformes d'âge et de durée 2003-2014 pour 65 % d'une génération (26,5), alors que l'iFRAP compte 4 pour les carrières longues |
| rn24_preference_nationale | +6,4 | +13,3 | — | Hypothèse sur la part d'étrangers rendus inéligibles (45 % au médian chez Montaigne) ; aucune méthode publiée par l'iFRAP |
| rn24_salaires | −0,8 (2025) | −8 | Montaigne 2027 : −4,8 | **Horizon** dans la synthèse Montaigne ; effet d'aubaine |
| rn24_tva_energie | −11,3 | −16,7 brut (−10,0 net du retour) | Bercy −16,8 ; parti −12 | **Assiette** : Montaigne exclut ce qui est déjà à 5,5 % ; l'iFRAP est brut |
| rn24_agences | +3,6 | +8 | — | **Périmètre** : ARS et hôpitaux, ou toutes les agences |
| rn24_audiovisuel | +2 (1,6) | +4 | — | Part cessible (Montaigne) ou dotations totales (iFRAP) |
| Lignes iFRAP seules | non chiffrées | fraude 3, armateurs 1,1, rentes 3, UE 2, retour TVA 6,68, IFF 4 | — | **Sélection** : c'est la principale raison de l'écart entre −71 et −14,5 |
| rn24_autres_dep | −21,05 | −9,95 | — | PTZ 12,6 contre 2 ; IR des jeunes 3,7 (ou 0,7) contre 3 ; enseignants 5,8 non chiffrés par l'iFRAP |

## 5. Familles et règles proposées (même logique que NFP et Ensemble)

| Ligne | Famille | Règle (facteur) | Ligne analogue | Commentaire |
|---|---|---|---|---|
| rn24_retraites | retraites_age | Substitution retraites (0,8) | nfp_retraites | — |
| rn24_tva_energie | **aucune** | — | ens_elec (accise électricité, 0,92) | voir proposition A |
| rn24_tva_pn | **aucune** | — | (nfp : blocage des prix, `controle_prix`, dans le résidu) | voir proposition B |
| rn24_production | **aucune** | — | — | voir proposition C |
| rn24_part_fiscale | impot_revenu | Élasticité revenus (0,9) | nfp_ir | discutable (section 6) |
| rn24_donations | succession | Élasticité succession (0,9) | ens_succession | — |
| rn24_medecins | niche_ir_retraites | Aucune (1) | e_abat (sens inverse) | — |
| rn24_salaires | exoneration_remuneration | Aucune (1) | ens_prime | — |
| rn24_autres_dep, rn24_autres_eco | residu | Aucune (1) | nfp_autres_dep, ens_autres_dep | — |
| rn24_preference_nationale | prestation_restriction | Aucune (1) | e_ame | discutable (section 6) |
| rn24_ame | prestation_restriction | Aucune (1) | e_ame | — |
| rn24_audiovisuel | reforme_structurelle_etat | Réforme structurelle (0,8) | e_oper | discutable (section 6) |
| rn24_agences | reforme_structurelle_etat | Réforme structurelle (0,8) | e_oper | — |
| rn24_chomage | assurance_chomage | Aucune (1) | ens_chomage (sens inverse) | valeur 0, voir section 7 |
| rn24_fraude | effet_promis | Effet promis (0,333) | ens_fraude | — |
| rn24_armateurs | impot_societes | Élasticité IS (0,94) | l_surtaxe | discutable (section 6) |
| rn24_rente_infra | contribution_exceptionnelle | Recette ponctuelle (0) | nfp_superprofits | — |
| rn24_ue | **aucune** | — | — | voir proposition D |
| rn24_retour_tva | effet_promis | Effet promis (0,333) | nfp_egalite | discutable (section 6) |
| rn24_iff | impot_patrimoine | Élasticité patrimoine (0,97) | nfp_isf | — |
| rn24_taux | charge_interets | Taux d'intérêt (1) | nfp_taux, ens_taux | valeur à calculer par l'intégrateur |

**Familles nouvelles proposées** (aucune n'est créée dans `data/`) :

- **A. `tva_energie`** (TVA sur les produits énergétiques). Règle d'élasticité-prix, « quel que soit le sens », comme les accises : une baisse de taxe fait monter la consommation, qui reste taxée. Deux options :
  1. découper la ligne selon l'assiette Montaigne (produits pétroliers 10,5 sur 15,6 au taux de 20 %, soit 67 % ; électricité 3,9 et gaz 1,3) et appliquer « Élasticité carburants » (0,7) à la première part, « Élasticité électricité » (0,92) au reste ;
  2. créer une règle propre.

  **Symétrie** : `ens_elec` (accise électricité) reçoit 0,92. Laisser la TVA énergie du RN à 1 serait moins favorable que le traitement d'Ensemble ; lui appliquer 0,7 en bloc serait plus favorable que celui de l'électricité.
- **B. `tva_produits`** (TVA réduite ou nulle sur des produits de consommation courante). Règle « Aucune » : Montaigne note qu'une hausse de consommation a « peu d'impact » avec un taux de 0 %. La question principale est ailleurs : faut-il compter une mesure conditionnelle (section 9, point 2) ?
- **C. `impots_production`** (impôts de production : CVAE, C3S). Règle « Aucune », car le chiffrage Montaigne intègre déjà le retour d'IS. Sinon, `aides_entreprises` (règle « Aucune » aussi) donne le même résultat numérique, mais son libellé vise les aides ciblées.
- **D. `contribution_ue`** (réduction négociée de la contribution au budget européen). Aucune ligne analogue chez le NFP ou Ensemble. La mesure dépend de partenaires extérieurs et, selon Le Point (via franceinfo) et l'OFCE, n'est pas possible avant le prochain cadre financier pluriannuel (2028). Deux options : facteur 0 pour l'horizon 2027 (logique de calendrier, proche de « Recette ponctuelle ») ou « Effet promis » (0,333), en créant la famille dans le premier cas.

## 6. Règles discutables (`exception_symetrie` laissé vide, décisions pour l'intégrateur)

1. **rn24_part_fiscale, Élasticité revenus (0,9)**. Cette règle est calibrée sur des hausses d'impôt du top 0,1 % (`eti_top`). La part fiscale pleine concerne 8 % des foyers, surtout des familles moyennes et aisées. Appliquer 0,9 réduit le coût de 10 %, au titre de la réaction des revenus. Par symétrie, une baisse d'IR reçoit la même élasticité qu'une hausse (logique « quel que soit le sens » des familles accise et succession). Si l'intégrateur juge l'élasticité hors champ, il faudrait une famille « quotient familial » avec la règle « Aucune ».
2. **rn24_preference_nationale, règle « Aucune »**. Le programme subordonne la mesure à un référendum constitutionnel « si nécessaire ». Montaigne et l'iFRAP la jugent contraire au principe d'égalité. La règle « Nouvelle assiette : risque juridique » (0,8) existe pour `l_zucman`, mais elle est rattachée à la famille `nouvelle_assiette_patrimoine`. Le cas analogue chez Ensemble, `ens_retention`, porte sur un effet de comportement (règle « Effet promis »), pas sur un risque juridique. Un risque juridique non appliqué ici le serait-il ailleurs ? Le NFP et Ensemble n'ont aucune mesure d'économie de ce type.
3. **rn24_audiovisuel, Réforme structurelle (0,8)**. L'économie n'arrive qu'à 3-5 ans selon Montaigne : en 2027 (horizon 3 ans), elle pourrait être nulle. La règle 0,8 est peut-être trop favorable, mais aucune règle « calendrier » n'existe.
4. **rn24_armateurs, Élasticité IS (0,94)**. On pourrait aussi retenir `niches_fiscales` (médiane des estimations), mais la niche est identifiée et unique. La règle IS paraît plus juste ; elle est calibrée sur les surtaxes d'IS 2013 et 2025.
5. **rn24_retour_tva, Effet promis (0,333)**. La règle « effets promis divisés par 3 » est calibrée sur CICE et TEPA (`cice_emploi`, `tepa_heures`). Le retour de TVA est un effet de bouclage macroéconomique, que le projet n'applique à aucun autre programme. Les retours keynésiens du NFP ne sont dans aucune ligne. Option symétrique stricte : **supprimer la ligne** (facteur 0). Option de compromis : la garder à ÷3, comme `nfp_egalite`.
6. **rn24_rente_infra, Recette ponctuelle (0)**. La règle est identique à celle de `nfp_superprofits`, ce qui assure la symétrie. Elle annule pourtant une recette que le RN présente comme pérenne. Le rendement réel de la contribution existante est nul en 2027 (état A, ligne 1752), ce qui va dans le même sens.

## 7. Points de vigilance et asymétries possibles avec NFP et Ensemble

- **Lignes iFRAP ajoutées à la base Montaigne** (+19,78 brut ; environ +7,4 après règles et facteurs de référence, plus 0 à 2 selon la règle retenue pour l'UE). Ce choix suit le précédent `ens_fraude` (iFRAP ajouté au −20,6 de Montaigne). Pour Ensemble, une seule ligne (3) était concernée ; pour le RN, il y en a six. Le résultat dépend fortement de ce choix.
- **Assurance chômage, sens inverse de `ens_chomage`.** Ensemble ne reçoit aucun crédit pour sa réforme, déjà dans la référence (facteur 0). Par symétrie, l'annulation promise par le RN devrait coûter par rapport à la référence 2027. Or Montaigne la chiffre à 0 et le montant 2027 n'est pas isolé (T1). Laisser 0 favorise le RN ; mettre −4,5 (le chiffre Montaigne pour Ensemble) serait symétrique, mais le décret de juillet 2024 a été remplacé par d'autres textes (T1).
- **CVAE.** Les deux chiffreurs supposent la CVAE supprimée en 2027. La référence 2027 en garde 4,11 Md€ (PLF 2027, état A). Par rapport à la référence 2027, « poursuivre la baisse de la CVAE » coûterait jusqu'à 4,1 brut (environ 3,3 net d'un retour d'IS à 20 %, hypothèse de Montaigne). Ce montant n'est pas compté.
- **Indexation des pensions.** Montaigne (fiche) attribue au RN le « maintien de la réindexation des pensions », neutre en 2024. Le PLFSS 2027 (art. 35) prévoit une sous-indexation de 4,0 Md€ au-dessus de 1 260-1 281 €/mois. Si la promesse est retenue, elle coûte 4,0 par rapport à une référence qui inclut le PLFSS (famille `annulation_economie_reference`). **Elle ne figure pas dans le programme écrit du 24/06** : aucune ligne n'est proposée. T1 fait la même remarque pour le NFP.
- **Horizon des salaires** (0,8 contre 4,8) et **total Montaigne incohérent** (97,4 listés contre 85) : voir section 3.
- **Retraites et référence 2027** : facteur 0,971, même calcul que `nfp_retraites`.

## 8. LR 2024 : pas de programme chiffrable, pas de chiffrage indépendant

- **Pas de programme législatif officiel.**
  - Voltage (juin 2024) : LR, « privé de leader, n'[a] pas présenté de programme officiel » après le ralliement d'É. Ciotti au RN.
  - La page `republicains.fr/programme2024/`, archivée le 20/06 et le 01/07/2024, est le programme des **européennes**. On y lit des orientations nationales sans chiffrage : baisse des cotisations salariales jusqu'à 3 SMIC, transmission d'un million d'euros sans droits, et « contre-budget présenté à l'automne 2023 » avec 25 Md€ de baisse de dépenses.
  - Les éléments relevés par la presse ne sont pas chiffrés par le parti, à une exception près : un plan police de 25 Md€ sur cinq ans (Voltage). Ces éléments sont : baisse des cotisations sous 3 SMIC (4 200 € net), taxes sur l'électricité finançant l'éolien, allocations familiales universelles, AME réduite, 200 000 places de prison (sic, Voltage).
- **Aucun chiffrage indépendant** :
  - Institut Montaigne : seules trois listes, « celles qui ont obtenu le plus grand nombre de voix à l'issue du premier tour » (communiqué) ;
  - iFRAP : comparateur qualitatif (contre-budget 2024, positions de 2022), sans fiche « vrai coût » ;
  - OFCE : pas de page LR (`programmes/lr.html` renvoie une 404) ;
  - Asterès : aucune note LR en 2024 dans l'index Wayback (la page « programme économique des Républicains n'est pas sérieux » date de 2017) ;
  - WebSearch (×3 : « chiffrage programme Les Républicains législatives 2024 », recherches sur le programme et sur le « pacte législatif » de juillet 2024) : rien.
- Le « pacte législatif d'urgence » de L. Wauquiez date de juillet 2024, après le scrutin, et n'est pas chiffré (presse).

Conformément à la consigne, la recherche LR s'arrête là. Une ligne « LR 2024, aucun chiffreur » est notée dans `totaux_par_institut.csv`.

## 9. Décisions laissées à l'intégrateur

1. **Retraites** : faut-il compter l'abrogation et la retraite progressive, renvoyées « après l'audit » ? Les deux chiffreurs les comptent, comme le NFP est compté. Valeur de départ : −34,7 (Montaigne) ou −14 (iFRAP).
2. **TVA sur les produits de première nécessité « en cas de forte inflation »** : compter −6,7, ou 0 tant que la condition n'est pas remplie ? Aucune règle « mesure conditionnelle » n'existe.
3. **Nouvelles familles** A à D (section 5) : TVA énergie, TVA sur produits, impôts de production, contribution à l'UE.
4. **Les six lignes iFRAP seules** (section 7), et surtout le **retour de TVA** (section 6, point 5).
5. **Assurance chômage, CVAE et indexation** par rapport à la référence 2027 (section 7).
6. **Asterès −101,8** : à exclure de la sensibilité, car c'est le chiffre de Montaigne sur le programme 2022.
7. **Montaigne, valeurs internes** : salaires 0,8 ou 4,8 ; audiovisuel 2 ou 1,6 ; IR des jeunes 3,7 ou 0,7 ; résidu des dépenses 21,05 (bandeau) ou 33,46 (postes listés).
8. **Charge d'intérêts `rn24_taux`** : à calculer avec la formule de `nfp_taux` sur le solde retenu.
9. **Chiffrages partisans** (RN, Bercy) : à exclure de la sensibilité principale, comme en T6.

## 10. Ce qui n'a pas été lu

- institutmontaigne.org en direct (Cloudflare) : remplacé par Wayback, sans perte de contenu identifiée.
- L'article de Telos (Cette et Chaney) et l'article des Échos de Marine Le Pen (février 2024, gain de 16 Md€ attendu de l'immigration) : cités de seconde main.
- La version de l'iFRAP à −5,5 citée par franceinfo : non retrouvée.
- L'article Europe 1 du 24/06 (programme « définitif ») et la page RN « 22 mesures » (programme 2022) : non lus, non archivés.

## 11. Intégration (15/10/2026)

Décisions prises à l'intégration dans `data/raw/` (détail dans `historique.csv`) :

- **Point de départ** : Montaigne (−71), complété par les lignes chiffrées par l'iFRAP seul, comme `ens_fraude`.
- **Retour de TVA** (`rn24_retour_tva`, +6,68) : pas de ligne. Aucun autre programme ne reçoit d'effet de bouclage. Il reste dans les chiffrages de l'iFRAP en `hors_lignes`, comme `ens_hors_lignes`.
- **TVA énergie** : découpée en `rn24_tva_carburants` (Élasticité carburants) et `rn24_tva_elec_gaz` (Élasticité électricité) selon l'assiette Montaigne taxée à 20 % (produits pétroliers 10,4 sur 15,6 Md€). Les familles `accise_*` deviennent `taxe_carburants` et `taxe_electricite_gaz`.
- **Familles ajoutées** (règle « Aucune ») : `tva_produits`, `impots_production` et `contribution_ue`.
- **Assurance chômage** : −4,5, par symétrie avec `ens_chomage`. La réforme est dans la référence, donc l'annuler coûte son rendement.
- **Indexation des pensions** : pas de ligne. Elle est absente du programme écrit et n'a pas été annoncée par le parti.
- **Charge d'intérêts** : −1,4. Même calcul que `nfp_taux` (≈ 3 pb par point de dette).
- **Lignes inchangées** : les autres lignes, dont la préférence nationale (règle « Aucune », risque juridique noté dans la justification) et les montants internes Montaigne (salaires 0,8).
- **Résultat** : chiffrage de départ −63,8 ; après correction −60,2.
- **Écart assumé dans la comparaison par organisme** : Montaigne compte l'annulation de la réforme de l'assurance chômage à 0, parce que la réforme est hors de sa base. Le site la compte à −4,5, parce que la réforme est dans la référence. Cette comparaison garde la convention de chaque organisme. L'iFRAP ne chiffre pas la ligne : il reçoit la médiane des autres, soit 0. Ses deux soldes (Montaigne −56, iFRAP −17) sont donc environ 4,5 Md€ moins coûteux que s'ils suivaient la convention du site. Les deux cas sont signalés dans la note de la ligne Montaigne de `chiffrages_instituts.csv` et dans le texte de la section du site.
