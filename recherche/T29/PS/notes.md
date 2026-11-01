# T29, PS : programme 2027 à partir du programme présidentiel 2022

Notes du 01/11/2026. Consigne : `recherche/T29/CONSIGNE.md`. Exemple suivi : `recherche/T29/RN/`. Aucun fichier de `data/`, `scripts/` ni `web/` n'a été modifié.

## 1. Ce qui a été lu

- Consignes : `AGENTS.md`, `CONTRIBUTING.md`, `recherche/CONSIGNES.md`, `recherche/T1/convention_application_2024.md`, `recherche/T1/rapport.md`, gabarits de `modeles/`, `scripts/garde_fous.py`, `recherche/T22/CONSIGNE.md` (seuil de 1 Md€, reste).
- Lignes `nfp_*` et `rn27_*`, `familles.csv`, `regles.csv`, `statut_reference_2027.csv`, `montee_en_charge.csv`.
- Textes de la référence déjà archivés par T1 (`sources/T1/`) : PLF 2027 (AN n° 3210), évaluations préalables, PLFSS 2027 (AN n° 3211), LFSS 2026 (JO du 31/12/2025).
- Sources nouvelles : `sources.csv` (31 fichiers dans `sources/T29/PS/`, dont 15 fiches Montaigne).

## 2. Programme retenu : présidentiel 2022 (A. Hidalgo)

| Candidat | Date | Chiffrage indépendant mesure par mesure | Décision |
|---|---|---|---|
| Contre-budget 2027 du groupe socialiste | 16/09/2026 | Aucun. Selectra (17/09/2026) : « Ces chiffrages sont les leurs, et n'ont été validés par aucune institution indépendante ». Recherches sans résultat chez Montaigne, l'iFRAP, l'OFCE, Fipeco. Atlantico (H. Spring-Ragain, GénérationLibre, 28/09/2026) : article payant, pas de chiffrage par mesure lisible. francebudget.fr : simulateur sans auteur identifié, qui code ses propres hypothèses. | Écarté |
| Contre-budget PLF 2026 (Blois, fin août 2025) | 2025 | Aucun trouvé | Écarté |
| Projet socialiste, adopté par les militants le 25/06/2026 (83 %) | 2026 | Aucun ; le projet n'est pas chiffré | Écarté (sert seulement à confirmer l'engagement sur les retraites) |
| NFP 2024 | 2024 | Montaigne, iFRAP… | Écarté : programme commun déjà saisi (`nfp_*`, libellé « NFP 2024 (LFI) ») ; le reprendre dupliquerait LFI |
| **Présidentielle 2022, A. Hidalgo** | 2022 | **iFRAP (tableau complet, 30/03/2022) ; Montaigne (15 fiches, sans synthèse ni total)** | **Retenu** |

Le contre-budget de 2026 (39,5 Md€ de recettes nouvelles, dont 15 pour la taxe Zucman, 10 pour la CSG sur les gros héritages et 10 pour la taxe sur le numérique ; 22 Md€ de dépenses ; 17,5 Md€ d'économies et de fraude ; déficit réduit de 24 Md€, presse) n'est donc pas saisi. Le SMIC à 1 700 € nets et la CSG progressive (10 Md€ selon le PS) n'ont pas de ligne. L'intégrateur peut demander une recherche de chiffrages indépendants de la taxe Zucman (CAE, rapports parlementaires de 2025) pour une variante.

**Chiffreur de départ.** Montaigne n'a pas fait de synthèse pour A. Hidalgo (`synthese: false` dans l'API ; elle n'était pas parmi les cinq premiers candidats), mais a chiffré 15 de ses mesures. On prend Montaigne quand il chiffre la mesure (montant `estimation_mediane`), l'iFRAP sinon, comme pour les lignes RN que Montaigne ne chiffrait pas (`rn27_fraude`, `rn27_iff`…). Il n'y a donc pas de ligne mère ni de total publié à respecter. Le reste regroupe les postes sous 1 Md€ des deux chiffreurs (iFRAP −2,5 ; Montaigne −0,56, mesures absentes du tableau iFRAP).

**Horizon.** Montaigne 2022 : « par an », mesure du quinquennat 2022-2027 (champ `temporalite`). iFRAP 2022 : solde 2027, « dans le cas d'une application complète des mesures ». `ps27_retraites` : Montaigne 2024, 2027, Md€/an. Annulations : 2027, Md€/an. L'horizon de chaque ligne est dans sa justification et dans `chiffrages.csv`.

## 3. Lignes (36)

Solde de départ (somme des montants) : **−60,5 Md€/an** (dépenses et baisses d'impôts −131,4 ; recettes et économies +78,2 ; annulations −6,4 ; charge d'intérêts −1,0).

| Ligne | Montant | Chiffreur | Autre | Famille, règle | Référence 2027 (facteur ; loi votée seule) |
|---|---|---|---|---|---|
| `ps27_smic` | −4,1 | Montaigne | iFRAP −4 | smic_cout_direct, Aucune | votée, 0 (SMIC net à 1 469 € dépassé) |
| `ps27_chomage_universelle` | −4,8 | iFRAP | — | assurance_chomage, Aucune | absente, 1 |
| `ps27_chomage_abrogation` | −2,0 | Montaigne | — | assurance_chomage, Aucune | absente, 1 |
| `ps27_enseignants` | −54,3 | Montaigne | iFRAP −7,8 | masse_salariale_publique, Aucune | absente, 1 |
| `ps27_mixite` | −2,0 | iFRAP | — | credits_sectoriels, Aucune | absente, 1 |
| `ps27_retraites` | −8,2 | Montaigne (NFP 2024, composante) | iFRAP 2022 : 0 | retraites_age, Substitution retraites | partielle, 0,878 ; 0,878 |
| `ps27_min_vieillesse` | −2,6 | Montaigne | iFRAP −1,3 | revalorisation_prestation, Aucune | partielle, 0,769 ; 0,769 |
| `ps27_soignants` | −5,5 | Montaigne | iFRAP −1,9 | masse_salariale_publique, Aucune | absente, 1 |
| `ps27_accueil_enfant` | −2,5 | iFRAP | — | credits_sectoriels, Aucune | absente, 1 |
| `ps27_logements_sociaux` | −7,5 | iFRAP | — | investissement_public, Aucune | absente, 1 |
| `ps27_armee` | −2,0 | iFRAP | — | credits_sectoriels, Aucune | partielle, 0,5 [0 ; 1] ; 0,5 |
| `ps27_policiers` | −1,1 | iFRAP | — | masse_salariale_publique, Aucune | partielle, 0,5 [0 ; 1] ; 1 |
| `ps27_vss` | −1,0 | iFRAP | — | credits_sectoriels, Aucune | absente, 1 |
| `ps27_co2_industrie` | −2,0 | iFRAP | — | aides_transition_ecologique, Aucune | absente, 1 |
| `ps27_recherche` | −8,4 | iFRAP | — | credits_sectoriels, Aucune | absente, 1 |
| `ps27_capital_jeunes` | −4,1 | Montaigne | iFRAP −3,25 ; candidate −4 | credits_sectoriels, Aucune | absente, 1 |
| `ps27_minimum_jeunesse` | −2,7 | iFRAP | — | prestation_nouvelle, Aucune (exception) | absente, 1 |
| `ps27_conge_paternite` | −1,2 | iFRAP | — | revalorisation_prestation, Aucune | partielle, 0,5 [0 ; 1] ; 0,5 |
| `ps27_depenses_nefastes` | +2,0 | iFRAP | — | aides_entreprises, Aucune | absente, 1 |
| `ps27_autres_dep_reste` | −3,06 | iFRAP et Montaigne | — | residu, Aucune | absente, 1 |
| `ps27_tva_carburants` | −6,56 | Montaigne (calcul de répartition) | iFRAP −1,92 | taxe_carburants, Élasticité carburants | absente, 1 |
| `ps27_tva_elec_gaz` | −3,74 | Montaigne (calcul de répartition) | iFRAP −10,8 | taxe_electricite_gaz, Élasticité électricité | absente, 1 |
| `ps27_tva_train_reemploi` | −2,0 | iFRAP | — | tva_produits, Aucune | absente, 1 |
| `ps27_salaires_1_20` | +9,1 | iFRAP | — | impot_societes, Élasticité IS | absente, 1 |
| `ps27_egalite_penalites` | +20,0 | iFRAP | — | effet_promis, Effet promis | absente, 1 |
| `ps27_flat` | +1,8 | iFRAP | — | impot_revenu_capital, Élasticité capital | absente, 1 |
| `ps27_isf` | +3,0 | Montaigne | iFRAP 4 ; candidate 4 | impot_patrimoine, Élasticité patrimoine | partielle, 0,967 ; 0,967 |
| `ps27_successions` | +6,3 | Montaigne | iFRAP 8 | succession, Élasticité succession | partielle, 0,881 [0,762 ; 1] ; 0,881 |
| `ps27_multinationales` | +6,0 | iFRAP | — | impot_multinationales, Médiane des estimations | partielle, 0,917 ; 0,917 |
| `ps27_fraude` | +5,0 | iFRAP | — | effet_promis, Effet promis | partielle, 0,8 ; 1 |
| `ps27_niches_ecologiques` | +7,0 | iFRAP | — | taxe_carburants, Élasticité carburants | partielle, 0,956 ; 0,956 |
| `ps27_niches` | +18,0 | iFRAP | — | niches_fiscales, Médiane des estimations | absente, 1 |
| `ps27_annul_pensions` | −4,0 | PLFSS 2027, art. 35 | — | annulation_economie_reference | absente, 1 ; 0 |
| `ps27_annul_abattement` | −1,4 | PLF 2027, art. 3 | — | annulation_economie_reference | absente, 1 ; 0 |
| `ps27_annul_ij` | −0,965 | PLF 2027, art. 2 | — | annulation_economie_reference | absente, 1 ; 0 |
| `ps27_taux` | −1,0 | calcul | — | charge_interets, Taux d'intérêt | absente, 1 |

**Familles.** Chaque famille reprend celle d'une ligne de même nature déjà saisie (citée dans la justification), sauf trois cas sans précédent :

- `ps27_capital_jeunes` : `credits_sectoriels` (versement universel à une classe d'âge, ni prestation sous condition ni prestation existante) ;
- `ps27_conge_paternite` : `revalorisation_prestation` (allongement d'une prestation existante) ;
- `ps27_depenses_nefastes` : `aides_entreprises` (baisse d'aides budgétaires).

`ps27_minimum_jeunesse` est de la famille de `nfp_autonomie` (`prestation_nouvelle`), mais sans la règle « Taux de recours » : l'iFRAP ne dit pas si son chiffrage suppose un recours complet, condition du garde-fou RECOURS. D'où `exception_symetrie` et une alerte des garde-fous.

**Découpage de la TVA sur l'énergie.** Montaigne chiffre 10,3 Md€ pour l'ensemble. On répartit selon l'assiette taxée à 20 % donnée dans sa fiche (2018) : produits pétroliers 9 047, gaz 1 282, électricité 3 872 sur 14 201 M€. Cela donne 6,56 pour les carburants et 3,74 pour l'électricité et le gaz, même méthode que `rn27_tva_*`.

## 4. Statuts par rapport à la référence 2027 qui changent le montant

- **SMIC (`votée`, 0).** Le libellé Montaigne est « augmenter le SMIC net à 1 469 € ». Le SMIC brut est de 1 867,02 € au 1er juin 2026 (MDA 06) et le net de 1 477,93 € (Selectra, source secondaire). La promesse en niveau est déjà atteinte, d'où le statut `votée`, facteur 0 (garde-fou DOUBLE COMPTE).
- **Retraites (`partielle`, 0,878).** En 2022, garder 62 ans ne coûtait rien (iFRAP : 0). Par rapport à 2027, cela revient à abroger la réforme de 2023, ce que le PS promet toujours (Projet socialiste 2026). Le montant est la composante « abrogation 2023 » (8,2) du chiffrage Montaigne de `nfp_retraites`, seul chiffrage indépendant de cette mesure, déjà utilisé pour `rn27_retraites`. On retranche la suspension (1,0, PLFSS 2027) : (8,2 − 1,0) / 8,2.
- **Minimum vieillesse (`partielle`, 0,769).** L'ASPA vaut 12 523,14 € par an (1 043,60 € par mois) au 1er janvier 2026, au-dessus des 1 000 € promis. La part ASPA du chiffrage Montaigne (0,6) est donc atteinte.
- **Armée, policiers, congé de paternité (`partielle`, 0,5).** Le recoupement existe mais n'est pas chiffrable, d'où le milieu de [0 ; 1] (convention de T1, comme `rn27_prisons`), avec une confiance faible :
  - armée : « La France aura doublé le budget consacré à la Défense depuis 2017 », PLF 2027 ;
  - policiers : « +1,0 Md€ pour le ministère de l'Intérieur permettant le recrutement de 235 gendarmes et 970 policiers », PLF 2027 ;
  - congé de paternité : congé supplémentaire de naissance, LFSS 2026, art. 99.
- **ISF, successions, multinationales, fraude, niches écologiques.** Même calcul que pour les lignes NFP, RN ou paniers de même nature (`nfp_isf`, `nfp_succession`, `nfp_zucman`, `ens_fraude`, `l_brunes`), appliqué aux montants du PS.

**`facteur_reference_loi_votee`** (colonne ajoutée en fin de `lignes.csv`) est rempli quand le facteur est inférieur à 1 ou pour les annulations :

- **Recoupement voté** (LFSS 2026, LFI 2026, Pilier 2, LPM, budget vert) : même valeur que le facteur ;
- **Recoupement tiré du seul PLF 2027** : 1 (`ps27_policiers`, et `ps27_fraude` comme `rn27_fraude`) ;
- **Annulations** : 0.

## 5. Annulations de la référence (règle 4)

| Ligne | Économie annulée | Montant | Engagement daté |
|---|---|---|---|
| `ps27_annul_pensions` | Sous-indexation des pensions (PLFSS 2027, art. 35) | −4,0 | Amendements de suppression n° AS17 (Mme Runel et des députés socialistes, commission, 03/10/2026, « Adopté ») et n° 117 (« les membres du groupe Socialistes et apparentés », séance, 08/10/2026) : « vise à supprimer la désindexation partielle des pensions de retraites pour 2027 » |
| `ps27_annul_abattement` | Abattement de 10 % des retraités plafonné à 3 000 € (PLF 2027, art. 3) | −1,4 | Scrutin public n° 8738 (15/10/2026) sur les amendements de suppression de l'art. 3 : groupe Socialistes et apparentés, « Pour : 15 », aucun contre. Le groupe n'a pas déposé d'amendement de suppression en séance (Légifiscal) : l'engagement est un vote, pas un amendement |
| `ps27_annul_ij` | Fiscalisation des indemnités journalières des ALD et des AT/MP (PLF 2027, art. 2) | −0,965 | Amendement n° I-502 (groupe Socialistes et apparentés, 08/10/2026, « Adopté ») : « supprimer les alinéas qui viennent fiscaliser les indemnités ». Montant : évaluations préalables, art. 2, § 4.2.1.4 (965 M€ en 2027). L'alignement du taux de CSG des indemnités (540 M€), qui n'est pas dans le PLF, n'est pas visé |

Pas de ligne, faute de source datée du groupe ou du parti :

- gel des prestations familiales (PLFSS 2027, 0,5) ;
- gel de la prime d'activité et des APL (PLF 2027, art. 74) ;
- gel du point d'indice ;
- gel des allègements généraux.

La suspension de la réforme des retraites n'est pas une économie de la référence. L'abrogation est la ligne `ps27_retraites`.

## 6. Charge d'intérêts et montée en charge

- **`ps27_taux`.** Même règle que `rn27_taux`. On prend la somme des lignes `ps27_` (hors `ps27_taux`), chacune pour sa part hors référence 2027, soit −54,3 Md€/an.
  - Dette supplémentaire : −54,3 × 2,5 / 3 135 ≈ 4,3 points, × 2,5 pb ≈ 11 pb.
  - Charge : 0,96 × 54,3 / 49,8 = −1,05, arrondie à −1,0.
  - Avec les montants bruts (−59,5) : −1,15.
  - Aucune ligne ne contient de spread propre (pas d'équivalent de `rn27_ptz`).
- **Profil.** `ps27_retraites` (famille `retraites_age`) reprend le profil de `l_ret62` tel quel (`montee_en_charge.csv`), puisque la ligne ne porte que l'abrogation de 2023. Les lignes d'annulation n'ont pas de profil, comme celles du RN.

## 7. Vérification

Copie du dépôt dans le dossier temporaire de la session, avec les cinq fichiers ajoutés à `data/raw/` (`application_lignes`, `statut_reference_2027`, `montee_en_charge`, `application_programmes`, `chiffrages_instituts`). `build.py`, `moteur.py`, `projection.py` et `check_regression.py` passent. `garde_fous.py` : **0 erreur, 1 alerte** (exception de famille de `ps27_minimum_jeunesse`).

- Solde de départ : −60,5 Md€/an.
- Solde corrigé par le moteur : **−73,1** (P10 −90,4 ; P50 −69,2 ; P90 −47,5). Variante « loi votée seule » : −67,0.

Le solde corrigé est plus bas que le solde de départ parce que les recettes « effet promis » sont divisées par trois : égalité salariale 20 → 5,8, fraude 5 → 1,2.

`test_web.py` n'a pas été lancé.

## 8. Décisions laissées à l'intégrateur

1. **Enseignants (−54,3).** Montaigne chiffre la proposition initiale (doublement, 47) plus la grille (7,3) : sa proposition révisée était imprécise. L'iFRAP retient 7,8. Avec 7,8, le solde corrigé passerait d'environ −73 à environ −27. C'est la ligne qui pèse le plus.
2. **Soignants (−5,5).** Le champ de Montaigne dit « 5,5 Md€ par an », son texte « 5,5 Md€ sur l'ensemble du quinquennat » (soit ≈1,1 par an). L'iFRAP retient 1,9.
3. **Choix du programme.** Faut-il garder un programme de 2022, dont plusieurs mesures ont vieilli (SMIC, ASPA), ou attendre un chiffrage indépendant du contre-budget 2026 ou du programme 2027 ?
4. `ps27_retraites` : faut-il emprunter le montant à une fiche Montaigne d'un autre programme (NFP 2024) ? La consigne T29 ne le prévoit pas explicitement. La solution alternative est une ligne non chiffrée à 0, comme `rn27_cvae`.
5. Familles sans précédent (`ps27_capital_jeunes`, `ps27_conge_paternite`, `ps27_depenses_nefastes`) et exception de `ps27_minimum_jeunesse`.
6. Facteurs 0,5 de confiance faible (armée, policiers, congé de paternité).
7. `ps27_annul_abattement` repose sur un vote (15 voix socialistes), pas sur un amendement : est-ce suffisant au sens de la règle 4 ?
8. `solde_montaigne` vide dans `entete.csv` : Montaigne n'a pas publié de total pour A. Hidalgo.

## 9. Lacunes

- Pas de chiffrage indépendant du contre-budget 2027 ni du Projet socialiste 2026.
- Pas de méthode détaillée de l'iFRAP 2022 : seulement le tableau image. Le périmètre des postes « baisse de la TVA sur l'énergie » (10,8) et « TVA carburants (1 an) » (1,92) reste incertain.
- Non lus :
  - la LOPMI (policiers) ;
  - la revalorisation du minimum contributif de 2023 (`ps27_min_vieillesse`) ;
  - les aides France 2030 à la décarbonation (`ps27_co2_industrie`).
- SMIC net de juin 2026 : source secondaire seulement (Selectra). Le brut vient de la MDA 06 ; service-public.fr et le JO n'ont pas été lus.
- Amendements socialistes sur l'art. 74 du PLF 2027 (gels de la prime d'activité et des APL) et sur le gel des prestations familiales du PLFSS 2027 : non trouvés.
