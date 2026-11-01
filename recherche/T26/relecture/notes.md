# T26, relecture indépendante : facteur de référence de `l_bandeaux`

Relecteur indépendant, 01/11/2026 (règle 2 de `CONTRIBUTING.md`). Mon calcul (§ 1) a été fait **avant** de lire `parts/notes_A.md` et `parts/lignes_A.csv`. J'avais seulement vu le résumé chiffré déjà publié dans `data/raw/paniers.csv` (0,4 [0,26 ; 0,50] ; loi votée 0,55), pas le modèle. Script : `modele_relecture.py` (numpy, `python3 -I modele_relecture.py`, environ 1 min). Sortie complète : `sortie_modele.txt`. Sources et empreintes : `sources.csv`.

Champ : statique, allègements généraux tous attributaires (régimes de base, Unédic, Agirc-Arrco), salaires exprimés en multiples du SMIC, année 2027. Le facteur est un rapport : il ne dépend pas du niveau en euros.

## Conclusion

| | Publié (agent A) | Recommandé (relecture) |
|---|---|---|
| Référence 2027 (loi votée + PLFSS 2027) | 0,4 [0,26 ; 0,50] | **0,55 [0,45 ; 0,65]** |
| Loi votée seule (RGDU, sans gel 2027 ni assiette) | 0,55 [0,44 ; 0,63] | **0,65 [0,60 ; 0,75]** |
| Loi votée, si le décret 2026-509 vaut aussi pour 2027 | 0,5 | 0,6 |

**Verdict : corriger 0,4 en 0,55** (et la variante loi votée de 0,55 en 0,65). Le facteur sur 11,4 Md€ passe de 4,6 à 6,3 Md€ (+1,7 Md€ pour le panier « LFI intégral »). Confiance : **medium** sur le sens de la correction (le facteur publié est trop bas), **low** sur la valeur (modèle, sans ventilation officielle par niveau de salaire).

L'écart ne vient pas de la distribution des salaires : avec les bandes de l'agent A, mon calcul retrouve mes résultats à 0,01-0,03 près (§ 2). Il vient de deux choix de méthode :

1. **La cible.** A transpose la mesure à la RGDU : en A, la cible part de la RGDU à 1,6 SMIC (10,9 %) et tombe à 0 à 1,88 ; en B, la RGDU reste entière jusqu'à 1,88 puis tombe à 0. Ces deux mesures sont plus généreuses que celle chiffrée par Bozio-Wasmer entre 1,6 et 1,88 SMIC, où la cible part de 7,8 %. Elles sont donc moins rentables, et la variante B (une marche à 1,88) n'est pas la mesure de la ligne. Le facteur 0,4 est la moyenne de A (0,46) et de B (0,31) : il est tiré vers le bas par B.
2. **L'assiette (art. 7).** A retire la totalité de l'effet de l'art. 7 au-dessus de 1,6 SMIC (−0,08 à −0,14, en divisant des euros de 2027 par des euros de 2024). Or entre 1,6 et 1,8 SMIC et entre 2,5 et 3 SMIC, la RGDU est plus généreuse que le barème de 2024. Là, l'assiette réduit cette générosité nouvelle, pas le rendement de la ligne. Au sens du recoupement, l'art. 7 ne retire que 0,05.

## 1. Mon calcul

### 1.1 La ligne (Bozio-Wasmer 2024)

- Rapport final, p. 202-203 : « supprimer les bandeaux maladie et famille, en prolongeant la courbe de la réduction générale jusqu'à une extinction complète des exonérations à 1,88 Smic » ; « économie budgétaire de 12,2 Md€ » ; graphique 4.11 : à 1,7 SMIC, « le taux d'exonération [...] passerait d'actuellement 7,8 % (au titre des taux réduits maladie, pour 6 points, et famille, pour 1,8 points) à 4,8 % ». Confiance high.
- Le barème de 2024 (p. 45-47 et p. 201) : le taux au SMIC est de 40,15 % (plus de 50 salariés ; « retrancher 0,4 point » sous 50), dont 7,8 points de bandeaux. Le taux maximal de la RG vaut donc T = 0,3235 (0,3195 sous 50 salariés) et la RG s'annule à 1,6 SMIC. Les seuils des bandeaux sont gelés en 2024 « à respectivement 2,47 et 3,46 Smic » (p. 46).
- La cible : taux = T/0,6 × (1,6/w − 1) + 0,078, borné à 0. Il s'annule à 1,87-1,88 SMIC et vaut 4,6-4,7 % à 1,7 SMIC (4,8 % dans le rapport, écart d'arrondi). Le barème ne change pas sous 1,6 SMIC (« taux marginal inchangé de 59 % jusqu'à 1,6 Smic », p. 204).
- Rendement par niveau de salaire : g(w) = E2024(w) − Ecible(w), nul sous 1,6 SMIC.

### 1.2 La référence 2027

- **Formule de la RGDU.** C = Tmin + Tdelta × [½ (3 × S / R − 1)]^P, avec Tmin = 0,02, Tdelta = 0,3781 (FNAL 0,1 %) ou 0,3821 (FNAL 0,5 %), P = 1,75, et 0 au-delà de 3 S. La source est FNTP 2026 (secondaire). Je l'ai recoupée sur une source primaire, le cas-type de l'annexe 9 du PLFSS 2027 (art. 7, p. 38) : « 1 SMIC 22 184 € » donne une réduction de « 8 528,54 € », et mon script trouve 8 528,50 € avec S = SMIC gelé (1 823,03 € × 12). Les cas-types de l'art. 7 (annexe 9, p. 41 : 213, 291 et 103 €) sont retrouvés à 217, 298 et 109 € (§ 1.5). Confiance high sur la formule.
- **Gel du SMIC de référence.** Décret 2026-509 : la valeur à retenir est le SMIC « applicable au 1er janvier 2026 », « au titre de l'année 2026 » (art. 2). FNTP : 12,02 € au lieu de 12,31 € après le 1er juin 2026. Annexe 4, p. 36 : « Le gel du barème de la réduction générale sera maintenu en 2027 ; ce gel permettra de maîtriser le coût du dispositif de 2,8 Md€ supplémentaires en 2027 ». Annexe 9, p. 100 : gain de « 5,6 Md€ pour les années 2026 et 2027 par rapport à l'absence de gel ». HCFP (§ 72) : « la revalorisation du SMIC au mois de janvier serait modeste ». Le montant de la hausse de janvier 2027 n'a pas été trouvé. J'ai donc pris S gelé / S réel ∈ {0,967 ; 0,973 ; 0,976}, où 0,976 = 12,02/12,31 correspond à l'absence de hausse en janvier. Contrôle : dans le modèle, le gel retire 6 à 8 % du coût de la RGDU, contre 5,6 / 74,7 = 7,5 % en officiel.
- **Assiette (PLFSS 2027, art. 7).** Les compléments (intéressement, participation, abondements) entrent dans la rémunération qui sert au coefficient, mais « sans qu'elles soient en revanche incluses dans la rémunération servant à calculer le montant de la réduction » (annexe 9, p. 38). Le rendement est de « + 3,3 Md€ pour 2027 », plus 0,4 Md€ au titre de la PPV (p. 41). Le coût total de la RGDU est de « 74 735 M€ » (annexe 9, p. 37, note 1). Profil par salaire : « Entre 1 et 2 SMIC, 49 % de la masse salariale, 35 % de l'intéressement, 33 % de la participation » (annexe 9, graphique p. 37). L'intensité relative est donc d'environ 0,7 entre 1 et 2 SMIC. Au-delà, elle n'est pas publiée ; j'ai testé 1,0, 1,3 et 1,8. Le niveau est calé pour que l'art. 7 retire 3,3/74,7 (variante 3,7/74,7) du coût de la RGDU. J'ai aussi testé une couverture de 54 % des salariés (« plus de 54 % des salariés sont couverts », p. 37).

### 1.3 Distribution des salaires

- Base : Insee Première n° 2079, figure 3. Ce sont les déciles et les centiles 95 et 99 des salaires nets en EQTP de 2024 dans le privé, pondérés par l'EQTP. Le SMIC net est déduit de la même source (« 10 261 euros net par mois (99e centile), soit 7,3 fois le Smic »). Le passage du net au brut suit un rapport brut/net qui croît avec le salaire : employés 2 500/1 941, cadres 6 224/4 629 (figure 1). Variante : rapport constant. L'interpolation est log-linéaire entre quantiles (variante : spline monotone).
- Calage : la distribution Insee (par personne) est plus dispersée que celle des postes utilisée par la DSS et par Bozio-Wasmer. Elle donne 43 % de la masse salariale entre 1 et 2 SMIC, contre 49 % pour la DSN 2025 (annexe 9). Je resserre donc log w d'un facteur λ (central 0,9, testé de 0,75 à 1). λ = 0,9 retrouve la part de la DSN (0,50). Les contrôles sont imparfaits mais cohérents : famille/maladie = 0,37 dans le modèle contre 9,69/26,62 = 0,36 dans le tableau 1.1 de Bozio-Wasmer (2024) ; ligne/bandeau maladie = 0,56 contre 12,2/26,62 = 0,46 (les bases diffèrent : microsimulation contre comptes de la CCSS) ; EQTP au-delà de 3,5 SMIC : 5,8 % contre 6,7 % (Bozio-Wasmer, p. 47, note 4).
- Le facteur est peu sensible à la distribution : de 0,55 à 0,59 pour λ entre 0,75 et 1 (sortie, bloc « Effet de la seule dispersion »).

### 1.4 Définition du facteur

La définition retenue est celle de la consigne : la « part du rendement statique de la ligne qui n'est pas déjà obtenue par la référence ». Pour chaque salaire w, la part déjà obtenue vaut min(max(E2024 − Eréf, 0), g). Là où la référence est plus généreuse que 2024, rien n'est obtenu, et la ligne ne gagne pas plus que g. Facteur = Σ (g − déjà obtenu) × w / Σ g × w. Cette définition (« recouvrement » dans le script) a l'avantage de ne pas obliger à réinventer la mesure dans le droit de 2026.

Pour situer l'incertitude de méthode, j'ai aussi calculé le rendement marginal de la cible de Bozio-Wasmer appliquée en 2027 (« cap » : exonérations ramenées à la cible au-dessus de 1,6 SMIC). Deux versions : cible exprimée en SMIC réel et en salaire seul (« cibleSmic »), ou cible soumise elle aussi au gel et à l'assiette (« cibleRef »). Le remplacement complet du barème (« remplacement ») mêle des écarts sous 1,6 SMIC, que la ligne ne vise pas : il n'est pas retenu.

### 1.5 Résultats (variante centrale ; entre crochets, min et max sur 432 combinaisons de paramètres)

| Référence | Recouvrement (retenu) | Cap, cible en SMIC réel | Cap, cible aux règles de la référence |
|---|---|---|---|
| RGDU seule (loi votée, 2027 sans gel) | **0,676** [0,657 ; 0,691] | 0,762 [0,734 ; 0,780] | 0,762 |
| RGDU + gel 2027 | 0,623 [0,588 ; 0,642] | 0,675 [0,627 ; 0,699] | 0,786 [0,745 ; 0,822] |
| RGDU + gel + art. 7 (référence 2027) | **0,574** [0,526 ; 0,600] | 0,608 [0,549 ; 0,638] | 0,760 [0,702 ; 0,809] |

Décomposition (recouvrement, sur 12,1 Md€) : la RGDU obtient déjà 3,9 Md€, le gel 2027 0,6 et l'art. 7 0,6. Il reste 6,9 Md€.

Contrôles : formule de la RGDU (cas-type exact) ; cas-types de l'art. 7 retrouvés à 2-6 % près ; part du gel dans le coût ; part de l'art. 7 au-dessus de 1,6 SMIC entre 26 et 41 % selon le profil (A trouvait 25 à 46 %).

Choix du facteur recommandé : 0,574 arrondi à **0,55**, en penchant vers le bas parce que les définitions « transposition A » de l'agent A (environ 0,52 dans mon modèle, § 2) et « cap, cible en SMIC réel » (0,61) encadrent le recouvrement. Intervalle **[0,45 ; 0,65]** : il couvre l'incertitude des paramètres (0,53-0,60), ces deux définitions et une marge pour la distribution par poste, qui n'est pas publiée. La version « cap aux règles de la référence » (0,76) en est exclue : elle prête à la ligne des gains (par exemple sur le plancher de 2 % jusqu'à 3 SMIC) que le chiffrage de Bozio-Wasmer ne contient pas. Loi votée seule : 0,676, arrondi à **0,65** [0,60 ; 0,75].

## 2. Comparaison avec l'agent A (lu après le § 1)

Bloc « Comparaison avec l'agent A » de la sortie : sans l'art. 7, avec gel = 12,02/12,31.

| Distribution | Référence | Transposition A | Transposition B | Cap Bozio-Wasmer | Recouvrement |
|---|---|---|---|---|---|
| la mienne | RGDU seule | 0,644 | 0,463 | 0,762 | 0,676 |
| la mienne | RGDU + gel | 0,592 | 0,425 | 0,686 | 0,630 |
| bandes de A | RGDU seule | 0,638 | 0,471 | 0,736 | 0,664 |
| bandes de A | RGDU + gel | 0,581 | 0,427 | 0,659 | 0,613 |

Mon modèle reproduit ceux de A (A : RGDU seule, A 0,56-0,63 et B 0,44-0,46 ; avec gel, A 0,51-0,58 et B 0,40-0,42). Les deux calculs s'accordent sur la formule et sur les données. L'écart tient aux choix suivants.

| # | Point | Agent A | Relecture | Le mieux fondé |
|---|---|---|---|---|
| 1 | Cible en 2027 | Transpositions A (RGDU(1,6) linéaire jusqu'à 0 en 1,88) et B (RGDU jusqu'à 1,88 puis 0) ; facteur = moyenne | Barème cible de Bozio-Wasmer tel que chiffré (7,8 % à 1,6, 0 à 1,88), ou recoupement sans cible | **Relecture.** Le 12,1 est le chiffrage de ce barème précis. B est une autre mesure (une marche à 1,88, avec 10,9 % gardés à 1,6) qui pèse à moitié dans le 0,4. A ne vaut que comme variante. |
| 2 | Définition | Rendement restant d'une mesure transposée / rendement 2024 | Part non obtenue par la référence, salaire par salaire (consigne) | **Relecture** : c'est la définition de la consigne, et elle ne demande aucune transposition. |
| 3 | Assiette art. 7 | −3,7 × [0,25 ; 0,46] / 12,1 = −0,08 à −0,14, tout retiré au-dessus de 1,6 | −0,05 (recouvrement) ; −0,07 (cap, SMIC réel) | **Relecture.** Les deux modèles s'accordent sur la part de l'art. 7 au-dessus de 1,6 (25-46 % contre 26-41 %), mais une partie porte sur des salaires où la RGDU est déjà plus généreuse qu'en 2024. Il faut aussi diviser des euros de 2027 par des euros de 2024 (A le signale lui-même) et compter 3,3 plutôt que 3,7 pour l'intéressement et la participation. |
| 4 | Gel 2027 | 12,02/12,31, −0,04 à −0,05 | 0,967-0,976, −0,05 (recouvrement) | Équivalents. Hausse de janvier 2027 non publiée. |
| 5 | Distribution | Effectifs par bandes (Bozio-Wasmer p. 47), uniformes dans la bande, non pondérés par l'EQTP | Déciles Insee en EQTP, resserrés pour retrouver la DSN 2025 (49 % de la masse entre 1 et 2 SMIC) | Relecture un peu mieux fondée (EQTP, calage DSN), mais l'effet est de 0,01 à 0,03 : ce n'est pas un écart majeur. |
| 6 | Barème 2024 | Seuils 2,5 et 3,5 ; Tmax déduit (0,314) | Seuils gelés 2,47 et 3,46 (Bozio-Wasmer p. 46) ; T = 0,3235/0,3195 (taux au SMIC de 40,15 %) | Relecture (valeurs lues), effet négligeable. |
| 7 | Formule RGDU | FNTP (secondaire), Tdelta 0,3781 | Même formule, recoupée par le cas-type primaire de l'annexe 9 ; moyenne 0,3781/0,3821 | Accord ; la relecture fournit la preuve primaire. |
| 8 | Contrôles | Coût RGDU 74-90, cas-types art. 7 à 10 % près, gel | Cas-type exact, cas-types art. 7 à 2-6 %, part du gel, rapports entre bandeaux | Comparables. |
| 9 | Gel 2027 en droit | Question ouverte (lecture de LégiSocial) | Art. 2 du décret : « au titre de l'année 2026 » ; HCFP et annexe 4 traitent le gel 2027 comme une mesure nouvelle (2,9 Md€) | Le gel 2027 est en projet ; à trancher par l'intégrateur. Avec le gel, loi votée = 0,6. |

Points où l'agent A est mieux fondé ou complète la relecture : il chiffre la baisse de 2025, qu'il écarte à juste titre puisque les bandeaux sont supprimés au 1/1/2026 (je ne la compte pas non plus). Il cite la CCSS de mai 2026 (non relue ici). Il signale que la transposition reste un choix de méthode, et qu'un rechiffrage T2 de « RGDU éteinte à 1,88 SMIC » serait préférable.

## 3. Réserves

- Aucune ventilation officielle de la RGDU par niveau de salaire n'est publiée : le facteur reste un modèle. Il serait remplacé par une distribution DSN au pas de 0,01 SMIC (la DSS en dispose, annexe 9 p. 41) ou par un rechiffrage T2.
- Le profil de l'intéressement et de la participation au-dessus de 2 SMIC n'est pas publié (testé de 1,0 à 1,8 fois la moyenne).
- La hausse du SMIC de janvier 2027 n'est pas connue (testée de 0 à environ 1 %).
- Sous 1 SMIC (temps partiel, apprentis), le plafonnement n'est pas modélisé ; sans effet sur la ligne, qui porte au-dessus de 1,6 SMIC.
- Le facteur, calculé en statique avant effets emploi, s'applique au montant retenu de 11,4 Md€, comme le prévoit la note actuelle.
- Rien n'a été modifié dans `data/` ni `scripts/`. La correction éventuelle passe par `scripts/appliquer_corrections.py`, avec une entrée dans `historique.csv`. Les champs concernés sont `facteur_reference`, `_bas`, `_haut`, `facteur_reference_loi_votee` et `note_reference` de `l_bandeaux`, plus `statut_reference_2027.csv` (`l_bandeaux_i`). Il faut aussi vérifier la variante `degel` de `variantes_sensibilite.csv` (0,715 [0,562 ; 0,87]), calculée sur l'ancienne méthode : mon modèle donne 0,63 (RGDU + art. 7, sans gel, recouvrement ; `run(s27=1.0)`, non affiché dans `sortie_modele.txt`).
