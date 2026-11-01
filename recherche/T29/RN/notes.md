# T29, RN : programme 2027 à partir du programme des législatives 2024

Notes du 01/11/2026. Consigne : `recherche/T29/CONSIGNE.md`. Aucun fichier de `data/`, `scripts/` ni `web/` n'a été modifié.

## 1. Ce qui a été lu

- Consignes : `AGENTS.md`, `CONTRIBUTING.md`, `recherche/CONSIGNES.md`, `recherche/T1/convention_application_2024.md`, `recherche/T1/rapport.md`, gabarits de `modeles/`, `scripts/garde_fous.py`.
- Lignes `rn24_*` (`data/raw/application_lignes.csv`, 32 lignes), leurs chiffrages (`chiffrages_instituts.csv`) et leur statut 2027 (`statut_reference_2027.csv`).
- T24 (chômage), T25 (prisons, rente inframarginale, CVAE), T21 et T26 § 1 (calcul de `rn24_taux`), T14 (profil de `l_ret60`).
- Sources nouvelles : `sources.csv` (10 fichiers dans `sources/T29/RN/`).

Le RN n'a publié aucun programme pour 2027 au 01/11/2026. franceinfo (21/05/2026) rapporte que le parti « boucle son programme » et que l'âge de départ divise les équipes de M. Le Pen et de J. Bardella. Le programme de 2024 reste donc le dernier programme chiffré.

## 2. Méthode

Les lignes sont produites par un script (gardé dans le dossier temporaire de la session) à partir des fichiers du dépôt.

- **Une ligne `rn27_X` par ligne `rn24_X`.** Elle reprend le libellé, le montant, le chiffreur, les autres estimations, la famille, la règle, le facteur, l'URL et la confiance. La justification de 2024 est gardée et complétée par l'origine de la ligne et l'horizon du montant (colonne `horizon` de `chiffrages_instituts.csv`, pour le chiffreur retenu).
- **Statut et facteur de référence** : ceux du registre (`statut_reference`, `facteur_suggere`), sauf les cas du § 3. `source_reference` assemble le texte, la citation et l'URL du registre. `note_reference` reprend la note du registre.
- **`registre.csv`** : une ligne par ligne `rn27_`, copiée de la ligne `rn24_` correspondante, sauf les cas du § 3.
- **Colonnes** : celles de `modeles/programme_2027.csv`, plus deux colonnes ajoutées à la fin, `facteur_reference_bas` et `facteur_reference_haut`. Le schéma `LigneApplication` les connaît déjà, mais `application_lignes.csv` ne les a pas encore. Seule `rn27_prisons` s'en sert.

## 3. Lignes réexaminées

| Ligne | 2024 (droit de juin 2024) | Registre 2027 | T29 | Compté | Raison |
|---|---|---|---|---|---|
| `rn27_chomage` | votée, 0 | votée, 1 | **votée, 0** | 0 | Voir ci-dessous |
| `rn27_prisons` | partielle, 0,06 | partielle, 1 | **partielle, 0,5 [0,06 ; 1]** | −0,75 | Voir ci-dessous |
| `rn27_cvae` (nouvelle) | (exclue du montant de `rn24_production`) | — | absente, montant 0 | 0 | Voir ci-dessous |
| `rn27_rente_infra` | Recette ponctuelle, 0 | absente, 1 | inchangé | 0 | La contribution ne rapporte rien en 2027 (PLF 2027, état A, ligne 1752). Le recoupement avec le programme de stabilité de 2024 (T25 § 4) n'a plus d'objet. La règle « Recette ponctuelle » la laisse à 0 de toute façon. |
| `rn27_taux` | −1,0 | — | recalculée | −1,0 | Voir ci-dessous |

**Chômage.** En 2024, la ligne comptait 0 parce que la réforme visée n'était pas dans le droit de juin 2024 (T24). Cette réforme n'a jamais été prise. Le décret n° 2024-648 l'a suspendue. La convention du 15/11/2024 s'est ensuite substituée au décret de 2019 (Unédic, circulaire n° 2025-03). Par rapport à 2027, annuler la réforme de juillet 2024 ne coûte donc toujours rien.

- La référence 2027 contient d'autres textes : la convention de 2024 et les réformes de 2025-2026, dont le PLF 2027 compte la montée en charge sans montant isolé (T1).
- Le programme de 2024 ne promet pas de les annuler, et aucun engagement de 2025-2026 en ce sens n'a été trouvé.
- Le registre indique « votée, facteur 1 » pour `rn24_chomage`. Telle quelle, cette valeur ferait échouer le garde-fou DOUBLE COMPTE : elle est corrigée à 0, avec `raison_ecart`.

**Prisons.** T25 retenait 6 % parce que le plan 15 000 était financé en juin 2024 (loi de programmation n° 2023-1059, budget 2024). En 2027, ce motif ne tient plus tel quel. Selon le Sénat (rapport n° 736 du 17/06/2026, annexe Justice, p. 21-22) :

- le plan n'était « réalisé qu'à hauteur de 37 % à la fin 2025 » ;
- son surcoût atteint 46 % ;
- les arbitrages de financement n'étaient « toujours pas » rendus en décembre 2025, selon la Cour des comptes ;
- la loi de programmation se termine en 2027.

Le PLF 2027 ajoute toutefois 0,4 Md€ pour l'immobilier pénitentiaire. On retient donc un facteur central de 0,5, milieu de l'intervalle [0,06 (financement de 2024) ; 1 (aucune part financée établie)], avec une confiance faible : c'est la convention de T1 pour un recoupement qu'on ne sait pas chiffrer. L'audit flash de la Cour des comptes (décembre 2025) n'a pas été lu et permettrait de préciser ce facteur.

**CVAE.** En 2024, le libellé de `rn24_production` comprenait « poursuite de la baisse de la CVAE ». Montaigne ne chiffrait que la C3S, parce que la suppression de la CVAE était déjà votée (T25 § 5).

- Dans la référence 2027, la CVAE rapporte encore 4,11 Md€ (PLF 2027, état A, ligne 1497) : la baisse promise coûterait donc par rapport à 2027.
- Le programme ne dit ni son rythme ni son ampleur, et aucun chiffreur ne l'évalue. Elle entre dans une ligne non chiffrée (montant 0, règle 1). Les 4,11 Md€ sont un plafond (suppression totale), pas un chiffrage.

**Charge d'intérêts.** Même règle que `rn24_taux` (T21, T26 § 1) :

1. Assiette : la somme des lignes `rn27_`, sans `rn27_ptz` (dont le montant contient déjà un spread) ni `rn27_taux`. Chaque ligne est comptée pour sa part hors référence 2027 (montant × facteur de référence), soit −50,3 Md€/an.
2. Dette supplémentaire : −50,3 × ≈2,5 ans / 3 135 Md€ de PIB ≈ 4,0 points ; × 2,5 pb par point ≈ 10 pb.
3. Charge : −0,96 × (−50,3 / −49,8) = −0,97, arrondie à −1,0. Le rapport Md€ par pb est celui de `rn24_taux` (0,96 / 9,9 pb).

Avec les montants bruts, comme en 2024, la charge serait de −1,06, soit −1,1 une fois arrondie. Le choix de l'assiette (part hors référence plutôt que montant brut) est laissé à l'intégrateur. Il ne change le solde que de 0,1.

## 4. Statuts 2027 qui changent le montant compté (par rapport à `rn24_`)

Ces écarts viennent du registre, dont les valeurs sont reprises :

| Ligne | Facteur de référence 2024 → 2027 | Compté 2024 → 2027 (moteur) |
|---|---|---|
| `rn27_retraites` | 1 → 0,971 | −27,76 → −26,95 |
| `rn27_fraude` | 1 → 0,67 | 0,87 → 0,58 |
| `rn27_armateurs` | 1 → 0,73 | 1,03 → 0,75 |
| `rn27_iff` | 1 → 0,975 | 3,88 → 3,78 |
| `rn27_prisons` (§ 3) | 0,06 → 0,5 | −0,09 → −0,75 |

`rn27_chomage` reste à 0. `rn27_agences` est « partielle » au facteur 1 : le recoupement avec les économies sur les opérateurs n'est pas chiffrable (registre).

## 5. Engagements d'annuler des économies de la référence 2027 (règle 4)

| Ligne | Économie annulée | Montant | Source de l'engagement |
|---|---|---|---|
| `rn27_annul_pensions` | Sous-indexation des pensions au-dessus de 1 260 € (PLFSS 2027, art. 35) | −4,0 | Amendements de suppression n° AS378 (commission des affaires sociales, « Adopté ») et n° 2241 (séance, 16/10/2026), « M. Ménagé et les membres du groupe Rassemblement National » : « Le groupe Rassemblement National sollicite donc la suppression de l'article 35 ». Montant : PLFSS 2027, art. 35, exposé des motifs (4,0 Md€, dont 3,0 pour la branche vieillesse). |
| `rn27_annul_abattement` | Plafond de l'abattement de 10 % des retraités ramené à 3 000 € (PLF 2027, art. 3) | −1,4 | Amendement n° I-633, « Mme Le Pen et les membres du groupe Rassemblement National », déposé le 08/10/2026, « Adopté » (art. 3 supprimé en séance le 15/10/2026 par sept amendements identiques, 116 voix contre 30, franceinfo et Légifiscal) : « Pour le Rassemblement national, aucun nouvel effort ne peut être imposé aux retraités ». Montant : évaluations préalables du PLF 2027, art. 3 (1,4 Md€ en 2027). |

Contexte, sans ligne :

- Le PLFSS 2027 a été rejeté par l'Assemblée le 23/10/2026. Une députée RN, S. Dogor-Such (communiqué relayé par Ouillade, presse locale, 24/10/2026), dit que ce rejet « préserve » l'indexation des retraites. Ce n'est qu'une source secondaire : elle n'a pas servi pour la ligne.
- Pas de ligne pour les autres économies :
  - **Jours fériés** : la mesure est absente de la référence 2027 (abandonnée en septembre 2025, T1), donc rien à annuler.
  - **Gels de prestations** (prime d'activité −0,33 et APL −0,10, PLF 2027, art. 74) : aucun amendement ni aucune déclaration du RN trouvés. La seconde partie du PLF ne semble pas encore examinée.
  - **Point d'indice** (gel 2027) : rien trouvé dans le temps imparti.
  - **Gel du SMIC de référence des allègements et assiette des allègements** (PLFSS 2027, art. 7) : la députée cite la défense des « exonérations de cotisations », mais aucun amendement RN n'a été lu. Pas de ligne.
- Déclarations de M. Le Pen et de J. Bardella sur ces mesures en 2026 : aucune trouvée en dehors des amendements. Nosparlementaires.fr cite une phrase de M. Le Pen de décembre 2025 (« La désindexation des pensions est une violation de la loi ») sans source primaire lue : elle n'a pas été retenue.

## 6. Montée en charge

- `rn27_retraites` (famille `retraites_age`, profilée par `l_ret60` et `l_ret62`) : le garde-fou PROFIL exige un profil. On applique le mécanisme de `l_ret60` (T14), adapté à la composition du chiffrage de Montaigne : (26,5 + 6,3 × coefficient de `l_ret62`) / 32,8. Les 8,2 Md€ de l'abrogation de 2023, moins la suspension (1,9 selon la convention de T14), suivent `l_ret62`. Les 26,5 restants sont supposés constants en % du PIB. Le coefficient central passe de 1,06 en 2028 à 1,19 en 2032.
  - Point de vigilance : T14 retient une suspension de 1,9, alors que le facteur de référence (0,971) utilise 1,0 (PLFSS 2027). L'écart est repris tel quel de `l_ret60`.
- Lignes d'annulation : pas de profil. Celui de l'abattement est publié (1,8 Md€ en 2028, 1,1 à partir de 2029), pas celui de la sous-indexation, dont l'effet sur le niveau des pensions persiste. En profiler une seule obligerait à profiler l'autre (garde-fou PROFIL). À trancher par l'intégrateur.

## 7. Vérification

Dans une copie du dépôt (dossier temporaire de la session), avec les quatre fichiers ajoutés à `data/raw/`, `build.py`, `moteur.py`, `projection.py` et `garde_fous.py` passent : 0 erreur, 0 alerte.

- Solde de départ (somme des montants) : −68,8 Md€/an.
- Solde corrigé par le moteur : **−59,8** (P10 −71,2 ; P50 −57,4 ; P90 −43,6), contre −53,9 pour RN 2024 dans la même sortie.
- Variante « loi votée seule » : −59,8 aussi, à cause du point 1 du § 8.

`test_web.py` n'a pas été lancé.

## 8. Décisions laissées à l'intégrateur

1. **Variante « loi votée seule »** : les deux lignes d'annulation y comptent encore, alors que les économies annulées n'existent que dans le PLF et le PLFSS (le PLFSS a été rejeté le 23/10). Il faudrait une colonne `facteur_reference_loi_votee` dans `application_lignes.csv` (elle n'existe que pour `paniers.csv`) et la mettre à 0 sur ces lignes. Effet : +5,4 sur cette variante.
2. Ajouter à `application_lignes.csv` les colonnes `facteur_reference_2028`, `facteur_reference_bas` et `facteur_reference_haut`.
3. `rn27_prisons` : facteur 0,5 de confiance faible, ou 1 (registre) ?
4. `rn27_taux` : assiette hors référence (−1,0) ou montants bruts (−1,1) ?
5. Faut-il ajouter des lignes `rn27_` à `chiffrages_instituts.csv` ? Le champ `autres_estimations` renvoie à ce fichier, qui n'a que les lignes `rn24_`.
6. `solde_montaigne` est vide dans `entete.csv` : le −71 de Montaigne se mesure par rapport au droit de juin 2024.

## 9. Lacunes

- L'audit flash de la Cour des comptes sur le plan 15 000 (décembre 2025) et la NEB Justice 2025 n'ont pas été lus.
- Les numéros des amendements RN de commission sur l'art. 3 du PLF 2027 n'ont pas été trouvés : le n° I-633 en séance suffit.
- Aucune recherche sur les amendements RN à l'art. 74 du PLF 2027 (gels de prestations) ni sur le point d'indice.
- Le montant 2027 des réformes de l'assurance chômage de la référence n'est pas isolé (comme dans T1).
- Les vigilances du registre restent non chiffrées : abonnements d'électricité et de gaz repassés au taux normal (`rn27_tva_elec_gaz`), Dutreil restreint (`rn27_transmissions`).
