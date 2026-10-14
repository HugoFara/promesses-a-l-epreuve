# T13 — Effet emploi du SMIC et règle propre pour les rachats d'actions (14 octobre 2026)

Points 3.3 et 3.4 de l'audit (`recherche/audit/rapport.md`). Recherches documentaires : `smic_recherche.md` et `rachats_recherche.md` (sources dans `sources/T13/`, index `sources.csv`). Citations clés vérifiées dans les PDF archivés.

## 1. Effet emploi du SMIC à 1 600 € net (`l_smic_emploi`)

**Ce qui n'allait pas.** Le moteur calculait 0,17 × 14,4 % × 2,2 M = 53 856 emplois perdus. Trois incohérences :
- **−0,17 (Dube 2019, p. 27)** est une élasticité « own-wage » : la variation de l'emploi d'un groupe rapportée à la hausse du salaire *moyen* de ce groupe. C'est une médiane d'études américaines, valide selon Dube « up to around 59% of the median wage » (p. 3). Or la France est à 62,5 % (rapport Smic 2025, p. 5) et passerait à environ 71 %. L'« intervalle » (−0,19 ; −0,17) était fait de deux médianes, pas d'un intervalle de confiance.
- **2,2 M** compte les bénéficiaires de la revalorisation du 1er novembre 2024 (enquête Acemo ; rapport Smic 2025, p. 51). Une hausse de 14 % touche toute la tranche 1-1,15 SMIC.
- Les élasticités françaises, issues des évaluations des allègements, sont plus fortes : **−0,6 à −0,9** pour le groupe d'experts Smic 2025 (p. 146 et 148), **−0,6** pour Bozio-Wasmer 2024 (« plus plausible que les élasticités des années 2000 », p. 175-176).

**Nouvelle règle** (`moteur_regles.csv`, formule `emploi_smic`) : emplois perdus = |élasticité au coût| × hausse moyenne du coût dans la tranche × effectif de la tranche, multipliés par le coût d'un emploi perdu (15-17 k€).

| Paramètre | Bas | Central | Haut | Source |
|---|---|---|---|---|
| Élasticité au coût (`eps_smic`) | −0,17 (Dube) | **−0,6** (Bozio-Wasmer, bas du groupe d'experts) | −0,9 (groupe d'experts) | `elasticites.csv` smic_fr |
| Effectif 1-1,15 SMIC (`n_smic_tranche`) | 2,2 M (Acemo) | **2,5 M** (BTS 2023 interpolée) | 3,0 M (Bozio-Wasmer ramené à 1,15) | `parametres_bareme.csv`, confiance low |
| Hausse moyenne du coût (`hausse_moy_smic`) | 6,9 % | **6,9 %** (sans diffusion) | 14,4 % (diffusion complète) | calcul sur la distribution BTS |

**Correction apportée à la proposition de l'agent de recherche** : il appliquait 14,4 % à toute la tranche (216 000 emplois au central), alors que la hausse ne vaut 14,4 % qu'au SMIC même ; vers 1,10 SMIC, elle n'est que de 4 %. Une élasticité au coût se multiplie par la hausse moyenne du coût de la tranche. La diffusion complète des hausses jusqu'à 1,15 SMIC, que supposent Montaigne et l'iFRAP, est gardée en borne haute.

**Résultat** : **103 500 emplois** au central (contre 53 856), soit **−1,67 Md€** (contre −0,87). Bornes : environ 29 000 (Dube appliqué strictement) et 389 000 (−0,9 × 14,4 % × 3,0 M ; Montaigne : 230 000-380 000). Solde LFI intégral −68,7 → −69,5 ; LFI ajusté +10,5 → +9,7.

**Limites** :
- aucun effectif 1-1,15 SMIC n'est publié : 2,5 M repose sur une lecture graphique (12,9 % entre 1,05 et 1,2 SMIC) ;
- ce sont des destructions brutes, avant effet de demande ; l'OFCE passerait de −322 000 brut à −29 000 net (chiffres lus seulement dans une contribution de FO, étude non lue) ;
- avec le gel du SMIC de référence des allègements, le coût monte plus que le salaire au niveau du SMIC (dégressivité), ce qui va vers la borne haute ;
- la hausse est calculée sur la base 2024 (celle du coût statique de Montaigne) ; sur la base de janvier 2026 (1 443,11 € net), elle ne serait que de 10,9 %, ce qui réduirait à la fois le coût et l'effet emploi ;
- tirages indépendants des trois paramètres dans le Monte-Carlo (l'agent proposait des triplets liés) : l'intervalle est un peu plus étroit aux extrêmes.

**Symétrie** : la même élasticité n'est appliquée à aucune ligne d'Ensemble. Le rabot des bandeaux d'allègements reprend un chiffrage qui inclut déjà ses effets emploi (statique 11,4 « après effets emploi »).

## 2. Règle propre pour la taxe renforcée sur les rachats d'actions (`l_rachats`)

**Ce qui n'allait pas** (audit §3.3) : la ligne (8,4 Md€ statiques = 33 % × 25,5 Md€, calcul de l'auteur de l'amendement I-105) recevait la règle « Élasticité capital » (facteur 0,437). Ce facteur était calculé sur les taux marginaux des dividendes chez l'actionnaire, alors que la taxe est payée par la société et que les dividendes, qui y échappent, sont un substitut direct. La taxe existante (0,2) n'était retirée qu'à 2,4 % près, par un facteur de référence multiplicatif.

**Ce que dit la recherche** (`rachats_recherche.md`) :
- **Assiette** : les « 25,5 milliards d'euros en 2025 » de l'amendement sont les rachats du **CAC 40 en 2024** (Lettre Vernimmen n° 223, vérifiée). La même série donne 30,1 Md€ en 2023 et 34,8 Md€ en 2025, dont environ 5 Md€ ponctuels (Axa).
- **Réaction à une taxe de 1 %** (États-Unis, 2023) : −25 % par entreprise (Autore et al., JCF 2025, résumé), −5 à −10 % (Bargeron et al., lu de seconde main), effet devenu non significatif en 2025 (communication AAA 2026, non relue par des pairs). Pas de hausse compensatoire des dividendes à ce taux.
- **Seuil de parité** : un taux d'environ 1,6 à 4,6 % suffit à supprimer l'avantage fiscal des rachats sur les dividendes aux États-Unis (Penn Wharton). À 33 %, payé par la société, le report vers les dividendes domine, sauf motifs non fiscaux (anti-OPA, plans salariés).
- **Chiffrages officiels d'une version renforcée** : aucun avec méthode. Le Sénat annonçait « autour d'un milliard » pour 4 % de la valeur réelle (PLF 2025, via Public Sénat) ; les « 6,5 milliards » prêtés à la ministre en 2025 n'ont pas été lus (senat.fr injoignable). À l'Assemblée, l'amendement I-105 a été adopté contre l'avis du rapporteur général et du gouvernement, sans chiffrage (compte rendu du 29/10/2025, vérifié).

**Nouvelle règle** « Taxe sur les rachats d'actions » (formule `assiette_reduite_nette`) : facteur = (1 − part perdue) × assiette relative − taxe existante / statique.

| Paramètre | Bas | Central | Haut | Fondement |
|---|---|---|---|---|
| Part de l'assiette perdue (`part_perdue_rachats`) | 0,60 | **0,85** | 0,97 | extrapolation s = 1 − (1 − b)^33, b = 2,5 à 10 % par point ; jugement (confiance low) |
| Assiette relative (`assiette_rachats_rel`) | 22/25,5 | **1** | 35/25,5 | Vernimmen ; bas = retrait des groupes à siège étranger (jugement) |
| Taxe existante retranchée (`part_taxe_rachats_existante`) | | **0,2/8,4** | | PLF 2027, état A, ligne 1796 |

Le facteur de référence passe à 1 : la taxe existante est retranchée en montant fixe dans la formule, ce qui reste juste quel que soit le tirage.

**Résultat** : **1,06 Md€** net (P10-P90 0,6-2,7), contre 3,58. Solde LFI intégral −69,5 → **−72,0** ; LFI ajusté +9,7 → **+7,2** ; variante « dégel » −96,6 et −17,3.

**Limites** :
- toutes les mesures causales portent sur un taux de 1 % ; 33 % est hors de tout échantillon ;
- les dividendes de substitution rapportent un peu de PFU, sur les seuls actionnaires résidents imposables : ce gain n'est pas compté, ce qui joue contre LFI (montant non chiffré) ;
- le risque juridique (directive mère-fille ; décision QPC 2026-1189 qui motive la conformité de la taxe actuelle « eu égard au taux ») n'est pas ajouté, pour éviter un double compte ;
- la règle n'est pas testable : il n'existe aucune mesure passée comparable.

## 3. Effets d'ensemble

| | Avant T13 | Après |
|---|---|---|
| LFI intégral | −68,7 | **−72,0** |
| LFI ajusté | +10,5 | **+7,2** |
| Ensemble | −7,2 | −7,2 |
| Dette 2032, LFI intégral / ajusté | 143,9 / 133,9 % | 144,2 / 134,2 % |

Les deux corrections jouent contre LFI (−3,3 Md€ au total), comme l'audit l'anticipait (« défavorable à LFI »). La part des corrections du panier LFI ajusté qui repose sur une règle confirmée tombe de 44 % à 8 %, parce que la correction des rachats ne relève plus de la règle « Élasticité capital », qui est confirmée. Aucune ligne d'Ensemble n'était concernée par ces deux points.
