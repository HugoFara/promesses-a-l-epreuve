# Prédictions enregistrées : budget 2027

Registre publié le 16/10/2026, avant que le coût réel de ces mesures n'existe. C'est le seul test de la méthode qui soit aveugle par construction : on ne peut pas choisir la règle qui « marche » quand le résultat n'est pas encore connu.

## Contenu

`predictions.csv`, une ligne par mesure et par année (2027, et 2028 quand la source la chiffre) :

- `chiffrage_md` : chiffrage officiel (évaluations préalables du PLF 2027, annexe 9 du PLFSS 2027, étude d'impact de la loi n° 2026-534), relevé dans `recherche/T19/mesures.csv`, avec citations et pages ;
- `regle` : règle attribuée à l'aveugle par un agent qui ne voyait que la mesure et la liste des règles (`recherche/T19/attribution_agent.csv`) ;
- `facteur`, `prediction_md` : facteur central de la règle et chiffrage × facteur, ce que la méthode prévoit pour le rendement ou le coût réel ;
- `comparable` : `non` pour les transferts entre administrations, dont l'effet sur le solde public n'est pas chiffré par la source, pour un doublon, et pour la règle « Recette ponctuelle », dont le facteur n'est pas une prévision du rendement.

143 lignes, dont 125 comparables. Pour 47 d'entre elles, la règle change le chiffre (facteur différent de 1). Pour 2027, la méthode retire au total environ 1,2 Md€ aux 18,9 Md€ d'amélioration nette du solde attendue des lignes comparables : l'essentiel vient de la contribution exceptionnelle des grandes entreprises (5,0 → 4,7) et des mesures sur les revenus du capital. Le test portera donc surtout sur ces lignes et sur les 17 effets promis (loi contre la fraude, notamment).

## État gelé

| Élément | sha256 |
|---|---|
| `recherche/T19/mesures.csv` | `9a9579308c52d2af99a94d8b7cffc4182ce9d1b330913c405e4cdcc26dbdd17b` |
| `recherche/T19/attribution_agent.csv` | `8d26ee71d38d893ae2b6e0f93dceea0eb977fa8cbea36f0faa7a8ccb4acafa42` |
| `predictions.csv` | `c427fd83cd17a71a2aa003f3e16275a8f4836dab0096e6fdc2b0575d4151b702` |
| `data/raw/regles.csv` | `3c97911a18e888fc1faefd9b1922172f32f5dfb703e0ef57a7b50f3da8a8eccb` |
| `data/raw/moteur_regles.csv` | `44b3fe92a754144f0995a2e676cd5d5c033f92869d8d324827488972fb3ff4b6` |
| `data/raw/moteur_parametres.csv` | `dd32dae6f1b29a5eef54a1244c935ef62ab7ec2125c7cf211f94d50933a786ad` |

La date certaine est celle du commit qui ajoute ce dossier. **Ces fichiers ne doivent plus être modifiés.** Une correction (erreur de relevé, mesure modifiée par le Parlement) s'ajoute dans un nouveau fichier daté, `corrections_AAAA-MM-JJ.csv`, qui dit quelle ligne elle touche et pourquoi ; la prédiction d'origine reste visible.

## Comparaison au réalisé

- **Quand** : à partir de mai 2028 (rapport de la Cour des comptes sur le budget de l'État 2027, notes d'exécution budgétaire, rapport de la commission des comptes de la Sécurité sociale), puis en 2029 pour les lignes 2028.
- **Quelles lignes** : seulement les mesures votées telles quelles. Une mesure supprimée ou modifiée en cours de débat est écartée, avec sa raison ; elle n'est jamais comparée à un réalisé qui ne lui correspond pas.
- **Comment** : même calcul que `scripts/validation.py` : erreur du chiffrage officiel et erreur de la prédiction, rapportées au chiffrage officiel, puis cas améliorés et dégradés, par règle. Les réalisés administratifs (crédits consommés, chiffrage à comportement constant) ne comptent pas.
- **Ce qui sera publié** : le résultat, qu'il soit favorable ou non à la méthode.
