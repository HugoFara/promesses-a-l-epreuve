# T4p – partie B (patrimoine, successions) : notes

Date d'accès : 2026-10-14. Valeurs dans `B_patrimoine_succ.csv`, sources dans `B_sources.csv` (fichiers archivés sous `sources/T4p/B_*`).

## Trouvé

- **Barème ISF 2017** (BOFiP BOI-PAT-ISF-40-10, version en vigueur 2013-2018) : 0 / 0,5 / 0,7 / 1 / 1,25 / 1,5 %, seuils 0,8 / 1,3 / 2,57 / 5 / 10 M€ ; seuil d'assujettissement 1,3 M€ ; décote entre 1,3 et 1,4 M€.
- **Rendement ISF 2017** : 4,2 Md€ (France Stratégie, rapport final 2023). DGFiP via fgeerolf : 4,226 Md€ nets, 358 198 foyers, patrimoine net taxable 1 028,8 Md€, donc un **taux moyen effectif de 0,41 %** (calculé par moi). France Stratégie : 0,45 % pour le top 0,1 %, 0,71 % pour le top 1 %, 0,51 % pour le top 10 % (2017).
- **NFP 2024** : le programme dit « ISF renforcé avec un volet climatique », **sans barème**. Le document macro du NFP chiffre la mesure à 15 Md€ et l'« impôt sur les successions dorées » (héritage maximal de 12 M€) à 17 Md€.
- **LFI, PLF 2026** : amendement I-2360 (« de repli », sans composante climatique), rejeté. Seuil 1,3 M€ ; taux 0 / 0,5 / 0,7 / 1 / 1,5 / 2 / 3 / 4 / 5 % ; seuils 0,8 / 1,3 / 2 / 3 / 5 / 10 / 100 / 1 000 M€. Recettes annoncées : 10 Md€.
- **Taxe Zucman** (PPL n° 768) : 2 % au-delà de 100 M€, impôt plancher (les impôts directs déjà payés sont déduits). Estimation de Zucman : 20 Md€ [15-25], sur une assiette de 1 228 Md€ (les 500 plus grandes fortunes selon Challenges 2024, rapport Sénat n° 689 p. 41). Si l'IS est imputé : 2-3 Md€ (A. Levy, rapport Sénat). Le Sénat note aussi que le départ des trois plus grandes fortunes réduirait le rendement de moitié (-10 Md€).
- **Exil fiscal, CAE Focus 118** (communiqué) : +1 pt de taux effectif → +0,02 à 0,23 % d'expatriations à long terme. Dans le contexte scandinave, la marge intensive pèse environ 2,5 fois la marge extensive.
- **DMTG en ligne directe en 2026** : 5 / 10 / 15 / 20 / 30 / 40 / 45 %, seuils 8 072 / 12 109 / 15 932 / 552 324 / 902 838 / 1 805 677 € ; abattement de 100 000 €.
- **Taux moyen effectif DMTG** : 5 % de l'ensemble des transmissions en 2015 ; 2-3 % en ligne directe ; environ 25 % sans enfant (France Stratégie 2017). CAE n° 69 : à peine 10 % pour le top 0,1 %.
- **Recettes DMTG** : 15 Md€ (CAE 2021, « système actuel ») ; 12,5 Md€ en 2015 (France Stratégie) ; flux transmis > 300 Md€.

## Non trouvé / tentatives

- **Légifrance** (art. 777, 885 U, LF 2026) : bloqué par Cloudflare, en curl comme en WebFetch. J'ai utilisé à la place BOFiP et service-public.
- **LF 2026 (loi n° 2026-103 du 19/02/2026)** et art. 777 : la fiche service-public a été vérifiée le 09/02/2026, donc avant la promulgation. L'absence de modification de l'art. 777 n'est confirmée que par une source secondaire (Legare). **À vérifier sur Légifrance.** Legare signale un nouvel art. 788 III bis (beaux-enfants : abattement de 15 932 €, taux de 60 %).
- **Chiffrage officiel de la taxe Zucman** (DGFiP, Trésor, CAE, rapport général PLF 2026) : non trouvé. Le quota de recherches web de la session a été épuisé en cours de tâche.
- **Recettes DMTG 2024-2026** (Voies et moyens) : non trouvées, pour la même raison.
- **PDF du CAE Focus 118** : URL introuvable. Seul le communiqué a été lu.
- **Barème « climatique » LFI** (amendement principal) : non trouvé. Les votes datan.fr évoquent l'amendement 2360 « avec composante climatique », mais son texte se dit « de repli » et ne contient pas de composante climatique.

## Vigilance

- Rendement de l'ISF : 4,2 Md€ (2017) ne vaut pas 5 Md€. Le contrefactuel 2022 de France Stratégie est de 6,3 Md€ (perte de 4,5 Md€).
- Les chiffrages NFP, LFI et Zucman sont ceux des auteurs : statiques, sans réaction comportementale.
- Taxe Zucman : le seuil de 100 M€ concerne environ 4 000 foyers selon la PPL, mais 1 600 à 1 800 selon Zucman au Sénat. L'assiette de 1 228 Md€ couvre les 500 plus grandes fortunes, pas l'ensemble des patrimoines au-delà de 100 M€.
- Plusieurs PDF ont été récupérés via web.archive.org (sites d'origine en 404, 403 ou refus TLS). L'URL d'archive est indiquée dans `B_sources.csv`.
- Les données ISF de fgeerolf sont une reproduction secondaire de fichiers DGFiP (confiance medium).
