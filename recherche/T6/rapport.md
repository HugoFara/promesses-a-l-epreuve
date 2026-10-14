# T6 – Chiffrages des programmes NFP 2024 et Ensemble 2024, ligne par ligne et par institut

Date d'accès de toutes les sources : 2026-10-14. Fichiers produits :

- `chiffrages_par_institut.csv` : 60 lignes (id_ligne × chiffreur) ;
- `totaux_par_institut.csv` : 11 soldes ou totaux publiés ;
- `sources.csv` : 40 fichiers archivés dans `sources/T6/`, avec leur sha256.

Signe : impact sur le solde public. Une valeur négative creuse le déficit.

## 1. Principe de saisie

- Une ligne par couple (ligne cible, chiffreur). Le périmètre est ramené à celui de `application_lignes.csv` seulement quand l'institut donne lui-même la ventilation. Exemple : pour l'iFRAP, les retraites valent 50 + 24 (minima de pension), pour s'aligner sur les 58 de Montaigne qui incluent ces minima.
- Pour Montaigne et l'iFRAP, les lignes « autres » sont des résidus calculés : total publié moins les lignes isolées. La somme des lignes d'un chiffreur retombe donc sur son solde publié :

  | Programme | Chiffreur | Somme des lignes | Solde publié | Origine de l'écart |
  |---|---|---|---|---|
  | NFP | Montaigne | −178,5 | −179 | recettes de 54 au bandeau, 54,5 en additionnant les postes |
  | NFP | iFRAP | −160,3 | −160,4 | arrondi |
  | Ensemble | Montaigne | −20,6 | −20,6 | aucun |
  | Ensemble | iFRAP | +3,97 | +4,0 | arrondi (ligne `ens_hors_lignes` ajoutée pour les postes iFRAP sans ligne cible) |

- Pour La Grande Conversation, la valeur retenue est le point milieu de chaque fourchette. Les auteurs écrivent que leur scénario central (90) est « approximativement la moyenne » des fourchettes basse (60) et haute (120). Les points milieux additionnés font bien 90.
- Les lignes qu'un institut n'a pas chiffrées sont absentes. Exemples : Zucman, niches et égalité salariale chez Montaigne ; Zucman chez l'iFRAP, qui l'exclut sans le chiffrer.

## 2. Résultats par chiffreur

### Institut Montaigne (NFP −179 ; Ensemble −20,6), confiance high

Le site d'origine renvoie un défi Cloudflare à curl. Les pages ont été lues sur web.archive.org : synthèses des 08/07 et 10/07/2024, et toutes les fiches mesure archivées.

Toutes les valeurs de la colonne `independant` sont confirmées, avec trois réserves :

- **Autres recettes NFP.** Les postes listés font 19,1, mais le bandeau annonce 54 au total, d'où un résidu de 18,6 dans `application_lignes`.
- **TTF.** La fiche mesure annonce 9,3 Md€ (snapshots des 04/07 et 24/07), la synthèse 3,0. Incohérence interne à Montaigne.
- **Prime de partage de la valeur.** La première version de la fiche (20/06) donnait 6,5 Md€. Elle a été révisée à 2 (fourchette 1-3) le 21/06, après échange avec la campagne. Le notaire a aussi été révisé le 26/06.

Les fiches NFP sur l'ISF, les successions, l'IR et la garantie d'autonomie n'existent pas dans l'archive. Ces chiffres ne viennent que de la synthèse (« Autres mesures »).

### Fondation iFRAP (NFP −160,4 ; Ensemble +4,0), confiance high

Tableaux en image, lus avec l'outil Read après agrandissement :

- `ifrap_nfp_27_06_2024_v12h16.png` (dernière version, 27/06) ;
- `ifrap_lrem_21_06_2024.png`.

La note d'écarts NFP du 24/06 est lue elle aussi. Quatre constats nouveaux par rapport à `application_lignes` :

1. **Niches fiscales : 5 + 5 = 10 dans le tableau, et non 5.** Il y a deux lignes, dont une « (montant maximal) ». La note dit pourtant « tout au plus […] 5 milliards ». Double compte probable dans le total iFRAP.
2. **Égalité salariale : +10 compté dans les recettes iFRAP.** Asterès la reprend aussi. Dire « aucun chiffrage indépendant » reste juste, mais ces deux instituts l'incluent dans leur solde.
3. **Retraites : 50 dans le tableau, sans explication.** La note d'écarts donne pour le seul retour à 60 ans 68,8 en 2027 : 47,1 de dépenses et 21,7 de cotisations perdues, montants « bruts ». La mention « 50 net » d'`application_lignes` n'est pas étayée.
4. **Ensemble : la réforme chômage (+4,4) est comptée dans le solde de +4,0.** Le texte la dit pourtant « déjà inscrite au budget ». Sans elle, le solde iFRAP vaut environ −0,4. L'iFRAP chiffre aussi les frais de notaire à −2, compensés par +2 d'« abandon des mesures fiscales classes moyennes », soit un effet net nul.

### Asterès (NFP), confiance high (notes primaires)

La note qui porte le chiffrage est `ASTERES_NFP2.pdf` (« le chiffrage du Père Noël »). Asterès réestime seulement la phase 1 du plan NFP :

- dépenses ≈ 50 au lieu de 25 : point d'indice 22, abrogation de la réforme des retraites 15 (0,6 % du PIB), chômage 4, gratuité de l'école 7,6, APL 1,3 ;
- **toutes les recettes du NFP reprises « telles quelles »** : superprofits 15, ISF 15, niches 25, successions 17, IR 5,5, flat tax 2,7, Zucman 26, égalité 10, TTF 3.

Asterès conclut à « environ 50 milliards » de déficit par an. Les lignes additionnées donnent −55,7, parce que les phases sont arrondies à 20 + 20 + 10. Une autre note (`ASTERES_RN_NFP.pdf`) juge « crédible » un coût de 100 à 200 Md€ et précise : « Asterès n'a pas réalisé de chiffrage détaillé ».

Corrections à apporter à `application_lignes` / `application_programmes` :

- « Asterès ≈6 » pour l'ISF est une erreur. Le 6 est le rendement historique de l'ancien ISF, cité par Asterès ; Asterès retient 15. Le chiffre ≈ 6 pour ISF + PFU vient en réalité de l'OFCE.
- « Asterès ≥−50 » est juste mais incomplet : c'est une borne basse, à côté de la fourchette de −100 à −200.
- « Asterès ≈−10 » pour Ensemble : aucune note Asterès sur Ensemble n'a été trouvée (recherche sur le site, dans l'arborescence des fichiers, en presse).

**Pour la sensibilité, Asterès n'est pas un chiffreur indépendant côté recettes.**

### La Grande Conversation, désignée « Terra Nova » dans `application_lignes` (NFP), confiance high

C'est une note de Lucas Chancel, Anne-Laure Delatte et Elise Huillery publiée par la revue de Terra Nova le 21/06/2024. La revue précise que la publication « ne vaut pas approbation ». Ce n'est donc pas un chiffrage institutionnel de Terra Nova.

- Recettes seulement : +90/an en 2027 (fourchette 60-120). Aucune dépense chiffrée, donc pas de solde.
- Périmètres différents des autres chiffreurs :
  - l'exit tax est rangée avec l'ISF ;
  - les « niches » comprennent 15 Md€ d'exonérations de cotisations au-dessus de 1,6 SMIC ;
  - le « Zucman » est un IS de 25 % sur les multinationales, assis sur le chiffre d'affaires ;
  - les superprofits (15) sont exclus du total, comme recette exceptionnelle.

Aucun chiffrage Terra Nova propre des programmes NFP ou Ensemble n'a été trouvé.

### OFCE, confiance high (pages du site ofce-legislatives2024.fr)

L'OFCE **n'a pas chiffré les programmes**. La page Sciences Po indique que « l'évaluation complète et le bouclage macroéconomique des programmes est impossible à réaliser ».

On ne trouve que des chiffrages partiels, saisis avec un périmètre « composante seule » :

- abrogation de la seule réforme 2023 : 9,5 en 2027, 15,6 en 2030 (V. Touzé) ;
- point d'indice +10 % : 23 ex ante (0,8 point de PIB), 0,5 point de PIB ex post ;
- rétablissement de l'ISF et suppression du PFU : « environ 6 milliards » pour les deux.

Les pages « programmes » compilent d'autres chiffrages (Rabault, « gouvernement », Montaigne) dans des colonnes incohérentes : les valeurs « gouvernement » sont celles de l'iFRAP. Elles ne sont pas reprises ici.

L'OFCE (page spreads) donne aussi une sensibilité de la charge d'intérêts, non propre à un programme :

| Hausse du spread | Surcoût en 2027 | Surcoût à 10 ans |
|---|---|---|
| +0,3 point | ≈4 Md€ | ≈10 Md€ |
| +1,1 point (niveau italien) | ≈15 Md€ | ≈36 Md€ |

Ces ordres de grandeur pourraient étayer `nfp_taux` / `ens_taux`, mais aucun chiffreur n'attribue un spread à un programme.

### Fipeco, Rexecode : non trouvés

- **Fipeco** : seuls des avis qualitatifs de F. Ecalle (Alternatives Économiques, 15/07/2024, PDF hébergé par fipeco.fr ; LCP, 27/06/2024). Aucun montant par mesure. Recherches : WebSearch (×3), liste des commentaires de fipeco.fr (vide pour curl), archives.
- **Rexecode** : aucune publication sur les programmes de 2024 trouvée (WebSearch ×3). Rexecode n'est cité que pour son étude « 60 Md€ d'économies pour stabiliser la dette ».

### Chiffrages partisans relevés dans la presse (confiance medium, signalés comme non indépendants)

- **Camp présidentiel**, visuel « 286,8 Md€ » cité par Public Sénat et LCP le 19/06/2024 : retraite à 60 ans 53, garantie d'autonomie 14,8, point d'indice 20, CSG progressive 39. C'est un coût brut, et il inclut la 6e semaine de congés payés (30), absente du programme.
- **Valérie Rabault (PS)**, via Les Échos : 106 de dépenses sur 2024-2027, hors retraite à 60 ans. Garantie d'autonomie 5. L'article des Échos n'a pas été lu (paywall).
- **NFP (parti)** : 150 de dépenses et 150 de recettes en 2027, lu via la note iFRAP. Le document NFP du 21/06 n'a pas été lu. Pour Ensemble, la page OFCE reprend les montants de la campagne (prime 0,401 ; notaire 2 ; SNU 1,4 ; versement 1 ; leasing 0,1). Ce sont des annonces du parti, non saisies comme chiffreur.

## 3. Lignes où les chiffreurs divergent le plus

| Ligne | Fourchette (Md€/an) | Valeurs | Raisons données |
|---|---|---|---|
| nfp_retraites | −9,5 à −74 | OFCE −9,5 ; Asterès −15 ; camp présidentiel −53 ; Montaigne −58 ; iFRAP −74 (dont 50 pour âge et durée) | **Périmètre** : abrogation de 2023 seule (OFCE, Asterès), ou retour à 60 ans + minima + RSA (Montaigne). **Brut ou net** : l'iFRAP donne 68,8 brut (cotisations perdues) dans sa note, 50 dans son tableau. Montaigne retient ±15 % et ignore les effets chômage/invalidité. |
| nfp_isf | +3,5 à +22,5 | Montaigne 3,5 ; OFCE ≈6 (ISF + PFU) ; Asterès 15 (repris) ; iFRAP 15,2 ; LGC 22,5 (15-30) | **Assiette** : seuil de 5 M€, biens professionnels. **Exit tax** incluse chez LGC. Comportements non modélisés par LGC (« estimation approximative »). Montaigne : pas de fiche. |
| nfp_zucman | absent à +26 | Montaigne non chiffré (« quasi-impossible […] avant 2027 ») ; iFRAP exclu (« très théorique ») ; LGC 16 ; Asterès 26 (repris) | **Calendrier** : coopération internationale nécessaire. **Conception** : LGC chiffre un IS assis sur le chiffre d'affaires. |
| nfp_niches | absent à +25 | Montaigne non chiffré (« en l'absence de précisions ») ; iFRAP 10 (5 + 5, double compte probable) ; LGC 23 ; Asterès 25 (repris) | **Périmètre** : LGC inclut 15 Md€ d'allègements de cotisations. L'iFRAP juge 5 au maximum. |
| nfp_superprofits | 0 à +15 | iFRAP 0 ; LGC 0 (15 exclus) ; Montaigne 15 ; Asterès 15 (repris) | **Récurrence** : l'iFRAP et LGC la jugent ponctuelle. Montaigne la compte mais documente des rendements ex post 20 à 43 fois inférieurs aux prévisions. |
| nfp_succession | +5 à +17 | iFRAP 5 ; Montaigne 9 ; LGC 12,5 ; Asterès 17 (repris) | **Constitutionnalité** de l'héritage maximum (iFRAP) ; ciblage du top 1 % (LGC). |
| nfp_autonomie | −5 à −14,8 | Rabault −5 ; Montaigne −12,3 ; iFRAP et camp présidentiel −14,8 | **Population** : jeunes sous le seuil de pauvreté, ou 16-18 ans (iFRAP). Taux de recours non explicité. |
| nfp_egalite | absent à +10 | iFRAP 10 et Asterès 10, montants du parti repris dans leurs soldes ; Montaigne et LGC absents | Aucune estimation propre. |
| nfp_autres_dep | −133 à −163 | iFRAP −133,3 ; Montaigne −162,7 ; Asterès −159,9 (dont 125 repris du NFP) | **Classement** : Montaigne compte SMIC 19, indexation des pensions 13,4, culture/sport 20,2 et juge le chômage « marginal ». L'iFRAP compte le chômage 11,3, gaz et kWh 15,5, APD 5,4, pôle médicament 6. |
| ens_prime | −1,07 à −2 | iFRAP −1,07 ; Montaigne −2 (1-3 ; 6,5 en première version) ; campagne −0,4 | **Hypothèse de substitution** prime/salaire et coût du travail. |
| ens_succession | −1,7 à −3 | iFRAP −1,7 ; Montaigne −3 | Montaigne extrapole l'étude d'impact de 2012 (successions + petits-enfants + donations, ≈1 chacun). |
| ens_chomage | +4,4 / +4,5 | Les deux le comptent comme économie | **Référence** : la règle du projet (déjà dans la référence, facteur 0) contredit les deux soldes publiés. |
| ens_fraude, ens_versement, ens_elec, ens_retention | – | Chacune chiffrée par un seul institut : fraude +3 (iFRAP) ; versement −5, électricité −2,4, rétention +1,8 (Montaigne) | Sélection des mesures. C'est la principale raison de l'écart entre les soldes Ensemble (−20,6 contre +4,0). |

Les soldes vont de −50 (Asterès, borne basse) à −179 (Montaigne) pour le NFP, et de −20,6 à +4,0 pour Ensemble. Pour le NFP, l'essentiel de l'écart vient du côté recettes : prendre ou non les montants du parti (Zucman, niches, superprofits, égalité salariale représentent 76 Md€ chez Asterès, contre 0 chez Montaigne). Côté dépenses, l'écart entre Montaigne et l'iFRAP n'est que d'environ 18 Md€ (−233 contre −215,3).

## 4. Décisions laissées à l'intégrateur

1. **Asterès comme point de départ.** Ses recettes sont celles du parti. Le traiter comme un scénario « montants du parti + correction des dépenses de phase 1 » plutôt que comme un chiffreur indépendant ? Et retenir −50 (borne basse) ou −100 à −200 (« crédible ») ?
2. **Niches iFRAP.** Garder 10 (tableau) ou 5 (note d'écarts) ?
3. **Retraites iFRAP.** Retenir −74 (aligné sur Montaigne) ou −50 (âge et durée seuls) ? Le 68,8 brut de la note contredit le 50 du tableau.
4. **Autres recettes Montaigne.** 19,1 (postes listés) ou 18,6 (résidu du bandeau) ? Et la TTF à 3,0 (synthèse) ou 9,3 (fiche) ?
5. **Lignes « composante seule » de l'OFCE.** Elles ne couvrent pas la ligne entière et ne doivent pas servir de point de départ pour toute la ligne.
6. **Égalité salariale.** L'iFRAP et Asterès la comptent : leur appliquer le facteur 0,333 « effet promis », comme au parti ?
7. **Chômage côté Ensemble.** La neutraliser (facteur 0) change le solde iFRAP de +4,0 à environ −0,4, et celui de Montaigne de −20,6 à −25,1.
8. **Chiffrages partisans** (camp présidentiel, Rabault) : à exclure de la sensibilité principale, à mentionner seulement en note.

## 5. Ce qui n'a pas été lu

- institutmontaigne.org en direct (Cloudflare) : remplacé par Wayback, sans perte de contenu identifiée ;
- l'article des Échos du 18/06 (Rabault) et celui du 24/06 (« 119 Md€ » de recettes) : paywall, non trouvés en accès libre ;
- le visuel du camp présidentiel et le document NFP « proposition macroéconomique » du 21/06, pas cherchés en priorité (montants des partis, hors périmètre T6) ;
- les fiches Montaigne NFP sur l'ISF, les successions, l'IR et la garantie d'autonomie : absentes de l'archive.

## 6. Précisions demandées par le coordinateur

1. **iFRAP et Zucman.** Le tableau iFRAP ne contient aucune ligne Zucman, et l'iFRAP ne l'évalue pas explicitement à 0. Sa note d'écarts dit seulement : « Le produit espéré de 26 milliards d’euros semble lui aussi très théorique ». Les « 73 milliards » de recettes qu'elle juge non crédibles valent 15 + 20 + 12 + 26 : les 26 du Zucman y sont donc retirés en entier, ce qui revient à un 0 implicite. Pas de ligne `nfp_zucman,iFRAP` ajoutée.
2. **Montaigne, Zucman et niches.** Les deux mesures sont explicitement non chiffrées, dans la liste « Autres mesures » des dépenses de la synthèse : « Appliquer l’impôt Zucman […] : mesure non-chiffrée car le temps des négociations multilatérales rend quasi-impossible son adoption avant 2027 » et « Supprimer les niches fiscales inefficaces, injustes et polluantes : mesure non chiffrée en l’absence de précisions ». Elles ne figurent pas dans les recettes (54 ; 54,5 en additionnant les postes) et ne pèsent donc rien dans le −179.
3. **Asterès.** Il n'y a pas de double compte : 50,2 = 25 + 17 + 5,5 + 2,7 et 39 = 26 + 10 + 3, soit neuf postes distincts. L'écart entre −55,7 et ≈−50,8 vient de l'arithmétique d'Asterès : en phase 2, il compare les recettes à 70 alors que les dépenses sont de 75. Note ajoutée à la ligne `nfp_autres_dep` d'Asterès ; aucune valeur modifiée.
