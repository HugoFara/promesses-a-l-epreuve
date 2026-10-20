# T22, collecte NFP 2024 (LFI) : `nfp_autres_dep` et `nfp_autres_rec`

Date d'accès : 2026-10-20. Chiffreur de référence : Institut Montaigne. Fichiers : `lignes_NFP.csv` (28 lignes découpées et 2 restes), `autres_chiffreurs_NFP.csv` (27 lignes), `sources_NFP.csv`.

## 1. Sources lues

Grille suivie : la synthèse, puis chaque fiche mesure et le PDF de détail qu'elle cite.

- **Synthèse NFP.** Archive T6 (Wayback 20240708183027). Le site direct répondait normalement le 2026-10-20, sans défi Cloudflare, et je l'ai archivé (`sources/T22/NFP/montaigne_nfp_synthese_live.html`). Le texte est identique à l'archive de 2024, à un ajout près : deux liens « retrouvez le détail ici » vers le PDF des micro-chiffrages.
- **PDF « Synthèses des micro-chiffrages – NFP ».** 17 pages, détail des « Autres mesures ». Archive T20 (`sources/T20/integration/nfp_microchiffrages.pdf`), dont le sha256 est identique au PDF en ligne le 2026-10-20. Je ne l'ai donc pas recopié.
- **Fiches mesures.** J'ai relevé la liste des fiches sur le site direct (`montaigne_nfp_liste_fiches_live.html`) : 14 fiches. J'ai lu les archives T20 pour le SMIC, l'indexation des pensions, la gratuité de l'école, l'indexation des salaires, le blocage des prix, l'AAH, les APL et l'asile, et les archives T6 pour la TTF. Les mesures suivantes n'ont **pas de fiche** et leur montant vient de la seule synthèse : enseignants, petite enfance, garantie universelle des loyers (GUL), 200 000 logements, cotisations vieillesse.
- **web.archive.org.** Hors service le 2026-10-20 (« Temporarily Offline », CDX en 429). Aucune archive nouvelle n'a été faite ; seules les archives T6 et T20 existantes ont servi.

## 2. Ce qui est découpé

### `nfp_autres_dep` (−162,7) : 23 lignes, somme −159,9

| id | Mesure | Montant |
|---|---|---|
| nfp_culture_sport | Groupe culture à 1 % du PIB et sport à 1 % du budget de l'État | −20,2 |
| nfp_point_indice | Point d'indice +10 % | −20,0 |
| nfp_smic | SMIC à 1 600 € net | −19,0 |
| nfp_indexation_pensions | Retraites indexées sur les salaires | −13,4 |
| nfp_gratuite_ecole | Gratuité intégrale à l'école | −13,0 |
| nfp_indexation_salaires | Salaires indexés sur l'inflation | −10,5 |
| nfp_blocage_prix | Blocage des prix de première nécessité | −9,0 |
| nfp_taxe_macron | « Taxe Macron » sur l'énergie (TICFE), de type Recette | −8,8 |
| nfp_aah | AAH au niveau du SMIC | −7,3 |
| nfp_enseignants | Enseignants (taille des classes) | −6,8 |
| nfp_petite_enfance | 500 000 places en petite enfance | −5,7 |
| nfp_soin_medicosocial | Soin et médico-social | −4,6 |
| nfp_avances_pme | Avances à 0 % aux PME-TPE | −3,5 |
| nfp_emplois_aides | Emplois aidés | −2,6 |
| nfp_bio | Bio et agroécologie | −2,4 |
| nfp_gul | Garantie universelle des loyers | −2,3 |
| nfp_logements_publics | 200 000 logements publics par an | −2,1 |
| nfp_vss | Loi intégrale contre les violences sexistes et sexuelles | −2,1 |
| nfp_apl | APL +10 % | −1,5 |
| nfp_asile | Abrogation de la loi asile et immigration | −1,3 |
| nfp_logement_social | Logement social (HLM) | −1,3 |
| nfp_fonds_tpe_pme | Fonds de solidarité TPE-PME | −1,3 |
| nfp_transports | Groupe tarifs et gratuité ciblée + TVA à 5,5 % sur les transports | −1,2 |

### `nfp_autres_rec` (+18,6) : 5 lignes, somme +19,1

| id | Mesure | Montant |
|---|---|---|
| nfp_cotis_vieillesse | Cotisations vieillesse +0,25 point par an | +6,3 |
| nfp_cotis_dividendes | Cotisations sur dividendes, participation, heures supplémentaires… | +6,3 |
| nfp_ttf | TTF renforcée | +3,0 |
| nfp_surcotisation | Surcotisation sur les hauts salaires | +2,5 |
| nfp_taxe_kilometrique | Taxe kilométrique sur les produits importés | +1,0 |

## 3. Ce qui reste

- **`nfp_autres_dep_reste` = −2,8**, soit **1,7 %** de la ligne mère. Il couvre huit postes sous le seuil, qui font 2,79 au total :
  - PTZ 0,3 ;
  - déplacés climatiques 0,13 ;
  - loi de programmation de la recherche 0,7 ;
  - travail de nuit et du week-end à l'hôpital 0,6 ;
  - isolation 0,46 ;
  - musées 0,3 ;
  - bâtiments publics 0,2 ;
  - fraude 0,1.

  L'écart de 0,01 est un arrondi (postes listés 232,99 pour 233). Les autres mesures sont non chiffrées, ou jugées « marginal » ou « imprécis » : assurance chômage, rénovation thermique, rail, services publics à 30 minutes, formation des policiers, postes biodiversité, crédit bonifié PME-TPE.
- **`nfp_autres_rec_reste` = −0,5**, soit **−2,7 %** de la ligne mère. Ce reste négatif est voulu par § 1.4 :
  - le bandeau donne 54, d'où un résidu de 18,6 pour la ligne ;
  - les postes listés de la ligne font 19,1, et tous les postes de recettes 54,5 ;
  - aucun poste de recettes sous le seuil n'est listé.

  Je l'ai signalé sans le corriger.

## 4. Groupes (non répartis, § 1.3)

- **Culture et sport (20,2).** Le PDF cite les dépenses de 2022 (sport 14,662 ; culture 18,343) mais ne ventile pas le coût. La ligne reste un groupe.
- **Transports (1,2).** Une dépense et une baisse de TVA. Le PDF donne des formules, mais pas de montant par composante. La ligne reste un groupe.
- **Gratuité de l'école (13).** C'est une seule mesure, avec une seule fiche. La fiche détaille 8,7 + 3 + 2,6 = 14,3 dans l'hypothèse public + privé, mais le 13 retenu est une médiane non ventilée.
- **SMIC (19).** C'est une seule mesure, dont les composantes publiées sont : allègements −21,5, masse salariale publique −3,7, prélèvements obligatoires +6. Elle n'est pas découpée plus finement.
- **Taxe Macron (8,8).** La citation du programme englobe aussi le gaz, les kWh gratuits, les frais bancaires, les coupures et le RSA. Montaigne ne chiffre que la TICFE.

## 5. Recouvrements vérifiés (§ 1.6)

- **Avec `nfp_retraites`.** Cette ligne couvre l'abrogation, l'âge, le minimum contributif (MICO), le minimum vieillesse et la validation du RSA. Ni l'indexation des pensions (13,4) ni les cotisations vieillesse (recette) ne la recoupent.
- **Avec `nfp_autonomie` (12,3).** Elle est déjà isolée et exclue des 162,7 : rien n'est découpé deux fois.
- **Avec `nfp_niches`.** Cette ligne est une médiane iFRAP / LGC, alors que Montaigne ne chiffre pas les niches. Les cotisations sur dividendes et heures supplémentaires sont des exemptions d'assiette sociale, de périmètre voisin mais distinct. Pas de recouvrement avec la ligne Montaigne ; je le signale à l'intégrateur.
- **Recouvrements internes à Montaigne (signalés, non corrigés).**
  - Indexation des salaires (10,5, appliquée au point d'indice) et point d'indice +10 % (20) : Montaigne additionne les deux.
  - Les deux lignes à 6,3 : voir § 6.

Aucune ligne n'a été écartée pour recouvrement.

## 6. Écarts internes de Montaigne

1. **Pensions.** La fiche donne « 13,4 Md€ sur trois ans » (6,6 / 3,4 / 3,4), la synthèse l'inscrit en coût par an.
2. **Blocage des prix.** Fiche : 24 (fourchette 9-38). Synthèse : 9,0, la borne basse.
3. **TTF.** Fiche : 9,3. Synthèse : 3,0. L'écart était déjà connu en T6.
4. **Asile.** La fiche juge un chiffrage impossible et ne donne aucun montant ; la synthèse et le PDF donnent 1,3, calculé sur la condition de 5 ans / 30 mois de la loi de 2024. Or l'exposé des motifs de l'article 37 du PLFSS 2027 rappelle que le Conseil constitutionnel (11 avril 2024) a jugé une durée de cinq ans disproportionnée : la base du chiffrage est fragile.
5. **Cotisations vieillesse et cotisations sur dividendes (6,3 chacune).** Dans le PDF (p. 15), la carte titrée « 0,25 point de cotisations vieillesse » cite et chiffre en fait la mesure « dividendes, participation… » (heures supplémentaires 1,7 + 4,57). Aucune méthode propre aux 0,25 point n'est publiée. Double compte possible ; les deux lignes sont découpées par la règle.
6. **Bio (2,4).** Le texte du PDF conclut à « 0,1 Md€ » de revalorisation, sans expliquer le passage à 2,4.

**Convention retenue partout : le montant de la synthèse**, celui qui compose les 233 et les 54. Les montants des fiches sont donnés en note.

## 7. Statut par rapport à la référence 2027

Tout est `absente`. Pour plusieurs mesures, la référence contient une mesure proposée **de sens inverse**, qui alourdit l'écart :

| Mesure | Mesure de la référence (proposée) |
|---|---|
| Pensions | PLFSS 2027, art. 35 : sous-indexation des pensions |
| APL | PLF 2027, art. 74 : gel des APL, −0,10 |
| Asile | PLFSS 2027, art. 37 : condition d'un an de résidence |
| Cotisations sur dividendes | PLFSS 2027, art. 7 : régime de l'intéressement et de la participation préservé, régime de la PPV pérennisé ; allègements corrigés de 3,7 |
| SMIC | gel du SMIC de référence de la RGDU (décret n° 2026-509, prolongation proposée en 2027, voir T1 l_smic_i) : la part « allègements » des 19 est probablement surestimée |

Pour les mesures sans vérification propre, le statut reprend la ligne mère de T1 (« Aucune des dépenses […] n'est dans la référence »), comme l'indique la note de chaque ligne.

## 8. Autres chiffreurs

| Chiffreur | Mesures |
|---|---|
| iFRAP (tableau du 27/06/2024) | 18 lignes (somme de deux lignes iFRAP pour culture + sport et pour les transports) |
| Asterès | point d'indice 22 (coût unitaire repris de Fipeco), école 7,6, APL 1,3, TTF 3 (montant du parti) |
| OFCE | point d'indice 23 |
| La Grande Conversation (LGC) | TTF 4, taxe kilométrique 3,5 (points milieux) |
| V. Rabault (PS), partisan | logements 10, « salaires » 23 |

Non repris :
- OFCE, SMIC : 0,3 point de PIB, sans montant en Md€ ; une conversion aurait été un calcul ;
- camp présidentiel, point d'indice 20 : non retrouvé dans les articles archivés relus ;
- iFRAP, SMIC : périmètre limité à la fonction publique (4), saisi en `composante`.

## 9. Sites inaccessibles ou lacunes

- **web.archive.org** était hors service le 2026-10-20, ce qui a empêché de nouvelles archives et la recherche CDX.
- **institutmontaigne.org** était accessible en direct le 2026-10-20.
- **Pas de fiche Montaigne** pour 5 mesures découpées (enseignants, petite enfance, GUL, 200 000 logements, cotisations vieillesse) : leur montant vient de la synthèse seule.
