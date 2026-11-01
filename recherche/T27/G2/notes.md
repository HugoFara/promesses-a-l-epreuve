# T27, groupe 2 : G2.2, G2.8, G2.9 (et G3.2)

Date : 01/11/2026. État du dépôt : commit `0ff7a16`. Rien n'est modifié dans `data/` ni `scripts/` ; les corrections sont proposées au format de `scripts/appliquer_corrections.py`.

Fichiers :

- `cas_recours.csv` : cas pour la version restreinte de « Taux de recours » (G2.2 a), au format de `data/raw/mesures_cout.csv` plus 4 colonnes (`recours_complet_suppose`, `citation_recours`, `page_recours`, `url_recours`) ;
- `recours_partiel.csv` : facteur réalisé / ex ante des cas où l'ex ante comptait déjà un recours partiel (G2.2 b) ;
- `corrections_dlf.csv` : 3 corrections `type_ex_post` (G2.8) ;
- `recette_ponctuelle_n2.csv` : indicateur « recette encore perçue à N+2 » sur les 6 cas (G2.9) ;
- `sources.csv` : sources archivées dans `sources/T27/G2/` (sous-dossiers `A` et `B` pour les deux recherches de G2.2 a, `C` pour le reste) ;
- `parts/` : fichiers bruts des deux recherches de G2.2 a.

## G2.2 « Taux de recours », version restreinte

### a) Cas passés dont l'ex ante supposait un recours complet

Deux recherches parallèles (`parts/cas_recours_A.csv` pour les prestations sociales, `parts/cas_recours_B.csv` pour les aides ponctuelles), fusionnées dans `cas_recours.csv` (11 lignes). Les pistes ont été prises dans un ordre fixé à l'avance, sans tri sur le résultat.

| id | Recours complet supposé | Ex ante | Réalisé | Réalisé / ex ante | Confiance |
|---|---|---|---|---|---|
| `acs_credit_impot_2005` | **oui** : « au moins 2 millions de personnes pourraient être éligibles […] un besoin potentiel de financement de l'ordre de 400 millions d'euros » (Sénat, avis n° 425, 2004, p. 175) | 0,4 | 0,01275 (provisoire, Fonds CMU 2005) | 0,03 | medium |
| `ati_2020` | **oui** : 140 M€ pour 29 300 bénéficiaires, issus de la population cible × critères d'éligibilité, allocation de 800 € × 6 mois, sans taux de recours (étude d'impact, AN n° 904, p. 241-243) | 0,14 | 0,003 (fin 2020, 14 mois, rapport AN n° 4051) | 0,02 | medium |
| `cmu_c_2000` | **oui** : « 9 milliards de francs (1.500 francs x 6 millions de bénéficiaires) » (Sénat, n° 376, 1999) | 1,372 | non trouvé | — | low |
| `rsa_jeunes_2011` | inconnu (« 160.000 jeunes […] pour un coût total de 250 millions d'euros » : éligibles ou allocataires attendus, non dit) | 0,25 | 0,0258 | 0,10 | medium |
| `cheque_bois_2022` | inconnu (2,6 M d'éligibles, 230 M€, 50 à 200 € : 88 € par éligible, compatible avec un recours complet, non écrit) | 0,23 | 0,060 | 0,26 | medium |
| `aide_200_etudiants_2020` | inconnu (ex ante reconstitué : 400 000 × 200 €) | 0,08 | 0,0101 | 0,13 | low |
| `ci_abonnement_presse_2020` | inconnu (60 M€ en année pleine, sans hypothèse) ; réalisé en `reestimation` (Voies et moyens) | 0,06 | 0,002 | 0,03 | medium |
| `apa_2002`, `apa_2003` | non (« lente montée en charge », 500 000 puis 550 000 bénéficiaires pour 800 000 personnes) | 2,29 ; 2,59 | 1,855 ; 3,205 | 0,81 ; 1,24 | medium |
| `demission_reconversion_2023` | non (enquête d'intentions, effets d'appel) | 0,2875 | 0,475 | 1,65 | high |
| `prime_conversion_2018` | non (100 000 primes « envisagées » ; dispositif existant depuis 2015, hors champ strict) | 0,122 | 0,365 | 2,99 | medium |

Abandonnés : PCH 2006 (pas de chiffrage officiel de la prestation), aide au permis des apprentis 2019 (pas d'ex ante), MonSoutienPsy (montants lus dans la presse seulement), bonus réparation (financé par les éco-organismes).

**Conclusion : 2 cas utilisables seulement (ACS, ATI), sous `MIN_CAS` (5) ; la version restreinte reste « non testée ».** Les deux vont dans le sens de la règle, et bien au-delà : la dépense réalisée vaut 2 à 3 % de l'ex ante, contre 65 % pour le facteur. Les 4 cas « inconnu » vont dans le même sens (3 à 26 %). Réserves : réalisés de première année (ACS provisoire, ATI en pleine crise sanitaire) ; ex ante secondaire pour l'ACS (avis du Sénat) ; la CMU-C n'a pas de réalisé sur le même périmètre. Pour atteindre 5 cas, il faudrait d'abord confirmer l'hypothèse de recours des cas « inconnu » (RSA jeunes : PAP 2010 ; chèque bois : évaluation de l'amendement n° 605). À l'inverse, deux ex ante à recours partiel (APA 2003, démissionnaires) sont dépassés : une décote leur aurait nui. Vérification de l'intégrateur : les citations ACS (avis n° 425, Fonds CMU 2005) et ATI (étude d'impact, rapport n° 4051) ont été relues dans les PDF archivés.

### b) Décote « recours partiel déjà compté » (cas existants, sans changer la règle)

Cas retenus : ceux dont l'hypothèse de recours partiel de l'ex ante est écrite dans une source lue. Facteur = réalisé central / ex ante (`deflateur_ex_ante` = 1 partout).

| id | Hypothèse de recours de l'ex ante (citée) | Ex ante | Réalisé | Facteur |
|---|---|---|---|---|
| `pa_2016` | « si nous prenons pour hypothèse un taux de recours de 50 %, cela signifierait 66 % pour les sommes à financer » (secrétaire d'État, Sénat, 30/11/2015) | 3,95 | 4,1 | 1,038 |
| `cheque_energie_gen_2018` | « taux d'usage de 90 % et plus entre 2018 et 2020 » (Cour 2022, p. 43) | 0,5634 | 0,4223 | 0,750 |
| `cheque_energie_elarg_2019` | idem | 0,8573 | 0,6857 | 0,800 |
| `pass_sport_2021` | « toucher un peu moins de 2 millions de jeunes soit 37% de la cible » (Cour, NEB 2021, p. 72) | 0,100 | 0,0656 | 0,656 |

Résultats (calculs) :

- **moyenne 0,81** (médiane 0,775) sur 4 lignes ; **0,82** (médiane 0,775) si les deux années du chèque énergie, même dispositif, comptent pour un seul cas (3 cas) ;
- moyenne pondérée par les montants : 0,96 (la prime d'activité domine) ;
- avec `indemnite_carburant_2023` (recours implicite de 70 %, calculé et non écrit par la source : 700 M€ pour 10 M de travailleurs à 100 €) : moyenne 0,77 sur 5 lignes, 0,77 (médiane 0,715) sur 4 cas dédoublonnés.

Exclus : `pa_2019` (hypothèse de recours non trouvée), `cir_2008` et `cite_2015` (crédits d'impôt, aucune hypothèse de recours écrite dans les sources de la ligne ; `validation.py` les dit « à recours partiel » sans citation), `cheque_fioul_2022` (ex ante = enveloppe sur 1,6 M de ménages éligibles, sans hypothèse de recours écrite ; hors statistique principale), et les lignes à hypothèse « inconnue » (Embauche PME, emplois francs, aides 2020, RSA activité 2009).

Lecture : quand l'ex ante compte déjà un recours partiel, la dépense réalisée reste en moyenne à environ 80 % de l'ex ante, mais avec une forte dispersion (0,66 à 1,04) et 3 dispositifs seulement, sous `MIN_CAS` (5). Une décote de 0,8 environ ferait mieux que le facteur 1 sur le chèque énergie et le Pass'Sport, plus mal sur la prime d'activité (erreur de +4 % à +22 %). Résultat présenté à part, sans proposition de changement de règle. Détail : `recours_partiel.csv`.

Réserve : pour le chèque énergie, envoyé d'office, l'hypothèse porte sur le taux d'usage, pas sur une demande ; l'agent d'attribution l'avait signalé (« hésitation avec Aucune »).

## G2.8 Cas de la DLF classés `observe`

Source relue : AN, rapport d'information n° 2172 (V. Rabault, 22/07/2014), p. 49-55, archivé en T18 (`sources/T18/A/an_rapinfo_i2172.pdf`, sha256 `07f6e889…178f`, inchangé).

Pour les trois mesures, le « rendement » est un **supplément d'impôt calculé par la direction de la législation fiscale** sur les déclarations, foyer par foyer, et ventilé par décile de RFR (« VENTILATION DE L'IMPOSITION SUPPLÉMENTAIRE ACQUITTÉE AU TITRE DE… », « Source : direction de la législation fiscale ») :

- `tranche45_2013` : nouvelle tranche du barème de l'IR (« L'article 3 de la loi de finances pour 2013 a introduit une nouvelle tranche marginale au sein du barème progressif », p. 51) ; 344 M€, p. 51-52 ;
- `qf_2013` : plafond du quotient familial, paramètre du barème (p. 52-53) ; 554 M€ ;
- `frais_pro_2013` : plafond de la déduction forfaitaire de 10 %, règle d'assiette (p. 54-55) ; 90 M€.

Aucune de ces mesures n'a de prélèvement propre : le supplément est la différence entre l'impôt calculé avec et sans la mesure, l'impôt « sans » n'étant pas observé. C'est le cas que le README (convention du 20/10/2026) classe en `reestimation` : « la mesure est fondue dans un impôt ou une dépense existante (changement de taux ou d'assiette […]), et son coût après coup est un nouveau chiffrage de l'administration ». Le chiffrage est fait sur les déclarations réelles et non sur un modèle, ce qui le rend plus solide qu'une prévision ; il reste un rechiffrage.

**Conclusion : les 3 lignes passent en `reestimation`** (`corrections_dlf.csv`, confiance inchangée). Effet : « Élasticité revenus » passe de 3 à 2 cas observés (`cehr_2012`, `cdhr_2025`) et reste sous `MIN_CAS` ; `qf_2013` et `frais_pro_2013` sont en règle « Aucune » (facteur 1, verdict « inchangé ») et ne changent aucun statut. Aucun effet sur le solde.

À ne pas étendre à `cehr_2012` (même rapport, p. 50) : la CEHR est un prélèvement propre (art. 223 sexies du CGI), « contribution exceptionnelle supplémentaire assise sur le revenu fiscal de référence », dont le montant constaté (630 M€ en 2012) est une recette isolable ; elle reste `observe`.

## G2.9 Durée de la CEHR, indicateur « Recette ponctuelle » ; G3.2 assiette des dividendes

### Durée de la CEHR

Source primaire : BOFiP, BOI-IR-CHR, version du 11/07/2017, affichée « Version en vigueur du 11/07/2017 à aujourd'hui » à la consultation du 01/11/2026 (`sources/T27/G2/C/bofip_BOI-IR-CHR-20170711.html`), § 1 :

> « La contribution exceptionnelle sur les hauts revenus s'applique à compter de l'imposition des revenus de l'année 2011 et jusqu'à l'imposition des revenus de l'année au titre de laquelle le déficit public des administrations publiques est nul. »

La version de 2014 (archivée, PDF) porte la même phrase, et le rapport AN n° 2172 (2014, p. 49) l'écrit déjà : « a vocation à l'être jusqu'à l'imposition des revenus de l'année au cours de laquelle le déficit public des administrations publiques sera nul ».

Conclusion :

- la CEHR n'a **jamais eu de date de fin fixe** : « exceptionnelle » par son nom, elle est conditionnée dès l'origine (art. 2 de la LFI 2012) au retour à un déficit public nul. Aucune LFI n'a donc eu à la proroger ou à la pérenniser, et nous n'en avons trouvé aucune qui le fasse ;
- elle est **perçue sans interruption depuis 2012** (revenus 2011) : 630 M€ en 2012, 522 M€ en 2013 (rapport n° 2172, p. 50), et la doctrine est toujours en vigueur ; la fiche service-public F31130, vérifiée le 15/04/2026 (archivée en T4p), la présente comme due en 2026. Confiance : high pour la base légale ; medium pour la perception de chaque année après 2013, faute d'une série annuelle de rendement lue (Voies et moyens non consultés). Le chiffre de « plus de 1 Md€ » trouvé dans des amendements n'est pas repris (source partisane, non vérifiée).

### G3.2 Assiette de la CEHR pour les dividendes

- BOI-IR-CHR § 40 : « La contribution est assise sur le revenu fiscal de référence du foyer fiscal » ; § 50 renvoie au IV de l'art. 1417 du CGI, qui réintègre « certains abattements appliqués pour la détermination du revenu catégoriel ».
- BOFiP BOI-RPPM-RCM-20-10-30-20 (version en vigueur du 20/12/2019 « à aujourd'hui »), § 80, « Neutralisation de l'abattement de 40 % pour la détermination du revenu fiscal de référence » : « il doit être ajouté aux revenus nets […] le montant de l'abattement en base de 40 % mentionné au 2° du 3 de l'article 158 du CGI ». Exemple du BOFiP : 5 000 € de dividendes bruts, 100 € de frais, 4 900 € retenus dans le RFR.

**Conclusion : la CEHR s'applique à 100 % du dividende (net des seuls frais), abattement de 40 % réintégré.** Le central actuel de `t1_capital` (46,27 %) est donc conforme ; la borne basse « France Stratégie » (CEHR sur 60 %) ne correspond pas au droit. Proposé à l'intégrateur : remplacer « Écart à trancher » dans la note de `parametres_bareme.csv:132` par la référence BOFiP ci-dessus, et figer le central (non fait ici). Point non vérifié : la déduction de la CSG déductible dans le RFR, que la formule de `div_tmi_45` applique (facteur 1 − 0,051 ou 0,932) ; les pages lues n'en parlent pas. Au PFU (depuis 2018), les dividendes n'ont pas d'abattement : leur montant brut entre dans le RFR au titre des revenus soumis à prélèvement forfaitaire (IV de l'art. 1417 cité par le BOFiP, § 50) ; le cas n'est pas traité dans les pages lues, c'est une déduction.

### Indicateur proposé pour « Recette ponctuelle »

**« Recette encore perçue à N+2 : oui / non »**, N étant la première année pleine d'encaissement de la ligne. La règle (facteur 0, recette nulle dans le solde durable) **a raison si « non »**. Deux lectures :

- *stricte* : le même dispositif juridique produit encore une recette à N+2 ;
- *large* : une recette du même prélèvement (même assiette, mêmes redevables) le prolonge à N+2, par prorogation, reconduction ou pérennisation d'une hausse.

Classement des 6 cas de la statistique principale (`recette_ponctuelle_n2.csv`) :

| id | N | Perçue à N+2, stricte | large | Source |
|---|---|---|---|---|
| `cef_2012` | 2012 | non | non | RBDE 2013, p. 82 (contrecoup de 2,33 Md€ en 2013) |
| `contrib_stocks_petroliers_2012` | 2012 | non | non | RBDE 2013, p. 82 (0,55 Md€) |
| `ce_is_2017` | 2017 | non | non | BOI-IS-AUT-35-20171228 § 250 (exercices clos jusqu'au 30/12/2018) ; RBDE 2018, p. 82 |
| `stdr_2014` | 2014 | **oui** (2 476 M€ en 2016) | oui | RBDE 2019, p. 64, tableau n° 12 |
| `cellule_regul_2010` | 2010 | non (medium) | non | réponse ministérielle JO 10/08/2010 (fermée le 31/12/2009) ; RBDE 2010, p. 81 |
| `ce_trs_2012` | 2012 | non | **oui** (partiel, medium) | RBDE 2013, p. 82 (doublement du taux de la taxe de risque systémique, 0,26 Md€ en 2013) |

**Résultat : la règle a raison pour 5 cas sur 6 en lecture stricte, 4 sur 6 en lecture large.** 6 cas atteignent `MIN_CAS` (5). Réserves : la cellule de 2010 renaît en STDR en 2013 (N+3, hors indicateur) ; pour la TRS, le produit de 2014 n'est pas lu (le « oui » repose sur 2013 et sur une hausse de taux sans fin annoncée) ; la cellule « non » repose sur l'absence de recette mentionnée dans les RBDE 2011 et 2012. Le STDR montre la limite de l'indicateur : une recette de régularisation peut durer plusieurs années sans être durable. La CEHR n'est pas un cas de la règle (attribuée à « Élasticité revenus ») ; si elle l'était, ce serait un « oui ».

Proposition pour `validation.py` (non faite) : sortir « Recette ponctuelle » de `NON_CONCLUANTES` et juger la règle sur cet indicateur (« confirmée » si la règle a raison dans plus de la moitié des cas), en publiant les deux lectures. Le choix de la lecture revient à l'intégrateur.
