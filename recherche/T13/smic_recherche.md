# T13 – SMIC à 1 600 € net : effectif concerné et élasticité de l'emploi

Date de consultation : 2026-10-14. Sources archivées dans `sources/T13/` et indexées dans `recherche/T13/sources.csv` (avec leur sha256).
Les pages données sont celles **imprimées** sur le document ; entre parenthèses, la page du fichier PDF quand elle diffère.

Niveaux de confiance : `high` = lu dans la source primaire ; `medium` = lu dans une source secondaire qui cite la primaire ; `low` = lecture d'un graphique, interpolation ou calcul de l'agent.

---

## 1. Tableau des sources lues

### 1.a Effectifs au voisinage du SMIC

| # | Source (fichier) | Chiffre | Citation exacte | Page | Champ | Conf. |
|---|---|---|---|---|---|---|
| E1 | Groupe d'experts Smic, rapport nov. 2025 (`groupe_experts_smic_2025.pdf`) | **2,2 millions**, soit **12,4 %** des salariés | « Au 1er novembre 2024, 2,2 millions de salariés des entreprises du secteur privé hors agriculture ont été directement concernés par la revalorisation du Smic horaire anticipée sur celle du 1er janvier 2025 […], soit 12,4 % des salariés sur ce champ, en baisse de 2,2 points par rapport au 1er janvier 2024 » | 51 (pdf 55) | Acemo. Note 14 : « l'ensemble des salariés sauf apprentis, stagiaires, intérimaires […] sauf agriculture, administration, particuliers employeurs, activités extraterritoriales, en France (hors Mayotte) ». Effectifs en personnes (temps complet et temps partiel) | high |
| E1b | idem | Mise en garde | « ce pourcentage ne doit pas être lu comme le pourcentage des salariés effectivement rémunérés au niveau du Smic » | 51 (pdf 55) | idem | high |
| E2 | Dares, « Combien de salariés sont rémunérés au Smic ? », 29 oct. 2025 (`dares_combien_salaries_smic_wayback.html`, copie Wayback) | 2,2 M ; 12,4 % | « 2,2 millions de salariés du secteur privé non agricole ont bénéficié directement de la revalorisation du 1er novembre 2024, soit 12,4 % des salariés » | section « mesure via les enquêtes Acemo » | Acemo, idem E1 | high (copie d'archive du texte Dares) |
| E3 | Groupe d'experts Smic, rapport nov. 2024 (`groupe_experts_smic_2024.pdf`) | 2,7 M au 1er janv. 2024 | « Au 1er janvier 2024, 2,7 millions de salariés des entreprises du secteur privé hors agriculture… » | 58 | Acemo | high |
| E4 | Institut Montaigne (fiche, `montaigne_smic1600_wayback20240710.html`) | 3,1 M au 1er janv. 2023 (17,3 %) | « bénéficiaires du Smic, qui s'établit au 1er janvier 2023 à 3,1 M selon la Dares, soit 17,3 % des salariés, contre 14,5 % un an plus tôt » | « Analyse synthétique » | Acemo (cité) | medium |
| E5 | Rapport 2025 (Encadré I.2) et Dares 2025 | **5,4 %** des salariés en EQTP, « un peu moins d'**un million** » sous **1,05 Smic** (rémunération horaire globale, primes comprises) | « selon les données de la Base tous salariés de l'Insee, en 2023, 5,4 % des salariés (en équivalent temps plein - EQTP) du privé environ, soit un peu moins d'un million de personnes (en EQTP), perçoivent un salaire brut horaire « global » inférieur à 1,05 Smic » | 55 (pdf 59) | BTS 2023. Graph. I.15 : « salariés du privé, y compris bénéficiaires de contrats aidés et de contrats de professionnalisation ; hors apprentis, stagiaires, salariés agricoles et salariés des particuliers employeurs » | high |
| E6 | Rapport 2025, graphique I.15 | **18,0 %** entre 1,2 et 1,4 Smic (texte) ; **≈ 12,9 %** entre 1,05 et 1,2 Smic (**lu sur le graphique**, ± 0,2 pt) | « en 2023, 18,0 % des salariés (en EQTP) perçoivent un salaire brut horaire compris entre 1,2 et moins de 1,4 Smic brut horaire » | 56 (pdf 60) | BTS 2023, EQTP | high (18,0) / low (12,9) |
| E7 | Rapport 2025 (Ecmoss 2022) | 14,5 % ont un salaire **de base** < 1,05 Smic ; parmi eux 40,2 % restent < 1,05 Smic en rémunération totale | « 14,5 % des salariés sont rémunérés avec un salaire de base inférieur à 1,05 Smic » ; « 40,2 % des salariés dont le salaire de base est inférieur à 1,05 Smic ont une rémunération totale qui demeure inférieure à 1,05 Smic » | 55-56 (pdf 59-60) | Ecmoss, entreprises de 10 salariés ou plus | high |
| E8 | Fondation iFRAP, 12 juil. 2024 (`ifrap_smic1600_wayback.html`) | 1,00-1,09 Smic : **10,0 %** ; 1,10-1,29 Smic : **17,2 %** des ETP ; total **18 490 144** ETP | tableau « Répartitions des salariés ETP par tranches de salaires dans les branches marchandes » : « 1,00-1,09 Smic 10,0% … 1,10- 1,29 Smic 17,2% » ; « Total 18 490 144 » | tableaux de la note | branches marchandes ; « une estimation de la distribution actuelle » (source de la distribution non précisée) | low |
| E9 | Bozio-Wasmer, rapport final oct. 2024 (`bozio_wasmer_2024_rapport_final.pdf`) | −0,65 % = 25 110 ETP entre 1 et 1,2 Smic ⇒ base implicite ≈ **3,86 M ETP** entre 1 et 1,2 Smic (calcul de l'agent) | « le modèle donne une diminution de l'emploi entre 1 et 1,2 Smic de 0,65 %, soit 25 110 ETP » | 198 | BTS postes (millésime non relevé) | high (citation) / low (base dérivée) |
| E10 | Rapport 2025 | La France est à **62,5 %** du salaire médian | « le salaire minimum dépasse à la fois 60 % du salaire médian (se situant à 62,5 %) » | 5 (pdf 9) | | high |

### 1.b Élasticités

| # | Source | Chiffre | Citation exacte | Page | Nature de l'élasticité | Conf. |
|---|---|---|---|---|---|---|
| L1 | Dube (2019), rapport pour HM Treasury (`dube2019_review_minimum_wages.pdf`) | **−0,17** | « Pooling across 36 estimates from the U.S. (regardless of the group under study), the median estimate is -0.17 » | 27 (pdf 31) | **Own-wage elasticity (OWE)**, médiane de 36 études américaines | high |
| L2 | idem | **−0,19** | « For this set of 26 estimates from the U.S., the median OWE is -0.19 » (26 études sur sous-groupes étroits : adolescents, restauration, commerce…) | 28 (pdf 32) | OWE, médiane | high |
| L3 | idem | Définition | « “own-wage employment elasticity” (OWE), which tells us how employment for the specific group responds to an increase in the average wage of that group induced by the minimum wage change » ; OWE = MWE / AWE | 26 | OWE = variation de l'emploi **du groupe** / variation **du salaire moyen du groupe** | high |
| L4 | idem | Échelle | « we can roughly think of an OWE less negative than -0.4 as small in magnitude, between -0.4 and -0.8 as medium, and more negative than -0.8 as large » | 27 (pdf 31) | | high |
| L5 | idem | Domaine de validité | « the best evidence suggests that the employment effects are small up to around 59% of the median wage » (jusqu'à 81 % du médian dans les comtés à bas salaires) | 3 (pdf 7) | | high |
| L6 | Rapport Smic 2024 (résumant Dube et Zipperer 2024, NBER w32925) | **−0,13** | « Pour les 88 études retenues, les résultats indiquent que l'élasticité médiane propre du salaire est de -0,13 » | 175 | OWE, méta-analyse | medium (primaire NBER non lue) |
| L7 | Kramarz et Philippon (version de travail de JPubE 2001, `kramarz_philippon_2000_rm0006.pdf`) | **−1,5** | « a one percent increase in the minimum wage cost induces a 1.5 percent increase in the probability that a minimum wage worker becomes non-employed » ; « the overall impact on the whole labor market is small since this group represents 3 to 4% of the workforce » ; en baisse de coût (1995) : « not significantly different from zero » | 23-24 et 27 | Élasticité de la **probabilité de perte d'emploi** des seuls salariés « rattrapés » (payés entre l'ancien et le nouveau coût minimum). Effet **asymétrique** (hausse de coût seulement) | high |
| L8 | Bozio-Wasmer (2024) | [−1,5 ; −1,0] | « Les élasticités de la demande de travail au coût du travail incluant les effets d'échelle se trouvent en général dans l'intervalle [-1,5 ; -1,0]. Une étude de référence pour la France est celle de Kramarz et Philippon (2001) » | 84 | Demande de travail (revue de littérature) | high |
| L9 | Bozio-Wasmer (2024) | **−0,9 à −0,2** (années 2000) ; **−0,6** retenu ; **−0,4 à −0,5** (plus de 25 ans) ; **−0,8 à −1,5** (moins de 25 ans) | « l'élasticité retenue variait ainsi entre -0,9 et -0,2 » ; « une élasticité maximale de -0,6 au niveau du Smic (à mi-chemin entre -0,3 et -0,9) est plus plausible que les élasticités des années 2000 » ; « une élasticité au niveau du Smic de l'ordre de -0,4 à -0,5 pour les plus de 25 ans, et entre -0,8 et -1,5 pour les jeunes de moins de 25 ans » | 175-176 | Élasticité de long terme de l'emploi au coût du travail, maximale au Smic, décroissante jusqu'à 2 Smic | high |
| L10 | Rapport Smic 2025 | **−0,6 à −0,9**, central **−0,8** | « Dans ce qui suit nous retenons des élasticités comprises entre -0,6 et -0,9, de manière cohérente avec le rapport Bozio-Wasmer (2024) et le rapport du Groupe d'experts (2024) » ; « une élasticité décroissante de la demande de travail, partant de -0,8 au niveau du Smic, puis décroissante linéairement pour atteindre -0,1 au niveau de deux fois le Smic » | 146 (pdf 150), 148 (pdf 152) | Demande de travail au coût (modèle d'équilibre partiel, offre +0,6 au Smic) | high |
| L11 | Rapport Smic 2025 | Cahuc, Carcillo, Le Barbanchon (2019) : −4 (embauches) ≈ −1 (emploi) | « une élasticité de l'embauche au coût du travail élevée pour les bas salaires, de −4 […] cohérente avec une élasticité de l'emploi de -1 » | 145 | | medium |
| L12 | Rapport Smic 2024, contribution FO (citant l'OFCE 2024) | OFCE : +12,4 % ⇒ **−10,4 %** de l'emploi au Smic (**322 000**), élasticité « 0,8 » ; net **−29 000** | « une augmentation de 12,4% du salaire minimum risquait de baisser l'emploi au niveau du SMIC de 10,4% (322 000 emplois) ce qui correspond à une élasticité élevée de 0,8 […] l'OFCE estime qu'une hausse de 12,4% du SMIC ne détruirait plus que 29 000 emplois » | contribution FO, p. 4 (pdf 230) | Brut puis net (demande, allègements) | medium (étude OFCE non lue) |
| L13 | iFRAP (2024) | **−0,5** ; brut −374 181, net −236 523 | « Elasticité moyenne de la demande de travail à son coût de -0,5 » ; tableau : « Total 18 490 144 +137 658 -374 181 -236 523 » | note | Demande moyenne, toutes branches marchandes | high (source de l'institut) |

### 1.c Méthode de l'Institut Montaigne (230 000 à 380 000)

Lu sur la copie Wayback du 10 juillet 2024 (le site actuel répond 403), section « Analyse détaillée » :
- **Laroque et Salanié (2000)** : « une hausse de 10 % serait susceptible de détruire 290 000 emplois » ; transposé à +14,4 % et actualisé avec l'emploi salarié : « les pertes d'emploi pourraient se chiffrer autour de 360 000 ».
- **Kramarz et Philippon (2001)**, élasticité « estimée à -1,5 » : « les destructions d'emplois pourraient cette fois se chiffrer à 600 000, soit une perte de 21 % de l'emploi concentré au niveau du Smic ». Montaigne range ce cas parmi les estimations « à prendre avec prudence ». Base implicite (calcul de l'agent) : 600 000 / (1,5 × 14,39 %) ≈ 2,8 M ; c'est proche des 3,1 M de bénéficiaires 2023 que la fiche cite.
- **Heyer et Plane (OFCE 2012)** : « une hausse du Smic de 1 % conduirait à la destruction de 14 500 emplois […] et la création de 12 200 » ; brut ajusté de +10 % d'emploi : « 223 300 ».
- Synthèse : « une hausse du Smic de 14,4 % pourrait causer des pertes d'emploi entre 230 000 et 380 000, 300 000 emplois apparaissant comme une estimation centrale, dont au moins 200 000 lors de la première année ».
- **Montaigne ne retient donc pas une élasticité unique.** Sa fourchette agrège des modèles structurels anciens qu'il actualise. L'élasticité implicite de son point central, rapportée à 3,1 M de salariés, vaut 300 000 / (0,144 × 3,1 M) ≈ −0,67 (calcul de l'agent).

---

## 2. Constats

1. **Le 2,2 millions est vérifié** (E1, E2). Il compte les bénéficiaires de la revalorisation anticipée du **1er novembre 2024**, et non du 1er janvier : la revalorisation de janvier 2025 a été avancée en novembre. Le champ est le secteur privé non agricole, hors apprentis, stagiaires et intérimaires, en effectifs physiques (temps partiels compris). Le champ total implicite est de 2,2 / 0,124 ≈ **17,7 M** salariés (calcul). Ce chiffre ne mesure pas les salariés « au SMIC » en rémunération totale (E1b, E7). **Aucune publication Dares de l'enquête Acemo 2026 (revalorisation du 1er janvier 2026) n'a été trouvée.**
2. **Aucune source lue ne publie directement l'effectif « entre 1 et 1,15 SMIC »**, ni les tranches 1-1,1 / 1-1,2 / 1-1,3 en effectifs. Ce qui est publié :
   - BTS 2023 (Dares/Insee, EQTP, rémunération globale) : < 1,05 Smic = 5,4 % (≈ 1 M) ; 1,05-1,2 ≈ 12,9 % (lu sur le graphique) ; 1,2-1,4 = 18,0 %. Le champ total implicite vaut 1 M / 0,054 ≈ 18 M EQTP.
   - **Estimation 1-1,15 Smic** (interpolation linéaire dans la tranche 1,05-1,2) : 5,4 + 12,9 × 0,10/0,15 ≈ **14,0 % ≈ 2,5 M EQTP** (calcul de l'agent, `low`). La tranche < 1,05 inclut des EQTP sous le Smic.
   - iFRAP : 10,0 % + 17,2 % × 0,05/0,20 ≈ 14,3 % de 18,49 M ≈ **2,6 M ETP** (calcul, `low`).
   - Bozio-Wasmer : ≈ 3,86 M ETP entre 1 et 1,2 Smic, soit ≈ **2,95 M** ramenés à 1,15 avec le ratio BTS 14,0/18,3 (calcul, `low`).
   - Écart de définition : l'enquête Acemo raisonne sur l'**assiette de vérification** du Smic, ce qui donne beaucoup de salariés « au Smic » (2,2 M). La BTS raisonne sur la **rémunération totale** (primes comprises), ce qui en donne moins (≈ 1 M sous 1,05). L'effectif « 1-1,15 Smic » dépend fortement de cette définition.
3. **Dube −0,17 est bien une élasticité « own-wage »** (L1, L3), et non une élasticité de l'emploi au salaire minimum. Elle rapporte la variation de l'emploi **du groupe étudié** à la variation **du salaire moyen de ce groupe**. Conséquences :
   - le multiplicande correct est la hausse du salaire moyen du groupe concerné, et non mécaniquement +14,4 %. Pour la tranche 1-1,15 Smic, la hausse mécanique moyenne vaut ≈ **6,9 %** sans diffusion (calcul de l'agent sur la distribution BTS : point milieu 1,025 → +11,6 %, point milieu 1,10 → +4,0 %, pondérés 5,4/8,6) ;
   - −0,17 et −0,19 sont deux **médianes** (36 études américaines tous groupes ; 26 études sur sous-groupes étroits). Ce n'est **pas un intervalle de confiance**. L'intervalle actuel du moteur (−0,19 à −0,17) n'a donc pas de sens statistique ;
   - Dube valide de faibles effets « up to around 59% of the median wage » (L5). La France est à 62,5 % (E10) ; +14,4 % la porterait à ≈ 71 % (calcul : 62,5 × 1,144), hors du domaine principal des études qu'il recense.
4. **Les élasticités françaises sont d'une autre nature et plus élevées.** Ce sont des élasticités de long terme de la demande de travail au coût, au niveau du Smic : −0,6 à −0,9 (groupe d'experts 2024-2025, central −0,8) ; −0,6 (Bozio-Wasmer, qui les juge « plus plausible[s] que les élasticités des années 2000 », −0,9) ; −0,4/−0,5 pour les adultes et −0,8/−1,5 pour les jeunes. Kramarz-Philippon (−1,5) mesure la probabilité de sortie d'emploi des seuls salariés rattrapés (3 à 4 % de la main-d'œuvre), lors de hausses de coût. L'appliquer au stock d'emplois au Smic comme le fait Montaigne est une extrapolation. Quand le salaire est fixé par la loi (Smic contraignant), c'est l'élasticité de **demande** qui s'applique, sans l'amortissement par l'offre du modèle du groupe d'experts.
5. **Le coût du travail ne suit pas le Smic net.** Les allègements sont exprimés en multiples du Smic : au niveau du Smic, le coût monte à peu près comme le salaire, mais il **baisse** pour les salariés au-dessus, qui redescendent dans la zone d'exonération. Montaigne : « le coût augmente pour les salariés rémunérés au niveau du Smic tandis qu'il diminue pour les salariés rémunérés au-dessus du Smic ». Ce mécanisme, et l'effet de demande, expliquent l'écart entre les chiffrages bruts et nets : OFCE −322 000 brut et −29 000 net (secondaire) ; iFRAP −374 000 brut et −237 000 net.

---

## 3. Proposition chiffrée (calculs de l'agent)

Formule du moteur : emplois perdus = |ε| × h × N, avec h = 14,4 % (14,39 % exact). Pour que les trois grandeurs restent cohérentes :
- ε est une élasticité **de l'emploi des salariés concernés à leur propre coût / salaire** ;
- N est l'effectif de la tranche directement touchée (1-1,15 Smic), comme le demande l'audit ;
- appliquer h = 14,4 % à toute la tranche surestime la hausse pour les salariés entre 1,05 et 1,15 Smic (≈ +4 %). Cela revient à supposer une diffusion complète, comme le font Montaigne et l'iFRAP. En contrepartie, la BTS (rémunération totale) sous-estime la concentration au Smic au sens de l'assiette (2,2 M selon Acemo contre ≈ 1 M sous 1,05 Smic selon la BTS). Les deux biais vont en sens contraire ; le scénario bas les traite explicitement.

| | Effectif N | Justification N | Élasticité ε | Justification ε | Emplois perdus (h = 14,4 %) | (h = 14,39 %) |
|---|---|---|---|---|---|---|
| **Bas** | 2,2 M | Bénéficiaires Acemo de la revalorisation (E1) : salariés effectivement « rattrapés » | −0,17 | OWE médiane de Dube (L1) ; Dube-Zipperer −0,13 (L6) serait encore plus bas | **53 856** | 53 819 |
| **Central** | 2,5 M | Tranche 1-1,15 Smic, BTS 2023 interpolée (≈ 14,0 % de ≈ 18 M EQTP) ; recoupée par l'iFRAP (≈ 2,6 M) | −0,6 | Borne prudente commune à Bozio-Wasmer (L9) et au groupe d'experts 2024-2025 (L10) ; classe « medium » chez Dube (L4) ; justifiée par un Smic au-dessus du domaine de Dube (62,5 % → ≈ 71 % du médian) | **216 000** | 215 850 |
| **Haut** | 3,0 M | 1-1,2 Smic de Bozio-Wasmer ramené à 1,15 (≈ 2,95 M) ; ordre de grandeur des 3,1 M de bénéficiaires Acemo de janvier 2023 utilisés par Montaigne | −0,9 | Haut de la fourchette du groupe d'experts (L10) ; élasticités des années 2000 (L9) | **388 800** | 388 530 |

Variantes utiles (h = 14,39 %) :
- ε = −0,8 (central du groupe d'experts), N = 2,5 M : **287 800**, proche du point central de Montaigne (300 000).
- ε = −0,4 (adultes, Bozio-Wasmer), N = 2,5 M : **143 900**.
- Dube appliqué de façon cohérente (OWE × hausse moyenne du groupe ≈ 6,9 % × 2,5 M) : **≈ 29 300**. C'est le vrai bas si l'on retient la lecture « own-wage » stricte.
- Test de résistance Kramarz-Philippon : −1,5 × 14,39 % × 3,0 M ≈ **647 600** (Montaigne : 600 000).

Lecture : avec un effectif de 1-1,15 Smic et des élasticités françaises (−0,6 à −0,9), le moteur retombe dans la fourchette de Montaigne (230 000-380 000). La valeur actuelle (53 856) ne tient qu'avec l'élasticité « own-wage » américaine, et cette élasticité exigerait de surcroît une hausse salariale moyenne plus faible que 14,4 %. Tous ces chiffres sont des **destructions brutes**, avant effet de demande et avant la baisse du coût du travail au-dessus du Smic par les allègements (cf. OFCE net −29 000).

Recommandation pour le moteur :
- remplacer l'intervalle (−0,19 ; −0,17) par **(−0,17 ; −0,6 ; −0,9)** et `smic_effectif` par **(2,2 ; 2,5 ; 3,0) M** ;
- propager les deux paramètres ensemble, pas en croisé, puisque chaque triplet est construit pour être cohérent. Une propagation croisée bas × haut donnerait un intervalle de 53 856 à 388 800 de toute façon.
- documenter que le « bas » correspond à la littérature américaine (OWE) et le « central/haut » aux évaluations françaises des allègements.

---

## 4. Limites

- Aucun effectif 1-1,15 Smic n'est publié : le 2,5 M repose sur une **lecture graphique** (12,9 %) et une interpolation linéaire. Le total EQTP (≈ 18 M) est déduit de « 5,4 % … un peu moins d'un million ».
- Les effectifs mélangent personnes (Acemo) et EQTP/ETP (BTS, iFRAP, Bozio-Wasmer). Pour des emplois perdus en têtes, un N en personnes serait plus grand (les temps partiels sont surreprésentés au Smic).
- La hausse de 14,39 % se rapporte au Smic net de 2024 (1 398,70 €). Le Smic a été revalorisé de 2,0 % au 1er novembre 2024 (E1, encadré I.2, lu). Une hausse au 1er janvier 2026 (+1,18 %) et une autre en juin 2026 (+2,41 %) n'ont été **vues que dans des extraits de recherche, sans être lues**. Sur une base 2026, l'écart à 1 600 € serait plus faible.
- Les élasticités françaises viennent d'évaluations de **baisses** de coût (allègements). Kramarz-Philippon trouvent une asymétrie (effet des baisses non significatif), ce qui plaide plutôt pour des effets plus forts en hausse. Les études Dube portent sur des hausses de salaire minimum, mais dans d'autres pays et pour des niveaux de Smic plus bas.
- L'élasticité « 0,8 » attribuée à l'OFCE et ses chiffres (322 000 / 29 000) n'ont été lus que dans la contribution FO au rapport 2024 : l'étude OFCE n'a pas été lue.

## 5. Ce qui n'a pas pu être lu

- **Site de la Dares** (`dares.travail-emploi.gouv.fr`) : réponse « Request Rejected » à curl. La page « Combien de salariés sont rémunérés au Smic ? » a été lue sur sa copie Wayback. Le Dares Résultats n° 52 (« La revalorisation du Smic au 1er novembre 2024 ») n'a pas été lu en PDF : ses chiffres clés sont repris dans le rapport 2025 (E1). Une éventuelle publication Acemo 2026 n'a pas été trouvée.
- **Institut Montaigne et iFRAP** : 403 sur les sites actuels (WebFetch et curl). Lus sur Wayback.
- **Insee** : non sollicité directement ; la distribution BTS a été lue via le rapport 2025 et la page Dares.
- **Étude OFCE 2024** (Smic à 1 600 €) et **NBER w32925** (Dube-Zipperer 2024) : non lus ; seulement cités par des sources secondaires (L6, L12).
- **Abowd, Kramarz, Margolis, Philippon** (« Minimum wages and employment in France and the United States ») : vus uniquement dans un extrait de recherche (−1,3 % pour les hommes, −1,0 % pour les femmes au Smic pour +1 % du Smic réel) ; **non lus, donc non utilisés**.
- **Laroque et Salanié (2000)** : non lu (cité par Montaigne).
- Remarque d'organisation : `sources/T13/` contient aussi des fichiers d'une autre tâche (rachats d'actions : `crs_R47397…`, `nber_w…`, `pwbm…`, etc.). Ils n'ont pas été touchés et ne figurent pas dans `sources.csv`.
