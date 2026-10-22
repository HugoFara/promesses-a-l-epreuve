# T25, partie C (agent B) : lignes 2024 dont le coût était déjà programmé, budgété ou dans la trajectoire

Notes du 22/10/2026. Gel vérifié : commit `0a905e8` ; sha256 de `application_lignes.csv` et `chiffrages_instituts.csv` identiques à la consigne. 87 lignes (toutes sauf `rn24_prisons` et `rn24_rente_infra`), dans `lignes_B.csv`, dans l'ordre du fichier source.

## 1. Méthode

- Pour chaque ligne, j'ai relu ce que le chiffreur retenu (`independant`) chiffre : la fiche ou la page des micro-chiffrages Montaigne (NFP, Ensemble, RN, dans `sources/T20/integration/`), la synthèse, ou l'introduction et le tableau iFRAP (`sources/T6`, `sources/T17`).
- Critère appliqué tel que fixé (consigne § 1) : P1 loi de programmation, P2 LFI/LFSS 2024 ou PAP, P3 chiffré dans le PStab d'avril 2024. Le PStab (`sources/T24/agent/pstab_2024-2027.pdf`) a été parcouru en plein texte pour chaque thème (point d'indice, SNU, leasing, fraude, petite enfance, apprentissage, recherche, AME, audiovisuel, CVAE, rentes…).
- La part comprise est mesurée d'après la référence au 30/06/2024, pas d'après l'exécution.
- Une phrase suffit pour les mesures manifestement nouvelles (baisses d'impôt, prestations créées ou revalorisées, recettes nouvelles). Pour une recette ou une économie, « comprise » voudrait dire déjà comptée dans la trajectoire : je n'en ai trouvé aucune.
- Lignes de calcul du site (`*_taux`, `nfp_smic_emploi`) et écarts arithmétiques (`*_ecart`) : sans objet.

## 2. Résultat

| Ligne | Montant | Critère | Part comprise (centrale ; fourchette) | Ce qui est compris |
|---|---|---|---|---|
| `ens_snu` | −3,6 | P2 | 0,16 ; 0,16 à 0,3 | Montaigne chiffre le coût complet d'un SNU généralisé (DITP, 4 218 €/jeune × 870 000) sans retrancher le SNU existant : 160,0 M€ en LFI 2024 (P163, action 06 ; PAP 2025, colonne LFI 2024, p. 11 et 85) |
| `ens_autres_dep_reste` | −2,911 | P2 | 0,4 ; 0 à 1,13 | Fauteuils roulants (0,4) : base juridique votée en LFSS 2024 (art. 85) ; remplacement des absences (0,7) : en partie financé par le Pacte enseignant (628 M€ au PLF 2024) ; retraites agricoles (0,1) : objectif inscrit dans la loi n° 2023-87 |

Les 85 autres lignes : `aucun`.

Effet si l'intégrateur retient les valeurs centrales (facteur = 1 − part / montant) : Ensemble 2024 +0,56 Md€ sur son solde (SNU +0,16, résidu +0,4). NFP 2024 et RN 2024 : 0.

### 2.1 `ens_snu` (P2)

- Fiche Montaigne (`sources/T22/ENS/montaigne_ens_snu_wb20240725.html`) : « l'application du coût actuel par jeune du SNU à une classe d'âge entière, qui donne un coût minimum de 1,9 Md€ » ; intermédiaire « 3,6 Md€ pour une cohorte de 870 000 jeunes ». C'est le coût total du dispositif, pas le surcroît par rapport au SNU de 2024.
- Référence : PAP 2025 SJVA (`sources/T25/B/an_pap2025_sjva.pdf`, p. 11) : « 06 – Service National Universel 160 047 188 » en LFI 2024 (AE = CP), 128,3 M€ au PLF 2025. Concordant avec l'avis du Sénat sur le PLF 2024 (`senat_a23-133-62_jeunesse_syn.pdf`) : « Les crédits inscrits en 2024 sur le programme 163 s'élèvent ainsi à 160 millions d'euros ».
- Borne haute 0,3 : l'équipe de campagne dit 1,4 Md€ « dont 0,3 Md€ déjà prévus dans la trajectoire ». Le PStab ne mentionne pas le SNU. Source partisane, gardée seulement comme borne haute.
- Non vérifié : effet du décret d'annulation du 21/02/2024 sur l'action SNU. Sans effet sur le critère, qui se lit sur la LFI.
- Pour comparaison, l'iFRAP (écart au PStab) compte 1,56 Md€.

### 2.2 `ens_autres_dep_reste` (P2, partiel)

Les postes de Montaigne (synthèse Ensemble et micro-chiffrages p. 1 à 4) font 2,911. L'iFRAP (`sources/T6/ifrap_ens.html`) écrit : « beaucoup de mesures annoncées sont en fait déjà inscrites au budget comme l'indexation des pensions, le remboursement des fauteuils roulants, la lutte contre les heures d'enseignement non remplacées ». Vérification poste par poste :

- **Fauteuils roulants, 0,4.** LFSS 2024, art. 85 (JORF du 27/12/2023, `jorf_lfss2024_lemediasocial.pdf`, p. 58) modifie l'art. L. 165-1 CSS (« le mot : « distinguer » est remplacé par le mot : « déterminer » »). C'est l'amendement n° 3294 du Gouvernement, dont l'exposé dit : « Le présent amendement a pour objet d'assurer un remboursement intégral pour les fauteuils roulants » ; extension « dans le courant 2024 » ; « L'impact financier […] dépendra de la négociation des conditions tarifaires ». Le texte de l'amendement est identique en substance à l'art. 85 : seule la mention « une ou » diffère. La base légale est votée en LFSS 2024, mais sans montant. Montaigne chiffre le reste à charge total (« ce coût qui correspondrait au coût supplémentaire pour la sécurité sociale, de 0,4 Md€ »). Central 0,4 ; bas 0 si l'on exige un crédit chiffré.
- **Remplacement des absences, 0,7.** Montaigne part du coût des absences non remplacées estimé par la Cour des comptes en 2021, donc avant le Pacte. Le PLF 2024 finance le Pacte enseignant : « Avec 628 millions d'euros, les crédits prévus pour le Pacte enseignant en 2024 » ; « Le ministère a fait de la réalisation de remplacements de courte durée l'un des objectifs prioritaires du Pacte dans le second degré » (Sénat, rapport spécial l23-128-314, § I.3, `senat_l23-128-314_enseignement.html`). La part du Pacte qui va aux remplacements n'est pas chiffrée : de 0 à 0,628. Montant du PLF 2024, non relu en LFI. L'iFRAP ne compte que 0,3 d'écart.
- **Retraites agricoles, 0,1.** Montaigne chiffre exactement le calcul sur les 25 meilleures années à partir du 01/01/2026 : « La mesure débuterait au 1er janvier 2026 ». Loi n° 2023-87, art. L. 732-24-1 CRPM : « La Nation se fixe pour objectif de déterminer, à compter du 1er janvier 2026, le montant de la pension de base […] en fonction des vingt-cinq années civiles d'assurance les plus avantageuses » (`senat_tas22-049_retraite_agricole.html`). C'est une cible chiffrée dans une loi en vigueur, mais pas une loi de programmation au sens strict : cas limite, mis dans la borne haute seulement. L'iFRAP compte 0,018.
- **Médecins en formation, 0,1.** Montaigne chiffre 8 000 étudiants de plus (16 000 en 2027 contre 8 000 en 2017), donc à partir de 2017 et non de 2024. Une partie de la hausse est peut-être déjà réalisée (fixation pluriannuelle par voie réglementaire, hors P1-P3) : non vérifié, hors bornes.
- **Congé de naissance (0,4), complémentaire à 1 € (0,47), logements étudiants (0,6), rénovation (0,09), France services (0,03), fournitures (0,021)** : absents de la LFSS 2024 et du PStab, mesures nouvelles. Je n'ai pas recherché si un plan budgété existait pour les logements étudiants ou France services.
- Haut = 0,4 + 0,628 + 0,1 = 1,13.

## 3. Cas limites (part comprise 0, à trancher par l'intégrateur)

- **`ens_leasing`** (−1,3 ; borne haute 0,65). Montaigne chiffre le coût total de 100 000 véhicules en 2025, soit le double du dispositif 2024, bonus compris, et écrit aussi « soit 650 M€ additionnels pour 2025 ». Mais l'édition 2024 était ponctuelle : budget prévisionnel 110 M€, environ 300 M€ dépensés, suspension après quelques semaines (Sénat r25-504, `senat_r25-504-3_vehicules.html`). La fiche dit la mesure « soumise à l'adoption du projet de loi de finances 2025 pour l'ouverture des crédits ». Le PStab ne la mentionne pas, et la 2e édition (septembre 2025) a été financée par les CEE. Aucune part du coût 2025-2027 n'était donc budgétée au 30/06/2024 : 0. La borne 0,65 n'a de sens que si l'on tient le dispositif 2024 pour reconductible.
- **`nfp_superprofits`** (+15). Il peut recouper « Mesures fiscales énergéticiens et autres mesures sur les rentes 3,0 » (PStab, tableau 7, p. 41) si la contribution frappe les mêmes bénéfices. La fiche Montaigne ne mentionne pas le PStab. C'est la même question que `rn24_rente_infra` (agent A) : appliquer la même lecture aux deux. Le cas de `rn24_armateurs` (« autres mesures sur les rentes ») est de même nature, mais le PStab ne détaille pas ces mesures.
- **`nfp_petite_enfance`** (−5,7). Le montant est égal à 28,5 Md€ / 5 ans, le chiffrage Montaigne 2022 pour la même promesse : c'est une inférence arithmétique, Montaigne ne la fait pas en 2024. Ce chiffrage porte sur 500 000 places « supplémentaires » au stock de 2019. Le PStab cite le service public de la petite enfance (p. 13), sans montant : pas P3. Le plan de places de la CNAF (convention d'objectifs, hors LFSS) n'a pas été examiné. Recoupement possible, non chiffrable.
- **`rn24_production`**. La CVAE (LFI 2024 et PStab) est programmée, mais la ligne (5,1 = rendement de la C3S) l'exclut déjà, comme l'écrit Montaigne lui-même. À garder à 0.
- **`nfp_taxe_macron`, `ens_elec`**. C'est le cas inverse : la référence contient le retour de l'accise, et la ligne chiffre sa perte. Rien n'est compris (déjà noté par T24).
- **`rn24_enseignants`**. Le montant est repris du chiffrage 2022 (base de rémunérations 2022). Les revalorisations 2023 et le Pacte sont dans la base. Aucune part de la nouvelle revalorisation n'est financée par la référence, mais le calibrage du montant est fragile.

## 4. Lignes de la liste § 2 C examinées et non comprises

- `nfp_enseignants` : pas de méthode publiée. Pas de loi de programmation de l'Éducation nationale, et le PLF 2024 supprime 2 300 postes d'enseignants (Sénat l23-128-314).
- `nfp_point_indice`, `ens_agents_publics` : nouvelles hausses du point. Aucune n'est chiffrée dans le PStab ; les hausses de 2022 et 2023 sont dans la base.
- `nfp_logements_publics` : pas de méthode, aucune programmation.
- `nfp_soin_medicosocial` : « coût supplémentaire de la revalorisation », en plus de celles déjà accordées.
- `rn24_apprentissage` : « aide supplémentaire de 100 € par mois ». Les aides existantes sont dans la base (PStab p. 36, « objectif du million d'apprentis d'ici 2027 »).
- `ens_fraude`, `rn24_fraude` : l'iFRAP chiffre explicitement l'« écart […] par rapport à la trajectoire affichée […] dans le programme de stabilité ». Le surcroît est donc compté par construction, et le PStab n'a aucune mesure fraude chiffrée.
- `rn24_autres_dep_reste` : tous les postes sont nouveaux ou en surcroît (médecine : « par rapport au nombre actuel »).
- `nfp_autres_dep_reste` : la LPR (0,7) est chiffrée au-delà de la loi (« renforcer ce mouvement à hauteur d'1 Md€ à l'horizon 2030 ») ; MaPrimeRénov' « +10 points » ; bâtiments publics « +50 % » de l'enveloppe. Ce sont tous des surcroîts. Les postes déjà dans le tendanciel (rail, rénovation thermique, France services) sont mis à 0 par Montaigne.
- `nfp_vss` : Montaigne retranche lui-même le budget 2024 (0,5 Md€, DPT 2024).
- `nfp_culture_sport`, `nfp_emplois_aides`, `nfp_bio` : chiffrés nets de l'existant.

## 5. Non trouvé, endroits cherchés

- PAP 2024 (budget.gouv.fr) : pages non lisibles par l'outil, et fichiers AN protégés contre curl. J'ai utilisé à la place le PAP 2025 (colonne LFI 2024) et les rapports du Sénat sur le PLF 2024. Les montants du Pacte enseignant et du leasing 2024 sont donc ceux du PLF ou de sources parlementaires, pas de la LFI : confiance medium.
- Ventilation du Pacte enseignant entre remplacement et autres missions : non trouvée.
- Montant ONDAM 2024 associé aux fauteuils roulants : non trouvé (l'amendement dit l'impact non connu).
- Méthodes Montaigne 2024 de `nfp_enseignants`, `nfp_logements_publics`, `nfp_gul` : aucune fiche (constat T22).
- Avis du HCFP sur le PStab 2024 : non recherché (déjà non trouvé par T24).

## 6. Points pour l'intégrateur

1. Deux lignes Ensemble remplissent P2 ; aucune ligne NFP ni RN (hors `rn24_prisons`, agent A). C'est le résultat qui ressort de l'examen et doit être publié tel quel, sans chercher à équilibrer les programmes.
2. `ens_snu` : facteur proposé 1 − 0,16/3,6 ≈ 0,956 (ou part fixe de 0,16).
3. `ens_autres_dep_reste` : part centrale 0,4 (fauteuils) ; la fourchette 0 à 1,13 tient à la lecture de P2 (base légale sans crédit) et au Pacte.
4. Symétrie à vérifier avec l'agent A : même lecture pour `nfp_superprofits` et `rn24_rente_infra` face aux « 3,0 » du PStab.
5. `ens_leasing` : 0 au critère, mais le texte même de Montaigne (« 650 M€ additionnels ») mérite une mention sur la fiche.
