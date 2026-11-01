# G6.3 : calibration des instituts, réalisés manquants (T10b point 4, T21 § 4)

Date : 01/11/2026. Rien n'est modifié dans `data/` ni `scripts/`. Sources archivées dans `sources/T27/G6/calibration/` (liste et sha256 dans `sources.csv`).

Fichiers :

- `lignes_proposees.csv` : les 14 lignes de `data/raw/calibration_instituts.csv` à modifier, avec leurs nouvelles valeurs (`inst_NN` = rang de la ligne, comme dans `scripts/validation.py`) ;
- `variantes.py` : calcul de `erreur_ligne` pour chaque variante (`python3 -I recherche/T27/G6/calibration/variantes.py data/raw/calibration_instituts.csv`) ;
- `sources.csv`.

**Pourquoi pas `appliquer_corrections.py`.** Le script cherche la ligne par la colonne `id` (sauf trois fichiers listés dans `CLES`). `calibration_instituts.csv` n'a pas de colonne `id`. Les changements sont donc donnés ligne par ligne (§ 3), à appliquer à la main avec une entrée par valeur dans `historique.csv`. Autre option : ajouter `calibration_instituts` à `CLES` avec une clé composée. Cela modifie `scripts/` et revient à l'intégrateur.

## 1. Résultats par mesure

Convention de T10b : les montants sont des impacts sur le solde, en Md€/an. L'écart vaut (réalisé − chiffré) / |chiffré|.

| Mesure | Réalisé (année) | Source primaire | Confiance | Même périmètre ? | Proposition |
|---|---|---|---|---|---|
| ASPA +100 €/mois (2017) | −0,752 (2020), borne basse −0,592 | CCSS juillet 2022, fiche 3.7, p. 141 et 137 ; calcul | medium | oui | **entre** (Montaigne −50,4 %, OFCE −25,3 %) |
| ASF +50 % (2022) | −1,1 (2023) | CCSS mai 2024, p. 98 (aussi p. 16 et 100) | high | oui | **entre** (Montaigne −22,2 %) |
| PPV, plafond triplé (2022) | non publié | CPO, octobre 2024, p. 57 | high (pour l'absence) | — | reste exclue |
| Suppression de la CVAE (2022) | non mise en œuvre (report à 2030) | Service public Entreprendre (DILA), mise à jour du 30/03/2026 | high | non | reste exclue, motif à corriger |
| Heures sup. 2012 (fin de TEPA) | +4,486 (calcul ; IR 2011 et social 2011-2013) | PLFSS 2024 annexe 4, p. 27 ; AN n° 2172, p. 58 | medium | oui pour le candidat et Terra Nova ; non pour Montaigne | verdict interne « oui » (−2,5 %) ; Montaigne « non » (+46,6 %) |
| Emplois d'avenir 2012 | −1,32 (CP 2015) | Sénat, avis n° 143 (2016-2017), t. VIII, p. 27 | medium | candidat : oui, sous réserve ; Montaigne et iFRAP : non | verdict interne candidat « oui » (+34,0 %) |
| Abattement de succession à 100 000 € (2012) | non trouvé | — | — | — | inchangé |
| Carrières longues, décret de 2012 | non trouvé | — | — | — | inchangé |
| Doublement de la TTF (2012) | non isolé | — | — | — | inchangé |

### ASPA (lignes `inst_19` Montaigne −0,5 et `inst_20` OFCE −0,6)

- Source : CCSS, *Les Comptes de la Sécurité sociale*, juillet 2022, fiche éclairage 3.7, tableau 4 (p. 141) : « Au total, 592 M€ supplémentaires ont été versées en Aspa ou ASV, du fait des revalorisations exceptionnelles 2018-2020 ». Ce montant porte sur 2020, première année où la hausse est complète. La Cnav l'a obtenu avec son modèle Prisme, contre un scénario où le minimum vieillesse « aurait été revalorisé comme les prix entre 2018 et 2020 » (encadré 4). Les 46 000 nouveaux éligibles sont compris.
- Limite écrite par la source (p. 141) : « ce modèle ne permet pas de connaître l’impact sur des bénéficiaires n’ayant aucun droit au RG, les chiffres présentés sont donc inférieurs à l’impact global de la mesure ».
- **Calcul** pour passer à tous les régimes : 592 × 3 530 / 2 780 = 752 M€. Les deux montants sont les masses versées en 2020, tous régimes puis Cnav (tableau 1, p. 137, « Ensemble […] 3 530 », « Cnav […] 2 780 »). L'hypothèse est un effet proportionnel aux masses dans les autres régimes. La valeur centrale est donc **−0,752**, avec une borne basse de −0,592 (régime général seul). Confiance `medium`, car c'est un calcul.
- Recoupement (DREES, *Les retraités et les retraites*, édition 2022, fiche 26) : « les dépenses au titre de l’ASV et de l’Aspa augmentent de 12,2 %, après une croissance de 14,8 % en 2019, pour s’élever à 3,5 milliards d’euros ». L'ordre de grandeur est cohérent.
- Le chiffrage visait le même périmètre : +100 € par mois pour tous les allocataires. L'étude d'impact du PLFSS 2018, citée par le Sénat, prévoyait 525 M€ en 2020, plus le coût de l'avancement des dates (vu dans un résultat de recherche, non archivé et non utilisé).

### ASF (ligne `inst_42`, Montaigne −0,9)

- Source : CCSS, mai 2024, p. 98 : « pour un coût supplémentaire de 1,0 Md€ par rapport au montant de 0,2 Md€ déjà constaté en 2022 (soit un coût total de 1,1 Md€) ». Voir aussi p. 16 (« soit un effet en année pleine de 1,1 Md€ ») et p. 100 : « dont 0,9 Md€ au titre de la revalorisation de 50% proprement dite […] et 0,1 Md€ au titre des nouveaux entrants ».
- Réalisé retenu : **−1,1 en 2023**, première année pleine, nouveaux entrants compris (ils font partie de l'effet de la mesure). Si on ne garde que l'effet barème (0,9 Md€ sur la hausse 2022-2023), l'écart est nul.
- Recoupement : la CNAF écrit (communiqué du 14/08/2025) « la masse financière consacrée à l’ASF a augmenté de 1 milliard d’euros du fait de la revalorisation, passant de 2 à 3 milliards d’euros ». L'étude CNAF-DREES elle-même (drees.solidarites-sante.gouv.fr) n'a pas pu être téléchargée : le site rejette les requêtes automatiques.

### PPV (ligne `inst_41`, Montaigne −6)

- Le chiffrage de Montaigne (6 Md€, fourchette 1,6 à 10) est un **coût net de substitution aux salaires**. Aucun coût réalisé de ce périmètre n'est publié. Le CPO l'écrit (octobre 2024, p. 57) : « Ce dispositif n’est pas suivi comme une dépense fiscale de l’IR et son coût pour les finances publiques n’est donc pas publié par l’administration en annexe des projets de lois de finances ».
- Les annexes 4 des PLFSS 2023 et 2024 décrivent le dispositif (PLFSS 2023, § 3.3, p. 45) sans en donner le coût. Les seuls chiffres trouvés n'ont pas le même périmètre : les montants versés (5,4 Md€ en 2022 et 5,3 Md€ en 2023, CPO p. 58) et le gain d'une soumission de la PPV à l'IR (+0,3 Md€, CPO).
- Proposition : `inclus_stats` = « non (réalisé non publié) ».

### CVAE (lignes `inst_34` à `inst_36`)

- La suppression complète, chiffrée à l'horizon 2027, n'a pas eu lieu. Service public Entreprendre (mise à jour du 30/03/2026) : « la loi de finances pour 2025 a reporté la suppression de la cotisation sur la valeur ajoutée des entreprises (CVAE) à 2030 ». Les taux de 2026 et 2027 restent à 0,28 %.
- Seule la baisse de moitié de 2023 a eu lieu. Son coût isolé n'a pas été trouvé, et ce n'est pas le périmètre du chiffrage.
- Proposition : `inclus_stats` = « non (non mise en œuvre : suppression reportée à 2030) ». Le motif actuel est « périmètre et calendrier différents ». La loi de finances pour 2026 n'a pas été lue : d'après la recherche web, la baisse proposée au PLF 2026 n'a pas été gardée, mais ce point est à vérifier sur le texte.

### Heures supplémentaires, 2012 (lignes `inst_53` à `inst_55`)

- **IR** : « Pour l’imposition des revenus de 2011, dernière année pleine d’application de cette défiscalisation, la perte de recettes d’impôt sur le revenu résultant de l’exonération des heures supplémentaires s’est élevée à 1,686 milliard d’euros » (AN, rapport n° 2172, p. 58, source DLF). Ce montant est mesuré sur les déclarations (cases 1AU à 1DU).
- **Cotisations** : « La forte baisse de coût qui en a découlé (0,6 Md€ pour l’ensemble des régimes en 2013, contre 3,4 Md€ en 2011) » (PLFSS 2024, annexe 4, p. 27). Les 0,6 Md€ restants correspondent à la déduction patronale gardée dans les entreprises de moins de 20 salariés.
- **Calcul** : 1,686 + (3,4 − 0,6) = **+4,486 Md€**. C'est un rendement statique : la baisse des heures déclarées après 2012 n'est pas déduite du volet IR, qui n'est plus mesurable (même rapport, p. 59 : les heures « ne font plus l’objet d’une déclaration individualisée »). Le rendement réel est donc au plus de 4,5 Md€. Confiance `medium`. Même logique que la ligne TEPA 2007, dont le réalisé est le coût constaté du dispositif.
- **Périmètre** :
  - candidat et Terra Nova (4,6) : même périmètre. Terra Nova écrit (p. 2) « après déduction des exonérations de cotisations patronales aux très petites entreprises » : écart de −2,5 % ;
  - Montaigne (3,06) : périmètre différent. Il garde toutes les exonérations des moins de 20 salariés (1,43 Md€), alors que le dispositif voté ne garde que la déduction patronale. Son hypothèse haute (4,04), qui ne garde que les exonérations patronales, correspond au dispositif voté. Écart informatif : +46,6 %, `non (périmètre différent)`, comme la ligne Montaigne de 2017 sur les heures supplémentaires.

### Emplois d'avenir, 2012 (lignes `inst_66` à `inst_68`)

- Source : Sénat, avis n° 143 (2016-2017), tome VIII Travail et emploi, p. 27, tableau (ASP-DGEFP, réponse au questionnaire budgétaire) : « Réalisé au 31/12/2015 Emplois d’avenir 82 557 1 505,37 1 319,63 ». Les colonnes sont les contrats, les AE et les CP, en M€. Les CP valent 1 024 M€ en 2014 et 1 186 M€ en LFI 2016 : 2015 est l'année la plus haute.
- Réalisé : **−1,32 Md€** (CP 2015). Il ne comprend ni les exonérations de cotisations patronales ni le reste à charge des employeurs publics.
- **Périmètre** :
  - candidat (2,0, dépêche Reuters, périmètre non détaillé, pris comme un coût budgétaire) : verdict interne « oui » sous réserve, écart de +34,0 % ;
  - Montaigne (3,2) : il compte 21 350 € par contrat, dont 4 830 € d'exonérations et 6 704 € à la charge des employeurs publics. Ce périmètre est plus large : « non (périmètre différent) », écart informatif de +58,8 % ;
  - iFRAP (300 000 emplois) : reste « non (périmètre différent) ».
- Comme pour les emplois francs de 2017 (ligne incluse), l'écart vient surtout du nombre de contrats (82 557 signés en 2015 ; l'objectif était un stock de 150 000).

### Non trouvés (2012)

- **Abattement de succession à 100 000 €** : aucun rendement isolé. Les recherches web n'ont donné que les prévisions (0,33 Md€ en année pleine, Cour, RBDE 2013) et la hausse totale des droits de succession, qui a plusieurs causes. Le rapport AN n° 2172 n'a pas de section sur cette mesure.
- **Retraite à 60 ans pour les carrières longues (décret du 2 juillet 2012)** : aucun coût isolé du décret. Deux recherches ciblées (CCSS, COR, Cour) n'ont donné que la dépense de tous les dispositifs de carrières longues confondus (« plus de 2 milliards d'euros pour la seule CNAV », réponse ministérielle de 2013, vue en extrait) et des effectifs (115 000 des 150 000 départs anticipés de 2013, d'après la presse). Rien n'a été retenu.
- **Doublement de la TTF (LFR 2 2012)** : le RBDE 2013 (`sources/T21/C/ccomptes_rbde_2013.pdf`) donne la hausse prévue (« la hausse de la taxe sur les transactions financières (0,66 Md€) ») et des moindres recettes pour la TTF entière (−0,4 Md€, puis −0,8 Md€ par rapport à la LFI). La part du doublement n'est pas isolée. La répartir au prorata serait un calcul `low` : non retenu.

## 2. Effet sur `erreur_ligne`

Méthode : la même que `scripts/validation.py` et T10b. Lignes dont `inclus_stats` commence par « oui » et qui ont un réalisé et un chiffrage ; médiane de |réalisé − chiffré| / |chiffré|. Le calcul est dans `variantes.py`.

| Variante | n | Erreur absolue médiane |
|---|---|---|
| Actuel | 22 | 14,9 % |
| **Proposée : + ASPA (×2, extrapolé) + ASF** | **25** | **22,2 %** |
| Idem avec l'ASPA du régime général seul (−0,592) | 25 | 16,0 % |
| + ASF seule | 23 | 16,0 % |
| Si 2012 entrait : proposée + 7 lignes 2012 déjà « oui » en interne + 3 nouvelles | 35 | 23,1 % |
| Idem sans le contrat de génération | 32 | 22,4 % |
| Idem + TEPA 2007 | 36 | 22,8 % |

Lecture :

- **La médiane est instable.** Les écarts autour du milieu de l'échantillon sont 13,9 ; 16,0 ; 22,2 ; 22,5 ; 24,0 ; 24,0. Une ligne de plus ou de moins la déplace de plusieurs points. Avec l'ASPA du régime général seul, l'OFCE tombe à +1,3 % et la médiane à 16,0 %.
- **Les trois lignes ajoutées sont toutes négatives** (−50, −25, −22 %). Les prestations à barème coûtent plus que prévu quand de nouveaux allocataires entrent. C'est l'inverse de l'AAH de 2017, où les trois chiffreurs avaient surestimé le coût.
- **Borne haute** (« Institut Montaigne seul », 40 %, n = 8) : avec l'ASPA et l'ASF, 38,9 % sur n = 10.
- Les lignes de 2012 n'entrent pas aujourd'hui : leur `inclus_stats` commence par « non (T21 : test de la médiane des chiffrages non jugeable ; … ) ». Il faudrait d'abord décider de faire entrer 2007 et 2012 dans la calibration (T21 § 6 point 8, G2.3). Elles n'ont pas non plus d'entrée `inst_43` et suivantes dans `validation_attribution.csv` : `validation.py` échouerait sur la clé si elles passaient à « oui ».

## 3. Changements proposés, ligne par ligne (`data/raw/calibration_instituts.csv`)

Les valeurs complètes (citations, URL, notes) sont dans `lignes_proposees.csv`. Chaque valeur modifiée doit être inscrite dans `historique.csv`.

| Ligne | Chiffreur | Colonnes : ancienne → nouvelle |
|---|---|---|
| inst_19 ASPA | Institut Montaigne | `cout_realise` vide → −0.752 ; `ecart_pct` vide → −50.4 ; `inclus_stats` « non (réalisé non trouvé) » → « oui (réalisé extrapolé du régime général) » ; `confiance` high → medium ; `source_realise`, `url_realise`, `citation_realise`, `page_realise`, `note`, `date_acces` (2026-11-01) |
| inst_20 ASPA | OFCE | idem, `ecart_pct` → −25.3 |
| inst_42 ASF | Institut Montaigne | `cout_realise` → −1.1 ; `ecart_pct` → −22.2 ; `inclus_stats` → « oui » ; `confiance` reste high ; colonnes du réalisé et `note` |
| inst_41 PPV | Institut Montaigne | `inclus_stats` « non (réalisé non trouvé) » → « non (réalisé non publié) » ; `url_realise`, `citation_realise`, `page_realise` (CPO p. 57) ; `note` |
| inst_34 à 36 CVAE | Montaigne, iFRAP, candidat | `inclus_stats` → « non (non mise en œuvre : suppression reportée à 2030) » ; colonnes du réalisé (DILA) ; `note` |
| inst_53, inst_55 HS 2012 | candidat, Terra Nova | `cout_realise` → 4.486 ; `ecart_pct` → −2.5 ; `inclus_stats` → « non (T21 : test de la médiane des chiffrages non jugeable ; oui) » ; `confiance` → medium |
| inst_54 HS 2012 | Institut Montaigne | `cout_realise` → 4.486 ; `ecart_pct` → 46.6 ; `inclus_stats` → « … ; non (périmètre différent)) » ; `confiance` → medium |
| inst_66 EA 2012 | candidat | `cout_realise` → −1.32 ; `ecart_pct` → 34.0 ; `inclus_stats` → « … ; oui) » ; `confiance` reste medium |
| inst_67 EA 2012 | Institut Montaigne | `cout_realise` → −1.32 ; `ecart_pct` → 58.8 ; `inclus_stats` → « … ; non (périmètre différent)) » ; `confiance` high → medium |
| inst_68 EA 2012 | Fondation iFRAP | `cout_realise` → −1.32 ; `ecart_pct` → 69.4 ; `inclus_stats` → « … ; non (périmètre différent)) » ; `confiance` high → medium |

Si les lignes de l'ASPA et de l'ASF entrent, les fichiers suivants changent aussi :

- `data/raw/moteur_parametres.csv` (`erreur_ligne`) : `val_central` 0.149 → 0.222. Dans la note, « T10b, n = 22 » devient « T10b et T27 G6.3, n = 25 ». La borne haute vaudrait 0,389 (Montaigne, n = 10) ; arrondie à 0,40, elle peut rester.
- `validation_attribution.csv` : rien à ajouter. `inst_19`, `inst_20` et `inst_42` y sont déjà (règle « Aucune »).
- **Texte en dur** : « erreur absolue médiane de 14,9 % » est écrit à la main dans `web/complet.html:313` et `web/dashboard_page.html:245`, ce que la règle 7 de `CONTRIBUTING.md` interdit. Les deux phrases sont à mettre à jour ou à faire lire dans les CSV. Les mentions « n = 22 » de `recherche/validation/README.md` (ligne 5) et de T10b sont aussi à mettre à jour.

## 4. Décisions laissées à l'intégrateur

1. **ASPA** : prendre l'extrapolation à tous les régimes (−0,752 ; `erreur_ligne` à 22,2 %) ou le seul régime général (−0,592, borne basse écrite par la source ; 16,0 %) ? L'extrapolation colle au périmètre du chiffrage ; le régime général seul est lu sans calcul.
2. **ASF** : coût en année pleine nouveaux entrants compris (1,1, proposé), ou effet barème seul (0,9, écart nul) ?
3. **Campagne 2012** : faut-il la faire entrer dans la calibration ? Si oui : 35 lignes, 23,1 %, après ajout des attributions `inst_43` et suivantes.
4. **Lignes 2012 de Montaigne sur les heures supplémentaires** : périmètre différent (proposé) ou comparaison de son hypothèse haute (4,04) ?
