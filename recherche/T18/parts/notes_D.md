# T18, groupe D : notes de recherche (phase 1)

Règles couvertes : **Effet promis** et **Recette ponctuelle**. Date d'accès de toutes les sources : 2026-10-16. Sources archivées dans `sources/T18/D/` (27 fichiers), listées avec leur sha256 dans `sources_D.csv`. Plusieurs fichiers sont des copies de sources déjà archivées par d'autres tâches (`sources/IS`, `T10a`, `T13`, `T2a`, `T18/A`), signalées comme telles dans le titre.

Règles gelées : commit `0b4175f`, `regles.csv` et `moteur_regles.csv` non modifiés. Rien n'a été écrit hors de `recherche/T18/parts/*_D.*` et `sources/T18/D/`.

## 1. Résultat

| Règle | Lignes retenues | dont `observe` | Cible |
|---|---|---|---|
| Recette ponctuelle (`cout_D.csv`) | 12 | 12 | 8 cas `observe` |
| Effet promis (`effets_D.csv`) | 12 | sans objet | 15 lignes d'effets |

La cible n'est **pas atteinte pour les effets** (12 sur 15). Pour la recette ponctuelle, elle est atteinte en nombre de lignes, mais elle ne l'est plus si l'on compte une seule fois le STDR (4 millésimes du même dispositif), et que l'on retire les doublons probables avec les groupes A et B (voir § 4) : il reste alors 6 dispositifs propres au groupe D (STDR, cellule 2010, pétrolier 2012, taxe additionnelle TRS 2012, versement anticipé IS 2012, CRI si B ne la garde pas).

### Recette ponctuelle (Md€, sens `economie`)

| id | Ex ante | Ex post central (bas-haut) | Écart calculé | Durée annoncée → réelle | Confiance |
|---|---|---|---|---|---|
| stdr_2014 | 1,0 (LFI) | 1,7 (1,7-1,9) | +70 % | guichet 2013-2017 → encaissements 2013-2019 (9,7 Md€) | high |
| stdr_2015 | 1,7 (LFI, presse) | 2,654 (2,1-2,7) | +56 % | idem | low |
| stdr_2016 | 2,4 (LFI, presse) | 2,476 (1,8-2,5) | +3 % | idem | low |
| stdr_2017 | 2,1 (LFI) | 1,1 (1,1-1,315) | -48 % | idem | high |
| cellule_regul_2010 | 0,7 (PLFR 1 2010) | 0,9 | +29 % | « non reconductible » ; remplacée par le STDR en 2013 | high |
| ce_fortune_2012 | 2,325 | 2,3 (2,26-2,33) | -1 % | 2012 seulement → 2012 seulement | high |
| ce_petrolier_2012 | 0,55 | 0,55 (0,55-0,6) | 0 % | 2012 → 2012 | medium |
| ce_trs_2012 | 0,55 | 0,5 | -9 % | 2012 ; mais doublement pérenne de la TRS ensuite | medium |
| ce_is_anticipe_2012 | 0,8 | 1,0 | +25 % | avance de 2013 ; la contribution de 5 % (2011-2012) a été reconduite | high |
| cehr_2012 | 0,6 (somme calculée) | 0,6 | 0 % | durée réelle **non vérifiée** | medium |
| ce_is_2017 | 4,7 | 4,9 | +4 % | une fois (reliquat 0,4 en 2018) | high |
| cri_2023 | 12,3 | 0,6 (0,6-1,7) | -95 % | 3 semestres → prorogée en 2024 | medium |

### Effet promis

| id | Annonce | Constaté | Ratio | Confiance |
|---|---|---|---|---|
| fraude_lfi2013 | 1 Md€ de recettes de lutte contre la fraude | nul | 0 | high |
| fraude_is_lfi2014 | 0,4 Md€ (volet IS) | nul | 0 | high |
| cir2008_levier | 2 € de R&D par € de CIR | ≈1 € | 0,5 | medium |
| cir2008_pib | +0,6 pt de PIB à 15 ans | +0,5 pt (simulation) | 0,83 | low |
| contrat_generation | 220 000 contrats à mi-2015 | 40 300 | 0,18 | medium |
| emplois_avenir_2013 | 100 000 fin 2013 | 88 000 embauches | 0,88 | high |
| ati_2019 | 29 300 bénéficiaires | ≈600 (stock fin 2023) | 0,02 | low |
| demission_reconversion_2019 | 23 500 par an | 25 500 (stock fin 2023) | 1,09 | low |
| prepare_partage | 20 % de pères relayant la mère | 2,5 % | 0,125 | high |
| prepare_emploi_meres | retour anticipé en emploi | pas de hausse | 0 | medium |
| cice_invest | hausse (objet légal) | non établie | 0 | medium |
| cice_export | hausse (objet légal) | aucun effet significatif | 0 | medium |

Statistique descriptive, pour information (calculée sur les ratios non indicatifs, hors `ati_2019`, `demission_reconversion_2019`, `cir2008_pib`) : sur 9 lignes, médiane du ratio = 0,125 ; 6 lignes à 0. Les trois lignes chiffrées hors zéro les plus solides (emplois d'avenir 0,88 ; CIR levier 0,5 ; contrat de génération 0,18) encadrent le facteur gelé de 0,29.

## 2. Pages lues et méthode, par source

- **Rapports « Budget de l'État » de la Cour (2010, 2012-2017, 2019)** : sections « recettes » et annexes des mesures nouvelles. Ils donnent, pour plusieurs années, le chiffrage de la loi de finances et le rendement exécuté : fraude 2013 (p. 83, p. 88 et annexe 7 du RBDE 2013), fraude et STDR 2014 (p. 76-77 du RBDE 2014), STDR 2014-2016 (RBDE 2015 p. 67 et RBDE 2016 p. 82), STDR 2017 (RBDE 2017 p. 17 et p. 71), série complète 2014-2019 (RBDE 2019 p. 63-64), mesures des LFR 2012 (RBDE 2012 p. 72-75, p. 78, annexe 6 p. 258-263), cellule de régularisation 2010 (RBDE 2010 p. 81).
- **PLFR 2 pour 2012 (AN n° 71)**, évaluations préalables des articles 3, 7, 8 et 9 (p. 166, 185-188, 195) ; **PLFR 1 pour 2010 (AN n° 2239)**, exposé général (p. 16) et évaluation de la taxe sur les bonus (p. 146) ; **rapport AN n° 376** sur le PLFR 1 2017 (p. 13 et 18).
- **Cour, prévision des recettes 2014-2023** (décembre 2024), chapitre CRI (p. 68-70).
- **CIR** : enquête de la Cour de 2013 reproduite dans le rapport AN n° 1359 (p. 103, qui cite le Trésor-Éco de janvier 2009 de Cahu, Demmou et Massé) ; avis CNEPI 2021 (p. 3) ; Trésor-Éco n° 290 (p. 1).
- **Contrat de génération** : Cour, RPA 2016 tome I, p. 59 (synthèse), p. 71 et p. 80 (réponse du ministère citant l'étude d'impact).
- **Emplois d'avenir** : étude d'impact AN n° 146 (p. 7 et 14) ; Dares Analyses n° 081 (p. 1 et encadré 2 p. 4).
- **Loi Avenir professionnel** : étude d'impact AN n° 904 (p. 228 et 243) ; Unédic, synthèse de mars 2025 (p. 2-4, p. 8).
- **PreParE** : étude d'impact du projet de loi pour l'égalité réelle (Sénat n° 717, 2013, page HTML) ; HCFEA, février 2019, p. 8-9, p. 155-163.
- **CICE** : France Stratégie 2020 (p. 7-8, p. 11) ; rapport Bozio-Wasmer 2024 (p. 120).

Toutes les citations des deux CSV ont été recherchées automatiquement dans le texte extrait des archives (pdftotext ou HTML nettoyé). Elles s'y trouvent, sauf deux lignes de tableau reconstituées (indiquées entre crochets) dont les chiffres ont été vérifiés à l'œil sur la mise en page (`pdftotext -layout`).

## 3. Exclusions et pistes non abouties (avec les endroits cherchés)

| Piste | Motif |
|---|---|
| Taxe exceptionnelle sur les bonus 2010 | Ex ante lu (362 M€, PLFR 1 2010 p. 146). Ex post incohérent : 298 M€ affectés à OSEO selon le RBDE 2010 (p. 66, note 51), « 360 M€ » dans une note mal composée du RBDE 2014. Exclue faute d'un réalisé net. |
| Emplois du pacte de responsabilité (45 000 en 2015, 190 000 en 2017) | Ex ante lu (étude d'impact PLFRSS 2014, `sources/T10a/C_an_plfrss2014_etude_impact.html`). Ex post non trouvé : COSAPE 2017 (déjà exclu par T10a), rapport Bozio-Wasmer 2024 (aucune estimation d'emploi du pacte 2015, seulement l'absence d'effet sur les exportations). Exclusion T10a maintenue. |
| Suramortissement 2015 | Aucune évaluation : la DGE écrit en avril 2026 qu'« il n'existe pas, à notre connaissance, d'évaluations empiriques des dispositifs de suramortissement » en France (Thema 40, p. 11). La note de conjoncture Insee de juin 2017 ne fait que constater un effet d'anticipation (non archivée). |
| Suramortissement numérique et robotique 2019-2020 | Évaluation trouvée (DGE 2026 : +12 à 14 % d'investissement en matériel des PME industrielles, publiée en 2026). Pas d'annonce ex ante d'effet lue (l'évaluation préalable du PLF 2019 n'a pas été lue ; budget.gouv.fr non tenté). Le document donne la dépense fiscale annuelle (3 à 6 M€, 30 M€ cumulés, d'après les Voies et moyens tome 2) : utile au groupe C si un chiffrage ex ante est trouvé. Source gardée en archive. |
| Autocars « Macron » (22 000 emplois annoncés) | L'étude d'impact de la loi Macron (AN n° 2447) ne contient pas ce chiffre (lue, non gardée). Origine des 22 000 non trouvée ; communiqué de l'Arafer de 2016 introuvable à l'URL indiquée (404). |
| Réforme de l'assurance chômage 2019 : effets sur l'emploi | Aucun chiffre gouvernemental d'emplois lu (recherches web ; dossier de presse du 18 juin 2019 non trouvé). L'Unédic (mars 2025) donne seulement des effets qualitatifs (accès plus rapide à des emplois courts, baisse limitée des séparations par le bonus-malus). |
| Réforme 2023 (« 100 000 à 150 000 retours à l'emploi ») | Chiffre vu seulement dans un résumé de recherche, non lu ; pas d'ex post. |
| Fiscalité du tabac 2018-2020 (-20 % de volumes de cigarettes en 2020) | Ex ante lu (PLFSS 2018, annexe 10, art. 12 ; non gardé). Ex post comparable non obtenu : le bilan OFDT 2019 ne donne que l'évolution 2019/2018 ; 2020 est faussé par les confinements. Piste à reprendre (OFDT, bilans 2017 à 2020). |
| Duflot (objectif de logements) | Ni l'objectif ex ante ni le référé de la Cour de 2018 n'ont été lus (recherche web sans document primaire). |
| Plan de lutte contre les fraudes sociales 2023 | HCFiPS 2026 (`sources/T16/B`) donne 2,06 Md€ de préjudices détectés en 2024 ; l'objectif du plan, à l'horizon 2027, n'a pas été lu et l'horizon n'est pas atteint. |
| Loi fraude de 2018 | Aucun rendement annoncé ou constaté lu. La synthèse de la Cour sur la fraude fiscale (2025, `sources/T16/C`) parle d'objectifs de programmation des contrôles, pas de rendement. |
| CICE : effet PIB (+0,5 pt annoncé) | Pas d'estimation ex post du PIB dans la synthèse de France Stratégie 2020. |
| CIR : +25 000 chercheurs d'ici 2022 | La CNEPI mesure +2 % d'ingénieurs dans les entreprises bénéficiaires : indicateur non comparable. |
| Emplois d'avenir, cible de fin 2014 (150 000) | Doublon du même dispositif ; Dares donne 141 000 recrutés à fin septembre 2014 seulement. |

Non testables, conformément à la consigne : « Effet emploi du SMIC », « Taxe sur les rachats d'actions », « Règle d'or », « Taux d'intérêt », « Médiane des estimations », « Déjà dans la référence ». Aucun cas étranger rencontré, donc pas de fichier `D_etranger.md`.

## 4. Points de vigilance

1. **Ce que teste la ligne « recette ponctuelle ».** La règle gelée met à zéro une recette non récurrente dans le solde de 2027. Les lignes de `cout_D.csv` comparent, comme les autres lignes de coût, le rendement annoncé à celui de la même année ; la durée réelle est donnée dans `note`. Pour juger la règle elle-même, il faut regarder si la recette a reparu les années suivantes. Elle est vraiment restée ponctuelle pour la contribution sur la fortune, la contribution pétrolière et la surtaxe IS de 2017. Elle a été prolongée ou renouvelée pour le STDR (7 ans d'encaissements), la cellule de 2010 (remplacée en 2013), la contribution de 5 % sur l'IS (2011-2012, reconduite puis relevée), la TRS (doublement pérenne) et la CRI (prorogée en 2024). Pour la CEHR, la durée n'est pas vérifiée. Il revient à l'intégrateur de choisir l'indicateur du test (écart de la première année, ou recette encore perçue à N+2).
2. **STDR** : quatre millésimes du même dispositif. Pour 2015 et 2016, l'ex ante vient d'un article de presse spécialisée qui rapporte les propos du secrétaire d'État, sans document ; son périmètre (total ou recettes fiscales de l'État) est incertain. D'où la confiance `low`.
3. **Doublons probables avec les autres groupes.** `ce_fortune_2012` et `cehr_2012` relèvent aussi du groupe A, qui a archivé les mêmes documents (`sources/T18/A`). `ce_is_2017` et `cri_2023` relèvent aussi du groupe B. Il faut garder une seule ligne par mesure ; l'attribution aveugle choisira la règle.
4. **Effets de volume.** `contrat_generation`, `emplois_avenir_2013`, `ati_2019` et `demission_reconversion_2019` mesurent le recours à un dispositif plus qu'un effet économique. La règle « Taux de recours » pourrait leur être attribuée. Pour ATI et démission, l'ex post est un stock et l'ex ante un flux : les ratios sont indicatifs.
5. **Annonces publiées après le vote.** Le Trésor-Éco de janvier 2009 sur le CIR (comme le bilan du contrat d'avenir pour la TVA restauration, déjà présent) date d'après l'adoption de la réforme de 2008, mais d'avant toute évaluation.
6. **Ex post simulé.** `cir2008_pib` compare deux simulations de la DG Trésor : à exclure si l'on exige un effet constaté.
7. **Fraude** : les deux lignes à rendement nul (2013, 2014) sont des constats d'exécution (direction du budget, repris par la Cour), pas des évaluations contrefactuelles. C'est pourtant le type de chiffre que les programmes inscrivent comme recette de lutte contre la fraude.
8. **`realise_publie_le` en 2026** : aucune ligne retenue. Seule l'évaluation DGE du suramortissement 2019 (avril 2026) l'aurait été, mais elle est exclue faute d'annonce ex ante.

## 5. Accès aux sites

- **budget.gouv.fr** : non tenté (inaccessible selon T10a) ; les chiffrages des LFI ont été lus à travers les rapports de la Cour.
- **senat.fr** : l'étude d'impact du projet de loi n° 717 a été obtenue avec `curl -A "Mozilla/5.0"`. Selon un autre groupe, un User-Agent Firefox complet est parfois nécessaire.
- **vie-publique.fr** : renvoie d'abord une page de redirection JavaScript ; il faut suivre l'URL `/redirect_...` avec les cookies.
- **assemblee-nationale.fr** : lent (plus de 100 s par PDF) ; plusieurs numéros devinés renvoient 404 (pl0122, pl0147-0149, l15b0382).
- **autorite-transports.fr** : 404 sur le communiqué de 2016.
- **ccomptes.fr** : non sollicité directement ; RPA 2016 obtenu sur un miroir (Dalloz Étudiant), le téléchargement a demandé plusieurs minutes.
- Recherches web : environ 22 requêtes utilisées.

## 6. Décisions laissées à l'intégrateur

1. Choisir l'indicateur du test « Recette ponctuelle » (§ 4.1) et décider si les quatre millésimes du STDR comptent pour un ou quatre cas.
2. Dédoublonner avec les groupes A et B (§ 4.3).
3. Garder ou non les lignes `low` (`stdr_2015`, `stdr_2016`, `cir2008_pib`, `ati_2019`, `demission_reconversion_2019`) et les effets de volume (§ 4.4).
4. Vérifier la durée réelle de la CEHR avant d'utiliser `cehr_2012` pour la question de la durée.
5. Pistes de reprise pour atteindre 15 effets : fiscalité du tabac 2018-2020 (OFDT) ; évaluation préalable du suramortissement 2019 ; objectif Duflot et référé de la Cour de 2018 ; annonces d'emplois de la réforme de l'assurance chômage 2019.
