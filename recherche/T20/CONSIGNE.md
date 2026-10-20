# T20 : TVA et taxes sur la consommation, effet sur les foyers et sur le solde

Consigne préparée le 20/10/2026. Lire d'abord `recherche/CONSIGNES.md` (règles communes ; date d'accès : celle du jour), puis `recherche/T15/regle_selection.md` (§ 3 à 6), `recherche/T18/CONSIGNE.md` et `recherche/T18/rapport.md`.

## Pourquoi cette tâche

Les mesures qui passent par les prix ne sont mesurées nulle part :

- **Pour les foyers** : « Mon foyer » repose sur OpenFisca-France, qui ne modélise pas la TVA ni les accises payées par les ménages. La règle T15 classe donc ces mesures `canal_prix` (« Passe par les prix : non calculée »). C'est le cas de la TVA à 5,5 % sur l'énergie et les carburants (`rn24_tva_carburants`, `rn24_tva_elec_gaz`), de la suppression de la TVA sur les produits de première nécessité (`rn24_tva_pn`), du gel des prix (`l_gel`), de la baisse de l'électricité (`ens_elec`, `e_elec`) et de l'idée des cahiers `tva_alimentation`. Un programme qui passe surtout par les prix paraît donc moins important pour les foyers qu'il ne l'est (T15 § 9).
- **Pour le solde** : la famille `tva_produits` n'a pas de règle (`Aucune`), aucun cas de backtest ne porte sur une baisse de TVA en dehors de `tva_resto_2009`, et la règle « Élasticité carburants » n'a aucun cas (T18 l'a jugée intestable : la recette d'une hausse d'accise n'est jamais isolée du volume).

Il faut d'autres sources qu'OpenFisca : la part de chaque baisse de taxe qui passe dans les prix, ce que consomment les ménages, et ce qu'ont coûté les changements de TVA passés.

Le résultat peut montrer qu'un calcul par foyer n'est pas assez fiable pour être publié. Ce serait un résultat à part entière, à rapporter tel quel.

## 0. Gel des règles

Comme pour T18, les règles de solde ne changent pas pendant la tâche :

| Élément | Valeur |
|---|---|
| Commit | `686902b` |
| `data/raw/regles.csv` (sha256) | `3c97911a18e888fc1faefd9b1922172f32f5dfb703e0ef57a7b50f3da8a8eccb` |
| `data/raw/moteur_regles.csv` (sha256) | `44b3fe92a754144f0995a2e676cd5d5c033f92869d8d324827488972fb3ff4b6` |

La règle T15 (version 0.1) ne change pas non plus. Si la tâche rend calculables des mesures `canal_prix`, la modification de T15 se propose dans le rapport ; c'est à l'utilisateur de la décider.

## 1. Groupes de recherche

Les pistes ci-dessous sont à vérifier, ce ne sont pas des faits : l'existence même des études, leurs chiffres et leurs éditions restent à établir sur source lue. Une piste sans source s'écrit « non trouvé ».

### Groupe A : répercussion sur les prix

Question : quand la TVA ou une accise baisse (ou monte) de x points, quelle part arrive dans le prix payé par le consommateur, et en combien de temps ?

- Par secteur : restauration, énergie (électricité, gaz, carburants), alimentation et biens courants, services (travaux, coiffure…), billetterie.
- Selon le sens : hausse ou baisse (une répercussion asymétrique change l'effet d'une baisse promise).
- Selon l'horizon : impact immédiat, puis 1 à 3 ans.
- Pistes : évaluations de la TVA restauration 2009 (Conseil des prélèvements obligatoires, IPP, Insee), hausses de TVA de 2014 (taux intermédiaire 7 → 10 %, taux normal 19,6 → 20 %), retour au taux normal des abonnements à l'électricité et au gaz (2025), remise carburant de 2022, bouclier tarifaire, travaux européens comparables (études de la Commission européenne, de la BCE, ou de banques centrales nationales sur des changements de TVA).
- Les études étrangères sont admises dans ce groupe (au contraire de T18), avec le pays et la période dans `pays_periode`. Une étude française est préférée à périmètre égal.

Sortie : `repercussion.csv`, au format de `data/raw/elasticites.csv` (mêmes colonnes et même ordre), `domaine` = `repercussion_prix`, `parametre` = secteur et sens (par exemple `tva_restauration_baisse`), valeur entre 0 et 1, `val_bas`, `val_central`, `val_haut` renseignés.

### Groupe B : ce que consomment les foyers

Question : pour chaque situation de la grille T15 § 5 (salariés de 41 ans et retraités de 71 ans ; seul, couple à un ou deux revenus ; 0 à 3 enfants ; 0,5 à 6 SMIC ; pensions de 900 à 5 000 € bruts par mois), combien le foyer dépense-t-il par an, et sous quels taux ?

- Dépense de consommation, ou taux d'épargne, par niveau de vie (décile ou quintile), type de ménage et âge de la personne de référence.
- Part de la dépense par catégorie fiscale : taux normal, intermédiaire, réduit, super-réduit, hors champ (loyers, assurances…). Pour l'énergie (électricité, gaz, fioul, carburants), séparer les volumes (kWh, litres) ou les montants TTC, pour pouvoir appliquer une accise.
- Charge de TVA et des accises en part du revenu disponible, par décile, si elle est publiée. Elle servira de contrôle du calcul.
- Pistes : enquête Budget de famille de l'Insee (vérifier quelle est la dernière édition publiée et la date de ses données ; ne pas supposer que c'est celle de 2017), comptes nationaux (consommation par fonction et par produit), publications de l'Insee, de la DG Trésor, du CAE, de l'IPP (modèle TAXIPP), de l'OFCE ou de France Stratégie sur l'incidence de la fiscalité indirecte, données du SDES sur les dépenses d'énergie des ménages.
- Noter la base de prix de chaque montant (année des euros), pour une mise à jour à 2026.

Sortie : `consommation.csv`, colonnes `id, decoupage, categorie_menage, poste, unite, valeur, annee_donnees, url, titre, citation, page, confiance, note`. `decoupage` dit selon quoi le tableau est découpé (`decile_niveau_vie`, `type_menage`, `age_pr`, ou un croisement). On recopie les tableaux tels qu'ils sont publiés. Le passage aux situations de la grille revient à l'intégrateur (§ 3).

### Groupe C : coût des changements de TVA passés

Question : les changements de taux de TVA votés depuis 2000 ont-ils coûté ou rapporté ce qu'annonçait leur chiffrage ?

- Même protocole et même format que T18 (§ 1 « Exigences de comparabilité » et § 4 « Format des CSV ») : un chiffrage avant adoption, un réalisé sur le même périmètre, `comportement_inclus_ex_ante`, `type_ex_post`, `realise_publie_le`.
- Pistes : TVA restauration (2009, puis 7 % en 2012 et 10 % en 2014), hausses de 2014, TVA sur les travaux de rénovation, TVA « sociale » de 2012 (votée puis abrogée : le noter, non comparable), TVA sur les abonnements d'énergie (2025), taux réduits ciblés (protections hygiéniques, masques et gels en 2020, billetterie, livres numériques). Pour le réalisé : Voies et moyens tome II (coût annuel de chaque taux réduit, qui est une réestimation, `type_ex_post` = `reestimation`), notes d'exécution budgétaire de la Cour des comptes (recettes fiscales), rapports du CPO et évaluations parlementaires.
- `tva_resto_2009` est déjà dans `data/raw/mesures_cout.csv` : ne pas la reprendre, sauf pour les étapes de 2012 et 2014, qui sont des mesures distinctes.
- Prévoir que peu de réalisés soient `observe` : la recette de TVA n'est presque jamais isolée par taux. Le dire franchement plutôt que de compléter avec des réestimations sans le signaler.
- `regle_pressentie` : `Aucune` (coût mécanique) ; la règle n'est choisie qu'en phase 3.

Sorties : `mesures_cout_nouvelles.csv` et, s'il y a des effets annoncés (baisse des prix, emplois), `mesures_effets_nouvelles.csv`, aux colonnes de T18.

## 2. Déroulé

1. **Collecte** : trois agents en parallèle (groupes A, B, C), chacun dans `recherche/T20/parts/` (`<sortie>_<G>.csv`, `notes_<G>.md` avec les pistes suivies, les pages lues, les tentatives et les exclusions motivées) ; sources dans `sources/T20/<G>/`, listées dans `parts/sources_<G>.csv`. Commencer par les documents qui couvrent beaucoup de cas à la fois. Noter tout site inaccessible (senat.fr a refusé `curl` lors des tâches précédentes).
2. **Fusion** : un agent fusionne les parts, contrôle les doublons avec `data/raw/` et les sha256, recalcule les écarts du groupe C et produit `aveugle/` comme T18 phase 2.
3. **Attribution à l'aveugle** du groupe C : un agent neuf, sans web, sur une copie de `aveugle/` placée hors du dépôt, même protocole que T18 phase 3 (`attribution_agent.csv`).
4. **Intégration** : hors tâche, voir § 3.

## 3. Décisions laissées à l'intégrateur et à l'utilisateur

À présenter dans `rapport.md`, avec les éléments trouvés, sans les trancher :

- **Calcul par foyer** : la façon de passer des tableaux du groupe B aux situations de la grille (interpolation par niveau de vie, convention pour les retraités, base de prix), et la répercussion retenue (centrale et fourchette). Ce serait un nouveau type de réforme dans `scripts/distributif.py`, écrit de façon générale pour tous les partis (T15 § 3.4).
- **Présentation** : afficher un effet par les prix à côté de l'effet OpenFisca, ou seulement une fourchette, ou continuer à le classer « non calculé ». Un effet calculé avec moins de précision ne doit pas être additionné sans le dire à celui qu'OpenFisca calcule.
- **Règle T15** : proposer la version 0.2 qui rend calculables tout ou partie des mesures `canal_prix`, avec l'entrée de journal et la liste des programmes à refaire.
- **Solde** : faut-il une règle propre à la famille `tva_produits` (répercussion incomplète, effets sur les volumes), et sur combien de cas `observe` elle reposerait. En dessous de 5 cas, la règle n'est pas jugée (seuil de `scripts/validation.py`).

## 4. Livrables (dans `recherche/T20/`)

- `repercussion.csv`, `consommation.csv`, `mesures_cout_nouvelles.csv` (et `mesures_effets_nouvelles.csv` s'il y a lieu) ;
- `aveugle/` et `attribution_agent.csv` ;
- `parts/` ;
- `sources.csv` (fusion des `parts/sources_<G>.csv`) ;
- `rapport.md` : résultats par groupe, ce qui n'a pas été trouvé, points de vigilance, décisions du § 3.

Critère de réussite, fixé à l'avance : au moins une valeur de répercussion `high` ou `medium` pour l'énergie et une pour l'alimentation ; une structure de consommation par décile et par type de ménage d'une enquête datée ; au moins 5 changements de TVA avec chiffrage et réalisé, quelle que soit la nature du réalisé. Le rapport dit lesquels sont atteints.
