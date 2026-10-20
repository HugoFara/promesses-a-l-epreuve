# T23, groupe « prestations » : notes de collecte (étape 1)

Date d'accès de toutes les sources : 2026-10-20. Champ : prestations sociales, conditions d'accès, dépenses et économies publiques (immigration, asile, AME, contrôle des prix compris). La fiscalité et les prélèvements (y compris cotisations et CSG) sont laissés au groupe fiscalité.

Fichiers produits :

- `cas_prestations.csv` : 5 cas dans le champ J1 au moment du vote, avec chiffrage avant adoption et réalisé (colonnes de T18 `cout_<G>.csv`, plus `pays`, `critere`, `decision_anterieure`, `issue_juridique`, `decision_posterieure`) ;
- `hors_champ_prestations.csv` : 4 mesures censurées sur le fond sans décision antérieure de même nature ;
- `sources_prestations.csv` : 43 fichiers archivés dans `sources/T23/prestations/`, avec leur sha256.

## 1. Méthode

Le point de départ, ce sont les décisions, pas les mesures. Les décisions ont été trouvées de trois façons : les commentaires officiels du Conseil constitutionnel (2024-6 RIP, 2020-856 QPC et 2010-1 QPC), qui recensent la jurisprudence antérieure ; des recherches web par thème (nationalité et résidence, pensions, asile, AME, assurance chômage, tarifs réglementés) ; et ArianeWeb pour le Conseil d'État. Pour chaque décision, j'ai vérifié le motif : fond ou procédure. J'ai ensuite cherché les mesures de même mécanisme votées après la décision, puis, pour chacune, un chiffrage avant adoption et un réalisé publié.

Cette méthode a une limite : je n'ai pas pu interroger la base QPC du Conseil constitutionnel par matière. Le site a coupé les connexions (voir § 6). Le recensement des QPC n'est donc **pas exhaustif**. Il couvre les censures citées par les commentaires officiels et celles qu'ont fait remonter les recherches web.

## 2. Décisions parcourues (25)

| Décision | Objet | Motif | Fond ou procédure | Suite |
|---|---|---|---|---|
| CC 89-269 DC, 22/01/1990 | Allocation supplémentaire du FNS réservée aux étrangers couverts par une convention | Égalité (cons. 35) | Fond, censure | J1 pour les conditions de nationalité (cas `harkis_allocation_reconnaissance_2003`) ; RSA 2008, ASPA 2012 et loi immigration 2023 exclus (§ 4) |
| CC 90-285 DC, 28/12/1990 | Complément de pension de victimes de guerre selon la date de la demande | Égalité | Fond, censure (lue seulement dans le commentaire de 2020-856 QPC) | J1 discutable pour `mineurs_greves_1948_lfi2015` |
| CC 93-325 DC, 13/08/1993 | Loi immigration 1993 | Formule de principe sur les droits sociaux des étrangers | Téléchargée, pas analysée en détail | Aucune |
| CC 2000-435 DC, 07/12/2000 | Exonération de cotisations des marins-pêcheurs sinistrés, conditionnée au paiement du rôle d'équipage | Égalité | Fond, censure (lue seulement dans un commentaire) | C'est un prélèvement : laissé au groupe fiscalité |
| CE Ass., Diop, 30/11/2001 | Cristallisation des pensions selon la nationalité | Art. 14 CEDH + art. 1 P1 | Fond | J1 pour `decristallisation_lfr2002` et `decristallisation_lfi2007` |
| CEDH, Koua Poirrez c. France, 30/09/2003 | AAH refusée à un étranger sans convention de réciprocité | Art. 14 + art. 1 P1, violation (§ 49-50) | Fond | J1 possible pour les conditions de nationalité ; aucune mesure postérieure chiffrée (§ 4) |
| CE, Aides, 07/06/2006 | Condition de 3 mois de résidence pour l'AME, appliquée aux mineurs | CIDE art. 3-1 | Fond, annulation partielle | Hors champ (`ame_residence_mineurs_2005`) ; aucune mesure postérieure de même nature trouvée |
| CC 2010-1 QPC, 28/05/2010 | Cristallisation (LFR 1981, LFR 2002 art. 68, LFI 2007 art. 100) | Égalité | Fond, censure | Décision postérieure des deux cas de décristallisation ; LFI 2011 art. 211 exclu (§ 4) |
| CC 2010-18 QPC, 23/07/2010 | Carte du combattant des supplétifs : condition de nationalité ou de domicile | Égalité | Fond, censure | Aucune mesure postérieure chiffrée ; date d'insertion de la condition non vérifiée |
| CC 2010-93 QPC, 04/02/2011 | Allocations des harkis : conditions de nationalité (lois de 1987, 1994 et 2005, LFR 1999) | Égalité (cons. 10) | Fond, censure partielle ; art. 67 de la LFR 2002 déclaré conforme | Décision postérieure de `harkis_allocation_reconnaissance_2003` |
| CC 2010-108 QPC, 25/03/2011 | Partage de la pension de réversion entre lits (art. L. 43 CPCMR, 1964) | Égalité | Fond, censure | Mesure votée avant 2000 : hors période |
| CC 2011-137 QPC, 17/06/2011 | RSA : condition de 5 ans de titre de séjour autorisant à travailler | — | Conformité | Pas une censure, mais montre que le champ J1 couvre aussi des mesures validées |
| CC 2014-698 DC, 06/08/2014 | Réduction dégressive des cotisations salariales (LFRSS 2014) | Égalité | Fond, censure | C'est un prélèvement : laissé au groupe fiscalité |
| CC 2015-504/505 QPC, 04/12/2015 | Harkis : condition de « statut civil de droit local » (LPM 2013) | — | Conformité (lue dans qpc360) | Aucune censure |
| CJUE, ANODE, C-121/15, 07/09/2016 | Tarifs réglementés du gaz | Directive 2009/73 | Fond (lu dans les motifs du CE 2017) | J1 pour `bouclier_gaz_2023` |
| CE, 23/12/2016, n° 394819 | Montant additionnel de l'ADA (4,20 €) | Directive 2013/33, montant insuffisant | Fond, annulation partielle | Hors champ (`ada_montant_additionnel_2015`) ; suite = relèvement (remède) |
| CE Ass., ANODE, 19/07/2017 | Décret de 2013 sur les TRV du gaz | Directive 2009/73 | Fond, annulation | J1 pour `bouclier_gaz_2023` |
| CE, 18/05/2018, n° 413688 | TRV de l'électricité applicables à tous les sites jusqu'à 36 kVA | Directive 2009/72 | Fond, annulation partielle | J1 pour le bouclier électricité, exclu (§ 4) |
| CE, Cimade, 31/07/2019 | Refus et retrait des conditions matérielles d'accueil (décret 2018) | Directive 2013/33, art. 20 | Fond, annulation partielle | Hors champ (`cma_retrait_2018`) ; mesure de 2023 (art. 69 de la loi immigration) censurée comme cavalier, sans chiffrage |
| CE, 25/11/2020, n° 434920 | Assurance chômage : calcul du SJR (décret 2019) | Égalité | Fond, annulation (le bonus-malus est annulé pour un motif de compétence) | Hors champ (`sjr_decret_2019`) ; J1 pour le décret du 30 mars 2021, exclu faute de réalisé (§ 4) |
| CE, référé, 22/06/2021, n° 452210 | Décret du 30 mars 2021 (SJR) | Doute sérieux sur l'entrée en vigueur au 1er juillet 2021 | Suspension, pas une censure | — |
| CE, 15/12/2021, n° 452209 et autres | Décret du 30 mars 2021 et décrets de juin 2021 | — | Rejet (et non-lieu partiel) | Le SJR de 2021 a été appliqué |
| CC 2020-856 QPC, 18/09/2020 | Allocations aux mineurs grévistes de 1948 et 1952 (LFI 2015, art. 100) | Égalité | Fond, censure partielle | Décision postérieure de `mineurs_greves_1948_lfi2015` |
| CC 2023-863 DC, 25/01/2024 | Loi immigration | Les articles sur les prestations (15, 19, 67, 68, 69…) sont censurés comme cavaliers (procédure) ; seuls l'art. 1er (quotas), « de plein droit » à l'art. 14 et l'art. 38 sont censurés sur le fond | Procédure pour les prestations | Hors champ comme décision ; l'art. 19 est dans le champ J1 (89-269 DC), mais exclu faute de chiffrage |
| CC 2024-6 RIP, 11/04/2024 | PPL référendaire : 5 ans de résidence ou 30 mois d'affiliation pour APL, prestations familiales, APA et droit au logement | Al. 10 et 11 du Préambule de 1946 (cons. 13) | Fond, non-conformité | J1 pour toute mesure postérieure de même nature (notamment `rn24_preference_nationale`, juin 2024) ; aucune mesure de ce type votée entre avril 2024 et 2025 n'a été trouvée |

Vues dans les recherches mais pas lues (non utilisées) : CEDH, Okitaloshima Okonda Osungu et Selpa Lokongo c. France (2015, non-violation, d'après un résumé de recherche) ; CJUE, 29 juillet 2024, revenu de citoyenneté italien (10 ans de résidence, discrimination indirecte ; d'après un communiqué de presse vu dans les résultats, ne vise pas la France).

## 3. Cas retenus (5)

| id | Issue | Ex ante → ex post (Md€) | Type | Confiance | Point à trancher |
|---|---|---|---|---|---|
| `decristallisation_lfr2002` | censurée (2010, après application) | 0,123 → 0,0884 (haut 0,1066) | observe | medium | Le critère de nationalité est remplacé par celui du pays de résidence : même mécanisme que la décision Diop ? |
| `decristallisation_lfi2007` | censurée (2010, après application) | 0,110 → 0,087 | observe | medium | Ex ante lu dans une réponse ministérielle postérieure au vote et dans la Cour ; année du réalisé non précisée |
| `harkis_allocation_reconnaissance_2003` | censurée en partie (2011) | 0,0055 → 0,007 | observe | medium | Réalisé lu dans un rapport parlementaire, non daté ; l'art. 67 lui-même a été déclaré conforme |
| `mineurs_greves_1948_lfi2015` | censurée en partie (2020) | 0,0007 → 0,000595 (haut 0,000635) | observe | low | Lien J1 faible (90-285 DC) ; sources incohérentes ; montants minimes |
| `bouclier_gaz_2023` | appliquée | 6,8 → 1,35 | observe (estimation CRE de juillet 2023) | medium | Doublon de `data/raw/mesures_cout.csv` (inclus_stats = 0) |

Par issue : 2 censurées, 2 censurées en partie, 1 appliquée, 0 retirée, 0 restituée. Les 5 cas sont en `observe`. Les quatre premiers sont des dépenses que la censure a **augmentées** par la suite. Le réalisé mesuré est antérieur à la censure, il n'est donc pas nul. Le réalisé vaut 0 seulement pour une mesure censurée avant application : aucun des cas retenus n'est dans ce cas (le seul exemple trouvé, le SJR de 2019, est hors champ).

## 4. Mesures dans le champ (J1) mais exclues, avec le motif

- **Décret du 30 mars 2021 sur le SJR** (J1 : CE 25/11/2020). Le chiffrage avant adoption existe : Unédic, avril 2021, p. 7, « Calcul du SJR et de la durée avec un plancher à 57,14 % » : 210 M€ en 2021, 940 M€ en 2022, 1 000 M€ en régime de croisière. Issue : appliquée (suspendue en juin 2021, entrée en vigueur au 1er octobre 2021, recours rejetés le 15/12/2021). **Réalisé monétaire non trouvé**. L'évaluation de l'Unédic (mars 2025, synthèse p. 4) écrit seulement : « Les observations de la montée en charge de la réforme confirment ces estimations ex ante ». Pages consultées sans montant observé : suivi de février 2024, étude SJR de mars 2025, recherches sur les comptes 2022 et sur la Cour des comptes. C'est le meilleur candidat à compléter si un compte de l'Unédic isole l'effet.
- **ASPA, condition portée de 5 à 10 ans de titre de séjour (LFSS 2012, art. 94)** (J1 : 89-269 DC, Koua Poirrez). Ex ante trouvé seulement dans la presse (Lyon Capitale, 28/10/2011 : « 100 millions d'euros seront à terme économisés », sans auteur du chiffrage) ; évaluation préalable du PLFSS 2012 non lue ; réalisé non trouvé (selon un résumé de recherche, non lu, une note de la Caisse des dépôts cite la condition comme « second facteur » de baisse des effectifs, sans chiffre).
- **RSA, condition de 5 ans de titre de séjour (loi du 1er décembre 2008)** : selon une réponse ministérielle, la condition reprend celle du RMI ; aucun chiffrage propre trouvé. QPC 2011-137 : conformité.
- **Loi immigration 2023, art. 19 (5 ans de résidence ou 30 mois d'affiliation)** : amendement n° 3 rect. quater du Sénat, sans chiffrage ; texte voté sans étude d'impact sur ce point. Censuré comme cavalier (2023-863 DC, § 95-96) ; réalisé 0. Exclu faute de chiffrage avant adoption.
- **Loi du 23 février 2005 sur les rapatriés, art. 6 et 9** (conditions de nationalité censurées en 2011). Ex ante = plafond théorique : « jusqu'à 776 millions d'euros de dépenses supplémentaires dans l'hypothèse où l'ensemble des bénéficiaires choisirait l'option la plus coûteuse » (Sénat, rapport n° 104, p. 26-27). Le réalisé sur ce périmètre n'a pas été trouvé ; le rapport au Parlement de juin 2013 n'a pas été lu.
- **LFI 2011, art. 211 (alignement complet des pensions)** : c'est le remède à la décision 2010-1 QPC, qui supprime la différence censurée. Ce n'est pas le même mécanisme. Chiffrage : 82, 100 et 125 M€ pour 2011-2013 (AN, QE 91491 et 96843) ; réalisé non cherché.
- **LFI 2002, art. 131 et 132 (levée de forclusion et réversion au taux cristallisé)**, votés le 28/12/2001, après la décision Diop : dans le champ, mais aucun chiffrage trouvé (non cherché en détail).
- **Bouclier tarifaire électricité 2023** (J1 : CE 18/05/2018). Le seul ex ante disponible (CRE, juillet 2023, 21,8 Md€, ligne `bouclier_elec` de `mesures_cout.csv`) est postérieur à l'adoption. Le chiffrage du PLF 2023 trouvé est « brut » (34 Md€ pour l'électricité, propos ministériels relayés par la presse) : ce n'est pas le même périmètre.
- **Gel des TRV du gaz en 2022 (LFI 2022, art. 181)** : le périmètre a changé en cours d'année (extension au 1er septembre 2022) ; d'après la note de `mesures_cout.csv`, 1,2 Md€ étaient budgétés. Non retenu.
- **PPL du Sénat de 2025 (2 ans de résidence, ppl24-299)** : vue dans les résultats de recherche ; pas votée à ma connaissance, et non vérifié.
- **Contrôle des prix hors énergie** (encadrement des loyers, blocage de prix) : aucune décision de censure sur le fond liée à une mesure à coût budgétaire n'a été trouvée ; ces mesures n'ont en général ni chiffrage ni réalisé budgétaire.

## 5. Hors champ (4)

Voir `hors_champ_prestations.csv` : SJR 2019 (CE 2020, réalisé 0, ex ante Unédic 0,25 Md€ en 2020 et 1,1 Md€ en 2021), AME des mineurs (CE 2006), montant de l'ADA (CE 2016), retrait des conditions matérielles d'accueil (CE 2019). Ce sont des décrets, sauf l'AME, dont la condition est législative (LFR 2003). Deux autres censures sur le fond ne figurent pas dans le CSV : la mesure était votée avant 2000 (2010-108 QPC, art. 26 de la LFR 1981 dans 2010-1 QPC) ou relève des prélèvements (2000-435 DC, 2014-698 DC).

## 6. Sites inaccessibles et lacunes

- **conseil-constitutionnel.fr** : environ 10 pages téléchargées par `curl`, puis « Connection reset by peer » sur toutes les requêtes. WebFetch a renvoyé ECONNRESET, et le miroir `webview-ccfr…aquaray.com` a aussi coupé. web.archive.org a fonctionné de façon intermittente (2023-863 DC et 2014-698 DC récupérées, les autres non). Le stockage `oos.cloudgouv-eu-west-1.outscale.com` (commentaires qpc360) a fonctionné. Les décisions 90-285 DC, 2000-435 DC, 2017-690 QPC, 2016-534 QPC et 2014-433 QPC n'ont pas été lues ; les deux premières l'ont été à travers le commentaire de 2020-856 QPC.
- **HUDOC** : l'API de recherche renvoie 404. Koua Poirrez a été lu sur une copie de l'université de Galway.
- **Cour des comptes, RPA 2010** : le chapitre a été lu sur une copie du GISTI ; je n'ai pas trouvé la version sur ccomptes.fr.
- **Sénat, rapport n° 214 (2016-2017)** : seule la première partie (15 pages) a été téléchargée ; les montants des mineurs grévistes sont lus dans le commentaire du CC.
- **Légifrance** : non utilisé ; les numéros d'articles viennent des décisions et des rapports.

## 7. Points pour la fusion

- `bouclier_gaz_2023` est un doublon voulu de `data/raw/mesures_cout.csv` (même id, mêmes valeurs).
- Les deux cas de décristallisation partagent la décision antérieure (Diop) et la décision postérieure (2010-1 QPC). Ils ne sont pas indépendants.
- Les quatre premiers cas sont de petites dépenses de réparation ou de pension, de 0,0006 à 0,123 Md€. Si la règle multiplie les montants quel que soit leur signe, ces rapports (0,72 ; 0,79 ; 1,27 ; 0,85) disent quelque chose de l'erreur de chiffrage de dépenses de reconnaissance, et peu du risque juridique : le réalisé est mesuré avant la censure. À signaler dans le rapport.
- `issue_juridique = censurée` est mis même quand la censure intervient après plusieurs années d'application. La colonne `note` donne les dates d'application.
