# T21 : tester les règles qui n'ont pas, ou pas assez, de cas

Consigne préparée le 20/10/2026. Lire d'abord `recherche/CONSIGNES.md` (règles communes ; date d'accès : celle du jour), puis `recherche/validation/README.md`, `recherche/T18/CONSIGNE.md` (protocole et format, repris ici) et `recherche/T18/rapport.md`.

## Pourquoi

D'après `data/validation_regles.csv`, la plupart des règles appliquées aux programmes ne sont pas jugées :

- **jamais testées** : Effet emploi du SMIC, Taxe sur les rachats d'actions, Taux d'intérêt, Médiane des estimations, Élasticité carburants (T18 l'a jugée intestable par la recette seule), Règle d'or, Déjà dans la référence ;
- **moins de 5 cas** (seuil de `scripts/validation.py`) : Réforme structurelle, Substitution retraites, Élasticité IS, Élasticité revenus, Élasticité capital, Élasticité succession, Élasticité électricité.

T18 a cherché ces règles avec les mesures françaises de 2000 à 2025 et en a trouvé peu. Cette tâche élargit les tests possibles : mesures étrangères pour les règles sans précédent français, test du paramètre lui-même quand la règle n'est pas un simple facteur, et sources que T18 n'a pas lues.

Le résultat peut être défavorable à la méthode ; il est publié pareil. Ne pas choisir les cas selon que la règle semble marcher.

## 0. Gel des règles

| Élément | Valeur |
|---|---|
| Commit | `686902b` |
| `data/raw/regles.csv` (sha256) | `3c97911a18e888fc1faefd9b1922172f32f5dfb703e0ef57a7b50f3da8a8eccb` |
| `data/raw/moteur_regles.csv` (sha256) | `44b3fe92a754144f0995a2e676cd5d5c033f92869d8d324827488972fb3ff4b6` |

## 1. Deux sortes de tests

1. **Test d'une mesure** (comme T18) : un chiffrage avant adoption, un réalisé sur le même périmètre, une règle qui s'applique d'après la seule nature de la mesure. Format : celui de `recherche/T18/mesures_cout_nouvelles.csv`, plus une colonne `pays` (`FR` par défaut). Les exigences de comparabilité de T18 § 1 s'appliquent, en particulier `type_ex_post` :
   - `observe` : recette ou dépense effectivement constatée, pour la mesure elle-même (comptabilité, déclarations, encaissements isolables) ;
   - `reestimation` : nouveau chiffrage de l'administration ou d'un évaluateur, y compris un coût de dépense fiscale dans les Voies et moyens, sans observation directe de la mesure ;
   - `administratif` : montant budgétaire ou enveloppe reprenant la prévision.
2. **Test d'un paramètre** : quand la règle repose sur un paramètre (élasticité, spread par point de dette, part perdue), comparer le paramètre gelé (`data/raw/moteur_parametres.csv`, `data/raw/elasticites.csv`) aux estimations publiées depuis, surtout celles qui observent l'effet après coup. Format : celui de `data/raw/elasticites.csv`, plus `parametre_teste` (id du paramètre gelé) et `valeur_gelee`. Ce test ne remplace pas le premier ; il dit si le paramètre tient.

**Mesures étrangères** : admises pour les règles sans précédent français (rachats, carburants, SMIC, Taux d'intérêt), avec `pays`. Elles formeront un sous-échantillon à part, jamais mêlé sans le dire aux cas français.

## 2. Groupes

Les pistes sont à vérifier, pas des faits. Une piste sans source s'écrit « non trouvé ». Ne pas reprendre une mesure de `data/raw/mesures_cout.csv`, `data/raw/mesures_effets.csv`, `recherche/T18/mesures_cout_nouvelles.csv` ni `recherche/T20/mesures_cout_nouvelles.csv`, sauf source nouvelle qui lève le motif d'exclusion (voir `recherche/T18/parts/notes_*.md`).

| Groupe | Règles | Pistes |
|---|---|---|
| A | Élasticité carburants, Élasticité électricité | volumes constatés après les hausses de la composante carbone (2014-2018) et le gel de 2019 ; remise carburant 2022 (volumes) ; taxes carbone étrangères évaluées après coup (Suède, Colombie-Britannique, Suisse) ; accise sur l'électricité 2024-2025 (consommation constatée, CRE, RTE) ; élasticités-prix observées en France depuis 2015 |
| B | Effet emploi du SMIC, Taux d'intérêt | coups de pouce et revalorisations du SMIC, évaluations de l'effet sur l'emploi (rapports du groupe d'experts SMIC, Dares, Insee) ; hausses du salaire minimum étrangères évaluées après coup (Allemagne 2015 et 2022, Royaume-Uni) ; pour les taux : sensibilité annoncée de la charge d'intérêts à un choc de taux (AFT, PLF, programme de stabilité) contre charge constatée en 2022-2024 ; estimations publiées de l'effet de la dette sur le spread |
| C | Taxe sur les rachats d'actions, Médiane des estimations | taxe d'accise de 1 % des États-Unis (2023) : chiffrage du JCT ou du CBO contre recettes constatées (IRS, Trésor américain) ; taxes comparables (Canada 2024, autres) ; pour la médiane : campagnes où plusieurs instituts ont chiffré la même mesure ensuite votée (présidentielles 2007, 2012, législatives), en plus de `data/raw/calibration_instituts.csv` |
| D | Réforme structurelle, Substitution retraites, Élasticité IS, revenus, capital, succession | sources que T18 n'a pas lues (voir `recherche/T18/parts/notes_*.md` et `sources.csv`) : rapports annuels du COR et de l'Unédic sur les économies constatées des réformes, évaluations de France Stratégie (comité ISF/PFU), notes de la Cour des comptes sur les recettes fiscales 2013-2019 (IS, IR, droits de succession), réformes des retraites 2003, 2010 (compléments), 2014 |

**Ne pas chercher** Règle d'or et Déjà dans la référence : ce sont des conventions comptables, pas des prédictions. Les citer comme « non testables par construction » dans le rapport.

## 3. Déroulé

1. **Collecte** : quatre agents en parallèle (A à D), chacun dans `recherche/T21/parts/` (`cout_<G>.csv`, `parametres_<G>.csv`, `notes_<G>.md`, `sources_<G>.csv`), sources dans `sources/T21/<G>/`. Commencer par les documents qui couvrent beaucoup de cas. Noter tout site inaccessible.
2. **Fusion** : un agent fusionne, contrôle doublons et sha256, recalcule les écarts, produit `aveugle/` (T18 phase 2 ; `pays` y figure, pas le réalisé).
3. **Attribution à l'aveugle** : un agent neuf, sans web, sur une copie de `aveugle/` hors du dépôt (T18 phase 3).
4. **Intégration** : hors tâche.

## 4. Livrables (dans `recherche/T21/`)

`mesures_cout_nouvelles.csv`, `parametres_testes.csv`, `aveugle/`, `attribution_agent.csv`, `parts/`, `sources.csv`, `rapport.md` (résultats par règle, cas français et étrangers séparés, ce qui n'a pas été trouvé, décisions laissées à l'intégrateur).

Critère de réussite, fixé à l'avance : pour chaque règle des groupes A à D, soit au moins 5 cas `observe`, soit un test de paramètre sur au moins une estimation ex post `high` ou `medium`, soit une explication écrite de l'impossibilité.
