# T23, étape 1 : groupe « fiscalite » (impôts, contributions et prélèvements obligatoires)

Date d'accès : 2026-10-20. Champ appliqué : `recherche/T23/CONSIGNE.md` § 1 (J1 seul pour les cas passés), sans le modifier. Les prestations et les dépenses relèvent de l'autre agente : elles ne sont pas traitées ici, sauf deux allègements de prélèvements (réduction de CSG ou de cotisations) qui sont des prélèvements.

Fichiers : `cas_fiscalite.csv` (7 lignes), `hors_champ_fiscalite.csv` (24 lignes, dont 1 ligne d'information qui n'est pas hors champ), `sources_fiscalite.csv`, sources dans `sources/T23/fiscalite/`.

## 1. Méthode et accès

- **Conseil constitutionnel.** Le site refuse `curl` et WebFetch après quelques dizaines de requêtes (connexion coupée). Les pages des décisions ont été lues sur web.archive.org (`/web/2024id_/…`), lentement. Les **commentaires officiels** des décisions sont lus sur le dépôt public du Conseil (`oos.cloudgouv-eu-west-1.outscale.com/ccqpc-drupal-prd/dqpc/commentaire/`), dont la liste est publique ; ils donnent les motifs et les décisions antérieures que le Conseil rapproche lui-même.
- **Légifrance** : refuse `curl` (403), non utilisé. **EUR-Lex et curia** : pages vides par WebFetch et par web.archive.org ; les arrêts de la CJUE sont lus de seconde main (communiqué de presse de la Cour, CLEISS, évaluations préalables du Gouvernement), confiance `medium`.
- **Repérage des décisions.** Liste des décisions DC 2000-2025 tirée de l'index de web.archive.org (477 adresses) ; intitulé de chaque décision lu sur la page archivée ou sur le commentaire. Toutes les décisions sur une loi de finances, de finances rectificative, de financement ou de financement rectificative de la sécurité sociale trouvées ont été parcourues (liste au § 2). Pour les QPC 2010-2025, 1 133 commentaires listés, 992 lus (3 premières pages) et filtrés sur les mots fiscaux (§ 3).
- **CJUE et CEDH** : pas de liste exhaustive accessible (EUR-Lex et curia illisibles ici). Ont été parcourus les arrêts sur la fiscalité française cités par les évaluations préalables, les rapports parlementaires et les commentaires lus (§ 4). Aucun arrêt de la CEDH sur un prélèvement français n'a été trouvé dans ces sources ; le Conseil d'État cite la CEDH (art. 14 + art. 1er du protocole 1) contre la contribution de 3 % (CE 29/03/2017, Layher, cité par le commentaire 2017-660 QPC), décision postérieure au vote.
- **Ordre de travail** : décision censurante, puis mesures de même nature votées après, puis chiffrage et réalisé. Aucune mesure n'a été écartée parce que la règle y paraissait marcher ou non ; les mesures non retenues l'ont été faute de chiffrage ou de réalisé sur le même périmètre (§ 5).

## 2. Décisions DC sur les lois financières parcourues (68 lignes, 69 décisions)

Censure « sur le fond » d'une disposition fiscale ou de prélèvement : **en gras**. Les autres n'ont censuré que des cavaliers, des dispositions adoptées après la CMP ou hors « entonnoir », des dispositions non fiscales, ou rien.

| Décision | Loi | Censures de fond fiscales retenues |
|---|---|---|
| 2000-432 DC | LFR 2000 | aucune |
| **2000-437 DC** | LFSS 2001 | ristourne dégressive de CSG (art. 3, avec 2 et 7) |
| **2000-441 DC** | LFR 2000 (II) | extension de la TGAP à l'énergie (art. 37 I-III) ; art. 3, 48 partiel, 64 : autres motifs, non fiscaux ou procéduraux (non détaillés) |
| 2000-442 DC | LFI 2001 | 3 cavaliers |
| 2001-453 DC | LFSS 2002 | annulation rétroactive d'une créance dans les comptes 2000 (non fiscal) |
| 2001-456 DC | LFI 2002 | 1 grief retenu (fonds spéciaux, non fiscal) + 3 cavaliers |
| 2001-457 DC | LFR 2001 | procédure (art. 55 après CMP et autres) |
| 2002-463 DC | LFSS 2003 | cavaliers |
| **2002-464 DC** | LFI 2003 | taxe sur la distribution d'imprimés (art. 88) : même motif que 2000-441 |
| 2003-486 DC | LFSS 2004 | déremboursement de certificats médicaux (prestation, autre groupe) |
| 2003-488 DC | LFR 2003 | mots « non nominatifs » (art. 20) : censure qui étend le champ ; non retenue (portée mineure, chiffrage non recherché) ; art. 80 et 86 : cavaliers |
| 2003-489 DC | LFI 2004 | aucune |
| 2004-508 DC | LFSS 2005 | cavaliers |
| 2004-511 DC | LFI 2005 | mots « dans la limite de dix zones » (art. 28) : non fiscal au sens strict, non retenu |
| 2005-528 DC | LFSS 2006 | aucune (censure « suspendue ») |
| **2005-530 DC** | LFI 2006 | plafonnement global des niches (art. 78, intelligibilité) ; art. 66 IV (affectation des surplus, non fiscal) |
| **2005-531 DC** | LFR 2005 | art. 111 (facture rectificative de TVA, validation) |
| 2006-544 DC | LFSS 2007 | procédure (art. 47, 134) ; mot « conforme » (non fiscal) |
| **2007-555 DC** | loi TEPA | crédit d'impôt sur les intérêts d'emprunt pour les prêts déjà contractés (art. 5, partiel) |
| 2007-558 DC | LFSS 2008 | 17 cavaliers |
| 2008-571 DC | LFSS 2009 | aucune de fond |
| 2008-574 DC | LFR 2008 | octroi de mer (procédure), garantie SNPE (art. 124, LOLF, non fiscal), cavaliers |
| 2009-575 DC | loi de relance | cavaliers |
| 2009-596 DC | LFSS 2010 | 10 cavaliers |
| **2009-599 DC** | LFI 2010 | contribution carbone (art. 7, 9, 10) ; CET des contribuables de moins de 5 salariés (art. 2 partiel) |
| 2009-600 DC | LFR 2009 | cavaliers ; art. 82 par voie de conséquence |
| 2010-620 DC | LFSS 2011 | domaine organique |
| 2010-622 DC | LFI 2011 | art. 41 V, 43, 150, 166, 196, 197 : soulevés d'office sans section propre (cavaliers d'après la structure de la décision, non vérifié article par article) |
| 2011-638 DC | LFR 2011 (juillet) | 4 cavaliers ; dispositions organiques |
| 2011-642 DC | LFSS 2012 | cavaliers ; mots relatifs aux « organes juridictionnels » |
| **2011-644 et 2011-645 DC** | LFI 2012 et LFR 2011 | LFI : art. 19 (taxe sur les cessions de titres de sociétés audiovisuelles, fait générateur lié à l'agrément du CSA) ; LFR : art. 23 (rachat d'actions, non fiscal) ; cavaliers |
| 2012-654 DC | LFR II 2012 | art. 11 (agrément CSA, cavalier, qui emporte la taxe revotée après 2011-644 DC) et art. 40 : censures de procédure ou non fiscales ; contribution exceptionnelle sur la fortune validée |
| **2012-659 DC** | LFSS 2013 | contribution sur les boissons énergisantes (art. 25) ; art. 37 (transfert de réserves des assureurs privés, non fiscal) ; art. 11 IV, 55, 58, 61 : non détaillés |
| **2012-661 DC** | LFR 2012 (déc.) | imposition des « donations-cessions » (art. 19) ; art. 28 non détaillé |
| **2012-662 DC** | LFI 2013 | art. 9 IV (PFL 2012), 11 partiel (stock-options), 12 (taxe à 75 %), 13 C et F (ISF), 14 (Corse), 15 (plus-values de terrains), 73 partiel (plafond de 4 %), art. L. 137-11-1 CSS (retraites chapeaux) ; art. 8, 44, 95, 104 : cavaliers |
| 2013-682 DC | LFSS 2014 | art. 14 (taux du forfait social liés aux clauses de recommandation) : voir § 5 ; art. 8 (taux historiques) conforme avec réserve |
| **2013-685 DC** | LFI 2014 | art. 13 (plafonnement ISF, chose jugée), 27 partiel (plus-values de terrains), 100 (abus de droit), 106 (transfert de fonctions), 96, 97, 99 (amendes), 92 II-III (emprunts structurés, non fiscal) |
| 2013-684 DC | LFR 2013 | art. 39, 60 partiel, 30, 43, 66 (non détaillés ; aucune mesure de rendement repérée) |
| **2014-698 DC** | LFRSS 2014 | réduction dégressive des cotisations salariales (art. 1er) |
| 2014-699 DC | LFR 2014 (août) | aucune |
| **2014-706 DC** | LFSS 2015 | art. 12 (taux de la « cotisation » FNAL renvoyés au décret : incompétence négative) ; art. 16 cavalier |
| **2014-707 DC** | LFI 2015 | art. 72, 5e al. (régime mère-fille, incompétence négative) ; art. 78-79 (sanctions) ; art. 109 cavalier |
| 2015-723 DC | LFSS 2016 | aucune de fond fiscale |
| **2015-725 DC** | LFI 2016 | art. 77 (réduction dégressive de CSG au titre de la prime d'activité) ; art. 30 (TTF, procédure) |
| 2015-726 DC | LFR 2015 | aucune de fond fiscale repérée |
| 2016-743 DC | LFR 2016 | art. 113 (cavalier) |
| **2016-742 DC** | LFSS 2017 | art. 28 II (encadrement de la répercussion de la contribution des fournisseurs de tabac : liberté contractuelle) ; art. 50 partiel (incompétence négative, affiliation, non fiscal) ; cavaliers |
| **2016-744 DC** | LFI 2017 | art. 78 (art. 209 C, « taxe Google ») ; 105 I et 133 I non fiscaux ; 7 cavaliers |
| 2017-755 DC | LFR I 2017 | aucune (contributions exceptionnelles sur l'IS validées) |
| 2017-756 DC | LFSS 2018 | cavaliers |
| 2017-758 DC | LFI 2018 | affectation de ressources à la métropole de Lyon (non fiscal pour le contribuable) |
| 2017-759 DC | LFR II 2017 | art. 24 et 29 : cavaliers |
| 2018-776 DC | LFSS 2019 | cavaliers |
| 2018-777 DC | LFI 2019 | art. 210 partiel (revalorisation, prestation : autre groupe) |
| 2019-795 DC | LFSS 2020 | art. 8 cavalier |
| 2019-796 DC | LFI 2020 | fichier de collecte de données (art. 154 partiel, non fiscal) ; art. 217 procédure |
| 2020-813 DC | LFI 2021 | aucune de fond fiscale (malus et autres validés) |
| 2021-832 DC | LFSS 2022 | cavaliers |
| 2021-833 DC | LFI 2022 | procédure uniquement |
| 2022-842 DC | LFR 2022 | aucune |
| 2022-845 DC | LFSS 2023 | cavaliers et prestations (autre groupe) |
| 2022-847 DC | LFI 2023 | procédure uniquement |
| 2023-849 DC | LFRSS 2023 | procédure (retraites, autre groupe) |
| 2023-860 DC | LFSS 2024 | cavaliers et prestations |
| **2023-862 DC** | LFI 2024 | art. 31 (exonérations des fédérations sportives reconnues par le CIO, égalité) ; autres articles : procédure |
| 2025-874 DC | LFI 2025 | aucune censure de fond repérée (articles censurés : procédure, d'après le filtre des motifs) |
| 2025-875 DC | LFSS 2025 | cavaliers ; art. 52 (rendez-vous médicaux, non fiscal) |
| 2025-899 DC | LFSS 2026 | décision de décembre 2025 : mesures postérieures hors période |

Non trouvées : aucune décision DC sur les LFI 2007, 2008 et 2009 dans l'index des décisions de décembre 2006 à janvier 2009 (lois probablement non déférées, non vérifié) ; LFSS 2021 (numéro non identifié : 2020-807 DC est la loi ASAP) ; une partie des décisions 2010-2011 n'a pas été obtenue (LFR de ces années). Voir § 6.

## 3. QPC fiscales repérées (2010-2025)

79 commentaires de QPC dont l'intitulé est fiscal et qui contiennent une mention de censure ou de non-conformité (le filtre ne distingue pas les décisions de conformité qui citent des censures). Issue vérifiée sur le commentaire seulement pour : 2014-417 (boissons énergisantes, censure partielle), 2015-520 et 2016-553 (régime mère-fille, discrimination « à rebours »), 2016-571 et 2017-660 (contribution de 3 %), 2016-615 (CSG des affiliés à un autre régime : conformité). Les autres (p. ex. 2013-362 et 2017-669 taxe sur les éditeurs de télévision, 2014-404 rachat d'actions, 2015-498 retraites chapeaux, 2016-614 art. 123 bis, 2017-629 CVAE des groupes, 2017-679 trust et ISF, 2018-733 CFE des ports, 2020-854 taux réduit d'IS) n'ont pas été suivies : dispositions anciennes ou de faible rendement, et aucun chiffrage de mesure postérieure de même nature n'a été repéré dans les sources lues. C'est une limite : la liste n'est pas exploitée jusqu'au bout.

## 4. Arrêts de la CJUE sur la fiscalité française suivis

| Arrêt | Objet | Mesures postérieures de même nature |
|---|---|---|
| C-169/98 et C-34/98, 15/02/2000 | CSG et CRDS sur des personnes affiliées à un autre régime de l'Union (unicité de législation, règlement 1408/71) | `ps_nonresidents_2012` (cas retenu) ; réaffectation au FSV par la LFSS 2016 (voir § 5) |
| C-9/02 de Lasteyrie du Saillant, 11/03/2004 | exit tax de 1998 contraire à la liberté d'établissement | `exit_tax_2011` (cas retenu) |
| C-338/11 à 347/11 Santander, 10/05/2012 | retenue à la source sur les dividendes versés aux OPCVM étrangers | la suppression de la retenue (LFR II 2012) est la mise en conformité, pas une mesure exposée ; la contribution de 3 % qui la finance est d'un autre mécanisme (hors champ) |
| C-623/13 de Ruyter, 26/02/2015 | prélèvements sociaux sur les revenus du capital des affiliés à un autre régime | réaffectation au FSV (LFSS 2016) : voir § 5 |
| C-365/16 AFEP, 17/05/2017 | contribution de 3 % et directive mères-filiales | aucune mesure postérieure de même nature trouvée |
| Steria (2015), Sofina (2018), Jahin (2018), Dreyer (2019), Accor (2011) | cités par des sources secondaires lues ou par la recherche web | non lus : piste non vérifiée |

## 5. Pistes suivies sans cas retenu (motif)

- **Taxe exceptionnelle sur les hautes rémunérations versée par les entreprises (LFI 2014, art. 15).** Votée après 2012-662 DC (et 2000-437 DC) : J1 plausible, appliquée. Ex ante lu : « Le rendement attendu est de 420 millions d’euros sur deux ans, dont 260 millions en 2014 » (AN, rapport général n° 1428 t. II, p. 195) ; la Cour retient +0,3 Md€ en prévision (NEB 2014 recettes fiscales, p. 39). **Réalisé non trouvé** sur source primaire : NEB 2014 et 2015 « recettes fiscales », RBDE 2015, rapports AN d'application des mesures fiscales n° 2172 et 3003 lus sans montant ; un chiffre de 309 M€ (2014) attribué au ministre dans la presse étrangère n'a pas été retenu. Le tome I des Voies et moyens du PLF 2016 n'a pas été trouvé en ligne.
- **Composante carbone (contribution climat-énergie, LFI 2014).** J1 (2009-599 DC), appliquée. Ex ante : « 340 millions d’euros en 2014, 2,41 milliards en 2015 et 4,05 milliards d’euros en 2016 » (rapport n° 1428 t. II, p. 479). Réalisé : la Cour (NEB 2015, p. 25) donne +1,2 Md€ pour 2015, chiffrage administratif des mesures nouvelles (part État de la TICPE, hors TICGN et charbon, en écart à 2014) : **périmètre différent**, écarté. Même règle que `carbone_convergence_2018` (classé `administratif`).
- **Réduction dégressive de CSG au titre de la prime d'activité (LFI 2016, art. 77).** Mécanisme identique à 2000-437 DC (J1 plausible) ; censurée par 2015-725 DC pour un autre motif (égalité salariés / non-salariés). Pas de chiffrage d'impact propre : le dispositif verse « en déduction de la prime d'activité » une fraction de prestation déjà budgétée (commentaire 2015-725 DC, § III). Écarté (ex ante nul ou non défini).
- **Plafonnement de l'ISF revoté (LFI 2014, art. 13).** J1 certain (objet analogue à 2012-662 DC, censure pour chose jugée par 2013-685 DC). Amendement sans chiffrage trouvé. Écarté.
- **Plus-values de terrains à bâtir sans abattement (LFI 2014, art. 27).** J1 probable (2012-662 DC, art. 15, même assiette, art. 13 DDHC). Chiffrage non trouvé dans le rapport n° 1428. Écarté (ligne d'information dans `hors_champ_fiscalite.csv`).
- **Taxe sur les imprimés (LFI 2003, art. 88).** J1 (2000-441 DC), censurée. Chiffrage non recherché faute de temps. Piste ouverte.
- **Forfait social différencié (LFSS 2014, art. 14).** Votée après 2013-672 DC (clauses de désignation) pour en contourner l'effet ; censurée par 2013-682 DC. Mesure incitative sans chiffrage de rendement trouvé. Écarté.
- **Prélèvements sociaux des non-résidents réaffectés au FSV (LFSS 2016).** J1 (de Ruyter 2015). L'enjeu cité par des amendements (« environ 250 millions d'euros ») n'est ni un chiffrage officiel lu ni un réalisé ; restitutions non trouvées. Écarté.
- **Extension de l'exonération de la contribution de 3 % (LFR 2016, art. 95).** Votée après 2016-571 QPC (J1), contribution entièrement censurée en 2017. Chiffrage non recherché. Piste ouverte.
- **Plafonnement global des niches (LFI 2009).** Voté après 2005-530 DC (J1 si l'on retient le mécanisme ; motif d'intelligibilité). Chiffrage et réalisé non recherchés. Piste ouverte.
- **Contribution sur les boissons sucrées (LFI 2012) et autres taxes comportementales postérieures à 2009-599 DC.** Rattachement J1 discutable (taxe de rendement autant qu'incitative) ; ex ante et réalisé non établis dans les sources trouvées (estimations de presse divergentes). Écarté.
- **Taxe à 75 %** : la consigne la citait comme piste ; elle est retenue en cas (J1 discutable via 2000-437 DC, voir la note de la ligne). Si l'attribution juge « aucun », elle passe hors champ.

## 6. Points de vigilance pour la fusion

1. **`ps_nonresidents_2012` n'est pas hors champ.** À la date du vote (août 2012), la CJCE avait déjà jugé (15/02/2000, C-169/98 et C-34/98) que la CSG et la CRDS ne pouvaient être prélevées sur des personnes relevant de la sécurité sociale d'un autre État membre (unicité de législation, art. 13 du règlement 1408/71, libre circulation). Le rapporteur général cite cet arrêt dans son commentaire de l'article (r0079, p. 309) et un député en tire un doute de compatibilité en commission (p. 316). Différence : revenus d'activité en 2000, revenus du capital en 2012. La consigne la présumait hors champ ; la source lue dit le contraire. Le réalisé de `data/raw/mesures_cout.csv` (0,275) est **brut** des restitutions de Ruyter, non trouvées.
2. **`taxe_dividendes_3pct_2012` est hors champ** d'après les sources lues : l'évaluation préalable ne cite que l'arrêt Santander (autre mécanisme) et conclut à la compatibilité ; toutes les décisions de même nature (2015-520, 2016-553, 2016-571 QPC, AFEP, 2017-660 QPC) sont postérieures au vote. Seule réserve : l'arrêt Accor (CJUE 2011, précompte mobilier) n'a pas été lu.
3. **Rapprochements laissés à l'attribution** (même motif, mécanisme voisin) : `taxe_75pct_2013` et `cotisations_salariales_degressives_2015` (via 2000-437 DC), `boissons_energisantes_2013` (via les taxes environnementales de 2000 et 2002), `taxe_carbone_2010`. C'est là que le critère « même nature » est le plus fragile.
4. **Réalisés faibles** : `exit_tax_2011` et `boissons_energisantes_2014` reposent sur des sources secondaires (`low`). L'écart de la seconde vient surtout du comportement des fabricants, pas du risque juridique.
5. **Doublon** : `ps_nonresidents_2012` reprend l'id et les valeurs de `data/raw/mesures_cout.csv`.
6. **Cas `observe` retenus** : 7, dont 4 censurés avant application (réalisé 0 : `taxe_carbone_2010`, `boissons_energisantes_2013`, `taxe_75pct_2013`, `cotisations_salariales_degressives_2015`), 2 censurés en partie (`ps_nonresidents_2012`, `boissons_energisantes_2014`), 1 appliqué (`exit_tax_2011`). L'échantillon est dominé par des censures, parce que les mesures appliquées de même nature trouvées (taxe sur les hautes rémunérations, composante carbone) n'ont pas de réalisé sur le même périmètre : ce biais pousse le facteur vers 0 et doit être dit dans le rapport.
7. **Décisions non lues** (§ 2) : une censure de fond fiscale dans la LFSS 2021 ou des LFR 2010-2011 a pu échapper au relevé ; pour la LFI 2011 et la LFI 2025, le caractère procédural des censures est déduit de la structure de la décision, pas vérifié article par article.

## 7. Sites inaccessibles

- conseil-constitutionnel.fr : coupe la connexion (`curl` et WebFetch) après une rafale ; contourné par web.archive.org et le dépôt public des commentaires.
- web.archive.org : coupe aussi la connexion par moments (rafales) ; relancé lentement, une centaine de pages non obtenues.
- legifrance.gouv.fr : 403.
- eur-lex.europa.eu, curia.europa.eu : contenu vide (application JavaScript ou défi anti-robot).
- actu-juridique.fr : 403 (WebFetch).
