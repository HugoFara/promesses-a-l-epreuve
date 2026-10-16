# T18, groupe C : notes (Taux de recours, Réforme structurelle)

Date d'accès de toutes les sources : 2026-10-16. Sources archivées dans `sources/T18/C/` (16 fichiers), listées avec leur sha256 dans `sources_C.csv`. Gel des règles : commit `0b4175f`, non modifié.

## Bilan face à la cible (8 cas `observe` par règle)

| Règle | `observe` | Tous types | Cible atteinte |
|---|---|---|---|
| Taux de recours | 10 | 10 | oui (avec deux réserves ci-dessous) |
| Réforme structurelle | 1 | 3 | **non** |

Réserves pour « Taux de recours » :

- `cheque_energie_gen_2018` et `cheque_energie_elarg_2019` portent sur le même dispositif, sur deux années ; `aej_2020`, `aide_apprentissage_2020` et `aide_contrat_pro_2020` viennent du même tableau de la Cour et du même plan. Ce ne sont pas des cas tout à fait indépendants.
- Les ex ante sont surtout des **crédits votés** (LFI, LFR) ou des trajectoires budgétaires, c'est-à-dire des prévisions de dépense faites par l'administration au moment de la création. Aucun ne suppose explicitement un recours complet.

Écarts calculés, (ex post central − ex ante) / ex ante : Embauche PME − 18 % ; emplois francs − 68 % ; AEJ − 13 % ; aide apprentissage + 56 % ; aide contrat pro − 13 % ; chèque énergie 2018 − 25 % ; 2019 − 20 % ; RSA activité 2009 − 49 % ; Pass'Sport − 34 % ; indemnité carburant − 38 % ; assurance maladie 2004 − 67 % ; RGPP − 3 % ; carte judiciaire (coût) − 10 %. Les mesures ont été prises dans l'ordre où les sources les donnaient, sans tri sur le résultat ; le seul filtre a été l'existence d'un couple ex ante / réalisé sur le même périmètre.

## Recours complet supposé ? (restriction du 14/10/2026)

| id | Recours complet supposé | Élément |
|---|---|---|
| embauche_pme_2017 | inconnu | la Cour souligne « l'absence de prévision possible du nombre de dossiers » |
| emplois_francs_2018 | inconnu | rien dans la source |
| aej_2020, aide_apprentissage_2020, aide_contrat_pro_2020 | inconnu | objectifs en nombre de primes (tableau n° 1 du RPA 2022), sans hypothèse de recours |
| cheque_energie_gen_2018, cheque_energie_elarg_2019 | **non** | « les indicateurs retenus dans les projets annuels de performance (PAP) reposent sur des taux d'usage de 90 % et plus entre 2018 et 2020 » (Cour 2022, p. 43) |
| rsa_activite_2009 | inconnu | prévisions « construites par croisement des modèles économiques des directions statistiques de l'État et de la Caisse nationale d'allocations familiales » (ministre, 2010) ; hypothèse de recours non trouvée |
| pass_sport_2021 | **non** | « l'objectif était donc de toucher un peu moins de 2 millions de jeunes soit 37% de la cible » (Cour, NEB 2021 Sport, p. 72) |
| indemnite_carburant_2023 | inconnu, probablement non | 700 M€ pour 10 M de travailleurs visés à 100 € : recours implicite de 70 % (calcul, non écrit par la source) |

**Conséquence** : la version restreinte de la règle (facteur 0,65 seulement si recours complet supposé) ne s'appliquerait à **aucun** de ces 10 cas sur la foi des sources lues. Ils testent la règle d'origine (« prestation à la demande »), pas la version restreinte. Le sens des écarts est néanmoins net : 9 cas sur 10 dépensent moins que prévu (de − 13 % à − 68 %), alors même que deux ex ante intégraient déjà un recours partiel (chèque énergie 90 %, Pass'Sport 37 %). Ce point est laissé à l'intégrateur (voir fin de note).

## Cas retenus : détails

### Taux de recours

1. **Embauche PME (2017)**. NEB 2018 Travail-emploi, p. 67, tableau « Coût consolidé » (source Chorus) : LFI 2017 1 932,0 M€ de CP, exécution 1 581,1. 2016 est exclu, car la mesure (décret du 25 janv. 2016) n'était pas budgétée en LFI 2016 (84,8 contre 539,6). 2018 n'est pas retenu (même mesure) : 1 105,8 contre 762,2.
2. **Emplois francs (2018)**. NEB 2019, p. 46 (tableau n° 5) et p. 63 : LFI 12 M€, exécution 3,8 M€. 2019 n'est pas retenu, car le périmètre a été élargi en cours d'année (arrêté du 22 mars 2019) : 51 contre 23.
3. **AEJ, aide apprentissage, aide contrat pro (2020)**. RPA 2022, p. 17 du PDF, tableau n° 3 (source DGEFP) : trajectoire initiale 2020 du plan de relance contre exécution 2020.
   - Aide apprentissage : la NEB 2021 Travail-emploi (p. 74) donne 300 M€ de CP en LFR3, puis + 330 M€ en LFR4 pour l'extension aux apprentis de niveau master. L'exécution de 630,47 M€ égale presque la somme des crédits ouverts. Le périmètre a changé : confiance low.
   - AEJ : paiement trimestriel à terme échu, donc une part de l'écart 2020 est un décalage.
4. **Chèque énergie (2018, 2019)**. Cour, févr. 2022, p. 44, tableau n° 8 (LFI / réalisé, d'après la DGEC et le PAP 2022). Le taux d'usage constaté (tableau n° 7, p. 33) est de 78,8 % en 2018 et 80,4 % en 2019. La NEB 2020 EDMD (p. 58 du rapport) confirme le même biais en 2020 : LFI 822,1 M€ de CP calculés sur « un taux d'usage global de 86 % », exécution 687,4 M€. 2020 n'est pas retenu, car ce n'est plus une mesure nouvelle.
5. **RSA activité (2009)**.
   - Ex ante : budget du FNSA du PAP 2009, « RSA chapeau 1 450 » M€ en 2009, lu dans le rapport général AN n° 1198, annexe 43, p. 23 ; en année pleine, 3,3 Md€.
   - Ex post : le ministre, devant la commission des finances de l'AN (15 juin 2010, compte rendu n° 85, p. 3), déclare « 744 millions d'euros ont été consommés au titre du RSA-activité ». La subvention d'équilibre du FNSA a été de 80 M€ exécutés contre 555 M€ en LFI.
   - Cela lève le motif d'exclusion de T10a (sources primaires non lues). Le RAP 2009 du programme 304 n'a pas été lu : l'ex post est une déclaration ministérielle, d'où la confiance medium.
6. **Pass'Sport (2021)**. NEB 2021 Sport, p. 72 : enveloppe de 100 M€ (LFR1 2021), exécution de 65,6 M€ en AE et 45,8 M€ en CP. La campagne a été prolongée jusqu'au 28 févr. 2022.
7. **Indemnité carburant (2023)**. NEB 2023 EDMD, p. 45-46 : LFI 700 M€, 277 M€ consommés sur ces crédits, 433 M€ en comptant les 156 M€ restitués par l'ASP (note 47), et 4,3 M de bénéficiaires. Le central retenu est de 433 M€, cohérent avec 4,3 M × 100 € (calcul). C'est un choix de lecture à confirmer.

### Réforme structurelle

1. **Assurance maladie 2004, transferts de charges** (`observe`, low).
   - Source : audition de la présidente de la 6e chambre de la Cour au Sénat, rapport n° 385 (2007-2008). Elle donne 1,5 Md€ d'économies attendues sur 2004-2006 contre 0,5 Md€ constatés dans les comptes nationaux de la santé.
   - L'ex ante est une reconstitution de la Cour, pas un chiffrage de 2004 lu : l'étude d'impact n'existait pas encore et l'exposé des motifs n'a pas été cherché.
   - senat.fr a répondu avec un en-tête de navigateur complet (voir « Accès »).
2. **RGPP 2012** (`reestimation`, low). Rapport IGA-IGF-IGAS de sept. 2012 :
   - p. 41, tableau n° 4 : CMPP 6 de déc. 2011, 12,3 Md€ en 2012 par rapport à 2008 ;
   - p. 43 : réestimation par la direction du budget à 11,9 Md€ ;
   - p. 39 : la cible initiale de 2008 était « de 10 à 15 Mds€ à horizon 2012 ».
   L'ex post n'est pas une observation, et les inspections jugent une partie des gains « purement optique ».
3. **Carte judiciaire** (`reestimation`, medium). RPA 2015, p. 43-44 : enveloppe de 457 M€ (juill. 2008) contre un coût de 413 M€ estimé par la Cour. C'est un coût de mise en œuvre, pas une économie : cas limite pour la règle. Les économies de fonctionnement (9,1 M€/an) n'ont pas d'ex ante.

## Pistes non retenues (motif, endroits cherchés)

**Taux de recours**

- **Complémentaire santé solidaire (2019)**.
  - Ex ante lu : PLFSS 2019, annexe 9, art. 34, p. 262-263 du PDF. Surcoût de 160 M€ en 2020, 190 en 2021 et 220 en 2022 pour le Fonds CMU-c/CNAM. Hypothèse explicite d'un **recours partiel** : « amélioration de 3 points du taux de recours en 2020 pour les anciens éligibles à l'ACS, de 6 points en 2021 et de 9 points en 2022 ».
  - Ex post non trouvé : les rapports annuels CSS (DSS) donnent la dépense totale (2 523 M€ engagés en 2021 par les régimes, rapport 2022 sur vie-publique.fr, PDF 288458), pas le surcoût par rapport à l'ACS.
  - Rapport 2021 du site complementaire-sante-solidaire.gouv.fr : lien mort (page HTML).
- **Prime à la conversion et bonus**.
  - NEB 2020 EDMD, p. 75-76 : objectif initial de 120 000 primes par an et 405 M€ d'AE en 2020, contre 186 000 primes pour 643,6 M€ réalisés. Le barème a été relevé en cours d'année (LFR3, plan de relance) : périmètre non comparable.
  - Les NEB du CAS « Aides à l'acquisition de véhicules propres » (2018, 2019) n'ont pas été trouvées sous le motif d'URL `2023-10/NEB-<année>-<mission>.pdf`.
- **Garantie jeunes, CEJ (2022)**. NEB 2022 Travail-emploi, p. 54-56 : l'ensemble des « mesures jeunes » donne 1,9 Md€ en LFI 2022 contre 1 604 M€ exécutés (− 16 %). Le périmètre mêle allocations et accompagnement : aucune ligne CEJ seule ex ante / ex post n'a été lue.
- **ACRE 2019** (NEB 2019, tableau n° 5 : LFI 528, exécution 644). Exonération largement automatique depuis 2019 : elle ne relève pas d'une prestation à la demande. Non retenue.
- **Garantie jeunes (généralisation 2017)**. Non cherchée faute de quota.

**Réforme structurelle**

- **Assurance chômage 2023**. Ex post toujours non trouvé. Les prévisions Unédic d'oct. 2024 et de févr. 2025 (lues, non archivées) ne chiffrent plus séparément les économies de la réforme 2023. La page de juin 2026 a été repérée, PDF non lu.
- **Convention d'assurance chômage 2017**. L'ex ante Unédic (juin 2017) donne 550 M€ dès 2018. La seule mise à jour lue (juin 2018) est une nouvelle prévision du même modèle (« 550 M€ d'économies dès 2018 ») : pas d'ex post. Le rapport financier 2019 confond conjoncture et convention.
- **Réforme 2019-2021** (`ac_2021`). Retenue par T10a mais absente de `data/raw/mesures_cout.csv`. Elle n'est pas reprise ici : à l'intégrateur de dire si elle doit être réintégrée sous « Réforme structurelle » (`reestimation`, même institution).
- **Régimes spéciaux 2008**.
  - Cour 2019 (rapport sur les régimes RATP, SNCF et IEG, lu puis non archivé) : gains cumulés 2011-2020 de ≈ 4,1 Md€ pour le régime SNCF, contre 4,7 Md€ de coûts d'accompagnement pour l'entreprise (estimations de 2012). RATP : 270 M€ de gains contre plus de 300 M€ de coûts. EDF (2009) : 113 M€ d'économies d'ici 2035 contre 250 M€ de coûts.
  - Sénat, rapport l17-108-324 : projections uniquement.
  - Aucun chiffrage gouvernemental de 2007 n'a été lu (seulement un article de presse citant 500 M€ d'ici 2012) : exclue.
- **Accord AGIRC-ARRCO 2015**. Ex ante lu : COR, doc. 3334 (avril 2016), « 6,1 Md€ d'économies à l'horizon 2020 ». Aucun bilan ex post trouvé (COR, Trésor-Éco n° 178 qui est une projection, IFRAP).
- **Fusion des régions 2015**.
  - Ex ante : déclarations ministérielles rapportées par la presse (10 Md€, ou 12 à 25 Md€), non lues en primaire.
  - Ex post : Cour 2019 (finances locales, fascicule 2), qualitatif (« les économies de gestion attendues ne sont donc pas encore au rendez-vous »), sans chiffre national.
- **DGFiP, dix ans après la fusion** (Cour 2018, lu puis non archivé) : aucun ex ante chiffré en euros.
- **Bases de défense** (Cour 2024, lu puis non archivé) : l'objectif est exprimé en emplois (54 000 suppressions), sans montant d'économies.
- **Convention d'assurance chômage 2014** (droits rechargeables, annexes 8 et 10). Recherche web du 16/10 : seul l'ex ante du rapport financier Unédic 2014 (≈ 300 M€ d'économie en 2014) est cité dans les résultats, sans être lu ; le projet d'évaluation de nov. 2015 annonce une évaluation ex post sans chiffre. Non retenue.
- **Réforme des retraites 2014**. Recherche infructueuse : aucun ex post publié des économies de la loi de 2014 n'a été trouvé.
- **Réforme 2003, MAP, carte territoriale de l'État**. Non cherchées faute de quota.

## Accès

- **ccomptes.fr** : accessible. Le serveur est lent : plusieurs PDF ont été tronqués avec `--max-time 120`, il faut 300 à 500 s. Les NEB 2016-2017 Travail-emploi et la NEB 2021 « Plan de relance » sont introuvables sous le motif d'URL `sites/default/files/2023-10/NEB-<année>-<mission>.pdf`.
- **senat.fr** : 403 avec `curl -A "Mozilla/5.0"`, mais **200 avec un User-Agent Firefox complet et les en-têtes Accept et Accept-Language**. À signaler aux autres groupes.
- **assemblee-nationale.fr** : accessible. L'annexe 9 du PLFSS 2019 (7 Mo) a été tronquée au premier essai.
- **complementaire-sante-solidaire.gouv.fr** : le lien du rapport 2021 renvoie une page HTML.

## Décisions laissées à l'intégrateur

1. **Taux de recours, version restreinte.** Aucun des 10 cas ne suppose un recours complet d'après les sources ; la version restreinte reste donc non testée. Pourtant, 9 cas sur 10 surestiment la dépense, de 13 à 68 %, y compris quand l'ex ante intégrait déjà un recours partiel. Cela plaiderait pour une décote, plus faible, applicable aussi aux crédits votés pour une aide à la demande nouvelle. À trancher sans modifier la règle pendant T18.
2. **Nature de l'ex ante.** Les crédits votés (LFI, LFR) sont-ils des « chiffrages avant adoption » au sens du § 1 de la consigne ? Pour Embauche PME (LFI 2017), la mesure existait déjà.
3. **Indépendance des cas** : chèque énergie 2018 et 2019, et les trois aides #1jeune1solution.
4. **Réforme structurelle** : la cible est inatteignable sur des réalisés `observe`. Les économies de réforme ne sont presque jamais observées, seulement réestimées par l'administration qui les a prévues (RGPP, Unédic). Le seul `observe` (assurance maladie 2004) repose sur un ex ante reconstitué a posteriori.
5. **Carte judiciaire** : coût de mise en œuvre, pas une économie. À exclure si la règle ne vise que les économies.
6. **`ac_2021`** (T10a) : à réintégrer ou non.
