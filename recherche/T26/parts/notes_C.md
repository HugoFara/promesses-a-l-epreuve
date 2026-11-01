# T26, agent C : points restés ouverts (§ 8 du rapport d'intégration)

Date : 01/11/2026. Lignes : `lignes_C.csv` ; sources : `sources_C.csv` (archives dans `sources/T26/C/`).

## 1. `eps_capital` (Lefebvre, Lehmann et Sicsic)

Document lu en entier sur les tableaux : IZA DP 16112, mai 2023 (`sources/T26/C/lls_iza_dp16112.pdf`).

- **La valeur centrale est conforme.** Tableau 2 (p. 19, PDF p. 21), spécification préférée (2SLS, splines de ln RFR_t, instruments à la Auten-Carroll) : élasticité directe 0,767, erreur-type 0,011. Texte : « This elasticity is around 0.77 ». Le résumé dit « around 0.76 ».
- **IC à 95 % statistique** (calcul : 0,767 ± 1,96 × 0,011) : [0,745 ; 0,789]. Il est trop étroit pour représenter l'incertitude, qui vient surtout de la spécification.
- **Spécifications** : tableau 3 (p. 20, contrôles de revenu de Kopczuk) : « remains in the interval [0.76, 1.17] » (p. 21). Tableau 4 (p. 22, instruments de Weber) : « from around 0.7 to around 0.5 » ; même spécification que le résultat préféré : 0,508 (e.-t. 0,017). Plusieurs lignes du tableau 4 descendent à 0,22-0,32.
- **Proposition** : bas 0,5, central 0,77, haut 1,17. Si l'intégrateur préfère s'en tenir à l'IC statistique : 0,745 / 0,789.
- **Effet attendu** (`nfp_flat`, seule ligne en règle « Élasticité capital » ; formule `taxe_elasticite`, t0 0,354, t1 0,4627) : facteur central 0,44 inchangé, fourchette 0,18 (eps 1,17) à 0,63 (eps 0,5), soit 0,6 à 2,0 Md€ pour 1,4 au centre. Le solde central ne bouge pas, la fourchette NFP s'élargit.
- **Limite** : je n'ai pas pu lire la version publiée (Scand. J. Econ. 2025) : HAL est bloqué par Anubis et l'éditeur est payant. La colonne VoxEU de 2024 (`sources/T2c/`) donne les mêmes chiffres (0,77 ; 57 % ; 43 %).

## 2. Médecins en formation (poste de 0,1 dans `ens_autres_dep_reste`)

- **Chiffrage Montaigne** (micro-chiffrages Ensemble, `sources/T20/integration/montaigne_ensemble_microchiffrages.pdf`) : « (12500 €) x 8 000 étudiants supplémentaires », avec 8 000 = 16 000 en 2027 moins 8 000 en 2017, selon le programme. Le chiffrage part donc de 2017.
- **Droit de juin 2024** : l'arrêté du 13/09/2021 (ONP 2021-2025) fixe 51 505 médecins à former sur cinq ans, soit 10 301 par an, avec des seuils de 48 850 à 54 160. À la rentrée 2022, 10 765 places étaient ouvertes en 2e année. Sources : réponses ministérielles QE 13531 (JO du 05/03/2024) et QE 331 (JO du 20/12/2022). Je n'ai pas lu l'arrêté sur Légifrance, qui refuse les accès automatisés.
- **LFSS 2024 et PStab d'avril 2024** : aucune mention de la cible de 16 000 ni du numerus clausus (recherche en plein texte des archives T24 et T25). La hausse 2017-2024 est financée dans la base des universités, sans ligne propre dans la LFI 2024. Je n'ai pas trouvé de montant par crédit.
- **Part déjà acquise** : 2 301 étudiants sur 8 000, soit 29 % (de 1 770 à 2 765 selon le seuil bas de l'ONP ou les places de 2022). Au-delà de 2025, aucun ONP n'était en vigueur au 30/06/2024 : je suppose la reconduction de la capacité (droit constant).
- **Facteur (méthode T25)** : central 0,853, bas 0,601, haut 0,992 (voir le calcul dans `lignes_C.csv`). La ligne comptée passe de −2,512 à −2,483 : effet de +0,03 Md€ sur Ensemble 2024. Confiance medium.
- **Non trouvé** : nombre national de places en 2023-2024 et en 2024-2025 (seulement des recensements de presse, partiels). Le nouvel ONP 2026-2030, cité par la presse, n'a pas été lu : il concerne la référence 2027, pas celle de juin 2024.

## 3. `rn24_heritage`

- **Aucune méthode publiée.** La synthèse Montaigne ne donne que « 1 Md€ » et ne renvoie à aucune fiche. L'index CDX de web.archive.org (`legislatives-2024/rassemblement-national/*`, 21 URL) ne contient aucune fiche sur l'héritage ou les successions. Les micro-chiffrages RN n'ont pas de carte pour cette mesure ; les cartes voisines sont `rn24_transmissions` (5,3) et `rn24_donations`.
- **Présidentielle et législatives 2022** (index CDX, 640 URL) : la seule fiche RN sur les successions porte sur une autre mesure, l'exclusion de l'immobilier de l'assiette jusqu'à 300 000 €, chiffrée à 3,8 Md€ (archivée).
- **Programme RN** : « Supprimer les impôts sur l'héritage direct pour les familles modestes et les classes moyennes », sans seuil.
- **iFRAP** : 1 (0,5 dans la version du 24/06/2024), chiffre visible seulement dans l'image du tableau, sans calcul dans le texte.
- **Proposition** : justification rédigée dans `lignes_C.csv` (sur le modèle de `nfp_cotis_vieillesse`), confiance de la ligne high → medium, `note_confiance` remplie. Aucun effet sur le solde.
