# T21, groupe C : Taxe sur les rachats d'actions, Médiane des estimations

Recherche du 20/10/2026. Règles gelées au commit `686902b`. Sources dans `sources/T21/C/`, listées avec leur sha256 dans `parts/sources_C.csv`.

## Fichiers

| Fichier | Contenu |
|---|---|
| `cout_C.csv` | 1 cas étranger (US) pour la règle « Taxe sur les rachats d'actions », au format de T18 plus une colonne `pays` |
| `cout_C_instituts.csv` | 32 lignes au format de `data/raw/calibration_instituts.csv` : 14 mesures (11 de 2012, 3 de 2007) |
| `parametres_C.csv` | 2 tests de paramètre (`part_perdue_rachats`, `part_taxe_rachats_existante`) |

## 1. Taxe sur les rachats d'actions

### 1.1 Cas trouvé : taxe américaine de 1 % (IRA 2022)

- **Avant adoption** : JCT, JCX-18-22 (09/08/2022), texte voté par le Sénat. Ligne « Part 2 - Excise Tax on Repurchase of Corporate Stock » : 5,697 Md$ (exercice 2023), 7,875 (2024), 8,070 (2025), 73,686 sur 2022-2031. jct.gov renvoie 403 (Cloudflare) ; lu sur la copie Wayback du 01/04/2023.
- **Réalisé** : IRS SOI, Historical Table 20, ligne « Repurchase of corporate stock [17] ». 4 539 034 milliers de $ en FY 2024, cellule vide en FY 2023. La table s'arrête à 2024. Note [17] : « The FY 2024 [...] marks the first full year of reporting the 1% excise tax ». Attention, mon premier lecteur XML plaçait ce chiffre en colonne B (1999) parce qu'il ignorait les cellules vides. Vérification faite dans le XML brut, la cellule est bien `AP104`, soit 2024.
- **Écart** : −42 % en 2024 (4,539 contre 7,875). Sur le cumul 2023-2024 : −67 % (4,539 contre 13,572).
- **Comparabilité, pour l'intégrateur** :
  1. *Calendrier.* Les premières déclarations (Form 720, n° IRS 150, avec Form 7208) n'étaient exigibles qu'après les règlements de procédure de juin 2024. Pour les rachats de 2023 d'une société à exercice civil, l'échéance tombait le 31/10/2024, donc sur l'exercice fédéral 2025. Ce point vient des instructions du Form 7208 et de commentaires lus en extrait de recherche ; je ne l'ai pas vérifié dans le règlement lui-même. Une partie de l'écart peut donc n'être qu'un décalage. Le chiffre FY 2025, qui permettrait de trancher, n'a pas été trouvé. Endroits cherchés : page SOI excise, page Historical Table 20, recherches web (« Form 720 IRS No. 150 collections », « buyback tax collected billion »). Le règlement final du 24/11/2025 (archivé) ne contient aucune donnée de recette.
  2. *Taux.* La règle gelée est calibrée pour un taux de 33 % (part perdue 0,85). Ici le taux est de 1 %. Le cas teste-t-il la règle, ou seulement l'idée qu'un chiffrage officiel de taxe sur les rachats est trop optimiste ? À décider.
  3. *Comportement inclus ex ante* : `inconnu`, JCX-18-22 n'en dit rien.
- `type_ex_post = observe` (encaissements IRS). Drapeaux : `etranger`, `calendrier_paiement_incertain`, `taux_hors_champ_regle`.

### 1.2 Pistes sans cas

- **Canada, taxe de 2 % sur les rachats nets (depuis le 01/01/2024)**. Les chiffrages avant adoption n'ont été vus qu'en extrait de recherche : 2,1 Md$ CA sur 5 ans d'après le budget 2023, 2,98 Md$ CA d'après le DPB. Aucun réalisé publié trouvé : pas de ligne isolée trouvée dans les recettes fédérales. La page « tax measures » du budget du 04/11/2025 (budget.canada.ca/2025/report-rapport/tm-mf-en.html) ne mentionne pas cette taxe. **Non trouvé.**
- **Inde, taxe sur les rachats (section 115QA, étendue aux sociétés cotées en 2019)** : ni chiffrage officiel ni recette isolée trouvés. **Non trouvé.**
- **France** : la taxe actuelle (8 % du nominal et des primes) figure déjà dans `data/raw/mesures_cout.csv` (`rachats_2025`). Elle n'est pas reprise ici. Aucune donnée 2026 n'est publiée (le rendement 2026 reste une prévision, 0,2 Md€ en LFI 2026 et au PLF 2027).
- **Nouvelles estimations causales depuis T13 (14/10/2026)** : aucune trouvée. Une thèse de 2026 (Fairfield University, digitalcommons.fairfield.edu/etds/41) conclut à une baisse significative des rachats, mais je ne l'ai vue qu'en extrait : non retenue. La page PWBM de janvier 2025, qui chiffre une hausse du taux à 2 % ou 4 %, n'a pas pu être lue (404 avec WebFetch, contenu chargé par JavaScript) : non retenue.

### 1.3 Tests de paramètre (`parametres_C.csv`)

| Paramètre | Gelé | Trouvé | Lecture |
|---|---|---|---|
| `part_perdue_rachats` | 0,85 | aucune estimation nouvelle ; rapport réalisé/JCT 0,58 (2024) ou 0,33 (cumul) | Ce rapport ne mesure pas la part perdue : il mêle calendrier, assiette nette et réaction. Confiance `low`. Le paramètre n'est **ni confirmé ni infirmé**, et rien n'observe un taux de 33 %. |
| `part_taxe_rachats_existante` | 0,0238 (0,2 / 8,4) | 0,059 (0,5 Md€ constatés en 2025, Cour des comptes, NEB 2025, tableau 13, p. 26) | Le rendement 2025 inclut la taxe temporaire de mars 2024 à février 2025, ponctuelle. La prévision de 0,2 pour 2026-2027 reste plausible, mais la prévision 2025 (0,4 en LFI) a été dépassée de 25 %. Effet sur le rendement net de la taxe renforcée : −0,3 Md€ si le niveau de 2025 se maintenait. |
| `assiette_rachats_rel` | 1 (25,5 Md€) | pas de donnée nouvelle depuis T13 (34,8 Md€ en 2025, soit 1,36, déjà dans la fourchette haute de 1,37) | Non testé à nouveau. |

## 2. Médiane des estimations

### 2.1 Ce qui a été relevé

**Présidentielle 2012 (programme Hollande)**. Trois sources couvrent les mêmes mesures :
- l'**Institut Montaigne** (« Chiffrages-Déchiffrages 2012 », avec Les Échos). Le site est toujours en ligne, et les 53 fiches Hollande ont été téléchargées ; 11 fiches sont archivées ;
- **Terra Nova** (note du 22/03/2012). Ses annexes 1 et 2 alignent, mesure par mesure, le chiffre du candidat (26/01/2012), celui de Montaigne (première version du 16/03) et le sien. Le chiffre du candidat est donc lu dans Terra Nova, en source secondaire (`medium`) ;
- la **Fondation iFRAP** (tableau d'octobre 2011 sur le projet du PS, antérieur au programme du candidat).

Pour les dépenses (contrat de génération, emplois d'avenir, retraite à 60 ans), le chiffre du candidat vient de la dépêche Reuters du 26/01/2012 lue sur Zonebourse avec WebFetch. curl renvoie 403 : la page **n'est pas archivée**. La ligne sur la retraite est tronquée (confiance `low`).

**Présidentielle 2007 (programme Sarkozy)**. L'Institut de l'entreprise (débat2007.fr) n'a été lu que via une dépêche AFP du 13/02/2007 (`medium`). Je n'ai trouvé aucun second chiffreur par mesure. Le candidat ne donne qu'un total : « Mon projet représente 30 milliards d’euros en cinq ans ». Rexecode (communiqués de mars 2007, lus) évalue l'impact macroéconomique, pas le coût mesure par mesure.

**Réalisés.** Ils sont repris quand ils existaient déjà dans `data/raw/mesures_cout.csv` (tranche à 45 %, quotient familial, ISF, barème du capital, TEPA, TVA restauration, successions TEPA). Pour la tranche à 45 %, le quotient familial, l'ISF, le barème du capital et le « rabot », j'ai relu les sources (AN n° 2172, Cour des comptes RBDE 2013). Pour la TVA restauration et les successions TEPA, les sources n'ont pas été relues ; la note de la ligne le dit. Un réalisé est nouveau : contrat de génération, 83,16 M€ de CP exécutés en 2014 (Cour des comptes, RPA 2016, tableau n° 3, p. 72).

### 2.2 Tableau indicatif (non intégré, calculé à la main ; erreur = |chiffrage − réalisé| / |réalisé|)

| Mesure | Chiffrages | Médiane | Réalisé | Erreur de chaque chiffrage | Erreur de la médiane | `inclus_stats` |
|---|---|---|---|---|---|---|
| Tranche à 45 % | PS 0,7 ; Montaigne 0,4 ; Terra Nova 0,6 | 0,6 | 0,344 (2013) | 103 % ; 16 % ; 74 % | 74 % | oui |
| Contrat de génération | PS −2,3 ; Montaigne −2,527 ; iFRAP −10,56 | −2,527 | −0,083 (2014) | 2 671 % ; 2 945 % ; 12 623 % | 2 945 % | oui (horizon et dispositif différents) |
| ISF (retour sur 2011) | 2,3 ; 2,283 ; 2,3 | 2,3 | 1,39 (calculé) | 65 % ; 64 % ; 65 % | 65 % | non |
| Revenus du capital au barème | 4,5 ; 4,381 ; 4,6 | 4,5 | 1,16 (périmètre partiel) | 288 % ; 278 % ; 297 % | 288 % | non |
| Déductibilité des intérêts | 4,0 ; 3,9 ; 4,0 | 4,0 | 1,7 (réestimation, autre périmètre) | 135 % ; 129 % ; 135 % | 135 % | non |
| Quotient familial | Montaigne 0,45 | — | 0,554 | 19 % | — | oui (un seul chiffreur) |
| TEPA heures supplémentaires (2007) | Institut de l'entreprise −4,6 | — | −4,81 (2008) | 4 % | — | oui (un seul chiffreur) |
| TVA restauration (2007) | Institut de l'entreprise −2,5 | — | −3,3 (réestimation) | 24 % | — | non |
| Successions TEPA (2007) | Institut de l'entreprise −5,0 | — | −1,6 (réestimation) | 212 % | — | non |

Lecture prudente : sur les deux seules mesures retenues qui ont au moins deux chiffreurs, la médiane **n'est jamais plus proche du réalisé que le meilleur chiffrage**. Elle est meilleure que le pire, ce qui découle de sa définition. Sur la tranche à 45 %, Montaigne seul fait mieux (16 % contre 74 %). Sur le contrat de génération, tous les chiffrages sont très loin, parce que le dispositif n'a pas trouvé preneur. Sur les mesures exclues, les chiffrages sont presque identiques entre eux (Terra Nova reprend souvent le chiffre du candidat), donc la médiane n'apporte rien. **Ces chiffrages ne sont pas indépendants** : Terra Nova « confirme » le candidat, et Montaigne révise ses fiches après la critique de Terra Nova (capital : 2,8 puis 4,38). Deux mesures, c'est très en deçà du seuil de 5 cas. La règle reste **non jugeable** avec ce matériel.

### 2.3 Non trouvé (avec les endroits cherchés)

- **Réalisés 2012 manquants** :
  - fin de la défiscalisation des heures supplémentaires : AN n° 2172 p. 59, l'administration ne dispose que des estimations des PLF ;
  - abattement de succession à 100 000 € : RBDE 2013 ne donne que l'effet « année pleine » prévu (0,33 Md€) ; recherche web sans résultat ;
  - emplois d'avenir : la Cour donne seulement le total des contrats aidés (3,3 Md€ en 2016, vu en extrait de presse) ; RAP du programme 102 non lus ;
  - retraite à 60 ans pour les carrières longues : la CCSS donne la dépense totale des départs anticipés, tous dispositifs confondus (vue en extrait), pas le surcoût du décret de 2012 ;
  - doublement de la TTF : seule la TTF entière est réestimée par la Cour (ligne `ttf_2012`).
- **Dépense 2015-2017 du contrat de génération** (régime plus proche du chiffrage) : non trouvée. Le tableau de la Cour s'arrête à l'exécution 2014 et aux prévisions 2015-2016.
- **Présidentielle 2007, second chiffreur** : débat2007.fr non lu (Wayback hors service, puis 429 « Too Many Requests ») ; Slate (2011, reconstitution) en 403 ; aucun chiffrage par mesure de l'UMP ni d'un autre institut trouvé. Les mesures 2007 restent à un seul chiffreur.
- **Législatives 2024** : les mesures chiffrées par Montaigne, l'iFRAP ou l'IPP pour le NFP, le RN et Ensemble n'ont pas été votées sous cette forme. Exemple : le relèvement de l'abattement de succession à 150 000 € (Ensemble), vu dans les résultats de recherche. Je n'ai pas fait de recherche systématique de mesures votées ensuite.
- **Présidentielle 2022** : en dehors des lignes déjà présentes dans `calibration_instituts.csv`, aucune mesure nouvelle votée avec deux chiffrages n'a été cherchée en détail, faute de temps.
- **Autres fiches Montaigne 2012 non exploitées**, faute de réalisé cherché : ARS +25 % (−381 M€, réalisé non cherché), TVA à 5,5 % sur les livres (−115 M€), 60 000 postes dans l'Éducation nationale (−1 744 M€ ; iFRAP : 9 Md€ sur 5 ans), cotisations sur les contrats courts (+611 M€), régime des acomptes d'IS (+1 210 M€), taxe à 75 % (+200 M€, devenue une taxe payée par les entreprises : autre périmètre). Pistes pour une suite.

## 3. Sites inaccessibles

- jct.gov et cbo.gov : 403 (Cloudflare), avec WebFetch comme avec curl. JCX-18-22 a été lu sur une copie Wayback.
- zonebourse.com : 403 avec curl, lu avec WebFetch (non archivé).
- slate.fr : 403.
- Wayback Machine : « Temporarily Offline », puis 429 en cours de tâche.
- ccomptes.fr : le curl direct n'a rien enregistré ; copies déjà archivées par T18 et IS réutilisées.
- PWBM (page des estimations de 2025) : 404 avec WebFetch.

## 4. Décisions laissées à l'intégrateur

1. Garder ou non le cas américain (taux de 1 %, calendrier de paiement) dans la validation de la règle « Taxe sur les rachats d'actions ». Il formerait de toute façon un sous-échantillon étranger à part.
2. Statut du contrat de génération dans la calibration. La mesure votée diffère du programme (aide forfaitaire) et le réalisé porte sur 2014, en montée en charge. Le garder teste aussi le non-recours, que la règle de la médiane ne vise pas.
3. Faut-il exiger l'**indépendance** des chiffreurs avant d'appliquer la médiane ? En 2012, Terra Nova reprend le candidat, et Montaigne révise après Terra Nova.
4. Pour 2012, le « candidat » est lu dans Terra Nova ou dans Reuters, non archivé : confiance `medium` ou `low`.
