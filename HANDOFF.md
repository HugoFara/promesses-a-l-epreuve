# Backtest des chiffrages budgétaires : document de passation

Destinataire : agent d'implémentation. État au 14 octobre 2026. La version du 12 octobre est conservée dans `../backtest-chiffrages.zip`.

## 1. Objectif

Construire une méthode reproductible pour évaluer la crédibilité budgétaire des programmes de la présidentielle 2027. On calibre des corrections sur l'histoire : on compare les chiffrages annoncés de mesures passées à leur coût réel, puis on applique les écarts observés aux programmes actuels. Le traitement est identique pour tous les partis.

Le 14 octobre, les tâches T1, T2, T4, T5, T6, T8, T9 et T10 ont été traitées (section 7), puis un audit indépendant (`recherche/audit/rapport.md`) a relu l'ensemble : les 2 problèmes bloquants et 8 des 10 importants ont été corrigés le jour même (section 3, « Corrections de l'audit »). T3 attend la publication des programmes (LFI le 6 novembre 2026). T7 est partiel : ménages types et grille de 468 situations (simulateur « Mon foyer ») oui, déciles non.

## 2. Contenu du paquet

```
backtest-chiffrages/
├── HANDOFF.md
├── requirements.txt            pandas, numpy, pydantic
├── requirements-web.txt        playwright (contrôle du site ; facultatif en local, requis en CI)
├── .github/workflows/ci.yml    lance run_all.sh à chaque push
├── data/
│   ├── raw/                    SOURCE DE VÉRITÉ : seuls fichiers à éditer (CSV UTF-8, virgule, point décimal, LF)
│   └── *.csv                   fichiers publiés et dérivés, régénérés par run_all.sh : ne pas éditer
├── scripts/
│   ├── run_all.sh              build → calc → moteur → sensibilité → projection → distributif → web → contrôles
│   ├── schemas.py              schémas pydantic de chaque fichier de data/raw/
│   ├── build.py                valide data/raw/ (schémas, clés, références croisées) et publie data/
│   ├── calc.py                 couches 1 et 2 (+ couche1_par_cause.csv)
│   ├── moteur.py               T4 : facteurs par formule + Monte-Carlo (P10/P50/P90)
│   ├── sensibilite.py          T6 : solde par chiffreur de départ
│   ├── validation.py           indicateur de confiance : notre méthode vs chiffrages de départ, sur le passé
│   ├── projection.py           T5 : trajectoires 2026-2032 (déficit, dette, intérêts, stress +25 pb)
│   ├── distributif.py / .sh    T7 : ménages types et grille du simulateur sous OpenFisca-France
│   ├── build_web.py            génère web/complet.html (tableau de bord complet, autonome)
│   ├── test_web.py             ouvre chaque vue du site dans Chromium (2 écrans) : erreurs JS, débordement, chiffres clés vs CSV
│   ├── check_regression.py     17 valeurs de référence
│   ├── garde_fous.py           T8 : symétrie, traçabilité, double compte
│   └── appliquer_corrections.py  applique un fichier de corrections (format T2) avec historique
├── modeles/programme_2027.csv  gabarit de saisie T3 (lignes, à ajouter à data/raw/application_lignes.csv)
├── modeles/programme_2027_entete.csv  gabarit T3 (une ligne par programme, à ajouter à data/raw/application_programmes.csv)
├── recherche/<tâche>/          rapports et extractions des agents (rapport.md, CSV, sources.csv)
├── sources/<tâche>/            ≈270 documents archivés (≈350 Mo), NON versionnés (.gitignore) ; URL, date et sha256 dans
│                               recherche/*/sources.csv ; contrôle : python3 scripts/verifier_sources.py
└── web/
    ├── index.html, site.css, site.js   site public en vues séparées (écrit à la main, lit les CSV de data/)
    ├── vendor/                 d3 7.9.0 en copie locale (intégrité vérifiée sur le registre npm), avec sa licence
    ├── dashboard_page.html     page du tableau de bord pour l'artifact claude.ai
    └── complet.html            tableau de bord complet, version autonome (générée)
```

Lancer `bash scripts/run_all.sh` : tout doit afficher OK et « garde-fous : 0 erreur(s) ». Le contrôle du site (`test_web.py`) est sauté si Playwright est absent, sauf avec `TEST_WEB_STRICT=1` (activé en CI). Le mode strict (statut de référence obligatoire) est activé par défaut ; `STRICT_REFERENCE=0` le désactive.

**Historique (règle 5).** Toute modification d'une valeur existante est inscrite dans `data/raw/historique.csv` (date, fichier, id, colonne, ancienne valeur, nouvelle, raison, source). Ce journal tient lieu de la colonne `valeur_precedente` demandée en T2. `appliquer_corrections.py` refuse une correction si la valeur actuelle ne correspond pas à l'ancienne valeur annoncée.

**Site local.** Depuis la racine : `python3 -m http.server 8000`, puis ouvrir http://localhost:8000/web/. Le site public répartit le contenu en vues adressables (`#/hier`, `#/programmes`, `#/equilibre`, `#/foyer`, `#/demain`, `#/methode`, `#/lexique`) : encadré « En bref » en langage courant, graphiques avec tableau de données équivalent, détail expert dans des accordéons, paramètres d'affichage (thème, taille du texte). Apparence inspirée des sites publics, sans en reprendre les signes distinctifs (ni Marianne, ni bloc-marque) ; un bandeau rappelle que le site est indépendant. Tous les chiffres viennent des CSV (`SOURCES` dans `web/site.js`). Accessibilité : audit WCAG 2.2 AA du 14/10 (`recherche/audit/accessibilite.md`) ; `test_web.py` lance axe-core (`scripts/vendor/`) sur chaque vue, aux deux tailles d'écran et dans les deux thèmes. Les choix faits dans une vue s'écrivent dans l'adresse (`#/foyer?statut=retraite&composition=couple_2`, seuls ceux qui diffèrent du défaut) : chaque vue a les boutons « Copier le lien de cette page » et « Imprimer » ; un lien rétablit les choix. L'impression ouvre les accordéons, passe en couleurs claires, masque navigation et boutons, et ajoute l'adresse et la date. **Accueil progressif** (14/10, après un test avec un novice : le site lui semblait technique et les graphiques intimidants, seul l'effet sur sa situation l'intéressait) : l'accueil est un simulateur minimal (statut, composition, enfants, revenu net ; sans dividendes), résultat en euros par mois avec un libellé en langage courant (`libelle_simple`) et le porteur de la mesure (`porteur`, colonnes de `distributif_reformes.csv`) ; le bouton « Affiner mon calcul » ouvre « Mon foyer » avec la même situation ; le reste du site est rangé sous « Pour aller plus loin ». Pas de présentation « par parti » tant que chaque grand parti n'a pas au moins deux mesures ménages sourcées et simulées (aujourd'hui : gouvernement et NFP seulement) ; l'accueil dit que les autres partis ne sont pas encore calculés. La vue « Mon foyer » est un simulateur : statut, composition, enfants, revenu net, dividendes ; il affiche la situation la plus proche de `distributif_grille.csv` (précalculée, rien n'est envoyé). Chaque montant corrigé (lignes des programmes et des paniers, totaux des cartes) a un bouton « Pourquoi ce chiffre ? » : chiffrage de départ et sa source, règle et ses références (`regles.csv`, élasticités, mesures du backtest), part déjà dans la référence, recoupements, fourchette P10-P90, statut de la règle (`validation_regles.csv`), et le détail du moteur (`moteur_lignes`, `moteur_regles`, `moteur_parametres`). Le tableau de bord complet (http://localhost:8000/web/complet.html) couvre 13 sections : les 8 d'origine (les sections 7 et 8 lisent désormais les montants corrigés du moteur, `moteur_lignes.csv`), puis incertitude et variantes (9), sensibilité au chiffreur (10), trajectoires 2026-2032 (11), validation (12), ménages types (13).

**OpenFisca.** `distributif.sh` utilise le clone local `../openfisca-france` (à côté du projet, version 176.1.4 rebasée sur l'upstream du 14/10/2026) et son `.venv`, recréé le 14 octobre. Si OpenFisca est absent, l'étape est sautée.

## 3. Démarche et résultats

### Conventions

- Montants en Md€ par an, à l'horizon indiqué (2027 par défaut).
- **Signe** : impact sur le solde public. Négatif = creuse le déficit.
- **Facteur total** = `facteur` (règle de comportement) × `facteur_reference` (part de la mesure qui n'est pas déjà dans la référence).
- **Confiance** : `high` = lu sur la source primaire ; `medium` = source secondaire, avec la raison dans `note_confiance` ; `low` = estimation ou source fragile.
- **Référence 2027** = loi votée (LFI et LFSS 2026, lois antérieures) **+ PLF et PLFSS 2027 tels que déposés**. C'est la seule définition cohérente avec la cible de 5,0 % utilisée en T5 : une mesure déjà dans ces budgets est déjà dans les 5,0 %. L'application 2024 reste jugée par rapport à sa propre référence (programme de stabilité d'avril 2024) ; le statut 2027 de ses lignes est conservé dans `note_reference` pour T3.

### Couche 1 : backtest mesure par mesure (29 mesures)

`mesures_cout.csv` : 29 mesures (11 d'origine + 14 ajoutées par T10a + 3 réalisés observés d'IS et d'IR tirés de la Cour des comptes + la taxe sur les rachats d'actions de 2025, T12 ; 4 candidates en confiance low écartées : Pinel, MaPrimeRénov', redevance, assurance chômage 2021). Colonnes ajoutées après l'audit : `deflateur_ex_ante` (ex ante ramené à la base de prix de l'ex post : retraites 2023 × 0,901, Woerth × 1,08), `type_ex_post` (observe / administratif / reestimation), `inclus_stats` (bouclier gaz, chèque fioul et bouclier électricité exclus de la statistique principale : prix de l'énergie exogènes, ex ante déjà en exécution).

| Échantillon (`couche1_stats.csv`) | n | Erreur absolue médiane | À ±15 % |
|---|---|---|---|
| **Principal** (`inclus_stats` = 1) | 26 | **11,2 %** | 16 |
| Toutes les mesures | 29 | 12,4 % | 17 |
| Ex post réellement observés (hors administratifs et réestimations) | 20 | 14,4 % | 11 |

Les cinq ex post « administratifs » (IS, taxe d'habitation 20 %, impôts de production, pacte, heures sup. IR) sont des chiffrages à comportement constant, mécaniquement proches de l'ex ante : ils tirent la médiane vers le bas. Le chiffre honnête pour une mesure réellement évaluée est plutôt **14 %**.
- **Par cause** (`couche1_par_cause.csv`) : coûts mécaniques à barème ≈2,5 % d'erreur ; comportement (PFU, CIR, CITE) ≈55 % ; énergie et conjoncture 12 à 48 % ; taux de recours dans les deux sens (prime d'activité sous-estimée ; chèques énergie et fioul surestimés).
- **Effets promis** (`mesures_effets.csv`, 15 lignes) : CICE 0,29 ; TVA restauration 0,49 (emplois) ; TEPA, ISF et PFU sur l'investissement 0. Exception : les réformes des retraites ont plus relevé l'emploi des seniors que prévu.

### Couche 2 : biais des trajectoires

Inchangé sur le fond, mais les 21 programmes de stabilité sont désormais tous en confiance high (2012, 2014, 2016 confirmés sur la Commission et l'Assemblée) et les valeurs réalisées ont été recoupées avec Eurostat (avril 2026) : aucun écart > 0,05 point. Biais hors crises : **−0,60 point à 1 an, −1,93 point à 3 ans** ; 15 programmes sur 15 trop optimistes à 3 ans. L'European Fiscal Board donne des ordres de grandeur cohérents (−0,40 / −1,85 hors crises, réalisé en première publication).

### Couche 3 : élasticités

75 estimations (62 + 13 lues sur sources primaires par T2b : Saez-Slemrod-Giertz 0,12-0,40, Colombie, Norvège, Suède, CNEPI, Bozio-Wasmer par tranche de salaire, Carbonnier, Mésange lu à la source, non-recours CSS et CMU-C). Colonnes numériques `val_bas`, `val_central`, `val_haut`, `unite`, `type`. 71 high, 4 medium (raison dans `note_confiance`).

### Moteur de correction (T4)

`moteur.py` calcule chaque facteur par formule (`moteur_regles.csv`) à partir de paramètres sourcés (`moteur_parametres.csv`, qui renvoient à `elasticites.csv`, au backtest ou à `parametres_bareme.csv`, 131 paramètres de barème lus par T4p). Chaque paramètre est tiré une fois par simulation et partagé par tous les partis. Chaque ligne reçoit en plus une erreur de chiffrage de médiane absolue 14,9 % (instituts, T10b), dont la moitié est commune à toutes les lignes d'un même chiffreur (hypothèse `part_commune_erreur`, non mesurée). Les facteurs de référence et d'interaction sont tirés dans leur intervalle documenté (bandeaux [0,09 ; 0,87], Zucman [0,3 ; 1]…). Une même mesure reçoit le même tirage dans toutes les variantes.

| Règle | Forfait | Moteur | Formule et paramètres |
|---|---|---|---|
| Élasticité capital | 0,45 | 0,437 | taxe t0 = 35,4 % (PFU 31,4 % + CEHR) → t1 = 46,27 % (barème), ε = 0,77 |
| Élasticité IS | 0,94 | 0,94 | paramètre direct `facteur_is` : surtaxe 2025 encaissée à 94 % de son chiffrage (Cour des comptes) ; fourchette de 0,73 (formule de moyen terme : 1 − 0,8 %/pt × (25,83 + 7,73)) à 1 (aucune réaction) |
| Élasticité patrimoine | 0,97 | 0,97 | 1 − perte de rendement à 3 ans : 3 % (ISF→IFI, backtest), de 1,2 % (départs nets) à 13 % (long terme étranger) ; affaiblie après validation (ancien forfait 0,85) |
| Élasticité carburants | 0,70 | 0,73 | accise : ε = −0,3, hausse de prix 32-47 % pondérée par niche, accise existante 1,27 × la hausse |
| Effet emploi du SMIC (ligne propre) | 0,87 Md€ | 0,87 Md€ | emplois perdus (Dube : 53 900 ; jusqu'à 380 000 selon Montaigne) × 16 k€ |
| Effet promis | 0,333 | 0,29 | mode = CICE ; de 0 (TEPA, ISF, PFU) à 1,1 (OFCE) — écart justifié |
| Réforme structurelle | 0,80 | 0,84 | à prix constants : retraites 2023 (0,82) et 2010 (0,86) |
| Revenus, successions | 0,90 | forfait | barème proposé (t1) non publié |

Critère T4 rempli : toutes les valeurs centrales sont à ±10 % des forfaits, sauf « effet promis » (−13 %, justifié). Le scénario `INCERTITUDE_LARGE=1` prend l'erreur de Montaigne seul (40 %).

### Application aux programmes de 2024

| | Somme indépendante | Corrigé (forfaits) | Moteur central | Moteur P10 / P50 / P90 |
|---|---|---|---|---|
| NFP 2024 | −150,5 | −159,5 | −160,0 | −203 / −154 / −105 |
| Ensemble 2024 | −18,1 | −25,5 | −25,7 | −31 / −25 / −19 |

La médiane des niches reste à 14 : la seconde ligne de 5 du tableau iFRAP porte un astérisque (montant repris du parti) et n'est pas un chiffrage indépendant.

### Sensibilité au chiffreur (T6, `sensibilite_chiffreurs.csv`)

Seuls Montaigne et l'iFRAP chiffrent les deux programmes ligne à ligne. Asterès reprend les recettes du parti (scénario à part) ; « Terra Nova » est en fait une note Chancel-Delatte-Huillery publiée par La Grande Conversation (recettes seules) ; l'OFCE ne donne que des morceaux.

| Programme | Chiffreur | Solde publié | Lignes propres → corrigé | Complété (médiane des autres) → corrigé |
|---|---|---|---|---|
| NFP | Montaigne | −179 | −179,0 → −181,8 | −142,5 → −151,9 |
| NFP | iFRAP (hors ligne reprise du parti) | −160,4 | −165,3 → −156,9 | −152,8 → −144,4 |
| NFP | La Grande Conversation | recettes seules | +90,0 → +83,0 | −135,0 → −132,3 |
| NFP | Asterès (recettes du parti) | −50 | −55,7 → −80,4 | −72,8 → −92,7 |
| Ensemble | Montaigne | −20,6 | −20,6 → −26,0 | −18,1 → −25,5 |
| Ensemble | iFRAP | +4,0 | +4,0 → −2,3 | −2,1 → −9,6 |

**Les corrections ne réduisent pas l'écart entre chiffreurs** (NFP : 17,8 Md€ avant, 19,6 après ; Ensemble : 16,0 → 15,9). L'écart vient du périmètre (retraites de −9,5 à −74 ; ISF de 3,5 à 22,5 ; recettes du parti reprises ou non : 76 Md€), pas du comportement. Le chiffreur de départ reste le premier facteur d'incertitude.

### Paniers à l'équilibre (référence 2027)

| Variante | Mesures phares | Financement | Solde central (moteur) | P10 / P50 / P90 | Loi votée seule | Variante « dégel » |
|---|---|---|---|---|---|---|
| LFI intégral | −111,2 | +39,2 | **−72,0** | −87 / −68 / −49 | −67,3 | −96,6 |
| LFI ajusté (hors 30 Md€ d'investissement emprunté) | −32,0 | +39,2 | **+7,2** | +2 / +8 / +14 | +11,9 | −17,3 |
| Ensemble | −14,7 | +7,5 | **−7,0** | −11 / −7 / −4 | −1,6 | −7,0 |

**Le résultat LFI dépend surtout du SMIC.** La référence 2027 contient le gel du SMIC de référence des allègements (voté pour 2026, proposé pour 2027). Par symétrie avec la décote des bandeaux d'allègements, qui invoque ce même gel, le SMIC à 1 600 € n'augmente plus les allègements : son coût statique (−19 selon Montaigne, dont −21,5 d'allègements) devient +2,3, plus une ligne d'effet emploi (−1,7 : 103 500 emplois, T13). Si au contraire la hausse du SMIC s'accompagne d'un dégel (variante « dégel », `variantes_sensibilite.csv` : coût −24,7 et bandeaux à 0,715), LFI ajusté passe de +7,2 à −17,3. **Les deux lectures sont cohérentes ; le programme LFI 2027 devra dire laquelle s'applique.**

Autres effets de la référence 2027 : surtaxe d'IS déjà au PLF 2027 (facteur de référence 0,286, puis 1 dès 2028 car la surtaxe de la référence n'est reconduite qu'un an) ; bandeaux d'allègements en partie rabotés (0,5, statique 11,4 après effets emploi) ; sous-indexation des pensions et abattement des retraités déjà au PLF 2027 (0) ; Zucman décoté de 35 % pour son interaction avec l'ISF, l'IR et la fin du PFU du même panier (impôt plancher, PPL 768). La variante « loi votée seule » ne décote pas les mesures seulement proposées (+3,7 pour LFI, +5,4 pour Ensemble). La taxe renforcée sur les rachats d'actions (8,4 statiques, calcul de l'auteur de l'amendement sur les rachats du CAC 40 de 2024) reçoit depuis T13 une règle propre : 85 % de l'assiette perdue au central (report vers les dividendes, extrapolé de la taxe américaine de 1 %), moins la taxe existante de 0,2, soit **1,06 Md€** net (P10-P90 0,6-2,7 ; confiance low).

### Projection 2026-2032 (T5, `projection.csv`)

Trajectoire du gouvernement (PLF 2027 et trajectoire communiquée au HCFP) : déficit 5,4 % (2026), 5,0 % (2027), 3,9 % (2028), 2,8 % (2029) ; PIB en valeur publié pour 2026 et 2027 (3 051 et 3 135 Md€, dossier de presse p. 53) ; 2030-2032 extrapolés (solde 2029 maintenu, colonne `extrapole`). Critère T5 rempli : à partir des déficits et des ajustements stock-flux du HCFP (+0,5 pt en 2026 et 2027), la dette calculée retrouve 119,3 % (2026) et 121,6 % (2027) pour 121,7 % publié (écart d'arrondi).

| Scénario | Déficit 2027 | 2029 | 2032 | Dette 2032 |
|---|---|---|---|---|
| Référence du gouvernement | 5,0 | 2,8 | 2,8 | 120,3 |
| Référence corrigée du biais | 5,6 | 4,8 | 5,1 | 130,3 |
| Panier LFI intégral | 7,9 | 7,3 | 8,1 | 144,8 |
| Panier LFI ajusté (dont 1,0 pt d'investissement emprunté) | 6,3 | 5,5 | 6,1 | 134,8 |
| Panier Ensemble | 5,8 | 5,1 | 5,4 | 131,8 |

Depuis l'audit : l'emprunt « règle d'or » entre dans le déficit et la dette (colonne `dont_investissement_pct`) ; l'impact de chaque ligne suit son facteur de référence de 2028 (`corrige_2028`) ; chaque tranche refinancée garde le spread de son année. Le stress +25 pb ajoute environ 0,2 point de déficit et 0,7 point de dette en 2032. Montée en charge (T14, `montee_en_charge.csv`) : le coût de l'abrogation de la réforme 2023 double en part du PIB entre 2027 et 2032 (`l_ret62`), celui du retour à 60 ans augmente de 11 % (`l_ret60`) ; les autres lignes restent constantes en % du PIB. Le HCFP juge la croissance 2027 « optimiste » et le retour sous 3 % en 2029 « très peu vraisemblable ».

### Corrections de l'audit indépendant (14 octobre)

Appliquées (détail et preuves : `recherche/audit/rapport.md`, chaque changement dans `historique.csv`) : emprunt d'investissement dans la dette (bloquant) ; traitement symétrique du gel des allègements entre `l_smic` et `l_bandeaux` (bloquant) ; formule de l'IS ; interaction Zucman ; suspension des retraites lue comme un niveau (1,9) et non un incrément (1,0) : `l_ret62` −6,4, `l_ret60` × 0,967 ; niches iFRAP à 5 ; montée en charge partielle (surtaxe 2028) ; erreur commune par chiffreur et intervalles des facteurs de référence ; recette existante des rachats d'actions déduite ; bases de prix et exclusions en couche 1 ; bandeaux à 11,4 ; règle unique « milieu de l'intervalle documenté » pour les recoupements non chiffrés (e_appr 0,67) ; variante « loi votée seule ».

Appliquées le 14/10 au soir (T13, `recherche/T13/rapport.md`) : règle propre pour la taxe sur les rachats d'actions ; effectif 1-1,15 SMIC et élasticité française de l'emploi au coût. Appliquées ensuite (T14, `recherche/T14/rapport.md`) : montée en charge des retraites dans la projection (`montee_en_charge.csv`) ; formule accise symétrique pour `e_elec` (facteur 0,92). Derniers points traités le 14/10 : `statut_reference_2027.csv` garde les propositions de T1, mais chaque écart avec les facteurs en vigueur (10 lignes des paniers) est expliqué dans la colonne `raison_ecart`, et `garde_fous.py` refuse un écart non expliqué ; biais signés : `biais_residuels.csv` (voir Validation) ; PPV (`e_prime`) : le chiffrage Montaigne révisé (2 Md€) intègre déjà l'aubaine (substitution 0,3), règle « Aucune » maintenue. Tous les points de l'audit sont traités ou tranchés.

### Validation de la méthode (indicateur de confiance, 14 octobre au soir)

Question : notre chiffrage corrigé est-il plus proche du réalisé que le chiffrage de départ ? Règles attribuées à l'aveugle par un agent séparé (sans le réalisé), facteurs calibrés recalculés sans la mesure testée. Protocole et limites : `recherche/validation/README.md` ; code : `scripts/validation.py`.

| Règle | Statut | Résultat |
|---|---|---|
| Effet promis | **confirmée** | 6 améliorations, 2 dégradations ; erreur médiane 61 % → 29 % |
| Élasticité capital | **confirmée** | PFU : erreur 55 % → 1 % (élasticité estimée avant 2018) |
| Substitution retraites | **confirmée** | 2 sur 2 ; 16 % → 4 % |
| Taux de recours | non testée (restreinte) | la version d'origine dégradait les 4 chiffrages officiels (prime d'activité 2016 et 2019, CIR, CITE), qui intégraient déjà un recours partiel. **Restreinte** aux chiffrages qui supposent un recours complet (colonne `recours_complet_suppose`, contrôlée par les garde-fous) ; c'est le cas de la garantie d'autonomie chiffrée par Montaigne (`recherche/recours/rapport.md`) |
| Réforme structurelle | mitigée | 1 sur 2 |
| Élasticité patrimoine | confirmée (faiblement) | avec 0,85 : 5 dégradations sur 5 ; **affaiblie à 0,97** : 3 améliorations, 2 dégradations, erreur 3 % → 2 % (recalculé sans ISF→IFI). La règle ne corrige presque plus rien |
| Élasticité IS | contredite (1 cas) | réalisés observés (Cour des comptes, `recherche/IS/rapport.md`) : surtaxe 2025 −6 % (8,0 → 7,5 d'acomptes), surtaxe de 5 % en 2013 +50 % (0,8 → 1,2). L'ancienne règle (0,73) prévoyait −27 %. **Remplacée par une décote faible (0,94)** calibrée sur 2025 ; recalculée sans 2025, il ne reste que 2013, qu'aucune décote ne peut rapprocher : la règle n'est pas confirmable avec deux cas |
| Élasticité revenus | confirmée (faiblement) | un seul cas : CDHR 2025 attendue à 2,0, 0,4 encaissé (acompte) ; la règle (0,9) ne corrige que 10 points d'un écart de −80 % |
| Nouvelle assiette : risque juridique | contredite (1 cas) | taxe sur les rachats d'actions 2025 (T12, attribution à l'aveugle par un 3e agent, issue inconnue de lui) : 0,4 prévu, 0,5 encaissé ; la décote de 0,8 donne 0,32 (erreur 25 % → 41 %). Règle appliquée à la taxe Zucman (`l_zucman`), non modifiée sur un seul cas |
| Successions, carburants | non testées | aucune mesure passée comparable |

Sur la statistique principale des chiffrages officiels (26 mesures), l'erreur médiane passe de 11,2 % à 10,2 %, mais l'erreur moyenne monte (20,2 % → 23,9 %) : la méthode ne fait pas nettement mieux que le départ : elle ne change rien aux coûts mécaniques, qui sont la majorité, et ses gains (comportement du capital, effets promis, retraites) sont compensés par les règles mitigées ou contredites.

**Part des corrections reposant sur une règle confirmée** (`confiance_programmes.csv`) : NFP 2024 29 %, Ensemble 2024 92 %, panier LFI intégral 37 %, LFI ajusté 8 %, Ensemble 0 %. LFI ajusté chute depuis T13 : sa principale correction confirmée (Élasticité capital sur les rachats) est remplacée par une règle propre, non testable faute de précédent. La correction la plus lourde du panier LFI qui ne soit pas confirmée est la garantie d'autonomie (taux de recours, +4,3 Md€) ; celle d'Ensemble est la décote de mise en œuvre de ses économies (−0,9).

**Biais signés résiduels** (`biais_residuels.csv`, sens du solde : + = mieux que prévu) : après correction, le biais **médian** est nul (+0,1 % pour les chiffrages officiels comme pour les instituts) ; l'erreur centrée du Monte-Carlo est donc justifiée pour la médiane. La **moyenne** reste négative (officiels −0,4 % au départ, −4,9 % après correction ; instituts −10,4 % et −12,3 %) : quelques gros ratés défavorables (taux de recours, réforme structurelle, CDHR) forment une queue asymétrique que les règles ne réduisent pas, et que les échantillons par règle (1 à 4 cas) ne permettent pas de corriger.

**Limites** : l'agent connaissait l'issue de 60 cas sur 83 (le 3e agent ne connaissait pas celle des rachats) ; échantillons très petits par règle (1 à 8) ; les règles les plus influentes pour 2027 (revenus, successions, nouvelle assiette Zucman) n'ont au mieux qu'un précédent.

**Décisions appliquées le 14/10** : « Taux de recours » restreinte aux chiffrages à recours complet (vérifié pour Montaigne : tous les éligibles au montant plein) ; « Élasticité patrimoine » affaiblie à 0,97. **Décision appliquée** : décote faible pour l'IS (0,94, fourchette 0,73-1). **À surveiller** : les soldes 2025 de la surtaxe et de la CDHR (déclarations de 2026), qui confirmeront ou non les acomptes.

### Effets distributifs (T7, `distributif_menages.csv`, `distributif_grille.csv`)

| Ménage type (législation 2026) | SMIC 1 600 € net | Gel des pensions > 1 281 € | Abattement retraités plafonné à 3 000 € | Fin du PFU |
|---|---|---|---|---|
| Salarié au SMIC, célibataire | +1 293 €/an | 0 | 0 | 0 |
| Couple de retraités (2 000 + 1 300 € bruts) | 0 | −521 €/an | −126 €/an | 0 |
| Cadre (4 SMIC, 5 000 € de dividendes) | 0 | 0 | 0 | −260 €/an |
| Famille monoparentale, 1 enfant, SMIC | +1 403 €/an | 0 | 0 | 0 |

**Correction du 14/10 (soir)** : les revenus n'étaient renseignés que pour 2026. Or OpenFisca lit ceux de l'année N-2 (taux de CSG des pensions selon le RFR 2024) et du trimestre précédent (prime d'activité, ASPA) : tous les retraités étaient exonérés de CSG, le couple de retraités touchait 2 140 € d'ASPA fictifs et la prime d'activité du salarié au SMIC était surestimée (3 338 € au lieu de 2 847 €). Hypothèse désormais : situation stable (mêmes revenus en 2024, 2025, 2026) et réformes appliquées sur les trois années (régime permanent). Anciens chiffres : SMIC +1 366 / +1 476, gel −550, abattement −154.

**Choix PFU / barème** : la situation de départ donne à chaque foyer le plus avantageux des deux (case 2OP, déjà permise) ; sans cela la suppression du PFU « faisait gagner » 225 situations de la grille. Le choix reste figé pour les autres réformes.

**Grille du simulateur** (`distributif_grille.csv`, 468 situations × 4 réformes, une simulation OpenFisca par réforme) : actifs (seul, couple à deux revenus, couple à un revenu ; 0 à 3 enfants ; 0,5 à 6 SMIC) et retraités (mêmes compositions, sans enfants ; pensions de 900 à 5 000 € bruts), dividendes 0, 2 000, 10 000 ou 50 000 €/an. Hausse du SMIC : salariés au SMIC horaire, y compris à temps partiel, sans effet de diffusion. Un effet de seuil réel apparaît : le gel fait *gagner* 631 € au couple à une pension de 2 000 € bruts, dont le RFR passe sous le seuil d'exonération de CSG.

Ménages types et grille = conventions (multiples du SMIC, montants ronds, pas de loyer ni d'aide au logement). Le critère T7 (reproduire un résultat par décile) n'est pas atteint : il faut une microsimulation sur données d'enquête (ERFS via le CASD). Un serveur OpenFisca (`openfisca serve`) permettrait un simulateur libre, mais imposerait un hébergement : la grille précalculée garde un site statique.

## 4. Schéma des données (data/raw/)

| Fichier | Clé | Rôle |
|---|---|---|
| `mesures_cout.csv`, `mesures_effets.csv` | `id` | Couche 1 (+ citations et pages ex ante / ex post pour les ajouts T10a) |
| `programmes_stabilite_fr.csv`, `pairs_frankel_schreger.csv` | `millesime`, `pays` | Couche 2 (Frankel-Schreger : positif = optimiste) |
| `elasticites.csv`, `hypotheses_defaut.csv` | `id` | Couche 3 (colonnes numériques T4) |
| `regles.csv` | `regle` | Facteur forfaitaire de chaque règle, fixe ou variable, avec ses références |
| `regles_calibration.csv` | `id` | Règles qualitatives de lecture |
| `moteur_regles.csv`, `moteur_parametres.csv` | `regle`, `id` | Formules et paramètres du moteur |
| `parametres_bareme.csv` | `id` | 131 paramètres de barème 2024-2027 (T4p) |
| `application_lignes.csv`, `application_programmes.csv`, `application_parametres.csv` | `id` | Application 2024 |
| `paniers.csv` | `id` + `variantes` | Une ligne par mesure, variantes séparées par `;` (publiée dépliée dans `data/paniers.csv`) |
| `statut_reference_2027.csv` | (`fichier`, `id_ligne`) | Statut de chaque ligne par rapport à la référence 2027 (T1) |
| `chiffrages_instituts.csv`, `totaux_instituts.csv`, `ifrap_nfp_2024.csv` | — | Chiffrages par institut (T6, T2a) ; `usage` : ligne / recettes_du_parti / composante / hors_lignes / partisan |
| `calibration_instituts.csv` | — | Chiffrages de campagne 2017/2022 vs coûts réalisés (T10b) |
| `rendements_leviers.csv` | `id` | Rendements sourcés de leviers génériques (point de CSG 17,8 Md€, TVA restauration à 20 % 2,1, carbone 1,8 par 10 €/t…) |
| `projection_reference.csv`, `projection_parametres.csv` | `annee`, `id` | T5 |
| `distributif_reformes.csv` | `id` | Réformes simulées sous OpenFisca (T7) |
| `historique.csv` | — | Journal des modifications |

## 5. Règles de correction en vigueur

Voir `data/raw/regles.csv` (facteurs forfaitaires, utilisés par les garde-fous et la non-régression) et `moteur_regles.csv` (formules). Changement du 14 octobre : la règle mixte « Déjà en partie dans la référence » n'est plus utilisée ; la part déjà votée passe par `facteur_reference`, et la ligne garde sa règle de comportement.

## 6. Limites connues

### Sources

- **Inaccessibles en automatique** : budget.gouv.fr (Incapsula), Légifrance (téléchargement), performance-publique, cepr.org (403), Dares et DREES (pare-feu anti-robot), une partie de senat.fr. Depuis le 14 octobre au soir, ces sites sont lus avec le navigateur Chrome (`recherche/T2c/rapport.md`) : PDF lus dans la page avec pdf.js et sha256 calculé dans la page, sans contourner les protections ; fiches d'extraits datées dans `sources/T2c/` quand le document ne peut pas être téléchargé.
- **Quota de recherche web** de la session (200 requêtes partagées) épuisé en fin de journée : non-recours APL et AAH, rapports EFB, document Lefebvre-Lehmann-Sicsic, évaluations préalables du PLF 2018 (annexe elle-même) restent à lire.
- **Non trouvés** : chiffrage de L'Avenir en commun 2022 ; effet des heures sup. 2019 sur les heures travaillées ; évaluation officielle d'une taxe renforcée sur les rachats d'actions ; barèmes NFP de l'IR à 14 tranches et des successions ; budget vert du PLF 2027 ; dette 2028-2030 ; rendement du Dutreil restreint (LFI 2026 art. 8).
- **Lignes encore fragiles** : `l_rachats` (low) ; `nfp_taux`, `ens_taux` (calculs, low) ; 8 lignes de paniers et 10 mesures de la couche 1 en medium, raison dans `note_confiance`. Les évaluations préalables des PLF 2015, 2020 et 2021 ont été lues le 14/10 (T12, `recherche/T12/rapport.md`) : elles confirment les ex ante repris de seconde main, `ip_2021` passe en high ; les 10 restantes le sont pour des raisons propres à l'ex post (sommes calculées, microsimulation) ou faute de document (CIR 2008 : pas d'évaluation préalable avant 2010).

### Choix méthodologiques discutables

1. **Le chiffreur de départ décide du résultat** (T6) : les corrections ne réduisent pas la dispersion.
2. **Référence 2027 = budgets déposés.** Si le Parlement modifie le PLF (l'abattement des retraités a été supprimé en commission le 9 octobre, la séance repart du texte du gouvernement), les facteurs de référence changent. Avec la loi votée seule, les lignes « proposées » repasseraient à 1.
3. **SMIC et gel des allègements** : résultat LFI très sensible (LFI ajusté de +7,2 à −17,3 selon le gel ou le dégel). Emplois perdus (T13) : 103 500 au central (élasticité française −0,6 × hausse moyenne de 6,9 % × 2,5 M de salariés entre 1 et 1,15 SMIC), de ≈29 000 (Dube) à 389 000 (diffusion complète, −0,9, 3 M) ; Montaigne 230 000 à 380 000.
4. **Suspension des retraites** : 1,9 Md€ en 2027 retenu (lettre rectificative 1,4 + amendement 0,5) ; le 1,0 du PLFSS 2027 est un incrément d'une année sur l'autre. Le 8,3 de l'iFRAP (rendement de la réforme) n'est pas archivé.
5. **Bases de prix** : corrigées par `deflateur_ex_ante` pour retraites 2023 et Woerth (déflateurs approchés : ≈1,75 %/an ; ≈+8 % de 2008 à 2016).
6. **Ex post administratif** : 5 mesures (marquées `type_ex_post = administratif`) ; la statistique sur ex post observés seulement est publiée à côté (13,1 %).
7. **Pas de bouclage macro** dans le solde (les multiplicateurs Mésange sont dans `elasticites.csv` mais pas utilisés) ; la projection n'a pas d'effet du programme sur la croissance.
8. **Projection** : 2030-2032 extrapolés ; biais tenu constant au-delà de 3 ans ; montée en charge seulement pour les deux lignes de retraites (coefficient central, profil calculé ; aucune ligne d'Ensemble profilée) ; `part_commune_erreur` = 0,5 est une hypothèse.
9. **Distributif** : ménages types seulement ; pas de déciles.

## 7. État des tâches et suite du travail

| Tâche | État au 14/10 | Reste à faire |
|---|---|---|
| T1 Référence 2027 | **Fait** : 68 lignes avec statut (aucune inconnue), `facteur_reference`, paramètres du PLF 2027 | Suivre le vote du PLF/PLFSS 2027 (abattement des retraités, surtaxe, holdings) et mettre à jour `statut_reference_2027.csv` |
| T2 Sources primaires | **Largement fait** : couche 2 entièrement high ; 74/75 élasticités high ; sources « navigateur » lues (T2c : cepr.org, Dares, DREES, Persée, Cour des comptes, budget.gouv.fr) | 10 mesures de la couche 1 et 8 lignes de paniers en medium (section 6 ; T12 a lu les évaluations préalables disponibles) |
| T3 Programmes 2027 | **Prêt** : gabarits `modeles/programme_2027.csv` (lignes) et `programme_2027_entete.csv` (programme : `scrutin` = « Présidentielle 2027 », référence `prevision_2027_actuelle` + `biais_t1`, car le PLF 2027 est à 1 an de 2027) ; garde-fous, sensibilité et site s'appliquent automatiquement (le site affiche l'élection la plus récente, avec un sélecteur d'élection et des cases à cocher au-delà de deux programmes) | Saisir LFI 2027 dès le 6/11, puis les autres ; faire auditer par un agent indépendant |
| T4 Moteur | **Fait** (critère rempli) | Barèmes IR et successions dès qu'un parti les publie ; distribution des dividendes par tranche (DGFiP) |
| T5 Projection | **Fait** (critère rempli) ; montée en charge des retraites ajoutée (T14) | Profils d'autres lignes si documentés ; propager les bornes ; bouclage macro (multiplicateurs Mésange) ; trajectoire 2030+ si publiée |
| T6 Sensibilité | **Fait** | Ajouter les chiffreurs des programmes 2027 |
| T7 Distributif | **Partiel** | Mesures ménages sourcées pour chaque grand parti (RN, LR, Ensemble, gauche), puis accueil « par parti » ; déciles : accès ERFS (CASD) ou maquette publique ; reproduire un cas type publié ; refaire tester l'accueil par 2-3 novices |
| T8 Garde-fous | **Fait** ; CI prête (dépôt git à créer) | — |
| T9 Pipeline | **Fait** : données dans `data/raw/`, schémas pydantic, 257 sources archivées avec sha256 | — |
| T10 Backtest | **Fait** : 29 mesures ; calibration par institut (aucun biais significatif, n ≤ 8) | Recalculer à périmètre et base de prix identiques ; sortir les ex post administratifs |
| T11 Tableau de bord (nouveau) | Fait le 14/10 : sections 9 à 13 (moteur, sensibilité, projection, validation, distributif) ; sections 7-8 sur le moteur | Déciles quand T7 sera fait ; mettre à jour l'artifact claude.ai seulement sur demande |
| T12 Rachats d'actions et évaluations préalables (nouveau) | Fait le 14/10 : taxe sur les rachats ajoutée à la couche 1 (0,4 prévu par la LFI 2025, 0,5 encaissé) ; évaluations préalables PLF 2015, 2020, 2021 lues (`recherche/T12/rapport.md`) | Évaluation préalable PLF 2018 (IS) sans objet ; dossier de presse PLF 2008 introuvable |
| T14 Retraites et électricité (nouveau) | Fait le 14/10 : montée en charge de `l_ret62` (×2,0 en 2032) et `l_ret60` (×1,11) ; accise symétrique sur l'électricité (Ensemble −7,2 → −7,0) (`recherche/T14/rapport.md`) | Chiffrage officiel de la suspension après 2027 ; élasticité de court terme de l'électricité |
| T13 SMIC et rachats (nouveau) | Fait le 14/10 : effet emploi du SMIC recalculé (103 500 emplois, −1,67 Md€) ; règle propre des rachats d'actions (1,06 Md€ net au lieu de 3,6) (`recherche/T13/rapport.md`) | Effectif 1-1,15 SMIC à confirmer si la Dares le publie ; taux de 33 % hors de tout échantillon observé |

**Calibration par institut (T10b)** : Montaigne n = 8, biais moyen −34 % (IC 95 % [−108 ; +39]) ; OFCE n = 5, +2 % [−19 ; +23] ; Fondation Concorde n = 5, +5 % [−30 ; +39]. Aucun facteur par institut n'est appliqué ; l'erreur absolue médiane (14,9 % tous instituts, 40 % pour Montaigne seul) sert d'incertitude par ligne.

## 8. Tableau de bord publié

L'artifact privé (claude.ai) n'a **pas** été mis à jour le 14 octobre (règle de l'utilisateur : pas de publication en ligne sans demande explicite). Il montre encore les données du 12 octobre. Les versions locales (`web/index.html`, `web/complet.html`) lisent les CSV à jour. Pour republier `dashboard_page.html`, il faudrait joindre à l'artifact les nouveaux CSV, y compris ceux du moteur, de la projection, de la validation et du distributif (liste `SOURCES` de `scripts/build_web.py`).

## 9. Règles à respecter

1. **Aucun chiffre sans source lue.** URL et niveau de confiance pour chaque valeur ; une valeur dérivée est marquée comme telle (`note`, `justification`, `source_type = calcul`).
2. **Traitement symétrique.** Une règle s'applique à toute mesure du même type, quel que soit le parti (`garde_fous.py` le vérifie). Faire auditer chaque nouvelle application par un agent qui n'a pas produit le chiffrage.
3. **Séparer les faits des préférences.** Le déficit volontaire (règle d'or, investissement) est une colonne à part.
4. **Pas de double compte avec la référence** (`statut_reference`, `facteur_reference`).
5. **Garder l'historique** (`historique.csv`, `appliquer_corrections.py`).
6. **N'éditer que `data/raw/`**, jamais les CSV publiés de `data/`.
