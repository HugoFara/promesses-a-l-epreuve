# T2b : sources primaires des couches 2 et 3

Date d'accès de toutes les sources : 2026-10-14. Outils : curl, WebFetch et WebSearch, sans navigateur. Fichiers produits :
- `corrections.csv` : 31 lignes ;
- `nouvelles_elasticites.csv` : 15 estimations ;
- `sources.csv` : 23 fichiers archivés dans `sources/T2b/`, avec leur sha256.

Contrainte rencontrée : le budget WebSearch de la session (200 requêtes, partagé entre agents) s'est épuisé en cours de tâche. Les dernières recherches (non-recours APL et AAH, document de travail Lefebvre-Lehmann-Sicsic, rapports annuels EFB) n'ont donc pas pu être faites. Elles sont listées plus bas.

## 1. Couche 2 : `programmes_stabilite_fr.csv`

### 1.1 Millésimes 2012, 2014 et 2016

Les trois couples (prev_t1, prev_t3) sont confirmés à l'identique, chacun par deux sources primaires indépendantes. Je propose de passer ces trois lignes en `high` et de remplacer leurs sources secondaires.

| Millésime | prev_t1 | prev_t3 | Source primaire lue | Recoupement |
|---|---|---|---|---|
| SP 2012-04 | −3,0 (2013) | −1,0 (2015) | Commission, SWD 2012, tableau III, p. 40 du PDF : « SBAP … −3,0 −2,0 −1,0 0,0 » (colonnes PS 2013 à 2016) | EFB Forecast Tracker, millésime SCP 2012 |
| SP 2014-04 | −3,0 (2015) | −1,3 (2017) | Commission, SWD(2014) 411, p. 9 et tableau p. 43 : « deficit of 3.0 % in 2015 », « target for 2017 … 1.3 % » | EFB SCP 2014 ; AN, compte rendu n° 70 du 23/04/2014 (Sapin : « déficit nominal de 3 % ») |
| SP 2016-04 | −2,7 (2017) | −1,2 (2019) | AN, rapport d'information n° 3684 (Rabault), p. 13 : « Programme de stabilité 2016 3,5 3,3 2,7 1,9 1,2 » | EFB SCP 2016 ; Conseil de l'UE, doc. 9200/16 (« 1,2 % du PIB en 2019 ») ; AN, compte rendu n° 74 du 20/04/2016 |

Points de vigilance :
- **SWD 2012** : la copie lue est hébergée par l'iFRAP et porte l'en-tête « projet » (« Bruxelles, le XXX »). Les chiffres sont identiques à ceux de l'EFB.
- **Programmes eux-mêmes** : le programme de 2014 est sur dalloz-actualite.fr, mais le site rejette curl et WebFetch. Le programme de 2012 n'a pas été retrouvé. Celui de 2016 non plus, avant épuisement du budget de recherche.

### 1.2 `real_t1` et `real_t3` contre Eurostat (toutes les lignes)

J'ai téléchargé la série gov_10dd_edpt1 (FR, B9, S13, PC_GDP, mise à jour du 2026-04-22) dans `sources/T2b/eurostat_gov_10dd_edpt1_FR_B9.json`.

- **Résultat** : aucun écart supérieur à 0,05 point sur les 40 valeurs renseignées. Toutes sont identiques à la série actuelle.
- **Valeurs vides** : `real_t3` de SP 2023-04 (année 2026) et de SP 2024-04 (année 2027) sont vides. C'est normal : Eurostat ne publie rien après 2025 (2025 = −5,1).

### 1.3 European Fiscal Board

Les rapports annuels de l'EFB (2017-2025, liens sur la page EFB de la Commission) n'ont pas été lus. J'ai trouvé mieux : le **Forecast Tracker** du secrétariat de l'EFB (`EFB_Forecast_Tracker.xlsx`, données 2001-2025). Il contient, pour la France, les prévisions de solde (% du PIB) :
- des programmes de stabilité (millésimes 2000-2023), à tous les horizons ;
- de la Commission (printemps et automne) ;
- des projets de plans budgétaires.

**Recoupement de tous les `prev_t1` / `prev_t3` du CSV.** Toutes les valeurs concordent, avec deux remarques :
- **SP 2003-12** : le CSV indique −3,55 pour 2004, l'EFB −3,6. L'écart est égal au seuil de 0,05, donc pas supérieur. C'est vraisemblablement un arrondi ; aucune correction proposée.
- **SP 2010-02** : il correspond au millésime EFB « SCP 2009 » (2011 : −6,0, identique). L'EFB s'arrête à 2012, ce qui ne permet pas de recouper prev_t3 (2013). La ligne EFB « SCP 2010 » (2010 : −8,0 ; 2011 : −7,4) ne correspond à aucun programme connu : la France n'a pas déposé de programme en 2010 et le suivant date d'avril 2011. Elle est à écarter.

**Erreurs de prévision (calcul T2b sur les données EFB).** Définition de l'EFB : réalisé au printemps T+1 moins prévision faite en T−1.

| Prévision | Toutes années | Hors années cibles 2009, 2010, 2020, 2021 |
|---|---|---|
| Programmes de stabilité, 1 an | −0,77 (n = 23) | −0,40 (n = 20) ; −0,54 sans la ligne douteuse « SCP 2010 » |
| Programmes de stabilité, 3 ans | −2,77 (n = 21) | −1,85 (n = 17) |
| Commission, printemps T−1 | −0,74 (n = 25) | −0,21 |
| Projets de plans budgétaires | −0,69 (n = 12) | −0,14 |

Ces résultats confirment le biais de la couche 2 (−0,60 à 1 an, −1,93 à 3 ans), avec une différence de méthode : le « réalisé » de l'EFB est la première publication, pas la série actuelle.

Comparaison avec d'autres pays, à 3 ans, hors crises :

| Pays | Erreur moyenne |
|---|---|
| Allemagne | −0,02 |
| Pays-Bas | +0,22 |
| Italie | −1,88 |
| Espagne | −1,74 |

## 2. Couche 3 : `elasticites.csv`

### 2.1 Lignes `medium` existantes

| id | Décision | Source primaire |
|---|---|---|
| `cir` | Passe en high. Le « ≈1 € » est une **moyenne toutes entreprises**, pas un chiffre propre aux PME (0,9 à 1,5 selon les études). Par taille (OCDE, cité par la CNEPI) : plus de 1,4 € sous 50 salariés, 1 € de 50 à 249 salariés, 0,4 € à partir de 250. Effets non significatifs pour les ETI et les grandes entreprises (IPP-PSE). | CNEPI 2019, p. 8 ; CNEPI 2021, p. 3, 12 et 13 (vie-publique.fr) |
| `mult_dep` | Passe en high. 0,78 la 1re année, 1,06 la 2e, 1,03 la 3e, 0,86 la 5e, 0,53 la 10e, 0,16 à long terme. Version 2026 : 0,76 / 1,01 / 0,88 / 0,54 / 0,17. | DG Trésor, DT 2017/04, p. 105 ; DT 2026/1, p. 18 |
| `mult_imp` | Passe en high. 1re année confirmée : TVA 0,32, IR 0,41, CSG 0,41, cotisations employeurs 0,20 ; s'y ajoutent les cotisations salariés (0,38). **La borne « 1,10, années 2 à 6 » n'est pas retrouvée.** Années 2 à 5 : 0,55 à 0,97 ; le DT ne donne pas l'année 6. | DT 2017/04, p. 107-117 |
| `apl` | Fourchette 50-80 % **confirmée** par le résumé de Fack (2005). Le 78 % ne figure pas dans le résumé et n'a pas été relu : le PDF Persée renvoie une erreur 403. | persee.fr (page archivée) |
| `capital_fr` | Reste en medium. cepr.org renvoie une erreur 403 et le budget de recherche était épuisé avant de retrouver le document de travail. | — |
| `tzcld` | Reste en medium. Primaire repérée (rapport final du comité scientifique, sur le site de la Dares), mais le site impose un captcha. | — |
| `garantie_jeunes` | Reste en medium. Le pare-feu de la Dares rejette les requêtes automatisées. | — |

Deux lignes déjà en `high` sont aussi à corriger ou à vérifier :
- **`rd_ocde`** : « 1,4 (moyenne) » semble faux. La CNEPI 2021 (p. 12), qui résume la note OCDE microBeRD de 2020, donne une moyenne d'environ 1 € ; 1,4 € est le ratio des petites entreprises. La colonne VoxEU, qui renvoie une erreur 403, n'a pas pu être relue. La correction est proposée avec un statut « à arbitrer ».
- **`sap`** : les 135 600 € par emploi viennent de Carbonnier (2009, p. 93 : 135 562 €/an). C'est une **borne basse**, car l'auteur suppose les nouveaux emplois payés au SMIC.

### 2.2 Nouvelles estimations (`nouvelles_elasticites.csv`)

- **Saez-Slemrod-Giertz** : élasticité du revenu imposable de 0,12 à 0,40 à long terme (« The most reliable longer-run estimates range from 0.12 to 0.4 », p. 58 du document de travail NBER 15012). La version JEL (2012) n'a pas été relue.
- **Colombie (Londoño-Vélez et Ávila-Mahecha)** :
  - élasticité du patrimoine déclaré au taux net de 2 (s.e. 0,35), fourchette 1,0 à 3,125 ; la double différence donne 4,0 ;
  - jusqu'à 20 % du rendement attendu perdu dès la première année ;
  - effets persistants après la fin de l'impôt (hystérésis).
- **Norvège** (Alstadsæter, Kopczuk, Telle 2013) : les dividendes versés par couronne de profit passent de 0,39 (2003) à environ 0 après la taxe de 2006. Les bénéfices non distribués doublent d'ici 2009. C'est une corrélation, pas un effet causal. Alstadsæter et Fjærli (2009) n'ont pas pu être lus (défi JavaScript de cesifo.org).
- **Suède** (Jacob, Michaely, Alstadsæter 2014) : après la baisse de 30 à 20 % de l'impôt sur les dividendes (2006), le ratio dividendes / rémunération totale augmente de 4 points (+35 %) dans les sociétés à propriétaire unique. L'effet tombe à environ 0 à partir de 4-5 propriétaires. Les salaires baissent de 3,6 points : c'est une substitution, pas un revenu nouveau.
- **CIR** : voir le tableau 2.1.
- **Bozio-Wasmer (2024)** :
  - **Élasticités des années 2000** (maquette Marsial de l'administration) : −0,9 au SMIC, décroissance linéaire jusqu'à −0,2 à 2 SMIC.
  - **Scénario central du rapport** : −0,4 d'élasticité individuelle au SMIC, décroissante jusqu'à 0 à 2 SMIC, plus −0,2 au niveau de l'entreprise (p. 194, note 57).
  - **Tableau 4.1 (modèle CES, p. 182), élasticités propres par tranche** : −0,608 (1 à 1,2 SMIC), −0,325 (1,2 à 1,6), −0,250 (1,6 à 2,5), −0,165 (2,5 à 3,5).
  - **Remplacement de l'interpolation 1,3-1,6 SMIC** : la valeur sourcée est −0,325 (CES). Avec le schéma linéaire central (calcul T2b), on obtient −0,48 à 1,3 SMIC et −0,36 à 1,6 SMIC ; avec les variantes, de −0,28 à −0,62. Les élasticités des années 2000 auraient donné −0,69 et −0,48.
  - **Chapitre 2 (p. 88)** : Kramarz-Philippon −1,5 ; CSERC 1996 environ −0,5.
- **Carbonnier (2009)**, étude retenue : réduction d'impôt pour emploi à domicile. Élasticité de la demande de −0,06, ratio d'efficacité de 0,13, coût par emploi d'au moins 135 562 €/an. Bozio-Wasmer citent aussi Carbonnier et al. (2022) sur l'incidence salariale du CICE ; cette étude n'a pas été lue.
- **Mésange** : tableaux de variantes 2017 et 2026, voir le tableau 2.1.
- **Non-recours** :

| Prestation | Taux | Source | Confiance |
|---|---|---|---|
| CSS, ensemble (2021) | 44 % | DREES, communiqué du 13/12/2022, lu par WebFetch | high, mais non archivé (le site rejette curl) |
| CSS sans participation | 31 % | idem | idem |
| CSS avec participation | 67 % | idem | idem |
| CMU-C (2018) | 32 à 44 % | Fonds CSS, rapport 2019 | medium |
| ACS (2018) | 38 à 57 % | idem | medium |
| AAH | 61 % | CGT, Mémo Sécu 44, primaire non identifiée | low, à ne pas utiliser |
| APL | non trouvé | — | — |

- **EFB** : erreurs de prévision, voir 1.3.

## 3. À lire avec un navigateur

| Document | Blocage |
|---|---|
| Programme de stabilité 2014-2017, dalloz-actualite.fr/document/programme-de-stabilite-2014-2017 | « Request Rejected » |
| Dares : rapport final TZCLD (2025) et rapport Garantie jeunes (2018) | captcha et pare-feu |
| DREES : pages et notes sur le non-recours (CSS : note du 11/12/2019 et mises à jour ; APL, AAH s'il en existe) | « Request Rejected » pour curl ; WebFetch fonctionne pour le texte des pages |
| CESifo WP 2530 (Alstadsæter et Fjærli 2009) | défi JavaScript |
| cepr.org / VoxEU : Lefebvre, Lehmann, Sicsic (capital_fr) ; Appelt et al. (rd_ocde) ; colonnes EFB | erreur 403 |
| Persée : texte intégral de Fack (2005) pour retrouver le 78 % | erreur 403 sur le PDF |
| old.parliament.bg (COM(2016) 330) et EUR-Lex | connexion coupée ; défi 202 |
| archive.org | 429, saturé par d'autres agents |

À noter : vie-publique.fr, qui bloquait les tâches précédentes, s'ouvre avec curl en suivant la redirection JavaScript (`/redirect_…`) et en conservant les cookies. C'est ainsi que les deux avis CNEPI et le rapport Bozio-Wasmer ont été obtenus.

## 4. Recherches non faites (budget WebSearch épuisé)

- Non-recours aux APL et à l'AAH (DREES, Cour des comptes, IPP) : rien trouvé avant l'épuisement.
- Mise à jour du non-recours à la CSS après 2021.
- Document de travail primaire de Lefebvre, Lehmann et Sicsic.
- Programmes de stabilité 2012 et 2016 eux-mêmes (sans objet en pratique, les chiffres étant confirmés deux fois).
- Rapports annuels de l'EFB, pour un éventuel paragraphe sur la France.

## 5. Décisions laissées à l'intégrateur

1. **Couche 2** : passer SP 2012, 2014 et 2016 en `high` et remplacer leurs URL. Le biais calculé ne change pas.
2. **Indicateur EFB** : ajouter ou non l'indicateur EFB (`biais_pstab_efb`) comme deuxième mesure du biais, sur la première publication. Il donne −0,40 à −0,54 à 1 an et −1,85 à 3 ans, hors crises.
3. **`cir` et `h_cir`** : la formulation « ≈1 € pour les PME » est inexacte ; la moyenne est d'environ 1 €. Par taille, retenir 1,4 / 1 / 0,4, ce qui est cohérent avec `h_cir`.
4. **`rd_ocde`** : arbitrer « 1,4 (moyenne) » contre « environ 1 (moyenne) », après lecture de la note OCDE de 2020.
5. **`mult_imp`** : supprimer la borne 1,10 non retrouvée et choisir la version de Mésange (2017 ou 2026, valeurs très proches).
6. **Interpolation 1,3-1,6 SMIC** : la remplacer par −0,33 (CES, Bozio-Wasmer) ou par le schéma linéaire (−0,36 à −0,48). Vérifier aussi `charges_smic`, qui reste fondé sur des élasticités supérieures à 1 (Crépon-Desplatz). Bozio-Wasmer jugent −0,6 au SMIC plus plausible aujourd'hui que les −0,9 des années 2000.
7. **`h_recours`** : ajouter la CSS (taux de recours 0,56). Ne pas utiliser le 61 % pour l'AAH.
8. **`sap`** : préciser que 135 600 € est une borne basse (Carbonnier 2009).
