# T10a : extension de la couche 1 (backtest mesure par mesure)

Date d'accès de toutes les sources : 2026-10-14. Toutes les sources primaires lues sont archivées dans `sources/T10a/`, soit 54 fichiers dont le sha256 a été vérifié. Ils sont listés dans `sources.csv`.

## 1. Résultat

**18 nouvelles mesures retenues.** Avec les 11 mesures existantes, la couche 1 en compte **29**, au-delà de l'objectif de 25. **7 lignes d'effets** ont été retenues.

| Fichier | Contenu |
|---|---|
| `mesures_cout_nouvelles.csv` | 18 lignes, aux colonnes de `data/mesures_cout.csv`, plus `citation_ex_ante`, `page_ex_ante`, `citation_ex_post` et `page_ex_post` |
| `mesures_effets_nouvelles.csv` | 7 lignes, aux colonnes de `data/mesures_effets.csv`, plus les citations, la page, `confiance` et `note` |
| `sources.csv` | 54 sources archivées |
| `parts/notes_[A-D].md` | Détail par candidate : pages, valeurs calculées, tentatives d'accès |
| `parts/*_[A-D].csv` | Fichiers bruts par groupe, avant fusion |

La recherche a été répartie entre quatre agents (groupes A à D), puis les résultats ont été fusionnés et contrôlés (§ 5).

### Coûts (Md€/an, grandeurs positives, le sens est donné par `sens`)

L'écart vaut (ex post central − ex ante) / ex ante. C'est une valeur calculée.

| id | Année | Sens | Ex ante | Ex post (bas-central-haut) | Écart | Cause | Confiance |
|---|---|---|---|---|---|---|---|
| tva_resto_2009 | 2009 | coût | 3,0 | 3,3 | +10 % | Base de référence | high |
| cir_2008 | 2008 | coût | 2,7 | 4,7-5,05-5,2 | +87 % | Élasticité comportementale | medium |
| cite_2015 | 2015 | coût | 1,4 | 1,7 | +21 % | Élasticité comportementale | medium |
| pinel_2015 | 2015 | coût (générationnel) | 1,7 | 1,563 | −8 % | Aucune | low |
| mpr_2020 | 2020 | coût | 0,39 | 0,162-0,162-0,455 | −58 % | Taux de recours | low |
| hs_ir_2019 | 2019 | coût | 1,9 | 1,879 | −1 % | Aucune | high |
| ir_baisse_2020 | 2020 | coût | 5,0 | 5,39 | +8 % | Aucune | medium |
| ip_2021 | 2021 | coût | 10 | 10,3-10,3-10,6 | +3 % | Aucune | medium |
| is_25 | 2018 | coût | 11,2 | 11,7 | +4 % | Aucune | medium |
| th_20 | 2021 | coût | 5,5 | 5,6 | +2 % | Aucune | medium |
| pacte_2015 | 2015 | coût | 5,4 | 5,3 | −2 % | Aucune | medium |
| cap_2022 | 2022 | coût | 3,1 | 3,0 | −3 % | Aucune | low |
| ac_2021 | 2021 | économie | 1,93 | 1,9 | −2 % | Aucune | low |
| apl_contemp_2021 | 2021 | économie | 0,75 | 1,11 | +48 % | Conjoncture | medium |
| cheque_energie_exc_2021 | 2021 | coût | 0,6 | 0,488-0,493 | −18 % | Taux de recours | high |
| cheque_energie_exc_2022 | 2022 | coût | 1,8 | 1,528-1,53 | −15 % | Taux de recours | medium |
| cheque_fioul_2022 | 2022 | coût | 0,23 | 0,036-0,048-0,052 | −79 % | Taux de recours | medium |
| bouclier_gaz_2023 | 2023 | coût | 6,8 | 1,35 | −80 % | Prix de l'énergie | medium |

**Statistiques calculées.** Pour chaque mesure, l'erreur absolue rapporte |ex post central − ex ante| à l'ex ante.

- Les 18 nouvelles : erreur absolue médiane de 9,0 % (moyenne 25 %) ; 11 sur 18 sont à ±15 %.
- En excluant les 4 lignes `low` : médiane de 12,5 %.
- Les 29 mesures, existantes comprises : médiane de 9,1 % ; 19 sur 29 sont à ±15 %.
- Avec cette formule, les 11 mesures existantes donnent 9,1 %, alors que le HANDOFF annonce 11,4 %. Le HANDOFF utilise donc une autre convention de calcul, qu'il faudra harmoniser lors de l'intégration.

**Lecture.**

- **Mesures fiscales à barème (IR, IS, TH, impôts de production, cotisations)** : écarts faibles, de 1 à 10 %.
- **Assiette mal connue ou comportement de recours à la hausse (CIR, CITE, APL)** : forts dépassements, de +20 à +90 %. Pour les APL, le dépassement de l'économie est favorable au solde.
- **Dispositifs d'urgence (chèques, bouclier gaz)** : surestimés ex ante, de −15 à −80 %, à cause du non-recours et de la baisse des prix. Leur budget initial est une enveloppe de crédits plus qu'un chiffrage.

### Effets

| id | Annoncé | Constaté | Ratio | Verdict | Confiance |
|---|---|---|---|---|---|
| tva_resto_emploi | 40 000 emplois en 2 ans | ≈19 500 en 3 ans (Thévenoud 2012) | 0,49 | Surestimé | medium |
| tva_resto_prix | −3 % de l'indice des prix (comité de suivi, déc. 2009) | −2,2 à −2,5 % | 0,78 | Surestimé | medium |
| tva_resto_prix_montant | 1 Md€/an rendu aux consommateurs | 0,59 Md€/an | 0,59 | Surestimé | medium |
| pinel_logements | 50 000 logements (génération 2015) | ≈50 000 | 1,0 | Conforme | low |
| pepa_2019_aubaine | Aubaine nulle (« neutre pour les finances publiques ») | 15 % (micro) à 40 % (macro) des 2,2 Md€ versés (Insee) | n.d. | Sous-estimé | high |
| ppv_2022_aubaine | « Pas de coût direct » | ≈30 % d'aubaine (Insee, première analyse) | n.d. | Sous-estimé | medium |
| cheque_fioul_benef | ≈1,6 M ménages éligibles | ≈306 000 chèques émis | 0,19 | Surestimé | medium |

- **TVA restauration, baisse de prix de 11,8 %** : elle portait sur 7 produits sur 10 et ne se compare pas à l'indice global. Aucun ratio n'est calculé.
- **TVA restauration, emplois** : le ratio de 0,49 avantage la mesure, car l'horizon constaté (3 ans) est plus long que celui de l'annonce (2 ans).

## 2. Candidates exclues et raisons

| Candidate | Raison |
|---|---|
| Bascule CSG / cotisations 2018 | Aucun ex post sur le même périmètre. De plus, le coût net 2018 est transitoire (cotisations chômage supprimées en deux temps). |
| Pepa 2019 et PPV 2022 (coût) | L'ex ante vaut 0, donc le ratio n'est pas défini. Aucun coût réalisé officiel n'a été trouvé. Elles sont gardées en effets (aubaine). |
| Heures sup., plafond à 7 500 € (LFR 2022) | Issu d'amendements, sans chiffrage. L'ex post n'est pas séparable de la dépense fiscale 120146. |
| Sous-indexation des pensions 2019 (+0,3 %) | Ex ante lu (2,8 Md€ en 2019 pour les retraites, PLFSS 2019, annexe 9, p. 380), mais aucun ex post trouvé. La comparaison serait possible sur 2019 (les mesures « gilets jaunes » portaient sur la CSG). |
| Suppression de la CVAE 2023-2024 | Étape 2024 étalée jusqu'en 2027 par la LF 2024, donc horizon non réalisé. Pour 2023, la Cour ne publie que des lignes de transfert, pas un coût comparable aux 3,5 Md€ annoncés. |
| Assurance chômage 2019 | Horizon 2019-2021 rompu (Covid, Conseil d'État). La version appliquée est traitée sous `ac_2021`. |
| Assurance chômage 2023 | Ex ante lu (Unédic, 4,5 Md€ en régime de croisière) ; aucun ex post chiffré. Le régime de croisière est attendu en 2027. |
| RSA 2009 | Chiffres seulement de seconde main (FNSA 1,3-1,55 Md€ ; non-recours de 68 %). Ni l'étude d'impact, ni le RAP 2010 du programme 304, ni le rapport du comité national d'évaluation n'ont pu être lus. |
| Remise carburant 2022 | Ex post lu (Cour : 7,6 Md€), mais le dispositif a changé quatre fois et l'ex ante se compose d'enveloppes successives, sans ex post par phase. |
| Chèque bois 2022 | Pas d'ex ante lu, ex post incomplet. |
| Désindexation, CITE effets, MPR effets | Les effets annoncés (2,33 Md€ de travaux, 210 000 primes) n'ont pas de mesure ex post lue. |
| Impôts de production, pacte de responsabilité (effets emploi) | France Stratégie juge l'évaluation causale « pas encore possible » ; le COSAPE 2017 ne produit pas de nouvelle estimation. |
| Limitation à 80 km/h | Exclue d'emblée : pas de coût budgétaire. |

## 3. Points de vigilance

1. **Nature de l'ex post.** Pour `is_25`, `th_20`, `ip_2021`, `pacte_2015` et `cap_2022`, l'ex post est un chiffrage administratif « à comportement constant » mis à jour à l'exécution (mesures nouvelles MEF reprises par la Cour, annexe 5 du PLFSS), pas une évaluation contrefactuelle. Ces lignes biaisent mécaniquement l'échantillon vers « coût conforme ». À traiter comme une catégorie à part, ou à pondérer moins.
2. **`cap_2022`** : l'ex post est la compensation versée à l'audiovisuel public, c'est-à-dire une décision budgétaire. À exclure si l'on exige un ex post observé.
3. **`ac_2021`** : l'ex ante et l'ex post viennent tous deux de l'Unédic, avec le même modèle. La borne haute (1,93) est un choix de lecture lié à la date d'entrée en vigueur (1er décembre 2021).
4. **`bouclier_gaz_2023`** : l'ex post est une estimation CRE non définitive (juillet 2023), citée par la Cour. Ni le PLF 2023 ni la délibération CRE n'ont été lus directement. La fin du bouclier au 30 juin 2023 est elle-même une conséquence de la baisse des prix.
5. **`cir_2008`** : l'ex ante (2,7 Md€) vient du dossier de presse du PLF 2008, cité par la Cour en 2013. Une note DG Trésor d'octobre 2007, citée, prévoyait déjà ≈4,1 Md€ en 2013. On compare des créances, pas des décaissements.
6. **`mpr_2020`** : l'ex post est un montant de paiements de l'année, et les primes sont versées après les travaux. Le −58 % reflète donc surtout un décalage de trésorerie. Ne pas prolonger cette ligne au-delà de 2020 : le périmètre change en 2021.
7. **`pinel_2015`** : la comparaison porte sur un coût générationnel estimé, pas sur un coût annuel réalisé.
8. **`ir_baisse_2020`** : l'ex post vient d'une microsimulation Insee (Ines, France métropolitaine), pas de l'exécution budgétaire.
9. **`tva_resto_2009`** : la comparaison porte sur le coût brut (3,0 contre 3,3). En net, on obtient ≈2,35 ex ante (calculé) contre ≈2,6 ex post.
10. **Colonne `annee`** : harmonisée sur l'année d'adoption ou d'entrée en vigueur, comme dans `data/mesures_cout.csv`. Quand elle diffère de l'année d'évaluation, celle-ci est indiquée dans `note`.
11. **Pas de doublon avec les lignes existantes.**
    - `hs_ir_2019` complète `hs_2019`, qui ne couvrait que le volet social.
    - `th_20` ne compte que les étapes 2022-2023 des 20 % restants, sans recouvrir `th_80`.
    - `bouclier_gaz_2023` est distinct du gel du gaz 2022 mentionné dans la note de `bouclier_elec`.
    - `pacte_2015` exclut le CICE.
12. **Valeurs calculées** : toutes sont signalées comme telles dans `note` ou dans les notes de groupe (sommes de mesures nouvelles annuelles, différences, ratios).

## 4. Accès aux sources (tentatives infructueuses)

- **senat.fr** : inaccessible presque toute la session (erreurs 500, réinitialisations TLS). Aucun rapport du Sénat n'a pu être lu, sauf le rapport Houel sur la TVA restauration.
- **budget.gouv.fr** (403, Incapsula) et **performance-publique** (DNS) : les annexes « Évaluations préalables » des PLF 2015, 2018, 2020, 2021 et 2023, ainsi que plusieurs Voies et moyens, ont été lues à travers les rapports généraux de la commission des finances de l'AN, qui les citent avec leur source. D'où la confiance medium.
- **ccomptes.fr et vie-publique.fr** : accès partiel. Les rapports « Budget de l'État » 2017-2023 de la Cour, le rapport sur les mesures énergie (2024) et le rapport sur les APL (2025) ont été lus. L'audit flash MaPrimeRénov' et le RBDE 2020 détaillé (IR) n'ont pas pu l'être.
- **assemblee-nationale.fr** : erreurs 503 avec curl, contournées par WebFetch. Un PDF de réponse ministérielle (QE 9837) a été récupéré sur un miroir ; c'est le PDF officiel de l'AN.
- **Quota WebSearch** épuisé en cours de tâche pour tous les groupes. Certaines pistes n'ont pas été creusées : CPO 2010 et IPP (Benzarti-Carloni) sur la TVA restauration, IGF/CGEDD sur le Pinel, comité d'évaluation du RSA.

## 5. Contrôles effectués à la fusion

- **Sources** : les 54 fichiers existent et leur sha256 correspond à `sources.csv`. Aucun fichier de `sources/T10a/` n'est hors liste.
- **Citations** : chaque citation a été recherchée dans le texte extrait des archives (pdftotext). La plupart se retrouvent mot pour mot. Les autres sont des lignes de tableau reconstituées, avec annotations entre crochets ; pour celles-ci, les chiffres clés ont été retrouvés dans le bon document : 161 914, 1 879, 5,4 milliards, 10,6 milliards, 5 400, 1 930 et 2 260, 1 530, 600 millions, 15 %.

## 6. Décisions laissées à l'intégrateur

1. Garder ou écarter les lignes `low` (`pinel_2015`, `mpr_2020`, `cap_2022`, `ac_2021`) et les ex post administratifs (point 1 du § 3) dans le calcul de l'erreur médiane. Les deux versions sont données au § 1.
2. Pour les dispositifs d'urgence (chèques, bouclier gaz), décider si l'ex ante (une enveloppe de crédits) doit compter comme un « chiffrage ». Sinon, en faire une sous-catégorie.
3. Harmoniser la formule de l'erreur avec celle du HANDOFF (11,4 % sur les 11 mesures existantes, contre 9,1 % avec la formule ci-dessus).
4. Pour les mesures d'économie (`ac_2021`, `apl_contemp_2021`), un écart positif signifie plus d'économie que prévu. Le signe de l'erreur signée est donc à interpréter selon `sens`.
5. Pistes de reprise prioritaires : RSA 2009 (RAP 2010 du programme 304, rapport final du comité national d'évaluation 2011), sous-indexation des pensions 2019 (CCSS septembre 2019, RALFSS 2020), bascule CSG 2018 (CCSS 2019), évaluations préalables primaires (budget.gouv.fr) pour passer plusieurs lignes en `high`.
