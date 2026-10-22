# T25 : dépenses et recettes des programmes 2024 déjà comprises dans la référence

Consigne préparée le 22/10/2026 (issue #10). Lire d'abord `recherche/CONSIGNES.md` (règles communes ; date d'accès : celle du jour), `recherche/T1/convention_application_2024.md` (référence des programmes 2024) et `recherche/T24/rapport.md` (§ 3 et 4).

## Pourquoi

Les programmes 2024 sont comptés par rapport au droit de juin 2024 et à la trajectoire du programme de stabilité d'avril 2024 (PStab). Une mesure déjà financée par cette référence ne doit être comptée que pour la part qui n'y est pas (`CONTRIBUTING.md`, règle 4). T24 a vérifié les dispositions censurées, abrogées ou non adoptées ; il reste le cas inverse : un programme qui promet, et dont le chiffreur chiffre, une dépense **déjà programmée ou budgétée**.

Cas qui a déclenché la tâche : `rn24_prisons` (−1,5 Md€/an, Montaigne). Le montant est le coût d'environ 12 000 places « restant à livrer » du plan 15 000 (micro-chiffrages RN, p. 3), alors que la loi n° 2023-1059 d'orientation et de programmation du ministère de la Justice 2023-2027 programme les crédits de la mission Justice jusqu'en 2027 et prévoit de « finaliser » ce plan (rapport annexé, § 2.3.1.2 ; texte adopté : `sources/T24/integration/senat_tas23-003_lopj.html`).

Le résultat peut toucher n'importe quel programme, ou aucun ; il est publié pareil.

## 0. Gel

| Élément | Valeur |
|---|---|
| Commit | `0a905e8` |
| `data/raw/application_lignes.csv` (sha256) | `2a30da02d5cf55b9fe82d004fcb0ed749269462633a155ba311bd5b181df9a5a` |
| `data/raw/chiffrages_instituts.csv` (sha256) | `4f71ea4165be16b0bf6b31401e440acc50ea8a7aba1143c1c8fc6a67f08b2f03` |

## 1. Critère (fixé avant la recherche)

Une ligne est **comprise dans la référence**, en tout ou en partie, si le montant retenu (`independant`) chiffre une dépense ou une recette qui, au 30/06/2024, était :

- **P1, programmée** : inscrite dans une loi de programmation en vigueur (Justice 2023-2027, militaire 2024-2030, recherche 2021-2030, intérieur 2023-2027…), avec des crédits ou une cible chiffrée ;
- **P2, budgétée** : inscrite en loi de finances ou de financement de la sécurité sociale pour 2024, ou dans le projet annuel de performances (PAP) d'un programme pour 2024 et les années suivantes ;
- **P3, dans la trajectoire** : chiffrée dans le PStab d'avril 2024 (mesure annoncée comprise, comme les « Mesures fiscales énergéticiens et autres mesures sur les rentes 3,0 » du tableau 7, p. 41).

Ce qui compte, c'est **ce que le chiffreur chiffre**, d'après son texte : le coût total d'un plan déjà financé (compris), ou seulement l'accélération, l'extension ou le surcroît par rapport au plan (non compris pour cette part). Un chiffreur qui mesure explicitement un « écart au programme de stabilité » (iFRAP) chiffre par construction ce qui s'ajoute à la référence : le noter.

Une programmation n'est pas une garantie de dépense : noter, quand une source le dit, les écarts entre crédits programmés et crédits votés ou exécutés (annulations de février 2024 notamment). La part comprise dans la référence se mesure d'après ce que la référence contenait au 30/06/2024 (crédits de la loi de programmation, LFI 2024, PStab), pas d'après l'exécution ultérieure.

Hors champ : les dispositions censurées, abrogées ou non adoptées (T24) ; l'opportunité des mesures ; leur risque juridique (T23).

## 2. Ce que l'on cherche

### A. `rn24_prisons` (agent A)

1. Le calcul de Montaigne (micro-chiffrages RN p. 3, `sources/T17/montaigne_rn_micro_chiffrages.pdf` ; synthèse) : places, coût unitaire, étalement.
2. Le financement du plan 15 000 dans la référence : loi n° 2023-1059 (art. 1er, rapport annexé) ; PAP 2024 du programme 107 « Administration pénitentiaire » (crédits immobiliers, autorisations d'engagement et crédits de paiement 2024 et suivants, coût total et restant à payer du plan) ; rapports de l'APIJ, du Sénat (rapport d'information n° 37, 2023-2024, cité par Montaigne), de la Cour des comptes ; effet des annulations de crédits de février 2024 sur ce programme.
3. Part du montant de la ligne déjà financée par la référence, avec sa fourchette si les sources ne permettent pas de trancher.

### B. `rn24_rente_infra` (agent A)

1. Ce que recouvre la promesse du RN (« hausse de la taxe sur les énergéticiens », 3 Md€) et l'annonce du Gouvernement chiffrée dans le PStab (« Mesures fiscales énergéticiens et autres mesures sur les rentes 3,0 ») : textes, dates, mécanisme.
2. Ce que chiffre l'iFRAP (« écart au programme de stabilité ») : sa méthode, si elle est publiée.
3. Conclusion : même mesure, mesure qui s'ajoute, ou non établi. La ligne est en règle « Recette ponctuelle » (facteur 0) : sans effet sur le solde, la conclusion sert à la fiche.

### C. Toutes les autres lignes 2024 (agent B)

Passer en revue **toutes** les lignes de `data/raw/application_lignes.csv` sauf `rn24_prisons` et `rn24_rente_infra` (NFP 2024, Ensemble 2024, RN 2024), y compris les résidus (`*_reste`, en lisant le détail des postes chez le chiffreur) ; une phrase suffit pour les mesures manifestement nouvelles (baisse d'impôt, prestation créée, hausse de barème). Lignes à examiner avec attention, sans préjuger du résultat : dépenses d'équipement, de recrutement ou de revalorisation qui peuvent recouper une loi de programmation ou un plan budgété (`nfp_enseignants`, `rn24_enseignants`, `ens_agents_publics`, `nfp_point_indice`, `nfp_logements_publics`, `nfp_petite_enfance`, `ens_snu`, `ens_leasing`, `nfp_soin_medicosocial`, `rn24_apprentissage`, `ens_fraude`, `rn24_fraude`, `ens_autres_dep_reste` — l'iFRAP y dit certaines mesures « déjà inscrites au budget » —, `rn24_autres_dep_reste`, `nfp_autres_dep_reste`).

## 3. Livrables (dans `recherche/T25/`)

- Agent A : `parts/prisons_rente.md` (raisonnement, citations, part comprise), `parts/sources_A.csv`, sources dans `sources/T25/A/`.
- Agent B : `parts/lignes_B.csv` : `id`, `programme`, `ligne`, `independant`, `ce_que_chiffre_le_chiffreur`, `texte_reference` (loi, PAP, PStab, ou « aucun »), `critere` (`P1`, `P2`, `P3` ou `aucun`), `part_comprise_md` (et `part_comprise_bas`, `part_comprise_haut` si incertaine), `url`, `citation`, `page`, `confiance`, `note` ; `parts/notes_B.md` ; `parts/sources_B.csv` ; sources dans `sources/T25/B/`.
- Intégrateur : `lignes_2024.csv` (89 lignes), `rapport.md`, `sources.csv`, et, après validation par l'utilisateur, `corrections.csv`.

Ne modifier ni `data/`, ni `scripts/`, ni `web/`. Aucun commit.
