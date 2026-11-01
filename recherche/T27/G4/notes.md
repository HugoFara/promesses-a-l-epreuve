# T27 G4.4 et G4.5 : solde net avec l'UE, coût d'un centime d'accise

Date d'accès : 01/11/2026. Sources archivées dans `sources/T27/G4/` (voir `sources.csv`). Rien n'a été modifié dans `data/` ni `scripts/`.

`idees_chiffres.csv` n'a pas de colonne `id` unique (la clé est le couple `idee`, `ordre`) et `appliquer_corrections.py` ne connaît pas cette clé. Les changements de ce fichier sont donc décrits ligne par ligne ci-dessous. `corrections_idees.csv` ne contient que les deux textes de `idees.csv` (`ue`, colonnes `resume` et `fiable`), qui ont une clé `id` et sont produits à partir des valeurs actuelles exactes.

## G4.4 Solde net de la France avec l'UE

### Source lue

Jaune « Relations financières avec l'Union européenne », annexé au PLF 2027. Il a été trouvé dans le dossier AN `PLF_2027` (https://www.assemblee-nationale.fr/dyn/17/dossiers/PLF_2027), fichier « 13-Jaune 2027 - Relations financières avec l'Union européenne.pdf », créé le 12/10/2026. Confiance `high` (source primaire, Direction du budget).

### Ce que dit le jaune (partie 3.3, « Le solde net de la France en 2025 »)

- p. 157 : « En 2025, le solde net de la France est estimé à -9,5 Md€ selon la méthode comptable (-0,31 % du RNB) et à -6,4 Md€ selon la méthode de la Commission (-0,21 % du RNB) hors NextGenerationEU. »
- p. 157 : « Le solde net de la France se détériore de -1,7 Md€ selon la méthode comptable et de -1,4 Md€ selon la méthode opérationnelle par rapport à 2024. […] retours français (16,4 Md€ en 2025 contre 16,5 Md€ en 2024), tandis que la contribution française au budget de l'UE (ressources propres traditionnelles incluses) augmente, passant de 24,3 Md€ en 2024 à 25,9 Md€ en 2025 »
- p. 157 : « Les soldes présentés ci-dessous tiennent désormais compte de la méthode comptable, sans prendre en compte en compte les crédits de NextGenerationEU »
- p. 158, tableau « Solde net français de 2000 à 2025 » (M€) :

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Paiements en France | 15 729 | 16 892 | 16 498 | 16 456 | 16 391 |
| Ressources propres versées | 28 109 | 26 476 | 25 831 | 24 330 | 25 865 |
| Solde, méthode comptable | −12 380 | −9 584 | −9 333 | −7 874 | −9 474 |
| Solde, méthode « Commission » | −9 718 | −6 484 | −6 410 | −4 999 | −6 446 |

- Les deux méthodes (p. 156-157). Méthode **comptable** : contribution totale, droits de douane (RPT) compris, moins toutes les dépenses de l'UE en France, administratives comprises. Méthode **de la Commission** (« opérationnelle ») : contribution hors RPT moins les dépenses réparties, hors dépenses administratives.
- p. 91, tableau « Retours français au titre de NextGenerationEU » : total NGEU France 8 873 M€ en 2024 et 2 244 M€ en 2025 ; p. 90 : « En 2025, les retours français au titre de NextGenerationEU représentent 2,2 Md€ ».

« Estimé » : la ligne 2025 est tirée du « rapport financier 2025 » de la Commission (source du tableau p. 158). C'est donc le dernier exercice exécuté connu, et non une prévision.

### Comparaison avec la carte

- La valeur actuelle (−7,9 Md€, 2024) est le solde **comptable** : le jaune 2027 donne −7 874 M€ pour 2024, ce qui la confirme.
- La note actuelle dit « Hors dépenses administratives : 8,4 Md€ » pour 2024. Le jaune 2027 donne −5,0 Md€ (méthode de la Commission) pour 2024. Le 8,4 vient de seconde main (rapport AN sur le PLF 2026) et ne se retrouve pas dans ce tableau : à retirer de la note.
- La consigne parlait de la « convention de la Commission ». Ce n'est pas celle de la valeur actuelle : je propose de garder la méthode comptable (continuité de la série, formule « ce que la France paie de plus qu'elle ne reçoit », droits de douane compris) et de citer la valeur de la Commission dans le texte. **Décision laissée à l'intégrateur** : −9,5 (comptable) ou −6,4 (Commission).

### Changements proposés dans `idees_chiffres.csv`

1. **`ue`, ordre 2** (solde) :
   - `valeur` −7.9 → **−9.5** ; `annee` 2024 → **2025** ; `confiance` medium → **high** ;
   - `url` → jaune PLF 2027 (URL dans `sources.csv`) ; `titre` → « Annexe au PLF 2027, Relations financières avec l'Union européenne (jaune) » ;
   - `citation` → « En 2025, le solde net de la France est estimé à -9,5 Md€ selon la méthode comptable (-0,31 % du RNB) et à -6,4 Md€ selon la méthode de la Commission (-0,21 % du RNB) hors NextGenerationEU » ; `page` → « p. 157 (tableau p. 158) » ;
   - `note` → « T27 G4.4 : jaune PLF 2027, méthode comptable (contribution RPT comprises moins toutes les dépenses en France), hors NextGenerationEU ; tableau p. 158 : −9 474 M€ en 2025, −7 874 en 2024. Méthode de la Commission (hors RPT et dépenses administratives) : −6,4 Md€ en 2025. Versé 25,9 Md€, reçu 16,4 Md€. Moyenne 2021-2025 : −9,7 Md€/an (calcul). Avec les retours NGEU (2,2 Md€) : environ −7,2 Md€ (calcul). »
   - Moyenne 2021-2025 : (12 380 + 9 584 + 9 333 + 7 874 + 9 474) / 5 = 9 729 M€.
2. **`ue`, ordre 3** (dépenses de l'UE en France) : on peut passer à 2025, `valeur` 16.456 → **16.391**, `annee` 2025, avec la même URL du jaune. Citation (p. 64) : « En 2025, les dépenses réalisées en France se sont élevées à 16,4 Md€ (hors crédits du plan de relance NGEU) » ; tableau p. 63, ligne « Total », 16 391 M€. Confiance high. Facultatif : la ligne actuelle (données de la Commission, 2024) reste juste pour 2024, mais l'aligner évite de mélanger 2024 et 2025 sur la carte.
3. `ue`, ordres 1 et 4 : pas de changement.

### Textes de `idees.csv` (dans `corrections_idees.csv`)

- `resume` : le texte actuel rapproche le versement 2027 (31) des retours et du solde de 2024. Or 31 − 16 ne fait pas 8 : les chiffres viennent d'années différentes. Le nouveau texte aligne versé (≈ 26), reçu (≈ 16) et solde (≈ 9,5) sur 2025, et donne le versement 2027 (≈ 31) à part.
- `fiable` : ajoute la valeur de la méthode de la Commission (6,4) et le solde avec le plan de relance pour 2025, qui devient négatif (−9 474 + 2 244 ≈ −7,2 Md€, calcul). Le +1,1 de 2024 est gardé. Le jaune donne +1,0 (−7 874 + 8 873 = +999 M€) ; l'écart vient de la source (données de la Commission dans T16). Le remboursement à partir de 2028 est confirmé p. 12 : « Le remboursement de cet emprunt interviendra à partir de 2028 pour une période maximale de 30 ans. »

## G4.5 Coût d'un centime d'accise sur les carburants

### Chiffrage officiel : rien de récent

J'ai cherché :
- les annexes du PLF 2027 du dossier AN `PLF_2027` : pas de tome I des Voies et moyens dans la liste des fichiers ; les « Évaluations préalables » (743 p.) n'ont aucune occurrence de « centime » liée à l'accise ;
- le rapport général AN n° 3291, tome I (avant-propos) : rien ;
- le guide MTE 2026 sur la fiscalité des énergies (déjà archivé en T16) : pas de rendement par centime ;
- les rapports de la Cour des comptes (mesures énergie 2024) et les autres sources T16 C : pas de chiffre par centime ;
- des recherches web sur Sénat, AN, DGDDI, CPO, avec les formules « un centime », « chaque centime », « par centime » : seulement des amendements de 2015 et une réponse ministérielle de 2005.

Seul chiffrage officiel lu : **réponse du ministère de l'économie** à la question écrite Sénat n° 19774 (JO Sénat du 08/12/2005, p. 3173) : « une baisse de TIPP de 1 centime d'euro/litre sur les grands produits entraîne une baisse des recettes de l'ordre de 60 millions d'euros par mois ». Cela fait environ 0,72 Md€/an (calcul). Ce chiffre n'est **pas utilisable tel quel** : il date de 2005, se fonde sur les volumes de 2005 et porte sur les « grands produits » (fioul domestique probablement compris). Il donne seulement un ordre de grandeur cohérent (quelques centaines de millions par an). Confiance `low` pour 2026.

Les déclarations publiques de 2026 sur le coût de baisses ponctuelles (par exemple « 20 centimes sur un mois, un milliard ») n'ont pas été lues en source primaire et ne sont pas retenues.

### Recoupement du calcul de la carte avec les volumes officiels

- **DGEC, enquête annuelle 2024** (France continentale), tableau I-A « Total des ventes » : « Total carburants 41 797 263 47 764 257 49 043 745 48 050 469 47 733 419 » (m³, 2020 à 2024) ; gazole B7/B10 32 947 130 m³, essences 14 756 094 m³ en 2024 ; « -0,7 % entre 2023 et 2024 » (p. 1). Confiance `high`.
- 47 733 419 m³ × 0,01 €/l = **0,477 Md€/an** (2024). L'Ufip donne 47,5 Mm³ en 2025 (chiffres SDES/CPDP), soit 0,475 Md€. L'écart est de 0,5 % : le calcul de la carte est confirmé par la source officielle. Il n'y a pas encore d'édition 2025 de l'enquête DGEC (URL 2025 en 404, rien trouvé par la recherche).
- Périmètre : « France continentale » exclut les outre-mer (pas d'accise métropolitaine) et, sans doute, la Corse (tarifs propres, faible volume) ; voir le guide MTE 2026, p. 24.
- **Accise brute** (guide MTE 2026, p. 30, d'après Voies et moyens tome I) : 31,6 Md€ en 2024 pour tous les produits pétroliers ; remboursements et dégrèvements 2,0 Md€. Rapportée aux 47,7 Mm³ de carburants routiers, elle fait au plus 0,66 €/l en moyenne : c'est un plafond, puisque le total comprend aussi le fioul et d'autres produits. Ce niveau est du même ordre que les tarifs normaux de 2026 (gazole 60,75, essences 77,647 €/MWh, guide p. 22). La conversion €/MWh → €/l n'a pas été lue dans une source : ce recoupement reste qualitatif. Il confirme seulement qu'un centime vaut environ 1,5 % de l'accise brute, soit environ 0,48 Md€.
- Effets qui réduisent un peu le coût net, déjà notés sur la carte : les tarifs réduits et remboursements (transport routier de marchandises 45,19 €/MWh, taxis, transport collectif, guide p. 24) et la hausse de consommation quand le prix baisse.

### Changement proposé dans `idees_chiffres.csv`

**`carburants`, ordre 1** : garder `valeur` **0.475**, `annee` 2025, `nature` calcul, `confiance` **medium**. C'est un calcul, et aucun chiffrage officiel récent n'existe : `high` ne se justifie pas. Il suffit de compléter `note` :

> « … Recoupé (T27 G4.5) avec les volumes officiels DGEC 2024 (France continentale) : 47,73 Mm³ → 0,477 Md€ (sources/T27/G4/dgec_distribution_petroliere_2024.pdf, tableau I-A, p. 1). Aucun chiffrage officiel récent du coût d'un centime n'a été trouvé (PLF 2027, Évaluations préalables, guide MTE 2026, Cour des comptes) ; le dernier lu date de 2005 : « de l'ordre de 60 millions d'euros par mois » sur les grands produits (réponse ministérielle, JO Sénat 08/12/2005). »

Variante, si l'intégrateur préfère une source publique primaire : `valeur` 0.477, `annee` 2024, `url` DGEC (voir `sources.csv`), `titre` « DGEC, enquête annuelle sur la distribution de carburants en France continentale en 2024 », `citation` « Total carburants … 47 733 419 », `page` « p. 1, tableau I-A (calcul) », confiance medium. La différence à l'affichage est nulle (« environ un demi-milliard »).

`carburants`, ordres 2 à 4 et texte `idees.csv` : pas de changement.

## Points de vigilance

- Le jaune parle de solde « estimé » pour 2025 : ce sont les données du rapport financier 2025 de la Commission. Elles peuvent être un peu révisées l'an prochain.
- Le choix de méthode (comptable ou Commission) fait varier le solde de 3 Md€. Le texte de la carte doit dire laquelle il emploie : c'est ce que fait la nouvelle version de `fiable`.
- La citation et le tableau du jaune ont été lus dans le texte extrait par `pdftotext`. Les numéros de page sont ceux du PDF ; ils coïncident avec les numéros imprimés aux pages 157 et 158.
