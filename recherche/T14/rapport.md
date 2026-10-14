# T14 — Montée en charge des retraites et accise symétrique sur l'électricité (14 octobre 2026)

Points 4.2 et 15 de l'audit (`recherche/audit/rapport.md`). Recherche documentaire sur les retraites : `retraites_recherche.md`. Sources dans `sources/T14/`, index `sources.csv`. Les citations clés ont été vérifiées dans les documents archivés.

## 1. Montée en charge des retraites dans la projection

**Ce qui n'allait pas.** `projection.py` gardait le coût 2027 (puis 2028) de chaque ligne constant en % du PIB. Or l'abrogation de la réforme de 2023 coûte de plus en plus cher : la réforme rapporte davantage chaque année, à mesure que l'âge légal monte.

**Sources** :
- rapport annexé au PLFRSS 2023, tableau 27, p. 96 (vérifié) : rendement net pour le système de retraite de 6,2 Md€ en 2027, 8,6 en 2028, 10,0 en 2029 et 11,8 en 2030 ;
- iFRAP (8,3 en 2027, 13,7 en 2030) ;
- Cour des comptes 2025 (régime général, pic de 7,1 Md€ en 2032).

L'agent de recherche corrige aussi l'audit : les montants du PLFSS 2027 (+1,9 / +2,8 / +3,7) sont des variations du rendement de la réforme sur les seuls régimes de base, pas des effets de la suspension. Aucun document lu ne chiffre la suspension après 2027 ; elle est supposée constante à 1,9 Md€.

**Correction.** Nouveau fichier `data/raw/montee_en_charge.csv` : un coefficient par ligne et par année (2027 = 1, en part du PIB), en bas, central et haut. La projection applique le central.

| Année | `l_ret62` (abrogation, LFI ajusté) | `l_ret60` (retour à 60 ans, LFI intégral) |
|---|---|---|
| 2028 | 1,32 (1,19-1,46) | 1,036 (1,022-1,052) |
| 2030 | 1,69 (1,45-1,99) | 1,078 (1,051-1,111) |
| 2032 | 2,00 (1,65-2,35) | 1,113 (1,073-1,152) |

Pour `l_ret60`, seule la composante « réforme 2023 » (8,2 Md€ sur 58, 6,3 nets de la suspension) monte en charge. Montaigne suppose lui-même stables en % du PIB le retour sur la réforme de 2010 et les minima.

**Effet** (2032) :

| Panier | Déficit | Dette |
|---|---|---|
| LFI intégral | 7,91 → **8,09** % | 144,2 → **144,8** % |
| LFI ajusté | 5,89 → **6,07** % | 134,2 → **134,8** % |
| Ensemble | inchangé (5,4 %) | inchangé (131,8 %) |

Le solde 2027 ne change pas.

**Limites** :
- les coefficients sont des calculs de l'agent, appuyés sur plusieurs sources de champs différents (système, régime général) ;
- la suspension après 2027 n'est chiffrée nulle part : elle est supposée constante ;
- pour `l_ret60`, la validation des années de RSA et la hausse du minimum contributif ne concernent que les nouveaux retraités : le niveau 2027 est probablement surestimé et la pente sous-estimée, sans qu'on puisse le chiffrer ;
- la projection n'utilise que le coefficient central ; les bornes sont documentées mais ne sont pas propagées ;
- aucune ligne d'Ensemble n'a de profil documenté (ses économies sont supposées constantes en % du PIB). C'est une asymétrie possible si certaines de ses mesures montent aussi en charge ; l'audit n'en a pas signalé.

## 2. Accise sur l'électricité : formule symétrique (`e_elec`)

**Ce qui n'allait pas.** La formule `accise` (élasticité-prix) s'appliquait aux hausses d'accise de LFI (`l_brunes`, facteur 0,73) mais pas à la baisse d'accise d'Ensemble (règle « Aucune »).

**Mesure** : selon la fiche Montaigne (`sources/T6/montaigne_ens_elec.html`), les −2,4 Md€ correspondent au maintien du tarif dérogatoire de l'accise sur l'électricité plutôt qu'au tarif normal. La baisse de 15 % des factures promise vient de la baisse des prix de marché, sans coût.

**Paramètres** (sources lues) :
- **tarifs** : 21 €/MWh au 1er février 2024 contre 32 €/MWh avant la crise (ministère de l'Économie, page lue dans le navigateur, fiche d'extraits) ;
- **effet sur le prix** : la hausse d'accise de 20 €/MWh a augmenté les factures de 8,6 % à 9,8 % ; un écart de 11 €/MWh vaut donc environ −5,1 % du prix (calcul) ;
- **élasticité-prix** : −0,8 (Insee, *Économie et Statistique* n° 513, consommation des ménages 2007-2015, résumé lu). Borne basse −0,2 pour un horizon court, valeur proposée par l'audit et non sourcée.

**Règle** « Élasticité électricité », même formule que `l_brunes` : facteur = 1 + ε·dp·(1 + a), avec a = 32 / (21 − 32). La consommation supplémentaire n'est taxée qu'au tarif réduit. Facteur **0,923** : e_elec passe de −2,40 à **−2,21** Md€, et le solde d'Ensemble de −7,2 à **−7,0** (l'audit attendait 0,1 à 0,3).

**Limites** :
- l'effet de la TVA sur la consommation supplémentaire n'est pas compté, pas plus que pour `l_brunes` (symétrie) ;
- l'élasticité de l'Insee est estimée sur données semestrielles et vaut sans doute davantage à moyen terme qu'en 2027.
