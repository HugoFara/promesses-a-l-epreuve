# T10b : calibration des chiffreurs sur les programmes d'Emmanuel Macron (2017 et 2022)

Date d'accès de toutes les sources : 2026-10-14.

Fichiers :
- `calibration_instituts.csv` : 43 lignes (une ligne par couple mesure × chiffreur), dont 22 retenues pour les statistiques ;
- `stats_calibration.py` : calcul des statistiques par chiffreur à partir du CSV (`python3 -I stats_calibration.py`) ;
- `sources.csv` : 41 fichiers archivés dans `sources/T10b/`, avec leur sha256.

## 1. Convention de signe et définition de l'écart

Tous les montants sont des **impacts sur le solde public, en Md€/an** (règle 5 de CONSIGNES.md). Une valeur négative creuse le déficit : une baisse d'impôt chiffrée à 8 Md€ s'écrit −8. Une économie s'écrit avec un signe +.

Les colonnes `chiffrage_campagne` et `cout_realise` suivent cette convention, malgré le mot « coût » dans le nom de la seconde.

**Écart** : `ecart_pct = (réalisé − chiffré) / |chiffré| × 100`.

- **Écart négatif** : la mesure a coûté plus, ou rapporté moins, que prévu. Le chiffrage était trop optimiste pour le solde : c'est le cas défavorable. C'est la même lecture que la couche 2 de HANDOFF.md (réalisé − prévu ; négatif = trop optimiste).
- **Écart positif** : la mesure a coûté moins que prévu. Le chiffreur a été prudent.

Exemple : Montaigne chiffrait la taxe d'habitation à −8 Md€ ; le réalisé est −10,2 Md€. L'écart vaut (−10,2 + 8) / 8 = −27,5 %.

Quand le chiffrage vaut 0 (mesure jugée neutre), l'écart en % n'est pas défini. La ligne est alors gardée dans le CSV mais exclue des statistiques.

Colonnes ajoutées au format demandé : `page_chiffrage`, `page_realise`, `inclus_stats` et `date_acces`. Elles répondent aux exigences de CONSIGNES.md (page, traçabilité) et rendent explicite le choix d'inclusion.

## 2. Résultats par chiffreur

Lignes retenues : `inclus_stats = oui`, même périmètre entre promesse et réalisation, réalisé trouvé.

| Chiffreur | n | Biais moyen (%) | Médiane (%) | Écart-type (pts) | IC 95 % t de Student | IC 95 % bootstrap | Erreur absolue médiane (%) | Lecture |
|---|---|---|---|---|---|---|---|---|
| Institut Montaigne | 8 | −34,3 | −13,8 | 87,8 | [−107,7 ; +39,2] | [−93,2 ; +19,7] | 40,0 | biais non significatif |
| Fondation Concorde | 5 | +4,6 | +3,3 | 28,0 | [−30,2 ; +39,4] | [−18,1 ; +24,4] | 24,0 | biais non significatif |
| OFCE | 5 | +1,8 | −1,9 | 16,8 | [−19,1 ; +22,7] | [−11,1 ; +15,0] | 13,9 | biais non significatif |
| Candidat (En Marche) | 2 | +0,6 | +0,6 | 3,7 | [−33,0 ; +34,3] | n.s. | 2,6 | **n trop petit : aucune conclusion** |
| Fondation iFRAP | 2 | +6,4 | +6,4 | 5,1 | [−39,3 ; +52,1] | n.s. | 6,4 | **n trop petit : aucune conclusion** |
| Tous chiffreurs (lignes non indépendantes) | 22 | −10,4 | +1,4 | 55,9 | [−35,2 ; +14,5] | [−35,2 ; +9,6] | 14,9 | biais non significatif |

Méthode du script :
- **IC t** : moyenne ± t(0,975 ; n−1) × écart-type / √n.
- **IC bootstrap** : percentiles 2,5 et 97,5 de 10 000 rééchantillonnages, graine fixe.
- **Lignes non indépendantes** : la ligne « tous chiffreurs » compte plusieurs fois les mêmes mesures et le même réalisé ; son IC est donc trop étroit.
- **Cas n = 2** : un bootstrap n'a pas de sens, d'où la mention « n.s. » (non significatif) dans le tableau.

### Écarts mesure par mesure

| Mesure | Montaigne | Concorde | OFCE | Candidat | iFRAP | Réalisé (Md€) |
|---|---|---|---|---|---|---|
| Taxe d'habitation 80 % (2017) | −27,5 | −2,0 | −10,9 | −2,0 | | −10,2 |
| ISF → IFI (2017) | −52,6 | +3,3 | −16,0 | +3,3 | | −2,9 |
| IS 33,3 % → 25 % (2017) | 0,0 | −37,5 | −1,9 | | | −11,0 |
| Heures sup., volet salarié (2017) | | +24,0 | +24,0 | | | −1,9 |
| AAH +100 € (2017) | +22,5 | +35,4 | +13,9 | | | −0,775 |
| Emplois francs (2017) | +88,2 | | | | | −0,112 |
| 50 000 postes d'État (2017) | −107,7 | | | | | −0,12 (dérivé) |
| Redevance (2022) | +2,8 | | | | +2,8 | −3,11 (dérivé) |
| Cotisations des indépendants (2022) | −200,0 | | | | +10,0 | −0,9 |

### Sensibilités (sorties complètes du script)

- **Écarts plafonnés à ±100 %** : Montaigne passe à −20,8 % (IC t [−74,0 ; +32,4]) ; les autres chiffreurs ne changent pas.
- **Montaigne sans les emplois francs ni la fonction publique**, soit les mesures fiscales et les prestations : n = 6, −42,5 % (médiane −13,8 %), IC t [−128 ; +43]. Le biais négatif vient de l'ISF, de la TH et des indépendants.
- **Lignes `high` ou `medium` seulement** : Montaigne perd la ligne fonction publique (réalisé dérivé, `low`) et passe à n = 7, −23,8 %, médiane 0,0 %.

## 3. Lecture

1. **Aucun chiffreur ne montre de biais moyen statistiquement établi.** Les intervalles à 95 % contiennent tous 0. Avec n ≤ 8 par chiffreur, le test ne détecte que des biais de plusieurs dizaines de points. **Pour le candidat et l'iFRAP (n = 2), aucune conclusion n'est possible.**

2. **L'Institut Montaigne se distingue par sa dispersion plus que par son biais.** L'écart-type est de 88 points et l'erreur absolue médiane de 40 %. Ses erreurs vont dans les deux sens :
   - côté solde, trop optimiste sur l'ISF (−53 %), la TH (−28 %), les indépendants (−200 %, sur une petite mesure de 0,3 Md€) et les suppressions de postes. Les 50 000 postes promis ont été remplacés par une hausse de 3 825 ETPT à l'État et de 14 672 ETPT chez les opérateurs (Cour des comptes, RBDE 2022, p. 117) ;
   - trop prudent sur les emplois francs (+88 %). Montaigne retenait l'hypothèse du candidat de 150 000 embauches par an ; il y a eu environ 27 000 demandes acceptées en 2022.

   La médiane (−14 %) est plus représentative que la moyenne (−34 %), tirée par deux mesures de moins de 2 Md€.

3. **L'OFCE est le plus précis** : biais de +1,8 %, écart-type de 17 points, erreur absolue médiane de 14 %. Mais tous ses chiffrages datent de juin-juillet 2017, après l'élection et avec les premières annonces du gouvernement (calendrier de la TH, scénario d'IS). Ce ne sont pas des chiffrages de campagne au sens strict ; l'avantage informationnel est réel.

4. **Concorde et le candidat** sont proches du réalisé sur la TH et l'ISF. Mais Concorde reprend sur ces deux lignes le chiffre du candidat (colonnes identiques dans son tableau) : ces lignes ne sont pas des estimations indépendantes. Sur l'IS, chiffrage propre de Concorde, l'écart est de −37,5 %.

5. **Constats par type de mesure** (n très petit, à titre indicatif) :
   - les prestations sociales à barème connu (AAH) ont été **surestimées par les trois chiffreurs** (+14 à +35 %) ;
   - les exonérations de cotisations sur les heures supplémentaires sont surestimées de 24 %, sous réserve du statut du réalisé (point 6) ;
   - les baisses d'impôt concentrées sur le haut de la distribution (ISF) ont été sous-estimées par Montaigne et l'OFCE ;
   - les promesses d'économies (postes, 60 Md€) ne se sont pas matérialisées ou ne sont pas mesurables.

6. **Ordre de grandeur.** L'erreur absolue médiane toutes lignes est de 14,9 %, contre 11,4 % pour les chiffrages gouvernementaux de la couche 1 (HANDOFF.md). Les écarts de calendrier et de documentation entre ces deux ensembles empêchent d'en tirer davantage.

## 4. Choix de périmètre (mesures comparées, exclues ou ajustées)

- **Taxe d'habitation** : comparaison au **même périmètre** (80 % des ménages). Le réalisé est de 10,2 Md€ : le rapport général du Sénat sur le PLF 2022 (p. 48, données DGFiP) écrit « 10,2 milliards d’euros bénéficient aux 80 % de ménages les moins aisés ». L'extension à 100 % (7,8 Md€ de plus) est exclue. La ligne « Dégrèvement 80 % des foyers : 13,7 Md€ en 2020 » de la Cour (NEB 2023 R&D, p. 27) n'a pas été retenue : elle inclut probablement des dégrèvements antérieurs à la réforme, puisque la ligne « plafonnement en fonction du revenu » y tombe à 0,0. C'est une interprétation, non confirmée par le texte.
- **Heures supplémentaires** :
  - la mesure de 2019 exonère les seules cotisations salariales et ajoute un volet IR non promis (réponse à la QE 18138) ;
  - pour l'OFCE et Concorde, on compare donc leur volet salarié (2,5 Md€) au réalisé de 1,9 Md€ ;
  - la fourchette Montaigne (3,3-4,1 Md€), construite sur le dispositif TEPA (cotisations salariales et patronales), est **exclue** des statistiques.
- **50 000 postes d'État** :
  - le réalisé en euros est **dérivé** : variation des ETPT de l'État (+3 825) multipliée par le coût unitaire de Montaigne (1,55 Md€ / 50 000 postes = 31 000 €) ;
  - en ajoutant les opérateurs (+14 672 ETPT jusqu'en 2021), le réalisé passe à −0,57 Md€ ;
  - le volet collectivités (70 000 postes, 1,62 Md€ chez Montaigne) n'a pas été vérifié.
- **Redevance** : réalisé **dérivé**. Il vaut la TVA transférée à l'audiovisuel public en 2022 (3,6 Md€, Cour des comptes, NEB 2023 Recettes fiscales, p. 22), moins les dégrèvements de contribution que l'État remboursait déjà (0,488 Md€, Voies et moyens PLF 2022 cité par Montaigne). L'écart quasi nul est en partie mécanique, car chiffrage et réalisé reposent sur la même assiette.
- **Indépendants** : le réalisé est la compensation par la TVA versée à la Sécurité sociale en 2023 (0,9 Md€, Cour des comptes, NEB 2023 Recettes fiscales, p. 23). On suppose que la compensation égale le coût.
- **Exclus, avec la raison dans la colonne `inclus_stats`** :
  - **PFU** : périmètre de l'OFCE différent ; réalisé très incertain, entre 0 (Fipeco) et 1,4 Md€ au plus (Sénat/IPP : coût surestimé d'au moins 0,5 Md€) ;
  - **prime d'activité** : la réforme de décembre 2018 dépasse le périmètre promis ;
  - **bascule CSG/cotisations** : chiffrage nul ; réalisé de −1,6 Md€ dû à une décision ultérieure (retraités) ;
  - **CVAE** : divisée par deux en 2023, suppression reportée à 2027 ; coût 2023 non isolable dans les documents lus ;
  - **retraites** : 65 ans promis, 64 ans votés ; aucun chiffrage institutionnel à 64 ans ;
  - **droits de succession** : mise en œuvre non vérifiée ;
  - **prime de partage de la valeur**, **ASF +50 %** et **ASPA** : réalisé non trouvé ;
  - **60 Md€ d'économies** : réalisé non mesurable sans contrefactuel.
- **Programmes législatifs 2017 et 2022** : non traités séparément. Le programme Ensemble 2022 chiffré par Montaigne reprend les mesures présidentielles ; l'ajouter compterait deux fois les mêmes lignes.

## 5. Sources des chiffrages

- **Institut Montaigne 2017 et 2022** : le site est protégé par Cloudflare (erreur 403 avec curl). Les pages ont été lues via les **copies de la Wayback Machine** d'avril 2017 (fiches et synthèse du candidat Macron) et de mars-avril 2022 (synthèse et fiches). Les fiches donnent aussi le chiffre du candidat quand il existe (TH 2017 ; CVAE, retraites et successions 2022).
- **OFCE** :
  - policy briefs 18 (TH, 26/06/2017), 19 (PFU), 23 (heures supplémentaires) et 25 (évaluation du programme, 12/07/2017) ;
  - fiches mesures n° 5, 6 et 9 du 12/07/2017 ;
  - ces documents sont **postérieurs à l'élection**.
- **Fondation Concorde** (22/03/2017) : tableau en annexe, p. 14-15, avec une colonne « Coût selon E. Macron ». Concorde n'était pas dans la liste de la consigne ; c'est le seul autre chiffrage ligne à ligne de 2017 trouvé.
- **Fondation iFRAP 2022** : *Société civile* n° 232, tableau p. 14, en texte (aussi archivé en image sur la page web).
- **Candidat** :
  - fiche synthèse Budget En Marche 2017, qui ne donne que des totaux (60 Md€ d'économies, 20 Md€ de baisse de prélèvements) ;
  - programme 2017, sans coût par mesure ;
  - chiffres par mesure lus chez Montaigne, l'OFCE et Concorde, d'où la confiance `medium` quand la source est secondaire.

## 6. Non trouvé, avec les recherches faites

- **Asterès, Terra Nova, Rexecode, Fipeco** (en tant que chiffreurs des programmes Macron 2017 et 2022) : aucun chiffrage par mesure trouvé. Recherches web ciblées pour chacun (« Asterès 2017 chiffrage programmes Macron », « Terra Nova chiffrage programme Macron », « Rexecode 2017 programme Macron chiffrage », « Fipeco 2022 programme Macron chiffrage »).
  - Un article d'Europe 1 attribue à COE-Rexecode un chiffre de 2,8 Md€ sur une exonération de TH « pour les classes moyennes ». L'attribution au programme Macron est douteuse et la source primaire n'a pas été lue : **non retenu**.
  - Fipeco sert ici de source pour le **réalisé** (billet du 27/01/2022, qui cite le RESF du PLF 2022).
- **iFRAP 2017** : comparateur de programmes avec *Le Point* mentionné, mais aucun tableau chiffré du programme Macron 2017 trouvé.
- **IPP 2017** : le chiffre de 11,1 Md€ pour l'IS, attribué à l'IPP par un support de cours, n'a pas été retrouvé chez l'IPP : non retenu.
- **Réalisés manquants** :
  - ASPA +100 € : dépense portée par le FSV ;
  - ASF +50 % ;
  - coût de la prime de partage de la valeur ;
  - coût isolé de la baisse de CVAE en 2023 ;
  - économies des collectivités.
- **Sources primaires inaccessibles** :
  - budget.gouv.fr (403) : RESF et Voies et moyens non lus, d'où la confiance `medium` pour l'IS (11 Md€, RESF cité par Fipeco) ;
  - vie-publique.fr et strategie.gouv.fr (rapports France Stratégie sur l'ISF et le PFU) : bloqués ou introuvables ;
  - senat.fr : inaccessible en direct, lu via la Wayback Machine.
- **Limite d'outil** : le quota de recherches web de la session a été épuisé pendant la collecte des réalisés. Les recherches restantes ont été faites par accès direct aux URL connues : pages de la Cour des comptes, Assemblée nationale, Wayback Machine. Les réalisés de l'ASPA, de l'ASF et de la PPV pourraient être trouvés avec de nouvelles recherches (annexes PLFSS, rapports CCSS, RALFSS).

## 7. Points de vigilance

- **Statut des « réalisés »** :
  - **IS** (11 Md€) et **heures supplémentaires** (1,9 Md€) : chiffrages gouvernementaux de la mesure **telle que votée**, à comportements inchangés, et non des évaluations ex post ;
  - **ISF** (2,9 Md€) : calculé par différence avec l'ISF de 2017. Contre un ISF contrefactuel qui aurait continué de croître, le coût serait plus élevé (voir `data/mesures_cout.csv`) ;
  - **AAH** (0,775 Md€, CNAF via la Cour) et **emplois francs** (0,112 Md€ de CP 2022) : de vrais réalisés.
- **Dépendance des lignes** : les mêmes réalisés servent à plusieurs chiffreurs ; les erreurs ne sont pas indépendantes entre chiffreurs.
- **Petites mesures** : les écarts en % sur les mesures de moins de 1 Md€ (indépendants, emplois francs, AAH) pèsent autant que ceux sur la TH ou l'IS. En euros, l'erreur de Montaigne sur l'ISF (−1,0 Md€) et sur la TH (−2,2 Md€) domine.
- **Calendrier** : les horizons diffèrent (2018 pour l'ISF, 2020 pour la TH et l'AAH, 2022 pour l'IS et les emplois francs, 2023 pour les indépendants). Aucune correction d'inflation ni de croissance de l'assiette n'a été faite.
- **Asymétrie de l'échantillon** : il n'y a que des mesures du candidat élu, et seulement celles mises en œuvre au même périmètre. Les mesures abandonnées ou très modifiées, par nature plus mal chiffrées, sont exclues : biais de sélection probable vers des erreurs plus faibles.

## 8. Décisions laissées à l'intégrateur

1. **Faut-il un facteur de correction par chiffreur ?** Les données ne le justifient pas : aucun biais significatif, n ≤ 8. Elles soutiennent plutôt une **incertitude par ligne** de l'ordre de ±40 % (erreur absolue médiane) quand le point de départ est Montaigne, et de ±15-25 % pour l'OFCE ou Concorde. C'est utile pour T4 (Monte-Carlo) et T6 (sensibilité au chiffreur).
2. **Garder ou non l'OFCE**, dont les chiffrages sont postérieurs à l'élection, dans une calibration « campagne ».
3. **Garder ou non les lignes à réalisé dérivé** : fonction publique, redevance, et PFU (exclu par défaut).
4. **Étendre l'échantillon** pour sortir de n ≤ 8 :
   - campagne 2012 (Hollande : Montaigne et iFRAP avaient chiffré) ;
   - programmes législatifs 2024 au fur et à mesure des réalisations ;
   - recherche des réalisés manquants (ASPA, ASF, PPV, CVAE 2023).
