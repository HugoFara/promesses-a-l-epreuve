# T10a — Groupe A : notes

Date d'accès de toutes les sources : 2026-10-14. Sources archivées dans `sources/T10a/A_*` (liste et sha256 dans `sources_A.csv`).

## Accès aux sources
- budget.gouv.fr renvoie 403 et performance-publique.budget.gouv.fr ne répond pas (DNS). Les annexes **Évaluations préalables** et **Voies et moyens tome II** n'ont donc pas pu être lues directement. Elles sont lues **via les rapports généraux de la commission des finances de l'AN**, qui les citent mot pour mot. Pour l'ex ante, cela donne une confiance medium.
- senat.fr a été indisponible une bonne partie de la session (erreurs 500, TLS, ECONNRESET). Le rapport Houel complet a fini par être récupéré. En revanche, les avis du Sénat sur les PLF 2015 et 2018 n'ont pas été lus.
- ccomptes.fr et vie-publique.fr (audit flash MaPrimeRénov' 2021) : pages anti-robot ou adresses introuvables, rien n'a été lu.
- Le quota WebSearch de la session a été épuisé en cours de tâche. Certaines pistes n'ont donc pas pu être poursuivies (voir plus bas).

## 1. TVA restauration 19,6 → 5,5 % (1er juillet 2009) — RETENUE (high)
- **Ex ante (primaire)** : audition de H. Novelli à la commission des finances de l'AN, 10/06/2009 (compte rendu n° 96, p. 4), avant le vote de la loi tourisme du 22/07/2009. Coût brut annuel de 3 Md€, moins 650 M€ d'aides supprimées, soit 2,35 Md€ net (calcul). Le gouvernement en déduit aussi 2 Md€ « en faveur du secteur HCR », hors restauration non-HCR (350 M€).
- **Ex post** : rapport d'information AN n° 337 (Thévenoud, 2012), p. 6. Dépense fiscale brute de 3,3 Md€ en 2010 et en 2011, et coût net « de l'ordre de 2,6 milliards ». Pour comparaison, la synthèse Houel (Sénat, 2010, p. 2) indique : « Le coût net … a été estimé ex ante à 2,4 milliards d'euros ».
- **Périmètre retenu** : perte brute de TVA en année pleine 2010, des deux côtés. Les années 2012 et suivantes (taux de 7 %) sont exclues.
- **Effets retenus** (`effets_A.csv`) :
  - **Emploi** : 40 000 annoncés en 2 ans (dépliant du contrat d'avenir ; Novelli : « dans les 26 mois »), contre ≈19 500 sur 3 ans selon Thévenoud. Ratio 0,49 (calcul). L'horizon ex post étant plus long, le ratio avantage la mesure. Houel : +19 400 dès la 1re année.
  - **Indice des prix** : objectif « baisse de 3 % de l'indice des prix » fixé par le comité de suivi de Bercy (déc. 2009, document gouvernemental postérieur à l'adoption), contre −2,2 à −2,5 % selon Thévenoud. Ratio 0,78 (calcul au milieu de la fourchette).
  - **Montant restitué aux consommateurs** : 1 Md€ annoncé par Novelli (p. 11), contre 590 M€/an selon Thévenoud. Ratio 0,59 (calcul).
  - **11,8 %** : cette baisse porte sur 7 produits sur 10. Elle n'est pas comparable à l'indice global (Houel : baisse maximale théorique de 7,5 %), donc aucun ratio n'est calculé.
- **Non lus** : CPO 2010 (« Entreprises et niches fiscales et sociales »), Insee, DG Trésor, Benzarti-Carloni (IPP). Faute de quota de recherche, ils n'ont pas été cherchés plus loin. Leurs chiffres, vus seulement dans des extraits de recherche (CPO : coût de 3 Md€ ; un débat au Sénat lui attribue 2,4 Md€ et ≈21 700 emplois), ne sont **pas utilisés**.

## 2. CIR, réforme 2008 — RETENUE (medium)
- **Ex ante** : le PLF 2008 n'avait pas d'étude d'impact (pas encore obligatoire) et l'exposé des motifs n'avance aucun chiffre. Le chiffre vient du **dossier de presse du PLF 2008 (p. 2)**, cité par la Cour des comptes (rapport 2013, p. 22, reproduit dans le rapport AN n° 1359) : surcoût de 1,3 Md€ en régime de croisière, soit une dépense totale de 2,7 Md€. Le dossier de presse lui-même n'a pas été lu, d'où medium.
- **Ex post** : Cour des comptes 2013, p. 23. Créance de 4,155 Md€ (2008), 4,7 (2009) et 5,05 Md€ (2010), puis 5,2 Md€ en 2011 (p. 66 du PDF).
- **Périmètre** : coût total du CIR (créance) en régime de croisière. Pour 2,7 ex ante, on retient 5,05 en valeur centrale (fourchette 4,7-5,2), soit un ratio de ≈1,9.
- **Vigilance** : 2,7 Md€ est le chiffre du dossier de presse. Le MINEFI, cité par le rapporteur général du Sénat, donnait 2,823 Md€ pour 2012. La DG Trésor (note du 29/10/2007) prévoyait ≈4,1 Md€ en 2013 : l'administration disposait donc déjà d'un chiffrage plus réaliste. La LFI 2011 a durci le dispositif, d'où le choix de 2010 comme année centrale. Ne pas confondre la créance avec la dépense budgétaire (décalages de remboursement, plan de relance 2009 : 6,2 Md€ selon le Sénat, non lu).

## 3. CITE (LFI 2015) — RETENUE (medium)
- **Ex ante** : l'évaluation préalable de l'article 3 du PLF 2015 chiffrait la dépense fiscale 2016 à ≈1,4 Md€. Ce chiffre est cité par le rapporteur général de l'AN pour le PLF 2018 (rapport n° 273, tome II, p. 236). Recoupement : le rapport Rabault sur le PLF 2015 (n° 2260, t. II vol. 1, p. 88) cite la même évaluation préalable, soit +701 M€ en 2016 pour un CIDD à ≈620 M€, ce qui donne ≈1,32 Md€ (calcul).
- **Ex post** : « près de 1,7 milliard d'euros » (même page). L'amendement AN I-300 du PLF 2017 indique que l'impact 2016 a été « revu à la hausse … de 1,4 à 1,7 milliard d'euros ». Le chiffre de 1 678 M€ (Voies et moyens PLF 2018) n'a été vu que dans un extrait de recherche : il n'est pas utilisé.
- **Cause** : volume de travaux et recours plus élevés que prévu (classé « Élasticité comportementale »). Une QE AN de 2017 indique que les parois vitrées représentaient à elles seules près de 900 M€ en 2016.
- **Effet annoncé** non retenu : 2,33 Md€ de travaux par an, sans mesure ex post trouvée.

## 4. Pinel (LFI 2015) — RETENUE, confiance low
- Le coût marginal de la réforme Duflot → Pinel (7 M€ en 2016, 33 M€ en 2017, selon l'évaluation préalable) n'a pas d'équivalent ex post : ce périmètre est exclu.
- **Périmètre retenu** : coût générationnel de la génération 2015.
  - Ex ante : 1,7 Md€ (évaluation préalable PLF 2015, via Rabault p. 131).
  - Ex post : 1,563 Md€ (« constaté pour l'année 2015 … estimé », évaluation préalable de l'art. 39 du PLF 2018, via le rapport n° 273 t. III p. 71).
  - Ratio 0,92.
- **Pourquoi low** : l'ex post reste une estimation administrative (la génération s'impute jusqu'à ~2027), et aucune des deux évaluations préalables n'a été lue directement.
- **Effet** : 50 000 logements annoncés pour 2015, contre 50 000 « évalués ». Jugé conforme, sans preuve de causalité.
- **Non trouvé** (quota de recherche épuisé) : évaluation IGF/CGEDD, Cour des comptes (2018-2019) et France Stratégie sur l'investissement locatif.

## 5. MaPrimeRénov' (2020) — RETENUE, confiance low
- **Ex ante** : PLF 2020, 390 M€ sur le P174 pour 210 000 primes et 170 000 ménages en 2020 (rapport général AN n° 2301 t. II p. 157, renvoyant aux évaluations préalables p. 42).
- **Ex post** : charges MaPrimeRénov' de l'ANAH en 2020, soit 161,9 M€ (rapport général AN n° 4524 t. II p. 438, source : rapport annuel ANAH 2020). En borne haute, on prend la dotation P174 versée à l'ANAH, soit 455 M€. Ce montant ne sert pas qu'à MPR.
- **Vigilance** : il s'agit de **paiements**, et les primes sont versées après les travaux. Les montants engagés et le nombre de dossiers 2020 (≈140 000-150 000 engagés selon des extraits de presse et de QE non lus) ne sont pas retenus. Les 575 M€ de crédits ouverts en 2020 (tableau du Sénat, non lu) non plus. L'ouverture à tous les ménages par le plan de relance (fin 2020 / 2021) sort du périmètre ex ante. Le chiffre utilisable pour 2020 correspond au coût en caisse de l'année. Pour les années suivantes, le périmètre change complètement (programmes 362 et 135) : il ne faut pas étendre cette ligne.
- **Effet** (210 000 primes) : ex post non trouvé sur une source lue, rien n'est retenu.

## Valeurs calculées (marquées comme calculées dans les CSV)
- TVA, coût net ex ante : 3,0 − 0,65 = 2,35 Md€. Ratios des effets : 19 512 / 40 000 = 0,49 ; 2,35 / 3 = 0,78 ; 0,59 / 1,0 = 0,59.
- CITE, recoupement : 0,62 + 0,701 ≈ 1,32 Md€.
