# T23 : règle « Base juridique contestée », pour les recettes comme pour les dépenses

Consigne préparée le 20/10/2026 (issue #5). Lire d'abord `recherche/CONSIGNES.md` (règles communes ; date d'accès : celle du jour), puis `recherche/T18/CONSIGNE.md` (format des cas passés et attribution à l'aveugle, repris ici), `recherche/T22/CONSIGNE.md` (attribution des familles) et `recherche/T1/convention_application_2024.md` (référence des programmes 2024).

## Pourquoi

La seule règle qui tient compte d'un risque juridique, « Nouvelle assiette : risque juridique » (facteur 0,8), ne vise que les impôts sur une assiette nouvelle (`recherche/validation/aveugle/regles_disponibles.csv`). Une économie ou une dépense exposée à une censure ne reçoit aucune correction : `rn24_preference_nationale` (+6,4 Md€) est en règle « Aucune », alors qu'une taxe nouvelle de même taille serait corrigée.

Cette tâche crée une règle propre, « Base juridique contestée », qui s'applique de la même façon aux recettes, aux économies et aux dépenses, quel que soit le parti. « Nouvelle assiette » garde son rôle (rendement d'un impôt sur une assiette nouvelle, évasion comprise) et ses 5 cas de T18.

Le résultat peut être défavorable à n'importe quel programme, ou à la méthode (facteur proche de 1, trop peu de cas). Il est publié pareil.

## 0. Gel

| Élément | Valeur |
|---|---|
| Commit | `a21f6ad` |
| `data/raw/application_lignes.csv` (sha256) | `07dc5bd71d3d0a548db489359161ba724828fcad6a54d5b7274f4972e72f456a` |
| `data/raw/paniers.csv` (sha256) | `60f922ad579893e1463e2b6ec16cd623882033a1ac222ae3e4332f40bdcd2334` |
| `data/raw/familles.csv` (sha256) | `4bd638e66d772a0d4d378171f07faddb274f87bc61dd9ac8f9a0e53821a21aa5` |
| `data/raw/regles.csv` (sha256) | `bfb4df1bb2c63128642ea68c42a2e69b27cc7d1dbe9d0e9f54f033854aef6074` |
| `data/raw/mesures_cout.csv` (sha256) | `8e523b2163a9c4cb02edb0fdec1e19e0a544c0643a09c305ca8d27ac62632f05` |

## 1. Champ de la règle (fixé avant la recherche)

Ne pas le changer en cours de route. Un cas qu'il règle mal se signale dans le rapport, il ne se corrige pas.

Une mesure est **dans le champ** si, **à la date où elle est votée (cas passés) ou annoncée (programmes)**, l'un des deux critères est rempli :

- **J1, jurisprudence** : une décision antérieure du Conseil constitutionnel, du Conseil d'État, de la Cour de justice de l'Union européenne ou de la Cour européenne des droits de l'homme a déclaré contraire à la Constitution, au droit de l'Union ou à la Convention une disposition **de même nature**. Même nature : même mécanisme (par exemple, condition de nationalité ou de durée de résidence pour une prestation ; impôt qui traite différemment les résidents d'autres États membres) et même motif de censure (égalité, liberté d'établissement, droit de propriété…).
- **J2, le texte le dit** : le programme ou le projet fait lui-même dépendre la mesure d'une révision de la Constitution ou d'un changement de traité (par exemple « par référendum si nécessaire »).

**Hors champ** :

- une censure de procédure (cavalier législatif, « entonnoir », vice de forme) : elle ne dit rien de la mesure elle-même ;
- l'avis d'un chiffreur, d'un juriste ou d'un parti, sans décision J1 ni texte J2 ;
- une décision **postérieure** au vote ou à l'annonce : le champ se juge avec ce qui était connu à la date de la mesure, pas après coup ;
- une mesure qui dépend d'une négociation (budget européen, accord international) sans exiger un changement de traité : c'est un risque de mise en œuvre, pas un risque juridique.

## 2. Ce que l'on cherche

### A. Cas passés (pour mesurer le facteur)

Toutes les mesures budgétaires françaises **votées** entre 2000 et 2025 qui étaient dans le champ (J1) **à la date de leur vote**, qu'elles aient ensuite été censurées ou non. Ne pas chercher seulement les mesures censurées : un échantillon de censures pousse le facteur vers 0 sans rien mesurer.

Méthode de recherche, pour limiter le tri :

1. Partir des décisions qui ont censuré sur le fond une disposition budgétaire ou fiscale (décisions DC sur les lois de finances et de financement de la sécurité sociale, QPC, arrêts de la CJUE sur la fiscalité française, arrêts de la CEDH contre la France en matière de prestations).
2. Pour chacune, chercher les mesures de même nature votées **après** elle, et retenir celles qui ont un chiffrage avant adoption et un réalisé.
3. Noter aussi, à part (`parts/hors_champ.csv`), les mesures censurées alors qu'aucune décision antérieure ne l'annonçait (exemple à vérifier : la contribution de 3 % sur les dividendes, 2012, déjà dans `data/raw/mesures_cout.csv`). Elles ne servent pas au facteur ; le rapport en donne le nombre, pour dire quelle part des censures le champ ne voit pas.

Pour chaque cas retenu : le format de T18 (`recherche/T18/CONSIGNE.md` § 1 et § 4 : chiffrage avant adoption, réalisé sur le même périmètre, `type_ex_post`, `comportement_inclus_ex_ante`, `realise_publie_le`…), plus :

| Colonne | Contenu |
|---|---|
| `critere` | `J1` (seul critère possible pour un cas passé) |
| `decision_anterieure` | référence, date et motif de la décision qui place la mesure dans le champ, avec URL et citation |
| `issue_juridique` | `censurée`, `censurée en partie`, `appliquée`, `retirée avant application`, `restituée` (impôt perçu puis remboursé) |
| `decision_posterieure` | référence de la censure, s'il y en a une, sinon vide |

Le réalisé d'une mesure censurée avant d'être appliquée vaut 0 ; celui d'un impôt restitué est le rendement net des remboursements (comme `taxe_dividendes_3pct_2012`).

Pistes à vérifier (ni leurs chiffres ni même l'existence d'un chiffrage ne sont établis) : conditions de résidence ou de nationalité pour des prestations (loi immigration de 2023 et décisions antérieures sur l'égalité devant les prestations), prélèvements sociaux sur les revenus des non-résidents votés après l'arrêt de Ruyter de la CJUE (`ps_nonresidents_2012`, voté avant cet arrêt, est hors champ), taxe à 75 % (2012, puis contribution des entreprises 2013-2014), mesures fiscales votées après une censure de même nature (contributions sur les hauts revenus, régimes des plus-values).

### B. Mesures des programmes et des paniers (pour appliquer la règle)

Passer en revue **toutes** les lignes de `data/raw/application_lignes.csv` et de `data/raw/paniers.csv`, pas seulement les candidates connues. Pour chacune, une ligne : `id`, `critere` (`J1`, `J2` ou `aucun`), décision ou texte qui la place dans le champ (référence, date, URL, citation), ou « Aucune décision de même nature trouvée » avec les recherches faites.

Candidates déjà notées, à traiter comme les autres : `rn24_preference_nationale`, `rn24_asile`, `nfp_asile`, `rn24_ame`, `l_zucman`, `nfp_taxe_kilometrique`. Cas limites à trancher avec le champ : `nfp_blocage_prix` (liberté d'entreprendre), `rn24_ue` (négociation européenne), les baisses de TVA (directive TVA), `ens_retention` (mesure de niveau européen).

Le champ se juge à la date de l'annonce du programme (juin 2024 pour les programmes 2024 ; date de la mesure pour les paniers), d'après les décisions connues à cette date. Une décision postérieure se note dans la colonne `note`, sans changer le critère.

## 3. Déroulé

1. **Collecte des cas passés** : deux agents en parallèle, un pour la fiscalité (impôts et prélèvements), un pour les prestations et les dépenses. Chacun écrit dans `recherche/T23/parts/` (`cas_<G>.csv`, `hors_champ_<G>.csv`, `notes_<G>.md`, `sources_<G>.csv`), sources dans `sources/T23/<G>/`.
2. **État du droit des lignes de programme** : un agent, sur toutes les lignes (§ 2 B), dans `parts/lignes_programmes.csv`, `parts/notes_programmes.md`, `parts/sources_programmes.csv`.
3. **Fusion** : un agent fusionne, contrôle doublons (avec `data/raw/mesures_cout.csv` et entre groupes) et sha256, recalcule chaque écart, et produit `aveugle/` :
   - `aveugle/cas_passes.csv` : libellé, année, sens, chiffrage avant adoption, auteur, décision antérieure (référence et motif) ; ni réalisé, ni issue juridique, ni décision postérieure ;
   - `aveugle/lignes.csv` : pour chaque ligne de programme, libellé, type, montant et décision ou texte relevé, **sans le programme ni le parti** ;
   - `aveugle/familles.csv` (famille, libellé, justification de `data/raw/familles.csv`) et le champ du § 1.
4. **Attribution à l'aveugle** : un agent neuf, sans web, sur une copie de `aveugle/` hors du dépôt. Pour chaque cas passé et chaque ligne, il dit si la mesure est dans le champ (J1, J2, aucun) d'après le seul texte du § 1. Pour chaque ligne dans le champ, il choisit une famille existante ou en propose une nouvelle, définie par la nature juridique de la mesure (par exemple « prestation conditionnée à la nationalité »), sans connaître la règle qui y sera attachée. Il répond à `issue_connue` (`oui` s'il pense connaître l'issue d'un cas passé). Son fichier `attribution_agent.csv` (`fichier,id,critere,famille,famille_nouvelle,justification,issue_connue`) est conservé tel quel.
5. **Intégration** : hors tâche.

## 4. Facteur (fixé à l'avance)

- Facteur de la règle = médiane, sur les cas passés retenus en `type_ex_post = observe` et jugés dans le champ par l'agent d'attribution, du rapport réalisé / chiffrage avant adoption (après `deflateur_ex_ante`). Un rapport négatif (restitution supérieure au rendement) est gardé tel quel.
- Fourchette : premier et troisième quartiles des mêmes rapports.
- **5 cas ou plus** : la règle est testée comme les autres (`scripts/validation.py`, seuil `MIN_CAS`).
- **1 à 4 cas** : le facteur est calculé de la même façon et la règle est marquée « trop peu de cas » ; l'intégrateur décide de l'appliquer ou non.
- **0 cas** : pas de facteur ; le rapport le dit, et les lignes restent en règle « Aucune ».

Le rapport donne la statistique séparément pour `issue_connue = non`.

## 5. Livrables (dans `recherche/T23/`)

- `cas_passes.csv`, `hors_champ.csv`, `lignes_programmes.csv` ;
- `aveugle/`, `attribution_agent.csv` ;
- `parts/`, `sources.csv` ;
- `rapport.md`, qui donne :
  1. le nombre de cas passés retenus, par critère et par issue juridique, et le nombre de cas hors champ ;
  2. le facteur provisoire et sa fourchette (§ 4), calculés en dehors du pipeline ;
  3. pour chaque programme et chaque panier, les lignes dans le champ, leur montant et le critère ;
  4. ce qui n'a pas été trouvé, avec les endroits cherchés ;
  5. les décisions laissées à l'intégrateur, dont : une ligne dans le champ qui relève aussi de « Nouvelle assiette » (une seule règle par ligne), la règle des familles nouvelles, et le sort de `taxe_dividendes_3pct_2012` et `ps_nonresidents_2012` (aujourd'hui dans le test de « Nouvelle assiette » ; hors champ s'ils ont été votés sans décision antérieure de même nature).

## 6. Critère de réussite, fixé à l'avance

- Toutes les lignes de programme et de panier ont un critère (`J1`, `J2` ou `aucun`), avec sa source ou les recherches faites ;
- au moins 5 cas passés `observe` dans le champ, ou leur absence est expliquée ;
- la recherche des cas passés part des décisions (§ 2 A, étape 1), pas des mesures censurées seules.

## 7. Pour l'intégrateur (rappel, hors tâche)

- Les familles dans le champ reçoivent la règle « Base juridique contestée », la même pour tous les partis ; `garde_fous.py` le vérifie déjà (une famille, une règle).
- La règle multiplie le montant, quel que soit son signe : une dépense exposée à une censure coûte moins, une économie rapporte moins.
- Les totaux « indépendant » ne changent pas ; les corrigés peuvent changer. Chaque changement entre dans `historique.csv`.
