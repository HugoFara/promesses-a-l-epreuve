# T26 : analyse de l'intégrateur (points du groupe 1 traitables avec le dépôt)

Rapport du 01/11/2026. Il porte sur les points du « groupe 1 » (ceux qui peuvent changer un chiffre publié) qui ne demandent pas de source nouvelle. Les autres sont confiés aux agents A et B (`CONSIGNE.md`). Les propositions ont été validées et appliquées le 01/11/2026 (§ 9).

## 1. PTZ du RN et charge d'intérêts `rn24_taux` : double compte du spread

**Constat (vérifié).** La fiche Montaigne de 2022, d'où vient le montant de 12,6 Md€ (`sources/T22/RN/montaigne_mlp2022_ptz_wb20240713.html`), compte dans le coût du PTZ un surcoût de spread sur toute la dette publique : « L'hypothèse moyenne ne retient qu'une hausse du spread d'un demi-point dans l'hypothèse centrale, soit un surcoût à l'horizon du quinquennat de 7,5 Md€ ». Le reste se compose de 2,2 Md€ d'intérêts pris en charge, des défaillances et du non-remboursement au 3e enfant. Le PDF de 2024 reprend le même montant sans donner de méthode.

La ligne `rn24_ptz` (−12,6) entre dans le solde des lignes (−62,4) qui sert à calculer `rn24_taux` (−1,2 ; 2,5 pb par point de dette). Le spread de cette ligne est donc compté deux fois : une fois par Montaigne, à son propre taux de 5 pb par point (0,5 point pour environ 10 points de dette), et une fois par le site.

**Options.**

| Option | Effet sur le solde RN 2024 | Remarque |
|---|---|---|
| (a) Garder tel quel | 0 | Double compte d'environ 0,24 Md€ |
| (b) Retirer `rn24_ptz` de l'assiette de `rn24_taux` | +0,2 (`rn24_taux` −1,2 → −1,0) | Règle générale : une ligne dont le montant du chiffreur contient déjà un surcoût de taux sort de l'assiette de la ligne `*_taux`. Elle s'applique à tous les programmes ; aucune autre ligne n'est signalée dans les notes de découpage (T6, T17, T22) |
| (c) Ne garder que la part hors spread (5,1) | +7,5 | Décomposition de 2022, non republiée en 2024 : contraire à la règle du montant du chiffreur (T22, § 1.1) |

**Proposition : (b).** Elle est minimale, et ne touche pas au montant du chiffreur. La justification de `rn24_ptz` mentionnera le spread inclus dans le montant.

## 2. Retraites : faut-il appliquer la décote du backtest au coût d'une baisse de l'âge ?

**Point de l'audit (§ 1.4).** La couche 1 montre que les réformes des retraites rapportent 82 à 86 % de leur chiffrage (`facteur_reforme`, 0,842). Cette décote sert à la règle « Réforme structurelle » (économies d'Ensemble et du RN sur l'État). Elle n'est pas appliquée aux lignes de la famille `retraites_age`, qui ne reçoivent que la règle « Substitution retraites » (0,8).

**Ce que montrent les deux cas du backtest.**

- `woerth_2010` : cause de l'écart « Conjoncture + report vers chômage/invalidité », et la note dit « ≈1/3 des économies compensées par chômage/invalidité ». Ce report est déjà la règle « Substitution retraites ». L'ajouter compterait deux fois le même effet.
- `retraites_2023` : cause « Concessions parlementaires + conjoncture ». Les concessions modifient la mesure pendant son adoption ; elles ne disent rien du coût d'un retour en arrière une fois la mesure votée. C'est de plus une réestimation de la Cour (`type_ex_post` = `reestimation`), et non un réalisé observé : depuis T20, seuls les réalisés observés jugent une règle.

**Effet si on l'appliquait** (0,842 en plus de 0,8) : NFP 2024 +7,3 ; RN 2024 +4,4 ; panier LFI +7,1. Ce serait le plus gros changement du groupe.

**Proposition : ne pas l'appliquer.** Le motif sera écrit dans la justification des lignes `retraites_age` : la part de l'écart due au report vers d'autres dépenses est déjà comptée, et le reste vient de concessions propres à la réforme de 2023. Le point de l'audit est clos comme « écarté, avec motif ».

## 3. Variante « loi votée seule » : lignes « partielle » dont le recoupement vient d'un projet

**Constat.** `scripts/moteur.py` (l. 138) ne retire la décote de référence que pour le statut « proposée ». Une ligne « partielle » dont le recoupement vient en partie d'un PLF ou PLFSS 2027 garde donc dans cette variante une décote qui dépend d'un texte non voté.

| Ligne | Facteur actuel | Part proposée du recoupement | Facteur « loi votée seule » | Calcul |
|---|---|---|---|---|
| `l_bandeaux` (LFI) | 0,4 [0,26 ; 0,50] proposé (§ 6) | gel 2027 et assiette (art. 7) | 0,55 [0,44 ; 0,63] | modèle de l'agent A, RGDU et gel 2026 seuls (§ 6) |
| `e_carence` (Ensemble) | 0,5 [0 ; 1] | tout (1 Md€ d'économies sur les IJ, PLFSS 2027) | 1 | aucun recoupement voté |
| `e_appr` (Ensemble) | 0,67 [0,5 ; 0,84] | −0,46 Md€ de CP (PLF 2027) | 0,83 | milieu de [0,5 + 0,46 / 2,86 = 0,66 ; 1] |
| `l_succ` (LFI) | 0,91 | aucune (le recoupement vient de la LFI 2026) | 0,91 | inchangé |

**Proposition.** Ajouter une colonne `facteur_reference_loi_votee` à `paniers.csv`, sur le modèle de `facteur_reference_2028`. Le moteur l'utilise quand elle est remplie ; sinon il garde la règle actuelle. `garde_fous.py` vérifie qu'elle est remplie pour toute ligne « partielle » dont la source de référence cite un PLF ou PLFSS 2027. Les valeurs de `l_bandeaux` et `e_carence` viennent de l'agent A (§ 6). Le PLFSS 2027 a été rejeté par l'Assemblée le 23/10/2026 (T.A. n° 358) et le Sénat examine le texte initial à partir du 09/11 : tout ce qui en vient reste un projet.

## 4. Horizons hétérogènes : ils ne sont pas affichés

**Constat.** La colonne `horizon` de `chiffrages_instituts.csv` donne l'horizon de chaque montant, mais le site ne l'affiche pas. Le croisement ne signalait que 5 lignes (T22, § 5.7). Pour les lignes dont le montant retenu vient de ce fichier, on relève au moins :

- `nfp_taxe_macron` « en 2025 » ;
- `ens_leasing` « par an (2025) » ;
- `ens_snu` « par an à partir de 2026 » ;
- `nfp_indexation_pensions`, montant cumulé sur 2025-2027 ;
- `nfp_indexation_salaires`, 3 ans d'indexation cumulés ;
- `rn24_part_fiscale` « 2024 » ;
- `rn24_salaires` « 2025 » ;
- `rn24_agences` « à horizon 2026 » ;
- `rn24_audiovisuel` « à horizon de 3 à 5 ans » ;
- `nfp_smic` « horizon 2025 (voire 2026) ».

**Proposition.** Afficher l'horizon du montant retenu dans la fiche de chaque ligne (« Pourquoi ce chiffre ? »), pour tous les programmes. Ne pas harmoniser les montants : ce serait refaire le chiffrage, ce qui sort de la règle (T22, § 5.7). Cela traite aussi `rn24_audiovisuel`, dont l'économie n'arrive qu'à 3 à 5 ans, faute de règle de calendrier.

## 5. Points clos sans changement de valeur

- **`l_rachats`, variante ancrée sur le réalisé de 0,5 Md€ (audit n° 9).** Ce réalisé est celui d'une taxe différente (8 % du nominal, temporaire). La fourchette de la règle propre (0,05 à 4 Md€) le couvre déjà, et il est cité dans `note_confiance`. Proposition : écarter, avec ce motif.
- **`a_sur_da_niches` sans intervalle (audit n° 8).** C'est un calcul de barème (rapport des accises existantes aux hausses, pondéré par le coût des niches), et non une estimation. Un intervalle n'aurait pas de base. Proposition : écarter, avec ce motif.
- **`ens_agents_publics`, fragilité.** Elle est déjà dite dans le libellé de la ligne (« hypothèse Montaigne : point d'indice +2 points, 2 Md€ par point »). Rien à faire.
- **`rn24_part_fiscale` (0,9).** La question porte sur le champ de la règle « Élasticité revenus », calibrée sur le top 0,1 %. Elle touche aussi `rn24_ir_jeunes`. Elle relève donc du groupe 2 (champ des règles, T18 point 17), et pas d'un réglage propre à cette ligne.

## 6. Résultats de l'agent A (paniers 2027, `parts/notes_A.md`)

| Ligne | Actuel | Proposé | Loi votée seule | Confiance | Effet sur le panier |
|---|---|---|---|---|---|
| `l_bandeaux` | 0,5 [0,09 ; 0,87] | 0,4 [0,26 ; 0,50] | 0,55 [0,44 ; 0,63] | low | LFI −1,1 (11,4 × 0,1) |
| `l_brunes` | 1 | 0,95 [0,91 ; 0,96] | 0,95 (tout est voté) | high | LFI −0,2 (6 × 0,7 × 0,05) |
| `e_carence` | 0,5 [0 ; 1] | 0,5 inchangé | 1 | medium | aucun ; à revoir après le 19/12/2026 |
| `e_oper` | 1 | 1 confirmé | 1 | medium | aucun |

- **`l_bandeaux`.** L'ancienne note se trompait sur deux points. La baisse de 2025 n'existe plus en 2027 (bandeaux supprimés au 1/1/2026). La réduction générale dégressive unique (RGDU, LFSS 2025 art. 18), qu'elle ne comptait pas, est le principal recoupement. Aucune ventilation officielle par niveau de salaire n'a été trouvée. Le facteur sort donc d'un modèle de l'agent (formule de la RGDU, répartition des salariés de Bozio-Wasmer). Le modèle retrouve le coût officiel de la RGDU (74 à 90 Md€ contre 74,7), le coût du gel en année pleine (4,8 à 5,8 contre 5,6) et les cas-types de l'art. 7 à 10 % près. Confiance low : le modèle doit être relu par quelqu'un d'autre que son auteur (`CONTRIBUTING.md`, règle 2). Point juridique : le décret 2026-509 réécrit l'art. D. 241-7 sans date de fin, mais son art. 2 limite le gel à 2026.
- **`l_brunes`.** Les 6 Md€ sont exactement les 59 dépenses fiscales « défavorables » du budget vert du PLF 2025 (6,05 Md€). Baisses votées d'ici 2027 : gazole non routier hors agriculture 646 → 398 M€ (vérifié dans `sources/T26/A/jaune2027_budget_vert.pdf`), Pinel et Duflot 299,6 → 239,8 M€. Facteur (6,05 − 0,25 − 0,06) / 6,05 = 0,95. Le même périmètre coûte 6,6 Md€ au PLF 2027 : un rechiffrage à la hausse de la ligne serait une question distincte.
- **`e_carence`.** L'enveloppe de 1 Md€ sur les indemnités journalières n'a toujours pas d'instrument. Une négociation des partenaires sociaux doit aboutir au plus tard le 19/12/2026, et la carence est absente du PLFSS. La lettre du ministre n'est connue que par une dépêche AFP.
- **`e_oper`.** Le PLF 2027 ne chiffre aucune économie de fusion ou de suppression d'opérateur.

## 7. Résultats de l'agent B (programmes 2024, `parts/notes_B.md`)

- **`rn24_asile`** : facteur 1 gardé, confiance medium. Le pacte européen (règlements 2024/1348 et 2024/1351) est dans le droit au 30/06/2024, mais il ne s'applique qu'à partir de juin et juillet 2026, et son mécanisme diffère de la mesure RN (demandes en ambassade). Le programme de stabilité ne parle pas de l'asile. Le passage de 1,6 à 1,2 reste inexpliqué : Montaigne n'a publié aucune méthode en 2024.
- **`ens_retention` (+1,8, règle « Effet promis », 0,333) : symétrie à examiner.** La fiche Montaigne fonde l'économie sur le pacte (« Grâce à la réforme européenne du droit d'asile… »). Si le pacte fait partie du droit de juin 2024, ce qu'il rapporte est déjà dans la référence. La ligne ne compterait alors que pour la part qui s'y ajoute, peut-être nulle. Le même critère vaut pour `rn24_asile` : il est gardé à 1 parce que son mécanisme est différent.
- **`ens_leasing`** : une mesure financée par CEE n'est pas une dépense publique. L'Insee ne classe pas les CEE en prélèvements ni en dépenses publiques (Cour des comptes, sept. 2024, p. 27), et Insee Première n° 2106 le confirme pour le compte 2025. Facteur inchangé.
- **`nfp_niches` et exemptions d'assiette** : pas de double compte (niches fiscales d'un côté, cotisations de l'autre). Une non-additivité non chiffrée subsiste avec `nfp_smic`.
- **`nfp_cotis_vieillesse` (6,3) : même base que `nfp_cotis_dividendes` (6,3).** Le seul calcul de Montaigne (PDF p. 15) porte sur les dividendes (1,7 + 4,57). Options :
  - (a) garder les deux lignes ;
  - (b) ne pas découper : le reste des recettes passe à +5,8, sans effet sur le total NFP (les deux lignes ont la règle « Aucune », facteur 1) ; le double compte possible serait seulement caché dans le reste ;
  - (c) prendre le 3,8 de l'iFRAP, NFP −2,5, sans méthode publiée non plus.

## 8. Reste ouvert après ce rapport

- `eps_capital` : il faut l'intervalle de confiance de Lefebvre, Lehmann et Sicsic (2024), à lire dans le document de travail.
- `rn24_heritage` : méthode de Montaigne non trouvée (1 Md€, « sans méthode ») ; la fragilité est à dire dans la justification, comme pour `ens_agents_publics`.
- Médecins en formation (0,1, dans `ens_autres_dep_reste`) : part déjà dans la référence non vérifiée (T25, `parts/notes_B.md`). Effet de 0,1 au plus.
- `e_carence` : à revoir après la négociation du 19/12/2026.
- `ens_retention` : décision de symétrie (§ 7).

## 9. Décisions appliquées (01/11/2026)

L'utilisateur a validé les recommandations et laissé à l'intégrateur le choix des n° 7 et 8. Corrections : `corrections.csv` (32 lignes, `scripts/appliquer_corrections.py`), plus la nouvelle colonne `facteur_reference_loi_votee` (6 lignes d'historique écrites à la main).

| N° | Décision | Effet sur le solde corrigé |
|---|---|---|
| 1 | `rn24_ptz` sort de l'assiette de `rn24_taux` (−1,2 → −1,0) ; règle générale écrite dans la base de la règle « Taux d'intérêt » | RN 2024 −53,06 → −52,86 |
| 2 | Décote du backtest non appliquée à la famille `retraites_age` ; motif écrit dans la base de « Substitution retraites » et dans `nfp_retraites` | aucun |
| 3 | Colonne `facteur_reference_loi_votee` (`paniers.csv`) : `l_bandeaux` 0,55, `e_carence` 1, `e_appr` 0,83, `l_succ` 0,91, `l_brunes` 0,95 ; lue par `moteur.py` ; `garde_fous.py` l'exige pour une ligne « partielle » décotée dont la source cite un PLF ou PLFSS 2027 | variante « loi votée seule » seulement |
| 4 | Horizon du montant affiché dans « Pourquoi ce chiffre ? » des programmes 2024, quand le chiffreur nomme une année ou un horizon (`web/site.js`, `horizonChiffrage`) | aucun |
| 5 | `l_bandeaux` 0,5 → 0,4 [0,26 ; 0,50], confiance low ; modèle à relire (dit dans la note) | panier LFI −1,1 |
| 6 | `l_brunes` `absente` → `partielle`, 0,95 [0,91 ; 0,96], confiance high ; registre 2027 aligné | panier LFI −0,2 |
| 7 | `ens_retention` : facteur de référence 1 gardé. Le programme invoque le pacte, mais Montaigne chiffre un autre mécanisme (demandeurs pris en charge dans des pays tiers, modèle australien), absent du droit de juin 2024 : même critère que `rn24_asile`. Motif écrit dans la justification | aucun |
| 8 | `nfp_cotis_vieillesse` : option (a), montant Montaigne gardé ; fragilité dite dans la justification, confiance high → medium. (c) aurait remplacé le chiffreur de départ pour une seule ligne, sans méthode publiée non plus ; l'iFRAP (3,8) reste dans les autres chiffrages | aucun |

`e_carence` : note mise à jour (instrument toujours absent ; à revoir après le 19/12/2026). `check_regression.py` : RN indépendant −63,4, corrigé −52,86 ; financement du panier LFI 37,6. `TEST_WEB_STRICT=1 bash scripts/run_all.sh` passe ; fiches vérifiées à l'écran (1400 × 1000 et 390 × 844) : `rn24_audiovisuel`, `rn24_taux`, `l_bandeaux`, `l_brunes`, `ens_retention`.

Reste ouvert : § 8, et la relecture du modèle de l'agent A pour `l_bandeaux`.

## 10. Clôture du groupe 1 (01/11/2026, suite)

| Point | Décision | Effet sur le solde corrigé |
|---|---|---|
| `l_bandeaux`, relecture indépendante (`relecture/notes.md`) | 0,4 → **0,55** [0,45 ; 0,65] ; loi votée seule 0,55 → 0,65 ; variante « dégel » 0,715 → 0,63 [0,50 ; 0,75]. Le premier modèle faisait la moyenne avec une transposition (RGDU entière jusqu'à 1,88 SMIC) qui décrit une autre mesure que le barème chiffré, et retirait tout l'effet de l'art. 7 au-dessus de 1,6 SMIC. Les deux modèles s'accordent sur la formule et les données. Confiance low (modèle) | financement LFI 37,6 → 39,3 |
| `eps_capital` (`parts/notes_C.md`) | bornes 0,5 et 1,17 (dispersion entre spécifications du papier) ; centre 0,77 inchangé. Paramètre de la règle « Élasticité capital » : `nfp_flat` et `l_pfu_i` (la note de l'agent ne citait que la première) | fourchettes seulement |
| Médecins en formation (`ens_autres_dep_reste`) | 29 % du poste déjà prévu par les objectifs 2021-2025 : facteur 0,863 → 0,853 | Ensemble 2024 −20,15 → −20,12 |
| `rn24_heritage` | aucune méthode publiée : fragilité dite dans la justification, confiance medium | aucun |

Corrections : `corrections_C.csv`, `corrections_relecture.csv`, et 3 lignes d'historique écrites à la main pour `variantes_sensibilite.csv`. Reste du groupe 1 : `e_carence` après le 19/12/2026. Suite du travail : `recherche/T27/suivi.md` (groupes 2 à 6).
