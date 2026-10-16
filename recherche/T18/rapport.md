# T18 : tester les règles de correction sur de nouvelles mesures passées

Rapport au 16/10/2026. Consigne : `CONSIGNE.md`. Détail de la collecte : `parts/notes_[A-D].md`. Fusion, contrôles et décisions en suspens : `rapport_fusion.md`. Rien n'est intégré à `data/` ; la phase 4 (intégration) reste à décider.

## 1. Ce qui a été fait

| Phase | Résultat |
|---|---|
| 0. Gel | Règles de l'état `0b4175f` (`regles.csv`, `moteur_regles.csv`), non modifiées |
| 1. Collecte (4 agents) | 60 lignes de coût, 15 d'effets, 83 sources archivées dans `sources/T18/` |
| 2. Fusion | 55 lignes de coût après 5 fusions ; 150 citations retrouvées dans les archives ; 83 sha256 conformes |
| 3. Attribution à l'aveugle | `attribution_agent.csv`, copié tel quel (sha256 `95b05341…`) ; 70 lignes ; issue connue : 26 oui, 44 non |

Un seul ajout a été fait au matériel aveugle : la règle « Élasticité électricité », absente de l'ancienne liste (`rapport_fusion.md`, dernière section).

## 2. Couverture par règle

Cas `observe` en dispositifs distincts (`rapport_fusion.md`) face à la cible de 8 : Taux de recours 9, Recette ponctuelle 9 (4 propres à la règle), Nouvelle assiette 6, patrimoine 5, revenus 4, capital 2, succession 2, IS 2, électricité 1, Réforme structurelle 1, carburants 0. **Critère de réussite non atteint** (1 règle sur 10 au lieu de 6). Effets : 15 lignes, cible atteinte de justesse.

Deux règles paraissent intestables avec ce protocole : carburants (la recette d'une hausse d'accise n'est jamais isolée du volume) et Réforme structurelle (économies réestimées par l'administration, pas observées).

## 3. Statistique provisoire

Calcul : `stats_provisoires.py` (lancé depuis `data/`), même formule que `scripts/validation.py` ; sorties `stats_provisoires.csv` et `stats_provisoires_mesures.csv`. Seules les lignes où la règle change le chiffre (facteur ≠ 1) et dont le réalisé est `observe` comptent. Ces chiffres ne remplacent pas ceux du site : les nouvelles mesures ne sont pas intégrées et les 27 décisions de `rapport_fusion.md` ne sont pas tranchées.

| Groupe | n | Erreur médiane : départ → règle | Améliorés / dégradés |
|---|---|---|---|
| Tout | 56 | 39,9 % → 34,5 % | 32 / 24 |
| Tout sauf Recette ponctuelle | 45 | 44,4 % → 29,0 % | 32 / 13 |
| — dont issue connue de l'agent | 25 | 50,0 % → 29,0 % | 19 / 6 |
| — dont issue inconnue de l'agent | 20 | 30,4 % → 29,0 % | 13 / 7 |
| Chiffrages officiels seuls, sauf Recette ponctuelle, issue inconnue | 16 | 25,0 % → 26,1 % | 10 / 6 |
| Comportement inclus ex ante = oui | 4 | 29,7 % → 12,5 % | 4 / 0 |

Par règle (observés) :

| Règle | n | Départ → règle | Améliorés / dégradés |
|---|---|---|---|
| Effet promis | 10 | 93,8 % → 29,0 % | 8 / 2 |
| Taux de recours | 15 | 34,4 % → 22,0 % | 10 / 5 |
| Nouvelle assiette : risque juridique | 5 | 62,3 % → 46,5 % | 5 / 0 |
| Élasticité patrimoine | 6 | 38,8 % → 38,5 % | 3 / 3 |
| Élasticité revenus | 2 | 32,5 % → 42,5 % | 0 / 2 |
| Élasticité IS | 2 | 67,9 % → 61,9 % | 2 / 0 |
| Élasticité électricité | 2 | 18,0 % → 18,0 % | 1 / 1 |
| Élasticité capital, succession ; Réforme structurelle | 1 chacune | — | 1 / 0 chacune |
| Recette ponctuelle | 11 | 25,0 % → 109,1 % | 0 / 11 |

## 4. Lecture

1. **Le gain dépend surtout de ce que l'agent d'attribution savait.** Sur les cas dont il connaissait l'issue, l'erreur médiane baisse de 50 % à 29 % ; sur ceux qu'il ignorait, elle ne bouge presque pas (30 % → 29 %), et elle monte légèrement pour les seuls chiffrages officiels (25 % → 26 %). On ne peut pas exclure qu'il ait choisi, même sans le vouloir, la règle qui « marche » pour les cas connus. Le résultat le plus prudent est celui de la ligne « issue inconnue » : les règles ne dégradent pas les chiffrages, mais ne les améliorent pas nettement non plus.
2. **Recette ponctuelle : le test est mal posé.** Le facteur 0 signifie « ne pas compter cette recette dans le solde durable ». Comparé au rendement de la première année, il donne mécaniquement une erreur de 100 %. Il faut un autre indicateur (recette encore perçue après la durée annoncée), à choisir par l'utilisateur (`rapport_fusion.md`).
3. **Effet promis et Taux de recours tiennent**, y compris sur les cas d'issue inconnue (3 améliorés sur 4 pour chacune), mais sur de petits nombres. Pour Taux de recours, c'est la version d'origine de la règle qui est testée : aucun ex ante lu ne suppose un recours complet, et les ex ante sont des crédits votés.
4. **Élasticités fiscales : rien de concluant.** 1 à 6 cas par règle. Patrimoine est neutre (3 / 3), revenus dégradée (0 / 2).
5. **Double compte du comportement** : les 4 seuls cas où l'ex ante dit inclure une réaction sont tous améliorés, ce qui ne va pas dans le sens de l'hypothèse ; 49 cas sur 55 restent `inconnu`. L'hypothèse ne peut être ni confirmée ni écartée.
6. **Test aveugle** : un seul réalisé publié en 2026 ; le sous-échantillon prévu pour réduire la fuite est vide.

## 5. Décisions laissées à l'utilisateur

En plus des 27 points de `rapport_fusion.md` :

- intégrer ou non ces mesures à `data/raw/` (phase 4), et avec quelles exclusions (drapeaux `low`, `credit_vote`, `ex_ante_conteste`…) ;
- choisir l'indicateur du test « Recette ponctuelle » avant de publier un statut pour cette règle ;
- décider comment le site présente la dépendance du résultat à `issue_connue` ;
- lancer ou non une seconde collecte ciblée (patrimoine, revenus, nouvelle assiette, IS), en priorité sur des réalisés récents, moins connus d'un agent d'attribution.

## 6. Après intégration (16/10/2026)

Une fois les mesures intégrées à `data/raw/` avec les décisions de l'utilisateur, la lecture du § 4.1 ne tient plus. Ces décisions : lignes fragiles et années suivantes d'un même dispositif hors statistique, « Recette ponctuelle » non concluante et sortie des agrégats. Sur les chiffrages officiels de la statistique principale de `scripts/validation.py` (anciennes et nouvelles mesures) :

| Groupe | n | Erreur médiane : départ → règle | Améliorés / dégradés |
|---|---|---|---|
| Issue connue de l'agent | 25 | 21,4 % → 22,0 % | 12 / 8 |
| Issue inconnue de l'agent | 24 | 16,4 % → 15,0 % | 8 / 6 |

L'écart entre cas connus et inconnus venait surtout des lignes désormais exclues. Il n'y a donc pas d'indice que la connaissance de l'issue ait favorisé la méthode. Le constat d'ensemble reste le même : sur le coût des mesures, les règles changent peu les chiffrages officiels ; sur les effets promis, elles les rapprochent nettement du réalisé.
