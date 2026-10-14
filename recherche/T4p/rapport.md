# T4p : paramètres de barème pour le moteur de calcul (accès 2026-10-14)

## Livrables

- `parametres_moteur.csv` : 131 paramètres, colonnes `id,parametre,val_bas,val_central,val_haut,unite,annee,url,citation,page,confiance,note`. Confiance : 109 high, 15 medium, 7 low.
- `sources.csv` : 59 documents archivés dans `sources/T4p/`, plus 2 de `sources/T6/`. Les sha256 ont été revérifiés à la fusion.
- `parts/` : les CSV et notes des quatre volets (A capital/IS, B patrimoine/successions, C carburants, D Smic/recours/retraites), produits par des sous-agents puis fusionnés sans modification.

Les fourchettes (`val_bas`/`val_haut`) ne sont remplies que si elles sont publiées ou dérivées explicitement. La colonne `note` dit laquelle des deux. Montants budgétaires : impact sur le solde, négatif = creuse le déficit.

## Résultats principaux

| Thème | Paramètre | Valeur | Source |
|---|---|---|---|
| Capital | PFU 2026 | 31,4 % (12,8 + 18,6). CSG capital de 9,2 à 10,6 %, LFSS 2026 art. 12. Exclus de la hausse : foncier, assurance-vie, PEL/CEL | high |
| Capital | TMI effectif dividendes au barème, tranche 45 % + CEHR 4 % | 46,27 % (42,54 % sans CEHR) ; au PFU 35,4 % | dérivé, high |
| Capital | TMI effectif intérêts et PV au barème, tranche 45 % + CEHR 4 % | 64,27 % ; au PFU 35,4 % | dérivé |
| Capital | CDHR (taux minimal 20 %) | prorogée par la LF 2026 tant que le déficit est ≥ 3 % | high |
| Capital | t1 moyen pondéré sur les dividendes | 31,4 à 35,4 % (répartition par TMI non trouvée) | low |
| IS | Surtaxe 2025 | 20,6 % de l'IS pour un CA de 1 à 3 Md€ ; 41,2 % au-delà de 3 Md€ | high |
| IS | Surtaxe 2026 | mêmes taux, seuil 1,5 Md€ ; rendement ≈ 7,0 Md€ | high / medium |
| IS | Surtaxe 2027 | PLF : 15,7 / 31,4 % ; 5,0 Md€ | high |
| IS | Taux marginal statutaire | 30,98 % et 36,13 % (28,40 et 30,98 % sur l'année seule, l'assiette étant une moyenne sur deux ans) | dérivé |
| ISF | Barème 2017 | 0,5 / 0,7 / 1 / 1,25 / 1,5 % ; seuil 1,3 M€ ; rendement 4,2 Md€ ; taux moyen 0,41 % | high / medium |
| ISF | NFP 2024 | pas de barème publié ; 15 Md€ annoncés | high |
| ISF | LFI, PLF 2026 (amdt I-2360) | 0,5 à 5 % ; 10 Md€ annoncés | high |
| Patrimoine | Taxe Zucman | 2 % au-delà de 100 M€ ; assiette 1 228 Md€ (500 fortunes) ; 20 Md€ [15-25] ; 2-3 Md€ si l'IS est imputé | high / medium |
| Successions | Ligne directe | 5 à 45 %, abattement 100 k€ ; taux moyen effectif 5 % (ensemble), 2-3 % (ligne directe), ≈ 10 % (top 0,1 %) ; rendement ≈ 15 Md€ | high |
| Carburants | Gazole | 1,619 €/l TTC (2025) ; 2,028 (janv.-sept. 2026) | high |
| Carburants | GNR | 1,192 €/l TTC (2025) | high |
| Carburants | Accise 2026 | gazole 60,75 €/hl ; GNR BTP 36,79 ; GNR agricole 3,86 ; remboursement TRM 15,56 | high |
| Niches brunes | Budget vert PLF 2026 | 8,13 Md€ (dépenses fiscales 6,38) : GNR agricole 1,69 ; TRM 1,18 ; GNR BTP 0,47 | high |
| Niches brunes | Hausse de prix si suppression | GNR agricole +79 % (+53 % aux prix 2026) ; GNR BTP +23 % (+17 %) ; TRM +12 % (+9 %) | dérivé, medium |
| Smic | Net mensuel | 1 398,70 € (janv. 2024) ; 1 443,11 € (janv. 2026), puis 1 477,93 € (juin 2026) | high |
| Smic | Bénéficiaires de la revalorisation | 2,2 M (12,4 %) au 1/11/2024 | high |
| Smic | Coût d'un emploi perdu | 15,1 à 17,2 k€/an, dérivé (ARE 1 055 €/mois + cotisations salariales) | low |
| Smic | Smic à 1 600 € (Montaigne) | −19 Md€ [−17 ; −21] = allègements −21,5 + masse salariale publique −3,7 + prélèvements +6. Hors effets emploi (300 k emplois) et hors chômage | high |
| Non-recours | RSA | 33-37 % (T4 2021, DREES ER 1370) ; 34 % (2018) | high |
| Retraites | Réforme 2023, gain en 2027 | brut +10,3 ; net +6,2 (+7,7 avec recettes) ; ≈ +4,1 net des autres prestations (dérivé) | high / medium |
| Retraites | Suspension (LFSS 2026 art. 105) | −0,3 Md€ (2026), −1,9 Md€ (2027), somme dérivée ; PLFSS 2027 : +1,0 Md€ de prestations en 2027 | medium |

## Lacunes

- Répartition des dividendes par tranche marginale : non trouvée (France Stratégie 2021-2023, DGFiP, IPP). J'ai aussi cherché dans le rapport final 2023 de France Stratégie, qui ne donne qu'une concentration (62 % au top 0,1 %) et le taux marginal de prélèvement par TMI (tableau p. ~150).
- Couverture du CEJ et de la Garantie jeunes, non-recours à la prime d'activité (non estimable selon la DREES 2022). Faute de chiffre, pas de taux de recours sourcé pour une nouvelle prestation jeunes.
- Coût budgétaire direct d'un emploi perdu au Smic (seulement dérivé). Coût de l'exonération du kérosène, budget vert du PLF 2027, élasticité-prix des carburants, chiffrage officiel (DGFiP/Trésor) de la taxe Zucman, recettes DMTG 2024-2026.
- Légifrance est inaccessible (403/Cloudflare). La LF 2026 a été lue via le BOFiP et service-public. Absence de modification de l'art. 777 en LF 2026 : confirmée seulement par une source secondaire.
- Le quota de recherches web a été épuisé en fin de tâche par les volets B et D.

## Décisions laissées à l'intégrateur

1. **Année de prix des carburants** : 2025 ou 2026 (choc pétrolier, gazole HT +46 %). Les hausses en % diffèrent d'un tiers.
2. **Smic 2026** : valeur de janvier, de juin ou moyenne annuelle (1 463,4 € net, dérivée).
3. **t1 capital** : sans répartition par TMI, prendre 35,4 % (PFU + CEHR) pour les hauts revenus, ou la borne 31,4 %.
4. **CEHR sur les dividendes** : `div_tmi_45` (46,27 %) assied la CEHR sur 100 % du dividende, car le RFR réintègre l'abattement de 40 %. France Stratégie 2023 (tableau 7, barème 2013-2017, ligne `div_tmi_45_2013_2017_fs`) l'assied sur 60 %. Avec cette convention, on obtient 44,78 %. À vérifier dans le BOFiP CEHR avant de figer la valeur.
5. **IS** : taux marginal statutaire, ou taux sur l'année seule (val_bas).
6. **Réforme 2023** : choisir le périmètre (système de retraite ou ROBSS ; net ou non des autres prestations). Ne pas additionner les 0,8 Md€ de « rendement net de la suspension » du PLFSS 2027, qui sont un écart d'une année sur l'autre.
7. **Chiffrages de parti (NFP, LFI, Zucman)** : ce sont ceux des auteurs, statiques. Le moteur doit leur appliquer les élasticités, comme aux autres.

---

# Notes détaillées par volet

## T4p, partie A : revenus du capital et IS (accès 2026-10-14)

### Trouvé (sources primaires lues et archivées dans sources/T4p/A_*)
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

### Taux marginaux effectifs, foyer TMI 45 % et CEHR 4 % (formules dans la colonne `note`)
- Dividendes au barème : 46,27 % (sans CEHR : 42,54 %). Dividendes au PFU : 35,4 % (31,4 % sans CEHR ; 38,6 % si la CDHR est contraignante).
- Intérêts et PV mobilières au barème (sans abattement) : 64,27 %. Au PFU : 35,4 %.
- Un foyer à la TMI 45 % a donc toujours intérêt au PFU.

### Non trouvé / tentatives
- **Répartition des dividendes par TMI** : non trouvée. J'ai cherché dans France Stratégie (note 2022), à la DGFiP et à l'IPP. Je n'ai trouvé qu'une concentration : 62 % des dividendes vont au 0,1 % des foyers en 2020. Le taux moyen pondéré n'est donc donné qu'en fourchette, 31,4 à 35,4 % (confiance low). Note : le rapport final 2023 de France Stratégie, archivé par l'agent B (B_fs2023_rapport_final_fiscalite_capital.pdf), pourrait contenir mieux ; je ne l'ai pas exploité.
- **Rendement de la hausse de CSG sur le capital** : environ 1,5 Md€ selon legifiscal (secondaire, non lu). Rien de primaire trouvé.
- **Légifrance** renvoie un 403 à curl. Le texte de la LF 2026 a donc été lu à travers les commentaires du BOFiP, pas directement.

### Vigilance
- L'assiette en moyenne sur deux ans fait que le taux marginal sur l'année seule est plus bas : 28,40 % au lieu de 30,98 %, et 30,98 % au lieu de 36,13 % (val_bas).
- PV mobilières : le taux de 18,6 % s'applique dès les plus-values 2025 (effet rétroactif). Le cas des titres acquis avant 2018, avec abattement pour durée de détention, n'est pas calculé.
- Le traitement exact des dividendes au PFU dans le revenu de référence de la CDHR n'a pas été vérifié dans BOI-IR-CDHR-10.

## T4p – partie B (patrimoine, successions) : notes

Date d'accès : 2026-10-14. Valeurs dans `B_patrimoine_succ.csv`, sources dans `B_sources.csv` (fichiers archivés sous `sources/T4p/B_*`).

### Trouvé

- **Barème ISF 2017** (BOFiP BOI-PAT-ISF-40-10, version en vigueur 2013-2018) : 0 / 0,5 / 0,7 / 1 / 1,25 / 1,5 %, seuils 0,8 / 1,3 / 2,57 / 5 / 10 M€ ; seuil d'assujettissement 1,3 M€ ; décote entre 1,3 et 1,4 M€.
- **Rendement ISF 2017** : 4,2 Md€ (France Stratégie, rapport final 2023). DGFiP via fgeerolf : 4,226 Md€ nets, 358 198 foyers, patrimoine net taxable 1 028,8 Md€, donc un **taux moyen effectif de 0,41 %** (calculé par moi). France Stratégie : 0,45 % pour le top 0,1 %, 0,71 % pour le top 1 %, 0,51 % pour le top 10 % (2017).
- **NFP 2024** : le programme dit « ISF renforcé avec un volet climatique », **sans barème**. Le document macro du NFP chiffre la mesure à 15 Md€ et l'« impôt sur les successions dorées » (héritage maximal de 12 M€) à 17 Md€.
- **LFI, PLF 2026** : amendement I-2360 (« de repli », sans composante climatique), rejeté. Seuil 1,3 M€ ; taux 0 / 0,5 / 0,7 / 1 / 1,5 / 2 / 3 / 4 / 5 % ; seuils 0,8 / 1,3 / 2 / 3 / 5 / 10 / 100 / 1 000 M€. Recettes annoncées : 10 Md€.
- **Taxe Zucman** (PPL n° 768) : 2 % au-delà de 100 M€, impôt plancher (les impôts directs déjà payés sont déduits). Estimation de Zucman : 20 Md€ [15-25], sur une assiette de 1 228 Md€ (les 500 plus grandes fortunes selon Challenges 2024, rapport Sénat n° 689 p. 41). Si l'IS est imputé : 2-3 Md€ (A. Levy, rapport Sénat). Le Sénat note aussi que le départ des trois plus grandes fortunes réduirait le rendement de moitié (-10 Md€).
- **Exil fiscal, CAE Focus 118** (communiqué) : +1 pt de taux effectif → +0,02 à 0,23 % d'expatriations à long terme. Dans le contexte scandinave, la marge intensive pèse environ 2,5 fois la marge extensive.
- **DMTG en ligne directe en 2026** : 5 / 10 / 15 / 20 / 30 / 40 / 45 %, seuils 8 072 / 12 109 / 15 932 / 552 324 / 902 838 / 1 805 677 € ; abattement de 100 000 €.
- **Taux moyen effectif DMTG** : 5 % de l'ensemble des transmissions en 2015 ; 2-3 % en ligne directe ; environ 25 % sans enfant (France Stratégie 2017). CAE n° 69 : à peine 10 % pour le top 0,1 %.
- **Recettes DMTG** : 15 Md€ (CAE 2021, « système actuel ») ; 12,5 Md€ en 2015 (France Stratégie) ; flux transmis > 300 Md€.

### Non trouvé / tentatives

- **Légifrance** (art. 777, 885 U, LF 2026) : bloqué par Cloudflare, en curl comme en WebFetch. J'ai utilisé à la place BOFiP et service-public.
- **LF 2026 (loi n° 2026-103 du 19/02/2026)** et art. 777 : la fiche service-public a été vérifiée le 09/02/2026, donc avant la promulgation. L'absence de modification de l'art. 777 n'est confirmée que par une source secondaire (Legare). **À vérifier sur Légifrance.** Legare signale un nouvel art. 788 III bis (beaux-enfants : abattement de 15 932 €, taux de 60 %).
- **Chiffrage officiel de la taxe Zucman** (DGFiP, Trésor, CAE, rapport général PLF 2026) : non trouvé. Le quota de recherches web de la session a été épuisé en cours de tâche.
- **Recettes DMTG 2024-2026** (Voies et moyens) : non trouvées, pour la même raison.
- **PDF du CAE Focus 118** : URL introuvable. Seul le communiqué a été lu.
- **Barème « climatique » LFI** (amendement principal) : non trouvé. Les votes datan.fr évoquent l'amendement 2360 « avec composante climatique », mais son texte se dit « de repli » et ne contient pas de composante climatique.

### Vigilance

- Rendement de l'ISF : 4,2 Md€ (2017) ne vaut pas 5 Md€. Le contrefactuel 2022 de France Stratégie est de 6,3 Md€ (perte de 4,5 Md€).
- Les chiffrages NFP, LFI et Zucman sont ceux des auteurs : statiques, sans réaction comportementale.
- Taxe Zucman : le seuil de 100 M€ concerne environ 4 000 foyers selon la PPL, mais 1 600 à 1 800 selon Zucman au Sénat. L'assiette de 1 228 Md€ couvre les 500 plus grandes fortunes, pas l'ensemble des patrimoines au-delà de 100 M€.
- Plusieurs PDF ont été récupérés via web.archive.org (sites d'origine en 404, 403 ou refus TLS). L'URL d'archive est indiquée dans `B_sources.csv`.
- Les données ISF de fgeerolf sont une reproduction secondaire de fichiers DGFiP (confiance medium).

## T4p – partie C : carburants / niches brunes

### Trouvé (sources primaires)
- Prix DGEC (xlsx officiel) : gazole routier 2025 = 1,6186 €/l TTC (HTT 0,7396) ; janv.-sept. 2026 = 2,028 €/l TTC en moyenne simple des mois (HTT 1,083), avec un pic de 2,33 en septembre. GNR (livraisons < 5 000 l, au tarif GNR général) : 1,1922 €/l TTC en 2025, 1,694 en janv.-sept. 2026.
- Accise 2026 (circulaire douane du 30/09/2026, mêmes valeurs en mars et juillet) : gazole 60,75 €/hl ; GNR hors agriculture (U173) 36,79 ; GNR agricole et forestier (U820) 3,86 ; ferroviaire 18,82 ; kérosène aviation commerciale exonéré.
- Remboursement TRM : 15,56 €/hl (taux plancher 45,19) ; voyageurs : 21,56 €/hl (plancher 39,19) (service-public, vérifié le 11/03/2026). Taxis : 30,55 €/hl (taux 2024, le dernier affiché par la douane).
- Budget vert PLF 2026 (CSV data.gouv) : dépenses défavorables = 8,13 Md€ (crédits 1,44 ; dépenses fiscales 6,38 ; taxes affectées 0,31). Principales niches : GNR agricole (800229) 1,693 Md€ ; outre-mer art. 73 (800401) 1,466 ; TRM (800221) 1,178 ; GNR hors agriculture (800201) 0,466 ; taxis 0,059.

### Hausses de prix (dérivées, base HT car la TVA est récupérable ; avec une TVA de 20 % sur les deux termes, le % est identique en TTC)
- GNR agricole : 0,5689 / (0,6855 + 0,0386) = +78,6 % (prix 2025), +52,6 % (prix 2026).
- GNR hors agriculture : 0,2396 / 1,0534 = +22,7 % (2025), +17,0 % (2026).
- TRM : 0,1556 / 1,3471 = +11,6 % (2025), +9,2 % (2026).
- Taxis : +22,7 % (2025, avec le taux 2024).

### Non trouvé / tentatives
- PDF du rapport « Impact environnemental du budget de l'État » PLF 2026 : budget.gouv.fr bloque curl (Incapsula). J'ai utilisé le jeu de données officiel à la place, et le recoupement fonctionne : la baisse de 1,27 Md€ par rapport à la LFI 2025 correspond à la « baisse de 1,3 milliard » rapportée par Acteurs publics.
- Budget vert PLF 2027 : rien trouvé au 14/10/2026 (ni sur data.gouv, ni par recherche web).
- Coût de l'exonération du kérosène : ce n'est pas une dépense fiscale du budget vert. Le prix du carburéacteur n'est pas publié par la DGEC, donc la hausse n'est pas calculée.
- Taux de remboursement taxis 2025/2026 : non affichés. Trajectoire GNR de la LF 2024 jusqu'en 2030 : pas lue sur le texte de loi.
- Élasticité-prix : rien dans les sources lues (le PDF du rapport n'a pas été lu).

### Vigilance
- 2026 est une année de choc pétrolier (gazole HTT +46 % par rapport à 2025) : les % calculés sur les prix 2026 sont plus faibles. L'intégrateur doit choisir l'année de référence.
- Les montants TRM et taxis sont reconduits à l'identique de 2024 à 2026 (chiffrage probablement non actualisé).
- La ligne 800229 inclut aussi les fiouls lourds et le GPL agricoles. Le prix HTT du GNR agricole est supposé égal à celui de la série GNR.
- Des aides exceptionnelles carburant existent en 2026 (GNR agricole, transporteurs), repérées par recherche web mais non vérifiées : à ne pas confondre avec les tarifs réduits.

## T4p, partie D : Smic, non-recours, retraites (notes)

Date d'accès : 2026-10-14. Toutes les valeurs, avec leur citation et leur page, sont dans `D_smic_recours_retraites.csv`. Les sources sont dans `D_sources.csv`.

### Trouvé

- **Smic** (Insee, service-public, info.gouv) :
  - 2024 : 1 766,92 € brut et 1 398,70 € net au 1er janvier ; 1 801,80 € brut et 1 426,30 € net au 1er novembre.
  - 2026 : 1 823,03 € brut et 1 443,11 € net au 1er janvier ; **nouvelle revalorisation au 1er juin 2026** (arrêté du 22/05/2026), à 1 867,02 € brut et 1 477,93 € net.
- **Bénéficiaires des revalorisations** (Dares, publication du 29/10/2025) : 2,2 M de salariés (12,4 %) au 1er novembre 2024. Avant : 2,7 M (14,6 %) au 1er janvier 2024 et 3,1 M (17,3 %) au 1er janvier 2023. Aucune publication trouvée pour janvier 2026.
- **ARE** (Unédic, T1 2026) : 1 055 € nets par mois en moyenne ; 881 € pour les allocataires de niveau inférieur au bac.
- **Smic à 1 600 € (Montaigne, 24/06/2024)** : 19 Md€ (fourchette 17-21). Décomposition : −21,5 d'allègements, −3,7 de masse salariale publique, +6 de prélèvements, soit −19,2.
  - Les effets emploi (300 000 emplois perdus, fourchette 230-380 k) et l'assurance chômage sont **exclus** du chiffrage.
  - La prime d'activité n'est pas isolée.
  - Premier chiffrage du 20/06/2024 : 3,5 Md€.
- **Non-recours au RSA** : 33-37 % au T4 2021 (DREES, ER 1370, mai 2026) ; 34 % en 2018 (Dossiers de la DREES n° 92).
- **Réforme 2023, en 2027** (rapport annexé au PLFRSS, janvier 2023) :
  - brut : 10,3 Md€ (système de retraite) ;
  - net des mesures d'accompagnement : 6,2 ;
  - avec les recettes nouvelles : 7,7.
- **Suspension (art. 105 LFSS 2026)** :
  - lettre rectificative : 0,1 Md€ en 2026 et 1,4 Md€ en 2027 ;
  - amendement gouvernemental n° 2686 (adopté) : +0,2 et +0,5 ;
  - **total dérivé : 0,3 et 1,9 Md€**.
  - PLFSS 2027 (n° 3211, 01/10/2026) : la suspension ajoute 1,0 Md€ aux prestations vieillesse des régimes de base en 2027.

### Non trouvé (tentatives)

- **Coût budgétaire d'un emploi perdu au Smic** : aucun chiffre direct.
  - Dérivation `cout_emploi_perdu` : ARE + (brut − net) × 12, soit 15,1 à 17,2 k€ par an. Confiance basse.
  - Non inclus : cotisations patronales résiduelles, effets RSA et prime d'activité, non-indemnisation d'une partie des chômeurs.
  - Pistes non lues : modèle DG Trésor, Cour des comptes.
- **Non-recours à la prime d'activité** : la DREES (2022) dit qu'il n'est pas estimable avec les données disponibles. Le taux de recours « ~50 % » souvent cité n'a pas été vérifié.
- **Couverture CEJ / Garantie jeunes** : non trouvée.
  - Le site Dares bloque curl et WebFetch (WAF) ; les PDF Dreets PACA ne sont plus servis.
  - Le quota de recherches web partagé a été épuisé en cours de tâche.
- **Rendement de la réforme 2023 en 2027 net des autres prestations** : non publié. Le val_bas 4,1 est dérivé avec le ratio de 20 % cité par la Cour des comptes (2025, p. 67).
- **Coût global officiel de la suspension après amendements** : la loi n'en donne pas, et le PLFSS 2027 ne donne pas de total explicite.

### Vigilance

- **Signe** : les colonnes budgétaires sont en impact sur le solde (négatif = creuse le déficit). Les montants Smic et ARE sont en niveau.
- **Smic 2026** : deux valeurs dans l'année. La moyenne annuelle dérivée est de 1 848,7 € brut et 1 463,4 € net. L'intégrateur choisit la valeur à retenir.
- **Champs différents pour la réforme 2023** :
  - système de retraite (base et complémentaires) ou ROBSS seuls (6,7 Md€ en 2027 avant accompagnement) ;
  - l'étude d'impact du PLFRSS s'arrête en 2026 ;
  - les 9,7 et 11,8 Md€ de la Cour des comptes portent sur 2030 en € 2024.
- **PLFSS 2027** : les « 0,8 Md€ en 2027 / 1,9 en 2028 » de rendement net de la suspension semblent être des **gains supplémentaires d'une année sur l'autre** (champ ROBSS), pas des niveaux. Ne pas les additionner aux autres valeurs.
- **Montaigne** : site derrière un captcha, page lue via Wayback (20240710). Le chiffrage de 19 Md€ suppose une hausse en euros constants, en plus de l'indexation.
- **Sources secondaires** : le ratio du groupe d'experts Smic 2017 (−240 M€ par point de Smic) a été lu chez Montaigne, pas dans le rapport.
