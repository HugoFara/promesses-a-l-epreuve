# T14 — Retraites : profil de montée en charge de `l_ret62` et `l_ret60`

Date de consultation : 2026-10-14. Objet : remplacer l'hypothèse « coût 2027 constant en % du PIB » (`scripts/projection.py`) pour les deux lignes signalées par l'audit (`recherche/audit/rapport.md` §4.2).

Conventions :
- **[lu]** : lu dans le document archivé (chemin indiqué) ;
- **[lu, graphique]** : valeur lue à l'œil sur un graphique (incertitude d'environ ±0,1 à 0,2 Md€) ;
- **[seconde main]** : chiffre lu chez un tiers qui cite la source ;
- **[extrait de recherche]** : vu seulement dans un résultat de moteur de recherche, non vérifié ;
- **[calcul]** : calcul de T14, non publié par la source.

Signe : les montants sont des **économies** de la réforme (amélioration du solde). Le coût d'une abrogation en est l'opposé.

---

## 0. Correction préalable : ce que dit vraiment le PLFSS 2027

L'audit (§4.2) parle de « +1,9 en 2028, +2,8 en 2029 et +3,7 en 2030 selon le PLFSS 2027 (effets de la suspension) ». **Ce n'est pas ce que dit le texte.** Ces montants sont le **rendement de la réforme 2023 net de la suspension**, sur le champ des régimes obligatoires de base (ROBSS), y compris la rétrocession des économies de la fonction publique d'État. Ce ne sont pas des effets de la suspension.

Ce sont aussi des **variations**, pas des niveaux. Le texte les cite pour expliquer l'évolution annuelle du solde. En niveau, le rendement de la réforme dépasse déjà 4 Md€ sur les ROBSS en 2027 (tableau 27 du rapport annexé).

Deux lectures restent possibles, et le texte ne permet pas de trancher :
- **Lecture A** : écarts cumulés depuis 2026. On aurait 0,8 / 1,9 / 2,8 / 3,7, soit des gains annuels de +0,8, +1,1, +0,9 et +0,9.
- **Lecture B** : 0,8 est l'écart 2026→2027, puis 1,9 / 2,8 / 3,7 sont des écarts cumulés depuis 2027.

**La lecture « gains annuels successifs de 1,9, puis 2,8, puis 3,7 » est peu plausible.** Elle donnerait 9,2 Md€ de gain sur les ROBSS entre 2026 et 2030. Le rapport annexé de 2023 n'en prévoyait que 5,5 sur ce champ (tableau 27 : 2,6 → 8,1), et la suspension ne fait que décaler le calendrier.

---

## 1. Profil annuel du rendement de la réforme 2023

### 1.1 Tableau des sources

| # | Source (fichier) | Champ | 2026 | 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | 2035 | Page | Statut |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Rapport annexé au PLFRSS 2023, tableau 16 (`sources/T2a/rapport_objectifs_effets_reforme_2023.pdf`) | Système de retraite, **brut** (mesure d'âge appliquée à tous, sans accompagnement), Md€ courants | 7,5 | 10,3 | 13,2 | 15,3 | 17,7 | – | – | – | p. 61 | [lu] |
| 1b | idem, tableau 16 | ROBSS vieillesse + FSV, hors effet SRE, brut | 4,9 | 6,7 | 8,5 | 9,9 | 11,5 | – | – | – | p. 61 | [lu] |
| 2 | idem, tableau 27 | Système de retraite hors effet SRE, **net des mesures d'accompagnement**, hors recettes nouvelles | 4,0 | 6,2 | 8,6 | 10,0 | 11,8 | – | – | – | p. 96 | [lu] |
| 2b | idem, tableau 27 | ROBSS vieillesse + FSV hors SRE, net | 2,6 | 4,1 | 5,7 | 6,7 | 8,1 | – | – | – | p. 96 | [lu] |
| 2c | idem, tableau 27 | Régimes complémentaires | 1,4 | 2,2 | 2,9 | 3,2 | 3,7 | – | – | – | p. 96 | [lu] |
| 3 | idem, tableau 28 | Recettes nouvelles (CNRACL + 0,12 pt) | 1,5 | 1,5 | 1,5 | 1,6 | 1,7 | – | – | – | p. 96 | [lu] |
| 4 | idem, tableau 5 | Système, brut (« 2 ans à 3 mois/génération + accélération DAR ») | – | – | – | – | 17,7 | – | – | **22,1** | p. 27 | [lu] |
| 5 | Étude d'impact PLFRSS 2023, AN n° 760 (`sources/T14/ret_an760_etude_impact_plfrss2023.pdf`) | Système, brut | 7,5 | – | – | – | – | – | – | – | PDF p. 39 | [lu] ; s'arrête en 2026 |
| 6 | iFRAP, 09/07/2024 (`sources/T14/ret_ifrap_mise_en_garde_wb20240709.html`) | Système : 10,3 brut − accompagnement + « autres mesures » | – | **8,3** | – | – | **13,7** | – | – | – | tableau HTML | [lu] |
| 7 | OFCE (V. Touzé), tableau (`sources/T14/ret_ofce_retraite_table.png`) | Système, net + recettes nouvelles | – | 7,9 | – | – | 13,8 | – | – | – | image | [lu] (reprend le rapport annexé) |
| 8 | Cour des comptes, févr. 2025, graphique 31 (`sources/T2a/ccomptes_retraites_2025.pdf`) | **Régime général seul** (Cnav, solde), Md€ constants 2024 | ≈3,0 | ≈4,0 | ≈4,8 | ≈5,5 | ≈6,0 | ≈6,5 | **7,1** (pic) | **6,0** | p. 65 | [lu] pour 2025 (1,6), 2032 et 2035 ; [lu, graphique] pour les autres années |
| 9 | Cour des comptes, tableau 5 | Système, en 2030, Md€ 2024 (DG Trésor / Rexecode) | – | – | – | – | 9,7 / 11,8 | – | – | – | p. 68 | [lu] |
| 10 | PLFSS 2027, AN n° 3211, annexe A (`sources/T1/PLFSS2027_projet_AN3211.html`) | ROBSS, rendement **net de la suspension**, y c. rétrocession FPE ; **variations** (cf. §0) | – | 0,8 | 1,9 | 2,8 | 3,7 | – | – | – | annexe A, « Situation par branche » et trajectoire ROBSS | [lu] |
| 10b | idem | ROBSS : rendement 2027 attendu avant suspension (variation) ; effet de la suspension | – | 1,8 ; −1,0 | – | – | – | – | – | – | idem | [lu] |

### 1.2 Citations exactes

- **(1)** Rapport annexé, p. 60 : « Elle produira ainsi un rendement brut de 10,3 Md€ en 2027 (et 17,7 Md€ en 2030) dans le champ du système de retraite ». Et : « Sur le seul champ des régimes obligatoires de base de sécurité sociale (ROBSS), le rendement de la mesure est évalué à 6,7 Md€ en 2027 […] En 2030, le solde des ROBSS sera amélioré de 11,5 Md€ hors rendement FPE ».
- **(2)** Tableau 27, p. 96 : « Système de retraite hors effet sur la dotation d'équilibre SRE -0,3 1,0 2,4 4,0 6,2 8,6 10,0 11,8 » (2023 à 2030). Le graphique 60 (p. 95), intitulé « à l'horizon 2040 », s'arrête en fait en 2030 et donne les mêmes valeurs (« Impact global »).
- **(4)** Tableau 5, p. 27 : « Hausse de l'âge légal de deux ans (3 mois/génération) + et accélération de la hausse de la durée d'assurance (1 trimestre par génération) 5,3 17,7 22,1 » (2025, 2030, 2035).
- **(5)** AN 760, p. 39 : « L'impact financier de la réforme est ensuite évalué à 3,3 Md€ en 2024, 5,3 Md€ en 2025, et 7,5 Md€ en 2026 pour l'ensemble [du système] ». Et p. 40 : « le surcroît de PIB associé serait de 0,7 % en 2027, et de 1,1 % en 2030 ».
- **(6)** iFRAP, tableau « Synthèse des effets des mesures de financement » : « Relèvement de l'âge […] 10,3 | 17,7 ; Mesures d'accompagnement -2,8 | -4,8 ; Autres mesures 0,8 | 0,8 ; Solde 8,3 | 13,7 ; Mesures Assemblée nationale -0,1 | -0,55 ; Mesures Sénat -0,4 | -0,7 ».
  - **C'est la source du 8,3 de `l_ret62`**, jusqu'ici « non archivé ».
  - Avec les amendements parlementaires, on obtient 7,8 en 2027 et 12,45 en 2030 [calcul].
  - Les −2,8 d'accompagnement de l'iFRAP diffèrent des −4,1 du tableau 29 du rapport annexé. Le périmètre de l'iFRAP n'est pas expliqué.
- **(7)** OFCE : « TOTAL système de retraite 7,9 | 13,8 » (2027 | 2030). Page `ofce_analyses_retraites.html` (T6) : « il est préférable de regarder 2030 voire 2032 pour avoir une idée de l'impact à plein régime ».
- **(8)** Cour, p. 65 : « Au total, le solde serait amélioré de + 1,6 Md€ en 2025, serait maximal en 2032 (+ 7,1 Md€), puis décroîtrait pour s'élever à 6 Md€ en 2035 et 3,8 Md€ en 2045 ». Titre de section : « un effet positif sur l'équilibre du système jusqu'en 2032 mais de plus en plus limité au-delà ».
- **(9)** Cour, p. 67 : « La direction générale du Trésor et Rexecode convergent sur les effets nets sur le solde, qu'ils considèrent respectivement amélioré de 9,7 Md€ et de 11,8 Md€ en 2030 ».
- **(10)** PLFSS 2027, annexe A, trajectoire des ROBSS :
  - « un rendement de la réforme des retraites de 2023, net de l'effet de la suspension décidée en LFSS pour 2026, de 1,9 milliard d'euros en 2028 (après 0,8 milliard en 2027, en tenant compte de la rétrocession à la sécurité sociale des économies générées pour le régime de retraites des fonctionnaires d'État) » ;
  - « la poursuite de la montée en charge des effets de la réforme des retraites de 2023, nets de l'effet de la suspension décidée en LFSS 2026 (+2,8 milliards d'euros en 2029 puis 3,7 milliards d'euros en 2030, y compris la rétrocession […]) ».
  - Branche vieillesse : « soit 1,9 milliard d'euros d'économies nettes de l'effet de la suspension de la réforme en 2028 et 3,7 milliards d'euros à l'horizon 2030 ».
- **(10b)** Même annexe : « La LFSS pour 2026 a suspendu la réforme de 2023 en décalant sa montée en charge d'une génération. La réforme de 2023 et sa suspension conduiront au total à une amélioration du solde des [ROBSS] de 0,8 milliard d'euros en 2027, la suspension réduisant de 1,0 milliard le rendement initialement attendu de 1,8 milliard d'euros ». Partie sur les écarts à la LPFP : « la montée en charge de la suspension […] vient […] augmenter les prestations vieillesse de 1,0 milliard d'euros ».

### 1.3 La suspension (LFSS 2026, art. 105) : calendrier et coût

**Calendrier voté** [lu, `sources/T1/LFSS2026_JO_2025-12-31_copie_afpa.pdf`, art. 105]. L'âge d'ouverture des droits (AOD) devient :
- 62 ans 9 mois pour les générations nées entre le 1/1/1963 et le 31/3/1965 ;
- 63 ans pour avril-décembre 1965 ;
- 63 ans 3 mois (1966), 63 ans 6 mois (1967), 63 ans 9 mois (1968) ;
- **64 ans à partir de la génération 1969**, contre 1968 avant la suspension.

La durée d'assurance requise (DAR) est de 170 trimestres jusqu'à mars 1965, de 171 pour avril-décembre 1965 et de 172 à partir de 1966.

C'est donc un **décalage d'un trimestre pour les générations 1964 à 1968**, qui disparaît pour les générations nées à partir de 1969. Ces générations atteignent 64 ans à partir de 2033.

**Coût chiffré** :
- Lettre rectificative, p. 124 et 133 [lu, `sources/T4p/D_lettre_rectif_plfss2026.pdf`] : « Cette mesure présente un coût estimé à 0,1 Md€ en 2026 et à 1,4 Md€ en 2027 pour le système de retraites ».
- Amendement n° 2686 [lu, `sources/T4p/D_AN_PLFSS2026_amdt2686.pdf`, p. 6] : « coût supplémentaire de 0,2 Md€ en 2026 et de 0,5 Md€ en 2027 ».
- Total 2027 : 1,9 Md€ [calcul, T4p]. **Aucun document officiel lu ne chiffre la suspension après 2027.**

**Indication de profil (proxy).** Cour des comptes, graphique 38, p. 95 [lu, graphique] : effet sur le solde tous régimes d'un trimestre d'AOD en moins **permanent** à partir de la génération 1964. Il est d'environ −1,3 en 2027, puis d'environ −1,1 à −1,0 de 2028 à 2031, et d'environ −1,5 en 2032-2033. Le trimestre de DAR en moins (permanent) vaut environ −0,4 en 2027 et monte jusqu'à −0,9 en 2031-2032.

La suspension réelle est moins coûteuse que ce proxy à partir de 2031-2033 :
- le trimestre d'AOD ne porte que sur les générations 1964-1968 ;
- le trimestre de DAR ne porte que sur les générations 1964-1965.

**Hypothèse retenue [calcul]** : coût de la suspension constant à 1,9 Md€ en euros 2027 sur 2027-2032, soit une part du PIB en légère baisse.

---

## 2. Coût d'un retour à 60 ans : profil

### 2.1 Fiche Montaigne (`sources/T6/montaigne_nfp_retraites.html`, copie Wayback du 08/07/2024) [lu]

**Pas de profil annuel.** Le chiffrage est un **régime de croisière évalué « à horizon 2027 »**.

Citations :
- « plusieurs éléments peuvent être estimés à horizon 2027 : annulation de la réforme de 2023 : coût de 8,2 Md€ ; annulation du recul de l'âge de la retraite de la réforme de 2010 : coût de 27 Md€ en 2027 ; revalorisation du minimum vieillesse : coût de 0,7 Md€ par an ; revalorisation du minimum contributif au niveau du Smic […] : coût de 13,9 Md€ […] ; intégration des années de RSA comme des années cotisées : coût de 8,4 Md€. »
- « Le total de ces éléments […] représenterait un coût annuel de l'ordre de 58 Md€ à horizon 2027 […] soit respectivement 49 Md€ et 67 Md€. »
- Sur la composante 2010 : « on peut s'appuyer sur les chiffrages publiés par la DREES dans son rapport [qui] concernent principalement l'horizon 2030. Néanmoins, […] les évolutions entre 2027 et 2030 sont minimes (lorsqu'il s'agit des grandeurs en points de PIB). » Puis : « un retour sur ces mesures d'âges représenterait un coût de 1,2 point de PIB à horizon 2027, soit 27 Md€. »
- Champ : « uniquement le régime de retraite, sans chiffrage de ses potentiels autres effets pour les finances sociales ».

Conséquences :
- **Les 58 Md€ correspondent à l'année 2027**, avec une composante 2010 calée en points de PIB de 2030.
- Montaigne suppose lui-même que cette composante (27 Md€, soit 47 % du total) est **stable en % du PIB**.
- Seule la composante « réforme 2023 » (8,2 Md€) monte en charge selon les sources du §1.

### 2.2 Autres chiffrages

| Source | Mesure | Montant | Année | Profil ? | Statut |
|---|---|---|---|---|---|
| Cour des comptes 2025, graphique 32, p. 71 | Arrêt de l'AOD à 63 ans dès la génération 1964 (système, Md€ 2024) | ≈0 en 2027 ; −1 en 2028 ; −1,8 en 2029 ; −2,4 en 2030 ; −3,2 en 2031 ; **−4,2 en 2032** ; ≈−4 à −4,2 en 2033-2036 ; ≈−3 en 2045 | 2027-2045 | **Oui** | [lu, graphique] |
| Cour des comptes 2025, tableau 6, p. 72 | Même scénario, en 2035 | −5,8 pour le système ; −7,2 d'autres recettes publiques ; **−13,0 pour l'ensemble des APU** | 2035 | Non | [lu] |
| iFRAP NFP (T2a/T6, `ifrap_nfp_page.html`) | « Retraite à 60 ans avec 40 annuités pour tous » | 50 (+24 pour minimum contributif et minimum vieillesse = 74) | 2027 ; « hypothèse d'un retour […] avant 2027 » | Non | [lu par T2a/T6] |
| Asterès (`sources/T6/asteres_nfp2.pdf`, p. 2) | Abrogation de la réforme 2023 seule | « 0,6 % de PIB, soit 15 milliards » | phase 1 | Non | [lu] |
| OFCE (`ofce_analyses_retraites.html`) | Abrogation 2023, « vision minimaliste » | 9,5 en 2027 ; 15,6 en 2030 | 2027 et 2030 | Deux points | [lu] |
| Étude d'impact de la réforme 2010 (`sources/T2a/ei_retraites_2010.html`), lue à rebours | 60 → 62 ans + 65 → 67 ans + durée | « économie de près de 2 milliards d'euros en 2011 et d'environ 20 milliards d'euros en 2020 » | 2011-2020 | Rampe sur 10 ans, mais pour un relèvement progressif | [lu] |
| iFRAP 09/07/2024 (tableau d'après la DREES) | AOD 64 ans, Md€ 2020 | 1,7 en 2024 ; 13,6 en 2030 ; 13,3 en 2040 ; 13,3 en 2050 | 2024-2050 | Plateau après 2030 | [lu] |
| G. Cette, cité par Montaigne | Retour à 60 ans, ensemble des finances publiques | 50 à 120 Md€/an | – | Non | [seconde main] |
| Camp présidentiel (Public Sénat, T6) | Retour à 60 ans | 53 | – | Non | [seconde main, T6] |
| Chiffrage du NFP lui-même (`sources/T2a/nfp_proposition_macro_2024.pdf`) | « abrogera les décrets », retour à 60 ans renvoyé à une conférence « durant la législature » | aucun montant ni calendrier chiffré | – | Non | [lu] |

**Différence de nature.** La rampe de la Cour (graphique 32) et celle de la réforme 2010 décrivent des mesures **progressives**, qui touchent une génération après l'autre. Un retour **immédiat** à 60 ans ouvrirait d'un coup les droits à toutes les générations âgées de 60 à 64 ans. Son coût serait donc proche du régime de croisière dès la première année pleine, ce qui est l'hypothèse de Montaigne.

Ce qui croît ensuite, c'est l'écart avec la référence, parce que l'AOD de référence continue de monter jusqu'à 64 ans (génération 1969, en 2033).

**Le calendrier du NFP ajoute une incertitude** : abrogation des décrets immédiate, mais 60 ans renvoyés à une conférence. Ce point relève de la définition de la mesure, pas du profil.

---

## 3. Coefficients proposés (2027 = 1, en part du PIB)

Tous les coefficients ci-dessous sont des **[calcul]** de T14. Ils sont exprimés **par rapport au montant 2027 en % du PIB**, ce qui correspond directement à la mécanique de `projection.py` (montant 2027 × PIB_t / PIB_2027 × coefficient).

PIB nominal et réel de `data/projection_reference.csv` : croissance réelle de 1,1 / 1,1 / 1,2 / 1,2 / 1,2 % et déflateur de 1,6 %. Indices du PIB nominal 2028-2032 : 1,027 ; 1,055 ; 1,085 ; 1,115 ; 1,147.

### 3.1 `l_ret62` (coût 2027 = 8,3 − 1,9 = 6,4 Md€)

Formule : coefficient(t) = [R(t) − S(t)] / 6,4, en Md€ de 2027 rapportés au PIB, avec :
- **S(t)** : coût de la suspension, constant à 1,9 Md€ en euros constants (§1.3) ;
- **R(t)** : rendement de la réforme sans suspension, construit différemment selon le scénario :
  - **central** : iFRAP 8,3 (2027) → 13,7 (2030), en € courants (source 6), avec une répartition 2028-2029 selon la forme du tableau 27 (10,6 et 12,0). Pour 2031-2032, on prolonge avec la croissance réelle du solde du régime général lue sur le graphique 31 de la Cour (6,0 → 6,5 → 7,1 Md€ 2024, soit +8 % puis +9 %) ;
  - **haut** : forme du tableau 27 appliquée à 8,3 (rapports 1,39 / 1,61 / 1,90 en € courants), puis la même prolongation ;
  - **bas** : profil ROBSS du PLFSS 2027 en lecture A (+1,1 / +2,0 / +2,9 au-dessus de 2027), étendu au système par le rapport système / ROBSS y compris SRE du tableau 27 en 2030 (11,8 / 9,3 = 1,27). Pour 2031-2032, on applique la même progression relative que le scénario central (×0,65).

| Année | Bas | Central | Haut |
|---|---|---|---|
| 2027 | 1,00 | 1,00 | 1,00 |
| 2028 | 1,19 | 1,32 | 1,46 |
| 2029 | 1,32 | 1,48 | 1,69 |
| 2030 | 1,45 | 1,69 | 1,99 |
| 2031 | 1,54 | 1,83 | 2,15 |
| 2032 | 1,65 | 2,00 | 2,35 |

**Effet en Md€ de 2027** (central, × 6,4 Md€, avant le facteur comportemental de 0,8) : 6,4 en 2027, 8,4 en 2028, 9,5 en 2029, 10,8 en 2030, 11,7 en 2031 et 12,8 en 2032.

**Recoupements** (rapports du dernier point au premier, avant déduction de la suspension) :

| Source | Champ | Période | En € courants | En part du PIB |
|---|---|---|---|---|
| Tableau 27 | système net | 2030/2027 | 1,90 | 1,75 |
| iFRAP | – | 2030/2027 | 1,65 | 1,52 |
| OFCE | – | 2030/2027 | 1,75 | 1,61 |
| Cour, régime général (graphique 31) | régime général | 2032/2027 | ≈1,78 (€ constants) | ≈1,68 |

La déduction d'une suspension constante amplifie le coefficient, parce que la base de 2027 est réduite de 23 %. Les scénarios central et haut l'intègrent.

### 3.2 `l_ret60` (valeur 2027 utilisée : 58 × 0,967 = 56,1 Md€)

Formule : coefficient(t) = [49,8 + 6,3 × coefficient_ret62(t)] / 56,1.

- **49,8** = 58 − 8,2 : composantes 2010, minimum vieillesse, minimum contributif et RSA. Elles restent constantes en % du PIB, selon l'hypothèse de Montaigne lui-même pour la composante 2010.
- **6,3** = 8,2 − 1,9 : composante « réforme 2023 » nette de la suspension. Elle suit le coefficient de `l_ret62`.

| Année | Bas | Central | Haut |
|---|---|---|---|
| 2027 | 1,000 | 1,000 | 1,000 |
| 2028 | 1,022 | 1,036 | 1,052 |
| 2029 | 1,036 | 1,054 | 1,078 |
| 2030 | 1,051 | 1,078 | 1,111 |
| 2031 | 1,061 | 1,093 | 1,129 |
| 2032 | 1,073 | 1,113 | 1,152 |

**Effet en Md€ de 2027** (central, avant le facteur de 0,8) : +2,0 en 2028, +4,4 en 2030 et +6,3 en 2032 par rapport au maintien constant en % du PIB.

---

## 4. Limites

1. **Il n'existe pas de série officielle unique 2027-2032.**
   - Le rapport annexé (système) s'arrête en 2030, avec un seul point en 2035 pour le brut (22,1).
   - La Cour ne couvre au-delà de 2030 que le régime général, en euros 2024.
   - Le PLFSS 2027 donne des variations ambiguës (§0), sur le seul champ ROBSS.
2. **Le chiffrage de la suspension n'est officiel que pour 2026-2027.** Le profil 2028-2032 repose sur un proxy (Cour, graphique 38, scénario permanent) et sur une hypothèse de coût constant. À partir de 2033, le décalage s'éteint (générations nées à partir de 1969 à 64 ans). Si la projection devait aller au-delà de 2032, la référence se rapprocherait de la réforme d'origine.
3. **Le niveau de 2027 (8,3, iFRAP) n'est pas cohérent avec le net officiel.** Le tableau 27 donne 6,2, ou 7,7 avec les recettes nouvelles. Les coefficients sont des rapports et dépendent donc moins de ce choix, mais une base plus basse donnerait des coefficients plus élevés à suspension fixe.
   - Exemple [calcul] : avec 6,2 au lieu de 8,3 et la forme du tableau 27, le coefficient de 2030 passerait à 2,35 pour le haut.
   - La décote ex post (couche 1 : 74 à 82 %) porte sur le niveau, pas sur le profil.
4. **Valeurs lues sur des graphiques.** Celles des graphiques 31, 32 et 38 de la Cour sont des lectures visuelles. Seuls 1,6 (2025), 7,1 (2032), 6,0 (2035) et 3,8 (2045) sont écrits dans le texte.
5. **`l_ret60`** :
   - la constance en % du PIB des composantes hors 2023 est l'hypothèse de Montaigne, non vérifiée dans la DREES (non lue) ;
   - la validation des années de RSA (8,4) ne concerne que les nouveaux liquidants. Elle devrait donc monter très progressivement, sur des décennies, et non être pleine en 2027. Cela surestime le niveau de 2027 et sous-estime la pente relative, sans que ce soit chiffrable avec les sources lues ;
   - de même, la hausse du minimum contributif porte en partie sur le flux de nouveaux retraités ;
   - une première année partielle (vote en 2027) n'est pas modélisée.
6. **Champ des chiffrages.** Tous les chiffrages portent sur le solde du système de retraite. Les effets sur les autres administrations publiques (recettes induites par l'activité, autres prestations) les doublent environ en 2035 (Cour, tableau 6 : 13,0 contre 5,8) et ne sont pas dans ces coefficients.

## 5. Non lu, ou bloqué

- **Sénat, rapport sur le PLFSS 2026** (`https://www.senat.fr/rap/l25-139-324/l25-139-324-syn.pdf`) : le téléchargement est resté sans réponse (délai dépassé) et WebFetch a échoué. Selon un **[extrait de recherche]**, le Sénat retiendrait 0,4 Md€ en 2026 et 1,8 Md€ en 2027 pour la suspension. Non vérifié.
- **Rapports du COR** (juin 2024, juin 2025, juin 2026) : non consultés. Ils donneraient peut-être un effet annuel de la réforme et de la suspension en points de PIB.
- **Annexes du PLFSS 2027** (annexe 9 / évaluations préalables, rapport à la CCSS d'octobre 2026) : non consultées. Le document n° 3211 archivé ne contient que les articles, les exposés et l'annexe A.
- **iFRAP**, site direct : HTTP 403, d'où l'usage de copies Wayback. La page « la suspension va coûter des milliards » (archivée) porte sur un gel permanent à 62 ans 9 mois, pas sur la suspension votée. Elle n'est pas utilisée pour les coefficients.
- **Rapport DREES** utilisé par Montaigne (décomposition de 2030 en points de PIB) : non lu, chiffres de [seconde main].
- **Rexecode, Repères #05** (avril 2023) : non lu, connu via la Cour.

## 6. Fichiers

- Créés (`sources/T14/`, préfixe `ret_`, sha256 dans `recherche/T14/sources.csv`) :
  - `ret_an760_etude_impact_plfrss2023.pdf` ;
  - `ret_ofce_retraite_table.png` ;
  - `ret_ifrap_mise_en_garde_wb20240709.html` ;
  - `ret_ifrap_suspension_wb20251014.html`.
- Réutilisés :
  - `sources/T2a/rapport_objectifs_effets_reforme_2023.pdf` ;
  - `sources/T2a/ccomptes_retraites_2025.pdf` ;
  - `sources/T1/PLFSS2027_projet_AN3211.html` ;
  - `sources/T1/LFSS2026_JO_2025-12-31_copie_afpa.pdf` ;
  - `sources/T4p/D_lettre_rectif_plfss2026.pdf` ;
  - `sources/T4p/D_AN_PLFSS2026_amdt2686.pdf` ;
  - `sources/T6/montaigne_nfp_retraites.html` ;
  - `sources/T6/ofce_analyses_retraites.html` ;
  - `sources/T6/asteres_nfp2.pdf` ;
  - `sources/T2a/ei_retraites_2010.html` ;
  - `sources/T2a/nfp_proposition_macro_2024.pdf`.
