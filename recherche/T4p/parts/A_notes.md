# T4p, partie A : revenus du capital et IS (accès 2026-10-14)

## Trouvé (sources primaires lues et archivées dans sources/T4p/A_*)
- **LFSS 2026** (loi 2025-1403, JO du 31/12/2025, art. 12) : la CSG sur les revenus du capital passe de 9,2 % à 10,6 %. Les prélèvements sociaux passent à 18,6 % et le PFU à 31,4 %. Restent à 9,2 % de CSG (17,2 % de PS) : revenus fonciers, PV immobilières, assurance-vie, PEL, CEL et PEP (art. L.136-8 IV CSS ; amendement gouvernemental n°1104 ; service-public F2329).
  - Date d'effet : 1/1/2026 pour les produits de placement prélevés à la source (dividendes, intérêts).
  - Pour les revenus du patrimoine (L.136-6, dont les PV mobilières), la hausse vaut dès l'imposition des revenus 2025.
  - La part de CSG déductible reste à 6,8 %.
- **CEHR** : 3 % / 4 %, sans changement. Le RFR réintègre l'abattement de 40 % (BOFiP).
- **CDHR** (taux minimal de 20 %) : la LF 2026 (art. 2) l'a prorogée jusqu'à ce qu'une loi de règlement constate un déficit inférieur à 3 % du PIB. Elle est donc en vigueur pour les revenus 2026. Le PLF 2027 (état A) en attend 0,6 Md€.
- **Contribution exceptionnelle IS** : LF 2025 art. 48, puis LF 2026 art. 12 (loi 2026-103 du 19/02/2026), commentée au BOFiP du 12/08/2026.
  - Exercice 2025 : 20,6 % de l'IS pour un CA de 1 à 3 Md€, 41,2 % au-delà de 3 Md€.
  - Exercice 2026 : mêmes taux, mais seuil relevé à 1,5 Md€.
  - L'assiette est la moyenne de l'IS de l'exercice et de l'exercice précédent.
  - Taux marginaux statutaires (IS + CSS 3,3 % + surtaxe) : 30,98 % et 36,13 %.
  - Rendement 2026 d'environ 7,0 Md€ : déduit du PLF 2027 (« 5,0 Md€, en diminution de 2,0 Md€ par rapport à 2026 »). Rendement 2025 : 8 Md€ selon le gouvernement (exposé de l'amendement n°3541).
- **PLF 2027** (déposé le 1/10/2026, art. 15) : 3e exercice à 15,7 % / 31,4 %, seuil 1,5 Md€, rendement 5,0 Md€ (5,2 Md€ dans l'état A). Ce n'est qu'un projet.

## Taux marginaux effectifs, foyer TMI 45 % et CEHR 4 % (formules dans la colonne `note`)
- Dividendes au barème : 46,27 % (sans CEHR : 42,54 %). Dividendes au PFU : 35,4 % (31,4 % sans CEHR ; 38,6 % si la CDHR est contraignante).
- Intérêts et PV mobilières au barème (sans abattement) : 64,27 %. Au PFU : 35,4 %.
- Un foyer à la TMI 45 % a donc toujours intérêt au PFU.

## Non trouvé / tentatives
- **Répartition des dividendes par TMI** : non trouvée. J'ai cherché dans France Stratégie (note 2022), à la DGFiP et à l'IPP. Je n'ai trouvé qu'une concentration : 62 % des dividendes vont au 0,1 % des foyers en 2020. Le taux moyen pondéré n'est donc donné qu'en fourchette, 31,4 à 35,4 % (confiance low). Note : le rapport final 2023 de France Stratégie, archivé par l'agent B (B_fs2023_rapport_final_fiscalite_capital.pdf), pourrait contenir mieux ; je ne l'ai pas exploité.
- **Rendement de la hausse de CSG sur le capital** : environ 1,5 Md€ selon legifiscal (secondaire, non lu). Rien de primaire trouvé.
- **Légifrance** renvoie un 403 à curl. Le texte de la LF 2026 a donc été lu à travers les commentaires du BOFiP, pas directement.

## Vigilance
- L'assiette en moyenne sur deux ans fait que le taux marginal sur l'année seule est plus bas : 28,40 % au lieu de 30,98 %, et 30,98 % au lieu de 36,13 % (val_bas).
- PV mobilières : le taux de 18,6 % s'applique dès les plus-values 2025 (effet rétroactif). Le cas des titres acquis avant 2018, avec abattement pour durée de détention, n'est pas calculé.
- Le traitement exact des dividendes au PFU dans le revenu de référence de la CDHR n'a pas été vérifié dans BOI-IR-CDHR-10.
