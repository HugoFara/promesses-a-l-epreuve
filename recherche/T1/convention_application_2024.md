# Convention : référence de l'application aux programmes 2024

Note d'intégration du 20/10/2026 (issue #8). Elle écrit une convention décidée le 14/10/2026 (`data/raw/historique.csv`, ajout de la colonne `statut_reference`), qui n'était jusqu'ici notée que dans l'historique.

## Règle

| | Programmes 2024 (`application_lignes.csv`) | Paniers 2027 (`paniers.csv`) |
|---|---|---|
| Référence retenue | Droit de juin 2024 (programme de stabilité d'avril 2024), celui des chiffreurs | Loi votée + PLF et PLFSS 2027 déposés (T1) |
| `statut_reference`, `facteur_reference` | Écart au droit de juin 2024 : `absente` et facteur 1 pour une mesure nouvelle ; seule exception, `ens_chomage` (réforme déjà dans la trajectoire du PStab, règle « Déjà dans la référence ») | Écart à la référence 2027 |
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
