# T16, volet A : État et institutions

Agent de recherche, 14 octobre 2026. Chiffres détaillés : `A_chiffres.csv` (86 lignes). Sources archivées : `sources/T16/A/` (27 fichiers), index `A_sources.csv`.

Conventions. Les montants sont en Md€ ou M€ courants. Une économie améliore le solde (signe +). Les lignes `calcul` du CSV sont des valeurs dérivées par moi : leur méthode est donnée dans `note`. Repère utilisé ci-dessous : le déficit public de 2025 est de 152,5 Md€ (Insee Première n° 2106). La conversion en pourcentage du déficit ou en euros par habitant reste à faire par l'intégrateur, avec `projection_reference.csv`.

Accès. Plusieurs sites refusent les téléchargements automatiques : budget.gouv.fr (jaunes, projets annuels de performances), EUR-Lex (pare-feu), les PDF `fileadmin` du Sénat, le site de la Banque de France. J'ai donc procédé ainsi :
- pour les textes européens, le Journal officiel de l'UE via le dépôt « cellar » de l'Office des publications ;
- pour la Banque de France, WebFetch, qui enregistre le PDF, archivé ensuite ;
- pour les jaunes, les rapports parlementaires qui les citent. Ces chiffres sont en `medium`.

---

## 1. « Réduire le train de vie de l'État »

### Ce que l'expression peut recouvrir, avec les montants

| Lecture | Montant | Source |
|---|---|---|
| a. Fonctionnement courant de l'État, hors personnel et hors opérateurs | **34,8 Md€** (PLF 2027) | PLF 2027, section de fonctionnement |
| b. Subventions de fonctionnement aux opérateurs (agences, établissements) | 33,2 Md€ (PLF 2027) ; 33,9 Md€ exécutés en 2025 | PLF 2027 ; Cour des comptes, RBDE 2025 |
| a + b. Titre 3 « fonctionnement » | 68,0 Md€ (PLF 2027) ; 70,1 Md€ exécutés en 2025 | idem |
| c. Personnel de l'État | 162,6 Md€ (PLF 2027) : 93,0 de rémunérations d'activité + 68,4 de cotisations, dont la contribution au CAS Pensions. En 2025 : 156,2 Md€ exécutés, dont 107,0 de rémunérations et 49,2 de CAS Pensions | idem |
| d. Opérateurs : nombre et financement | 434 opérateurs ; plafond d'emplois 2027 de 397 282 ETPT ; 77,0 Md€ de financements publics au PLF 2025, dont 53 hors universités et recherche ; hors enseignement et recherche, 14 Md€ de personnel et 13,2 Md€ de fonctionnement | RBDE 2025 ; PLF 2027 art. 64 ; Sénat, commission d'enquête n° 807 (jaune cité) |
| e. « Pouvoirs publics » (élus, institutions) | 1,16 Md€ | voir § 2 |

### Économies déjà chiffrées
- **Gouvernement (2025)** : 2 à 3 Md€ sur les agences et opérateurs, hors universités. Je ne l'ai trouvé que tel que rapporté par le Sénat, qui précise que la ministre « n'a pas été en mesure de préciser » le calcul.
- **Sénat, commission d'enquête de juillet 2025** :
  - environ 540 M€ par la mutualisation des fonctions support (hypothèse « très volontariste ») ;
  - 2,2 Md€ pour une baisse de 8 % des coûts de personnel et de fonctionnement des opérateurs, effort qui « ne serait pas réellement à missions constantes » ;
  - environ 10 M€ en supprimant 20 % des commissions consultatives.
- **PLF 2027** : −2 209 ETP chez les opérateurs, −800 ETP en administration centrale, gel du point d'indice, mesures catégorielles limitées à 166 M€. Ces mesures sont **déjà dans la référence 2027** : ne pas les compter une seconde fois.

### Non trouvé
- Le jaune « Opérateurs de l'État » du PLF 2027 (budget.gouv.fr inaccessible ; le Chrome n'était pas autorisé). Le nombre d'opérateurs en 2027 et le total des financements 2026-2027 ne sont donc pas sourcés.
- Un chiffrage de la Cour des comptes sur les fusions d'opérateurs : je n'ai pas trouvé de chiffre propre à la Cour dans les documents lus.

### Pièges
- **Double compte opérateurs** : les 33,2 Md€ de subventions pour charges de service public paient en partie le personnel des opérateurs. Ne pas les additionner aux 14 Md€ de personnel des opérateurs.
- **Financements des opérateurs** : les 77 Md€ comprennent des crédits d'intervention qu'ils redistribuent (France compétences, ANAH, AFITF, France Travail). Ce n'est pas du « train de vie ».
- **Fonctionnement 2025** : la baisse de 2025 (−6,7 Md€) est un effet de périmètre, la suppression du programme 369.
- **Personnel** : la contribution au CAS Pensions (49 Md€) paie des pensions déjà servies. Elle ne baisse pas si l'on réduit le fonctionnement.

**Proposition pour la carte.** « Selon ce qu'on y met, le "train de vie" de l'État va de 35 Md€ (fournitures, loyers, informatique, déplacements des ministères) à plus de 230 Md€ si l'on ajoute les salaires et les agences. Les économies chiffrées sur les agences vont de 0,5 Md€ (Sénat, à missions constantes) à 2 à 3 Md€ (annonce du gouvernement, sans détail du calcul). »

---

## 2. « Réduire les privilèges des élus, le nombre de parlementaires »

### Trouvé

**Mission « Pouvoirs publics », PLF 2027, état B (en CP)** : 1 159,4 M€, soit environ 0,8 % du déficit 2025. En 2026 : 1 140,2 M€.

| Institution | PLF 2027 | Rappel 2025-2026 |
|---|---|---|
| Présidence de la République | 122,56 M€ | inchangée |
| Assemblée nationale | 619,80 M€ | 607,65 M€ (+2,0 %) |
| Sénat | 360,54 M€ | 353,47 M€ (+2,0 %) |
| La Chaîne parlementaire | 35,60 M€ | |
| Conseil constitutionnel | 20,0 M€ | |
| Cour de justice de la République | 0,88 M€ | |

Le Sénat évalue le coût de la mission à « moins de 17 euros par habitant en 2025 ».

**CESE** : 34,0 M€ en CP (PLF 2027), dont 27,6 M€ de personnel. Il relève de la mission « Conseil et contrôle de l'État », pas de « Pouvoirs publics ».

**Anciens présidents** (Nicolas Sarkozy et François Hollande) :
- 1,39 M€ en 2024 pour le personnel, les locaux et les frais (programme 129 ; rapport spécial de l'AN sur le PLF 2026, annexe 1) ;
- 2,51 M€ de sécurité en 2022 (réponse à la question écrite n° 9580, lue par WebFetch, fiche d'extraits) ;
- ordre de grandeur total, calculé : environ 4 M€ par an, hors dotation annuelle prévue par la loi de 1955.

La PPL n° 3083 (2026) avance 4 036 k€ pour 2022, dotation comprise. C'est une source secondaire militante : je ne l'utilise que comme recoupement.

**Indemnité et moyens d'un député** (AN, fiche n° 7, régime 2026) :
- indemnité : 7 637,39 € bruts par mois (5 953,34 € nets) ;
- dotation de fonctionnement : 7 238,04 € par mois ;
- crédit collaborateurs : 11 463 € par mois.

**Réduction du nombre de parlementaires** : l'étude d'impact du projet de loi organique n° 2204 (2019) retient une baisse de 25 % (577 → environ 433 députés ; 348 → environ 261 sénateurs). **Elle ne chiffre aucune économie** : la partie « impacts » est seulement juridique.

### Calcul indicatif (`low`)
Les enveloppes individuelles de 144 députés en moins représentent environ 45 M€ par an. Ce calcul exclut les charges patronales, les déplacements et les coûts fixes de l'Assemblée, qui ne baissent pas en proportion. Le Sénat n'est pas calculé.

### Non trouvé
- Un chiffrage officiel d'une réduction du nombre de parlementaires. Recherches menées :
  - l'étude d'impact de 2019 ;
  - l'avis du Conseil d'État, cité dans les résultats de recherche ;
  - un chiffrage de l'iFRAP (160 M€), page en erreur 403, non lu, donc non retenu ;
  - un article universitaire (UT Capitole), qui ne contient aucun chiffre.
- L'indemnité des sénateurs sur une source du Sénat : la règle est la même (ordonnance n° 58-1210), mais elle n'a pas été vérifiée sur place.
- Le coût 2024 de la sécurité des anciens présidents : la question écrite n° 11485 (2025) est sans réponse lisible.

### Pièges
- La dotation de l'Assemblée et du Sénat paie surtout des services, des bâtiments et les pensions des anciens parlementaires, pas les seules indemnités.
- Pour les anciens présidents, la sécurité relève du ministère de l'Intérieur et le reste du programme 129 : deux budgets distincts.
- Les montants de la sécurité (2022) et des autres dépenses (2024) ne portent pas sur la même année.

**Proposition pour la carte.** « La présidence, les deux assemblées et le Conseil constitutionnel coûtent ensemble 1,16 Md€ par an, moins de 1 % du déficit. Les deux anciens présidents coûtent environ 4 M€ par an, sécurité comprise. Réduire d'un quart le nombre de parlementaires n'a jamais été chiffré officiellement ; les seules indemnités et enveloppes des députés concernés représenteraient environ 45 M€. »

---

## 3. « Supprimer 250 000 à 300 000 postes de fonctionnaires »

### Trouvé

**Effectifs fin 2024** (Insee Première n° 2094) :

| Versant | Agents |
|---|---|
| Fonction publique de l'État | 2 587 400 |
| Fonction publique territoriale | 2 039 400 |
| Fonction publique hospitalière | 1 249 900 |
| **Ensemble** | **5 876 700** |

Mouvements en 2024 : 528 800 entrées et 499 400 sorties de personnels civils, tous motifs confondus.

**État** :
- plafond d'emplois 2027 : 2 032 750 ETPT ;
- schéma d'emplois 2027 : **+8 025 ETP** (le PLF crée des postes) ;
- effectifs exécutés en 2025 : 1 974 000 ETPT.

**Coût moyen d'un poste**, trois mesures possibles :
- **État hors pensions** : 107,0 Md€ / 1,974 M ETPT ≈ **54 200 € par an** (calcul sur le RBDE 2025) ;
- **coût d'un agent entrant** : 31 000 € (État) et 23 240 € (collectivités), utilisé par l'Institut Montaigne en 2017 pour chiffrer un départ non remplacé (`medium`) ;
- **tous versants** : 370 Md€ de rémunérations des administrations publiques / 5,88 M agents ≈ 63 000 € (`low`, périmètres différents).

**Départs à la retraite** (DGAFP, édition 2025) :
- 136 700 nouvelles pensions en 2024, tous statuts, en baisse de 13 % à cause de la réforme de 2023 ;
- dont environ 114 700 fonctionnaires et militaires : État civils 38 800, militaires 11 800, territoriaux 43 000, hospitaliers 19 800, ouvriers d'État 1 300.

**Précédents** :
- Montaigne 2017 : 120 000 suppressions sur 5 ans, pour 3,17 Md€ par an au terme du quinquennat. Backtest du projet : les effectifs de l'État ont **augmenté** de 3 825 ETPT entre 2018 et 2022 (ligne déjà présente dans `mesures_cout`) ;
- RGPP 2008-2012 : 840 M€ par an selon la Cour des comptes, citée par Montaigne (rapport non lu) ; la moitié des économies a été rendue aux agents.

### Calcul indicatif (`low`)
- **Économie brute une fois tous les postes supprimés** : entre 7,75 et 9,3 Md€ par an au coût d'un entrant (euros de 2017), et entre 13,6 et 16,3 Md€ au coût moyen de l'État.
- **Calendrier** : il y a environ 115 000 départs de titulaires par an. Avec un départ sur deux non remplacé, 250 000 à 300 000 postes demandent **environ 4,5 à 5 ans**, en supposant que tous les versants appliquent la mesure (calcul).

### Non trouvé
- Un chiffrage publié en 2026 d'une suppression de 250 000 à 300 000 postes.
- Le jaune « Rapport sur l'état de la fonction publique et les rémunérations » (budget.gouv.fr), qui donnerait le coût moyen officiel par catégorie.

### Pièges
- **Pensions** : la contribution au CAS Pensions ne disparaît pas avec le poste. Prendre 79 000 € par ETPT surestime l'économie.
- **Brut et net** : il faut retirer l'impôt et les cotisations que paient les agents, ainsi que les coûts de remplacement (sous-traitance, heures supplémentaires, contractuels).
- **Qui décide** : les collectivités (2 M d'agents) fixent librement leurs effectifs, et les hôpitaux sont financés par l'assurance maladie. L'État ne peut décider que pour son propre versant.
- **Périmètre** : environ 1,1 M d'agents de l'État sont dans l'Éducation nationale (plafond du ministère : 1 092 923 ETPT). Une telle mesure touche donc forcément l'école, la défense ou la sécurité.
- **Calendrier** : la réforme des retraites de 2023 réduit les départs et allonge ce calendrier.

**Proposition pour la carte.** « Supprimer 250 000 postes sur 5,9 millions d'agents publics rapporterait, une fois fait, entre 8 et 16 Md€ par an selon le coût retenu par poste. En ne remplaçant qu'un départ à la retraite sur deux, il faudrait environ cinq ans. Les annonces passées de ce type n'ont pas été tenues : l'État a gagné des postes entre 2018 et 2022. »

---

## 4. « Réduire la contribution française au budget de l'UE »

### Trouvé

**Prélèvement sur recettes (PSR-UE)** :
- **30,906 Md€ dans le PLF 2027** (article 55) ;
- 28,440 Md€ en LFI 2026 (28,118 Md€ en prévision révisée) ;
- 22,96 Md€ exécutés en 2025 (Cour des comptes).

Les droits de douane s'ajoutent au PSR : 1,9 Md€ en 2024 et environ 2 Md€ en 2027.

**Solde net de la France (contributeur net)** :
- **−7,9 Md€ en 2024**, hors plan de relance, et −8,4 Md€ hors dépenses administratives (jaune du PLF 2026, cité par l'AN, `medium`) ;
- −9,3 Md€ en 2023 ;
- −9,8 Md€ par an en moyenne de 2021 à 2024.

**Données de la Commission (`high`)** :
- en 2024 : 16,46 Md€ de dépenses de l'UE en France hors NextGenerationEU, 8,87 Md€ de versements NextGenerationEU, 24,33 Md€ de ressources propres ;
- solde que j'en recalcule : −7,8 Md€ hors NextGenerationEU, ce qui confirme le jaune. **Il devient positif (+1,1 Md€) en 2024 si l'on compte les subventions du plan de relance** ;
- en 2025 : −8,7 Md€ hors plan de relance, −6,5 Md€ avec.

**Rabais accordés à cinq pays** : la France en paie 1,5 Md€ (2025). La Commission donne 1,49 Md€ en 2024 et 1,51 Md€ en 2025.

### Ce que disent les textes, avec citations dans le CSV
- **Article 311 TFUE** : la décision « ressources propres » est adoptée à l'unanimité et ratifiée par chaque État.
- **Article 9 § 3 de la décision 2020/2053** : les États « mettent les ressources propres […] à la disposition de la Commission ».
- **Article 12 du règlement n° 609/2014** : un retard de paiement entraîne des intérêts de retard.
- **Article 258 TFUE** : la Commission peut engager un recours en manquement.

Aucun texte ne prévoit de réduction unilatérale. Une baisse ne peut se négocier que pour le prochain cadre financier (2028-2034), à l'unanimité. Le rabais est la voie que d'autres États ont suivie, par l'article 2 § 4 de la décision.

### Non trouvé
- Le jaune « Relations financières avec l'Union européenne » du PLF 2027, lu ni directement ni de seconde main : les rapports spéciaux du PLF 2027 ne sont pas encore en ligne.
- La version consolidée du règlement n° 609/2014 : seule la version initiale a été lue.
- Aucun chiffrage officiel d'une « baisse » de la contribution.

### Pièges
- **Brut et net** : le PSR (30,9 Md€) n'est pas le coût net. La France reçoit environ 16 Md€ par an, surtout pour l'agriculture.
- **Plan de relance** : avec ou sans NextGenerationEU, le solde change de signe en 2024. Ces subventions seront remboursées par le budget de l'UE à partir de 2028.
- **2026-2027** : la hausse est un rattrapage habituel en fin de cadre financier, pas une décision nouvelle.
- **Effet retour** : réduire la contribution, si c'était possible, réduirait aussi les retours.

**Proposition pour la carte.** « La France verse environ 31 Md€ à l'UE en 2027 et en reçoit environ 16 Md€ : elle est contributrice nette d'environ 8 Md€ par an (2024). Le montant découle de règles adoptées à l'unanimité ; la France ne peut pas le baisser seule. Un changement passe par la négociation du prochain budget européen (2028-2034). »

---

## 5. « Annuler la dette détenue par la BCE »

### Trouvé

**Stock détenu** : la Banque de France détient au titre de l'APP et du PEPP 546 Md€ de dette publique (coût amorti, fin 2025), puis 488 Md€ au 30 juin 2026. La baisse vient des seules tombées : aucune vente, et plus de réinvestissement depuis 2023 et 2025 (communiqué du 12/9/2026).

**Intérêts** : ces titres rapportent en moyenne 0,68 %. La Banque de France paie 2,26 % sur les dépôts des banques qui les financent. Sa marge sur ces titres est donc **négative de 12,6 Md€ en 2025** (−31,1 Md€ en 2024).

La BCE confirme que les intérêts des titres français sont perçus par la Banque de France et non partagés (lettre du 28/5/2021). Aucun montant d'intérêts publié n'a été trouvé. Ordre de grandeur calculé (`low`) : 0,68 % × 546 Md€ ≈ 3,7 Md€ par an.

**Retour vers l'État** : il passe par l'impôt sur les sociétés et le dividende de la Banque de France.
- 6,1 Md€ en 2019 ;
- 0,84 Md€ en 2023 ; 0,16 Md€ en 2024 ; 2,2 Md€ en 2025 (1,55 Md€ d'impôt et 0,66 Md€ de surcouverture des retraites) ;
- **aucun dividende de 2022 à 2025** ;
- résultat net de la Banque de France : 0 en 2023, −7,7 Md€ en 2024, +8,1 Md€ en 2025, grâce à 11 Md€ de plus-values exceptionnelles sur l'or.

**Texte** : article 123 § 1 TFUE, cité dans le CSV. La BCE a écrit le 5 février 2021 que « l'annulation de dettes publiques par la BCE n'est pas compatible avec les traités, car elle enfreindrait l'interdiction du financement monétaire ».

**Contexte** : charge nette de la dette de l'État de 72,9 Md€ (PLF 2027) ; intérêts de l'ensemble des administrations publiques de 64,7 Md€ (2025).

### Non trouvé
- Les intérêts réellement versés par l'État sur les titres détenus par la Banque de France. La BCE ne publie pas ce montant par pays.
- La part exacte de titres d'État (OAT) dans les 546 Md€. Le stock comprend aussi des agences, des collectivités et des titres supranationaux, selon la BCE.
- **Aucune source chiffrant un « gain » d'une annulation** : je n'en propose pas, conformément à la consigne.

### Pièges
- **Ce que l'État paie vraiment** : les intérêts que l'État verse à la Banque de France lui revenaient en partie avant 2022. Ce n'est plus le cas depuis la hausse des taux.
- **Ce qu'une annulation ferait** : elle supprimerait l'actif de la Banque de France (546 Md€), qui dépasse sa situation nette (283 Md€, surtout des plus-values latentes sur l'or). Elle ne supprimerait pas le coût des réserves bancaires. Cette conséquence relève de l'analyse ; aucun chiffre sourcé ne l'accompagne.
- **Stock qui baisse** : le stock diminue d'environ 100 Md€ par an au rythme observé au premier semestre 2026 (58 Md€ en six mois), par simple remboursement.

**Proposition pour la carte.** « La Banque de France détient environ 490 Md€ de dette publique française, achetée sur les marchés depuis 2015. Les traités interdisent aux banques centrales de financer les États, et la BCE juge qu'une annulation enfreindrait cette règle. Depuis la hausse des taux, la Banque de France perd de l’argent sur ces titres (au moins depuis 2023) et ne verse plus de dividende à l’État depuis 2022 : les intérêts qu'il lui paie ne lui reviennent donc presque plus. »

---

## Décisions laissées à l'intégrateur
1. **Train de vie** : quelle lecture chiffrer en central (34,8 hors personnel et opérateurs ? 68,0 ?), et faut-il afficher l'annonce de 2 à 3 Md€, non documentée, à côté des 0,54 Md€ du Sénat ?
2. **Fonctionnaires** : le coût par poste (31 000 € pour un entrant, 54 200 € de coût moyen de l'État) et la règle du backtest à appliquer. La ligne Montaigne 2017 montre un réalisé de signe opposé.
3. **UE** : afficher le solde net avec ou sans NextGenerationEU.
4. **Lignes `calcul`** : les marquer `source_type = calcul` si elles entrent dans `data/raw/idees.csv`.
5. **Mises à jour** : refaire le PSR-UE et le solde net dès que le jaune UE du PLF 2027 ou les rapports spéciaux seront lisibles.
