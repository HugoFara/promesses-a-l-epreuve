# T15 — Règle de sélection des mesures « ménages » par parti

Projet, version 0.2 du 20 octobre 2026 (version 0.1 du 14 octobre 2026), **à valider avant toute recherche dans les programmes**.

## 0. But et principe

L'accueil doit pouvoir montrer ce que le programme de chaque parti change pour un foyer donné. Le risque de parti pris ne vient pas des calculs, qui sont faits par OpenFisca de la même façon pour tous. Il vient du **choix des mesures**. Cette règle fixe ce choix à l'avance, sans regarder les résultats.

Trois principes :

1. **Exhaustivité, puis tri.** On inventorie *toutes* les mesures de chaque programme. Chacune reçoit un verdict selon les critères de la section 3. On ne choisit pas des mesures « représentatives ».
2. **Même règle, pas même nombre.** Un parti peut avoir 12 mesures calculées et un autre 2. On ne complète pas et on ne retire rien pour équilibrer. Le site affiche pour chaque parti combien de mesures ont été calculées sur combien de mesures ménages repérées.
3. **Règle figée avant lecture.** Une modification après le début de la recherche est datée, motivée dans le journal (section 8) et appliquée à tous les programmes déjà traités.

## 1. Quels partis

- **Avant la liste officielle des candidats** : tout parti ou toute coalition qui présente un candidat déclaré à la présidentielle de 2027 **et** qui a un groupe à l'Assemblée nationale à la date de publication de son programme.
- **Après la publication de la liste officielle par le Conseil constitutionnel** : tous les candidats officiels, sans exception. Ceux qui n'entraient pas dans le premier critère sont ajoutés dès que leur programme est publié.
- Un parti n'apparaît qu'une fois son programme publié. Avant, l'accueil indique « programme non publié au [date] ».

*À décider par l'utilisateur* : ce premier seuil (groupe à l'Assemblée) écarte les petits candidats jusqu'à la liste officielle. On pourrait aussi tous les inclure dès le départ, mais la charge de travail serait plus lourde.

## 2. Quelle source

- **Le programme écrit et daté** publié par le candidat ou le parti (document ou page officielle), archivé avec son sha256 dans `sources/T15/`, comme les autres sources du projet.
- **Le chiffrage publié par le parti lui-même**, s'il existe. Il sert seulement à fixer un paramètre que le programme laisse implicite (par exemple un seuil). Il ne sert jamais à fixer un effet.
- **Exclus** : interviews, déclarations orales, réseaux sociaux, propositions de loi antérieures non reprises dans le programme. Les déclarations sont trop instables et trop faciles à choisir selon ce qu'on veut montrer.
- **Mise à jour** : si le programme est révisé, la nouvelle version est archivée, l'inventaire est refait, et le site indique la version utilisée.
- **Programmes de 2024** : ils ne sont pas utilisés pour la présentation par parti en 2027. Les deux mesures NFP actuelles restent dans « Mon foyer » comme exemples, jusqu'à leur remplacement.
- **Mesures du gouvernement** (PLF et PLFSS 2027) : elles ne sont pas attribuées à un parti. Elles forment un bloc à part, « Budget 2027 en discussion », parce qu'elles s'appliqueront quel que soit le résultat de l'élection, si elles sont votées.

## 3. Critères d'une mesure calculée

Une mesure est **calculée** si elle remplit les quatre critères. Sinon, elle est classée dans une des catégories de la section 4, et cette classification est publiée.

1. **Mesure ménages** : elle change directement l'un de ces éléments du revenu disponible : impôt sur le revenu, CSG et CRDS, cotisations salariales, prestations sociales et familiales, minima sociaux, prime d'activité, pensions de retraite (montant ou revalorisation), salaire minimum, imposition des revenus du capital.
2. **Précise** : le programme (ou le chiffrage du parti, section 2) fixe chaque paramètre nécessaire : montant, taux, seuil et public visé. On ne comble aucun manque par une hypothèse. Si deux lectures sont plausibles, la mesure est classée « imprécise ».
3. **Visible dans la grille** : elle change le revenu disponible d'au moins une situation de la grille actuelle (section 5). La grille est figée avant l'inventaire, pour qu'on ne puisse pas l'adapter aux mesures d'un parti.
4. **Simulable** : elle s'exprime par un paramètre d'OpenFisca-France ou par un type de réforme de `scripts/distributif.py`. Un nouveau type est permis s'il est écrit de façon générale, testé, et utilisable tel quel pour la mesure d'un autre parti.

**Exception « prix » (version 0.2)** : une mesure qui change le taux de TVA ou d'accise, ou le prix TTC, de l'électricité, du gaz, du fioul ou des carburants est calculée par le type `prix` de `scripts/distributif.py`, si le programme fixe le taux ou la variation de prix. Le critère 1 est alors remplacé par « change directement le prix d'un poste de consommation que l'enquête Budget de famille isole ». Le résultat est une baisse (ou hausse) de dépenses, affichée à part du revenu disponible, avec une fourchette de répercussion dans les prix (`rep_energie_logement_baisse`, `rep_carburants_baisse` dans `data/raw/parametres_bareme.csv`, même règle pour tous). Les autres mesures sur les prix (alimentation, produits de première nécessité, gel des prix) restent `canal_prix` : la liste des produits ou l'effet sur les prix n'est pas assez précis, ou la consommation n'est pas isolée par taux de TVA.

## 4. Catégories des mesures non calculées

Elles sont toutes listées pour chaque parti, à côté du résultat, avec une citation.

| Catégorie | Exemples | Ce que dit le site |
|---|---|---|
| `imprecise` | « baisser l'impôt des classes moyennes » sans barème | « Pas assez précise pour être calculée » |
| `hors_grille` | mesure pour les moins de 30 ans, les étudiants, les locataires (aides au logement), les indépendants, les chômeurs, les personnes handicapées | « Ne concerne pas les situations du simulateur » |
| `canal_prix` | TVA ou prix hors énergie (alimentation, produits de première nécessité), gel des prix, péages ; énergie sans taux ni variation précis | « Passe par les prix : non calculée » |
| `canal_retraite_age` | âge de départ, durée de cotisation | « Change l'âge de départ, pas le revenu d'une année : non calculée » |
| `canal_patrimoine` | droits de succession, impôt sur la fortune, taxe foncière | « Porte sur le patrimoine : non calculée » |
| `canal_entreprises` | impôt sur les sociétés, cotisations patronales, aides aux entreprises | « Pèse d'abord sur les entreprises : effet sur les foyers incertain » |
| `services` | santé, école, transports, services publics | « Service, pas revenu : non calculée » |
| `indirect` | effets attendus sur l'emploi, la croissance, les salaires au-dessus du minimum | « Effet indirect : non calculé » |
| `conditionnelle` | expérimentation, mesure renvoyée à une négociation ou à un référendum | « Non certaine : non calculée » |

Un parti dont le programme passe surtout par des canaux non calculés paraîtra moins touché qu'il ne l'est. Le nombre de mesures par catégorie, affiché pour chaque parti, sert à le montrer.

## 5. Grille figée

C'est la grille actuelle de `distributif.py` (468 situations) :

- salariés de 41 ans et retraités de 71 ans ;
- seul, en couple avec deux revenus, en couple avec un seul revenu ;
- 0 à 3 enfants de 4, 7 et 10 ans pour les salariés ;
- salaires de 0,5 à 6 SMIC, pensions de 900 à 5 000 € bruts par mois ;
- dividendes de 0, 2 000, 10 000 ou 50 000 € par an ;
- sans loyer ni aide au logement ;
- législation de 2026, régime permanent.

*À décider par l'utilisateur* : élargir la grille **avant** l'inventaire, par exemple aux jeunes actifs de 25 ans, aux locataires ou aux chômeurs. Cela rendrait calculables des mesures aujourd'hui `hors_grille`, mais chaque ajout demande des conventions (loyer, zone, durée de chômage). On ne peut plus l'élargir pendant l'inventaire, sauf pour tous les partis à la fois, avec une entrée au journal.

## 6. Conventions de calcul, identiques pour tous

- **Statique** : aucun effet de comportement, d'emploi ni de diffusion des salaires (comme le SMIC aujourd'hui). Le site le rappelle.
- **Mesure à sa cible** : une mesure prévue par étapes est calculée à son niveau final, avec la mention « à terme (prévu pour [année]) ».
- **Montants** : on applique le montant tel qu'il est écrit (net ou brut, mensuel ou annuel, en euros courants). Si le programme ne précise pas net ou brut et que le chiffrage du parti ne tranche pas, la mesure est `imprecise`.
- **Base** : législation de 2026, comme les mesures actuelles ; les montants ne sont pas indexés.
- **Gains et pertes** : une hausse d'impôt ou une baisse de prestation est calculée comme une hausse de prestation. On ne retient pas seulement les mesures favorables.
- **Interactions** : chaque mesure est d'abord calculée seule. On calcule aussi le programme entier (toutes ses mesures calculées appliquées ensemble), mais il n'est affiché que s'il est clairement étiqueté « ensemble des mesures calculées, pas du programme entier ».

*À décider par l'utilisateur* : afficher ou non cet effet d'ensemble par parti. Il répond à la question du testeur (« et pour moi, ce parti ? »), mais ressemble à un total, alors qu'il omet toutes les mesures non calculées.

## 7. Présentation sur le site

- Un bloc par parti, avec la même structure et les mêmes formulations : mesures calculées et leur effet par mois, puis « Non calculé : n mesures » dépliable par catégorie, avec citations.
- **Ordre** : alphabétique en attendant la liste officielle, puis l'ordre de la liste du Conseil constitutionnel.
- **Aucun classement ni tri par gain**, aucun « meilleur pour vous ».
- **Lien avec le financement** : chaque bloc renvoie à la vue « Programmes » et donne le solde corrigé du programme, quand il est calculé. Un gain financé par la dette n'est pas gratuit.
- **Couleurs** : pas les couleurs des partis. Vert et rouge seulement pour le signe, comme aujourd'hui.
- Le rappel « aucune consigne de vote, un critère parmi d'autres » reste visible sans dérouler la page.

## 8. Procédure et contrôle

1. **Inventaire** : un agent de recherche lit le programme et liste chaque mesure dans `recherche/T15/inventaire_<parti>.csv`. Colonnes : `programme, mesure_id, libelle_programme, citation, page, url, categorie, motif, parametres, confiance`.
2. **Double codage** : un second agent, qui ne voit pas les verdicts du premier, code à nouveau toutes les mesures. Les désaccords sont tranchés par l'intégrateur, avec le motif écrit. Le taux d'accord par parti est publié dans le rapport.
3. **Paramétrage** : seules les mesures calculées entrent dans `data/raw/distributif_reformes.csv`, avec `porteur`, `url`, citation et confiance `high` (programme lu). Le lien vers l'inventaire est gardé.
4. **Même délai** : chaque programme est traité dans les jours qui suivent sa publication, pour qu'aucun parti ne reste longtemps seul affiché. Tant que deux partis au moins ne sont pas traités, l'accueil garde la présentation actuelle, par mesures.
5. **Audit** : à la fin de chaque vague, un agent indépendant relit un échantillon des verdicts et vérifie l'absence de biais (par exemple : y a-t-il plus de mesures `imprecise` pour un camp ? Est-ce justifié par les textes ?).
6. **Journal des modifications** de cette règle :

| Date | Version | Modification | Motif | Programmes retraités |
|---|---|---|---|---|
| 14/10/2026 | 0.1 | Rédaction | — | aucun |
| 20/10/2026 | 0.2 | Exception « prix » (§ 3) : TVA et accises sur l'énergie calculées hors OpenFisca ; `canal_prix` restreint au reste | Recherche T20 (répercussion, consommation des ménages) | exemples 2024 : RN (TVA sur l'énergie) et Ensemble (accise sur l'électricité) ajoutés à « Mon foyer » ; NFP inchangé (gel des prix : reste `canal_prix`) |

## 9. Ce que cette règle ne garantit pas

- Elle garantit un **traitement identique**, pas un **résultat représentatif** du programme : la plupart des politiques (prix, retraites, services) ne sont pas calculées. Le site doit le dire autant que les montants.
- Le choix des critères eux-mêmes (par exemple exclure les prix) a des effets différents selon les partis. C'est inévitable ; la règle le rend visible, par le comptage des catégories.
- Le double codage réduit les erreurs de lecture, pas les biais communs aux deux agents. La relecture humaine des cas limites reste nécessaire.
