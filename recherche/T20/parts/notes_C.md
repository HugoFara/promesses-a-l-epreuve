# T20, groupe C : coût annoncé et coût réalisé des changements de taux de TVA (2000-2025)

Accès : 2026-10-20. Sources archivées dans `sources/T20/C/` (26 fichiers, `sources_C.csv`). Règles de solde non modifiées.

## 1. Résultat

`cout_C.csv` : 7 lignes, toutes `regle_pressentie` = `Aucune`, `inclus_stats` = 0.

| id | ex ante | réalisé | écart | `type_ex_post` | confiance |
|---|---|---|---|---|---|
| `tva_7pct_2012` (taux de 7 %, 2012) | 1,8 | 2,0 | +11 % | reestimation | high |
| `tva_resto_7pct_2012` (restauration 5,5 → 7 %) | 0,34 | 0,3 (0,2-0,4) | −12 % | reestimation | low |
| `tva_hausse_2014` (10 % et 20 %) | 5,2 | 4,9 | −6 % | reestimation | medium |
| `tva_logement_social_10_2018` | 0,7 | 0,8 | +14 % | reestimation | medium |
| `tva_presse_en_ligne_2018` | 0,15 | 0,15 | 0 | administratif | medium |
| `tva_zoos_2018` (coût) | 0,01 | 0,01 | 0 | administratif | medium |
| `tva_equitation_2024` (coût) | 0,065 | 0,049 | −25 % | reestimation | medium |

Répartition : **0 `observe`**, 5 `reestimation`, 2 `administratif`. Aucun réalisé n'est une recette observée : la TVA est encaissée globalement, jamais par taux. Les « montants exécutés » de la Cour sont des chiffrages faits après coup par la direction du budget (réestimations). Quand le montant exécuté est égal au centime près à la prévision, il s'agit très probablement de la prévision reconduite. Ces lignes sont classées `administratif`. Ce classement de la Cour diffère de celui de `tva_resto_2009` dans `data/raw/mesures_cout.csv` (`observe` pour un chiffrage de dépense fiscale) : la cohérence est à trancher par l'intégrateur.

Dépendances : `tva_resto_7pct_2012` est une composante de `tva_7pct_2012`. Ce ne sont pas deux cas indépendants.

Critère T20 (« au moins 5 changements de TVA avec chiffrage et réalisé, quelle que soit la nature du réalisé ») : atteint de justesse. On compte 6 changements distincts, plus une composante. Deux ont un réalisé égal à la prévision et un a un ex ante publié après le vote. Si l'on exige un ex ante antérieur au vote et un réalisé distinct de la prévision, il reste 4 lignes (`tva_7pct_2012`, `tva_resto_7pct_2012`, `tva_hausse_2014`, `tva_logement_social_10_2018`). Pour une règle propre à la famille `tva_produits`, aucun cas n'est `observe` : le seuil de 5 cas n'est pas atteint.

Choix des mesures : toutes les mesures pour lesquelles un ex ante et un réalisé ont été trouvés ont été retenues, quel que soit l'écart.

Effets annoncés (`effets_C.csv`) : **non produit**. Aucune paire « effet annoncé chiffré / effet constaté » n'a été trouvée pour ces mesures :
- 7 % en 2012 : effet prix annoncé sans chiffre (« augmentation modérée des prix », pl3952, p. 210).
- Hausse 2014 : l'amendement n° 5 affirme seulement que la réforme « n'entraînera pas de hausse des prix des biens et services produits en France » (p. 3).
- TVA « sociale » : « pas d'impact significatif sur les prix » (pl4332, p. 13), mais la mesure n'a pas été appliquée.
- Cinéma 2014 : baisse de 12 centimes par billet annoncée (r1428, p. 155) ; aucun constat trouvé.

Thévenoud constate une hausse des prix de la restauration de 0,75 % en janvier 2012, pour 1,02 % théoriques (i0337, p. 9). Cette donnée relève du groupe A.

## 2. Mesures non comparables ou sans réalisé

- **TVA « sociale » (LFR 1 du 14/03/2012)** : votée puis abrogée avant d'entrer en vigueur. Taux normal 19,6 → 21,2 % au 1/10/2012, « transfert à la Caisse nationale d'allocations familiales de 10,6 Md€ au titre de la TVA » en année pleine (pl4332, p. 13). Le PLFR 2 2012 propose d'« abroger le mécanisme de TVA dite « sociale » [...] avant son entrée en vigueur programmée pour 1er octobre 2012 » (pl0071, p. 21). Pas de réalisé : non comparable.
- **Fin du taux réduit sur les abonnements d'électricité et de gaz (LFI 2025, au 1/8/2025)** : réalisé lu, « + 0,5 Md€ » en 2025 (NEB 2025, p. 20). La mise en œuvre tardive aurait réduit le rendement des mesures de TVA de 0,3 Md€ (p. 13). L'ex ante n'est pas isolé : l'évaluation préalable du PLF 2025 donne « +1,2 Md€ » de TVA pour l'ensemble de l'article, qui comprend la TVA assise sur l'accise (p. 93), et compense la mesure par une baisse d'accise (4,96 €/MWh pour l'électricité, 1,75 €/MWh pour le gaz). Le chiffrage propre aux abonnements n'a pas été trouvé (rapport général du PLF 2025 non lu ; AN et Sénat cherchés par moteur, sans résultat). Ligne non produite. C'est la piste la plus utile à reprendre, avec le rapport général AN ou Sénat sur le PLF 2025, article « accises sur l'énergie ».
- **Restauration 7 → 10 % (2014)** : ex ante trouvé chez Thévenoud (30/10/2012, avant le vote de la hausse), « une augmentation d'un point du taux de TVA réduit dans la restauration pourrait rapporter à l'État une recette supplémentaire de l'ordre de 300 millions d'euros » (i0337, p. 19). Cela donne environ 0,9 Md€ pour 3 points (calculé, statique). Aucun réalisé isolé n'a été trouvé. La dépense fiscale passe de 3,08 Md€ (2013, base 19,6 %) à 2,49 Md€ (2015, base 20 %) (CPO 2015, p. 167). Sa baisse mêle la hausse du taux normal de référence et l'assiette : elle ne mesure pas le rendement de l'étape. Ligne non produite. L'étape est incluse dans `tva_hausse_2014`.
- **Cinéma à 5,5 % (LFI 2014)** : ex ante « 55 millions d'euros en 2014 et 60 millions d'euros les années suivantes », calculé sur un passage de 10 % à 5 % (r1428, p. 155). Le taux finalement retenu est 5,5 %, ce qui donne un coût un peu moindre. Pas de dépense fiscale propre dans les voies et moyens 2025 et 2026, pas de ligne dans les NEB 2014 et 2015. Réalisé non trouvé.
- **Logement social, rénovation énergétique et logement intermédiaire (LFI 2014)** : ex ante chez le rapporteur général, respectivement 350 M€, environ 500 M€ et 45 M€ (r1428, p. 143 ; « quelque 500 à 800 millions » pour la rénovation thermique selon un député, p. 145). Les dépenses fiscales correspondantes (730216, 730223, 730222) sont calculées par rapport au taux normal de 20 %, pas par rapport au taux de 10 % qui se serait appliqué sans la mesure. Elles ne mesurent donc pas le coût de la mesure. Les voies et moyens 2015-2016, qui donneraient 2014, n'ont pas été obtenus. Non comparable en l'état.
- **Retour des livres à 5,5 % (1/1/2013)** : ex ante « le coût est estimé à 50 M€ à compter de l'année 2013 » (pl0071, p. 233). Réalisé non trouvé (pas de dépense fiscale propre ; NEB 2013 sans détail).
- **Équidés (taux normal imposé par la CJUE, 2013)** : évaluation préalable « Non chiffrable » (pl0403, p. 303). Non comparable.
- **Baisse du taux normal 20,6 → 19,6 % (1/4/2000) et travaux dans les logements à 5,5 % (LFI 2000)** : le PLFR 2000 (pl2335) a été téléchargé, mais son texte n'est pas extractible (polices non codées) et l'OCR n'a pas été fait. Un extrait de moteur de recherche cite « 18,45 milliards F » ; il n'a pas été vérifié et n'est pas retenu. Le rapport de la Cour sur l'exécution 2000 est introuvable en ligne (recherche infructueuse). Non trouvé.
- **Masques et gels à 5,5 % (2020), protections hygiéniques (2016), billetterie des spectacles (2012), livres numériques (2012), œuvres d'art (2015)** : non trouvés. Les NEB 2015, 2016, 2017, 2020 et 2021 ont été lues : pas de tableau des mesures de TVA, ou des mesures dites « négligeables ». Les NEB 2021-2023 ne listent que des transferts de TVA et l'effet du bouclier tarifaire. Les rapports d'évaluation des articles n'ont pas été cherchés faute de réalisé.
- **Taux réduits récents (bornes de recharge 2023, équipements solaires 2025)** : la dépense fiscale 730234 vaut 3 M€ en 2023 et 4 M€ en 2024 ; pour 730236, la première année réalisée n'est pas publiée. Chiffrage préalable non cherché ou non trouvé.

## 3. Documents parcourus

Documents couvrant plusieurs mesures (lus en premier) :

- Cour des comptes, notes d'exécution budgétaire sur les recettes : 2012, 2014, 2015, 2016, 2017, 2018, 2020, 2021, 2025 (archivées ici). Les NEB 2013, 2019, 2022, 2023 et 2024 ont été lues dans `sources/T18/B/` (sans mesure de taux de TVA utile, sauf 2013 : effet de structure seulement).
- Cour des comptes, RBDE 2012 et 2014 (archivés ici). RBDE 2013, 2015, 2016 et 2017 lus dans `sources/T18/` : pas de tableau par mesure de TVA, à part le total des mesures antérieures de TVA en 2017 (+0,1 Md€).
- CPO, *La taxe sur la valeur ajoutée* (déc. 2015) : dépenses fiscales de TVA par année (tableau 8), restauration, travaux.
- Voies et moyens, tome II : PLF 2025 (copie de Public Sénat) et PLF 2026 (site de l'AN) ; tome I du PLF 2026.

**Inaccessibles** : les tomes II des voies et moyens antérieurs au PLF 2025 n'ont pas été obtenus. performance-publique.budget.gouv.fr ne figure plus dans les résultats de recherche. budget.gouv.fr a renvoyé une page vide à WebFetch. La page média de l'AN pour le PLF 2024 (`/dyn/media/.../evaluation-des-voies-et-moyens-tome-ii`) renvoie du HTML par curl et une erreur 404 par WebFetch. C'est la principale limite : avec les tomes II de 2013 à 2017, on pourrait chiffrer d'autres réestimations (cinéma, rénovation énergétique, étape restauration 2014). Les évaluations préalables du PLF 2014 ne sont pas dans le projet n° 1395 : l'annexe séparée n'a pas été trouvée par les URL testées. Les chiffrages ex ante 2014 viennent donc du rapport général. senat.fr n'a pas été sollicité directement.

## 4. Points de vigilance pour l'intégrateur

- **Nature du réalisé** : la consigne T20 l'annonçait. Les « montants exécutés » de la Cour sont classés `reestimation`, et `administratif` quand ils égalent la prévision. Dans T18, des chiffrages analogues de la Cour ont été classés `observe` (par exemple `maj_is_5pct_2012`, `cef_2012`) ou `administratif` (`carbone_convergence_2018`). Une règle de classement commune reste à fixer.
- **Année et périmètre** : 2012 et 2014 sont des premières années à 11 mois d'encaissements, des deux côtés. Pour la hausse de 2014, l'ex ante au vote (6,4 Md€, régime de croisière) porte sur un dispositif différent de celui appliqué. La ligne compare donc la prévision LFI 2014 (5,2) au réalisé de la même année.
- **Comportement** : les deux chiffrages ex ante lus en primaire (7 % en 2012, restauration) sont mécaniques (rendement d'un point × écart de taux), d'où `non`. Les autres sont `inconnu`.
- **Écarts** : de −25 % à +14 %, de signe variable (deux hausses de taux sous-estimées, une surestimée ; une baisse de taux surestimée). Ces écarts ne disent rien de la répercussion sur les prix ni de l'effet sur les volumes, que ces chiffrages ne séparent pas de l'évolution spontanée de l'assiette.
