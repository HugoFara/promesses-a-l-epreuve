# T23 : règle « Base juridique contestée », rapport (première version, après fusion)

Version du 20/10/2026, rédigée par l'agent de fusion (§ 3, étape 3 de `CONSIGNE.md`), avant l'attribution à l'aveugle. Les sections 1, 3 et 4 reprennent ce qu'ont trouvé les collecteurs (`parts/`). La section 2 sera remplie après l'attribution. La section 5 liste les décisions laissées à l'intégrateur. Rien n'a été corrigé dans les données collectées : les points de méthode sont seulement signalés.

## Fichiers

| Fichier | Contenu |
|---|---|
| `cas_passes.csv` | 12 cas passés (7 fiscalité, 5 prestations). Colonnes de `data/raw/mesures_cout.csv` dans le même ordre, puis colonnes T18 (`regle_pressentie`, `url`, `citation`, `page`, `groupe`), puis colonnes T23 (`critere`, `decision_anterieure`, `issue_juridique`, `decision_posterieure`), puis deux colonnes recalculées (`ecart_calcule`, `rapport_realise_ex_ante`) |
| `hors_champ.csv` | 28 lignes (24 fiscalité, 4 prestations). Une colonne `hors_champ` a été ajoutée : `non` pour la seule ligne d'information (`pv_terrains_sans_abattement_2014`) |
| `lignes_programmes.csv` | copie à l'identique de `parts/lignes_programmes.csv` (122 lignes) |
| `sources.csv` | 117 sources des trois groupes, avec une colonne `groupe` et le résultat du contrôle `controle_sha256` |
| `correspondance.csv` | lien entre l'id anonyme (L001 à L122) et l'id d'origine, le fichier et le programme. Ce fichier ne doit pas être donné à l'agent d'attribution |
| `aveugle/` | `cas_passes.csv`, `lignes.csv`, `familles.csv`, `champ.md` (voir « Dossier aveugle » plus bas) |

### Contrôles de fusion

- **Doublons avec `data/raw/mesures_cout.csv`** :
  - `ps_nonresidents_2012` (dans `cas_passes.csv`). L'id existe déjà. `ex_ante` (0,3) et `ex_post_central` (0,275) sont identiques. Ce qui diffère :
    - `inclus_stats` : 0 dans `data/raw`, 1 ici ;
    - `ex_post_bas` : 0,275 dans `data/raw`, vide ici ;
    - `cause_principale` : « Aucune (coût conforme) » dans `data/raw`, « Risque juridique (restitution partielle…, non chiffrée) » ici ;
    - `comportement_inclus_ex_ante` : `inconnu` dans `data/raw`, `non` ici, avec une citation ;
    - `indicateur` : « brut des restitutions » est ajouté ici ;
    - `annee_ex_post` : 2013 dans `data/raw`, 2012-2013 ici ;
    - `realise_publie_le` : 2014-07-22 dans `data/raw`, 2014-07 ici ;
    - `selection` (`test_regles`) et `drapeaux` (`ex_post_calcule;ex_ante_secondaire`) sont vides ici ;
    - libellé, estimateur et note sont complétés.

    La note du collecteur dit « mêmes valeurs », ce qui est vrai des montants mais pas de `inclus_stats`.
  - `bouclier_gaz_2023` (dans `cas_passes.csv`). L'id existe déjà. Montants et `inclus_stats` (0) sont identiques. Ce qui diffère : libellé détaillé, note, pages, citation ex post raccourcie, `comportement_inclus_ex_ante`, `annee_ex_ante`, `annee_ex_post` et `realise_publie_le` sont renseignés ici et vides dans `data/raw`. La colonne `selection` (`generale` dans `data/raw`) est vide ici.
  - `taxe_dividendes_3pct_2012` (dans `hors_champ.csv`). L'id existe déjà. `ex_ante` (1,1) est identique. Le libellé de `data/raw` mentionne la censure et la restitution, pas celui-ci. La citation ex ante n'a pas été relue (« valeur reprise de data/raw/mesures_cout.csv, non relue ici »), d'où la confiance `medium` au lieu de `high`.

  Ces trois ids sont aussi dans `recherche/T18/mesures_cout_nouvelles.csv`, d'où ils viennent.
- **Doublons entre groupes** : aucun id n'est commun aux fichiers fiscalité et prestations (cas et hors champ). Aucune mesure n'est en double sous deux ids différents : la réduction dégressive de cotisations (2014-698 DC) et l'exonération des marins-pêcheurs (2000-435 DC) ont été laissées au groupe fiscalité par le groupe prestations, et le groupe fiscalité n'a retenu que la première. Il y a en revanche un doublon de sens dans les lignes de programme : `l_gel` (panier) reprend `nfp_blocage_prix`, et `l_pfu` reprend `nfp_flat` (signalé par le collecteur).
- **sha256** : 117 fichiers listés dans les trois `parts/sources_*.csv` (41 fiscalité, 43 prestations, 33 programmes, dont 13 sources reprises de T17, T20 et T22). Tous sont présents et leur sha256 correspond. Aucun fichier de `sources/T23/` n'est absent des listes.
- **Écarts recalculés** : les parts n'avaient pas de colonne d'écart. `ecart_calcule` = (ex_post_central − ex_ante × deflateur_ex_ante) / (ex_ante × deflateur_ex_ante) ; `rapport_realise_ex_ante` = ex_post_central / (ex_ante × deflateur_ex_ante). `deflateur_ex_ante` vaut 1 pour les 12 cas.
- **Ajout mécanique** : la colonne `pays` manquait dans `cas_fiscalite.csv`. Elle vaut « France » pour les 7 cas.

### Dossier aveugle

- `aveugle/cas_passes.csv` : `id, mesure, annee, sens, ex_ante_md_eur, estimateur_ex_ante, decision_anterieure`. Il ne contient ni réalisé, ni issue juridique, ni décision postérieure, ni note, ni citation ex post. L'indicateur n'y figure pas, parce que celui de `ps_nonresidents_2012` (« brut des restitutions ») révèle l'issue.
- `aveugle/lignes.csv` : `id` (L001 à L122, dans un ordre tiré au hasard avec la graine 23, pour ne pas regrouper les lignes par programme), `ligne, type, montant_md_eur, decision_ou_texte, citation`. Il ne contient ni programme, ni parti, ni id d'origine, ni URL, ni critère du collecteur. Le `type` vient de `application_lignes.csv`. Pour les paniers, qui n'ont pas de colonne type, il est déduit du signe : « Recette ou économie » ou « Dépense ou baisse de recette ».
- `aveugle/familles.csv` : `famille, libelle, justification` de `data/raw/familles.csv`, sans la colonne `regle`.
- `aveugle/champ.md` : le § 1 de la consigne tel quel et le § 3, étape 4.
- **Contrôle de fuite** : les mots « censur », « annul », « restitu », « QPC », les numéros des décisions postérieures, les noms de partis et les préfixes d'id ont été recherchés dans les deux CSV aveugles. Il reste des occurrences de « censurée », « annulé » ou « QPC », mais elles décrivent toutes des décisions **antérieures** (par exemple 2012-659 DC pour `boissons_energisantes_2014`, 2019-774 QPC) ou le contenu d'une mesure (« abrogation 2023 », « annuler les coupes HLM »). « LFI » n'y désigne que des lois de finances initiales.

#### Champs retouchés dans le dossier aveugle

Libellés (`mesure`, `ligne`) :

| id | Avant | Après |
|---|---|---|
| `taxe_carbone_2010` | « …(LFI 2010, art. 7, 9 et 10), censurée avant application » | « …(LFI 2010, art. 7, 9 et 10) » |
| `boissons_energisantes_2013` | « …(LFSS 2013, art. 25, amendement parlementaire), censurée avant application » | « …amendement parlementaire) » |
| `taxe_75pct_2013` | « …(« taxe à 75 % », PLF 2013, art. 12 de la loi), censurée avant application » | « …art. 12 de la loi) » |
| `cotisations_salariales_degressives_2015` | « …(Pacte de responsabilité, LFRSS 2014, art. 1er), censurée avant application » | « …LFRSS 2014, art. 1er) » |
| L117 (`nfp_taxe_macron`) | « Abolir la « taxe Macron » de 10 % sur les factures d'énergie (TICFE) » | « Abolir la taxe de 10 % sur les factures d'énergie (TICFE) » (le nom d'une personnalité désigne le camp politique) |

`boissons_energisantes_2014` : « , recréée après la censure de 2012 » retiré par l'intégrateur avant l'attribution, parce que le libellé révélait l'issue de `boissons_energisantes_2013`. La décision antérieure du cas 2014 (2012-659 DC) reste dans le dossier : elle est la censure du cas 2013, que l'agent d'attribution peut donc déduire. Les deux cas ne sont pas indépendants ; le cas 2013 est à lire comme `issue_connue = oui`, quoi que réponde l'agent.

Autres champs :

- Estimateur ex ante, parce qu'il citait la décision postérieure :
  - `cotisations_salariales_degressives_2015` : « , citée par le commentaire officiel de la décision 2014-698 DC » est retiré ;
  - `mineurs_greves_1948_lfi2015` : « , et par le commentaire du Conseil constitutionnel » est retiré.
- `decision_anterieure`, réduite à la référence, au motif et à la citation. Les URL, les « Sources : » et les appréciations du collecteur sur la « même nature » ont été retirés, pour que l'agent juge seul. Le détail par cas :
  - `ps_nonresidents_2012` : « Même mécanisme… ; même motif » est retiré ; « L'arrêt portait sur des revenus d'activité » est gardé ;
  - `cotisations_salariales_degressives_2015` : « À confirmer » et « Mécanisme proche, motif différent (voir note) » sont retirés (le motif différent est celui de la décision postérieure) ;
  - `mineurs_greves_1948_lfi2015` : « lue dans le commentaire de 2020-856 QPC » est retiré, parce qu'il cite la décision postérieure ;
  - `exit_tax_2011`, `taxe_carbone_2010`, les deux décristallisations, `harkis_allocation_reconnaissance_2003` et `bouclier_gaz_2023` : URL et renvois de page retirés.
- `decision_ou_texte` des lignes :
  - les étiquettes « J1 : » et « J2 : » du collecteur sont remplacées par « Décisions : » et « Texte du programme » (L115, `rn24_preference_nationale`) ;
  - « programme RN » (`rn24_asile`) et « NFP, cité par Montaigne » (`nfp_ir`, `nfp_taxe_kilometrique`) deviennent « le programme » ;
  - pour les lignes en « aucun », la phrase du collecteur « Aucune décision de même nature trouvée. » est remplacée par « Aucune décision ni texte relevé. » Elle donnait son verdict. Quand le collecteur avait examiné une décision ou un texte, cités dans la citation ou dans la note, la référence factuelle est donnée à la place, sans appréciation. C'est le cas de `nfp_taxe_macron`, `nfp_asile`, `nfp_transports`, `nfp_isf`, `nfp_flat`, `ens_retention`, `rn24_tva_elec_gaz`, `rn24_tva_pn`, `rn24_medecins`, `rn24_ir_jeunes`, `rn24_ame`, `rn24_iff`, `l_isf`, `l_zucman` et `l_pfu`.

## 1. Cas passés retenus

Le seul critère possible pour un cas passé est J1 : les 12 cas sont en J1 selon les collecteurs, et les 12 sont en `type_ex_post = observe`. `bouclier_gaz_2023` est en `inclus_stats = 0`, comme dans `data/raw`. Ces classements restent à confirmer par l'attribution à l'aveugle.

| Issue juridique | Fiscalité | Prestations | Total |
|---|---|---|---|
| censurée | 4 | 2 | 6 |
| censurée en partie | 2 | 2 | 4 |
| appliquée | 1 | 1 | 2 |
| retirée avant application | 0 | 0 | 0 |
| restituée | 0 | 0 | 0 |
| **Total** | 7 | 5 | **12** |

Détail, montants en Md€ (écarts recalculés) :

| id | Groupe | Issue | Ex ante | Réalisé | Écart | Réalisé / ex ante |
|---|---|---|---|---|---|---|
| `ps_nonresidents_2012` | fiscalité | censurée en partie | 0,3 | 0,275 | −8 % | 0,92 |
| `taxe_carbone_2010` | fiscalité | censurée | 4,2 | 0 | −100 % | 0 |
| `exit_tax_2011` | fiscalité | appliquée | 0,189 | 0,063 | −67 % | 0,33 |
| `boissons_energisantes_2013` | fiscalité | censurée | 0,035 | 0 | −100 % | 0 |
| `boissons_energisantes_2014` | fiscalité | censurée en partie | 0,06 | 0,003 | −95 % | 0,05 |
| `taxe_75pct_2013` | fiscalité | censurée | 0,21 | 0 | −100 % | 0 |
| `cotisations_salariales_degressives_2015` | fiscalité | censurée | 2,5 (coût) | 0 | −100 % | 0 |
| `decristallisation_lfr2002` | prestations | censurée (en 2010, après application) | 0,123 (coût) | 0,0884 | −28 % | 0,72 |
| `decristallisation_lfi2007` | prestations | censurée (en 2010, après application) | 0,110 (coût) | 0,087 | −21 % | 0,79 |
| `harkis_allocation_reconnaissance_2003` | prestations | censurée en partie | 0,0055 (coût) | 0,007 | +27 % | 1,27 |
| `mineurs_greves_1948_lfi2015` | prestations | censurée en partie | 0,0007 (coût) | 0,000595 | −15 % | 0,85 |
| `bouclier_gaz_2023` | prestations | appliquée | 6,8 (coût) | 1,35 | −80 % | 0,20 |

**Hors champ** (mesures censurées sur le fond sans décision antérieure de même nature) : **27**, dont 23 en fiscalité et 4 en prestations (SJR 2019, AME des mineurs, montant additionnel de l'ADA, retrait des conditions matérielles d'accueil). `hors_champ.csv` compte une 28e ligne, `pv_terrains_sans_abattement_2014`. Elle n'est pas hors champ : son collecteur la juge en J1 probable, mais elle n'a pas de chiffrage. Le groupe prestations relève deux autres censures de fond qu'il n'a pas mises dans le CSV : une mesure votée avant 2000 (2010-108 QPC) et des prélèvements laissés à la fiscalité. Pour mettre ces 27 lignes en regard des cas censurés du champ : 10 cas du champ sont censurés en tout ou en partie, et 27 censures de fond ont été trouvées hors champ.

## 2. Facteur provisoire (après attribution)

Attribution à l'aveugle : `attribution_agent.csv` (sha256 `7321f63e79628d06bec7190789bb0fa04e8d583746e23a2f0e3217a6c22e840a`), conservé tel quel. L'agent a jugé les 12 cas passés dans le champ (J1). Il dit connaître l'issue de 11 cas sur 12 (seul `mineurs_greves_1948_lfi2015` est à `non`) : le test n'est pas aveugle sur l'issue.

Calcul du § 4 de la consigne (12 cas `observe`, rapport réalisé / chiffrage avant adoption, déflateur 1 partout) :

| Statistique | Valeur |
|---|---|
| Médiane (facteur) | **0,27** |
| Premier et troisième quartiles (fourchette) | 0,00 et 0,84 |
| Cas à `issue_connue = non` | 1 (rapport 0,85) |

Rapports par cas : 0 pour les quatre censures avant application (taxe carbone 2010, boissons énergisantes 2013, taxe à 75 %, cotisations salariales dégressives) ; 0,05 (boissons 2014) ; 0,20 (bouclier gaz 2023) ; 0,33 (exit tax 2011) ; 0,72 et 0,79 (décristallisations) ; 0,85 (mineurs grévistes) ; 0,92 (prélèvements des non-résidents, brut des restitutions) ; 1,27 (harkis).

**Test sur les mêmes cas, calculé hors du pipeline avec la formule de `scripts/validation.py`** (erreur = écart entre le chiffrage corrigé et le réalisé, rapporté au chiffrage corrigé) : l'erreur médiane passe de 73,4 % sans correction à 100,0 % avec le facteur 0,27. La règle dégrade les chiffrages de son propre échantillon. La raison est mécanique : pour une mesure au réalisé nul, l'erreur relative vaut 100 % quel que soit le facteur, et le facteur éloigne les cas appliqués de leur réalisé.

Le facteur mélange deux populations : des censures avant application (réalisé 0) et des dépenses dont le réalisé est mesuré avant la censure (rapports 0,7 à 1,3), qui mesurent l'erreur de chiffrage et pas l'issue juridique. Le bouclier gaz (0,20) mesure surtout l'évolution des prix de l'énergie.

### Lignes jugées dans le champ par l'agent d'attribution

11 lignes (10 J1, 1 J2), contre 7 à la collecte :

| Ligne | Montant | Critère | Famille choisie | Collecte |
|---|---|---|---|---|
| `rn24_preference_nationale` | +6,4 | J2 | nouvelle : `prestation_condition_nationalite_residence` | J1 et J2 |
| `rn24_asile` | +1,2 | J1 | `politique_migratoire` | J1 |
| `rn24_tva_carburants` | −7,53 | J1 | `taxe_carburants` | J1 |
| `nfp_blocage_prix` | −9 | J1 | `controle_prix` | J1 |
| `l_gel` (panier) | −9 | J1 | `controle_prix` | J1 |
| `nfp_taxe_kilometrique` | +1 | J1 | `taxe_importations` | J1 |
| `nfp_ir` | +4,7 | J1 | `impot_revenu` | J1 (part CSG) |
| `rn24_ir_jeunes` | −3,7 | J1 | nouvelle : `exoneration_ir_categorielle` | aucun |
| `rn24_medecins` | −0,95 | J1 | nouvelle : `exoneration_ir_categorielle` | aucun |
| `nfp_flat` | +3,2 | J1 | nouvelle : `imposition_depart` | aucun (part exit tax ≤ 0,067) |
| `l_pfu` (panier) | +3,4 | J1 | nouvelle : `imposition_depart` | aucun (même part) |

**Conflit avec la règle « une famille, une règle »** : l'agent a rangé six lignes dans des familles existantes, qui portent déjà une règle de comportement. Attacher « Base juridique contestée » à ces familles changerait aussi des lignes que personne n'a jugées dans le champ : `l_brunes` (`taxe_carburants`), `rn24_part_fiscale` et `l_ir` (`impot_revenu`), `nfp_asile` (`politique_migratoire`). Et une ligne ne peut avoir qu'une règle : `rn24_tva_carburants` perdrait son élasticité carburants, `nfp_ir` son élasticité revenus. Le risque juridique ne dépend pas de la nature économique de la mesure : la consigne (familles définies par la nature juridique) ne l'a pas assez prévu.

## 3. Lignes de programme et de panier dans le champ (d'après la collecte)

Le collecteur a donné un critère aux 122 lignes : 89 lignes de `application_lignes.csv` et 33 de `paniers.csv`. 7 lignes sont dans le champ, toutes en J1 ; une seule est aussi en J2. Aucune n'est en J2 seul. L'attribution à l'aveugle peut changer ce classement. Montants en Md€, avec le signe du solde public.

| Programme ou panier | id | Ligne | Montant | Critère | Confiance |
|---|---|---|---|---|---|
| NFP 2024 | `nfp_blocage_prix` | Bloquer les prix des produits de première nécessité | −9 | J1 (2019-774 QPC ; CE ANODE 2017 pour l'énergie) | low |
| NFP 2024 | `nfp_ir` | IR à 14 tranches + CSG progressive | +4,7 | J1, pour la seule part CSG (2000-437 DC) | low |
| NFP 2024 | `nfp_taxe_kilometrique` | Taxe kilométrique sur les produits importés | +1 | J1 (CJCE 2/69 et 3/69, 1969) | medium |
| RN 2024 | `rn24_preference_nationale` | Prestations familiales réservées aux foyers avec un parent français ; RSA et prestations de solidarité conditionnés à 5 ans de travail | +6,4 | J1 (89-269 DC, 2024-6 RIP, Koua Poirrez, Martinez Silva) et J2 (« si nécessaire par référendum constitutionnel ») | high |
| RN 2024 | `rn24_asile` | Réforme de la politique de l'asile | +1,2 | J1 (93-325 DC) | medium |
| RN 2024 | `rn24_tva_carburants` | TVA de 20 % à 5,5 % : carburants et fioul | −7,53 | J1 (CJUE C-479/13, directive 2022/542) | medium |
| Ensemble 2024 | aucune | | | | |
| Panier LFI intégral | `l_gel` | Gel des prix de première nécessité | −9 | J1 (comme `nfp_blocage_prix`) | low |
| Panier Ensemble | aucune | | | | |
| Lignes de panier sans variante (`l_ret62`, `l_point5`, `l_eco_rg`) | aucune | | | | |

Les 115 autres lignes sont en « aucun » : 101 n'ont aucune décision de même nature trouvée, et 14 sont des lignes techniques sans mesure propre (restes non découpés, écarts, charge d'intérêts, effet emploi du SMIC). Pour la plupart des lignes de dépense, de cotisation, de retraite et de crédit, le jugement repose sur le libellé, la fiche du chiffreur et le dispositif des décisions sur les lois de finances, sans recherche web propre (`recherches_faites`).

## 4. Ce qui n'a pas été trouvé (d'après les notes des collecteurs)

**Fiscalité** (`parts/notes_fiscalite.md`) :

- Réalisé non trouvé sur source primaire pour la taxe exceptionnelle sur les hautes rémunérations (LFI 2014). Sources lues : NEB 2014 et 2015, RBDE 2015, rapports AN n° 2172 et 3003. Le tome I des Voies et moyens du PLF 2016 n'a pas été trouvé.
- Composante carbone 2014 : seul un réalisé de périmètre différent a été trouvé (Cour des comptes, NEB 2015).
- Pas de chiffrage trouvé pour le plafonnement de l'ISF revoté en 2014, les plus-values de terrains sans abattement (2014) et le forfait social différencié (2014).
- Restitutions de Ruyter (non-résidents) non trouvées. Le réalisé de `ps_nonresidents_2012` est donc brut.
- Pistes ouvertes faute de temps : taxe sur les imprimés (2003), extension de l'exonération de la contribution de 3 % (LFR 2016), plafonnement global des niches (2009). Pour les boissons sucrées (2012), ex ante et réalisé ne sont pas établis.
- Décisions DC introuvables : LFI 2007 à 2009, LFSS 2021 et une partie des LFR 2010-2011. Pour la LFI 2011 et la LFI 2025, le caractère procédural des censures a été déduit de la structure de la décision, sans vérification article par article.
- QPC : 79 commentaires fiscaux ont été repérés, mais peu ont été suivis jusqu'au bout. Les arrêts de la CJUE Steria, Sofina, Jahin, Dreyer et Accor n'ont pas été lus. Accor est la seule réserve sur le classement hors champ de la contribution de 3 %.
- Aucun arrêt de la CEDH sur un prélèvement français n'a été trouvé dans les sources lues.
- Sites inaccessibles : conseil-constitutionnel.fr (coupures, contournées par web.archive.org et le dépôt des commentaires), Légifrance (403), EUR-Lex et curia (pages vides), actu-juridique.fr.

**Prestations** (`parts/notes_prestations.md`) :

- Le recensement des QPC n'est pas exhaustif : la base du Conseil constitutionnel n'a pas pu être interrogée par matière.
- Exclus faute de réalisé ou de chiffrage avant adoption :
  - décret SJR de 2021 : ex ante Unédic de 1 Md€ en croisière, réalisé monétaire non trouvé. C'est le meilleur candidat à compléter ;
  - ASPA à 10 ans de titre de séjour (2012) : ex ante seulement dans la presse ;
  - RSA à 5 ans (2008) : pas de chiffrage propre ;
  - art. 19 de la loi immigration de 2023 : pas de chiffrage ;
  - loi rapatriés de 2005 : réalisé non trouvé ;
  - LFI 2002, art. 131 et 132 : pas de chiffrage ;
  - bouclier électricité 2023 : seul ex ante disponible postérieur au vote ;
  - gel des TRV du gaz en 2022 : périmètre changé en cours d'année.
- Aucune décision de censure sur le fond n'a été trouvée pour un contrôle des prix hors énergie ayant un coût budgétaire.
- Non lus : 90-285 DC et 2000-435 DC (lues à travers un commentaire), 2017-690, 2016-534 et 2014-433 QPC, et la partie du rapport du Sénat n° 214 (2016-2017) au-delà de ses 15 premières pages. HUDOC n'a pas été atteint.

**Programmes** (`parts/notes_programmes.md`) :

- Pour la plupart des lignes en « aucun », aucune recherche web propre n'a été faite.
- Décisions vues de seconde main et non utilisées : CE n° 375887 (2015), CJUE du 19/12/2024 sur les prestations familiales, 2022-842 DC, 86-217 DC, CE sur les blocages de prix de 2020.
- Le programme NFP n'a pas été relu dans son texte d'origine (il est cité d'après Montaigne).
- Martinez Silva et C-479/13 sont lus dans les communiqués de presse de la CJUE ; Koua Poirrez dans une copie universitaire.

## 5. Décisions laissées à l'intégrateur

Décisions prévues par la consigne (§ 5) :

1. **Une seule règle par ligne.** `nfp_taxe_kilometrique` est dans le champ (J1) et déjà en « Nouvelle assiette : risque juridique ». Il faut choisir l'une des deux règles.
2. **Règle des familles nouvelles** que proposera l'agent d'attribution.
3. **`ps_nonresidents_2012` et `taxe_dividendes_3pct_2012`**, tous deux aujourd'hui dans le test de « Nouvelle assiette ».
   - Le collecteur fiscalité juge `ps_nonresidents_2012` **dans le champ**. La consigne le présumait hors champ ; il s'appuie sur l'arrêt de la CJCE du 15/02/2000 (C-169/98 et C-34/98, CSG et CRDS des affiliés à un autre régime de l'Union), cité par le rapporteur général au moment du vote. Différence : l'arrêt de 2000 visait des revenus d'activité, la mesure de 2012 vise des revenus du capital. Son réalisé est brut des restitutions.
   - `taxe_dividendes_3pct_2012` est jugée **hors champ** : toutes les décisions de même nature sont postérieures au vote ; seul l'arrêt Accor (2011) n'a pas été lu.
   - Il faut décider si ces deux mesures restent dans le test de « Nouvelle assiette », passent dans celui de la nouvelle règle, ou figurent dans les deux. Il faut aussi arbitrer les écarts de doublon de `ps_nonresidents_2012` (`inclus_stats` 0 contre 1, `ex_post_bas`, `cause_principale`, `selection`, `drapeaux`).

Points de méthode relevés par les collecteurs, signalés sans correction :

4. **Échantillon dominé par des censures.** 10 cas sur 12 sont censurés en tout ou en partie. Le champ n'a trouvé presque aucune mesure appliquée de même nature avec un réalisé : seulement `exit_tax_2011` et `bouclier_gaz_2023`, ce dernier en `inclus_stats = 0`. Les mesures appliquées repérées (taxe sur les hautes rémunérations, composante carbone 2014, SJR 2021) n'ont pas de réalisé sur le même périmètre. La consigne (§ 2 A) avertit qu'un échantillon de censures pousse le facteur vers 0 sans rien mesurer.
5. **Prestations dont le réalisé précède la censure.** Pour les quatre cas de prestations censurés (deux décristallisations, harkis, mineurs grévistes), le réalisé est mesuré avant la censure, et la censure a ensuite **augmenté** la dépense. Leur rapport (0,72 ; 0,79 ; 1,27 ; 0,85) mesure l'erreur de chiffrage de petites dépenses de reconnaissance, pas l'effet de l'issue juridique. Ce sont aussi de très petits montants, de 0,0006 à 0,123 Md€.
6. **Cas non indépendants.**
   - Les deux décristallisations (`decristallisation_lfr2002`, `decristallisation_lfi2007`) ont la même décision antérieure (CE Diop, 2001) et la même censure (2010-1 QPC).
   - Les deux taxes sur les boissons énergisantes (2013, 2014) visent la même mesure, recréée après sa censure. La décision postérieure de la première est la décision antérieure de la seconde.
   - Si la médiane les compte comme quatre cas, deux mécanismes pèsent double.
7. **Rattachements « même nature » fragiles.**
   - `taxe_75pct_2013` et `cotisations_salariales_degressives_2015` sont rattachées à 2000-437 DC (CSG dégressive). Pour la seconde, le collecteur la dit « à confirmer » : mécanisme proche, motif différent.
   - `boissons_energisantes_2013` et `taxe_carbone_2010` sont rattachées aux taxes environnementales de 2000 et 2002.
   - `mineurs_greves_1948_lfi2015` est rattaché à 90-285 DC : lien faible, confiance `low`.
   - `decristallisation_lfr2002` : le critère de nationalité est remplacé par celui du pays de résidence ; s'agit-il du même mécanisme que dans Diop ?
   - `harkis_allocation_reconnaissance_2003` : l'art. 67 lui-même a été déclaré conforme.

   L'attribution à l'aveugle peut sortir certains de ces cas du champ. Le facteur est calculé sur les seuls cas qu'elle retient (§ 4).
8. **`nfp_asile`** (en « aucun »). Le coût de 1,3 Md€ est calculé sur l'art. 19 de la loi de 2024. Cet article a été censuré le 25/01/2024 (2023-863 DC, procédure), et son contenu jugé contraire au fond le 11/04/2024 (2024-6 RIP), donc avant juin 2024. La disposition dont l'abrogation est chiffrée n'était pas en vigueur. C'est une question de **référence** (le montant pourrait être nul), pas de risque juridique : elle relève de `statut_reference`, hors de cette règle.
9. **`nfp_taxe_kilometrique`** est en J1 et déjà en « Nouvelle assiette » (voir le point 1).
10. **Les deux volets de `rn24_preference_nationale`.** La part familiale (3,8 Md€) est nettement dans le champ : 89-269 DC, Koua Poirrez et Martinez Silva pour la nationalité, 2024-6 RIP pour la durée de résidence. La part RSA (2,6 Md€) l'est moins : 2011-137 QPC a **validé** la condition de 5 ans de titre de séjour pour le RSA, et va donc en sens contraire. La ligne est aussi en J2. Il faut décider si la règle s'applique aux 6,4 Md€ ou à la seule part familiale. Une décision postérieure (2026-901 DC, APL des étudiants étrangers, conforme avec réserve) est notée sans changer le critère.

Autres points relevés pendant la fusion :

11. **Lignes de confiance `low`** : `nfp_blocage_prix` et `l_gel` reposent sur 2019-774 QPC, qui valide aussi l'encadrement des marges limité aux produits de première nécessité ; `nfp_ir` ne vise que la part CSG d'un montant porté surtout par l'IR. Pour `nfp_ir`, il faut décider si la règle s'applique à toute la ligne ou à une part.
12. **Asymétrie à surveiller** : `rn24_asile` est en J1, mais `ens_retention`, que Montaigne chiffre avec une méthode proche, est en « aucun ». Le collecteur fonde la différence sur le mécanisme juridique : obligation nationale de dépôt à l'étranger d'un côté, dispositif de droit de l'Union de l'autre. À comparer avec l'attribution à l'aveugle.
13. **Hors champ « de fond » proches de la procédure.** Plusieurs lignes de `hors_champ.csv` ont été censurées pour incompétence négative, intelligibilité de la loi, légalité des délits ou séparation des pouvoirs (par exemple `mere_fille_al5_2015`, `transfert_fonctions_2014`, `cotisation_fnal_taux_decret_2015`, `plafonnement_global_niches_2006`). Ce ne sont pas des censures de procédure au sens du § 1, mais elles disent peu de chose de la mesure elle-même. Il faut décider si elles comptent dans les 27 censures « que le champ ne voit pas ».
14. **Type des lignes de panier dans le dossier aveugle** : il est déduit du signe du montant (voir « Dossier aveugle »).

## 6. Décision de l'intégrateur (20/10/2026, validée par l'utilisateur)

1. Aucun facteur n'est appliqué : la règle dégrade son propre échantillon (§ 2), le test n'est pas aveugle (11 issues connues sur 12) et les cas mélangent censures avant application et erreurs de chiffrage. Les montants ne changent pas.
2. Le risque est affiché, pour information, sur la fiche des 7 lignes où la collecte et l'attribution concordent : `rn24_preference_nationale`, `rn24_asile`, `rn24_tva_carburants`, `nfp_blocage_prix`, `l_gel`, `nfp_taxe_kilometrique`, `nfp_ir` (part CSG). Les quatre lignes ajoutées par la seule attribution (`rn24_ir_jeunes`, `rn24_medecins`, `nfp_flat`, `l_pfu`) ne le sont pas : rapprochements faibles, ou part infime de la ligne (exit tax ≤ 0,067 sur 3,2). `garde_fous.py` vérifie qu'une même mesure a le même critère dans un programme et dans un panier.
3. Limite écrite sur la page « Méthode ».
4. La règle « Nouvelle assiette : risque juridique » devient « Nouvelle assiette » : ses cas mesurent le rendement d'une assiette nouvelle, pas un risque juridique. Facteur et test inchangés ; `ps_nonresidents_2012` et `taxe_dividendes_3pct_2012` y restent.
5. `nfp_asile` (coût fondé sur un article censuré avant juin 2024) : question de référence, traitée dans une issue à part.
