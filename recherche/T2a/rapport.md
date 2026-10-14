# T2a : sources primaires manquantes (couche 1, application 2024, paniers)

Date d'accès de toutes les sources : 14 octobre 2026. Les fichiers lus sont archivés dans `sources/T2a/` et listés, avec leur empreinte sha256, dans `sources.csv`.

## Fichiers produits

- `corrections.csv` : 50 lignes. Chaque ligne confirme une valeur (même valeur, confiance relevée) ou la corrige. Les corrections sont marquées « PROPOSITION » dans `note`.
- `nouveaux_rendements.csv` : 9 rendements (CSG, TVA restauration, TTF, taxe carbone, rachats d'actions).
- `ifrap_nfp_2024.csv` : transcription complète du tableau iFRAP NFP (image du 27 juin 2024). Contrôle : les sommes recalculées (215,3 et 55,0) égalent les totaux affichés.
- `sources.csv` : 28 fichiers archivés.

## Couche 1 : ce qui a été trouvé

| Ligne | Avant | Après | Source primaire lue |
|---|---|---|---|
| isf_ifi | 3,2 / 2,9 / 3,1, high | inchangé, confirmé | PLF 2018, exposé général p. 17 (−3,2) ; France Stratégie (FS) 2019 p. 13 et FS 2020 p. 138 |
| pfu | 1,9 / 0–0,85–1,7, high | inchangé, confirmé | FS 2019 p. 13 (ex ante 1,9) ; FS 2020 p. 15 (1,4–1,7 hors comportement, −0,5 selon l'Insee, « jusqu'à l'annuler ») ; Sénat r19-042 |
| cice | ex post central 20 | **18,5 (proposition)** | FS synthèse CICE 2020, tableau 1 p. 9 : créances de 18,2 à 18,5 Md€ en 2014-2016 au taux de 6 % ; 22,2 en 2017 au taux de 7 % |
| th_80 | 10 / 10,2, medium | inchangé, **high** | Sénat, rapport général PLF 2018 (« 10 milliards ») et PLF 2018 p. 17 (−3,0 pour la première tranche de 30 %) ; Sénat, rapport général PLF 2022 (10,2) |
| hs_2019 | 2 / 1,7, low | **1,94** / 1,7, high | Étude d'impact PLFSS 2019 p. 14 (1,94 Md€ en année pleine) ; annexe 4 du PLFSS 2023 p. 26 (1,7 Md€ réalisés en 2019, non compensés) |
| pa_2016 | 3,95 / 4,4, medium | 3,95 / **4,1 (proposition)**, high | Sénat, compte rendu du 30/11/2015 (3,95) ; Sénat, rapport n° 728 (2026), qui reprend l'enquête de la Cour des comptes, p. 90 (4,1 Md€ exécutés en 2016) |
| pa_2019 | 9,6 | confirmé | Sénat, rapport n° 728, p. 33 |
| woerth_2010 | 20,2 / 18,4, low | 20,2 / **18,8 (dérivé)**, high | Étude d'impact 2010, tableau § 3.4.6 (20,2 Md€ de 2008 en 2020) ; DREES ER 985 (0,8 pt de PIB × 23,5 Md€) |
| retraites_2023 | 13,7 / 10, medium | **13,5 (proposition)** / 10, high | « Rapport sur les objectifs et les effets du projet de réforme », janvier 2023, p. 94-96 (11,8 + 1,7) ; Cour des comptes, février 2025, p. 65-67 |
| Effets | | | CICE ≈100 000 emplois (FS 2020 p. 6) et 160 000 avec bouclage macroéconomique (p. 7) ; retraites 2023 : +6 points de taux d'emploi des 60-64 ans annoncés pour 2030 (étude d'impact PLFRSS, p. 36) |

## Couche 1 : ce qui n'a pas été trouvé (et tentatives)

- **Évaluations préalables du PLF 2018 (annexe)** : non lues. budget.gouv.fr bloque l'accès (Incapsula, 403 y compris via WebFetch) ; sur le site de l'AN, `l15b0235_etude-impact` renvoie 404 et `_evaluation-prealable` 503 ; le Sénat (`leg/etudes-impact/pjl17-107`) renvoyait 500. Les chiffres sont toutefois confirmés par trois documents primaires concordants : l'exposé général du PLF, la communication Éblé (Sénat, 26 octobre 2017) et FS 2019, qui cite l'évaluation préalable.
- **Dossier de presse retraites (10 janvier 2023)** : travail-emploi.gouv.fr rejette la requête ; Wayback non disponible. Il est remplacé par le rapport gouvernemental de janvier 2023, plus complet.
- **Heures supplémentaires 2019** : le coût IR après coup (1,9 Md€ en 2019) n'est sourcé que par l'Institut Montaigne (source secondaire) ; le tome II des Voies et moyens du PLF 2021 est hébergé sur budget.gouv.fr (bloqué). Aucune évaluation de l'effet sur les heures travaillées n'a été trouvée. Le quota de recherche web de la session a été épuisé avant qu'une recherche ciblée (Dares, Insee, IPP) aboutisse.
- **Cour des comptes, CICE** : aucun rapport propre n'a été lu. Le coût est désormais sourcé par FS (créances DGFiP), qui suffit.
- **France Stratégie 2023 (4e rapport, « ≈0 » pour le PFU)** : l'ancienne URL renvoie 404 et la nouvelle page n'a pas été trouvée. FS 2020 contient déjà la formule « jusqu'à l'annuler ».
- **Annonce CICE de 300 000 à 400 000 emplois** et **ex ante CICE de 20 Md€** : toujours sourcés par maire-info. Le dossier du Pacte de compétitivité n'a pas été lu.

## Application et paniers

- **Note NFP du 21 juin 2024** (« Notre proposition macroéconomique ») : trouvée via l'archive de la page LFI. Le PDF est sur lafranceinsoumise.fr. Tous les montants du parti utilisés dans `application_lignes.csv` sont confirmés à l'identique : superprofits 15, ISF 15, niches 25, successions 17, IR et CSG 5,5, flat tax 2,7, Zucman 26, égalité salariale 10, TTF 3, plus 30 Md€ pour la bifurcation écologique (panier `l_eco`). La note n'a ni tableau ligne par ligne, ni méthode, ni coût chiffré du retour à 60 ans.
- **Chiffrage de L'Avenir en commun 2022** : **non trouvé**. melenchon2022.fr redirige vers melenchon2027.fr. Dans l'index Wayback, le domaine ne compte qu'une page de 2022 contenant « chiffrage », l'annonce de l'émission vidéo du 12 mars 2022, sans PDF. Les 90 PDF archivés du domaine (livrets et plans) ont été listés : aucun n'est un chiffrage (le « Plan justice fiscale » a été vérifié). Le chiffrage semble n'avoir existé qu'en vidéo ou sous une forme non archivée.
- **Tableau iFRAP** : lu directement dans l'image PNG (navigateur Chrome indisponible : extension non connectée après 3 essais). Il est transcrit en entier. Points saillants : l'iFRAP **ne chiffre pas** l'impôt sur les multinationales (aucune ligne). Le « 0 » de `nfp_zucman` est donc une absence, et la médiane de 8 ne repose que sur Terra Nova. L'iFRAP **reprend tels quels** les 10 Md€ de l'égalité salariale (`nfp_egalite`). Il chiffre l'ISF à 15,2. Il compte deux lignes « niches » de 5 Md€ chacune.
- **Taxe sur les rachats d'actions (8,4)** : l'amendement I-105 a été lu (8,415 Md€, soit 33 % × 25,5 Md€ de rachats, calcul de l'auteur, sans effet de comportement). Aucune évaluation officielle de cette version n'a été trouvée. Repère officiel : la taxe de 8 % sur le nominal (LFI 2025) a rapporté **0,5 Md€ en 2025** (Cour des comptes, NEB 2025, p. 22). La confiance est abaissée à `low`.
- **Bozio-Wasmer** : 12,1 Md€ et −61 000 ETP confirmés (synthèse, p. 30). Le chapitre 4 (p. 202) précise : 12,2 Md€ ex ante, 11,4 Md€ après effets sur l'emploi, −61 870 ETP. **Le libellé du panier est inexact** : le scénario supprime les bandeaux maladie et famille et éteint les allègements à 1,88 SMIC (sans recyclage). Ce n'est pas une suppression « au-dessus de 1,6 SMIC ».

## Nouveaux rendements

| Levier | Rendement | Source |
|---|---|---|
| 1 point de CSG (toutes assiettes) | 17,77 Md€ (2026 p) ; activité 11,71, remplacement 4,02, capital 1,94 | CCSS mai 2026, tableau 6, p. 54 |
| TVA restauration 10 % → 20 % | 2,12 Md€ (2025 p ; 2,0 réalisé en 2023), statique | Voies et moyens tome II PLF 2025, p. 167 |
| TTF (relèvement LFI 2025) | 0,5 Md€ en 2025 (≈0,7 en année pleine, dérivé) | Cour des comptes, NEB 2025, p. 9 et 22 |
| Taxe carbone +10 €/t | ≈1,8 Md€ (dérivé : 8,0 Md€ / 44,6 €/t ; base 2019, hors TVA) | CPO 2019, p. 88 |

## Points de vigilance

1. **Base de prix incohérente dans le backtest.** Retraites 2023 : ex ante en euros courants de 2030 (13,5), ex post de la Cour en euros constants de 2024 (9,7 pour la DG Trésor). Woerth : ex ante en euros de 2008, ex post DREES en euros de 2016. Une partie des écarts « −27 % » et « −9 % » est un artefact de prix.
2. **Retraites 2023, borne basse 7,1** : ce chiffre porte sur le seul régime général, en 2032. Il n'est pas comparable à l'ex ante.
3. **Retraites 2023, nature de l'ex post** : le « 10 Md€ » de la Cour reprend des réestimations (DG Trésor, Rexecode), pas un réalisé. Attribuer l'écart aux « concessions parlementaires » n'est pas démontré par la source.
4. **CICE et prime d'activité 2016** : les primaires conduisent à des écarts différents de ceux du jeu actuel (CICE −7,5 % au lieu de 0 ; PA 2016 +3,8 % au lieu de +11 %). Cela modifie la médiane d'erreur de la couche 1 (11,4 %) : à recalculer.
5. Deux documents officiels n'ont été lus que sur des copies hébergées par des tiers : le rapport gouvernemental retraites 2023 (Landot avocats) et le tome II des Voies et moyens 2025 (Public Sénat). Le PDF DREES a été obtenu via WebFetch, curl étant rejeté.
6. Le Sénat était inaccessible (erreurs 500, puis échec de connexion) en début de session, puis accessible : toutes les pages du Sénat citées ont été effectivement lues.

## Décisions laissées à l'intégrateur

- Adopter ou non les propositions : CICE 18,5 ; PA 2016 4,1 ; retraites 2023 13,5 (et la borne basse) ; Woerth 18,8 ; hs_2019 1,94.
- Harmoniser la base de prix des couples ex ante / ex post (retraites 2010 et 2023) avant de calculer les écarts.
- `nfp_zucman` : garder une « médiane » à une seule source, ou documenter l'absence de l'iFRAP.
- `nfp_niches` (iFRAP) : compter 5 ou 10.
- Paniers, rachats d'actions : remplacer 8,4 (auteur, statique) par une valeur ancrée sur le réalisé de 0,5 Md€ ajusté au nouveau barème, ou garder 8,4 en `low` avec le facteur 0,45.
- Paniers, bandeaux : corriger le libellé ; utiliser 11,4 (après effets sur l'emploi) plutôt que 12,1 ; la base est antérieure à la réforme 2025-2026 (voir T1).
