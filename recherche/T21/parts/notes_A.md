# T21, groupe A (Élasticité carburants, Élasticité électricité) : notes

Date d'accès : 2026-10-20. Règles gelées au commit `686902b` (non modifiées ; valeurs gelées relues avec `git show 686902b:…`, car l'arbre de travail contient des modifications de `data/` faites par d'autres que ce groupe). Fichiers : `cout_A.csv` (7 lignes, toutes étrangères), `parametres_A.csv` (5 lignes), `sources_A.csv` (17 fichiers archivés dans `sources/T21/A/`, 4 pages canada.ca lues mais non archivées).

## 1. Bilan

| Règle | Cas `observe` FR | Cas `observe` étrangers | Tests de paramètre (ex post, high/medium) |
|---|---|---|---|
| Élasticité carburants (facteur 0,7 ; ε gelé −0,3 CT, −0,65 LT) | 0 | 7 (3 Colombie-Britannique, 4 Canada fédéral), 2 dispositifs seulement | 1 ex post (Suède, medium) + 1 français non ex post (medium) |
| Élasticité électricité (facteur 0,92 ; ε gelé −0,8, bas −0,2) | 0 | 0 | 2 ex post étrangers (Suisse high, Finlande high) + 1 non comparable |

Critère de la consigne (§ 4) : **Élasticité carburants** a 7 cas `observe`, mais tous étrangers et issus de deux dispositifs (même estimateur, plusieurs années) ; le test de paramètre (Suède) est `medium`. **Élasticité électricité** n'a aucun cas de mesure ; elle passe le critère par le test de paramètre (deux estimations ex post lues sur la primaire).

## 2. Cas de mesure (`cout_A.csv`)

Écart = (ex post central − ex ante) / ex ante.

| id | Pays | Ex ante | Ex post | Écart | Type | Comportement ex ante | Réalisé publié |
|---|---|---|---|---|---|---|---|
| bc_carbon_tax_2008_09 | CA-BC | 0,338 | 0,306 | −9 % | observe | inconnu | 2010-03-02 |
| bc_carbon_tax_2009_10 | CA-BC | 0,631 | 0,542 | −14 % | observe | inconnu | 2011-05-03 |
| bc_carbon_tax_2010_11 | CA-BC | 0,880 | 0,741 | −16 % | observe | inconnu | 2012-02-21 |
| ca_fuel_charge_2019_20 (ON, NB, MB, SK) | CA | 2,330 | 2,378 | +2 % | observe | inconnu | 2021 |
| ca_fuel_charge_ab_2019_20 | CA | 0,230 | 0,260 (bas 0,211) | +13 % (ou −8 %) | observe | inconnu | 2021 |
| ca_fuel_charge_2020_21 (ON, MB, SK) | CA | 3,325 | 3,089 | −7 % | observe | inconnu | 2021 |
| ca_fuel_charge_ab_2020_21 | CA | 1,365 | 1,111 | −19 % | observe | inconnu | 2021 |

Montants en Md CAD (pas en Md€) : seul l'écart relatif compte.

Points de lecture :

- **Pourquoi ces cas sont `observe`** : ce sont des taxes nouvelles perçues sur une ligne propre (« carbon tax », « fuel charge proceeds »). Le réalisé est donc la recette de la mesure elle-même, ce qui manque aux hausses d'accise françaises (T18, notes_B § 1).
- **Assiette mixte** : les deux taxes portent sur tous les combustibles fossiles (gaz naturel de chauffage compris), pas seulement sur les carburants routiers. La règle « Élasticité carburants » s'y applique d'après la nature (taxe carbone sur l'énergie), mais l'effet volume mêle carburants et chauffage.
- **Conjoncture** : récession 2008-2009 (BC) et COVID-19 (2020-21) pèsent sur les volumes sans être isolées. Le Budget 2010 de BC fait l'hypothèse que « consumption of gasoline is expected to be decline by 1.0 per cent » (Budget and Fiscal Plan 2010/11, p. 26 du PDF) : c'est la prévision suivante, pas celle de 2008, dont l'hypothèse de volume n'est pas écrite.
- **Même dispositif** : 3 années d'un même chiffrage (BC, Budget 2008 sur 3 ans) et 4 lignes d'un même système fédéral. L'intégrateur peut préférer un cas par dispositif (1re année seulement : −9 % et +2 %).
- **Pour information, sans statistique** : avec le facteur gelé de 0,7, l'ex ante corrigé est inférieur au réalisé dans les 7 cas (par exemple 0,237 contre 0,306 pour BC 2008/09). Calcul à refaire par l'agent de fusion.
- **Canada, révisions** : les produits sont révisés d'un rapport à l'autre (Alberta 2019-20 : 210,5 puis 259,6). Les deux valeurs sont dans le CSV (bas et central).

## 3. Tests de paramètre (`parametres_A.csv`)

| Paramètre gelé | Valeur gelée | Estimation trouvée | Source, nature | Lecture |
|---|---|---|---|---|
| eps_carbu (CT) / carbu_lt | −0,3 / −0,65 | **−1,57** à la taxe carbone ; −0,51 au prix hors taxe | Andersson (Suède 1970-2011), ex post sur une taxe carbone en vigueur, medium | La réponse à la taxe est environ 3 fois plus forte que la réponse au prix. Si elle vaut ailleurs, le gelé **sous-estime** la perte de base. Cela va contre les 7 cas canadiens, où l'écart est bien plus faible que −30 %. |
| eps_carbu | −0,3 | −0,45 | Douenne (2020), BdF 2011, cité par le Focus CAE n° 98 ; pas une observation après une mesure, medium | Légèrement hors de la fourchette gelée (−0,21 à −0,40). |
| eps_elec (elec_menages) | −0,8 (bas −0,2) | **−0,15 à −0,34** | Swiss Economics/SECO 2024, ménages suisses 2013-2023, high | Nettement moins élastique que le central ; au niveau de la borne basse gelée. |
| eps_elec (elec_menages) | −0,8 | **−0,184** | Ahlvik et al. 2025, Finlande, crise de 2022, quasi-expérience, high (document de travail) | Même conclusion : près de −0,2, loin de −0,8. |
| eps_elec (non comparable) | −0,8 | −0,042 | Swiss Economics, charge horaire France 2018-2023 au prix de gros | Ne teste pas le paramètre (prix de gros, horizon horaire) ; gardé pour éviter une sélection. |

Pour l'électricité, les deux estimations ex post (dont une pendant la crise, saillante) donnent −0,15 à −0,34 : le central gelé (−0,8, Insee 2007-2015, horizon semestriel plus long) ne tient pas pour un horizon de 1 à 2 ans ; la borne basse (−0,2, « hypothèse non sourcée » selon `elasticites.csv`) est désormais appuyée par ces deux sources. Le facteur de règle 0,92 dépend aussi de `dp_elec` et `a_elec`, non testés ici.

## 4. Pistes sans résultat (non trouvé ou exclu)

| Piste | Statut | Où l'on a cherché |
|---|---|---|
| Volumes constatés après la composante carbone 2014-2018, gel 2019 | **Non trouvé** pour un chiffrage ex post de l'effet volume. Seul résultat : Gloriant (2018), dont la partie ex post (contrôle synthétique 2014-2017) « does not allow a robust conclusion to be drawn » sur les transports ; ses 0,6-1,7 Mt de 2017 viennent de l'approche ex ante par élasticités (résumé archivé). Article complet payant. | WebSearch (FR) ; francoangeli.it ; réponse AN QE 12710 vue en résultat de recherche seulement (gazole −2,3 % au 1er semestre 2018, non lue, non utilisée) |
| Remise carburant 2022 (volumes) | Pas de cas nouveau : la source gelée carbu_ct (Insee/CAE 2023) couvre déjà septembre 2021-janvier 2023 ; exclusion T10a maintenue | Focus CAE n° 98 |
| Élasticités-prix observées en France depuis 2015 (carburants) | Seulement Douenne (2020, cité) ; aucune estimation ex post d'une mesure | WebSearch, Focus CAE n° 98 (bibliographie) |
| Suède (taxe carbone) | Test de paramètre seulement ; aucun chiffrage de recette avant/après isolable | Andersson (2017) |
| Colombie-Britannique : Rivers et Schaufele (2015) | **Non lu** : ruor.uottawa.ca « Request Rejected », ivey.uwo.ca 403, article payant. Chiffres (effet 7 fois / 4,9 fois plus fort, 10,6 % pour 5 c) vus seulement dans des résumés de recherche, non utilisés | ruor.uottawa.ca, test2.ivey.uwo.ca, ideas.repec.org |
| BC, hausses 2011/12 et 2018-2021 | Exclues : pas d'ex ante du Budget 2008 pour 2011/12 ; pour les hausses ultérieures, la ligne contient la taxe existante (même problème que la TICPE) | Budgets BC 2012 et 2013 |
| Suisse | La taxe CO2 suisse ne frappe que les combustibles de chauffage, pas les carburants : hors du champ de la règle. Évaluation EPFL/Ecoplan 2015 non téléchargée | WebSearch |
| Colombie (impuesto al carbono 2017) | Réalisé vu dans des résultats de recherche (477 Md COP en 2017, réponse du ministère des Finances), **ex ante non trouvé** ; non retenu | WebSearch (DIAN, La República, Congreso visible) |
| Irlande (taxe carbone 2010) | Ex ante (250 M€ en 2010) et réalisé (223,08 M€) vus seulement dans des résumés de recherche ; **oireachtas.ie bloque curl et WebFetch** (pare-feu AWS, 403). Le rapport du C&AG 2024 (archivé) ne donne pas de réalisé par hausse : les montants « hypothéqués » sont les estimations | oireachtas.ie, audit.gov.ie |
| Allemagne, Stromsteuer 1999 (Élasticité électricité) | Ex ante lu (4 200 M DM en 1999, Drucksache 14/40 p. 15 ; hausses 2000-2003 : 1,1 / 2,3 / 3,4 / 4,6 Md DM, Drucksache 14/2049 p. 2), mais le projet prévoyait une entrée en vigueur au 1er janvier 1999 alors que la loi s'applique au 1er avril 1999 ; **réalisé national non trouvé** (seuls des chiffres du Bade-Wurtemberg en résultat de recherche). Piste à reprendre : BMF « Kassenmäßige Steuereinnahmen » 1999-2000 | dserver.bundestag.de, WebSearch |
| Accise sur l'électricité 2024-2025 (consommation constatée, CRE, RTE) | Pas de cas nouveau : 2024 exclu par T18 (ex ante nul), 2025 déjà `accise_elec_2025`. RTE attribue la baisse de 2022-2023 à « sobriété » et prix réunis, sans part chiffrée du prix ; pas d'élasticité publiée | WebSearch (RTE, CRE, SDES) |
| Élasticité-prix de l'électricité des ménages en France depuis 2015 | **Non trouvé** : la seule estimation française reste Auray et al. (2019, données 2007-2015 = source gelée). La note de conjoncture Insee de juin 2023 (archivée) porte sur les entreprises et ne donne pas d'élasticité | WebSearch (Insee, Trésor, CRE, CGDD, Ademe), insee.fr |

## 5. Accès aux sources

- **canada.ca** : curl reste sans réponse (délai de 60 s dépassé, HTTP/2 et HTTP/1.1) ; WebFetch fonctionne. Les quatre pages utilisées ne sont donc pas archivées (confiance `medium`, drapeau `non_archive`).
- **oireachtas.ie** : pare-feu (« Human Verification ») pour curl, 403 pour WebFetch.
- **ruor.uottawa.ca** (« Request Rejected »), **test2.ivey.uwo.ca** (403), **cccep.ac.uk** (erreur 522 ; copie obtenue sur lse.ac.uk).
- bcbudget.gov.bc.ca, swiss-economics.ch, ceepr.mit.edu, cae-eco.fr, insee.fr, dserver.bundestag.de, audit.gov.ie : accessibles avec curl.
- Quota : environ 17 WebSearch et 9 WebFetch utilisés ; pas épuisé.

## 6. Décisions laissées à l'intégrateur

1. **Cas étrangers à assiette mixte** : les taxes carbone canadiennes portent aussi sur le gaz de chauffage. Faut-il les rattacher à « Élasticité carburants » ou les garder à part ?
2. **Un cas par dispositif ou un par année** : 7 lignes, 2 dispositifs. Garder les 1res années seulement (BC 2008/09 et Canada 2019-20 ; Alberta 2019-20 n'a que 3 mois) ou toutes les lignes, avec le drapeau `meme_dispositif` ?
3. **Signal contradictoire sur les carburants** : la littérature ex post sur les taxes carbone (Suède) trouve une réponse plus forte que le gelé, alors que les recettes canadiennes sont proches des chiffrages (écarts de −19 % à +13 %, conjoncture comprise). Le facteur 0,7 suppose −30 % ; aucun des 7 cas ne va aussi loin.
4. **eps_elec** : le central gelé (−0,8) n'est confirmé par aucune estimation ex post récente ; deux études (Suisse, Finlande) donnent −0,15 à −0,34. Faut-il prendre la borne basse comme central à l'horizon 2027 ? (Les estimations sont étrangères ; aucune estimation française récente n'existe.)
5. **Alberta 2019-20** : choisir la valeur révisée (259,6, retenue) ou la première (210,5) ; le sens de l'écart en dépend.
