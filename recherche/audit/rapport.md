# Audit indépendant du backtest des chiffrages (état au 14 octobre 2026)

Auditeur : agent indépendant. Je n'ai produit aucun des chiffrages audités. L'audit s'est fait en lecture seule : aucun fichier de `data/`, `scripts/`, `web/` ni `HANDOFF.md` n'a été modifié, et `run_all.sh` n'a pas été lancé, parce qu'il réécrit `data/*.csv`. Je n'ai fait aucune recherche web : les preuves viennent des archives de `sources/`, lues avec `pdftotext` ou après suppression des balises HTML, et des rapports `recherche/*/rapport.md`.

Scripts d'analyse produits dans ce dossier :
- `couche1_sensibilite.py` : sensibilité de l'erreur médiane de la couche 1 aux exclusions et aux bases de prix. À lancer depuis la racine du projet.
- `projection_variantes.py` : variantes de la projection T5. À lancer depuis `data/`. Il reproduit exactement les chiffres publiés (LFI ajusté 2032 : 5,70 % et 132,7 %), ce qui valide la réimplémentation.

Gravité :
- **bloquant** : le résultat publié est faux ou trompeur dans sa comparaison entre partis ;
- **important** : biais de plus de 1 Md€, ou défaut de méthode qui touche une règle ;
- **mineur** : incohérence documentaire, ou effet inférieur à 0,5 Md€.

« Favorise X » signifie que la correction proposée dégraderait le solde de X ou améliorerait celui de l'autre camp.

---

## 1. Symétrie des paniers et référence 2027

### 1.1 Convention « loi votée + PLF/PLFSS 2027 déposés » : cohérente, mais il manque une variante

**Constat.** La mise à 0 de `e_pens` et `e_abat` et la décote de `l_surtaxe` (0,286) découlent de la même logique : on ne compte que l'écart par rapport à la référence. `e_pens` (4,0 contre 4,0 au PLFSS, art. 35, vérifié dans `sources/T1/PLFSS2027_projet_AN3211.html`) et `e_abat` (1,4) sont identiques aux mesures proposées, d'où le facteur 0. La surtaxe pérenne n'ajoute que 7,0 − 5,0 = 2,0, d'où (7 − 5) / 7 = 0,286. Les deux camps sont traités de la même façon.

**Ordre de grandeur, calculé par l'audit.** Avec une référence « loi votée seule » :
- Ensemble récupère +5,4 (4,0 + 1,4) ;
- LFI récupère environ +7,7 :
  - surtaxe : 7,0 × 0,93 = 6,5 au lieu de 1,86 ;
  - bandeaux : seuls 1,6 + 2,8 = 4,4 sont votés, donc un facteur dans [0,64 ; 0,87], soit un milieu de 0,75 et 9,1 au lieu de 6,05.

La convention pèse donc sur les deux camps, à peu près en proportion de leurs financements. Ce n'est pas une asymétrie.

**Gravité : mineur** (méthode). `e_abat` a été supprimé en commission le 9/10 et le PLF est rejeté en commission.

**Correction.** Publier les deux variantes de référence côte à côte, comme T1 le recommande (§7.1). Aujourd'hui seule la variante « PLF déposé » est calculée.

### 1.2 SMIC : le gel du SMIC de référence des allègements est compté contre LFI dans `l_bandeaux`, mais ignoré dans `l_smic`

**Gravité : bloquant** pour le panier LFI (les deux variantes). **Favorise Ensemble.**

**Fichiers et lignes.** `data/raw/paniers.csv` (`l_smic` et `l_bandeaux`), `data/raw/parametres_bareme.csv` (`smic1600_decomposition_*`).

**Preuve.**
- Le facteur de référence de `l_bandeaux` (0,5) repose sur une baisse de 11,0 Md€ des allègements dans la référence, dont 2,8 (gel 2026, voté) et 2,9 (gel 2027, proposé). Le gel est donc réputé être dans la référence.
- Le coût de `l_smic` (−19, Montaigne) se décompose ainsi (`parametres_bareme.csv`) : **−21,5 d'allègements généraux**, −3,7 de masse salariale publique, +6 de prélèvements. Le coefficient de Montaigne est « estimé sur 2021-2023 », donc avec un SMIC de référence indexé.
- Avec le SMIC de référence figé à sa valeur du 1/1/2026 (décret 2026-509, prolongé par le PLFSS 2027), une hausse du SMIC n'augmente plus les allègements. Elle les réduit, car le rapport entre le SMIC de référence et la rémunération baisse. Le poste de −21,5 disparaît donc presque entièrement dans la référence 2027.
- La ligne garde pourtant un facteur de référence de 1. T1 l'avait signalé (§7.3, « probablement surestimé »), et la note de la ligne aussi.
- Second effet, dans le même sens : le statique est en base 2024 (+14,4 % pour atteindre 1 600 € net). Le SMIC net est de 1 477,93 € depuis le 1/6/2026, soit +8,3 % seulement pour atteindre 1 600 € en nominal. T4p précise que Montaigne chiffre une hausse « en euros constants, en plus de l'indexation » : tout dépend de ce que promettra le programme 2027.

**Correction.** Choisir une hypothèse et l'appliquer aux deux lignes à la fois :
- **soit** le gel est dans la référence : `l_smic` est rechiffré sans le poste allègements (statique compris entre ≈0 et −5 selon l'effet de la baisse du coefficient). L'effet emploi devient alors nettement plus fort, puisque le coût du travail au SMIC monte davantage ;
- **soit** la hausse du SMIC suppose de dégeler le SMIC de référence : le coût du dégel (5,7 Md€) s'ajoute à `l_smic`, et `l_bandeaux` ne peut plus invoquer le gel (facteur dans [(12,1 − 5,3) / 12,1 ; 0,87], soit environ 0,7).

Dans les deux cas, l'écart avec la situation actuelle dépasse 5 Md€ sur le solde LFI.

### 1.3 Zucman, ISF, IR et PFU : interaction non traitée dans le financement LFI

**Gravité : important.** **Favorise LFI** (double compte).

**Fichiers et lignes.** `paniers.csv` : `l_zucman`, `l_isf`, `l_ir`, `l_pfu`.

**Preuve.** La proposition de loi n° 768 (`sources/T4p/B_an_ppl768_impot_plancher.pdf`) définit l'impôt plancher comme 2 % du patrimoine, **diminué** de « l'impôt sur le revenu, de l'IFI, de la CSG, de la CRDS et de la CEHR » acquittés : « ce qui neutralise tout risque de double taxation ». Rétablir l'ISF (qui remplace l'IFI), relever l'IR (14 tranches) et imposer les dividendes au barème (fin du PFU) augmentent tous les impôts imputables des ménages à plus de 100 M€. Le rendement de la taxe Zucman baisse d'autant. Le panier additionne pourtant 5,5 (Zucman) + 4,5 (ISF) + 4,7 (IR) + 3,4 (PFU) sans interaction. La seule décote appliquée concerne la taxe holdings (0,1 retiré deux fois, une fois dans `l_isf` et une fois dans `l_zucman`).

**Correction.** Ajouter une décote d'interaction sur `l_zucman` : retirer l'ISF, l'IR et le PFU supplémentaires payés par les patrimoines de plus de 100 M€. France Stratégie 2023 donne l'ISF par tranche de patrimoine (tableau p. 70). À défaut, retenir un intervalle large, avec un facteur de référence de Zucman dans [0,3 ; 1], et le propager.

### 1.4 `l_ret62` : la correction −6,9 → −7,3 lit un incrément annuel comme un niveau

**Gravité : important.** **Défavorise LFI** de 0,4 à 0,9 Md€ (avant le facteur 0,8).

**Fichiers.** `paniers.csv` (`l_ret62`, `l_ret60`), `historique.csv` ligne 7.

**Preuve.**
- PLFSS 2027 (`sources/T1/PLFSS2027_projet_AN3211.html`) : « La réforme de 2023 et sa suspension conduiront au total à une amélioration du solde des [ROBSS] de **0,8 milliard d'euros en 2027**, la suspension réduisant de 1,0 milliard le rendement initialement attendu de 1,8 milliard ». Le même texte poursuit : « un rendement […] net de l'effet de la suspension […] de 1,9 milliard d'euros en 2028 (après 0,8 milliard en 2027) » et « +2,8 milliards d'euros en 2029 puis 3,7 milliards d'euros en 2030 ».
- Ces montants sont des **gains d'une année sur l'autre**. Le rendement de la réforme en niveau dépasse largement 1,8 Md€ en 2027 : 6,2 à 7,7 selon le rapport annexé au PLFRSS 2023 (`sources/T2a/rapport_objectifs_effets_reforme_2023.pdf`, tableau 29). Le rapport T4p (« Vigilance ») le dit explicitement : « semblent être des gains supplémentaires d'une année sur l'autre […] pas des niveaux ».
- T4p donne le coût total de la suspension en 2027 : 1,4 (lettre rectificative) + 0,5 (amendement 2686) = **1,9 Md€**.
- Le statique cohérent est donc 8,3 − 1,9 = **−6,4**, et non −7,3. Il faut aussi corriger le facteur de référence de `l_ret60` : (58 − 1,9) / 58 = 0,967, au lieu de 0,98.

**Autre réserve.** Le chiffre de 8,3 attribué à l'iFRAP n'est pas archivé dans `sources/` et ne correspond à aucun chiffre gouvernemental :
- 7,7 avec les recettes nouvelles, 6,2 net des mesures d'accompagnement (rapport annexé 2023) ;
- or les recettes nouvelles ne disparaissent pas avec une abrogation de l'âge.

Par ailleurs, la couche 1 montre que la réforme 2023 rapporte 74 à 82 % de son chiffrage ex ante, et cette décote est appliquée aux économies d'Ensemble (`facteur_reforme`). Chiffrer le coût de l'abrogation sur le rendement ex ante, sans cette même décote, n'est pas symétrique.

**Correction.**
- Ramener le statique à −6,4. La valeur −6,9 est acceptable si l'on ne retient que la lettre rectificative.
- Documenter la source du 8,3, ou le remplacer par 6,2 (ou 7,7) × le ratio de la couche 1, moins la suspension. Cela donne une fourchette de −3 à −5.

### 1.5 Décotes de référence : des méthodes différentes selon les lignes

**Gravité : mineur à important** (au cas par cas). **Sens mixte.**

| Ligne | Recoupement identifié | Traitement | Sens |
|---|---|---|---|
| `l_succ`, `l_ir` (LFI, recettes) | partiel, non chiffré | milieu d'intervalle (0,91 ; 0,94) | défavorise LFI |
| `e_carence` (Ens., recette) | enveloppe IJ sans instrument | milieu (0,5) | défavorise Ensemble |
| `e_appr` (Ens., recette) | borne calculée 0,84 | 0,5 maintenu « en attendant » | défavorise Ensemble (≈1,0 Md€) |
| `e_oper` (Ens., recette) | économies sur les opérateurs, France compétences | 1 (« non chiffrable ») | favorise Ensemble |
| `e_succ` (Ens., coût) | art. 4 du PLF (dons d'argent, temporaire) | 1 | défavorise Ensemble |
| `l_brunes` (LFI, recette) | trajectoire GNR BTP votée (niche de 0,713 à 0,466 Md€, `parametres_bareme.csv`) | 1 | favorise LFI (≈0,25) |
| `l_rachats` (LFI, recette) | taxe existante de 0,2 (montant_reference = 0,2, déjà dans la note) | 1, statut « absente » | favorise LFI (0,2) ; incohérent avec `l_isf` et `l_zucman`, où 0,1 est retiré |

**Correction.** Adopter une seule règle :
- recoupement chiffré : (statique − recoupement) / statique ;
- recoupement identifié mais non chiffré : milieu de [borne basse ; 1], avec l'intervalle propagé dans le Monte-Carlo (voir 3.5) ;
- `e_appr` : passer à 0,84, ou au milieu de [borne basse documentée ; 0,84] ;
- `l_rachats` : passer en « partielle » avec 0,976 ;
- `l_brunes` : passer à environ 0,96.

### 1.6 Règles comportementales appliquées d'un côté seulement

**Gravité : mineur.**

- **Effet emploi des bandeaux.** Bozio-Wasmer donnent eux-mêmes 11,4 Md€ après effets emploi (−61 870 ETP), contre 12,1 ex ante (T2a). Le panier garde 12,1 avec la règle « Aucune », alors que l'effet emploi d'une hausse du coût du travail est compté contre LFI pour le SMIC. Retenir 11,4 (facteur 0,94). **Favorise LFI** de 0,35 après la décote de référence.
- **Accise sur l'électricité (`e_elec`).** La formule `accise` (élasticité-prix) s'applique aux hausses d'accise de LFI (`l_brunes`, 0,73) mais pas à la baisse d'accise d'Ensemble (« Aucune »). Appliquée de façon symétrique avec une élasticité de −0,2, elle réduirait un peu le coût d'Ensemble (environ 0,1 à 0,3). **Défavorise Ensemble.**
- **PPV à 10 000 € (`e_prime`).** Le projet documente lui-même un effet d'aubaine de la PPV d'environ 30 % (`mesures_effets.csv`, `ppv_2022_aubaine`). Il faut vérifier si le chiffre de Montaigne (−2) l'intègre. Sinon, la règle « Aucune » **favorise Ensemble**.
- **Taux de recours sur `l_autonomie`.** La règle 0,65 n'est juste que si le chiffre de Montaigne (12,3) suppose un recours complet. La synthèse archivée (`sources/T6/montaigne_nfp_synthese_wb20240708.html`) ne le précise pas. À vérifier : si Montaigne intègre déjà le non-recours, la décote est comptée deux fois et **favorise LFI** (4,3 Md€).

### 1.7 Annulation des mesures d'économie de la référence (à traiter en T3)

**Gravité : important pour T3** ; sans effet sur les paniers actuels.

La référence inclut désormais :
- la sous-indexation des pensions (4,0) ;
- les gels de la prime d'activité et des APL (0,43) ;
- le gel du point d'indice ;
- 1 Md€ d'économies sur les IJ ;
- l'élargissement de l'assiette des allègements (3,7).

Tout programme qui promet des indexations complètes doit compter l'annulation de ces mesures comme un coût. T1 le signale (§7.4) pour `nfp_autres_dep`. Les paniers n'en tiennent pas compte. Ce n'est pas une erreur tant qu'ils restent des « mesures phares », mais le gabarit 2027 doit prévoir une ligne « annulation de mesures de la référence ».

### 1.8 Incohérences de données sur les lignes modifiées

**Gravité : mineur.**

- `l_isf`, `note_reference` : la note dit « Facteur = (2,8 − 0,1) / 2,8 = 0,96 », alors que le statique vaut 4,5. Le facteur correct est (4,5 − 0,1) / 4,5 = **0,978**. Écart : +0,08 Md€.
- `l_isf`, même note : « Le gain est déjà net de l'IFI (3,08 Md€ en 2027) » est inexact. Le 4,5 est net de l'IFI **2022** (1,83 Md€) ; voir 2.1.
- `statut_reference_2027.csv` : `l_surtaxe_i` et `l_surtaxe_a` restent à `facteur_suggere` 0,17 et `montant` 5,0, alors que `paniers.csv` est passé à 0,286. Les deux fichiers de `data/raw/` se contredisent.
- `l_ret62`, `note_reference` : la note dit encore « décision laissée à l'intégrateur (−6,9 ou −7,3) ».
- `garde_fous.py` ne détecte pas une ligne « absente » dont `montant_reference_2027` n'est pas nul (cas de `l_rachats`). Il ne vérifie pas non plus qu'une même nature de mesure (une accise, par exemple) reçoit la même règle d'un parti à l'autre. Il ne contrôle que l'égalité des facteurs pour une règle donnée.

---

## 2. Valeurs modifiées aujourd'hui (`historique.csv`)

### 2.1 `l_isf` : 2,8 → 4,5 (lignes 101 à 104)

**Citation : vérifiée.** `sources/T4p/B_fs2023_rapport_final_fiscalite_capital.pdf`, avis du comité p. 12-13 et p. 213-214 : « les recettes d'ISF en 2022 auraient été égales à 6,3 milliards d'euros, et la perte de recettes liées à sa transformation en IFI se serait donc élevée à 4,5 milliards d'euros ».

**Périmètre et horizon : non comparables.**
- Le 4,5 est l'écart de **2022**, avec un IFI de 1,83 Md€ (graphique 68, même page). France Stratégie suppose un IFI égal à 29 % d'un ISF contrefactuel.
- L'état A du PLF 2027 inscrit **3,08 Md€** d'IFI (ligne 1406, `sources/T1/PLF2027_projet_AN3210.html`). L'IFI a donc été multiplié par 1,7 depuis 2022, peut-être sous l'effet de la LFI 2026.
- Avec le ratio de France Stratégie, l'écart 2027 serait de 3,08 × (1/0,29 − 1) ≈ 7,5. Si une partie de la hausse de l'IFI vient d'un élargissement de l'assiette, qui recouperait l'ISF, l'écart serait plus proche de 4,5 à 5,5.
- Le contrefactuel est par construction statique (rapport IFI/ISF constant). La décote « Élasticité patrimoine » (0,87) reste donc justifiée.

**Gravité : mineur** sur la valeur : 4,5 est plutôt prudent pour LFI, et l'ancienne valeur de 2,8 était l'écart 2017 tiré de la presse. **Important** sur l'interaction avec Zucman (1.3).

**Correction.**
- Préciser dans la note qu'il s'agit d'un écart 2022.
- Soit actualiser (fourchette de 4,5 à 7,5 dans le Monte-Carlo), soit garder 4,5 comme borne basse.
- Corriger le facteur de référence à 0,978.

### 2.2 `l_surtaxe` : 6 → 7, facteur de référence 0,17 → 0,286 (lignes 105 à 110)

**Citation : vérifiée.** Exposé général du PLF 2027 : « La prorogation de la contribution exceptionnelle sur les bénéfices des grandes entreprises représenterait par ailleurs un rendement de 5,0 Md€, en diminution de 2,0 Md€ par rapport à 2026 ». Le rendement 2026 de 7,0 en est déduit correctement. Le calcul (7 − 5) / 7 = 0,286 est juste.

**Réserves.**
1. Le 7,0 est un **rendement de caisse 2026** : acompte de l'exercice 2026 et solde de l'exercice 2025, avec une assiette égale à la moyenne de l'IS sur deux ans. Ce n'est pas exactement le rendement en régime permanent d'une surtaxe pérenne. Écart non chiffrable, mineur.
2. Le 7,0 est quasi observé : il intègre déjà le comportement de 2025-2026. Lui appliquer en plus la règle « Élasticité IS » revient à compter une partie du comportement deux fois. L'erreur de formule décrite en 3.2 va en sens inverse et l'emporte.

**Gravité : mineur.**

### 2.3 `nfp_niches` : 14 → 16,5 (ligne 5)

**Preuve.** La médiane retient l'iFRAP à 10 = 5 + 5. Le rapport T6 (§49) dit pourtant : « Double compte probable dans le total iFRAP. […] La note dit pourtant "tout au plus […] 5 milliards" ». T2a précise que l'astérisque de la seconde ligne signale des « mesures du chiffrage NFP du 21/06 », c'est-à-dire un montant repris du parti et non un chiffrage indépendant. L'autre estimation (La Grande Conversation, 23) inclut 15 Md€ d'exonérations de cotisations au-dessus de 1,6 SMIC : c'est un autre périmètre.

**Gravité : important.** **Favorise LFI** (+2,5 sur l'application 2024).

**Correction.** Revenir à l'iFRAP à 5 (médiane de 5 et 23 = 14), ou mieux, ramener La Grande Conversation à un périmètre comparable (23 − 15 = 8), ce qui donne une médiane de 5 et 8 = 6,5. Dans tous les cas, ne pas utiliser une ligne marquée d'un astérisque comme chiffrage indépendant.

### 2.4 `l_ret62` : −6,9 → −7,3 (ligne 7)

Voir 1.4. **Erronée** : le 1,0 est un incrément annuel. **Important.**

### 2.5 Couche 1 : CICE 20 → 18,5 (ligne 72)

**Citation : vérifiée.** `sources/T2a/fs_cice_synthese_2020.pdf`, tableau 1 : créances de 18 183 (2014), 18 332 (2015), 18 510 (2016) et 22 152 M€ (2017). Le texte parle d'un coût « de l'ordre de 18 milliards d'euros en 2016 ».

**Périmètre : comparable.** Le chiffre de 20 était annoncé en 2012 « au taux plein » de 6 % ; 2016 est encore à 6 %. L'écart de prix entre 2012 et 2016 (masse salariale plus élevée en 2016) rend l'écart réel un peu plus grand (environ −10 %). Correct.

### 2.6 Couche 1 : prime d'activité 2016, 4,4 → 4,1 (ligne 79)

**Citation : vérifiée.**
- `sources/T2a/senat_r25-728_prime_activite.pdf` : « En 2024, les dépenses exécutées de prime d'activité atteignaient 10,6 Md€, contre 4,1 Md€ en 2016 ».
- Ex ante : `senat_cra_20151130.html` : « les prévisions de dépenses - 3,95 milliards d'euros ».

**Périmètre : comparable** (dépense de la même année).

**Résiduel (mineur).** `ex_post_haut` = 4,73 reste une valeur que T2a dit absente de toute source lue. La supprimer, ou la remplacer par 4,1.

### 2.7 Couche 1 : retraites 2023, ex ante 13,7 → 13,5 (lignes 83 à 86)

**Citations : vérifiées.**
- Rapport annexé de janvier 2023 : « améliorer le solde du système de retraite de 6,2 Md€ en 2027 et 11,8 Md€ en 2030 » ; déficit évité de 13,5 en 2030.
- Cour des comptes 2025 (`ccomptes_retraites_2025.pdf`, p. 65-67) : 10 Md€ en 2030 ; 9,7 (DG Trésor) et 11,8 (Rexecode).

**Non comparables.**
- **Base de prix.** Note 117 de la Cour : les résultats DG Trésor et Rexecode « étaient exprimés en euros courants 2030. Ils ont été retraités par la Cour […] en euros constants (valeur 2024) ». L'ex ante (13,5) est en euros courants 2030. À prix 2024, l'ex ante vaut environ 12,2 et l'écart passe de **−26 % à environ −18 %** (`couche1_sensibilite.py`).
- **Périmètre.** 13,5 = 11,8 (mesures nettes) + 1,7 (recettes nouvelles). L'« évolution du solde du système de retraites » de la Cour ne permet pas de savoir si les recettes nouvelles sont incluses.
- **Nature.** C'est une **réestimation**, pas un réalisé (la note de la ligne le dit).
- **Borne basse.** `ex_post_bas` = 7,1 porte sur une autre chose : régime général, 2032, ou l'effet d'une baisse en 2035 selon le passage. T2a le signale, mais la valeur est restée.

**Gravité : important**, parce que cette ligne fixe la borne basse de `facteur_reforme` (0,73), qui s'applique aux économies d'Ensemble (`e_feries`, `e_oper`, `e_fp`) et à `l_zucman`.

**Correction.**
- Comparer les deux chiffres à prix constants : 11,8 courants 2030 ramenés en 2024, soit environ 10,6, contre 9,7 à 11,8.
- Remplacer `ex_post_bas` par 9,7.
- Marquer la ligne « réestimation ».

### 2.8 Couche 1 : Woerth 2010, 18,4 → 18,8 (ligne 82)

Le correctif note lui-même que l'ex ante est en euros de 2008 et l'ex post en euros de 2016 (environ +8 %). À prix constants, l'écart est d'environ **−14 %** et non −7 %.

**Gravité : mineur.** Ces deux corrections de base de prix (2.7 et 2.8) se compensent presque dans la moyenne de `facteur_reforme` : 0,822 et 0,862 à prix constants, contre 0,741 et 0,931 aux prix actuels.

### 2.9 Paramètres non mis à jour après les corrections du jour

**Gravité : mineur.**

- `moteur_parametres.csv`, `facteur_reforme` : il vaut 0,73 / 0,82 / 0,911, calculé sur les anciennes valeurs (10 / 13,7 et 18,4 / 20,2). Avec les valeurs actuelles : 0,741 / 0,836 / 0,931 ; à prix constants : 0,822 / 0,842 / 0,862.
- `moteur_parametres.csv`, `erreur_ligne` : la borne basse vaut encore 0,114 (couche 1 à 11 mesures), contre une médiane de 10,0 % sur 25 mesures.
- `regles.csv`, « Réforme structurelle » : la base est encore décrite comme « retraites 2010 −9 % ; 2023 −27 % ».

---

## 3. Moteur (`scripts/moteur.py`)

### 3.1 Formules vérifiées

- **`f_taxe_elasticite`.** Avec une assiette proportionnelle à (1 − t)^ε, la recette réelle rapportée à la recette statique vaut (t1·b − t0) / (t1 − t0). **Formule correcte** : elle inclut la perte sur l'impôt existant. Pour `l_pfu` : ε = 0,77, t0 = 0,354, t1 = 0,4627, soit b = 0,868 et un facteur de **0,437**, retrouvé par l'audit.
- **`t0_capital` et `t1_capital`.** Vérifiés dans `parametres_bareme.csv` :
  - t0 = 31,4 + CEHR 4 = 35,4 ;
  - t1 = 18,6 + 45 × (1 − 0,4 − 0,068) + 4 × (1 − 0,068) = 46,27.
  - Le RFR réintègre l'abattement de 40 %, ce qui est cohérent.
- **`f_accise`.** Le facteur vaut (1 + q) + a·q avec q = ε·dp. **Formule correcte**, perte sur l'accise existante comprise. Résultat : 0,8815 − 1,274 × 0,1185 = **0,7305**.
- **`a_sur_da_niches`.** Moyenne pondérée de (3,86 / 56,89 ; 36,79 / 23,96 ; 45,19 / 15,56) par (1,693 ; 0,466 ; 1,178) = **1,276**. Correct.
- **`dp_niches`.** (78,6 × 1,693 + 22,7 × 0,466 + 12 × 1,178) / 3,337 = **47,3 %**. Correct pour la borne haute.
- **`perte_patrimoine`.** La borne basse vaut 0,15 × 0,41 = 0,0615 : correct.
- **`f_smic`.** Unités cohérentes (emplois × €/emploi / 1e9 / Md€). Numériquement, 0,17 × 0,1439 × 2,2 M = **53 800 emplois**, et non « ≈46 000 » comme l'écrit la justification de `moteur_regles.csv`. Coût : 0,87 Md€, soit un facteur de 1,046. **Mineur** (texte).
- **Erreur de ligne.** La médiane de |N(0, σ)| vaut 0,6745σ : la conversion est correcte.

### 3.2 `f_semi_elasticite` (règle « Élasticité IS ») oublie la perte d'assiette sur l'IS existant

**Gravité : important** (erreur de formule). **Favorise LFI** d'environ 0,4 Md€ sur `l_surtaxe`. La même erreur est inscrite dans le forfait de 0,93.

**Preuve.** La formule est 1 − s·Δ·h : elle ne compte que la perte de recette **de la surtaxe**. Or, avec une semi-élasticité de l'assiette (s = 0,8 % par point, `is_shifting`), l'assiette qui baisse fait aussi perdre l'IS de base et la CSS (t0 = 25,83 points). Le calcul complet est le suivant :
- recette = (t0 + Δ) · B0 · (1 − sΔ) ;
- gain réel / gain statique = **1 − s · (t0 + Δ)** ;
- avec t0 + Δ ≈ 33,6 (milieu des taux 2026), on obtient 1 − 0,008 × 33,6 = **0,73**, contre 0,93.

C'est le même raisonnement que le terme `a` de `f_accise`, qui, lui, est bien compté. Le résultat ne dépend pas du point de départ (référence avec la surtaxe réduite à 15,7 / 31,4 %, ou sans surtaxe).

**Erreur secondaire.** `delta_is` = 8,56 mesure l'écart avec un IS à 25 % au lieu de 25,83 % (la CSS de 3,3 % est déjà dans la situation de base) :
- les bons écarts sont 25 × 0,206 = 5,15 et 25 × 0,412 = 10,3, soit un milieu de 7,73 au lieu de 8,56 ;
- les bornes 5,98 et 11,13 sont décalées de la même façon.

Cette erreur secondaire devient sans objet si la formule est corrigée.

**Correction.**
- Remplacer la formule par 1 − s·(t0 + Δ)·h, avec t0 = 25,83 et Δ = 7,73.
- Mettre à jour le forfait de « Élasticité IS » (environ 0,73).
- Donner une fourchette à `s_is` : aucune incertitude n'est propagée aujourd'hui.

### 3.3 `l_rachats` : règle « Élasticité capital » appliquée à un impôt qui n'a rien à voir

**Gravité : important.** Sens incertain ; 3,7 Md€ reposent sur un calcul d'auteur unique.

**Preuve.**
- Le facteur de 0,437 est calculé avec t0 et t1 = **taux marginaux des dividendes au PFU et au barème** (35,4 % et 46,3 %). La taxe visée est un prélèvement de 33 % sur la valeur d'acquisition des rachats d'actions, payé par la société, contre 8 % sur le nominal aujourd'hui.
- L'amendement I-105 (`sources/T2a/amendement_I-105_plf2026_rachats.pdf`), déposé par le groupe RN et non retenu dans la LFI 2026, calcule « 8,415 milliards d'euros la première année » sur 33 % × 25,5 Md€. Ce montant brut inclut la recette déjà existante (0,2). L'auteur annonce lui-même vouloir « dissuader ces opérations […] les années suivantes » : l'année 2027 n'est pas la première année.
- La substitution entre rachats et dividendes est quasi parfaite, et les dividendes ne sont pas soumis à cette taxe. L'élasticité de l'assiette n'a donc aucun rapport avec ε = 0,77 appliqué au taux net de l'actionnaire.

**Correction.**
- Créer une règle propre, ou au minimum appliquer la formule avec t0 = 0,08 et t1 = 0,33.
- Retirer la recette existante (facteur de référence 0,976).
- Élargir fortement l'intervalle : la fourchette actuelle de 2,7 à 4,9 est beaucoup trop étroite pour une « estimation unique » en confiance faible.
- Ancrer une variante sur le réalisé : 0,5 Md€ à 8 % sur le nominal.

### 3.4 SMIC : effectif concerné et effet emploi

**Gravité : important**, écart documenté mais non tranché. **Favorise LFI** d'environ 3,8 Md€ si l'on retient Montaigne.

- `n_smic` = 2,2 M compte les salariés **exactement** au SMIC. Une hausse de 8 à 14 % touche tous les salariés entre 1 et 1,14 SMIC, soit nettement plus de monde.
- Le moteur obtient 54 000 emplois perdus ; Montaigne en estime 230 000 à 380 000. `moteur_regles.csv` reconnaît l'écart (facteur d'environ 1,25 avec le chiffre de Montaigne).
- À traiter en même temps que 1.2 : si le gel des allègements fait partie de la référence, la hausse du coût du travail au SMIC est plus forte, et l'effet emploi aussi.

**Correction.**
- Prendre comme effectif le nombre de salariés entre 1 et 1,15 SMIC (Dares).
- Propager l'intervalle de l'élasticité, dont la borne haute manque aujourd'hui.

### 3.5 Incertitude : sous-estimée

**Gravité : important** pour l'interprétation des bandes P10-P90.

1. **Le bruit de ligne est indépendant d'une ligne à l'autre.** Or l'erreur d'un chiffreur est corrélée sur toutes ses lignes. Les preuves :
   - T6 montre que « le chiffreur de départ reste le premier facteur d'incertitude » (NFP de −50 à −179) ;
   - Montaigne seul a une erreur médiane de 40 % (T10b).

   Avec 30 lignes indépendantes, la bande du total LFI intégral (−103 / −85 / −67) est mécaniquement étroite. **Correction** : ajouter un facteur commun par chiffreur (le même tirage pour toutes les lignes d'une même source), en plus du bruit propre à chaque ligne.
2. **Les facteurs de référence ne sont pas propagés.** C'est le cas de `l_bandeaux` [0,09 ; 0,87], `e_carence` [0 ; 1], `e_appr`, `l_succ` et `l_ir`. Ce sont pourtant les incertitudes les plus larges du panier (bandeaux : 1,1 à 10,5 Md€). **Correction** : tirer `facteur_reference` dans son intervalle documenté.
3. **Plusieurs paramètres n'ont pas d'intervalle** : `eps_capital` (0,77, qui pèse sur 2 × 2 lignes), `s_is`, `a_sur_da_niches`, `hausse_smic`. La règle Élasticité capital n'a donc aucune incertitude de paramètre.
4. **Le bruit est tiré séparément dans chaque variante.** Une même mesure (`l_smic_i` et `l_smic_a`) reçoit deux tirages différents selon la variante. C'est sans effet sur les totaux de chaque variante, mais la différence entre variantes n'est pas cohérente. Mineur.
5. **Le bruit est symétrique et centré**, alors que T10b et la couche 1 mesurent des biais signés par cause : recours sous-estimé, comportement surestimé. Le fait de ne pas corriger ces biais doit au moins être signalé.

---

## 4. Projection (`scripts/projection.py`)

### 4.1 L'emprunt « règle d'or » de LFI ajusté est absent de la dette

**Gravité : bloquant** pour la comparaison des trajectoires. **Favorise LFI ajusté.**

**Preuve.** `moteur.py` écarte les lignes `Investissement…` du solde (« déficit volontaire : colonne à part »), et `projection.py` lit ce solde. Les 30 Md€ par an de planification écologique « financée par emprunt » n'entrent donc ni dans la dette ni dans les intérêts. `HANDOFF.md` publie en conséquence une dette 2032 de 132,7 % pour LFI ajusté, contre 132,2 % pour Ensemble.

Avec l'emprunt (`projection_variantes.py`) : **déficit 2032 de 6,99 % et dette de 139,0 %** (intérêts supplémentaires de 35,3 Md€). La règle 3 de §9 (« colonne à part, pas une pénalité ») vaut pour le solde de crédibilité. Elle ne peut pas valoir pour une trajectoire de dette : l'emprunt est de la dette.

**Correction.**
- Dans la projection, ajouter les lignes « Investissement » au déficit et à la dette, en les affichant dans une colonne séparée.
- Ou bien publier deux trajectoires (« hors investissement » et « y compris investissement »), en signalant clairement la différence.

### 4.2 Impact constant en % du PIB : montée en charge et mesures temporaires de la référence ignorées

**Gravité : important.** Hypothèse non signalée comme limite, alors que T5 demandait « la montée en charge des mesures ». **Sens mixte.**

- **Abrogation ou retraite à 60 ans.** Le rendement de la réforme 2023 monte en charge : 6,2 en 2027, puis 11,8 en 2030 selon le rapport annexé ; +1,9 en 2028, +2,8 en 2029 et +3,7 en 2030 selon le PLFSS 2027. Maintenir le coût de 2027 (−7,3 ou −58) constant en % du PIB **sous-estime le coût LFI** de plusieurs Md€ par an à partir de 2029. Favorise LFI.
- **Surtaxe d'IS.** Dans la référence, la surtaxe est **temporaire** : le PLF 2027 « n'est pas pérennisé » (T1). À partir de 2028, la référence perd les 5,0, et la surtaxe pérenne de LFI rapporte la totalité (environ 6,5 corrigé au lieu de 1,86). Cela **sous-estime le financement LFI** d'environ 4,6 Md€ par an dès 2028. Défavorise LFI.
- **Abattement des retraités.** Même logique pour `e_abat` : 1,4 en 2027, 1,8 en 2028, 1,1 ensuite. Les deux camps à 0 aujourd'hui, donc sans effet.

**Correction.** Introduire un profil annuel par ligne (colonnes `montant_2027` à `montant_2032`, ou un coefficient de montée en charge). Pour les mesures proposées comme temporaires, réintroduire leur montant hors référence dès qu'elles expirent.

### 4.3 Spread : le surcoût est appliqué aux tranches déjà refinancées

**Gravité : mineur.** Prudent ; affecte surtout les scénarios à forte dette, donc défavorise LFI intégral.

**Preuve.** Les intérêts sont calculés comme `spread_t × DETTE_REF × part_refinancée(t − 2026)` : le spread de l'année t s'applique à toute la dette refinancée depuis 2027. En réalité, chaque tranche garde le spread de l'année où elle a été refinancée. Avec un calcul par millésime, les intérêts supplémentaires de LFI intégral en 2032 passent de 55,1 à 43,7 Md€ (déficit de 9,11 → 8,79 %, dette de 149,2 → 148,5 %). Pour Ensemble : 22,3 → 17,4.

**Correction.** Cumuler le spread par millésime de refinancement (méthode codée dans `projection_variantes.py`).

### 4.4 Autres points

**Gravité : mineur.**

- `taux_oat` = 4,3 % (10 ans) est appliqué à toute la dette supplémentaire, dès la première année. Le coût moyen à l'émission, toutes maturités confondues, est plus bas. Prudent.
- Le choc de stress et le spread ne s'appliquent qu'à `DETTE_REF`, pas à la dette supplémentaire. Effet de second ordre.
- Le profil `part_refinancee` vient de la sensibilité de la seule dette de l'État (AFT). Il est normalisé à 1 à 9 ans puis appliqué à la dette de toutes les administrations publiques. Ordre de grandeur acceptable : 38 Md€ à 9 ans, contre 32,6 pour l'État seul.
- Le biais de la couche 2 est maintenu à −1,93 au-delà de 3 ans, et le solde 2030-2032 est extrapolé (colonne `extrapole`). Ces deux hypothèses sont bien signalées.
- Le PIB 2027 vaut 3 134 dans la projection et 3 140 dans l'application 2024 (`application_parametres`). Harmoniser.
- Le biais est commun à tous les scénarios : pas d'asymétrie.

---

## 5. Couche 1 (`mesures_cout.csv`, 25 mesures)

### 5.1 Comparabilité des chiffrages ex ante et ex post

| id | Problème | Gravité | Action |
|---|---|---|---|
| `retraites_2023` | Euros courants 2030 contre euros constants 2024 ; réestimation et non réalisé ; `ex_post_bas` d'un autre périmètre (voir 2.7) | important | recalculer à prix constants (environ −18 %) ; `ex_post_bas` = 9,7 ; marquer « réestimation » |
| `woerth_2010` | Euros 2008 contre euros 2016 (voir 2.8) | mineur | recalculer à prix constants (environ −14 %) |
| `is_25`, `th_20`, `ip_2021`, `hs_ir_2019`, `pacte_2015` | L'« ex post » est un chiffrage administratif à comportement constant (la note de `is_25` le dit), ou une somme calculée. Il est mécaniquement proche de l'ex ante | important pour l'erreur médiane | marquer `type_ex_post = administratif` et calculer la statistique avec et sans ces lignes |
| `bouclier_elec`, `bouclier_gaz_2023`, `cheque_*` | Écarts dus à des prix de l'énergie exogènes ou à une décision de non-prolongation (gaz −80 %, fioul −79 %). Ces dispositifs ne ressemblent pas aux mesures d'un programme | mineur à important | les exclure du calcul de `erreur_ligne`, ou les présenter dans une catégorie séparée |
| `bouclier_elec` | L'ex ante (21,8) est une estimation de la CRE de juillet 2023, déjà en cours d'exécution, pas un chiffrage avant adoption | mineur | prendre le chiffre du PLF 2023, ou exclure la ligne |
| `pa_2016` | `ex_post_haut` = 4,73 non sourcé | mineur | supprimer |
| `cir_2008` | Ex ante = coût total en croisière, ex post = créance 2010 (montée en charge, puis durcissement en 2011) | mineur | garder, en signalant le décalage |
| `tva_resto_2009` | Comparaison brute contre brute (3,0 et 3,3) : correcte. Le net (2,35 contre 2,6-2,7) est mentionné en note | — | — |

### 5.2 Sensibilité de l'erreur médiane (`couche1_sensibilite.py`)

| Échantillon | n | Erreur absolue médiane | À ±15 % |
|---|---|---|---|
| 25 mesures (publié) | 25 | 10,0 % | 16/25 |
| Hors énergie | 20 | 7,6 % | 14/20 |
| Hors ex post administratifs | 20 | 13,7 % | 11/20 |
| Hors énergie et administratifs | 15 | 10,0 % | 9/15 |

La médiane publiée de 10,0 % est stable, mais par compensation : les ex post administratifs la tirent vers le bas, les mesures énergie vers le haut. Sur les seules mesures dont l'ex post est réellement observé, l'erreur est de 13,7 % hors énergie. La borne basse de `erreur_ligne` (11,4 %) est donc plutôt optimiste.

**Gravité : important** pour la calibration. **Mineur** pour les paniers, qui utilisent la valeur centrale de T10b (14,9 %).

### 5.3 Lignes à exclure ou à requalifier

- **Exclure de la statistique principale** : `bouclier_gaz_2023`, `cheque_fioul_2022` et `bouclier_elec` (ex ante en cours d'exécution).
- **Requalifier** : `retraites_2023` en « réestimation », et les cinq lignes à ex post administratif.

---

## 6. Corrections recommandées, par ordre de priorité

| # | Gravité | Fichier / id | Correction | Effet estimé, sens |
|---|---|---|---|---|
| 1 | bloquant | `projection.py` + `moteur.py` (lignes « Investissement ») | Inclure l'emprunt règle d'or (30 Md€/an) dans la dette et les intérêts de la projection, dans une colonne séparée | LFI ajusté 2032 : dette 132,7 → 139,0 % ; défavorable à LFI ajusté |
| 2 | bloquant | `paniers.csv` `l_smic` et `l_bandeaux` | Traiter le gel du SMIC de référence des allègements de la même façon dans les deux lignes (voir 1.2) ; rechiffrer `l_smic` hors poste allègements (−21,5), ou ajouter le coût du dégel et retirer le gel de la décote des bandeaux | plus de 5 Md€ sur le solde LFI ; sens selon l'option |
| 3 | important | `moteur.py` `f_semi_elasticite`, `regles.csv` « Élasticité IS », `delta_is` | Formule 1 − s·(t0 + Δ) avec t0 = 25,83 et Δ = 7,73 ; forfait d'environ 0,73 ; donner une fourchette à `s_is` | `l_surtaxe` −0,4 ; défavorable à LFI |
| 4 | important | `paniers.csv` `l_zucman` (avec `l_isf`, `l_ir`, `l_pfu`) | Décote d'interaction : l'impôt plancher est diminué de l'IR, de l'IFI ou ISF, de la CSG et de la CEHR (PPL 768) | jusqu'à plusieurs Md€ ; défavorable à LFI |
| 5 | important | `paniers.csv` `l_ret62` (`l_ret60`) | Statique −6,4 (suspension 2027 de 1,9, T4p ; le 1,0 du PLFSS est un incrément) ; documenter ou remplacer le 8,3 de l'iFRAP ; facteur de référence de `l_ret60` à 0,967 | +0,9 (+0,7 après le facteur 0,8) ; favorable à LFI |
| 6 | important | `application_lignes.csv` `nfp_niches` | Ne pas retenir la ligne iFRAP marquée d'un astérisque : médiane de 14, ou 6,5 avec La Grande Conversation à périmètre comparable | −2,5 à −10 ; défavorable à LFI (application 2024) |
| 7 | important | `projection.py` | Profil de montée en charge par ligne ; expiration de la surtaxe dans la référence en 2028 | retraites : défavorable à LFI ; surtaxe : favorable à LFI (environ 4,6 Md€/an dès 2028) |
| 8 | important | `moteur.py` (incertitude) | Facteur d'erreur commun par chiffreur ; tirer `facteur_reference` dans son intervalle ; intervalles pour `eps_capital`, `s_is`, `a_sur_da`, `hausse_smic` | bandes P10-P90 nettement plus larges |
| 9 | important | `paniers.csv` `l_rachats`, `moteur_regles.csv` | Règle propre (t0 = 8 %, t1 = 33 %, forte substitution vers les dividendes) ; facteur de référence 0,976 ; variante ancrée sur le réalisé de 0,5 ; intervalle large | incertain, probablement défavorable à LFI |
| 10 | important | `mesures_cout.csv` `retraites_2023` et `woerth_2010` ; `moteur_parametres.csv` `facteur_reforme` | Comparer à prix constants ; `ex_post_bas` de `retraites_2023` à 9,7 ; recalculer `facteur_reforme` (≈0,82 / 0,84 / 0,86) | faible ; touche `e_feries`, `e_oper`, `e_fp` et `l_zucman` |
| 11 | important | `mesures_cout.csv` (5 lignes administratives, 5 lignes énergie) | Colonne `type_ex_post` ; statistiques avec et sans ces lignes ; exclure `bouclier_gaz_2023`, `cheque_fioul_2022` et `bouclier_elec` | médiane de 13,7 % sur les ex post observés (hors énergie) |
| 12 | important | `moteur_parametres.csv` `n_smic` | Effectif des salariés entre 1 et 1,15 SMIC ; intervalle sur l'élasticité ; trancher l'écart avec Montaigne (54 000 contre 300 000 emplois) | jusqu'à −3,8 ; défavorable à LFI |
| 13 | mineur | `paniers.csv` `e_appr`, `l_brunes`, `l_rachats`, `e_oper` | Règle unique pour les recoupements non chiffrés ; `e_appr` vers 0,84 ; `l_brunes` à environ 0,96 (trajectoire GNR BTP) | ±1 Md€, sens mixte |
| 14 | mineur | `paniers.csv` `l_bandeaux` | Retenir 11,4 (Bozio-Wasmer après effets emploi) au lieu de 12,1 | −0,35 ; défavorable à LFI |
| 15 | mineur | `paniers.csv` `e_elec`, `e_prime`, `l_autonomie` | Formule accise symétrique pour la baisse d'accise sur l'électricité ; vérifier l'effet d'aubaine de la PPV et l'hypothèse de recours de Montaigne | ±0,3 à 4 ; à vérifier |
| 16 | mineur | `paniers.csv` `l_isf` | Facteur de référence 0,978 ; note « écart 2022 », sans référence à « IFI 2027 » ; fourchette de 4,5 à 7,5 | +0,08 ; favorable à LFI |
| 17 | mineur | `statut_reference_2027.csv` `l_surtaxe_*` ; note de `l_ret62` | Synchroniser avec `paniers.csv` (0,286 ; statique tranché) | aucun |
| 18 | mineur | `moteur_regles.csv` (SMIC), `moteur_parametres.csv` `erreur_ligne` (borne basse), `regles.csv` (bases) | Texte « ≈46 000 » → 53 800 ; borne basse à 0,10 ; bases de « Réforme structurelle » à jour | aucun |
| 19 | mineur | `garde_fous.py` | Contrôler les lignes « absente » dont le montant de référence n'est pas nul, et l'égalité de règle par nature de mesure entre partis | aucun |
| 20 | mineur | `projection.py` | Spread cumulé par millésime ; PIB 2027 harmonisé | LFI intégral 2032 : −0,3 point de déficit ; favorable aux scénarios endettés |
| 21 | mineur | référence | Publier aussi la variante « loi votée seule » | LFI +7,7, Ensemble +5,4 |
