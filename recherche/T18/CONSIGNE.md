# T18 : tester les règles de correction sur de nouvelles mesures passées

Consigne préparée le 16/10/2026. Lire d'abord `recherche/CONSIGNES.md` (règles communes), puis `recherche/validation/README.md` (protocole de validation) et `recherche/T10a/rapport.md` (la dernière extension de la couche 1, même format).

## Pourquoi cette tâche

La validation actuelle (`data/validation_resume.csv`, `data/validation_regles.csv`) ne démontre pas que les règles améliorent les chiffrages :

- sur les 13 chiffrages officiels où une règle change le chiffre, l'erreur médiane passe de 21,4 % à 40,8 % (5 améliorés, 8 dégradés) ;
- la plupart des règles appliquées aux programmes sont testées sur 0 ou 1 cas : Élasticité IS (1 cas retenu), capital (1), revenus (1), succession (0), carburants (0), électricité (0), rachats (0), Nouvelle assiette : risque juridique (1), Réforme structurelle (2) ;
- l'agent d'attribution connaissait l'issue de 60 cas sur 83 : le test n'est aveugle qu'en intention.

Le but n'est **pas** d'ajouter des mesures en vrac. Les coûts mécaniques (barème, montant fixé, facteur 1) ne testent rien. Il faut des cas où **une règle s'applique**, en nombre suffisant par règle pour conclure, et un test d'attribution plus aveugle.

Le résultat peut être défavorable à la méthode. Il sera publié de la même façon (règle de présentation « Dire les limites »). Ne pas choisir les mesures selon que la règle semble marcher ou non.

## 0. Gel des règles (avant toute recherche)

Les règles testées sont celles de l'état suivant, qui ne doit pas changer pendant la tâche :

| Élément | Valeur |
|---|---|
| Commit | `0b4175f` |
| `data/raw/regles.csv` (sha256) | `3c97911a18e888fc1faefd9b1922172f32f5dfb703e0ef57a7b50f3da8a8eccb` |
| `data/raw/moteur_regles.csv` (sha256) | `44b3fe92a754144f0995a2e676cd5d5c033f92869d8d324827488972fb3ff4b6` |

Le champ de chaque règle est celui de `recherche/validation/aveugle/regles_disponibles.csv`. Une règle qu'on voudrait modifier au vu des nouveaux cas se note dans le rapport (« décisions laissées à l'intégrateur ») ; elle ne se modifie pas pendant la tâche.

## 1. Ce qu'on cherche

Une **mesure** retenue réunit :

1. **Un chiffrage avant adoption**, daté, par un auteur identifié : évaluation préalable d'un article de PLF ou PLFSS, étude d'impact, exposé des motifs, chiffrage d'un rapporteur, chiffrage d'un candidat ou d'un institut pour une mesure ensuite votée.
2. **Un réalisé** publié après coup, sur le même périmètre : Voies et moyens tome II (niches), rapports de la Cour des comptes (analyses de l'exécution budgétaire, notes sur les recettes fiscales, rapports sur la sécurité sociale), rapports d'évaluation (France Stratégie, CPO, IGF, Sénat, Assemblée nationale, DREES, Unédic, IPP, OFCE, CAE), comptes d'un organisme.
3. **Une règle qui s'applique**, d'après la seule nature de la mesure (tableau du § 2).

Période : de 2000 à 2025 (réalisé publié au plus tard le 16/10/2026). Mesures nationales françaises.

### Exigences de comparabilité

Elles expliquent une partie des mauvais résultats actuels ; chacune a sa colonne (§ 4).

- **Même périmètre et même année.** Régime de croisière contre régime de croisière, première année contre première année. Si le réalisé ne porte pas sur la même année que le chiffrage, le dire et le noter.
- **Comportement déjà inclus ?** Dire si le chiffrage avant adoption intègre déjà une réaction des contribuables ou des bénéficiaires (« chiffrage statique », « après effets de comportement », hypothèse de recours). Citer la phrase. Appliquer une élasticité à un chiffrage qui la contient déjà compte l'effet deux fois : c'est peut-être la cause des dégradations de la règle « Élasticité IS ». Si rien n'est dit, écrire `inconnu`.
- **Base de prix.** Si les montants sont dans des euros d'années différentes, renseigner `deflateur_ex_ante` comme dans `data/raw/mesures_cout.csv`.
- **Nature du réalisé** (`type_ex_post`) :
  - `observe` : recette ou dépense effectivement constatée ;
  - `administratif` : montant budgétaire ou enveloppe, pas une observation ;
  - `reestimation` : nouveau chiffrage par l'administration, sans observation directe.

  Seuls les cas `observe` comptent dans la statistique principale.
- **Contrefactuel.** Si le réalisé est « par rapport à ce qui se serait passé sans la mesure » (comme l'ISF dans `isf_ifi`), le dire.

## 2. Objectifs par règle

Cibles minimales : **8 cas `observe` par règle** pour les règles appliquées aux programmes. Le tableau donne des pistes à vérifier, pas des faits : leurs chiffres, leur existence même d'un chiffrage préalable et d'un réalisé restent à établir sur source lue. Une piste sans source se note « non trouvé ».

Ne pas reprendre les mesures déjà présentes dans `data/raw/mesures_cout.csv` et `data/raw/mesures_effets.csv`, ni celles écartées par T10a (`recherche/T10a/parts/notes_*.md`), sauf source nouvelle qui lève le motif d'exclusion.

| Groupe | Règle (`regles_disponibles.csv`) | Cas actuels | Pistes |
|---|---|---|---|
| A | Élasticité capital | 1 | barémisation des revenus du capital (2013), prélèvements sociaux sur le capital (hausses 2011-2018), plus-values mobilières (réforme 2013-2014), PEA et assurance-vie |
| A | Élasticité patrimoine | 5 | bouclier fiscal (2006, 2007), réforme de l'ISF 2011, contribution exceptionnelle 2012, plafonnement ISF |
| A | Élasticité revenus | 1 | CEHR (2012), taxe à 75 % (2013-2014), tranche à 45 % (2013), tranche à 41 % (2006), plafonnement des niches |
| A | Élasticité succession | 0 | réforme TEPA des successions (2007), baisse de l'abattement en ligne directe (2012), rappel fiscal 6 → 10 → 15 ans, pacte Dutreil |
| B | Élasticité IS | 1 | contributions exceptionnelles d'IS (2011-2016, 2017), contribution sociale sur l'IS, baisse du taux réduit PME, changements de déductibilité (intérêts 2012-2014) |
| B | Nouvelle assiette : risque juridique | 1 | contribution de 3 % sur les dividendes (2012, annulée), taxe sur les services numériques (2019), taxe sur les rentes infra-marginales (2022-2023), taxe sur les transactions financières (2012) |
| B | Élasticité carburants | 0 | composante carbone de la TICPE (2014-2018), rattrapage gazole-essence, suppression du tarif réduit du GNR, remise carburant 2022 |
| B | Élasticité électricité | 0 | relèvement de l'accise sur l'électricité (2024, 2025), TICFE pendant le bouclier, CSPE |
| C | Taux de recours | 8 (restreinte) | RSA activité (2009), complémentaire santé solidaire (2019), garantie jeunes, aide à l'embauche PME (2016), aides exceptionnelles à l'apprentissage (2020), prime à la conversion, bonus écologique, indemnité carburant 2023 |
| C | Réforme structurelle | 2 | réformes de l'assurance chômage (2019-2021, 2023), réforme des retraites 2014 (Touraine), réformes des régimes spéciaux (2008), RGPP et MAP, réforme de la carte territoriale |
| D | Effet promis | 8 | recettes de lutte contre la fraude annoncées (lois de 2013 et 2018, STDR), emplois du pacte de responsabilité, effets annoncés du CIR et du suramortissement (2015), du crédit d'impôt apprentissage |
| D | Recette ponctuelle | 0 | régularisations fiscales (STDR 2013-2017), contributions exceptionnelles annoncées comme ponctuelles et prolongées |

Le groupe D produit surtout des lignes d'effets (format de `data/raw/mesures_effets.csv`) ; les autres, des lignes de coût.

**Ne pas chercher** les règles sans précédent possible (« Effet emploi du SMIC », « Taxe sur les rachats d'actions », « Règle d'or », « Taux d'intérêt », « Médiane des estimations », « Déjà dans la référence »). Les citer comme « non testables » dans le rapport.

**Mesures étrangères** : hors champ par défaut. Un agent qui rencontre un cas étranger très proche d'une règle sans précédent français (taxe sur les rachats aux États-Unis en 2023 par exemple) le note dans `parts/<groupe>_etranger.md`, sans l'intégrer au CSV. L'intégrateur décidera.

## 3. Déroulé et séparation des rôles

### Phase 1 : collecte (4 agents en parallèle, groupes A à D)

Chaque agent :

- ne travaille que sur son groupe ;
- écrit dans `recherche/T18/parts/` : `cout_<G>.csv`, `effets_<G>.csv` (groupe D surtout), `notes_<G>.md` (pistes suivies, pages lues, tentatives, exclusions avec motif) ;
- archive ses sources dans `sources/T18/<G>/` et les liste dans `parts/sources_<G>.csv`.

Recherches web : les tâches T4p et T10a ont épuisé leur quota en cours de route, et senat.fr a parfois refusé `curl` et WebFetch. Commencer par les documents qui couvrent beaucoup de mesures à la fois (Voies et moyens tome II, rapports de la Cour des comptes sur l'exécution, rapports du CPO). Noter tout site inaccessible.

### Phase 2 : fusion et fichier aveugle (agent de fusion)

- Fusionner les parts dans `mesures_cout_nouvelles.csv` et `mesures_effets_nouvelles.csv`.
- Contrôler les doublons avec `data/raw/` et entre groupes, ainsi que les sha256.
- Recalculer chaque écart : (ex post central − ex ante) / ex ante.
- Produire `aveugle/mesures_officielles.csv` et `aveugle/effets_annonces.csv` aux colonnes de `recherche/validation/aveugle/`. Ils contiennent seulement : libellé, année, sens, indicateur, chiffrage avant adoption, auteur. Ni réalisé, ni cause, ni note, ni citation de l'ex post.
- Copier `recherche/validation/aveugle/regles_disponibles.csv` tel quel dans `aveugle/`.

### Phase 3 : attribution à l'aveugle (un agent neuf)

L'agent :

- reçoit **uniquement** une copie de `aveugle/`, placée hors du dépôt (dans un dossier vide) ;
- n'a pas accès au web ;
- choisit une règle par ligne d'après la seule nature de la mesure, avec une justification d'une phrase ;
- répond honnêtement à `issue_connue` : `oui` s'il pense connaître le réalisé ou le sens de l'écart, `non` sinon ;
- produit `attribution_agent.csv` aux colonnes `fichier,id,regle,justification,issue_connue`.

Ce fichier est conservé tel quel ; aucune attribution n'est retouchée après coup.

Pour limiter la fuite d'information, la phase 1 signale dans une colonne `realise_publie_le` la date de publication du réalisé. Les cas dont le réalisé est publié en 2026 sont probablement inconnus de l'agent d'attribution ; ils formeront un sous-échantillon à part.

### Phase 4 : intégration (hors tâche)

Revient à l'utilisateur, ou à un agent qui en reçoit la demande : copie dans `data/raw/`, historique, relance de `scripts/validation.py`. La tâche T18 s'arrête au rapport.

## 4. Format des CSV

**`cout_<G>.csv` et `mesures_cout_nouvelles.csv`** : les colonnes de `data/raw/mesures_cout.csv`, dans le même ordre, plus :

| Colonne | Contenu |
|---|---|
| `regle_pressentie` | règle du § 2 qui a motivé la recherche (pour l'analyse ; l'attribution officielle est celle de la phase 3) |
| `comportement_inclus_ex_ante` | `oui`, `non` ou `inconnu` |
| `citation_comportement` | phrase du chiffrage qui le dit, ou vide |
| `annee_ex_ante`, `annee_ex_post` | année à laquelle se rapporte chaque montant |
| `realise_publie_le` | date de publication du réalisé (AAAA-MM-JJ, ou AAAA) |
| `url`, `citation`, `page`, `confiance`, `note` | exigés par `recherche/CONSIGNES.md` ; `citation_ex_ante`, `page_ex_ante`, `citation_ex_post` et `page_ex_post` comme dans T10a |

**`effets_<G>.csv` et `mesures_effets_nouvelles.csv`** : les colonnes de `data/raw/mesures_effets.csv`, plus `regle_pressentie` et `realise_publie_le`.

Signe et unités : ceux de `data/raw/mesures_cout.csv` (montants positifs, sens donné par `sens`, Md€/an).

## 5. Livrables (dans `recherche/T18/`)

- `mesures_cout_nouvelles.csv`, `mesures_effets_nouvelles.csv` ;
- `aveugle/` et `attribution_agent.csv` ;
- `parts/` (fichiers par groupe) ;
- `sources.csv` (fusion des `parts/sources_<G>.csv`) ;
- `rapport.md`, qui contient :
  1. le nombre de cas retenus par règle, `observe` seuls et tous types, face à la cible de 8 ;
  2. pour information, une **statistique provisoire** par règle, calculée en dehors du pipeline avec les facteurs gelés du § 0 : erreur médiane avant et après la règle, améliorés et dégradés. Elle est donnée séparément pour `issue_connue = non`, pour les réalisés publiés en 2026 et pour `comportement_inclus_ex_ante = oui / non` ;
  3. ce qui n'a pas été trouvé, avec les endroits cherchés ;
  4. les décisions laissées à l'intégrateur : règles à restreindre, affaiblir ou retirer au vu des résultats, cas étrangers, exclusions discutables.

Critère de réussite : au moins 8 cas `observe` pour au moins 6 des 10 règles des groupes A à C, et au moins 15 nouvelles lignes d'effets. Si la cible n'est pas atteinte, le dire, règle par règle.
