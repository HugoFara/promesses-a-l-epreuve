# T25 : dépenses et recettes des programmes 2024 déjà comprises dans la référence

Rapport d'intégration du 22/10/2026 (issue #10). Consigne : `CONSIGNE.md`. Détail : `parts/prisons_rente.md` (agent A, `rn24_prisons` et `rn24_rente_infra`), `parts/notes_B.md` et `parts/lignes_B.csv` (agent B, 87 autres lignes). Une ligne par ligne de programme dans `lignes_2024.csv` (89 lignes) ; sources dans `sources.csv` et `sources/T25/`.

## 1. Résultat

| Ligne | Montant | Critère | Part comprise (centrale ; fourchette) | Confiance |
|---|---|---|---|---|
| `rn24_prisons` | −1,5 | P1 + P2 | 1,39 ; 1,34 à 1,44 | medium |
| `ens_snu` | −3,6 | P2 | 0,16 ; 0,16 à 0,3 | medium |
| `ens_autres_dep_reste` | −2,911 | P2 | 0,4 ; 0 à 1,13 | medium |
| `rn24_rente_infra` | +3 | non établi | 0 à 3 | medium |

Les 85 autres lignes : aucune part comprise. NFP 2024 : aucune ligne concernée.

Citations clés relues par l'intégrateur sur les sources archivées (PAP 2024 Justice, NEB 2023 Justice de la Cour des comptes, PAP 2025 Sport, jeunesse et vie associative, amendement n° 3294 au PLFSS 2024, fiche Montaigne SNU).

## 2. `rn24_prisons`

- **Ce que chiffre Montaigne** (micro-chiffrages RN, p. 3) : les quelque 12 000 places du plan 15 000 restant à livrer, à 370 000 € la place (4,44 Md€ sur 3 ans), au calendrier du plan, sans accélération ni extension.
- **Référence** : loi n° 2023-1059, art. 1er (crédits de la mission Justice 10 081 M€ en 2024 à 10 748 M€ en 2027) et rapport annexé § 2.3.1.2 (« poursuivre et […] finaliser » le plan) ; PAP 2024 Justice : « Les opérations menées au titre du plan 15 000 (AE : 524,4 M€ et CP : 308,4 M€) ».
- **Ce qui n'est pas financé** : Cour des comptes, NEB 2023 Justice (avril 2024) : coût APIJ « à hauteur de 5,87 Mds€. Par ailleurs, 117,5 M€ ne sont pas encore financés » ; hypothèse de l'administration pénitentiaire : 303 M€ de surcoûts en plus. Soit 117,5 à 420 M€, 2,6 à 9,5 % du coût chiffré par Montaigne.
- **Limites** : « financé » s'entend au sens des autorisations d'engagement ; l'enveloppe de la loi de programmation n'est pas ventilée par opération ; les annulations de février 2024 (−103 à −124 M€ sur le programme 107 hors personnel) ne sont pas isolées pour l'immobilier ; une partie des paiements tombe après 2027 (effet de calendrier non chiffrable).

## 3. `ens_snu` et `ens_autres_dep_reste`

- `ens_snu` : Montaigne chiffre le coût complet d'un SNU généralisé (« 4 218 € par jeune […] 3,6 Md€ pour une cohorte de 870 000 jeunes ») sans retrancher le SNU existant, doté de 160,0 M€ en LFI 2024 (PAP 2025, colonne LFI 2024 : « 06 – Service National Universel 160 047 188 »). Borne haute 0,3 : l'équipe de campagne, citée par Montaigne (« dont 0,3 Md€ déjà prévus dans la trajectoire ») ; le programme de stabilité ne cite pas le SNU.
- `ens_autres_dep_reste`, poste « fauteuils roulants » (0,4) : l'art. 85 de la LFSS 2024 est l'amendement du Gouvernement qui « a pour objet d'assurer un remboursement intégral pour les fauteuils roulants » ; base légale votée, mais « l'impact financier […] dépendra de la négociation des conditions tarifaires » : le montant n'est pas inscrit. Borne haute : remplacement des absences (0,7, Pacte enseignant de 628 M€ au PLF 2024, part non chiffrée) et retraites agricoles (0,1, loi n° 2023-87). La critique de l'iFRAP (« déjà inscrites au budget ») est confirmée pour les fauteuils, en partie pour les remplacements.

## 4. `rn24_rente_infra` et `nfp_superprofits`

Même cible, même instrument annoncé et même montant (3 Md€) que les « Mesures fiscales énergéticiens et autres mesures sur les rentes » du programme de stabilité (tableau 7, p. 41). Mais le périmètre de l'annonce n'est « pas clairement défini » (Sénat, n° 559), le programme de stabilité ne la chiffre que pour 2024, et l'iFRAP dit mesurer un écart à ce programme. Non établi. Sans effet sur le solde : la ligne est en règle « Recette ponctuelle » (facteur 0), comme `nfp_superprofits`, que l'agent B signale pour le même recoupement possible. Les deux lignes gardent leur traitement actuel.

## 5. Cas limites (part comprise nulle, notés)

`ens_leasing` (édition 2024 ponctuelle, aucune édition 2025 budgétée) ; `nfp_petite_enfance` (service public de la petite enfance cité sans montant par le programme de stabilité) ; `rn24_production` (baisse de la CVAE déjà exclue du montant) ; `nfp_taxe_macron`, `ens_elec` (cas inverse : la référence contient la recette que la ligne fait perdre) ; médecins en formation (0,1, résidu Ensemble, non vérifié). Détail : `parts/notes_B.md`.

## 6. Lacunes

PAP 2024 lus en version PLF (budget.gouv.fr et Légifrance refusent les accès automatisés) ; non trouvés : échéancier propre au plan 15 000, part du Pacte enseignant consacrée aux remplacements, enveloppe de l'ONDAM 2024 pour les fauteuils, effet des annulations de février 2024 sur le SNU et sur l'immobilier pénitentiaire, mécanisme de la mesure « rentes » du Gouvernement.

## 7. Proposition de l'intégrateur (à valider)

Même mécanisme qu'en T24 : `statut_reference` `partielle`, `facteur_reference` = part non comprise, montant du chiffreur inchangé. `application_lignes.csv` n'a pas de colonnes de fourchette pour le facteur de référence : la fourchette va dans `source_reference`.

| Ligne | `facteur_reference` | Compté | Effet sur le solde |
|---|---|---|---|
| `rn24_prisons` | 0,06 (0,026 à 0,095) | −0,09 | +1,41 |
| `ens_snu` | 0,956 (0,917 à 0,956) | −3,44 | +0,16 |
| `ens_autres_dep_reste` | 0,863 (0,612 à 1) | −2,51 | +0,40 |

Effet sur les soldes centraux : RN 2024 +1,4 ; Ensemble 2024 +0,6 ; NFP 2024 inchangé. `rn24_rente_infra` et `nfp_superprofits` : pas de changement de valeur ; la fiche de `rn24_rente_infra` mentionne le recoupement possible.

Validée par l'utilisateur et appliquée le 22/10/2026 (`corrections.csv`, 11 valeurs, dont la mention du recoupement possible dans la justification de `rn24_rente_infra` et de `nfp_superprofits`). Soldes corrigés : Ensemble 2024 −20,7 → −20,15 ; RN 2024 −54,5 → −53,06 ; NFP 2024 inchangé (−157,6).
