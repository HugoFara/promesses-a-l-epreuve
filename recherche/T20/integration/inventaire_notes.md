# Inventaire des mesures ménages : RN et Ensemble (programmes 2024)

Date d'accès : 20/10/2026. Fichier : `inventaire_rn_ens_2024.csv` (41 lignes : 23 RN, 18 Ensemble). Sources : `sources_inventaire.csv`.

## 1. Sources et accès

- Le site de l'Institut Montaigne répond `403` (page Cloudflare « Just a moment… ») à `curl`. Toutes les pages ont été lues **via web.archive.org**, comme pour le NFP dans T6. Aucune autre source n'a été utilisée.
- Synthèse RN : la seule capture de 2024 est celle du 17/07/2024 (pas de capture avant l'élection). Une capture du 25/01/2025 donne le même texte (vérifié par diff, en dehors des liens). Une capture de 2026 a la même empreinte que celle de 2024 dans l'index Wayback.
- Synthèse Ensemble : captures du 10/07/2024 et du 25/07/2024. Le texte est le même. Seule différence : la seconde ajoute le lien « retrouvez le détail ici » vers les micro-chiffrages. Le NFP avait été lu sur la capture du 08/07/2024.
- Les deux synthèses renvoient à des fiches de mesures (13 pour le RN, 11 pour Ensemble, toutes archivées) et à un PDF « Synthèses des micro-chiffrages » par parti, sur le même site. Ces PDF sont archivés et cités par page (RN : 9 p., Ensemble : 6 p.).
- Colonne `url` : l'adresse d'origine sur institutmontaigne.org, comme dans `non_chiffre_foyer.csv`. L'adresse Wayback réellement lue est dans `sources_inventaire.csv`.

## 2. Règle d'inclusion (« touche directement les ménages »)

Cette règle a été appliquée de la même façon aux deux partis :

- **Inclus** : toute mesure qui change l'argent qu'un foyer reçoit ou paie. Cela couvre les impôts, cotisations, prestations, salaires (y compris ceux des agents publics, comme le point d'indice pour le NFP), pensions, prix et taxes sur la consommation, et le reste à charge d'un service (couverture santé). S'y ajoutent les mesures d'âge de départ en retraite, qui ont une catégorie à elles.
- **Exclus**, et non listés dans le CSV :
  - les mesures qui augmentent l'offre d'un service public sans en changer le prix pour le foyer ;
  - les règles de police, de justice ou d'immigration qui ne touchent pas une prestation ;
  - les impôts des entreprises qui ne visent pas un salaire ;
  - l'organisation de l'État.

Exclus pour le RN :
- baisse des impôts de production (CVAE, C3S) ;
- impôt sur les sociétés des entreprises créées par des moins de 30 ans ;
- places de prison ;
- police municipale ;
- carte Vitale biométrique ;
- 80 % de produits français dans les cantines ;
- interdiction des importations agricoles non conformes ;
- fin du numerus apertus ;
- suppression des zones à faibles émissions ;
- suppression du droit du sol ;
- privatisation de l'audiovisuel public ;
- suppression des ARS ;
- réforme de l'asile.

Exclus pour Ensemble :
- service national universel ;
- remplacement des absences d'enseignants ;
- 35 000 logements étudiants ;
- doublement des médecins en formation ;
- maisons France services ;
- 20 millions de rendez-vous médicaux ;
- centres de rétention aux frontières de l'Europe.

Cas discutables :
- **ZFE** (RN) : la mesure change ce que certains ménages peuvent faire de leur voiture, mais pas un revenu ni un prix.
- **Logements étudiants** (Ensemble) : ils baissent le loyer de ceux qui en obtiennent un, mais c'est une offre nouvelle, pas un barème.

Si l'intégrateur les inclut, il faut les classer `hors_grille`, l'un et l'autre.

## 3. Asymétrie avec le NFP déjà publié

Les 7 lignes NFP de `non_chiffre_foyer.csv`, plus les 2 mesures calculées, ne forment **pas** un inventaire complet de la synthèse NFP. La synthèse NFP contient aussi, entre autres :
- l'AAH au niveau du SMIC ;
- les APL + 10 % ;
- l'indexation des pensions et des salaires ;
- la gratuité de l'école ;
- l'abolition de la « taxe Macron » sur l'énergie (TICFE) ;
- la TVA à 5,5 % sur les transports en commun ;
- la cotisation sur les dividendes et les heures supplémentaires ;
- la surcotisation des hauts salaires.

Le présent inventaire est complet pour le RN et Ensemble. Si on le publie tel quel, le NFP paraîtra avoir moins de mesures non calculées. **Il faut refaire l'inventaire NFP selon la même règle** avant de publier les comptes par catégorie (T15 § 0, principe 1).

## 4. Choix de catégorie : ordre suivi

Quand plusieurs motifs s'appliquent, la catégorie retenue suit cet ordre :

1. un canal de T15 § 4 (`canal_prix`, `canal_retraite_age`, `canal_patrimoine`, `canal_entreprises`, `services`) ;
2. sinon `hors_grille`, si le public visé n'est pas dans la grille, même si la mesure est aussi imprécise : précisée, elle ne serait de toute façon pas calculée ;
3. sinon `imprecise`.

Le second motif est écrit dans `motif` (exemples : enseignants, agents publics, demi-part des veufs).

## 5. Cas limites et hésitations

**Mesures `calculable_*`**

- **RN, TVA de 20 % à 5,5 % sur l'énergie** (`calculable_prix`) : une seule mesure dans le programme. Le projet la sépare déjà en deux (`tva_carburants_55`, `tva_elec_gaz_55`). La fiche précise que l'assiette déjà à 5,5 % (abonnements, CTA) n'est pas concernée. En 2026, ces abonnements sont repassés au taux normal (voir `statut_reference_2027.csv`). Il faut décider si la mesure les ramène à 5,5 % : le programme ne le dit pas. Faisabilité : la fiche juge le taux réduit sur les carburants contraire à la directive TVA. Ce n'est pas un critère de T15, donc ce n'est pas un motif d'exclusion.
- **RN, part entière dès le 2e enfant** (`calculable_openfisca`) : le seul paramètre fixé est le nombre de parts. La fiche rappelle le plafond de 1 678 € par demi-part, mais ni le programme ni la fiche ne disent comment il s'applique à une part entière pour le 2e enfant. Lecture la plus directe : 2 demi-parts plafonnées chacune, comme pour le 3e enfant aujourd'hui. C'est la règle actuelle appliquée au nouveau nombre de parts, pas une hypothèse ajoutée. Si l'intégrateur juge qu'une seconde lecture est plausible, la mesure passe en `imprecise` (T15 § 3.2).
- **Ensemble, électricité − 15 %** (`calculable_prix`) : la fiche dit que la baisse « n’est donc pas une mesure à proprement parler ». La baisse du tarif réglementé vient des prix de marché. La seule partie fiscale est le maintien de l'accise au tarif réduit : 21 € le MWh au lieu de 32 € le MWh, deux montants lus dans la fiche. Le classement suit ce que le projet a déjà retenu (`elec_accise_reduite`, type `prix`) : seule la part due à l'accise est calculée. Autre lecture possible : `canal_prix` non calculable, au motif que le chiffre de 15 % n'est pas un paramètre fiscal. Décision laissée à l'intégrateur.

**Autres cas**

- **RN, TVA sur les produits de première nécessité** : `canal_prix` non calculable. La liste des produits n'est pas publiée (deux scénarios Montaigne) et la mesure ne s'applique qu'« en cas de forte inflation ». `conditionnelle` serait aussi défendable.
- **RN, prêt à taux zéro transformé en subvention pour un 3e enfant** : les couples avec 3 enfants sont dans la grille, mais aucun montant n'est donné, ni dans la synthèse ni dans les micro-chiffrages (12,6 Md€ sans détail). Classée `imprecise`.
- **Indexation des pensions sur l'inflation (RN et Ensemble)** : la synthèse la mentionne pour les deux listes et la dit « déjà ancrée dans la réglementation ». Elle est classée `hors_grille`, car elle ne change aucune situation (critère 3). Le site affiche « Déjà la règle en vigueur ». On pourrait aussi l'exclure de l'inventaire. Dans les deux cas, il faut traiter les deux partis de la même façon.
- **Versement à la source des aides (Ensemble)** : le barème ne change pas. Le coût de 5 Md€ vient du recours, alors que le simulateur verse déjà chaque droit. Classée `hors_grille`. `conditionnelle` serait aussi défendable : la fiche dit que la seconde phase a un « calendrier et [des] modalités [qui] ne sont pas connus ».
- **Prime de partage de la valeur (Ensemble) et exonération de cotisations sur les hausses de salaire (RN)** : les deux dépendent d'une décision de l'employeur. Toutes deux sont classées `canal_entreprises`, avec le même texte affiché (« Dépend de l'employeur »), comme la PPV du gouvernement dans `non_chiffre_foyer.csv`.
- **Effets de seuil (Ensemble)** : `imprecise` plutôt que `canal_entreprises`, car les micro-chiffrages citent aussi la prime d'activité, qui est dans la grille. Montaigne la juge « trop imprécis[e] ».
- **AME (RN), complémentaire santé à 1 €/jour et fauteuils roulants (Ensemble)** : toutes trois en `services` (couverture santé), y compris l'AME, alors que son public n'est pas non plus dans la grille. Ce choix vise la cohérence entre les trois.
- **Âge de 65 ans (Ensemble)** : la synthèse dit qu'Ensemble « n’a pas formulé d’annonce relative au régime des retraites ». Pourtant, ses « Autres mesures » et les micro-chiffrages (p. 5) listent « Reculer l’âge d’ouverture des droits à la retraite de 64 à 65 ans : 0 € ». La mesure est inscrite parce qu'elle figure dans la synthèse. La contradiction est interne à la source.
- **Assurance chômage** : le maintien (Ensemble) et l'annulation (RN) sont tous deux classés `hors_grille`. Montaigne note que la réforme ne figure « pas en tant que telle » dans le programme d'Ensemble ; il l'attribue par hypothèse. Elle est gardée parce qu'elle est dans la synthèse, comme pour le RN.
- **Revalorisation des enseignants (RN) et des agents publics (Ensemble)** : `hors_grille`, avec le texte « Pas encore simulé », comme le point d'indice du NFP. Les deux sont aussi imprécises : les 2 points d'indice d'Ensemble sont une hypothèse de Montaigne.
- **Mesures réservées aux Français ou aux étrangers (RN)** : `hors_grille`. La grille ne décrit pas la nationalité, donc aucune de ses situations ne change. Si le simulateur suppose des foyers français, l'effet calculé est nul, ce qui n'est pas la même chose que « non calculé ». Le site devrait le dire.
- **Demi-part des veufs (RN)** : `hors_grille`. Le retraité seul de la grille n'a ni veuvage ni enfant élevé déclaré. De plus, les conditions de la demi-part ne sont pas précisées.

## 6. Pour l'intégrateur

1. Valider la règle d'inclusion (§ 2) et refaire le NFP selon elle (§ 3).
2. Trancher les trois mesures `calculable_*` (§ 5).
3. Faire un double codage (T15 § 8.2) : non fait ici, un seul codeur.
