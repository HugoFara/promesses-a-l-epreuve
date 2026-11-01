# T27, groupe 6 : G6.6, G6.7, G6.9 (recherche du 01/11/2026)

Consigne : `recherche/T27/suivi.md`, § G6.6, G6.7 et G6.9. Rien n'est modifié dans `data/` ni `scripts/`. Sources archivées dans `sources/T27/G6/divers/` et listées, avec leur sha256, dans `sources.csv` (les archives d'autres tâches réutilisées y figurent aussi).

Fichiers produits :

| Fichier | Contenu |
|---|---|
| `elasticites_propositions.csv` | 4 lignes au format de `data/raw/elasticites.csv`, précédées d'une colonne `action` |
| `tva_coicop.csv` | 67 postes COICOP hors énergie : taux 2026, autres taux, part, article du CGI, source, citation |
| `ttf_correction.csv` | correction proposée pour `ttf_relevement_2025` (format ancienne/nouvelle valeur, pour `appliquer_corrections.py`) |
| `sources.csv` | 44 sources |

---

## 1. G6.6 : non-recours (APL, AAH, CSS après 2021)

### 1.1 Complémentaire santé solidaire : pas d'estimation après 2021

Aucune estimation postérieure à 2021 n'existe au 01/11/2026. Le rapport annuel 2025 de la C2S (Direction de la sécurité sociale, janvier 2026, archivé) l'écrit :

> « A la date de publication du présent rapport, la DREES n'est pas en mesure d'établir une mise à jour des estimations du taux de recours pour les années 2022 et 2023. Ces estimations sont toutefois en cours de réalisation. » (p. 33 du PDF)

> « le taux de recours à la C2S était évalué à 56 % en 2021 : 69 % pour la C2SG et 34 % pour la C2SP » (p. 8 du PDF)

Le rapport 2024 disait déjà que le taux 2022 « n'a pas pu être calculé » (p. 8). Confiance `high` : rapport du ministère qui reprend la DREES.

**Proposition** : garder les valeurs de `nr_css` (44 %, 31 %, 66 ou 67 %), mais remplacer la source par ce rapport, qui peut être archivé (le site de la DREES rejette curl), et écrire dans la note que 2021 reste la dernière année estimée. Un écart à trancher : 1 − 34 % donne 66 % pour la C2SP, alors que le communiqué DREES du 13/12/2022 donne 67 %. C'est un écart d'arrondi.

Autre chiffre trouvé, proposé en ligne nouvelle (`nr_css_rsa`) : « le taux de recours à la C2S gratuite des allocataires du RSA est estimé à 80% en 2023 » (p. 38). Cela donne environ 20 % de non-recours, grâce à l'attribution automatique depuis 2022.

### 1.2 APL : aucune estimation nationale

Recherches faites : DREES (Dossiers n° 92 et 94, fiche 34 « Les aides au logement » de *Minima sociaux et prestations sociales* 2025), Cnaf (Dossiers d'étude n° 12 et 173), recherche web générale. La fiche 34 ne parle pas du non-recours. Le Dossier n° 94 ne donne un chiffre que pour les Pays-Bas (18 % en 2011), et le Dossier d'étude n° 173 aussi (27 % pour l'allocation logement).

Le seul chiffre français est **local et ancien** : Cnaf, Dossier d'étude n° 12 (Credoc, septembre 2000), sur la CAF du Havre : « le nombre de cas de non-recours n'excèderait donc pas 5 % du nombre de familles bénéficiaires » (p. 7). L'auteur parle lui-même d'un « recalcul approximatif et incomplet ». Ligne `nr_al_local` proposée en `low`, pour mémoire, à ne pas appliquer.

Un site secondaire (cesdefrance.fr) attribue à « un rapport de la DREES » un non-recours de « près de 20 % ». Je n'ai pas trouvé le rapport d'origine, donc ce chiffre n'est pas repris.

### 1.3 AAH : aucune estimation officielle

Rien chez la DREES (*Handicap* 2023, Dossiers n° 92 et 94), à la Cnaf ou à la Cour des comptes. Le seul chiffre est **61 %**, dans le Mémo Sécu n° 44 de la CGT (mars 2026, p. 3), avec pour seules sources « DREES, ODENORE, compilation de l'auteur ». Ligne `nr_aah` en `low`, avec l'action « ne pas ajouter ». Cela confirme T2b (« à ne pas utiliser »).

Hypothèse non vérifiée : le droit à l'AAH dépend d'un taux d'incapacité fixé par la CDAPH, que l'ERFS ne contient pas. Le modèle Ines ne peut donc pas simuler les personnes éligibles. Aucun document lu ne l'écrit.

**Effet sur le site** : aucun, comme prévu (`h_recours` est un texte ; l'AAH est en règle « Aucune »).

---

## 2. G6.7 : table COICOP → taux de TVA 2026 (hors énergie)

### 2.1 Niveau retenu

`data/raw/consommation_menages.csv` utilise la nomenclature de l'enquête Budget de famille (BdF) 2017 (TF106), au niveau de la division (01), du groupe (073, 126) ou de la classe (0451, 0954). La table suit les groupes à 3 chiffres. Elle descend à la classe (4 chiffres) quand un groupe mêle plusieurs taux (alimentation, eau, santé, loisirs, restauration). Les libellés viennent du fichier de métadonnées de la BdF 2017 (`sources/T20/B/insee_bdf2017_metadonnees_bdf2017.csv`). Exclus : 045, 0722 (énergie), 13 (hors consommation : impôts, gros travaux, remboursements), 046, 024, 129 (cadeaux, dépenses sans objet précis).

### 2.2 Sources

- Doctrine administrative : 24 documents du BOFiP, archivés, dans la version en vigueur au 01/11/2026. Chacun cite l'article du CGI. Légifrance rejette curl (code 403) : le CGI n'a été lu qu'à travers le BOFiP.
- *Voies et moyens*, tome II, du PLF 2026 (archive T20) : liste des taux réduits qui ne sont pas des dépenses fiscales (p. 10-11), et fiches 730205 à 730305.
- Insee, *Économie et statistique* n° 522-523 (André et Biotteau, 2021), tableau 1 : liste des dépenses que le modèle Ines traite comme exonérées. Ines applique un taux à chacun des 247 postes COICOP, mais cette table n'est pas publiée dans l'article. Elle pourrait être demandée à l'Insee ou à la DREES.

### 2.3 Résultats principaux

- **Alimentation (01)** : 5,5 % (CGI, art. 278-0 bis, A-1°), sauf la confiserie, les chocolats hors liste, les margarines, le caviar (20 %) et les produits vendus pour être consommés tout de suite (10 %). La part à 20 % n'est publiée nulle part. **Borne haute** calculée sur la BdF 2017 : (0115 + 0118) / 01 = **7,2 % à 8,4 %** selon le décile. C'est une borne haute, car ces deux classes contiennent aussi des produits à 5,5 % (beurre, huiles, sucre, confiture, miel, chocolat noir).
- **Taux à part dans la division 01** : boissons alcoolisées 20 % ; tabac 20 % (taux normal par défaut).
- **Autres postes** : loyers, soins, assurances, services financiers et enseignement sont exonérés. Livres 5,5 % ; presse 2,1 % ; transport de voyageurs 10 % ; restauration 10 % (alcool 20 %) ; hébergement 10 % ; médicaments 2,1 % (remboursables) ou 10 % (non remboursables) ; eau 5,5 % (assainissement 10 %). Le reste est au taux normal de 20 %.
- **Postes mixtes sans part connue** : 061, 0118, 0562, 0942, 1112, 124, 0444. La BdF 2017 ne sépare pas, par exemple, les médicaments remboursables des autres.

### 2.4 Changements de 2026 (loi n° 2026-103 du 19/02/2026)

Le texte de la loi a été lu sur Légifrance par WebFetch : on obtient un résumé, pas le texte brut, et la lecture se fait par tranches de 100 000 caractères. Seuls les articles 92 à 97 touchent la TVA des ménages :

- art. 92 : pompes à chaleur air/air ;
- art. 93 : énergie frigorifique distribuée par réseaux ;
- art. 94 : panneaux photovoltaïques ;
- art. 95 et 97 : logement social et Jeux olympiques de 2030 ;
- art. 96 : travaux forestiers (BOFiP ACTU-2026-00038).

L'article 81 abroge le h de l'article 279 (déchets). Ces mesures portent sur l'énergie ou les gros travaux, hors du champ de la table. Les taux par poste de la table ne changent donc pas en 2026, **sauf le point suivant**.

**Point de vigilance, les margarines.** Cerfrance (source secondaire) écrit que la LFI 2026 les passe à 5,5 % au 21/02/2026. L'article 25 sexies du PLF 2026 le prévoyait : l'amendement AN n° 3126 qui voulait le supprimer donne un coût de 50 M€. Mais ni la lecture de la loi promulguée par WebFetch, ni le BOFiP (BOI-TVA-LIQ-30-10-10, version du 19/11/2025, toujours en vigueur) ne montrent ce changement. La table garde donc 20 %, en `medium`, avec une note. **À trancher sur le texte de Légifrance, lu en entier, avant de coder.** L'effet par foyer est minime (0115 représente 1,7 à 2,3 % de la division 01).

### 2.5 Décisions laissées à l'intégrateur

1. Quel taux appliquer aux postes mixtes : le taux principal, ou un taux moyen pondéré à documenter ? Pour 01, la borne haute de la part à 20 % permet un encadrement : taux moyen entre 5,5 % et 5,5 + 0,084 × 14,5 ≈ 6,7 % (calcul).
2. Parking : le BOFiP le met au taux normal (BOI-TVA-CHAMP-30-10-50, § 50), alors qu'Ines le classe parmi les exonérés. La table suit le BOFiP.
3. Les postes en `low` (013, 0444, 0932, 093A, 0953, 124, 127, 128, 1113) sont à relire avant tout usage.

---

## 3. G6.9 : TTF, relèvement de 2025

- **Taux avant / après** : **0,3 % → 0,4 %** du prix d'acquisition (CGI, art. 235 ter ZD, V).
  - Avant : « Son taux est de 0,3 % du prix d'acquisition » (évaluations préalables du PLF 2025, p. 262 du PDF, archive T20).
  - Après : « Le I de l'article 98 de la loi n° 2025-127 du 14 février 2025 de finances pour 2025 porte à 0,4 % le taux, prévu au V de l'article 235 ter ZD » (BOFiP ACTU-2025-00034, 28/05/2025). Confiance `high`.
- **Date** : acquisitions « à compter du 1er avril 2025 » (même source, qui cite l'art. 98, II).
- **Origine** : la mesure n'était pas dans le PLF 2025 initial, où le taux restait à 0,3 %. Elle a été ajoutée au Sénat (article 26 quater, d'après legifiscal.fr, source secondaire).
- **Rendement attendu (ex ante)** : « de l'ordre de 500 millions », selon les estimations du ministère citées par l'amendement AN n° I-2523 au PLF 2026 (p. 2). C'est une source **secondaire** : l'amendement gouvernemental du Sénat, avec son chiffrage, n'a pas été trouvé. Confiance `medium`.
- **Réalisé** (déjà dans la ligne) : +0,5 Md€ de mesures nouvelles en 2025 (Cour des comptes, NEB 2026, tableau 13, p. 26 du PDF ; p. 22 imprimée). La Cour estime l'effet de l'entrée en vigueur au 1er avril à 0,2 Md€ (p. 13 du PDF).
- **Année pleine** : le tome I des *Voies et moyens* du PLF 2026 (p. 37) prévoit 2 630 M€ en 2026, « soit une hausse de +244 M€ par rapport à 2025 en raison de l'application en année pleine du taux relevé à 0,4 % ».
- **2026** : le taux reste à 0,4 %. Le BOFiP BOI-TCA-FIN-10-30 (version du 28/05/2025, en vigueur au 01/11/2026) indique : « Le taux de la taxe est fixé à 0,4 % » (§ 150). Dans la LFI 2026, lue par WebFetch, l'article 17 ne modifie que le II, 5°, de l'article 235 ter ZD, et l'article 80 ne cite la TTF que dans une clause de gage. Les amendements au PLF 2026 qui portaient le taux à 0,5 %, 0,6 % ou 0,7 % n'ont pas été retenus.

**Correction proposée** (`ttf_correction.csv`) : `rendement_md` (0,5, réalisé) et la source ne changent pas. La note est réécrite pour donner le taux, la date, le rendement attendu et l'effet en année pleine. Elle ajoute un ordre de grandeur pour une extrapolation : +0,1 point ≈ +0,7 Md€ par an, à assiette inchangée (calcul, sans effet sur les volumes). Un libellé plus précis est proposé en option. Il faut passer par `scripts/appliquer_corrections.py` : la colonne `ancienne_valeur` est identique, caractère pour caractère, à la note actuelle (vérifié).

**Effet sur le site** : aucun, comme prévu.
