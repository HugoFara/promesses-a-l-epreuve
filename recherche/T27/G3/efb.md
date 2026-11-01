# T27 G3.4 : biais des programmes de stabilité mesuré sur la première publication (EFB)

Date : 01/11/2026. Calcul : `python3 recherche/T27/G3/efb.py` (depuis la racine ; lit `sources/T2b/EFB_Forecast_Tracker.xlsx`, sha256 `8c036cc6…26106c`, indexé dans `recherche/T2b/sources.csv`).

## Source et définitions

- **Classeur** : EFB Forecast Tracker, secrétariat du European Fiscal Board (https://commission.europa.eu/document/download/b3d0287b-cfc7-4ced-9c8b-903296900a0c_en?filename=EFB_Forecast_Tracker.xlsx), onglet `Forecast_Data`, pays `FR`, variable `nom_BB_pc_GDP` (« General government (S13), Net Lending », % du PIB, onglet `Definitions and abbreviations`).
- **Réalisé** (onglet `Information`) : « Outturn data always refer to the spring vintage of year T+1 ». Pour l'année T, ligne `SPR T+1`, horizon T : c'est la première publication du déficit, pas la série actuelle d'Eurostat qu'utilise la couche 2.
- **Prévision** : lignes `SCP <année>` (programmes de stabilité). Millésime EFB = année cible à 1 an − 1, sauf SP 2010-02 = `SCP 2009` ; la ligne `SCP 2010` ne correspond à aucun programme déposé (T2b § 1.3).
- **Erreur** = réalisé − prévision (négatif = programme optimiste).
- **Exclusion des crises** : celle de l'indicateur actuel (`scripts/calc.py`, `scripts/check_regression.py`) : années cibles 2009 et 2020 à 1 an ; 2009, 2010, 2020 et 2021 à 3 ans. T2b excluait les quatre années aussi à 1 an.

## Résultats (hors crises)

| Échantillon | 1 an | 3 ans |
|---|---|---|
| Indicateur actuel : couche 2, réalisé Eurostat actuel (`biais_t1`, `biais_t3`) | −0,60 (n = 19) | −1,93 (n = 15) |
| **A'. mêmes millésimes et prévisions que la couche 2, réalisé EFB (retenu)** | **−0,429 (n = 19)** | **−1,720 (n = 15)** |
| A. millésimes de la couche 2, prévision et réalisé lus dans le classeur | −0,394 (n = 18) | −1,750 (n = 14) |
| B. tous les programmes du classeur, sans `SCP 2010` | −0,445 (n = 20) | −1,847 (n = 17) |

Toutes années comprises : A' −0,91 (n = 21) et −2,76 (n = 19) ; B −0,91 (n = 22) et −2,77 (n = 21). Médianes hors crises (A') : −0,30 et −1,50 ; part des programmes optimistes : 74 % à 1 an, 100 % à 3 ans.

**Valeurs retenues** : `biais_t1_efb` = −0,43, `biais_t3_efb` = −1,72 (échantillon A'). C'est le seul qui ne change qu'une chose par rapport à l'indicateur actuel, la mesure du réalisé : mêmes 21 millésimes, mêmes prévisions (recoupées avec l'EFB par T2b § 1.3, seule différence SP 2003-12 : −3,55 contre −3,6), mêmes exclusions, mêmes effectifs. L'échantillon A perd SP 2010-02 à 3 ans (l'EFB s'arrête à 2012 pour ce millésime) et SP 2024-04 à 1 an (pas de ligne `SCP 2024`, seulement `MTP 2024`). B ajoute `SCP 2000` et `SCP 2001`, absents de la couche 2, et perd SP 2010-02 à 3 ans.

**Contrôle de reproduction de T2b** : avec `SCP 2010` et les quatre années exclues à 1 an, on retrouve −0,395 (n = 20), soit le −0,40 de T2b ; B à 3 ans redonne −1,85 (n = 17).

## Lecture

Sur la première publication, le biais est plus faible d'environ 0,17 point à 1 an et 0,21 point à 3 ans : les déficits ont surtout été révisés à la hausse après coup (par exemple 2005 : −2,9 en première publication, −3,5 aujourd'hui ; 2013 : −4,3 contre −4,9). Une partie du « dépassement » de la couche 2 vient donc de révisions statistiques postérieures, que le gouvernement ne pouvait pas viser. Inversement, la série actuelle est celle qui mesure le déficit réellement constaté ; d'où le choix de garder le central et de publier l'EFB en variante.

## Effet sur la projection (variante, `data/projection_variantes.csv`)

Référence corrigée du biais, dette en % du PIB : 2029 125,1 au lieu de 125,7 ; 2032 129,1 au lieu de 130,3. Déficit 2027 : 5,43 au lieu de 5,6 % du PIB. Le central (`data/projection.csv`) est inchangé.
