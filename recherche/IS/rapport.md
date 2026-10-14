# Réalisés observés pour l'impôt sur les sociétés (14 octobre 2026)

Objectif : tester la règle « Élasticité IS » sur des rendements réellement encaissés, et non sur des chiffrages administratifs à comportement constant (baisse de l'IS à 25 %, chiffrages d'instituts de 2017). Sources : rapports de la Cour des comptes sur le budget de l'État (archivés dans `sources/IS/`, index `sources.csv`).

## Cas retenus (ajoutés à `mesures_cout.csv`)

| Mesure | Annoncé | Encaissé | Écart | Source |
|---|---|---|---|---|
| Surtaxe d'IS des grandes entreprises, 1re année (2025) | 8,0 | 7,5 (acomptes) | −6 % | Cour, budget de l'État 2025, p. 77 et 43 ; note recettes fiscales p. 42 |
| Contribution de 5 % sur l'IS des grandes entreprises (2013) | 0,8 | 1,2 | +50 % | Cour, budget de l'État 2013, p. 251 |
| Contribution différentielle sur les hauts revenus (2025) | 2,0 | 0,4 (acompte) | −80 % | Cour, note recettes fiscales 2025, p. 42 |

## Résultat de la validation (règles attribuées à l'aveugle)

- **Élasticité IS : contredite.** La règle (facteur 0,73) prévoit −27 %. Observé : −6 % en 2025, alors que le bénéfice fiscal a été un peu meilleur que prévu (+1,0 % contre 0) ; +50 % en 2013. Sur les deux cas observés, l'erreur médiane passe de 28 % à 49 %.
- **Élasticité revenus : confirmée, faiblement.** La CDHR a rapporté 80 % de moins que prévu ; la règle (0,9) ne corrige que 10 points de cet écart. Un seul cas.

## Réserves

- 2025 : montants d'acomptes ; les soldes de l'IS et de la CDHR ne seront connus qu'après les déclarations de 2026. La Cour signale de possibles effets croisés entre la surtaxe et l'IS dans les déclarations.
- Ce sont des réponses de 1re ou 2e année. L'élasticité de la règle (Heckemeyer-Overesch, transfert de bénéfices des multinationales) mesure plutôt un ajustement de moyen terme.
- 2013 : la prévision (0,8) est déduite de l'écart publié par la Cour (1,2 − 0,4).

## Non trouvés

- Rendement réalisé de la hausse à 10,7 % (2014-2015) : le chiffrage annoncé (+2,5 Md€, Cour, budget 2014, p. 71) existe, mais aucun rapport n'isole le réalisé.
- Taxe sur les rachats d'actions 2025 : 0,5 Md€ encaissés (Cour, note recettes fiscales 2025), mais le chiffrage d'avant adoption n'est connu que par la presse (0,2 Md€) : à vérifier sur l'évaluation préalable du PLF 2025.
- Baisse de l'IS à 33 → 25 % : pas de coût réellement observé (le contrefactuel n'est pas observable) ; les « réalisés » disponibles sont des chiffrages administratifs.
