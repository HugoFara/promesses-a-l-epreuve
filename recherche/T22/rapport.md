# T22 : découpage des lignes « Autres » des programmes 2024 (fusion)

Fusion faite le 2026-10-20, à partir des collectes de `parts/` (non modifiées). Règle de découpage : `CONSIGNE.md` § 1, appliquée telle qu'écrite. Chiffreur de référence : Institut Montaigne pour les cinq lignes mères. Montants en Md€ par an, signe du solde (négatif = creuse le déficit). Montants mères : `data/raw/application_lignes.csv` (sha256 `6b13f3ff…4b84`, identique au gel du § 0).

## 1. Fichiers produits

| Fichier | Contenu |
|---|---|
| `lignes_decoupees.csv` | 44 lignes : 39 mesures découpées et 5 restes (un par ligne mère), colonnes du § 4 |
| `autres_chiffreurs.csv` | 35 lignes au format de `data/raw/chiffrages_instituts.csv` (NFP 27, RN 6, Ensemble 2) |
| `controle_totaux.csv` | une ligne par ligne mère : montant, somme découpée, reste, écart aux postes listés |
| `sources.csv` | 52 fichiers, dédoublonnés, sha256 recalculés |
| `aveugle/lignes.csv`, `aveugle/familles.csv`, `aveugle/consigne.md` | dossier pour l'attribution des familles (39 lignes) |
| `correspondance.csv` | `id_aveugle` → `id` (hors du dossier `aveugle/`) |

`attribution_agent.csv` n'existe pas encore : il sera produit par l'agent d'attribution (étape 3), colonnes `id_aveugle,famille,famille_nouvelle,justification,issue_connue`, à relier aux `id` par `correspondance.csv`.

Changements faits à la fusion (les fichiers de `parts/` restent tels quels) :

- l'identifiant du reste Ensemble passe de `ens_autres_dep_autres` à `ens_autres_dep_reste`, pour suivre la convention des deux autres programmes (une phrase l'indique dans la `note`) ;
- les deux restes RN avaient un `statut_reference` vide. Ils reprennent le statut de leur ligne mère dans `recherche/T17/statut_reference.csv` (`absente`), comme les restes NFP et Ensemble reprennent celui de T1 ;
- les montants sont écrits sans zéros inutiles (`3.0` → `3`) ;
- la colonne `note` de `sources_RN.csv` (« réutilisée », « nouvelle archive ») n'est pas reprise, puisque le format de `sources.csv` ne l'a pas.

## 2. Par programme

Part du reste = reste / montant de la ligne mère. Elle est négative quand le reste est de signe opposé à la ligne mère.

### NFP 2024

| Ligne mère | Montant | Lignes découpées | Somme découpée | Reste | Part du reste |
|---|---|---|---|---|---|
| `nfp_autres_dep` | −162,7 | 23 | −159,9 | −2,8 | 1,7 % |
| `nfp_autres_rec` | +18,6 | 5 | +19,1 | −0,5 | −2,7 % |

Lignes découpées, par montant (en valeur absolue) :

- **Dépenses** :
  - −20,2 : groupe culture et sport ;
  - −20 : point d'indice +10 % ;
  - −19 : SMIC ;
  - −13,4 : indexation des pensions ;
  - −13 : gratuité de l'école ;
  - −10,5 : indexation des salaires ;
  - −9 : blocage des prix ;
  - −8,8 : taxe sur l'énergie, de type Recette ;
  - −7,3 : AAH ;
  - −6,8 : enseignants ;
  - −5,7 : petite enfance ;
  - −4,6 : soin et médico-social ;
  - −3,5 : avances aux PME ;
  - −2,6 : emplois aidés ;
  - −2,4 : bio ;
  - −2,3 : garantie universelle des loyers (GUL) ;
  - −2,1 : logements publics ;
  - −2,1 : violences sexistes et sexuelles (VSS) ;
  - −1,5 : APL ;
  - −1,3 : asile ;
  - −1,3 : fonds TPE-PME ;
  - −1,3 : logement social ;
  - −1,2 : groupe transports.
- **Recettes** :
  - +6,3 : cotisations sur dividendes ;
  - +6,3 : cotisations vieillesse ;
  - +3 : TTF ;
  - +2,5 : surcotisation ;
  - +1 : taxe kilométrique.

Ce qui reste, et pourquoi :

- **Dépenses (−2,8).** Huit postes sous le seuil, qui font −2,79 :
  - recherche 0,7 ;
  - hôpital (travail de nuit et du week-end) 0,6 ;
  - isolation 0,46 ;
  - PTZ 0,3 ;
  - musées 0,3 ;
  - bâtiments publics 0,2 ;
  - déplacés climatiques 0,13 ;
  - fraude 0,1.

  Ils laissent un écart d'arrondi de −0,01. S'y ajoutent des mesures non chiffrées ou jugées « marginal » ou « imprécis » : assurance chômage, rail, services publics à 30 minutes, formation des policiers, biodiversité, crédit bonifié.
- **Recettes (−0,5).** Aucun poste sous le seuil. Le reste est l'écart entre le bandeau (54, d'où 18,6 pour la ligne) et les postes listés (19,1). Il est de signe opposé à la ligne mère.

Recouvrements écartés : aucun. Les lignes `nfp_retraites` et `nfp_autonomie` (déjà isolées) ne recoupent aucune ligne découpée. Le voisinage avec `nfp_niches` est traité au § 5.3.

### RN 2024

| Ligne mère | Montant | Lignes découpées | Somme découpée | Reste | Part du reste |
|---|---|---|---|---|---|
| `rn24_autres_dep` | −21,05 | 7 | −31,1 | +10,05 | −47,7 % |
| `rn24_autres_eco` | +1,3 | 1 | +1,2 | +0,1 | 7,7 % |

Lignes découpées, par montant (en valeur absolue) :

- **Dépenses et baisses d'impôts** :
  - −12,6 : PTZ transformé en subvention au 3e enfant ;
  - −5,8 : enseignants ;
  - −5,3 : transmissions d'entreprises, de type Recette ;
  - −3,7 : IR des moins de 30 ans, de type Recette ;
  - −1,5 : prisons ;
  - −1,2 : apprentissage ;
  - −1 : héritage des classes populaires et moyennes, de type Recette.
- **Économies** :
  - +1,2 : asile.

Ce qui reste, et pourquoi :

- **Dépenses (+10,05).** Sept postes sous le seuil, qui font −2,36 :
  - IS des jeunes créateurs 0,7 ;
  - demi-part des veufs 0,5 ;
  - carte Vitale biométrique 0,4 ;
  - polices municipales 0,3 ;
  - cantines 0,3 ;
  - médecine 0,1 ;
  - contrôles des importations 0,06.

  Plusieurs postes sont à 0 ou « marginal ». Le reste vient surtout de l'écart de +12,41 entre le bandeau (85) et les postes listés (97,41). Il est de signe opposé à la ligne mère.
- **Économies (+0,1).** Allocations familiales des parents de mineurs récidivistes (0,002) et 0,098 d'arrondis (bandeau 14 contre 13,902 de postes).

Recouvrements écartés : aucun. Trois cas sont examinés au § 5.3 : héritage et transmissions contre `rn24_donations`, asile contre `rn24_preference_nationale` et `rn24_ame`, PTZ contre `rn24_taux`.

### Ensemble 2024

| Ligne mère | Montant | Lignes découpées | Somme découpée | Reste | Part du reste |
|---|---|---|---|---|---|
| `ens_autres_dep` | −11,7 | 3 | −8,9 | −2,8 | 23,9 % |

Lignes découpées :

- −4 : agents publics, hypothèse du chiffreur de +2 points d'indice ;
- −3,6 : SNU ;
- −1,3 : leasing social.

Ce qui reste, et pourquoi : douze postes sous le seuil, qui font −2,911 :

- remplacement des absences 0,7 ;
- logements étudiants 0,6 ;
- complémentaire santé 0,47 ;
- fauteuils roulants 0,4 ;
- congé de naissance 0,4 ;
- retraites agricoles 0,1 ;
- numerus clausus 0,1 ;
- rénovation 0,09 ;
- France services 0,03 ;
- fournitures 0,021 ;
- retraite à 65 ans 0 ;
- effets de seuil, non chiffrés.

Ils laissent un écart de +0,111 avec le bandeau (postes 27,011 contre bandeau 26,9).

Recouvrements écartés : aucun. Aucune ligne Ensemble déjà isolée ne recoupe les trois mesures.

### Comparaison des trois programmes

| Programme | Somme des valeurs absolues découpées | Somme des valeurs absolues des lignes mères | Rapport | Mesures découpées |
|---|---|---|---|---|
| NFP | 179,0 | 181,3 | 98,7 % | 28 |
| RN | 32,3 | 22,35 | 144,5 % (le bandeau RN est sous ses postes) | 8 |
| Ensemble | 8,9 | 11,7 | 76,1 % | 3 |

## 3. Contrôles

| Contrôle | Résultat |
|---|---|
| Identifiants uniques dans `lignes_decoupees.csv` | oui (44) |
| Identifiants déjà dans `data/raw/application_lignes.csv` ou `chiffrages_instituts.csv` | aucun |
| Lignes de `autres_chiffreurs.csv` sans ligne découpée | aucune |
| Colonnes | conformes au § 4 (lignes) et à `chiffrages_instituts.csv` (autres chiffreurs) |
| Montants numériques | oui, tous |
| Seuil de 1 Md€ | respecté : aucune ligne découpée sous 1 en valeur absolue. Deux lignes sont pile au seuil, une NFP (taxe kilométrique, 1) et une RN (héritage, 1) ; « au moins 1 Md€ » les fait découper toutes les deux |
| Retombée sur la ligne mère (tolérance 0,05) | les 5 lignes mères retombent exactement : mère − (découpées + reste) = 0 ; le reste recalculé est égal à celui des collecteurs |
| sha256 | 52 fichiers présents dans `sources/`, 52 empreintes recalculées identiques à celles déclarées, aucun fichier manquant |
| Doublons de sources | 2 fichiers listés par deux collecteurs (`sources/T1/PLF2027_projet_AN3210.html`, `sources/T1/PLFSS2027_projet_AN3211.html`), gardés une fois |
| Sources citées mais non listées | 3, cités par la collecte Ensemble et ajoutés avec l'URL et le titre de `recherche/T6/sources.csv` : `sources/T6/montaigne_ens_synthese_wb20240710.html`, `sources/T6/ifrap_ens_tableau.png`, `sources/T6/ofce_programmes_ensemble.html` |

**Signe par rapport au type** :

- Toutes les lignes `Dépense` découpées sont négatives, et les lignes `Recette` et `Économie` des lignes mères de recettes ou d'économies sont positives.
- Quatre lignes sont typées `Recette` mais négatives : ce sont des baisses d'impôt, rangées par Montaigne dans « dépenses et baisses d'impôts ». Elles diffèrent donc aussi du type de leur ligne mère (`Dépense`).

  | id | Programme | Montant |
  |---|---|---|
  | `nfp_taxe_macron` | NFP | −8,8 |
  | `rn24_transmissions` | RN | −5,3 |
  | `rn24_ir_jeunes` | RN | −3,7 |
  | `rn24_heritage` | RN | −1 |

  Le signe suit la convention du solde ; c'est la même convention que les lignes isolées existantes (`ens_notaire`, `rn24_tva_*`, etc.).
- Deux restes ont un signe opposé à leur type : `nfp_autres_rec_reste` (Recette, −0,5) et `rn24_autres_dep_reste` (Dépense, +10,05). C'est voulu par le § 1.4 (voir § 5.1).

**`controle_totaux.csv`.** La colonne `ecart_postes_listes` est le reste moins la somme des postes que Montaigne liste sous le seuil, en signe du solde. C'est la part du reste qui ne correspond à aucun poste publié.

| Ligne mère | Reste | Postes listés | Écart non expliqué |
|---|---|---|---|
| NFP dépenses | −2,8 | −2,79 | −0,01 |
| NFP recettes | −0,5 | 0 | −0,5 |
| RN dépenses | +10,05 | −2,36 | +12,41 |
| RN économies | +0,1 | +0,002 | +0,098 |
| Ensemble | −2,8 | −2,911 | +0,111 (France services comptée en coût) |

## 4. Écarts internes de Montaigne relevés par les collecteurs

| Programme | Mesure | Écart | Montant retenu |
|---|---|---|---|
| NFP | Total des dépenses | Postes listés 232,99, bandeau 233 | bandeau |
| NFP | Total des recettes | Postes 54,5, bandeau 54 (d'où le reste de −0,5) | bandeau |
| NFP | Indexation des pensions | Fiche : 6,6 en 2025, 3,4 en 2026, 3,4 en 2027, « soit 13,4 Md€ sur trois ans » (en tête de fiche : « Coût en 2025 » 6,6). Synthèse : 13,4 en coût par an | 13,4 (synthèse) |
| NFP | Blocage des prix | Fiche 24 (fourchette 9-38), synthèse 9 (borne basse) | 9 (synthèse) |
| NFP | TTF | Fiche 9,3, synthèse 3 (connu depuis T6) | 3 (synthèse) |
| NFP | Asile | Fiche : aucun montant, chiffrage jugé impossible. Synthèse et PDF : 1,3, calculé sur la condition de résidence de 5 ans / 30 mois de la loi de 2024 | 1,3 (synthèse) |
| NFP | Cotisations vieillesse et cotisations sur dividendes | La carte « 0,25 point » du PDF (p. 15) chiffre en fait la mesure sur les dividendes (1,7 + 4,57) ; aucune méthode propre aux 0,25 point | 6,3 et 6,3 |
| NFP | Bio | Le texte du PDF conclut à 0,1 de revalorisation ; synthèse 2,4 | 2,4 (synthèse) |
| RN | Total des dépenses | Postes listés 97,41, bandeau 85 (−12,41) | bandeau |
| RN | Total des économies | Postes 13,902, bandeau 14 ; audiovisuel 2 dans le tableau, 1,6 dans le texte | bandeau |
| RN | IR des moins de 30 ans | Synthèse 3,7, PDF 0,7 (le 0,7 ressemble à une erreur de report du 0,735 de l'IS des jeunes de 2022, non établi) | 3,7 (synthèse) |
| RN | IS des jeunes créateurs | Synthèse 0,7. Le PDF (p. 4) ajoute « 4,8 Md€ d'ici 2027, puis 12 Md€ en 2029 », profil identique à celui d'une autre fiche, probablement collé par erreur | 0,7 (reste) |
| RN | Asile | 1,2 en 2024, 1,6 (1 à 2,5) dans la fiche 2022 ; passage non expliqué | 1,2 (synthèse) |
| RN | Héritage | Montant 1,0 dans la synthèse, absent du PDF, sans méthode | 1 (synthèse) |
| RN | PTZ 3e enfant | Montant 12,6, identique à la fiche 2022, dont 7,5 sont un surcoût de spread sur toute la dette ; le PDF 2024 ne donne pas de méthode | 12,6 (synthèse) |
| Ensemble | Total des dépenses | Postes 27,011, bandeau 26,9 ; le texte dit aussi « 25 Md€ sur 3 ans » et « près de 27 Md€ » | bandeau |
| Ensemble | Leasing social | Coût total 1,3 ; la fiche dit aussi « soit 650 M€ additionnels pour 2025 » | 1,3 (synthèse) |
| Ensemble | Agents publics | 4 = hypothèse de Montaigne (2 points d'indice), « non précisée dans le programme » ; pas de fiche | 4 (synthèse) |
| Ensemble | SNU | Campagne : 1,4 « dont 0,3 Md€ déjà prévus dans la trajectoire » ; Montaigne 3,6 (1,9-5,4) sans retrancher les 0,3 | 3,6 (synthèse) |
| Ensemble | Retraites agricoles | Encadré 0,1 « à horizon 2027 » ; texte : « 0,1 Md€ en 2027 et 1 Md€ à horizon 2027 » | 0,1 (reste) |
| Ensemble | France services | Synthèse : coût de 30 M€ ; PDF : « −0,03 Md€ » (signe ambigu) | reste |

Les trois collectes ont retenu la même convention, sans s'être concertées : **le montant de la synthèse**, celui qui compose le bandeau. Le montant de la fiche ou du PDF est donné en note.

## 5. Décisions laissées à l'intégrateur

Rien n'est tranché ici. Pour chaque question, les options et leur effet sur le découpage, la ligne mère restant fixe (§ 1.4 de la consigne, `check_regression.py`). Une option qui change le montant d'une ligne découpée déplace la différence dans le reste.

### 5.1 Restes de signe opposé à la ligne mère

| Ligne mère | Reste | Origine |
|---|---|---|
| `rn24_autres_dep` | **+10,05** | bandeau 85 contre postes listés 97,41 (+12,41), moins 2,36 de petits postes |
| `nfp_autres_rec` | −0,5 | bandeau 54 contre postes 54,5 |

Options, les mêmes pour les deux lignes :

- (a) **Afficher le reste tel quel**, comme une seule ligne « Autres ».
- (b) **Le scinder en deux lignes de même total** :
  - les postes listés sous le seuil (RN −2,36 ; NFP 0) ;
  - « écart entre le bandeau et les postes du chiffreur » (RN +12,41 ; NFP −0,5).

  Appliquée aux cinq lignes mères, l'option (b) donne aussi NFP dépenses −2,79 et −0,01, RN économies +0,002 et +0,098, Ensemble −2,911 et +0,111.
- (c) **Corriger le bandeau.** La consigne l'exclut (§ 1.4) : le total « indépendant » ne doit pas changer.

### 5.2 Montant de la synthèse ou montant de la fiche

| Programme | Mesure | Synthèse (retenu) | Autre montant publié | Effet de l'autre montant |
|---|---|---|---|---|
| NFP | Blocage des prix | 9 | 24 (fiche, médiane) | découpées −174,9 ; reste dépenses **+12,2** (signe opposé) |
| NFP | TTF | 3 | 9,3 (fiche) | découpées recettes 25,4 ; reste recettes **−6,8** |
| NFP | Indexation des pensions | 13,4 (cumul sur 3 ans) | 3,4 (fiche, coût 2027) ou 6,6 (fiche, coût 2025, en tête) | reste dépenses −12,8 (avec 3,4) ou −9,6 (avec 6,6) |
| NFP | Bio | 2,4 | 0,1 (texte du PDF) | sous le seuil : la ligne retourne au reste, qui passe à −5,2 |
| RN | IR des moins de 30 ans | 3,7 | 0,7 (PDF) | sous le seuil : découpées −27,40, reste **+6,35** |
| RN | IS des jeunes créateurs | 0,7 (reste) | 4,8 « d'ici 2027 » (PDF, probablement erroné) | découpée : découpées −35,90, reste **+14,85** (avec IR des jeunes à 0,7 : reste +11,15) |
| Ensemble | Leasing social | 1,3 | 0,65 additionnels (fiche) | sous le seuil : découpées −7,6, reste **−4,1** (35,0 %) |
| Ensemble | Retraites agricoles | 0,1 (reste) | 1 « à horizon 2027 » (texte du PDF) | découpée : découpées −9,9, reste −1,8 |

Options, les mêmes pour les trois programmes :

- (a) **Synthèse partout** : c'est l'état des fichiers.
- (b) **Fiche partout où elle diffère** : on cumule les effets ci-dessus. Les restes deviennent :
  - NFP dépenses : −2,8 + 15 (blocage) − 10 (pensions à 3,4) − 2,4 (bio) = −0,2, ou +3,0 avec les pensions à 6,6 ;
  - NFP recettes −6,8 ;
  - RN dépenses +6,35, ou +11,15 avec l'IS des jeunes ;
  - Ensemble −4,1, puis −3,1 avec les retraites agricoles.

  Ces cumuls supposent chaque fois l'autre montant publié ; ils dépendent du montant choisi pour les pensions et du sort de l'IS des jeunes.
- (c) **Au cas par cas, selon un critère écrit d'avance.** Par exemple : « le montant de la fiche quand la synthèse reprend une borne ou un cumul ». Ce critère toucherait le blocage des prix, les pensions et le leasing. Un critère choisi après avoir vu les effets ne serait pas neutre.

Dans tous les cas, le montant d'un autre chiffreur ne sert pas au découpage (§ 1.5).

### 5.3 Doubles comptes possibles

| Programme | Cas | Options et effet |
|---|---|---|
| NFP | **Deux lignes à 6,3** (cotisations vieillesse et cotisations sur dividendes) : le PDF chiffre la première avec la méthode de la seconde | (a) garder les deux (reste recettes −0,5) ; (b) ne pas découper les cotisations vieillesse : reste recettes **+5,8** |
| NFP | **Indexation des salaires (10,5) et point d'indice +10 % (20)** : deux hausses du point que Montaigne additionne | (a) garder les deux (reste −2,8) ; (b) ne pas découper l'indexation : reste **−13,3**. Les règles s'appliquent à l'une comme à l'autre ; la question porte sur le double compte, pas sur le total |
| NFP | Cotisations sur dividendes, participation, heures supplémentaires et `nfp_niches` (médiane iFRAP / LGC) : périmètres voisins | aucun recouvrement avec la ligne Montaigne ; à vérifier si les niches de l'iFRAP comprennent ces exemptions d'assiette |
| RN | **PTZ (12,6) qui inclut, d'après la fiche 2022, 7,5 de surcoût de spread sur la dette**, de même nature que `rn24_taux` (−1,2, calculé par le site sur le solde du programme) | (a) garder 12,6 tel quel (risque de double compte si le PTZ entre dans le solde qui sert à `rn24_taux`) ; (b) garder 12,6 et retirer cette ligne de l'assiette de `rn24_taux` ; (c) n'en garder que la part hors spread (5,1) : c'est une décomposition de 2022, non republiée en 2024, donc hors de la règle § 1.1. Avec (c), le reste RN passerait à **+2,55** |
| RN | Héritage (1) et transmissions (5,3) contre `rn24_donations` (1) : une donation d'entreprise familiale peut entrer dans deux mesures | non chiffré, mesures séparées chez Montaigne et chez l'iFRAP ; pas d'option chiffrable |
| Tous | **Résidus des autres chiffreurs** : chaque résidu de `chiffrages_instituts.csv` contient déjà les montants que `autres_chiffreurs.csv` rattache aux lignes découpées | voir le tableau ci-dessous |

Si l'on rattache les montants aux lignes découpées sans les retirer des résidus, ils sont comptés deux fois dans la fourchette entre chiffreurs.

| Résidu dans `chiffrages_instituts.csv` | Valeur | Rattaché aux lignes découpées | Résidu après retrait |
|---|---|---|---|
| iFRAP `nfp_autres_dep` | −133,3 | −88,92 (14 lignes) ; plus la composante SMIC −4 si elle est dans le résidu | −44,38 (ou −40,38) |
| iFRAP `nfp_autres_rec` | +13,3 | +11,5 | +1,8 (retour en cotisations du SMIC) |
| La Grande Conversation `nfp_autres_rec` | +7,5 | +7,5 | 0 |
| Asterès `nfp_autres_dep` | −159,9 | −30,9 | −129,0 |
| iFRAP `rn24_autres_dep` | −9,95 | −6,7 | −3,25 |
| iFRAP `ens_autres_dep` | −2,36 | −1,76 (SNU, leasing) | −0,60 |

Les lignes OFCE (point d'indice, −23) et Asterès (TTF, 3, montant du parti) existent déjà dans `chiffrages_instituts.csv` comme composante ou recette du parti de la ligne mère : il ne faut pas les ajouter deux fois. Les chiffrages partisans (Rabault, RN 2022) sont à exclure de la fourchette principale, pour les deux partis de la même façon.

### 5.4 Mesures à risque juridique ou à base fragile

- **NFP asile (1,3).** La fiche juge le chiffrage impossible. Le 1,3 de la synthèse repose sur la condition de 5 ans de la loi de 2024, qu'une décision du Conseil constitutionnel du 11 avril 2024 a jugée disproportionnée (rappel de l'exposé des motifs de l'art. 37 du PLFSS 2027). Options :
  - (a) garder 1,3 ;
  - (b) ne pas le découper : reste −4,1 ;
  - (c) le découper et laisser l'agent d'attribution choisir la famille, puis signaler la fragilité dans la page.

  La même question vaut, dans l'autre sens, pour **RN asile (+1,2)** : la fiche 2022 donnait 1,6, le passage à 1,2 n'est pas expliqué, et le pacte européen sur la migration et l'asile n'a pas été lu (statut à confirmer). Si l'on écarte NFP asile pour base fragile, il faut examiner RN asile avec le même critère. L'écarter remettrait les +1,2 dans le reste RN économies, qui passerait à +1,3.
- **Ensemble agents publics (4)** et, dans une moindre mesure, **RN héritage (1, sans méthode)** : montants que le chiffreur pose sur une hypothèse non précisée par le programme. La règle les découpe ; leur fragilité est à dire de la même façon.

### 5.5 Lignes de groupe

Montants publiés pour plusieurs mesures sans détail (§ 1.3) :

| Programme | Ligne | Montant | Contenu |
|---|---|---|---|
| NFP | `nfp_culture_sport` | −20,2 | culture à 1 % du PIB et sport à 1 % du budget de l'État ; le PDF cite les dépenses 2022 sans ventiler le coût |
| NFP | `nfp_transports` | −1,2 | tarifs et gratuité ciblée (dépense) et TVA à 5,5 % (baisse de recette), sans montant par composante |

Options :

- (a) **Une ligne par groupe**, une famille pour le tout : c'est l'état des fichiers. Le groupe transports mêle une dépense et une baisse de TVA ; la famille choisie à l'aveugle s'appliquera aux deux.
- (b) **Les remettre dans le reste** : reste −23,0 sans la culture et le sport, −4,0 sans les transports, −24,2 sans les deux.

Les collectes RN et Ensemble n'ont trouvé aucune ligne de groupe. Le même critère s'appliquerait si l'on en trouvait.

Deux mesures uniques se décomposent chez Montaigne. Elles ne sont pas des groupes, et la décision reste ouverte de la même façon :

- **SMIC (−19)** : allègements −21,5, masse salariale publique −3,7, prélèvements +6. La famille `smic_cout_direct` et la règle « Effet emploi du SMIC » (`smic_effet_emploi`) sont séparées dans `familles.csv`. Si l'agent choisit `smic_cout_direct`, il faut décider s'il faut une ligne d'effet emploi pour ce programme. Aucune autre ligne SMIC n'existe dans les programmes 2024.
- **Gratuité de l'école (−13)** : médiane non ventilée, alors que la fiche détaille 14,3 dans l'hypothèse public + privé.

### 5.6 Statut par rapport à la référence 2027

Tout est `absente`, sauf `rn24_prisons` et `ens_leasing`, qui sont `partielle` (facteur non chiffré).

Plusieurs mesures ont dans la référence une mesure voisine, ou de sens inverse, proposée et non votée :

| Programme | Mesure | Mesure de la référence |
|---|---|---|
| NFP | Pensions | sous-indexation, PLFSS 2027 art. 35 |
| NFP | APL | gel des APL, PLF 2027 art. 74 |
| NFP | Asile | condition d'un an de résidence, PLFSS art. 37 |
| NFP | Cotisations sur dividendes | intéressement et PPV, PLFSS art. 7 |
| NFP | SMIC | gel du SMIC de référence de la RGDU |
| NFP | Point d'indice et indexation des salaires | gel du point d'indice |
| Ensemble | Agents publics | gel du point d'indice |
| RN | PTZ 3e enfant | PTZ « parentalité », PLF 2027 art. 7, 0,47 |
| RN | Transmissions | pacte « Papin », PLF 2027 art. 10 |
| RN | Asile | pacte européen, non lu |

À décider de la même façon pour les trois programmes : faut-il garder `absente`, ou traiter ces mesures avec la famille `annulation_economie_reference` ? Pour le leasing, il faut aussi savoir si un dispositif financé par les CEE compte en dépense publique, ce qui n'a pas été vérifié.

### 5.7 Horizons hétérogènes

Toutes les lignes ne sont pas annuelles à l'horizon 2027 :

| Ligne | Horizon publié |
|---|---|
| `nfp_taxe_macron` | « en 2025 » |
| `ens_leasing` | « 2025 » |
| `ens_snu` | à partir de 2026 |
| `nfp_indexation_pensions` | cumul sur 3 ans |
| `nfp_indexation_salaires` | 3 ans d'indexation cumulés |

C'est l'horizon de la synthèse dont vient la ligne mère ; la règle n'y touche pas. Une harmonisation passerait par un autre chiffrage, ce qui est hors de la règle.

### 5.8 Attribution à l'aveugle

- `aveugle/familles.csv` ne garde que `famille`, `libelle` et une colonne `champ`. Les justifications de `data/raw/familles.csv` décrivent presque toutes le traitement (« Montant mécanique », « Élasticité… », « médiane… »). Elles nomment donc la règle ou la laissent deviner. Seuls deux champs sont gardés, réécrits sans la règle :
  - `annulation_economie_reference` : « Rétablir une indexation ou un point d'indice gelés dans la référence 2027 » ;
  - `effet_promis` : « Exemples : fraude, égalité salariale, rétention… ».

  La consigne T22 (§ 3) prévoyait de transmettre la justification ; ce choix, plus strict, suit la demande de fusion.
- Deux libellés ont été reformulés pour retirer une mention qui identifie le parti ou le chiffreur :
  - `nfp_taxe_macron` : « Abolir la « taxe Macron » de 10 % sur les factures d'énergie (TICFE) » devient « Supprimer la taxe de 10 % sur les factures d'énergie (accise sur l'électricité, TICFE) » ;
  - `ens_agents_publics` : « (hypothèse Montaigne : … ) » devient « (hypothèse du chiffreur : … ) ».

  Les autres libellés sont repris tels quels. Certains restent reconnaissables par leur contenu (SMIC à 1 600 €, loi asile et immigration, SNU, PTZ au 3e enfant, IR des moins de 30 ans) : la colonne `issue_connue` le mesurera.
- Ordre : alphabétique sur le libellé, sans accents ni casse ; identifiants A01 à A39.

## 6. Ce qui n'a pas été fait ou lu (rappel des collectes)

- web.archive.org était hors service le 2026-10-20 pour la collecte NFP : aucune archive nouvelle n'a été faite pour ce programme.
- Fiches Montaigne inexistantes : NFP enseignants, petite enfance, GUL, logements, cotisations vieillesse ; RN, aucune fiche 2024 pour les « autres mesures » ; Ensemble agents publics.
- Documents non lus :
  - pacte européen asile et migration, projet de loi d'habilitation d'avril 2026 (RN asile) ;
  - arrêté du 14/04/2026 sur le leasing social (cité par la presse) ;
  - PAP 2027 Sport, jeunesse et vie associative (SNU) ;
  - interview de J. Bardella (IR des jeunes à 2 Md€, de seconde main).
- La fusion n'a fait aucune recherche web.

## 7. Attribution à l'aveugle : résultat (ajouté par l'intégrateur, 20/10/2026)

L'agent a travaillé sans web, sur une copie de `aveugle/` hors du dépôt. Son fichier est copié tel quel dans `attribution_agent.csv` (sha256 `03c1fe4da453ca90b6dd1584b198123c6e676ce8e6a1d77679d9d6f5f0333af8`) ; `correspondance.csv` relie `id_aveugle` aux identifiants.

- **39 lignes** : 20 dans 11 familles existantes, 19 dans 9 familles nouvelles proposées (`credits_sectoriels` 4, `politique_migratoire` 2, `aides_logement` 2, `gratuite_service_public` 2, `aides_transition_ecologique` 2, `revalorisation_prestation` 2, `emplois_aides`, `taxe_transactions_financieres`, `taxe_importations`). Le champ proposé pour `credits_sectoriels` contient « justice des femmes », formulation que l'agent signale lui-même comme maladroite (il visait la lutte contre les violences faites aux femmes) ; il n'est pas retouché.
- **`issue_connue` = oui pour 23 lignes sur 39.** Le test n'est donc aveugle qu'en partie, surtout pour les mesures du NFP, comme en T18.

Règle que reçoit chaque ligne d'après `data/raw/familles.csv` (familles nouvelles : pas encore de règle), en Md€ :

| Programme | Aucune | Élasticité électricité | Élasticité revenus | Élasticité succession | Famille nouvelle |
|---|---|---|---|---|---|
| NFP 2024 | −76,4 | −8,8 (`nfp_taxe_macron`) | | | −55,6 |
| RN 2024 | −8,5 | | −3,7 (`rn24_ir_jeunes`) | −6,3 (`rn24_transmissions`, `rn24_heritage`) | −11,4 |
| Ensemble 2024 | −4,0 | | | | −4,9 |

Points pour l'intégrateur, en plus du § 5 :

1. **Familles nouvelles** : elles portent 82 Md€ des 220 Md€ découpés (en valeur absolue), soit 37 %. Leur règle est à fixer d'après `regles.csv`, avant de regarder l'effet sur chaque programme, et la même pour tous. Les deux mesures d'asile (NFP et RN) sont dans la même famille, `politique_migratoire`, ce qui rejoint l'issue #5 (risque juridique).
2. **Cohérence avec les lignes existantes** : `nfp_taxe_macron` tombe dans `taxe_electricite_gaz`, comme `ens_elec` ; les transmissions et l'héritage RN dans `succession`, comme `nfp_succession`, `ens_succession` et `rn24_donations` ; l'IR des jeunes dans `impot_revenu`, comme `rn24_part_fiscale`.
3. **SMIC** : `nfp_smic` est en `smic_cout_direct` (règle « Aucune »). L'effet emploi (`smic_effet_emploi`, règle « Effet emploi du SMIC ») n'existe aujourd'hui que dans les paniers 2027 (`l_smic_emploi`). Ajouter une ligne d'effet emploi au programme NFP 2024 serait une décision de méthode : la prendre pour toute hausse du SMIC, quel que soit le programme.
4. **Contrôle de l'agent** : `cotisations_sociales_taux` pour les cotisations vieillesse et la surcotisation, `exoneration_remuneration` pour la mise à cotisation des dividendes et heures supplémentaires. Les deux familles ont la règle « Aucune » : le choix ne change pas le chiffre.

## 8. Intégration (20/10/2026)

Décisions prises avec l'utilisateur, appliquées de la même façon aux trois programmes :

1. **Familles nouvelles** : ajoutées à `data/raw/familles.csv`, avec leur règle fixée d'après la nature de la mesure, avant le calcul des programmes. Huit reçoivent « Aucune » (montants budgétaires ou mécaniques) ; `taxe_importations` reçoit « Nouvelle assiette : risque juridique », comme les autres impôts sur une assiette jamais appliquée. `politique_migratoire` reste à « Aucune » en attendant l'issue #5 (la règle de risque juridique ne vise aujourd'hui que les impôts).
2. **Restes** : chaque ligne mère garde un reste `*_reste` (postes non découpés). Quand l'écart entre le total publié et la somme des postes atteint la tolérance de 0,05 Md€, il devient une ligne à part `*_ecart` : RN dépenses +12,41, NFP recettes −0,5, Ensemble +0,11, RN économies +0,098. Total de chaque ligne mère inchangé.
3. **Montant de la synthèse** partout ; le montant de la fiche Montaigne est cité dans la justification quand il diffère (blocage des prix, TTF, indexation des pensions, IR des jeunes, leasing).
4. **Effet emploi du SMIC** : ligne `nfp_smic_emploi` (statique −1, règle « Effet emploi du SMIC »), comme `l_smic_emploi` du panier LFI 2027. La hausse du coût (`hausse_moy_smic`) était déjà calculée sur le SMIC de 2024 (T13), base du chiffrage Montaigne : mêmes paramètres. Cette ligne n'entre pas dans le chiffrage de départ (site, `check_regression.py`, `sensibilite.py`).

**Autres chiffreurs** (`chiffrages_instituts.csv`) : valeurs de `autres_chiffreurs.csv` ajoutées, sauf deux doublons (OFCE point d'indice, Asterès TTF), dont les lignes existantes sont rattachées à `nfp_point_indice` et `nfp_ttf`. Les résidus sont diminués des montants rattachés (§ 5) et rattachés au reste. Pour l'iFRAP et Asterès sur les dépenses NFP, le résidu est « total publié − lignes isolées » : il couvre aussi les lignes découpées que ces chiffreurs ne chiffrent pas à part, marquées `dans_residu` (valeur 0) pour que la lecture « complété » ne les remplisse pas une seconde fois. Les autres résidus sont des listes explicites : rien n'est marqué.

**Sensibilité au chiffreur** (`scripts/sensibilite.py`) : un écart `*_ecart` n'est jamais reporté sur un autre chiffreur ; un reste ne l'est que depuis un chiffreur dont le résidu ne couvre pas aussi les lignes découpées.

**Effets** :

| | Avant | Après |
|---|---|---|
| Indépendant (NFP, Ensemble, RN) | −149,9 ; −18,0 ; −63,6 | inchangé |
| Corrigé, moteur, central (NFP, Ensemble, RN) | −159,4 ; −25,6 ; −60,3 | −159,8 ; −25,6 ; −59,3 |
| NFP, fourchette P10-P90 | −202,2 à −104,1 | −193,0 à −115,9 |
| Écart entre chiffreurs indépendants, avant correction (NFP ; Ensemble ; RN) | 17,8 ; 16,0 ; 43,4 | 5,6 ; 12,0 ; 36,1 (voir ci-dessous) |

- RN : +1,0 par les élasticités des baisses d'impôt découpées (IR des jeunes, transmissions, héritage).
- NFP : taxe Macron (élasticité électricité), taxe kilométrique (risque juridique) et effet emploi du SMIC (−0,5) se compensent presque.
- La fourchette NFP se resserre : l'erreur de chiffrage est tirée ligne par ligne (une part commune au chiffreur, une part propre à chaque ligne), et la grosse ligne unique est devenue trente lignes. C'est le traitement des autres lignes ; la largeur de la fourchette dépend donc du niveau de détail.
- L'écart entre chiffreurs NFP double : La Grande Conversation ne chiffre que des recettes, et ses dépenses sont remplies ligne par ligne par la médiane des autres. Avant, la ligne mère était remplie d'un bloc par la médiane de −162,7, −133,3 et −159,9 (−159,9) ; après, par les médianes de chaque ligne découpée et par le seul reste Montaigne (−2,8). Les mesures que seul l'iFRAP compte dans son résidu (chômage, kWh gratuits, gaz…) ne sont plus reportées. Autre choix possible : la médiane des restes Montaigne et iFRAP (−23,6), qui reporterait une partie de ces mesures au risque de compter deux fois celles que l'iFRAP range aussi dans son résidu.

Restent ouverts : la part « allègements » du coût du SMIC par rapport à la référence 2027 (le panier LFI 2027 la retire, gel du SMIC de référence ; la ligne `nfp_smic` la garde, statut `absente`, comme la ligne mère avant) ; la base fragile des deux mesures d'asile (issue #5).

**Décision complémentaire (20/10/2026)** : l'écart entre chiffreurs ne compte plus que les chiffreurs qui publient un solde total pour le programme (`scripts/sensibilite.py`, statut « partiel, sans total publié » sinon), la même règle pour tous les programmes. La Grande Conversation, qui ne chiffre que des recettes, reste dans le tableau mais sort de l'écart : son solde « complété » était surtout reconstitué par nous, et l'écart passait de 17,8 à 34,5 Md€ selon la seule façon de remplir le reste. Écart NFP entre Montaigne et l'iFRAP : 5,6 Md€ avant correction, 13,3 après (10,3 et 9,0 avant le découpage). Le reste est toujours reconstitué depuis le seul reste Montaigne.
