# T22, étape 1 (collecte) : RN 2024

Date d'accès : 2026-10-20. Chiffreur de référence : Institut Montaigne. Lignes mères : `rn24_autres_dep` (−21,05) et `rn24_autres_eco` (+1,3). Signe : impact sur le solde, négatif = creuse le déficit.

Fichiers : `lignes_RN.csv` (8 lignes découpées + 2 restes), `autres_chiffreurs_RN.csv` (6 lignes), `sources_RN.csv` (5 nouvelles archives dans `sources/T22/RN/`, 13 archives réutilisées de T17 et T1, sha256 recalculés, identiques).

## 1. Sources lues

- Synthèse Montaigne RN (archive Wayback 17/07/2024, `sources/T17/montaigne_rn_synthese_wb20240717.html`). L'index Wayback donne le même contenu (même empreinte) du 17/07/2024 au 19/01/2026, avec une seule exception, le 25/01/2025 (empreinte différente, non relue). Les listes « Autres mesures » renvoient (« retrouvez le détail ici ») au PDF des micro-chiffrages.
- PDF des micro-chiffrages RN (12/07/2024, `sources/T17/montaigne_rn_micro_chiffrages.pdf`, 9 pages, lu en entier ; page 4 vérifiée sur l'image).
- Il n'existe pas de fiche HTML 2024 pour les « autres mesures ». L'index Wayback de `institutmontaigne.org/legislatives-2024/rassemblement-national/*` ne liste que les fiches des postes principaux.
- Les fiches Montaigne 2022 (programme présidentiel de M. Le Pen) qui portent les mêmes montants ont été archivées pour documenter les méthodes, qui ne sont pas reprises dans le PDF 2024 : PTZ, enseignants, IR des jeunes, IS des jeunes, asile. Elles ne servent pas de montant de découpage.
- Le site institutmontaigne.org n'a pas été consulté en direct (Cloudflare, déjà constaté en T17). Toutes les pages Montaigne viennent de web.archive.org (horodatages dans les noms de fichiers).

## 2. Ce qui a été découpé (seuil : |montant Montaigne| ≥ 1 Md€)

| id | Mesure | Type | Montant | Statut référence 2027 |
|---|---|---|---|---|
| rn24_ptz | PTZ transformé en subvention au 3e enfant | Dépense | −12,6 | absente (mesure voisine proposée : PTZ « parentalité », PLF 2027 art. 7, ≈0,47) |
| rn24_enseignants | Revalorisation du métier d'enseignant | Dépense | −5,8 | absente (point d'indice gelé, mesures catégorielles à 166 M€) |
| rn24_transmissions | Suppression de la fiscalité sur les transmissions de TPE/PME/ETI | Recette | −5,3 | absente (Dutreil restreint par la LFI 2026 art. 8 ; pacte « Papin » proposé, PLF 2027 art. 10) |
| rn24_ir_jeunes | IR supprimé pour les moins de 30 ans | Recette | −3,7 | absente |
| rn24_prisons | Construction des places de prison | Dépense | −1,5 | partielle (plan 15 000 places en cours ; +0,4 Md€ pour la Justice au PLF 2027, non isolé) |
| rn24_apprentissage | Aide supplémentaire à l'apprentissage | Dépense | −1,2 | absente (la référence baisse les aides) |
| rn24_heritage | Impôts sur l'héritage supprimés pour les classes populaires et moyennes | Recette | −1,0 | absente (le PLF 2027 art. 4 porte sur les donations, temporairement) |
| rn24_asile | Réforme de la politique de l'asile | Économie | +1,2 | absente (à confirmer : le pacte européen n'a pas été lu) |

Somme découpée pour `rn24_autres_dep` : −31,10. Pour `rn24_autres_eco` : +1,2.

## 3. Ce qui reste

| Ligne mère | Montant | Découpé | Reste | Part du reste |
|---|---|---|---|---|
| rn24_autres_dep | −21,05 | −31,10 | **+10,05** | −47,7 % (signe opposé) |
| rn24_autres_eco | +1,3 | +1,2 | +0,1 | 7,7 % |

**Le reste des dépenses est de signe opposé à la ligne mère (+10,05), comme la règle § 1.4 le prévoit.** Il est signalé ici, pas corrigé. Il se décompose ainsi :

- postes listés sous le seuil, −2,36 : IS des jeunes créateurs 0,7 ; demi-part des veufs 0,5 ; carte Vitale biométrique 0,4 ; polices municipales 0,3 ; cantines 0,3 ; médecine 0,1 ; contrôles des importations 0,06 ;
- postes à 0 ou « marginal » : assurance chômage (0, déjà isolée à part dans `rn24_chomage`), droit du sol, loi Ciotti, proches aidants, ZFE ;
- écart interne de Montaigne, +12,41 : le bandeau annonce 85 Md€ de dépenses, alors que les postes listés font 63,95 + 33,46 = 97,41. Le bandeau fait foi (T17).

Reste des économies (+0,1) : allocations familiales des parents de mineurs récidivistes (0,002, dans le tableau principal mais pas isolée dans `data/`), plus 0,098 d'écart entre le bandeau (14) et les postes (12,7 isolés + 1,2 + 0,002 = 13,902). L'écart vient des arrondis ; l'audiovisuel compte 2 dans le tableau et 1,6 dans le texte.

## 4. Recouvrements vérifiés (§ 1.6)

Aucune mesure découpée ne recouvre une ligne `rn24_*` déjà isolée. Cas examinés :

- `rn24_heritage` et `rn24_transmissions` contre `rn24_donations` : Montaigne chiffre les trois séparément (successions des classes moyennes ; transmissions d'entreprises, donation et succession ; dons familiaux jusqu'à 100 000 €). L'iFRAP les sépare aussi. Pas de recouvrement de mesure. Le PDF précise toutefois que « les droits de transmission comprennent les droits de donation et de succession ». Une donation d'entreprise familiale pourrait entrer dans les deux mesures ; ce point n'est pas chiffré.
- `rn24_asile` contre `rn24_preference_nationale` et `rn24_ame` : ce sont des mesures différentes. Le groupe « immigration, près de 8 Md€ » de la synthèse vaut 3,8 + 2,6 + 1,2, sans montant de groupe à répartir.
- **`rn24_ptz` contre `rn24_taux` (point pour l'intégrateur).** Ce n'est pas un recouvrement de mesure, donc la mesure est découpée. Mais la fiche 2022 dont vient le 12,6 en compte 7,5 au titre d'un surcoût de spread sur toute la dette publique (« hausse du spread d'un demi-point […] surcoût à l'horizon du quinquennat de 7,5 Md€ »). Ce surcoût est de même nature que la charge d'intérêts `rn24_taux`, calculée par le site sur le solde du programme. Si la ligne PTZ entre dans le solde qui sert à calculer `rn24_taux`, le spread est compté deux fois. Le PDF 2024 ne donne pas de méthode : il n'est pas écrit que le 12,6 de 2024 reprend la décomposition de 2022, seul le montant est identique.

## 5. Écarts internes de Montaigne

1. **Bandeau contre postes listés** : 85 contre 97,41 de dépenses (écart 12,41, voir § 3). C'est la cause du reste positif.
2. **IR des moins de 30 ans** : 3,7 dans la synthèse, 0,7 dans le PDF (p. 2). Selon le PDF, son chiffrage « s'appuie en partie sur le calcul réalisé en 2022 ». Or la fiche 2022 donne 3,7 ; c'est la fiche 2022 de l'IS des jeunes créateurs qui donne 735 M€. Le 0,7 du PDF ressemble donc à une erreur de report, sans que ce soit établi. **Retenu : 3,7 (la synthèse, qui porte la ligne mère).** Avec 0,7, la mesure passerait sous le seuil : la somme découpée serait −27,40 et le reste +6,35.
3. **IS des jeunes créateurs** (non découpé, 0,7) : la page 4 du PDF ajoute « Les coûts pour les finances publiques devraient monter à 4,8 Md€ d'ici 2027, puis à 12 Md€ en 2029 ». C'est mot pour mot le profil de la fiche « hausses de salaire » (0,8 en 2025, 4,8 en 2027, 12 en 2029), probablement collé par erreur. La règle prend le montant de la synthèse (0,7) : la mesure reste dans le reste. Si l'on retenait 4,8 « d'ici 2027 », même horizon que la ligne mère, elle dépasserait le seuil. Point signalé, non tranché.
4. **Asile** : 1,2 en 2024, 1,6 (fourchette 1 à 2,5) dans la fiche 2022 de la même proposition. Le passage de l'un à l'autre n'est pas expliqué ; aucune fiche 2024.
5. **Héritage des classes moyennes (1,0)** : présent dans la synthèse, absent du PDF, aucune méthode. Le montant est pile au seuil : le « au moins 1 Md€ » de la règle le fait découper.
6. **Prisons** : 1,5 « à horizon 2027 », coût d'investissement de 12 000 places étalé sur 3 ans. C'est le seul poste découpé dont l'horizon est écrit.

## 6. Autres chiffreurs (`autres_chiffreurs_RN.csv`)

- **iFRAP (tableau du 26/06/2024)** : PTZ −2,0 ; transmissions −0,7 ; IR des jeunes −3,0 ; petites et moyennes successions −1. Les versions antérieures diffèrent : successions −0,5 le 24/06 ; PTZ et successions absents le 20/06. L'iFRAP ne chiffre ni les enseignants, ni les prisons, ni l'apprentissage, ni l'asile. Son « exécuter l'ensemble des OQTF » (−0,5) est une autre mesure que la réforme de l'asile.
- **Chiffrages partisans** : IR des jeunes, 2 Md€ (J. Bardella, 2022, cité par la fiche Montaigne 2022 et par l'OFCE). Enseignants, 4 Md€ (« montant calculé par le RN » selon l'OFCE, 2022). Pour ce dernier, l'attribution des 4 aux enseignants est déduite de l'ordre des montants, d'où une confiance low. Ces deux chiffres sont à exclure de la sensibilité principale.
- **OFCE, Asterès, La Grande Conversation, Terra Nova, Fipeco** : aucun chiffrage propre de ces mesures pour 2024. Constat de T17, plus deux recherches web le 2026-10-20 (PTZ du 3e enfant ; enseignants et IR des jeunes) qui n'ont renvoyé que des fiches 2022.

## 7. Statut par rapport à la référence 2027 : méthode et limites

Les textes de `sources/T1/` ont été parcourus par mots-clés : PLF 2027 (articles, exposé général, évaluations préalables), PLFSS 2027, LFI 2026, avis HCFP. Seule la ligne `rn24_prisons` est `partielle`, et son facteur n'est pas chiffré (montant 2027 non isolé). Le statut de `rn24_apprentissage` s'appuie sur `recherche/T1/statut_reference.csv` (ligne `e_appr_e`, PAP 2027 Travail, p. 121). Le PAP n'a pas été relu ici. Pour `rn24_asile`, le pacte européen sur la migration et l'asile (applicable en juin 2026 selon une recherche web) et le projet de loi d'habilitation d'avril 2026 n'ont pas été lus : statut à confirmer.

## 8. Décisions laissées à l'intégrateur

1. IR des jeunes : 3,7 (retenu) ou 0,7 (PDF). Ce choix décide si la mesure est découpée.
2. IS des jeunes créateurs : 0,7 (retenu, reste) ou 4,8 « d'ici 2027 » (texte du PDF, probablement erroné).
3. Reste des dépenses positif (+10,05) : il vient de l'écart de 12,41 du bandeau Montaigne. La règle interdit de le corriger. Il faut décider comment l'afficher.
4. PTZ et `rn24_taux` : risque de double compte du spread (§ 4).
5. Statuts `absente` à revoir : PTZ (PTZ « parentalité »), transmissions (pacte Papin), asile (pacte européen).

## 9. Sites inaccessibles ou non lus

- institutmontaigne.org en direct (Cloudflare) : remplacé par Wayback.
- Interview de J. Bardella (IR des jeunes à 2 Md€) : citée de seconde main seulement.
- Pacte européen asile et migration, projet de loi d'habilitation (avril 2026) : non lus.
