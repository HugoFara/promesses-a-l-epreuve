# T21 : tester les règles sans cas ou avec trop peu de cas (brouillon)

Fusion faite le 20/10/2026, à partir de `parts/` (non modifié). Règles et paramètres gelés au commit `686902b` : les sha256 de `data/raw/regles.csv` et `data/raw/moteur_regles.csv` à ce commit sont ceux de la consigne. Les valeurs gelées viennent de `git show 686902b:…`, pas de l'arbre de travail (modifié depuis par T20). Les facteurs centraux ont été recalculés avec `facteurs_centraux()` de `scripts/validation.py` dans sa version gelée.

Ce brouillon ne contient pas l'attribution à l'aveugle (phase 3). Les écarts « après la règle » utilisent la règle pressentie par les groupes de collecte. Ils sont donc provisoires.

## 1. Fichiers

| Fichier | Contenu |
|---|---|
| `mesures_cout_nouvelles.csv` | 14 cas de mesure (A : 7, B : 6, C : 1, D : 0). Colonnes de `recherche/T18/mesures_cout_nouvelles.csv`, plus `pays` |
| `ecarts_recalcules.csv` | Pour chaque cas : écart avant la règle, facteur central gelé, prévision et écart après la règle, effet (`ameliore`, `degrade`, `neutre`) |
| `instituts_nouveaux.csv` | 32 lignes (`parts/cout_C_instituts.csv`), aux colonnes de `data/raw/calibration_instituts.csv` |
| `parametres_testes.csv` | 26 tests de paramètre (A : 5, B : 8, C : 2, D : 11). Colonnes de `parametres_D.csv`, plus la fourchette gelée relue sur `686902b`, `valeur_trouvee`, `verdict_parametre`, `sens_vs_central` et `lecture_verdict` |
| `sources.csv` | 88 lignes : 84 fichiers archivés dans `sources/T21/<G>/`, tous au bon sha256 ; 4 pages canada.ca lues mais non archivées (`verif_sha256 = non_archive`) |
| `aveugle/mesures_officielles.csv` | 14 lignes, colonnes de `recherche/T18/aveugle/mesures_officielles.csv`, plus `pays` |
| `aveugle/regles_disponibles.csv` | Copie identique de `recherche/T18/aveugle/regles_disponibles.csv` (vérifiée avec `cmp`) |

Écart = (ex post central − ex ante) / ex ante. Écart après la règle = (ex post central − ex ante × facteur) / (ex ante × facteur).

## 2. Contrôles et anomalies

- **Identifiants** : tous uniques. Aucun doublon d'identifiant avec `data/raw/mesures_cout.csv` (version gelée et arbre), `data/raw/mesures_effets.csv`, T18 ni T20. Aucun doublon de fond trouvé non plus : la taxe française sur les rachats (`rachats_2025`) et la trajectoire carbone française (`carbone_convergence_2018`) ne sont pas reprises.
- **Champs obligatoires** : tous remplis, sauf une erreur de colonne dans le part B (ci-dessous).
- **Erreur de colonne, cas `p117_*`** : dans `parts/cout_B.csv`, la colonne `confiance` des 4 lignes contient une phrase (« Écart −6,2 %. Cause donnée par la Cour… »). La phrase a été reportée dans `note`. `confiance` a été mise à `medium`, car la LFI est lue dans la note d'exécution de la Cour et non dans la LFI elle-même (`note_confiance`). Drapeau `confiance_corrigee_fusion`. À valider par l'intégrateur.
- **Unités** :
  - 7 cas en milliards de dollars canadiens et 1 en milliards de dollars américains (drapeaux `monnaie:CAD`, `monnaie:USD`). Seul l'écart relatif compte ;
  - 2 cas SMIC en **milliers d'emplois perdus** (drapeau `unite_emplois`), pas en euros. Le facteur de la règle ne s'y applique pas (§ 3.2).
- **Proxy** : les 4 cas `p117_*` sont un proxy (drapeau `proxy_charge_dette`). Ils comparent la charge de la dette prévue en LFI à son exécution. Ils ne contiennent pas d'effet « spread × dette ».
- **Écarts recalculés** : identiques à ceux des notes des groupes (à l'arrondi près).
- **Instituts** : mêmes colonnes que `data/raw/calibration_instituts.csv`. Aucune ligne déjà présente : les campagnes 2007 et 2012 sont nouvelles. Les 19 écarts déclarés sont conformes à la convention du fichier existant, (réalisé − chiffrage) / |chiffrage|. Un point : les 3 lignes du contrat de génération ont `inclus_stats = « oui (horizon et dispositif différents : voir note) »`. `scripts/validation.py` lit tout ce qui commence par « oui » comme inclus. Elles seraient donc comptées.
- **Paramètres** : toutes les valeurs gelées déclarées par les groupes sont celles de `686902b`. Pour `spread_dette` et `taux_100pb`, absents de `moteur_parametres.csv`, la fourchette vient de `elasticites.csv`.
- **Fichier aveugle** : aucune valeur réalisée, cause, note ni citation de l'ex post. Pour 3 lignes, l'auteur du chiffrage a été raccourci, parce que le texte du part citait un document postérieur (ES : « cité par l'AIReF elle-même (juillet 2020) »).
- **Problème pour la phase 3** : la copie demandée de `regles_disponibles.csv` (T18) indique « (non applicable ici) » pour « Taux d'intérêt », « Effet emploi du SMIC » et « Médiane des estimations ». Elle ne contient pas du tout « Taxe sur les rachats d'actions ». Avec ce fichier, l'agent à l'aveugle ne peut pas attribuer la règle pressentie à 7 des 14 cas (SMIC, programme 117, rachats). Décision à prendre avant la phase 3 (§ 6).

## 3. Résultats par règle

### 3.1 Élasticité carburants (facteur central gelé 0,7305 ; ε −0,3, fourchette −0,4 à −0,21)

**Cas français** : aucun.

**Cas étrangers** : 7 cas `observe`, tous des taxes carbone nouvelles perçues sur une ligne propre. Ils viennent de deux dispositifs seulement : Colombie-Britannique (3 années d'un même budget) et redevance fédérale du Canada (4 lignes). Leur assiette est mixte (carburants et gaz de chauffage).

| id | Écart avant la règle | Écart après la règle | Effet |
|---|---|---|---|
| bc_carbon_tax_2008_09 | −9 % | +24 % | dégrade |
| bc_carbon_tax_2009_10 | −14 % | +18 % | dégrade |
| bc_carbon_tax_2010_11 | −16 % | +15 % | améliore |
| ca_fuel_charge_2019_20 | +2 % | +40 % | dégrade |
| ca_fuel_charge_ab_2019_20 | +13 % | +55 % | dégrade |
| ca_fuel_charge_2020_21 | −7 % | +27 % | dégrade |
| ca_fuel_charge_ab_2020_21 | −19 % | +11 % | améliore |

- Erreur médiane : 13 % avant la règle, 24 % après. La règle améliore 2 cas et en dégrade 5. Selon les définitions de `scripts/validation.py`, ce serait un statut « contredite », mais sur un sous-échantillon étranger.
- Avec un seul cas par dispositif (la 1re année) : 2 cas, tous deux dégradés (−9 % → +24 % ; +2 % → +40 %).
- Réserves : récession de 2008-2009 et COVID-19 non isolées ; assiette mixte ; Alberta 2019-20 révisé (0,2105 puis 0,2596), le sens de l'écart en dépend.

**Tests de paramètre** :
- Suède (Andersson), ex post, `medium` : −1,57 à la taxe carbone, **hors fourchette, plus fort**. Avec ε = −1,57, la formule gelée donnerait un facteur négatif (−0,41).
- Douenne (2020), non ex post, `medium` : −0,45, hors fourchette, plus fort (facteur 0,60).

Les deux signaux vont en sens contraire. Les recettes canadiennes sont proches des chiffrages, alors que la règle retire 27 %. La littérature suédoise trouve une réaction plus forte que le paramètre gelé.

### 3.2 Effet emploi du SMIC (facteur 1,674 ; eps_smic −0,6, fourchette −0,17 à −0,9)

**Cas français** : aucun. Aucune hausse du SMIC n'a un chiffrage budgétaire avant adoption suivi d'un réalisé budgétaire.

**Cas étrangers** : 2 cas en emplois, `reestimation` (évaluations économétriques), `inclus_stats = 0`. Le facteur ne s'y applique pas : le chiffrage contient déjà l'effet emploi.
- Espagne 2019 : 40 000 emplois perdus prévus, 49 500 estimés après coup (+24 %). Le signe dépend du millésime de l'AIReF retenu (2020, 2025 ou 2026).
- Allemagne 2015 : 910 717 prévus (chiffrage universitaire), environ 76 500 estimés (−92 %).

**Tests de paramètre** (5 sur eps_smic, dont 4 ex post sur des hausses du salaire minimum) :

| Estimation | Valeur | Confiance | Verdict |
|---|---|---|---|
| Allemagne 2022 (bunching) | −0,18 | medium | dans la fourchette (près de la borne basse) |
| Royaume-Uni, IFS | −0,17 | high | dans la fourchette (à la borne basse) |
| Royaume-Uni, LPC 2023 | +0,476 | high | hors fourchette, plus faible (signe opposé) |
| Espagne 2019, Banco de España | −0,3 à −0,5 | high | dans la fourchette |
| France, zéro charges 2009 | ≈ −1 | medium | hors fourchette, plus fort (baisse de coût, pas hausse du SMIC) |

Toutes les estimations sur des hausses sont plus faibles que le central (−0,6). Avec la formule gelée, le montant passerait de 1,67 Md€ (ε = −0,6) à 0,47 Md€ (ε = −0,17).

`cout_emploi_perdu` : ≈23 000 € dérivés par l'agent du Groupe d'experts 2025, contre 16 175 € gelés (hors fourchette, plus fort), mais confiance `low`.

### 3.3 Taux d'intérêt (facteur 1 ; spread_dette 3 pb, jusqu'à 6 ; taux_100pb 3,2 Md€ à 1 an)

**Cas français** : 4 cas `observe`, **proxy** (programme 117, LFI contre exécution) : −6,2 %, +6,0 %, −4,1 %, −6,1 %. Erreur médiane 6 %. Facteur 1, donc la règle ne change rien. Les écarts viennent des taux courts et de l'inflation (OATi), pas du spread.

**Cas étrangers** : aucun.

**Tests de paramètre** :
- `spread_dette` : ≈2 pb par point de dette (1,2 à 7,7 dans la littérature citée), Banco de España, économétrie sur les spreads observés de 2000 à 2023, `high`. **Hors fourchette, plus faible** (fourchette gelée 3 à 6).
- `taux_100pb` : 3,2 Md€ dans le PLF 2026, `medium`. Égal au gelé, mais c'est le même modèle de l'AFT, pas une observation. **Aucun test ex post trouvé.**

### 3.4 Taxe sur les rachats d'actions (facteur 0,126 ; part perdue 0,85)

**Cas français** : aucun nouveau (`rachats_2025` est déjà dans `data/raw/`).

**Cas étrangers** : 1 cas `observe`, la taxe américaine de 1 % : 7,875 Md$ prévus par le JCT pour l'exercice 2024, 4,539 encaissés (−42 %). Avec le facteur gelé, la prévision tomberait à 0,99 Md$, et l'écart deviendrait +357 %. Ce calcul est mécanique : le facteur est calibré pour un taux de 33 %, pas de 1 %. Une partie de l'écart peut venir du calendrier des premières déclarations.

**Tests de paramètre** :
- `part_perdue_rachats` : **non comparable**. Le ratio réalisé / prévu (0,58) mêle calendrier, assiette nette et réaction (`low`).
- `part_taxe_rachats_existante` : 0,059 contre 0,0238 gelé (recette constatée de 2025, Cour des comptes, `high`). **Hors fourchette, plus fort**. Mais le chiffre de 2025 inclut une taxe temporaire, ponctuelle.

### 3.5 Médiane des estimations (facteur 1)

Pas de cas de mesure au sens de T18. Le groupe C a ajouté 32 lignes de chiffrages de campagne (2012 : 11 mesures ; 2007 : 3), dans `instituts_nouveaux.csv`.

Seules 2 mesures incluses ont au moins deux chiffreurs et un réalisé :

| Mesure | Avec le candidat (3 chiffrages) | Instituts seuls |
|---|---|---|
| Tranche à 45 % | médiane 0,6 ; erreur 74 % (meilleur 16 %, pire 103 %) | médiane 0,5 ; erreur 45 % |
| Contrat de génération | médiane −2,527 ; erreur 2 945 % | médiane −6,5 ; erreur 7 784 % |

Erreur = |chiffrage − réalisé| / |réalisé|. La médiane ne fait jamais mieux que le meilleur chiffrage. Les chiffrages ne sont pas indépendants : Terra Nova reprend le candidat, et Montaigne révise ses fiches après Terra Nova. Le contrat de génération teste surtout le non-recours. Pour comparaison, `data/raw/calibration_instituts.csv` contient déjà 7 mesures (2017, 2022) avec au moins deux instituts et un réalisé. Mais ses réalisés ne sont pas classés par `type_ex_post`.

### 3.6 Élasticité électricité (facteur 0,9227 ; eps_elec −0,8, fourchette −0,2 à −0,8)

**Cas français et étrangers** : aucun.

**Tests de paramètre** :
- Suisse 2013-2023 (Swiss Economics), ex post, `high` : −0,15 à −0,34, central −0,25. Dans la fourchette, mais près de la borne basse.
- Finlande, crise de 2022 (Ahlvik et al., document de travail), `high` : −0,184. **Hors fourchette, plus faible.**
- Prix de gros en France : non comparable.

Avec ε = −0,25, le facteur passerait de 0,923 à 0,976. Aucune estimation française récente.

### 3.7 Réforme structurelle (facteur 0,842)

Aucun cas, aucun test de paramètre. Le COR écrit que ses projections « ne permettent pas l'évaluation des effets purs des réformes ». Les économies d'une réforme sont réestimées par le modèle de l'institution qui les a chiffrées, souvent pour des horizons pas encore atteints (2030, 2050). Les réformes de 2003, 2014, assurance chômage 2023 et carrières longues 2012 ont été cherchées sans réalisé (notes D, § 4).

### 3.8 Substitution retraites (facteur 0,8 ; part_substitution 0,2, fourchette 0,2 à 0,4)

Aucun cas de mesure nouveau. Trois tests de paramètre français, tous sur la réforme de 2010, comme la source gelée :
- COR 2017, `medium` : ≈0,15 sans le chômage. Hors fourchette, plus faible.
- IPP 2025, `high` : 0,079 pour l'ARE seule ; effet net ≈0 une fois les cotisations comptées. Hors fourchette, plus faible.
- DREES-DARES citées par la Cour, `medium` : ≈0,20. Dans la fourchette.

Ces estimations ne sont pas indépendantes des données de la source gelée.

### 3.9 Élasticité IS (facteur 0,94 ; s_is 0,008 pour la borne basse 0,73)

Aucun cas de mesure nouveau (la contribution de 10,7 % de 2014-2015 n'a pas de réalisé isolé ; la surtaxe 2026 pas encore de réalisé). Tests de paramètre :
- Vicard (2015), France, `high` : 0,005 (un seul canal). Plus faible.
- Beer, de Mooij et Liu, méta-analyse, `high` : 0,010 (≈0,015 récemment). Plus fort.

Ces tests ne portent que sur la borne basse. Avec s = 0,010 ou 0,015, la formule gelée 1 − s × (25,83 + 7,73) donnerait 0,66 ou 0,50 au lieu de 0,73. Le facteur central (0,94, surtaxe 2025) n'est pas en cause.

### 3.10 Élasticité revenus (facteur 0,9 ; eps_top 0,175, fourchette 0,15 à 0,2)

Aucun cas français. Deux tests, britanniques seulement (taux de 50 % de 2010) : HMRC 0,48 (`medium`) et IFS 0,31 à 0,95 (`high`). Tous deux **hors fourchette, plus forts**. Population plus large que le top 0,1 % et fort effet d'anticipation. Le cas britannique (2,5 Md£ annoncés, 1,1 Md£ estimés par HMRC, `reestimation`) est signalé par D, mais non intégré : la consigne n'admet pas de cas étranger pour cette règle.

### 3.11 Élasticité capital (facteur 0,437 ; eps_capital 0,77)

Aucun cas de mesure nouveau. Tests français :
- Bach et al. (2023), `high` : 4,2 pour la hausse de 2013, 2,1 pour la baisse de 2018, sur les dividendes des sociétés contrôlées. **Hors fourchette, plus fort.**
- Lefèbvre-Zanoutene (2022), `medium` : qualitatif, non comparable (sens : perte de recette en 2013).

Contradiction à lever : Bach et al. écrivent aussi (p. 26) que la hausse de 2013 « actually increased fiscal revenues ».

### 3.12 Élasticité succession (facteur 0,9 ; eps_succession 0,16, fourchette 0,08 à 0,34)

Aucun cas. Deux tests `medium`, lus dans des résumés seulement : France ≈0,25 en borne haute, Allemagne < 0,1. Tous deux dans la fourchette ; ils encadrent le central.

### 3.13 Non testables par construction

« Règle d'or » et « Déjà dans la référence » sont des conventions comptables, pas des prédictions. Elles n'ont pas été cherchées (consigne § 2).

## 4. Ce qui n'a pas été trouvé

Détail et endroits cherchés dans `parts/notes_[A-D].md`. En bref :

- **Carburants** : aucun chiffrage ex post de l'effet volume des hausses de la composante carbone de 2014-2018 ni du gel de 2019 ; Colombie (ex ante non trouvé) ; Irlande (oireachtas.ie inaccessible) ; Rivers et Schaufele (non lu).
- **Électricité** : aucun réalisé national pour la Stromsteuer allemande de 1999 ; aucune élasticité française publiée depuis 2015.
- **SMIC** : aucune évaluation ex post française d'une revalorisation ; pas d'ex ante pour la hausse allemande à 12 € ; pas d'effectif national pour le Royaume-Uni ; pas d'ex ante pour l'Espagne 2023-2024.
- **Taux d'intérêt** : aucune publication ne confronte la sensibilité annoncée (+100 pb → +3,2 Md€) à la charge constatée après 2022 ; pas de test ex post de `spread_dette` propre à la France ; LFI 2021-2022 du programme 117 contradictoires, NEB 2019, 2021 et 2022 introuvables.
- **Rachats** : pas de recette FY 2025 aux États-Unis (qui permettrait de trancher le calendrier) ; pas de réalisé au Canada ni en Inde ; aucune estimation causale nouvelle de la part perdue.
- **Médiane** : pas de second chiffreur par mesure en 2007 ; plusieurs réalisés de 2012 manquants (heures supplémentaires, abattement de succession, emplois d'avenir, carrières longues, TTF) ; 2022 et 2024 non explorés en détail.
- **Groupe D** : aucun réalisé isolé pour la contribution IS de 10,7 %, la taxe sur les hautes rémunérations, les prélèvements sociaux de 2011-2012 ni l'abattement de succession de 2012 ; aucune élasticité française du revenu imposable après 2012 ; 4e rapport de France Stratégie (2023) et NEB 2021 « recettes fiscales » non téléchargés.
- **Sites inaccessibles** : ccomptes.fr (coupures en cours de tâche), jct.gov, cbo.gov, obr.uk, oireachtas.ie, HAL (anti-robot), mindestlohn-kommission.de, canada.ca avec curl (d'où 4 pages non archivées).

## 5. Critère de réussite (§ 4 de la consigne)

Le critère : au moins 5 cas `observe`, ou un test de paramètre sur au moins une estimation ex post `high` ou `medium`, ou une explication écrite de l'impossibilité.

| Règle | Cas `observe` FR / étrangers | Meilleur test de paramètre ex post | Critère |
|---|---|---|---|
| Élasticité carburants | 0 / 7 (2 dispositifs) | Suède, `medium` | **atteint** (deux branches), sur des données étrangères seulement |
| Élasticité électricité | 0 / 0 | Suisse et Finlande, `high` | **atteint** (paramètre) |
| Effet emploi du SMIC | 0 / 0 (2 `reestimation` en emplois) | Royaume-Uni et Espagne, `high` | **atteint** (paramètre) |
| Taux d'intérêt | 4 (proxy) / 0 | `spread_dette`, `high` | **atteint** (paramètre) ; `taux_100pb` non testé ex post |
| Taxe sur les rachats d'actions | 0 / 1 | `part_taxe_rachats_existante`, `high` | **atteint au sens strict** par un paramètre secondaire ; **non atteint** pour la part perdue (0,85) |
| Médiane des estimations | 0 | aucun | **non atteint** : 2 mesures à plusieurs chiffreurs, non indépendants ; pas une impossibilité de principe |
| Réforme structurelle | 0 | aucun | **atteint par l'explication** de l'impossibilité (§ 3.7) |
| Substitution retraites | 0 | IPP 2025, `high` | **atteint** (paramètre) |
| Élasticité IS | 0 | Vicard, Beer et al., `high` | **atteint** (paramètre), pour la borne basse seulement |
| Élasticité revenus | 0 | IFS 2017, `high` | **atteint** (paramètre), données étrangères seulement |
| Élasticité capital | 0 | Bach et al., `high` | **atteint** (paramètre) |
| Élasticité succession | 0 | 2 résumés, `medium` | **atteint au sens strict** (texte intégral non lu) |
| Règle d'or, Déjà dans la référence | — | — | non testables par construction |

Aucune règle n'atteint 5 cas `observe` français.

## 6. Décisions laissées à l'intégrateur

1. **`eps_elec`** : central gelé −0,8 contre −0,15 à −0,34 pour les deux estimations ex post (Suisse, Finlande). Prendre la borne basse (−0,2) comme central à l'horizon 2027 ? Le facteur passerait d'environ 0,92 à environ 0,98. Les deux sources sont étrangères.
2. **`eps_smic`** : central gelé −0,6 contre des estimations ex post de hausses du salaire minimum entre +0,48 et −0,5, la plupart entre 0 et −0,2. Abaisser le central, ou garder −0,6 en disant qu'il vient d'élasticités au coût mesurées sur des baisses de cotisations ? Le montant passerait de 1,67 à 0,47 Md€ avec −0,17.
3. **`spread_dette`** : ≈2 pb par point de dette (Banco de España, 2000-2023) contre ≈3 pb gelés, et 6 en haut de fourchette. Abaisser ou élargir la fourchette ?
4. **Élasticité capital** : les estimations françaises ex post (2 à 4) sont bien plus fortes que 0,77, sur un champ plus étroit. Vérifier la phrase p. 26 de Bach et al. avant tout usage.
5. **Borne basse du facteur IS** : avec la méta-analyse récente (1 à 1,5 %/pt), la borne basse serait 0,50 à 0,66 au lieu de 0,73. Le central n'est pas en cause.
6. **Cas SMIC en emplois** : les garder pour tester « Effet emploi du SMIC » (le montant est proportionnel aux emplois), ou les reverser au format `mesures_effets.csv` ? Pour l'Espagne, choisir le millésime de l'AIReF.
7. **Proxy programme 117** : garder les 4 cas comme test « facteur 1 » d'une charge d'intérêts, ou les exclure faute de lien avec le spread ? Valider aussi la confiance `medium` mise à la fusion.
8. **Cas Médiane** : intégrer les campagnes 2007 et 2012 dans la calibration ? Exiger l'indépendance des chiffreurs avant d'appliquer la médiane ? Compter le candidat parmi les chiffrages ? Garder le contrat de génération (`inclus_stats` commençant par « oui », donc compté par le script) ?
9. **Carburants** : rattacher les taxes carbone canadiennes (assiette mixte) à la règle, ou les garder à part ? Un cas par dispositif ou un par année ? Alberta 2019-20 : valeur révisée ou première ?
10. **Rachats** : garder le cas américain (taux de 1 %, calendrier incertain) dans un sous-échantillon étranger, ou l'écarter ?
11. **Estimations étrangères pour des paramètres français** (revenus : Royaume-Uni ; électricité : Suisse, Finlande) : les admettre comme tests ?
12. **Substitution retraites** : les trois sources portent sur la réforme de 2010, comme la source gelée. L'IPP suggère un effet net quasi nul sur l'assurance chômage.
13. **Succession** : garder `medium` pour des résumés, ou passer à `low` ?
14. **Fichier des règles pour la phase 3** : la copie de T18 marque « Taux d'intérêt », « Effet emploi du SMIC » et « Médiane » « (non applicable ici) », et n'a pas de ligne « Taxe sur les rachats d'actions ». Il faut décider avant l'attribution à l'aveugle s'il faut une version adaptée à T21. Sinon, 7 cas sur 14 ne pourront pas recevoir leur règle pressentie.

## 7. Attribution à l'aveugle

Faite le 20/10/2026 par un agent neuf, sans web, sur une copie de `aveugle/` placée hors du dépôt. Sortie : `attribution_agent.csv`, conservé tel quel.

**Ajout au matériel aveugle avant l'attribution** : la liste copiée de T18 marquait « (non applicable ici) » Taux d'intérêt, Effet emploi du SMIC et Médiane des estimations, et n'avait pas de ligne « Taxe sur les rachats d'actions ». 7 cas sur 14 n'auraient pas pu recevoir leur règle. Leur champ a été décrit dans `aveugle/regles_disponibles.csv`, sans toucher aux règles gelées (même démarche que T18 pour « Élasticité électricité »).

- **Règle attribuée = règle pressentie dans les 14 cas** : Élasticité carburants (7 cas canadiens), Effet emploi du SMIC (Espagne, Allemagne), Taux d'intérêt (4 cas du programme 117), Taxe sur les rachats d'actions (États-Unis).
- **Hésitation** : pour les taxes carbone canadiennes, l'agent a hésité avec « Nouvelle assiette : risque juridique » (instrument nouveau). Il a retenu « Élasticité carburants ».
- **`issue_connue` = `oui` pour 7 cas sur 14** : les 3 années de la Colombie-Britannique, l'Espagne, l'Allemagne, et le programme 117 en 2020 et 2023 (souvenirs approximatifs, selon l'agent). Les 4 années de la redevance fédérale canadienne, le programme 117 en 2024 et 2025 et la taxe américaine : `non`. Parmi les cas carburants, seuls les 4 cas fédéraux forment donc un sous-échantillon aveugle.

## 8. Intégration et correction des paramètres (20/10/2026)

Décision de l'utilisateur le 20/10/2026 : intégrer T21 et corriger les paramètres remis en cause.

**Données intégrées** (`data/raw/`, journal dans `historique.csv`) :

- `mesures_cout.csv` : 12 lignes et une colonne `pays` (vide = France). Les 7 taxes carbone canadiennes et la taxe américaine sur les rachats ont `selection` = `test_regles`. `scripts/validation.py` les classe à part (« étranger ») : elles ne comptent ni dans les statistiques françaises ni dans le statut des règles, et leur résultat est écrit à côté, dans la note de la règle. Les 4 lignes du programme 117 sont hors statistique (proxy). Les 2 cas SMIC, exprimés en emplois, restent ici comme tests de paramètre.
- Écarts : `validation.py` rapporte l'erreur au chiffrage de départ, comme pour toutes les mesures ; `ecarts_recalcules.csv` la rapportait à la prévision corrigée. Carburants, cas étrangers : 3 améliorés, 4 dégradés, erreur médiane 13 % → 18 %. Rachats : 42 % → 45 %.
- `validation_attribution.csv` : `attribution_agent.csv` tel quel. `elasticites.csv` : les 26 estimations de `parametres_testes.csv` (verdict dans `note_num`). `calibration_instituts.csv` : les 32 chiffrages de 2007 et 2012, hors statistique (test de la médiane non jugeable).
- Confiance des 4 lignes du programme 117 : `medium`, comme l'a proposé la fusion. Les 3 lignes « contrat de génération » sont hors statistique, comme toutes les lignes de `instituts_nouveaux.csv`.

**Règle de correction**, la même pour chaque paramètre : central = médiane des estimations « high » qui mesurent la même grandeur (source gelée comprise) ; bornes = plus basse et plus haute de ces estimations. Une estimation d'une autre grandeur ne compte pas. Cette règle diffère de celle de la répercussion dans les prix (T20, estimation française d'abord) : la répercussion dépend des institutions du marché national (tarifs réglementés), une élasticité de comportement se transpose mieux.

| Paramètre | Avant | Après | Estimations « high » de la même grandeur |
|---|---|---|---|
| `eps_elec` | −0,8 (−0,2 à −0,8) | −0,25 (−0,15 à −0,8) | Insee −0,8 ; Suisse −0,25 ; Finlande −0,18 |
| `eps_smic` | −0,6 (−0,17 à −0,9) | −0,17 (0 à −0,9) | experts / Bozio-Wasmer −0,6 ; Dube −0,17 ; IFS −0,17 ; Low Pay Commission +0,48 ; Banque d'Espagne −0,4 ; borne basse plafonnée à 0 |
| spread par point de dette | ≈3 pb | ≈2,5 pb | Pamies et al. 3 ; Banque d'Espagne 2 (1,2 à 7,7) |

Conséquences (`recherche/T21/corrections_parametres.csv`, `corrections_smic.csv`) : lignes `nfp_taux` −3,5 → −2,9, `ens_taux` −0,5 → −0,4, `rn24_taux` −1,4 → −1,2 ; effet emploi du SMIC 1,67 → 0,47 Md€ (≈29 300 emplois au lieu de 103 500). Soldes centraux : NFP 2024 −160,0 → −159,4 ; Ensemble 2024 −25,5 → −25,6 ; RN 2024 inchangé (−60,3) ; panier LFI intégral −72,0 → −70,8 ; panier Ensemble −7,0 → −7,2. Le seul cas d'électricité du backtest reste amélioré, moins nettement (erreur 12 % → 10 %, contre 5 % avant).

**Paramètres remis en cause mais inchangés après vérification** :

- `eps_capital` (0,77) : Bach et al. (2,1 à 4,2) ne portent que sur les dividendes des sociétés contrôlées par leurs dirigeants, la part la plus mobile ; 0,77 porte sur l'ensemble des revenus du capital. Ce n'est pas la même grandeur. La phrase de leur p. 26 (« the tax hike actually increased fiscal revenues ») contredit la phrase précédente et la conclusion de la même section (« the 2013 reform has actually decreased tax revenues ») : coquille probable.
- `s_is` (0,8 %/pt) et borne basse de `facteur_is` (0,73) : médiane de 0,8 (gelé), 0,5 (Vicard) et 1,0 (Beer et al.) = 0,8. Inchangés.
- `part_substitution` (0,2) : l'IPP (0,08) ne mesure que l'assurance chômage, le COR (0,15, `medium`) le reste ; leur somme (≈0,23) est cohérente avec 0,2.
- Non modifiés faute d'estimation « high » de la même grandeur : `eps_carbu` (Suède et Douenne, `medium`), `part_perdue_rachats`, `cout_emploi_perdu` (`low`). `part_taxe_rachats_existante` : 0,059 constaté en 2025, mais avec une taxe temporaire ; à revoir quand le rendement 2026 sera publié.
