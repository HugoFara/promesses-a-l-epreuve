# T10a, groupe B : notes

Date d'accès de toutes les sources : 2026-10-14. Les fichiers archivés sont listés dans `sources_B.csv`.

## Bilan

| Candidat | Décision | Fichier |
|---|---|---|
| (1) Bascule CSG / cotisations salariales 2018 | **Exclu** : ex post non trouvé | — |
| (2) Pepa 2019 | **Coût exclu**, **effet retenu** (aubaine) | effets_B.csv `pepa_2019_aubaine` |
| (3) PPV 2022 | **Coût exclu**, **effet retenu** (aubaine) | effets_B.csv `ppv_2022_aubaine` |
| (4a) Relèvement du plafond heures sup à 7 500 € (LFR 2022) | **Exclu** : aucun chiffrage ex ante, pas d'ex post séparé | — |
| (4b) Volet IR des heures sup 2019 | **Retenu** | cout_B.csv `hs_ir_2019` |
| (5) Baisse de l'IR 2020 | **Retenu** (confiance medium) | cout_B.csv `ir_baisse_2020` |
| (6) Sous-indexation des pensions 2019 (+0,3 %) | **Exclu** : ex post non trouvé | — |

## (4b) Exonération d'IR des heures supplémentaires (LMUES, décembre 2018) : retenu

- **Ex ante** (étude d'impact du PJL portant mesures d'urgence économiques et sociales, 19/12/2018, art. 2, §3.2.2, PDF p. 17) : « Le coût de l'exonération d'impôt sur le revenu est estimé à 1,9 Md€ en année pleine, mais à 1,0 Md€ seulement en 2019 ».
  - Le tableau donne les montants pour l'État : −1,1 en 2019, −1,9 en 2020, −2,2 en 2021 et −1,9 en 2022 (Md€).
  - Le régime de croisière est annoncé pour 2022, à cause du prélèvement à la source.
- **Ex post** (Voies et moyens tome II, dépense fiscale 120146, fiabilité « ordre de grandeur ») :
  - réalisé 2020 : 1 879 M€ (PLF 2022) ;
  - réalisé 2021 : 2 091 M€ (PLF 2023) ;
  - réalisé 2022 : 1 707 M€ (PLF 2024).
- **Comparaison retenue** : 2020, première année pleine. 1,9 contre 1,879, soit un ratio d'environ 0,99 (calculé). Les autres années restent proches : 2021 donne 2,2 contre 2,091 (ratio d'environ 0,95), 2022 donne 1,9 contre 1,707 (environ 0,90).
- **Vigilance**
  - Le plafond a été relevé temporairement à 7 500 € pour les heures effectuées du 16/03 au 10/07/2020, puis de façon pérenne à partir de 2022 (LFR 2022). Les réalisés 2021 et 2022 ne sont donc pas exactement sur le périmètre ex ante (plafond de 5 000 €).
  - Le réalisé 2019 (VM tome II du PLF 2021) n'a pas été trouvé en ligne.
- **Volet cotisations salariales** (ex ante 1,96 Md€ en année pleine, dont 1,74 Md€ pour le régime général) : le réalisé n'a pas été trouvé. Endroits cherchés : annexe 5 du PLFSS, CCSS, recherches web. Ce volet n'est donc pas retenu.

## (5) Baisse de l'IR 2020 (LF 2020, art. 2) : retenu, confiance medium

- **Ex ante** (exposé des motifs de l'art. 2, PLF 2020 n° 2272, PDF p. 37) : « pour un montant global d'environ 5 milliards d'euros », 16,9 millions de foyers, gain moyen de 303 €.
  - Le document séparé « Évaluations préalables des articles » du PLF 2020 n'a pas été obtenu. Essais infructueux : AN `pl2272-ei.pdf`, `l15b2272_evaluation-prealable.pdf`, `l15b2272_etude-impact.pdf`.
- **Ex post** (Insee, *France, portrait social* 2022, dossier « Les réformes sociofiscales de 2020 et 2021 », figure 1 p. 89, texte p. 91) : +5 390 M€ de revenu disponible pour 15,3 millions de ménages, soit environ 5,4 Md€.
  - Il s'agit d'une microsimulation (Ines 2021) et non de l'exécution budgétaire.
  - Champ : France métropolitaine, ménages ordinaires. Les DOM sont exclus, ce qui sous-estime légèrement le total national.
  - Législation 2021 : mesure pleinement montée en charge.
- **Ratio** : environ 1,08 (calculé). Cause classée « Aucune (coût conforme) », l'écart étant inférieur à 10 %.
- **Non obtenu** : le coût réalisé en comptabilité budgétaire, cherché dans le RBDE 2020 et la NEB Recettes fiscales 2020 de la Cour des comptes. vie-publique.fr (279420.pdf) et ccomptes.fr renvoient du HTML ou bloquent, avec curl comme avec WebFetch.
- **Vigilance** : la note Trésor sur le PLF 2020 (vue seulement dans un extrait de recherche, non lue) évoque 4,3 Md€ de gain pour les ménages en 2020, en année budgétaire. Je ne l'ai pas utilisée.

## (2) Pepa 2019 : coût exclu, effet retenu

- **Ex ante** (étude d'impact LMUES, art. 1er, §4.1.3, PDF p. 8) : « Dès lors que les primes n'auraient pas été versées sans ce dispositif, son impact est neutre pour les finances publiques. » Le coût annoncé est donc nul, et aucun montant de primes attendu n'est chiffré.
  - L'étude rappelle seulement le précédent de 2006 (600 M€) et ajoute que ce précédent « ne permet donc pas d'anticiper l'ampleur du dispositif ».
- **Ex post** (Insee, ECRT 2020, encadré 3) :
  - 2,2 Md€ versés au T1 2019 (4,8 millions de salariés, selon l'Acoss, cité par l'Insee) ;
  - effet d'aubaine de 15 % (estimation micro par appariement) à 40 % (estimation macro).
- **Pourquoi le coût est exclu** : avec un ex ante de 0, le ratio n'est pas défini. Le coût ex post de 2019 (prélèvements perdus sur la part d'aubaine) n'est chiffré par aucune source lue.
  - Je n'ai pas calculé d'ordre de grandeur (environ 2,2 Md€ × 15-40 % × taux de prélèvement), car ce serait une valeur dérivée et fragile.
  - Pour la **Pepa 2021**, l'Insee (FPS 2022, encadré p. 88) chiffre l'exonération côté ménages à 70, 190 ou 460 M€ selon une aubaine de 15, 40 ou 100 %. Ce chiffrage exclut les cotisations employeurs et porte sur un autre millésime : il n'est pas comparable.
- **Effet** : annonce nulle, contre 15 à 40 % d'aubaine mesurée, d'où le verdict « Sous-estimé ». ratio_central est laissé vide.

## (3) PPV 2022 : coût exclu, effet retenu

- **Ex ante** (étude d'impact du PJL pouvoir d'achat, juillet 2022, art. 1er, §4.2.3, p. 33) : l'exonération « n'occasionne pas de coût direct ». Les conditions de versement visent à éviter la substitution.
  - Le seul ordre de grandeur donné est illustratif : « à titre d'exemple, une hausse de 50 % [...] représenterait des gains de pouvoir d'achat de plus de 6 milliards d'euros » (p. 34). Ce n'est pas une prévision, je ne l'ai pas retenu.
  - Le Conseil d'État avait jugé l'étude d'impact insuffisante sur ce point (avis 405548, vu seulement dans un extrait de recherche).
- **Ex post** (Insee, Note de conjoncture de mars 2023) :
  - 4,1 Md€ versés au second semestre 2022 (branches marchandes non agricoles), près de 5 millions de bénéficiaires, 806 € en moyenne ;
  - aubaine « estimée en première analyse à environ 30 % », avec une marge d'erreur importante.
- **Pourquoi le coût est exclu** :
  - ex ante nul ;
  - la PPV n'apparaît pas comme dépense fiscale dans les VM tome II des PLF 2022 à 2024 (recherche de « partage de la valeur » et de « pouvoir d'achat » : 0 résultat) ;
  - aucun coût réalisé officiel n'a été trouvé. Le rapport d'évaluation que le Gouvernement devait remettre avant le 30/06/2024 (ou le 31/12/2024 selon la version du texte) n'a pas été trouvé.
  - Montants Urssaf 2023 (5,3 Md€) : vus seulement dans des extraits de recherche secondaires, non utilisés.
- **Effet** : confiance medium, car l'estimation est explicitement provisoire.

## (1) Bascule CSG / cotisations 2018 : exclu

- **Ex ante** : PLFSS 2018 (hausse de CSG d'environ 22,5 Md€, suppression de cotisations d'environ 17,7 à 18,5 Md€, chiffres vus seulement dans des extraits secondaires). L'étude d'impact elle-même n'a pas été lue faute d'ex post.
- **Ex post** : aucun bilan du rendement réalisé ni du coût net 2018 sur le même périmètre. Endroits cherchés : CCSS juin et septembre 2019, Cour des comptes RALFSS, Acoss, recherches web multiples.
- **Vigilance pour une reprise** :
  - calendrier en deux temps : cotisations chômage réduites de 1,45 pt au 1/1/2018 puis supprimées au 1/10/2018 ;
  - la hausse de la CSG porte aussi sur les revenus du capital et les pensions ;
  - compensation pour les fonctionnaires et les indépendants.
  - Le coût net de 2018 n'est donc pas un régime de croisière.

## (4a) Plafond des heures sup à 7 500 € (LFR 2022, art. 4) : exclu

- Mesure issue d'amendements parlementaires (n° 166 et suivants), sans chiffrage dans les amendements trouvés.
- Ex post non séparable : la DF 120146 agrège tout le dispositif.

## (6) Revalorisation de 0,3 % des pensions en 2019 : exclu

- **Ex ante** lu (PLFSS 2019, annexe 9, art. 44, PDF p. 380, sur l'ensemble des prestations hors APL, PA et AAH) :
  - économie totale de 3,2 Md€ en 2019, 6,1 en 2020 et 6,4 en 2021 ;
  - dont pensions de retraite : 2,8 Md€ en 2019 (ROBSS 2,0 et État 0,8), 5,2 en 2020 et 5,4 en 2021 ;
  - hypothèses macro du 04/09/2018.
- **Ex post** : aucune estimation de l'économie réalisée trouvée (CCSS, Cour des comptes, Drees, recherches web).
  - Les rapports du Sénat (PLFSS 2020, l19-104) sont inaccessibles par curl.
- **Périmètre** :
  - l'économie réalisée dépend de l'inflation effective. Le coefficient légal hors mesure aurait été d'environ 1,5-1,6 %, vu seulement dans des extraits secondaires (circulaire Cnav, QE) ;
  - l'annulation de la sous-indexation pour les pensions de moins de 2 000 € (LFSS 2020) porte sur **2020**, pas sur 2019 ;
  - la mesure « gilets jaunes » de 2019 portait sur la CSG des retraités (taux de 6,6 %), et non sur la revalorisation.
  - Une comparaison sur 2019 serait donc possible sur le même périmètre si l'on trouvait un ex post, par exemple dans le rapport CCSS de septembre 2019 ou le RALFSS 2020.

## Fichiers produits

`cout_B.csv` (2 lignes), `effets_B.csv` (2 lignes), `sources_B.csv` (10 fichiers), ce fichier.
