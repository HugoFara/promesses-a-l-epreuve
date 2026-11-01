# T27 G6.4 et G6.5 : nouveaux cas passés

**État au 01/11/2026.** Collecte seule. Rien n'est intégré à `data/`. Aucune règle n'est attribuée ici : l'attribution à l'aveugle reste à faire par un autre agent (`recherche/validation/README.md`). Pour lui préparer le matériel, il faut retirer de `cas.csv` les colonnes du réalisé (`ex_post_*`, `estimateur_ex_post`, `cause_principale`, `source_ex_post`, `citation_ex_post`, `page_ex_post`, `note`, `url`, `citation`, `page`).

Fichiers : `cas.csv` (colonnes de `data/raw/mesures_cout.csv`, plus `url`, `citation` et `page` ; la nature du réalisé est dans `type_ex_post`), `sources.csv` (12 sources archivées dans `sources/T27/G6/cas/`, avec leur sha256).

## 1. Cas trouvés (4)

| id | Ex ante → réalisé (Md€) | `type_ex_post` | Confiance | Drapeaux |
|---|---|---|---|---|
| `prime_conversion_2018` | 0,214 → 0,377 | observe | high | même dispositif que 2019 |
| `prime_conversion_2019` | 0,740 → 0,820 | observe | medium | ex ante de préparation du PLF (le montant de la LFI, plus bas, n'est pas donné) ; barème modifié en juillet 2019 |
| `garantie_jeunes_2017` | 0,420 → 0,352 | observe | medium | `credit_vote` : nombre de bénéficiaires visés non lu dans une source primaire |
| `tabac_droits_2018` | 0,51 → 0,86 (0,9) | reestimation | medium | ex ante secondaire (Sénat, qui cite le Gouvernement) |

Les trois cas `observe` sont des dépenses de dispositifs à la demande. D'après leur seule nature, aucun ne semble relever des cinq règles prioritaires (revenus, IS, succession, réforme structurelle, substitution retraites). Le choix de la règle reste celui de l'agent d'attribution.

## 2. Pistes sans cas

- **Sous-indexation des pensions de 2019 (G6.5)** : l'ex ante est confirmé (2,8 Md€, « évaluation préalable de l'article 44 du PLFSS 2019 », d'après la Cour, *Sécurité sociale 2020*, ch. III, p. 22 du PDF). Aucun réalisé chiffré n'a été trouvé : la CCSS de septembre 2019 et le rapport du Sénat n° 600 (2019-2020) disent seulement que la mesure a freiné les dépenses, et que la revalorisation « aurait atteint 1,6 % » sans elle. Même s'il était trouvé, ce réalisé serait une réestimation.
- **Bascule CSG de 2018 (G6.5)** : aucune source ne compare le rendement de la hausse de CSG à sa prévision (recherches web, Cour, CCSS).
- **Carrières longues, décret du 2 juillet 2012** (piste ajoutée, règles retraites) : réalisé = surcoût de 2,7 Md€ en 2019 « estimé […] selon la Drees » (Cour, *Sécurité sociale 2020*, p. 25 du PDF), donc une réestimation. L'ex ante du Gouvernement (3 Md€ par an en 2017, selon l'IFRAP) n'a pas été lu dans une source primaire, et il porte sur une autre année. Non retenu.
- **Taxe sur les plus-values immobilières élevées (2013)** (piste ajoutée) : l'ex ante est lu (230 M€, rapport du Sénat n° 213 sur le PLFR 2012). Le produit réel n'a pas été trouvé : seule la part affectée à la CGLLS, plafonnée, est publiée.
- **Complémentaire santé solidaire** : coût de la réforme évalué à « 220 M€ à horizon 2022 » (presse, non lu dans une source primaire). Aucun réalisé sur le même périmètre (surcoût de la réforme) : seule la dépense totale de la C2S est publiée.
- **Bonus écologique de 2018** : écart de -34 % au prévisionnel (NEB 2018, tableau n° 5). Écarté, car les modifications de 2018 sont des « ajustements mineurs » d'un dispositif existant : c'est une prévision de dépense courante, pas le chiffrage d'une mesure.
- **Impôt minimum mondial (pilier 2)** : prévision de 500 M€ pour 2026 (réponse ministérielle de juin 2026). Les premières déclarations étaient dues au 30 juin 2026, et aucun montant encaissé n'est encore publié. Piste à reprendre en 2027 (règle IS, réalisé récent).
- **Non trouvés** : assurance chômage 2019 et 2023 (pas d'ex post de l'Unédic sur les économies), suramortissement de 2015 et de 2019 (pas de réalisé), objectif Duflot (effet, pas un coût ; aucune source primaire lue), CSPE (charges prévues et constatées par la CRE : prévision d'un dispositif existant, pas d'une mesure ; non approfondi).

## 3. Points de vigilance

- `prime_conversion_2018` et `prime_conversion_2019` : deux réformes distinctes du même dispositif. Elles comptent séparément selon le README, mais leurs erreurs ne sont pas indépendantes.
- `garantie_jeunes_2017` : l'ex ante est la somme de deux lignes de crédits (calcul) ; il porte sur tout le dispositif, pas sur la seule généralisation (165 M€ de mesures nouvelles).
- `tabac_droits_2018` : l'ex ante dit inclure une réaction des volumes (élasticité -0,75) ; d'où `comportement_inclus_ex_ante = oui`.
