# Convention : référence de l'application aux programmes 2024

Note d'intégration du 20/10/2026 (issue #8). Elle écrit une convention décidée le 14/10/2026 (`data/raw/historique.csv`, ajout de la colonne `statut_reference`), qui n'était jusqu'ici notée que dans l'historique.

## Règle

| | Programmes 2024 (`application_lignes.csv`) | Paniers 2027 (`paniers.csv`) |
|---|---|---|
| Référence retenue | Droit de juin 2024 (programme de stabilité d'avril 2024), celui des chiffreurs | Loi votée + PLF et PLFSS 2027 déposés (T1) |
| `statut_reference`, `facteur_reference` | Écart au droit de juin 2024 : `absente` et facteur 1 pour une mesure nouvelle ; facteur 0 quand le chiffrage porte sur une disposition absente du droit de juin 2024 : `nfp_asile` (`partielle`, article censuré), `rn24_chomage` (`votée`, réforme non prise) ; voir T24. Facteur < 1 quand une part du montant est déjà financée par la référence : `rn24_prisons`, `ens_snu`, `ens_autres_dep_reste` (`partielle`) ; voir T25 | Écart à la référence 2027 |
| Statut par rapport à 2027 | Pour information : `note_reference` (« Statut par rapport à la référence 2027 (…) : … ; source : … ») et `data/raw/statut_reference_2027.csv` | Dans `statut_reference` |

Pourquoi : les chiffrages des programmes 2024 (Montaigne, iFRAP, OFCE, Asterès…) mesurent l'écart à la loi de juin 2024. Les juger par rapport à 2027 changerait leur montant de départ, sans que les chiffreurs aient pu en tenir compte, et rendrait la fourchette entre chiffreurs incomparable. La comparaison avec la référence 2027 est le rôle des paniers.

## Même mesure dans un programme et dans un panier

La colonne `mesure_panier` de `statut_reference_2027.csv` relie une ligne 2024 au panier de la même mesure (17 paires). `garde_fous.py` vérifie que les deux ont le même statut par rapport à 2027, sauf `raison_ecart`. Les montants, eux, peuvent différer, puisque les références diffèrent.

Cas du SMIC à 1 600 € net :

- `nfp_smic` (−19) : en juin 2024, les allègements de cotisations suivent le SMIC ; leur hausse (−21,5 selon Montaigne) fait partie du coût.
- `l_smic` (+2,3) : dans la référence 2027, le SMIC de référence des allègements est gelé (décret n° 2026-509 du 12/06/2026, prolongation proposée par le PLFSS 2027) ; cette part disparaît.
- Statut 2027 des deux lignes : `partielle`. Celui de `nfp_smic` valait `absente` après T22 (repris de `recherche/T1/statut_reference.csv`, ligne `l_smic_i`, que le panier avait déjà corrigé avec `raison_ecart`) ; il est aligné.

## Ce qui a changé le 20/10/2026

- 49 lignes (48 issues du découpage T22, plus `nfp_smic_emploi`) avaient leur statut et leur source 2027 dans `statut_reference` et `source_reference`. Elles reprennent la convention : `absente` (écart au droit de juin 2024) ; le statut 2027 et sa source passent dans `note_reference`. Deux lignes étaient `partielle` (`ens_leasing`, `rn24_prisons`). Aucun montant ne change : tous les facteurs valaient 1.
- Ces lignes entrent dans `statut_reference_2027.csv`.
- Page « Méthode » : accordéon « par rapport à quelle loi chaque mesure est comptée » ; lexique « Référence » ; fiche de chaque ligne 2024 : les deux statuts.

## Ce qui a changé le 22/10/2026 (T24, issue #9)

- `nfp_asile` : le chiffrage porte sur l'article 19 de la loi n° 2024-42, censuré avant promulgation (2023-863 DC). `statut_reference` `partielle`, facteur 0 ; le montant de Montaigne reste affiché.
- Réforme de l'assurance chômage de juillet 2024 : absente du droit de juin 2024 (pas de décret ; programme de stabilité sans montant ; Montaigne la laisse hors de sa base). `ens_chomage` perd la règle « Déjà dans la référence » et compte +4,5 ; `rn24_chomage` passe à `votée`, facteur 0, comme la même promesse du NFP (0 chez Montaigne, dans le résidu). Avant, `ens_chomage` et `rn24_chomage` la mettaient dans la référence et le NFP non.
- Détail et sources : `recherche/T24/rapport.md`.

## Ce qui a changé le 22/10/2026 (T25, issue #10)

- Dépenses déjà programmées ou budgétées au 30/06/2024 : seule la part non financée est comptée (`statut_reference` `partielle`, montant du chiffreur inchangé ; fourchette dans `source_reference`, faute de colonnes).
- `rn24_prisons` : facteur 0,06 (0,026 à 0,095) ; Montaigne chiffre le plan 15 000, financé par la loi n° 2023-1059 et le budget 2024, dont 117,5 à 420 M€ ne l'étaient pas.
- `ens_snu` : facteur 0,956 (0,917 à 0,956) ; les 160 M€ du SNU en LFI 2024 ne sont pas retranchés par Montaigne.
- `ens_autres_dep_reste` : facteur 0,863 (0,612 à 1) ; le poste « fauteuils roulants » (0,4) est déjà voté (LFSS 2024, art. 85).
- `rn24_rente_infra`, `nfp_superprofits` : recoupement possible avec la mesure « rentes » du programme de stabilité, non établi ; inchangées (recette ponctuelle, facteur 0), mention dans la justification.
- Détail et sources : `recherche/T25/rapport.md`.
