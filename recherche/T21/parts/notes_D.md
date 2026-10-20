# T21, groupe D : notes

Règles du groupe : Réforme structurelle, Substitution retraites, Élasticité IS, Élasticité revenus, Élasticité capital, Élasticité succession. Date d'accès de toutes les sources : 2026-10-20. Règles gelées au commit `686902b` (non modifiées). Fichiers : `cout_D.csv` (en-tête seul, aucun cas retenu), `parametres_D.csv` (11 tests de paramètre), `sources_D.csv` (20 fichiers archivés dans `sources/T21/D/`, sha256 calculé). Rien n'a été écrit hors de `recherche/T21/parts/*_D.*` et `sources/T21/D/`.

## 1. Bilan par règle

| Règle | Cas `observe` nouveaux | Autres cas | Tests de paramètre (ex post) | Critère T21 § 4 |
|---|---|---|---|---|
| Réforme structurelle | 0 | 0 | 0 | non atteint : impossibilité expliquée au § 4 |
| Substitution retraites | 0 | 0 | 3 (FR : 1 `high`, 2 `medium`) | atteint par le test de paramètre |
| Élasticité IS | 0 | 0 | 2 (FR 1 `high`, international 1 `high`) | atteint par le test de paramètre |
| Élasticité revenus | 0 | 0 | 2 (Royaume-Uni : 1 `high`, 1 `medium`) | atteint par le test de paramètre, mais estimations étrangères seulement |
| Élasticité capital | 0 | 0 | 2 (FR : 1 `high`, 1 `medium`) | atteint par le test de paramètre |
| Élasticité succession | 0 | 0 | 2 (FR 1 `medium`, DE 1 `medium`) | atteint au sens strict (`medium`), mais résumés seulement |

Aucun cas de mesure (chiffrage avant adoption + réalisé sur le même périmètre) n'a été trouvé qui ne soit pas déjà dans `data/raw/mesures_cout.csv`, `recherche/T18/mesures_cout_nouvelles.csv`, `recherche/T20/mesures_cout_nouvelles.csv` ou écarté par T18 pour un motif que je n'ai pas pu lever. Le § 4 donne les pistes suivies. Je n'ai écarté aucun cas trouvé selon le sens de son écart.

## 2. Tests de paramètre (`parametres_D.csv`)

Valeurs telles que les sources les donnent ; les rapports et différences sont des calculs signalés comme tels.

| id | Paramètre gelé (valeur) | Estimation | Pays | Confiance | Lecture |
|---|---|---|---|---|---|
| subst_cor_2017 | part_substitution (0,2) | ≈0,15 (invalidité + RSA, AAH, ASS ; chômage non chiffré) | FR | medium | borne basse ; proche du gelé |
| subst_ipp_2025_are | part_substitution (0,2) | 0,08 (ARE seules) ; effet net sur le solde de l'assurance chômage ≈0 (−0,009 à +0,018, calcul) | FR | high | le chômage pèse peu une fois les cotisations comptées |
| subst_drees_dares_2022 | part_substitution (0,2) | ≈0,20 (prestations sociales et AC, hors invalidité, 2019) | FR | medium | égal au gelé |
| is_vicard_2015 | s_is (0,008) | 0,005 (canal des prix de transfert sur biens seul) | FR | high | même ordre ; un seul canal |
| is_beer_demooij_liu_2019 | s_is (0,008) | 0,010 (consensus), ≈0,015 (années récentes) | international | high | au-dessus du gelé |
| cap_bach_et_al_2023 | eps_capital (0,77) | 4,2 (hausse 2013), 2,1 (baisse 2018), dividendes des sociétés contrôlées | FR | high | bien au-dessus ; champ plus étroit |
| cap_lefebvre_zanoutene_2022 | eps_capital (0,77) | qualitatif : la hausse 2013 fait perdre de la recette sur les dividendes des redevables de l'ISF | FR | medium | plus fort que le gelé |
| rev_hmrc_2012 | eps_top (0,175) | 0,48 (0,35 supposé au chiffrage) | UK | medium | au-dessus |
| rev_ifs_2017 | eps_top (0,175) | 0,31-0,95 | UK | high | au-dessus |
| succ_goupille_infante_2016 | eps_succession (0,16) | ≈0,25, borne haute | FR | medium | proche, au-dessus |
| succ_glogowsky_2021 | eps_succession (0,16) | < 0,1 (court terme) | DE | medium | en dessous |

Points de lecture :

- **Substitution retraites.** Les trois sources portent sur la même réforme (2010) que la source gelée (Rabaté-Rochut) et ne sont pas indépendantes de ses données. Elles encadrent 0,2 : 0,15 sans le chômage (COR), 0,20 avec le chômage mais sans l'invalidité (DREES-DARES citées par la Cour). L'IPP (2025) montre que la hausse des allocations chômage (8 % de l'effet sur les pensions) est presque entièrement compensée par les cotisations des seniors restés en emploi : l'effet net sur l'assurance chômage est quasi nul. Les deux premières sources additionnent des dépenses brutes, sans ces recettes. Le paramètre gelé tient, avec une incertitude d'environ ±0,05 (lecture, pas un calcul des sources).
- **Élasticité IS.** Le facteur gelé (0,94) vient d'un rendement observé (surtaxe 2025) ; ces sources ne testent que la semi-élasticité de moyen terme (borne basse 0,73). La méta-analyse de Beer, de Mooij et Liu donne 1,0 à 1,5 %/pt, au-dessus de 0,8 : la borne basse gelée serait plus basse (≈0,5 à 0,66 pour 1 à 1,5 %/pt sur 33,6 points ; calcul fait sur la formule de `moteur_parametres.csv`, `1 − s × (25,83 + 7,73)`, que l'intégrateur doit vérifier). Pour 2026, le HCFP note seulement que le rendement prévu de la surtaxe d'IS « a été révisé à la baisse » (avis 2026-5, p. 21), sans chiffre : pas de cas.
- **Élasticité capital.** Les deux travaux français sur la réforme 2013 vont dans le même sens : la réponse des dividendes est bien plus forte que 0,77, au moins chez les dirigeants-actionnaires. Bach et al. écrivent pourtant p. 26 que la hausse « actually increased fiscal revenues », ce qui contredit en apparence leur propre élasticité > 1 et le résumé de Lefèbvre-Zanoutene. Je ne tranche pas.
- **Élasticité revenus.** Pas d'estimation française publiée après 2014 trouvée (voir § 4). Les estimations britanniques sur le taux de 50 % (0,31 à 0,95) sont toutes au-dessus de 0,175, mais pour une population plus large (0,66 % des adultes) et avec un fort effet d'anticipation.
- **Élasticité succession.** Deux résumés seulement, une borne haute française (0,25) et une borne haute allemande (0,1) : ils encadrent la valeur gelée (0,16).

## 3. Cas étranger signalé (non intégré)

Taux marginal de 50 % au Royaume-Uni (avril 2010) : rendement annoncé d'environ 2,5 Md£ par an (élasticité supposée 0,35), contre 1,1 Md£ estimé par HMRC sur les déclarations de 2010-11 (IFS W17/12, p. 3 et note 4 ; les IFS jugent même la recette nette possiblement négative). La consigne T21 n'admet les cas étrangers que pour les règles sans précédent français ; « Élasticité revenus » en a un. Le cas n'est donc pas dans `cout_D.csv`. De plus, le réalisé est une estimation par modèle (`reestimation`), pas une recette observée. L'intégrateur décidera.

## 4. Mesures cherchées sans résultat (« non trouvé »), avec les endroits cherchés

**Réforme structurelle**

- **Réformes des retraites 2003, 2010 (compléments), 2014.** COR, séance du 14/12/2016 (doc. n° 9, `cor_doc-3734.pdf`, et présentation, `cor_doc-3739.pdf`). Le COR écrit que ses projections « ne permettent pas l'évaluation des effets purs des réformes à champ et environnement démographique et économique constants » (doc. 9, p. 3 du PDF). Les seuls chiffres sont des projections (2003 : −1,2 point de PIB de besoin de financement en 2050, rapport 2006, cité p. 5 du PDF). Il n'y a aucun réalisé, et pour 2014 aucun ex post (T18 avait aussi cherché, sans résultat). La présentation de la même séance (p. 7) parle d'« Un effet non négligeable des réformes et accords, mais difficilement chiffrable ».
- **Assurance chômage 2023.** Unédic, prévisions de juin 2026 (`unedic_prev_juin2026.pdf`) : effets décrits en nombre d'indemnisés (« Toujours puissants, les effets de la réforme 2023 »), aucune économie en euros ni comparaison au chiffrage de février 2023. Une recherche web (Cour des comptes, Unédic) n'a trouvé aucun bilan chiffré constaté.
- **Assurance chômage 2019-2021.** Déjà `ac_2021` (T10a, `reestimation`). Pas de source nouvelle : les documents Unédic lus par T10a et T18 restent les seuls.
- **Carrières longues (décret du 2 juillet 2012).** Le coût ex ante (« 1,1 Md€ en 2013 », vu dans des résultats de recherche) n'a pas été lu sur une source primaire. Le réalisé non plus : la Cour (RALFSS 2019, chapitre « départs anticipés », p. 28 du PDF) donne les prestations des carrières longues (6,1 Md€ en 2016) mais écrit que « la Cour n'a pu apprécier le coût global des départs anticipés ». Ce cas aurait aussi pu tester « Substitution retraites » dans le sens d'un abaissement de l'âge.
- **Pourquoi la règle reste non testée** : les économies d'une réforme structurelle ne sont presque jamais observées. Elles sont seulement réestimées, par le modèle de l'institution qui les a chiffrées au départ (COR, Unédic, DSS), et souvent sur des horizons pas encore atteints (2030 ou 2050). Le seul test possible du paramètre (`facteur_reforme`, 0,842) serait un ratio réalisé / annoncé sur une autre réforme, et je n'en ai trouvé aucun de nouveau.

**Substitution retraites (cas de mesure)**

- Aucune mesure nouvelle avec un chiffrage net avant adoption et un réalisé net. Les cas existants (`woerth_2010`, `retraites_2023`) restent les seuls. L'étude d'impact 2023 (lue par T2a) ne sépare pas, dans les passages vus, un chiffrage de substitution comparable à un réalisé.

**Élasticité IS (cas de mesure)**

- **Contribution exceptionnelle de 10,7 % (2014-2015).** Aucun réalisé isolé, comme pour T18. Les notes d'exécution de la Cour « recettes fiscales » 2014 à 2017 et 2020 sont introuvables sous les motifs d'URL `sites/default/files/2023-10/NEB-<année>-Recettes-fiscales.pdf`, `…-Recettes-Etat.pdf` et `EzPublish/NEB_<année>_Recettes_Etat.pdf` (réponse HTML). La NEB 2021 existe à l'URL `2023-10/NEB-2021-Recettes-fiscales.pdf`, mais son téléchargement a échoué (voir § 5).
- **Surtaxe d'IS 2026 (LFI 2026, art. 12).** Pas encore de réalisé : HCFP 2026-5, p. 21, « révisé à la baisse » sans montant. Le PLF 2027 (évaluations préalables, archivé par T1) ne chiffre que la prorogation 2027 (5 Md€).

**Élasticité revenus (cas et paramètre)**

- **Taxe exceptionnelle de solidarité sur les hautes rémunérations (2014-2015).** Ex ante vu seulement dans un amendement de seconde main (310 M€ brut). Aucun réalisé : recherche web, QE AN n° 51111 (réponse sans chiffre), rapport AN n° 3973 de 2016 sur l'application des mesures fiscales (`an_rapinfo_i3973_2016.pdf`, lu : il traite de la fiscalité locale, de la prime d'activité, de l'énergie et des rescrits, pas des hauts revenus).
- **Élasticité française du revenu imposable après les réformes 2012-2013.** Non trouvée. Pacifico (AMSE) n'a que des résumés de séminaire, sans chiffre. L'article de synthèse de Sicsic (Revue de l'OFCE n° 183, 2023) n'a pas pu être téléchargé (404 sur ofce.fr, voir § 5). Lefebvre, Lehmann et Sicsic (IZA DP 16112) portent sur le capital, et c'est déjà la source gelée de `capital_fr`.

**Élasticité capital (cas de mesure)**

- **Hausses des prélèvements sociaux sur le capital (LFR 2011, LFR 2012).** Rapports de la CCSS 2012-2013 introuvables : URL `securite-sociale.fr/files/live/sites/SSFR/files/medias/CCSS/<année>/RAPPORT/…` en 404, 2 recherches web sans résultat.
- **Dividendes seuls en 2013.** Comme T18 : pas de chiffrage gouvernemental avant adoption pour les dividendes seuls. Les travaux français (Bach et al., Lefèbvre-Zanoutene, France Stratégie 2021) ne servent qu'au test de paramètre.
- **France Stratégie, 3e rapport (octobre 2021, lu, `fs_2021_fiscalite_capital_3e_rapport.pdf`).** Le coût du PFU recalculé y figure, mais la mesure `pfu` est déjà dans `data/raw/mesures_cout.csv` avec le rapport 2023. Aucune élasticité chiffrée nouvelle. Le 4e rapport (octobre 2023) n'a pas pu être téléchargé : l'ancienne URL renvoie une 404 après la migration de strategie.gouv.fr vers strategie-plan.gouv.fr.
- **Exit tax (dégrèvements élargis en LFI 2024).** La NEB 2025 (archivée par T18) décrit l'effet de rattrapage, sans chiffrage ex ante comparable.

**Élasticité succession (cas de mesure)**

- **Abattement ramené à 100 000 € et rappel à 15 ans (LFR II 2012).** Réalisé toujours non trouvé. Lu : NEB 2012 et 2013 (« réduction des abattements sur les successions » 0,1 Md€ en 2012 ; 0,33 Md€ d'effet en année pleine en 2013 ; moindres rendements des DMTG de −0,9 et −0,4 Md€ sans isoler la mesure), QE AN n° 5892 et 11823 (sans chiffre), recherche web d'un rapport de la Cour sur les DMTG (aucun trouvé).
- **Hausse de 5 points des tranches supérieures et rappel 6 → 10 ans (LFR I 2011).** La NEB 2012 (p. 14) ne donne que les impacts prévus (+0,2 et +0,3 Md€) ; pas de réalisé isolé. Le rappel est déjà `rappel_donations_2011` (T18).
- **DMTG 2026.** Le HCFP (p. 21) signale 1,6 Md€ de « recettes exceptionnelles » de DMTG en 2026, sans mesure associée : sans objet.

## 5. Accès aux sources

- **ccomptes.fr** : en IPv6, la connexion TLS est coupée (« Connection reset by peer ») ; en IPv4 (`curl -4`), les requêtes HEAD ont abouti, puis tous les GET ont échoué (code curl 35) le 2026-10-20 après-midi. La NEB 2021 « recettes fiscales » n'a donc pas pu être lue.
- **HAL (hal.science, shs.hal.science, halshs.archives-ouvertes.fr)** : bloqué par un contrôle anti-robot (Anubis) pour curl comme pour WebFetch. D'où les résumés IDEAS seulement pour Goupille-Lebret-Infante, Lefèbvre-Zanoutene et Glogowsky.
- **strategie.gouv.fr** : redirige vers strategie-plan.gouv.fr, où les anciens PDF sont en 404 (4e rapport du comité, 2023). Le 3e rapport (2021) a été obtenu par `www.vie-publique.fr/files/rapport/pdf/281944.pdf`. `medias.vie-publique.fr` ne se résout pas (DNS).
- **ofce.sciences-po.fr / ofce.fr** : 404 sur les PDF de la Revue n° 183.
- **ifo.de** (DICE Report 2018, Garbinti et Goupille-Lebret) et **imf.org** (WP 18/168) : page HTML au lieu du PDF. Pour la seconde, une copie de travail hébergée par la NYU a été lue.
- **securite-sociale.fr** : 404 sur les URL des rapports CCSS essayées.
- **assemblee-nationale.fr, cor-retraites.fr, ipp.eu, ifs.org.uk, banque-france.fr, unedic (S3), conference.nber.org, ideas.repec.org** : accessibles.
- **senat.fr** : pas utilisé.
- Quota : environ 22 recherches WebSearch et 3 WebFetch ; il n'est pas épuisé.
- Deux fichiers sont copiés d'autres tâches (`ccomptes_retraites_2025_copie_T2a.pdf`, `hcfp_avis_2026-5_copie_T1.pdf`), avec sha256 recalculé.

## 6. Décisions laissées à l'intégrateur

1. **Réforme structurelle** : aucun cas `observe` ni test de paramètre. Faut-il garder la règle sur la base de deux backtests (`woerth_2010`, `retraites_2023`, dont un en `reestimation`) en le disant, ou la classer « non testable sur réalisé » ?
2. **Substitution retraites** : les trois estimations reposent sur la même réforme que la source gelée. Elles confirment 0,2 sans être indépendantes. L'IPP suggère que l'effet net sur l'assurance chômage est quasi nul une fois les cotisations comptées : le 0,2 serait alors surtout de l'invalidité, des minima et des indemnités journalières.
3. **Élasticité IS** : la borne basse (0,73) repose sur 0,8 %/pt ; la méta-analyse la plus récente lue donne 1,0 à 1,5. Le facteur central (0,94, rendement 2025) n'est pas en cause.
4. **Élasticité capital** : les estimations françaises ex post (élasticités 2 à 4 pour les dividendes des sociétés contrôlées ; perte de recette en 2013 selon Lefèbvre-Zanoutene) sont plus fortes que 0,77. Champ et sens de la phrase p. 26 de Bach et al. à vérifier avant tout usage.
5. **Élasticité revenus** : seules des estimations britanniques ont été trouvées, toutes au-dessus de 0,175. Faut-il les admettre comme test d'un paramètre français ?
6. **Élasticité succession** : deux résumés, sans texte intégral. Confiance à garder `medium`, ou à abaisser à `low` si l'on exige le texte intégral.
7. **Cas étranger** du taux de 50 % britannique (§ 3) : hors champ selon la consigne, signalé seulement.
