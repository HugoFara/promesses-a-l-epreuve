# T2c — Sources lues avec le navigateur (14 octobre 2026)

Lecture avec Chrome des sources inaccessibles en automatique (403, pare-feu anti-robot, Incapsula). Les PDF protégés ont été lus dans le navigateur (extraction de texte avec pdf.js dans la page) et leur sha256 calculé dans la page ; les protections anti-robot n'ont pas été contournées (pas de réutilisation des cookies de défi dans `curl`). Quand le document a pu être téléchargé normalement, il est archivé dans `sources/T2c/` ; sinon, une fiche d'extraits datée le remplace (`extrait_*.txt`). Corrections appliquées : `corrections.csv` (23 lignes, toutes inscrites dans `data/raw/historique.csv`).

## Résultats

| Ligne | Avant | Après | Source primaire |
|---|---|---|---|
| `capital_fr` (ε = 0,77) | medium | **high** | Colonne des auteurs (cepr.org). Apport nouveau : élasticité croisée des revenus du travail positive (jusqu'à 1/10 de l'élasticité directe) ; le taux de Laffer passe de 57 % à 43 %. La règle « Élasticité capital » l'ignore : elle surestime un peu le rendement d'une hausse d'impôt sur le capital. |
| `rd_ocde` | « ≈1 (moyenne) » (correction T2b) | **1,4 (moyenne OCDE, 20 pays)** | Colonne OCDE (cepr.org) : « around 1.4 units ». La valeur d'origine était juste ; le ≈1 de la CNEPI est propre au CIR français (ligne `cir`). |
| `tzcld` | medium | **high** | Rapport final du comité scientifique (Dares, 2025), p. 9 : coût brut 26 600 €/EQTP, coûts évités et recettes 12 900-15 300 € → coût net 11 300-13 700 €. |
| `garantie_jeunes` | medium | **high** | Rapport final (Dares, 2018), p. 7 : +7,1 points (1re cohorte), non significatif (2e). |
| `apl` | fourchette non numérique | **[0,5 ; 0,8]** | Fack (2005), Persée, p. 17 : « entre 50 % et 80 % ». Le 78 % n'apparaît pas dans le texte numérisé (central conservé, signalé). |
| `nr_css` | high | inchangé (confirmé) | Communiqué DREES : 44 % (2021), 31 % sans participation. |
| `e_carence` | 1,0, medium | **0,95, high** | Cour des comptes, Sécurité sociale 2024, p. 214 : 945 M€ (950 au tableau 25), base 2022. |
| `e_appr` | 2,86, medium | **2,86, high** | Cour des comptes, janvier 2025, p. 16 : 2 857,8 M€ en 2027 (scénario 2). |
| `l_point5` | medium | medium (note précisée) | Coût ministériel de +1,5 % en 2023 (3,2 Md€) via Acteurs publics ; le jaune « fonction publique » 2027 n'est pas encore publié. |
| PIB 2026-2027 | calculé (3 051,2 / 3 134,0) | **publié : 3 051 / 3 135** | PLF 2027, dossier de presse, p. 53 (budget.gouv.fr). Même tableau : prix hors tabac 2027 = 1,7 % → gel des pensions recalculé (−550 €/an pour le couple type au lieu de −581). |

## Non trouvé

- Non-recours aux aides au logement et à l'AAH : aucune estimation DREES publiée (recherche sur le site de la DREES).
- Coût d'un point d'indice dans un document officiel 2026-2027 : jaune non publié ; le dossier de presse confirme seulement le gel.

## Reste en confiance medium

- `nr_cmuc` (élasticités).
- Paniers : `l_smic`, `l_smic_emploi` (valeurs dérivées), `l_point5`, `l_surtaxe` (rendement 2026 dérivé), `e_feries`, `e_oper`, `e_fp`, `e_ame` ; `l_rachats` en low.
- Couche 1 : 11 mesures ajoutées par T10a, surtout parce que l'ex ante ou l'ex post est une somme calculée ou une citation d'évaluation préalable dans un rapport parlementaire. Pour les relever : lire les évaluations préalables des PLF 2008 (CIR), 2015 (CITE), 2018 (IS), 2020 (IR, taxe d'habitation), 2021 (impôts de production) sur budget.gouv.fr, désormais lisible avec le navigateur.
