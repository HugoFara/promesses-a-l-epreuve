# T4p – partie C : carburants / niches brunes

## Trouvé (sources primaires)
- Prix DGEC (xlsx officiel) : gazole routier 2025 = 1,6186 €/l TTC (HTT 0,7396) ; janv.-sept. 2026 = 2,028 €/l TTC en moyenne simple des mois (HTT 1,083), avec un pic de 2,33 en septembre. GNR (livraisons < 5 000 l, au tarif GNR général) : 1,1922 €/l TTC en 2025, 1,694 en janv.-sept. 2026.
- Accise 2026 (circulaire douane du 30/09/2026, mêmes valeurs en mars et juillet) : gazole 60,75 €/hl ; GNR hors agriculture (U173) 36,79 ; GNR agricole et forestier (U820) 3,86 ; ferroviaire 18,82 ; kérosène aviation commerciale exonéré.
- Remboursement TRM : 15,56 €/hl (taux plancher 45,19) ; voyageurs : 21,56 €/hl (plancher 39,19) (service-public, vérifié le 11/03/2026). Taxis : 30,55 €/hl (taux 2024, le dernier affiché par la douane).
- Budget vert PLF 2026 (CSV data.gouv) : dépenses défavorables = 8,13 Md€ (crédits 1,44 ; dépenses fiscales 6,38 ; taxes affectées 0,31). Principales niches : GNR agricole (800229) 1,693 Md€ ; outre-mer art. 73 (800401) 1,466 ; TRM (800221) 1,178 ; GNR hors agriculture (800201) 0,466 ; taxis 0,059.

## Hausses de prix (dérivées, base HT car la TVA est récupérable ; avec une TVA de 20 % sur les deux termes, le % est identique en TTC)
- GNR agricole : 0,5689 / (0,6855 + 0,0386) = +78,6 % (prix 2025), +52,6 % (prix 2026).
- GNR hors agriculture : 0,2396 / 1,0534 = +22,7 % (2025), +17,0 % (2026).
- TRM : 0,1556 / 1,3471 = +11,6 % (2025), +9,2 % (2026).
- Taxis : +22,7 % (2025, avec le taux 2024).

## Non trouvé / tentatives
- PDF du rapport « Impact environnemental du budget de l'État » PLF 2026 : budget.gouv.fr bloque curl (Incapsula). J'ai utilisé le jeu de données officiel à la place, et le recoupement fonctionne : la baisse de 1,27 Md€ par rapport à la LFI 2025 correspond à la « baisse de 1,3 milliard » rapportée par Acteurs publics.
- Budget vert PLF 2027 : rien trouvé au 14/10/2026 (ni sur data.gouv, ni par recherche web).
- Coût de l'exonération du kérosène : ce n'est pas une dépense fiscale du budget vert. Le prix du carburéacteur n'est pas publié par la DGEC, donc la hausse n'est pas calculée.
- Taux de remboursement taxis 2025/2026 : non affichés. Trajectoire GNR de la LF 2024 jusqu'en 2030 : pas lue sur le texte de loi.
- Élasticité-prix : rien dans les sources lues (le PDF du rapport n'a pas été lu).

## Vigilance
- 2026 est une année de choc pétrolier (gazole HTT +46 % par rapport à 2025) : les % calculés sur les prix 2026 sont plus faibles. L'intégrateur doit choisir l'année de référence.
- Les montants TRM et taxis sont reconduits à l'identique de 2024 à 2026 (chiffrage probablement non actualisé).
- La ligne 800229 inclut aussi les fiouls lourds et le GPL agricoles. Le prix HTT du GNR agricole est supposé égal à celui de la série GNR.
- Des aides exceptionnelles carburant existent en 2026 (GNR agricole, transporteurs), repérées par recherche web mais non vérifiées : à ne pas confondre avec les tarifs réduits.
