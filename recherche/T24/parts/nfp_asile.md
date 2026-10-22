# T24 A : `nfp_asile` (intégrateur, 22/10/2026)

## 1. Sur quoi porte le 1,3 Md€

Une seule source donne un montant : l'Institut Montaigne.

- **Micro-chiffrages NFP, PDF p. 5** (`sources/T20/integration/nfp_microchiffrages.pdf`, web.archive.org 20241219114355, sha256 `a9cdbaf8…`), encadré « Abroger la loi asile et immigration », « 1,3 Md€ » : « La loi réduit l'attribution d'allocations familiales pour les immigrés récemment arrivés (5 ans de résidence ou 30 mois d'activité professionnelle pour toucher les prestations familiales ou d'autres allocations) ». Le calcul part d'un chiffrage de la campagne présidentielle de 2022 (« 2,3 Md€ sur la base d'un délai uniforme pour tous de 5 ans »), corrigé pour l'option des 30 mois d'activité, puis traite à part les APL (« le gain obtenu d'étalement sur 5 ans est évalué à 0,77 Md€ », avec l'accès après 3 mois de travail). Le montant entier porte donc sur **une seule disposition** : la condition de 5 ans de résidence ou 30 mois d'activité pour les prestations familiales, les APL et les autres allocations visées.
- **Synthèse NFP** (`sources/T6/montaigne_nfp_synthese_wb20240708.html`), tableau « Dépenses », « Autres mesures » : « Abroger loi asile et immigration : 1,3 Md€ ». Aucun détail de calcul.
- **Fiche mesure** (`sources/T20/integration/nfp_asile.html`, web.archive.org 20240725013734) : « l'absence de précisions supplémentaires sur la forme que prendrait cette abrogation […] empêche un chiffrage, même approximatif, de cette mesure ». La fiche décrit les mesures de la loi de 2024 telles que promulguées (régularisation dans les métiers en tension, carte « talent – profession médicale », exigences de langue, éloignement…) et ne cite pas la condition de résidence. Écart interne à Montaigne déjà relevé par T22.
- **iFRAP et Asterès** : la mesure est dans leur résidu, sans montant propre (`data/raw/chiffrages_instituts.csv`, lignes `nfp_asile` iFRAP et Asterès, `dans_residu`). Aucun chiffreur ne donne de montant pour les articles en vigueur des lois de 2018 et de 2024.

## 2. État de la disposition au 30/06/2024

- **Décision n° 2023-863 DC du 25/01/2024** (`sources/T23/programmes/cc_2023863dc.html`), § 94 : « L'article 19 a pour objet de soumettre le bénéfice du droit au logement, de l'aide personnelle au logement, de l'allocation personnalisée d'autonomie et des prestations familiales pour l'étranger non ressortissant de l'Union européenne à une condition de résidence en France d'une durée d'au moins cinq ans ou d'affiliation au titre d'une activité professionnelle depuis au moins trente mois » ; § 96 : « adoptées selon une procédure contraire à la Constitution, elles lui sont donc contraires ». Dispositif, article 1er : « Sont contraires à la Constitution […] les articles 15, 16, 17, 18, 19, 22 […] ».
- **Loi n° 2024-42 du 26/01/2024, version JORF** (Légifrance, copie web.archive.org 20250107210918, `sources/T24/integration/loi_2024-42_jorf_wb.html`) : « Article 19 [Dispositions déclarées non conformes à la Constitution par la décision du Conseil constitutionnel n° 2023-863 DC du 25 janvier 2024.] ». La disposition n'a jamais été promulguée.
- **Décision n° 2024-6 RIP du 11/04/2024** (`sources/T23/programmes/cc_20246rip.html`) : la même condition, proposée par référendum, est jugée contraire à la Constitution sur le fond. Elle n'a pas non plus été adoptée.

État au 30/06/2024 : **censurée** (critère R1 de la consigne). En juin 2024, le droit en vigueur ne contenait pas la mesure dont la ligne chiffre l'abrogation. Abroger les lois de 2018 et de 2024 ne change donc pas l'accès des étrangers récemment arrivés aux prestations familiales et aux APL.

## 3. Ce qui reste de la ligne

La promesse vise aussi les articles en vigueur des lois du 10/09/2018 et du 26/01/2024 (titres de séjour, procédure d'asile, rétention, éloignement…). Leur effet budgétaire n'est chiffré par aucun chiffreur ; Montaigne le juge impossible à chiffrer « même approximativement ». Le projet ne chiffre pas de mesure lui-même : cette part reste non calculée, comme les autres mesures sans chiffrage.

## 4. Proposition de traitement (à valider)

Selon la convention de référence 2024 (écart au droit de juin 2024) :

| Colonne | Actuel | Proposé |
|---|---|---|
| `statut_reference` | `absente` | `partielle` : la part chiffrée est déjà dans le droit de juin 2024 (la condition n'existe pas) ; le reste de la promesse est une mesure nouvelle, non chiffrée |
| `facteur_reference` | 1 | 0 : tout le montant chiffré porte sur la part déjà acquise |
| `source_reference` | phrase de la convention | décision 2023-863 DC, § 94-96 et dispositif ; loi n° 2024-42, version JORF, art. 19 ; micro-chiffrages Montaigne p. 5 |
| `confiance_reference` | `medium` | `high` (sources primaires lues) |
| `note_reference` | statut 2027 | inchangée (le statut 2027 reste « absente » : le PLFSS 2027 propose une condition d'un an, que la ligne de 2024 ne chiffre pas) |
| `independant`, `regle`, `facteur` | −1,3, Aucune, 1 | inchangés : le chiffrage reste affiché tel que publié par Montaigne |

Effet : le solde central du programme NFP 2024 s'améliore de 1,3 Md€ (la ligne compte pour 0). La fiche de la ligne dit pourquoi.

Autres fichiers à aligner :

- `data/raw/non_chiffre_foyer.csv`, ligne NFP n° 22 : le libellé « accès aux prestations des étrangers récemment arrivés » ne correspond plus à la mesure. Proposé : « Abrogation des lois asile et immigration (articles en vigueur : séjour, asile, éloignement) », avec la même raison (« Ne concerne pas les situations du simulateur ») et la source de la décision 2023-863 DC.
- `data/raw/statut_reference_2027.csv` : inchangé.

Variante écartée : passer `independant` à 0. Le montant publié par le chiffreur doit rester visible ; c'est la référence qui l'annule, comme pour `ens_chomage` (règle « Déjà dans la référence », facteur 0). La règle « Déjà dans la référence » n'est pas reprise ici : elle vise une économie inscrite dans la trajectoire de référence, pas une disposition censurée, et changer la règle ferait passer la ligne dans un autre test de symétrie.
