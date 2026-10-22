# T24 : lignes 2024 dont le montant porte sur une disposition absente du droit de juin 2024

Consigne préparée le 22/10/2026 (issue #9). Lire d'abord `recherche/CONSIGNES.md` (règles communes ; date d'accès : celle du jour), puis `recherche/T1/convention_application_2024.md` (référence des programmes 2024) et `recherche/T23/rapport.md` § 6, point 5.

## Pourquoi

Les programmes 2024 sont comptés par rapport au droit de juin 2024, celui des chiffreurs (`convention_application_2024.md`). Un chiffrage qui mesure l'abrogation, la modification ou le maintien d'une disposition suppose que cette disposition était en vigueur, ou inscrite dans la trajectoire de référence (programme de stabilité d'avril 2024), à cette date.

Cas qui a déclenché la tâche : `nfp_asile` (NFP 2024, « Abroger la loi asile et immigration », −1,3 Md€, Institut Montaigne). Le montant est calculé sur l'article 19 de la loi du 26/01/2024 (condition de 5 ans de résidence ou 30 mois d'activité pour les prestations familiales et les APL), censuré par la décision 2023-863 DC du 25/01/2024, avant la promulgation. En juin 2024, la mesure que la ligne propose d'abroger n'existait pas.

Ce n'est pas un risque juridique (T23) : c'est une question de référence. Le résultat peut toucher n'importe quel programme ; il est publié pareil.

## 0. Gel

| Élément | Valeur |
|---|---|
| Commit | `2c0948c` |
| `data/raw/application_lignes.csv` (sha256) | `efc51b918547af7e9e9dc3c31e88023e0a31f30108db7923c4b3e509e38e6e41` |
| `data/raw/chiffrages_instituts.csv` (sha256) | `62c8bc03008bb70c273a1044f9708cc06c8772a75333f815abcc616a861af561` |
| `data/raw/statut_reference_2027.csv` (sha256) | `060e8afaa08369e855a16380e4d6a04c753a2928013795a13dc63e7fb01da1f6` |

## 1. Critère (fixé avant la recherche)

Une ligne est **concernée** si le montant retenu (`independant`, ou la part chiffrée d'une ligne groupée) repose, d'après le texte du chiffreur, sur une disposition qui, **au 30/06/2024** :

- **R1, censurée** : déclarée contraire à la Constitution (DC, QPC, RIP) ou au droit de l'Union, avant d'entrer en vigueur ou depuis ;
- **R2, abrogée ou expirée** : abrogée, arrivée à son terme (mesure temporaire), ou remplacée ;
- **R3, pas encore adoptée** : seulement annoncée, en projet ou en débat, **et absente** de la trajectoire du programme de stabilité d'avril 2024.

À l'inverse, une disposition votée mais pas encore entrée en vigueur, ou inscrite dans la trajectoire du programme de stabilité, **fait partie** de la référence (cas de `ens_chomage`) : la ligne n'est pas concernée, mais on le note.

Ce qui compte, c'est la disposition **sur laquelle porte le calcul du chiffreur**, pas l'intitulé de la ligne : une ligne « Abroger la loi X » dont le calcul porte sur un article en vigueur n'est pas concernée, même si d'autres articles de X ont été censurés.

Hors champ : l'opportunité de la mesure, son risque juridique futur (T23), un écart de chiffrage sans lien avec le droit en vigueur.

## 2. Ce que l'on cherche

### A. `nfp_asile` (intégrateur)

1. Sur quelle disposition porte le 1,3 Md€ (micro-chiffrages Montaigne, p. 5 ; fiche mesure ; synthèse).
2. Statut de cette disposition au 30/06/2024 (décision 2023-863 DC, loi n° 2024-42 promulguée).
3. Ce que chiffrent les autres chiffreurs (iFRAP, Asterès : dans le résidu, sans montant propre) et s'il existe un chiffrage des articles de la loi de 2024 effectivement en vigueur.
4. Proposition de traitement selon la convention de référence 2024, avec sa justification.

### B. Toutes les autres lignes 2024 (agent)

Passer en revue **toutes** les lignes de `data/raw/application_lignes.csv` sauf `nfp_asile` (programmes NFP 2024, Ensemble 2024, RN 2024), y compris les lignes de résidu (`*_reste`, `*_ecart`) et de charge d'intérêts (`*_taux`), pour lesquelles une phrase suffit.

Pour chaque ligne :

1. Lire le texte du chiffreur cité (`url`, `source_independant` ; détail dans `data/raw/chiffrages_instituts.csv` ; copies déjà archivées dans `sources/T6/`, `sources/T17/`, `sources/T20/`, `sources/T22/`, `sources/T23/`, listées dans les `sources.csv` de ces tâches).
2. Dire sur quelle disposition existante le calcul repose, s'il y en a une (une mesure entièrement nouvelle n'en a pas : `critere = aucun`, motif « mesure nouvelle »).
3. Si elle en a une, établir sur source primaire son état au 30/06/2024 : texte en vigueur (Légifrance, version à date), décision de censure, date d'expiration, ou présence dans la trajectoire du programme de stabilité d'avril 2024.

Lignes à examiner avec attention (sans préjuger du résultat) : celles qui abrogent, annulent, prolongent, rehaussent, « maintiennent » ou remplacent un dispositif, par exemple `nfp_retraites`, `rn24_retraites` (loi n° 2023-270 et décision 2023-849 DC), `rn24_chomage` (réforme de l'assurance chômage de juillet 2024 : était-elle prise par décret au 30/06/2024, et est-elle dans la trajectoire du programme de stabilité, comme pour `ens_chomage` ?), `rn24_rente_infra` (contribution sur les rentes inframarginales : en vigueur en 2024 ?), `ens_elec` (taux de l'accise sur l'électricité en juin 2024 et trajectoire prévue), `nfp_taxe_macron`, `nfp_logement_social`, `rn24_production`, `rn24_iff`, `rn24_armateurs`, `rn24_donations`, `nfp_flat`, `nfp_ttf`.

Ne pas compléter un état du droit de mémoire : chaque statut se lit sur une source datée.

## 3. Livrables (dans `recherche/T24/`)

- `lignes_2024.csv`, une ligne par id de `application_lignes.csv` (89 lignes, `nfp_asile` compris, remplie par l'intégrateur) : `id`, `programme`, `ligne`, `independant`, `disposition` (texte, article, ou « mesure nouvelle »), `etat_30_06_2024` (`en vigueur`, `votée, pas encore en vigueur`, `dans la trajectoire du PStab`, `censurée`, `abrogée ou expirée`, `pas encore adoptée`, `sans objet`), `critere` (`R1`, `R2`, `R3` ou `aucun`), `part_concernee_md` (part du montant qui porte sur la disposition absente, si `critere` ≠ `aucun`), `url`, `citation`, `page`, `confiance`, `note`.
- `rapport.md` : méthode, lignes concernées, cas limites, ce qui n'a pas été trouvé, décisions laissées à l'intégrateur.
- `sources.csv` (`fichier,url,titre,date_acces,sha256`) ; sources archivées dans `sources/T24/`.

Ne modifier ni `data/`, ni `scripts/`, ni `web/`. Les changements de données sont décidés ensuite par l'intégrateur, après validation par l'utilisateur, et passent par `scripts/appliquer_corrections.py`.
