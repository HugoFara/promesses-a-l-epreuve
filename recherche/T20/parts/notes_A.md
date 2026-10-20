# T20, groupe A : répercussion de la TVA et des accises sur les prix

Accès : 2026-10-20. Sorties : `repercussion_A.csv` (36 lignes), `sources_A.csv` (24 fichiers archivés dans `sources/T20/A/`).

Convention : une valeur de répercussion est la part de la variation de taxe qui passe dans le prix TTC (1 = intégrale). Quand une source donne un effet sur les prix et non un taux, le taux est calculé par l'agent ; c'est indiqué dans `note_num`. Quelques valeurs dépassent 1 (sur-répercussion) : elles restent telles quelles, sans plafond.

## 1. Résultats par secteur

| Secteur | Sens | Centrale | Horizon | Source principale | Confiance |
|---|---|---|---|---|---|
| Restauration (FR 2009) | baisse | 0,21 | 2–5 mois | Insee DT F1404 (+ Benzarti-Carloni) | high |
| Restauration (FR 2009-2011) | baisse | 0,20 | 1–2,5 ans | Insee F1404 ; Benzarti-Carloni 0,135 | high |
| Restauration | hausse | **non trouvé** (voir § 3) | | | |
| Services à forte main-d'œuvre (FR 1995 / 2000) | hausse / baisse | 0,91 / 0,22 | ≤ 4 mois | Carbonnier 2005 via Insee F1404 | medium |
| Travaux du logement (FR 1999) | baisse | 0,77 | non précisé | Carbonnier 2007 (résumé) | medium |
| Voitures neuves (FR 1987) | baisse | 0,57 (0,52 en WP) | non précisé | Carbonnier 2007 (résumé) | medium |
| Coiffure (FI 2007) | baisse | 0,5 | | Kosonen 2015 (résumé) | medium |
| Électricité, TRVE (FR 2025) | accise en baisse, TVA abonnement en hausse | 1,0 | immédiat | CRE, délibération 2025-155 | high |
| Électricité (BE 2014 / 2015) | baisse / hausse | 1,0 / 1,0 | | Hindriks-Serse (résumé) | medium |
| Logement-énergie COICOP 04 (UE 1996-2015) | hausse / baisse | 0,92 / 0,12 | 1–3 mois | Benzarti et al. 2017, fig. A.12 | high |
| Gaz seul | | **non trouvé** | | | |
| Carburants, remise 2022 (FR) | baisse d'accise | 1,0 (0,999–1,11) | ~2 semaines | Drolsbach et al. 2022 | high |
| Carburants, Tankrabatt 2022 (DE) | baisse d'accise | essence 0,98, gazole 0,80 | 3 mois | Bernhardt et al. 2023 et autres (résumés) | medium |
| Carburants, TVA 2020 (DE) | baisse | 0,61 (0,40–0,83) | quelques semaines | Montag et al. 2020 | high |
| Essence COICOP 04.5.2 (UE) | hausse / baisse | 0,91 / 0,16 | 1–3 mois | Benzarti et al. 2017, fig. A.11 | high |
| Carburants, accises d'État (US) | les deux | 1,0 | immédiat | Marion-Muehlegger 2011 (résumé) | medium |
| Alimentation (PT 2023-2024) | baisse / hausse | 0,998 / 1,0 | immédiat, persistant | Bernardino et al., note SUERF | high |
| Alimentation (ES 2023) | baisse | 0,90 (0,30–1,0) | 1–2 mois | BdE via CNMC 2023 | medium |
| Alimentation, supermarchés (DE 2020-2021) | baisse / hausse | 0,70 / 0,35 | semaines | Fuest et al. (résumés) | medium |
| Alimentation COICOP 01 (UE 1996-2015) | hausse / baisse | 0,65 / 0,23 | 1–3 mois | Benzarti et al. 2017, fig. A.12 | high |
| Toutes TVA (UE 1996-2015) | hausse / baisse | 0,33 / 0,063 | 1 mois | Benzarti et al. 2017 | high |
| Toutes TVA (zone euro 1999-2013) | hausse / baisse | 0,40 / 0,24 | cumul 2 ans | FMI WP/15/214, tableau 4 | high |
| Taux normal / taux réduit (zone euro) | les deux | 1,0 / 0,30 | cumul 2 ans | FMI WP/15/214 | high |
| Hausse TVA 2014 (FR), **prévision** | hausse | 0,8 à 6 mois | 6 mois | Insee, Note de conjoncture déc. 2013 | high (mais c'est une hypothèse) |

## 2. Points de vigilance pour l'intégrateur

1. **Deux familles de résultats qui ne disent pas la même chose.**
   - Les études qui portent sur *toutes* les réformes de TVA en Europe donnent des répercussions faibles et nettement asymétriques à court terme (Benzarti et al. : 33 % pour les hausses, 6 % pour les baisses au 1er mois ; énergie du logement 92 % / 12 % ; essence 91 % / 16 %). Le FMI trouve 40 % / 24 % en cumul sur 2 ans, sans asymétrie significative, mais environ 100 % pour le taux normal et environ 30 % pour les taux réduits.
   - Les études récentes sur des baisses **ciblées, saillantes et surveillées** (carburants 2022, alimentation en Espagne et au Portugal en 2023, électricité belge) trouvent une répercussion proche de 1. Plusieurs ont un cadre particulier : obligation légale de répercuter en Espagne (la CNMC cite le décret-loi qui « prohíbe no trasladar la reducción del IVA »), versement de la remise aux distributeurs en France, forte inflation, attention politique.
   Les deux mesurent des choses différentes : réformes ordinaires d'un côté, baisses temporaires très visibles de l'autre. Choisir une valeur pour une promesse électorale revient à choisir laquelle des deux situations ressemble le plus à la promesse. **C'est à l'intégrateur de trancher**, et le choix doit être dit.
2. **Restauration : la seule estimation française solide est une baisse, faible (~0,2) et durable.** Benzarti-Carloni (incidence) : 13,6 % du gain aux consommateurs à 30 mois, 55,7 % aux propriétaires.
3. **Énergie au tarif réglementé : répercussion mécanique de 1.** La CRE fixe les TRVE hors taxes ; accise et TVA s'ajoutent (la TVA s'applique aussi à l'accise). Vérification par l'agent : (33,70 − 29,98) × 1,2 = 4,46 €/MWh, soit la baisse TTC annoncée. Cela ne couvre ni les offres de marché ni le gaz.
4. **Asymétrie hausse/baisse** : établie par Benzarti et al. (3 à 4 fois plus forte pour les hausses), par Carbonnier 2005 pour les services (91 % contre 22 %) et par Fuest et al. pour l'Allemagne en 2021 (hausse moitié moindre que la baisse, c'est-à-dire une asymétrie dans l'autre sens) ; le FMI ne la trouve pas, et le Portugal est symétrique. Le sens de l'asymétrie n'est donc pas stable d'une étude à l'autre.
5. **Horizons** : la plupart des mesures valent pour 1 à 3 mois. Les seules au-delà d'un an : restauration France (Insee, Benzarti-Carloni, jusqu'à 2,5 ans), FMI (cumul sur 2 ans), coiffure en Finlande (persistance après 3,5 ans selon Benzarti et al., sans chiffre extrait).
6. **Valeurs supérieures à 1** : biens intensifs en capital, baisse 2000 (1,30) ; carburants France 2022 avec contrôles (1,11) ; FMI, taux normal (estimation ponctuelle 1,39). Elles sont gardées telles quelles.
7. **Prévision Insee 2014** : c'est une hypothèse ex ante (0,4 point d'inflation attendu à fin juin 2014 contre 0,5 en cas de répercussion intégrale, soit 0,8, calcul de l'agent), et non un réalisé. Ne pas la compter comme observation.
8. **Versions** : Benzarti et al. sont lus dans la version NBER 2017, pas dans celle du JPE 2020 ; Benzarti-Carloni dans un manuscrit AEA ; Montag et al. dans le préprint v1. Les chiffres publiés peuvent différer.

## 3. Non trouvé (avec les endroits cherchés)

- **Hausse de TVA dans la restauration (France 2012 : 5,5 → 7 % ; 2014 : 7 → 10 %)** : non trouvé en chiffre. Benzarti et al. 2017 (fig. 10b) montrent la persistance pour la France sans taux chiffré dans le texte. Aucun bilan ex post de l'Insee trouvé (recherche web : Insee, « hausse TVA 2014 bilan répercussion »). Un relevé de l'UFC-Que Choisir (2014) existe mais n'a pas été lu.
- **Bilan ex post de la hausse de TVA de 2014 (tous secteurs)** : non trouvé ; seule la prévision de l'Insee (déc. 2013) a été lue. Un « de l'ordre de 75 % » attribué à l'Insee et un « 80 % en un trimestre » attribué à la Banque de France n'apparaissent que dans des extraits de presse, non vérifiés et non retenus.
- **Gaz naturel seul** (France ou étranger) : non trouvé. Seul le groupe agrégé COICOP 04 de Benzarti et al. est disponible. Recherches : « VAT gas pass-through », baisse de TVA allemande sur le gaz en octobre 2022 (seule l'annonce a été trouvée, pas d'étude ; Hansen-Schmerer porte sur l'essence malgré le mot « Gas » dans le titre).
- **Électricité, offres de marché en France** : non trouvé.
- **Composante carbone de la TICPE, 2014-2018 (hausse d'accise en France)** : non trouvé. Recherches : « répercussion TICPE composante carbone », « fuel tax pass-through France 2014-2018 ». Un bloc-notes de la Banque de France sur la transmission du prix du pétrole (et non des taxes) n'a pas été retenu.
- **Bouclier tarifaire 2022-2023** : aucune étude de répercussion trouvée ; pour les TRVE le mécanisme est réglementaire (point 3 du § 2).
- **Billetterie, services culturels** : non trouvé.
- **Évaluation du CPO ou de l'IPP de la TVA restauration** : non trouvée lors de cette passe ; le rapport Houel (Sénat, 2010) n'est connu que par Insee F1404 (effet maximal de −2,6 % en avril-mai 2010, puis −2,1 % en août 2010) : chiffres en source secondaire, non portés au CSV.
- **Remise carburant 2022, étude française officielle** : non trouvée. Insee Analyses n° 86 mesure l'élasticité de la consommation (−0,21 à −0,40), pas la répercussion. Ce fichier est archivé pour le groupe B ou les élasticités, sans ligne dans le CSV.
- **Insee DT E2015/02 (Quantin, Robin, Accardo)** : il ne donne qu'un résultat qualitatif (« répercussion seulement partielle »). Il est archivé, sans ligne.
- **Jongen, Lejour, Massenz (2018), coiffure aux Pays-Bas en 2000** (« close to full pass-through » selon un extrait de recherche) : page RePEc en 404, non lu, non retenu.

## 4. Sites inaccessibles

- **HAL (hal.science, shs.hal.science, halshs.archives-ouvertes.fr)** : page anti-robot (Anubis), avec curl comme avec WebFetch. Le texte de Carbonnier n'a donc pas pu être lu ; seuls les résumés RePEc l'ont été.
- **fiscalcouncil.ie** (revue « VAT rate changes and pass-through », 2025) : 403 avec curl et WebFetch.
- **i3.cnrs.fr** (PDF de Fuest et al.) : certificat TLS refusé ; ifo.de et cesifo.org renvoient du HTML au lieu des PDF.
- **alfresco.uclouvain.be** (PDF de Hindriks-Serse) : le nom d'hôte ne se résout pas.
- **imf.org** : curl reçoit du HTML ; le PDF a été obtenu par WebFetch (copie binaire archivée).
- **doria.fi** : page Cloudflare. **archiv.ub.uni-marburg.de** : erreur, mais le PDF a été obtenu via open.uni-marburg.de.
- Revues payantes (Energy Economics, Review of Economics, Economics Letters, JPE, JPubE, IJIO) : seuls les résumés ont été lus.

## 5. Pistes non suivies faute de temps

- L'article publié de Bernardino et al. (JPubE 248, 2025), pour les intervalles de confiance.
- Le document de la Banque d'Espagne (2023) sur la TVA alimentaire (90 %), lu seulement via la CNMC.
- Les études de la Commission européenne (Copenhagen Economics 2007, citée par Insee F1404) et de la BCE sur les mesures fiscales énergétiques de 2022.
