# Inventaire des mesures ménages : NFP (programme 2024)

Date d'accès : 20/10/2026. Fichier : `inventaire_nfp_2024.csv` (42 lignes). Sources : `sources_inventaire_nfp.csv`. Méthode : celle de `inventaire_notes.md` (RN et Ensemble), reprise sans changement.

## 1. Sources et accès

- Comme pour le RN et Ensemble, le site de l'Institut Montaigne bloque `curl` (Cloudflare). Toutes les pages ont été lues **via web.archive.org**. Aucune autre source n'a été utilisée.
- Synthèse NFP : captures du 08/07/2024 (celle de T6) et du 25/07/2024. Le texte est le même (diff fait). La seule différence est le lien « retrouvez le détail ici » vers les micro-chiffrages, ajouté le 25/07. C'est le même cas que pour Ensemble.
- Fiches : la synthèse renvoie à 12 fiches, toutes archivées, y compris celles des deux mesures exclues (superprofits, déplacé climatique). S'y ajoute la fiche « asile et immigration », présente dans l'archive sans lien depuis la synthèse ; elle est citée. Pour chaque fiche, on a pris la capture la plus proche du 25/07/2024, comme l'autre agent.
- PDF « Synthèses des micro-chiffrages » du NFP : 17 pages, créé le 12/07/2024, cité par page. Il est en deux colonnes. Deux citations (gaz et RSA, p. 2) ont été vérifiées sur l'extraction `pdftotext -layout`, car l'extraction simple mélange les colonnes.
- Fiche SMIC : la version archivée est celle qui a été « actualisée le 24 juin ». Le 20/06, elle annonçait 3,5 Md€. Ce chiffre ne sert pas ici.
- Colonne `url` : l'adresse d'origine sur institutmontaigne.org. Elle renvoie à la fiche quand il y en a une, sinon à la synthèse.
- Toutes les citations du CSV ont été vérifiées par script sur le texte archivé (espaces normalisés).

## 2. Règle d'inclusion, appliquée au NFP

C'est la règle du § 2 de `inventaire_notes.md`, sans changement.

**Découpage des mesures groupées.** Les citations du programme NFP reprises par Montaigne regroupent souvent plusieurs mesures en une seule ligne, ce qui n'est pas le cas pour le RN et Ensemble (leurs citations ne portent qu'une mesure chacune ; vérifié dans le PDF RN). Pour respecter l'exhaustivité (T15 § 0), chaque mesure ménages d'une citation a sa propre ligne quand sa catégorie diffère :
- **Retraites** (fiche) : âge légal ; trimestres validés au RSA ; minimum contributif ; minimum vieillesse.
- **« Taxe Macron »** (PDF p. 2) : accise ; gaz ; premiers kWh ; frais bancaires ; RSA.
- **Transports** (synthèse) : TVA ; gratuité ciblée.
- **Cotisations** (synthèse) : cotisations vieillesse ; cotisations patronales.
- **Flat tax et exit tax** (fiche) : PFU ; exit tax.
- **Point d'indice** (PDF p. 1) : point d'indice ; stagiaires et apprentis.

Sans ce découpage, il y aurait 31 lignes au lieu de 42. Si l'intégrateur préfère une ligne par intitulé Montaigne, il faut le dire sur le site, car les comptes par catégorie changent.

**Mesures exclues** (non listées dans le CSV) :
- superprofits ;
- impôt Zucman ;
- avances à 0 %, fonds de solidarité et crédit bonifié pour les PME-TPE ;
- bio et agroécologie ;
- emplois aidés pour les associations ;
- embauche d'enseignants ;
- 500 000 places en crèche ;
- 200 000 logements publics par an ;
- logement social (HLM) ;
- culture et sport à 1 % ;
- loi sur les violences sexistes et sexuelles ;
- recherche ;
- rénovation des bâtiments publics ;
- recrutements contre la fraude ;
- rail et fret ;
- services publics à moins de 30 minutes ;
- formation des policiers ;
- postes dans les organismes de biodiversité ;
- statut de déplacé climatique ;
- fin des coupures d'électricité, de chaleur et de gaz (PDF p. 2) : cette mesure ne change ni un prix ni un revenu.

**Cas discutables** :
- **Crèches** : elles baissent le coût de garde des familles qui obtiennent une place, mais c'est une offre nouvelle (comme les logements étudiants d'Ensemble). De plus, les enfants de la grille ont 4, 7 et 10 ans. Si l'intégrateur l'inclut : `hors_grille`.
- **Emplois aidés** : c'est une aide aux employeurs associatifs. Si l'intégrateur l'inclut : `canal_entreprises`.

## 3. TVA et taxes sur l'énergie : taux fixé ou non

L'exception « prix » de T15 (version 0.2) ne vaut que si le programme fixe un taux ou une variation de prix pour l'électricité, le gaz, le fioul ou les carburants. Aucune mesure NFP n'est `calculable_prix`.

- **« Taxe Macron » (accise sur l'électricité)** : `canal_prix`. Citation : « Abolir la “taxe Macron” de 10% sur les factures d’énergie ». Le programme ne donne pas le tarif d'accise visé.
  - Le « 10 % » décrit la taxe, pas la baisse ni le tarif.
  - « factures d’énergie » ne dit pas si le gaz est concerné.
  - Montaigne y voit la TICFE (« La TICFE a été abaissée pendant la crise ukrainienne ») et chiffre seulement le fait de ne pas faire la « dernière hausse attendue pour début 2025 ». Il ne donne aucun tarif.
  - Deux lectures sont donc possibles : une baisse de 10 % des factures, ou le gel de l'accise à un tarif que ni le programme ni Montaigne ne donnent.

  **C'est le principal cas limite.** La lecture de Montaigne repose sur le même instrument que la mesure d'Ensemble classée `calculable_prix` (accise maintenue au tarif réduit). Mais pour Ensemble, la fiche donnait les deux tarifs (21 € et 32 € le MWh). Les documents NFP n'en donnent aucun. Reprendre les tarifs de la fiche Ensemble ferait entrer dans le calcul du NFP une source extérieure à son programme. L'autre option est de lire « 10 % » comme une baisse de prix fixée et de classer la mesure `calculable_prix`, avec −10 % sur l'électricité. Décision laissée à l'intégrateur. Il faut alors retraiter Ensemble avec la même exigence.
- **Blocage des prix** (alimentation, énergie, carburants) : `canal_prix`. Citation : « Bloquer les prix des biens de première nécessité dans l’alimentation, l’énergie et les carburants par décret ». Un blocage ne fixe ni taux ni niveau de prix : son effet dépend de la hausse qu'il empêche. Ce classement est conforme au journal de T15 (« NFP inchangé (gel des prix : reste `canal_prix`) »).
- **Hausse du gaz au 1er juillet annulée** : `canal_prix`. Citation : « annuler la hausse programmée du prix du gaz au 1er juillet ». L'ampleur de la hausse n'est donnée ni par le programme ni par Montaigne. La mesure est en outre datée de juillet 2024.
- **Gratuité des premiers kWh** : `canal_prix`. Citation : « faire la gratuité des premiers KwH ». Ni le nombre de kWh ni l'énergie visée ne sont fixés.
- **TVA sur les transports en commun à 5,5 %** : `canal_prix`, bien que le taux soit fixé. Citation : « baisser la TVA sur la tarification des transports en commun à 5,5 % », avec un taux actuel de 7 % (PDF p. 7). Les transports collectifs ne sont pas dans la liste de l'exception (électricité, gaz, fioul, carburants). Si l'exception est un jour élargie aux transports, ce serait la seule mesure NFP sur les prix dont le taux est fixé.

## 4. Autres cas limites

- **SMIC à 1 600 € net** (`calculable_openfisca`, déjà calculé `smic_1600`) : la fiche suppose une hausse « en euros constants », ce que le programme ne dit pas. T15 § 6 retient le montant écrit, en euros courants : c'est ce que fait `smic_1600`.
- **Suppression du PFU** (`calculable_openfisca`, déjà calculé `fin_pfu`) : l'exit tax, rétablie dans la même phrase, est sur une ligne à part (`canal_patrimoine`).
- **Indexation des pensions sur les salaires** (`imprecise`) : l'indice n'est pas précisé, et l'effet ne se voit pas en statique. On pourrait aussi la classer `hors_grille`, comme l'indexation sur l'inflation du RN et d'Ensemble (classée `hors_grille`, car déjà en vigueur). Ici la règle changerait, d'où `imprecise`.
- **Minimum vieillesse au seuil de pauvreté** (`imprecise`) : la fiche donne deux valeurs (1 058 € puis 1 041 € pour une personne seule). Il reste à voir si le retraité seul à 900 € bruts de la grille y aurait droit : à vérifier dans OpenFisca si la mesure est un jour précisée.
- **Minimum contributif au SMIC** (`hors_grille`) : il dépend de la carrière, que la grille ne décrit pas.
- **Garantie d'autonomie** (`hors_grille`) : la synthèse dit « jeunes ». La citation du programme dans le PDF (p. 2) dit « ménages situés sous le seuil de pauvreté (accessible dès 18 ans […]) ». Si elle s'adressait à tous les ménages pauvres, elle toucherait des foyers de la grille et serait `imprecise` (montant non fixé). La classification actuelle (« Jeunes adultes ») suit la synthèse.
- **Cotisations vieillesse + 0,25 point par an** (`imprecise`) : la hausse est fixée, mais pas sa répartition entre salarié et employeur. Dans le PDF (p. 15), le titre de cette mesure est placé au-dessus du texte d'une autre (cotisations sur les dividendes) : c'est une erreur de mise en page de la source.
- **Taxe sur les transactions financières** (`canal_patrimoine`) : elle est incluse parce qu'elle est payée à l'achat d'actions, y compris par des ménages, comme les droits de mutation d'Ensemble. On pourrait aussi l'exclure comme impôt sur la finance.
- **Taxe kilométrique sur les importations** (`canal_prix`) : c'est une taxe sur la consommation, répercutée dans les prix. `canal_entreprises` serait aussi défendable.
- **Réformes du RSA** (`imprecise`) : les réformes visées ne sont pas nommées. Si elles portent seulement sur l'accompagnement, la mesure est `hors_grille`, comme le versement à la source d'Ensemble.
- **Loi asile et immigration** (`hors_grille`) : son coût vient des prestations des étrangers récemment arrivés (PDF p. 5). Elle est classée comme les mesures RN sur les prestations des étrangers.
- **Salaires des agents publics et assimilés** (point d'indice, soin et médico-social, travail de nuit à l'hôpital, stagiaires et apprentis) : tous `hors_grille`, comme les enseignants (RN) et les agents publics (Ensemble).

## 5. Écarts avec les 7 lignes NFP de `non_chiffre_foyer.csv`

| Ligne actuelle | Inventaire | Écart |
|---|---|---|
| 1. Retraite à 60 ans | `canal_retraite_age` | Aucun. La fiche y ajoute trois mesures, sur 3 lignes : trimestres validés au RSA (`canal_retraite_age`), minimum contributif (`hors_grille`), minimum vieillesse (`imprecise`). |
| 2. Garantie d'autonomie | `hors_grille`, « Pas encore simulé » | Aucun, mais voir § 4 (le mot « ménages » dans le PDF). |
| 3. Point d'indice + 10 % | `hors_grille`, « Pas encore simulé » | Aucun. |
| 4. Gel des prix des produits de première nécessité | `canal_prix` | Le programme dit « bloquer » et vise aussi l'énergie et les carburants. Le texte affiché (« Effet sur les prix non calculable avec ce simulateur ») diffère de la formule commune « Passe par les prix : non calculée ». |
| 5. Impôt sur le revenu à 14 tranches et CSG progressive | `imprecise` | Aucun. |
| 6. Cotisations retraite + 0,25 point par an | `imprecise` | Le site affiche « Pas encore simulé », ce qui laisse croire que la mesure est calculable. Or la répartition entre salarié et employeur n'est pas fixée : il faudrait afficher « Pas assez précise pour être calculée ». La modulation des cotisations patronales est sur une ligne à part (`canal_entreprises`). |
| 7. ISF rétabli et droits de succession réformés | 2 lignes `canal_patrimoine` | Une ligne actuelle devient deux mesures distinctes dans la synthèse (ISF climatique ; successions dorées). |

Les 7 lignes actuelles et les 2 mesures calculées couvrent 10 des 42 lignes de l'inventaire. Les 32 autres manquent. Exemples :
- l'AAH, les APL, l'indexation des pensions et celle des salaires ;
- la gratuité de l'école ;
- la « taxe Macron » ;
- la TVA sur les transports ;
- les cotisations sur les dividendes et les heures supplémentaires ;
- la surcotisation des hauts salaires ;
- l'exit tax et la taxe sur les transactions financières ;
- les mesures sur le gaz, les kWh et les frais bancaires.

Ce constat confirme le § 3 de `inventaire_notes.md`.

## 6. Comptes par catégorie (42 lignes)

| Catégorie | Lignes |
|---|---|
| `calculable_openfisca` | 2 (SMIC à 1 600 € net, suppression du PFU, toutes deux déjà calculées) |
| `calculable_prix` | 0 |
| `hors_grille` | 14 |
| `imprecise` | 9 |
| `canal_prix` | 7 |
| `canal_patrimoine` | 4 |
| `services` | 3 |
| `canal_retraite_age` | 2 |
| `canal_entreprises` | 1 |

## 7. Pour l'intégrateur

1. Trancher la « taxe Macron » (§ 3) : `canal_prix` ou `calculable_prix` avec −10 % sur l'électricité. Appliquer la même exigence à Ensemble.
2. Valider le découpage des mesures groupées (§ 2). C'est la principale différence de forme avec l'inventaire RN et Ensemble.
3. Corriger le texte affiché pour les cotisations à + 0,25 point, et scinder la ligne ISF et successions (§ 5).
4. Double codage (T15 § 8.2) : non fait ici, un seul codeur.
