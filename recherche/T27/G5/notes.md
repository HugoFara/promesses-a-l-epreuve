# T27, groupe 5 : notes périmées (01/11/2026)

Corrections préparées, **non appliquées**. Les corrections de `data/raw/` gérées par `scripts/appliquer_corrections.py` sont dans `corrections_notes.csv` (20 lignes). Ce fichier décrit le reste.

Essai sur une copie du dépôt : 20 corrections appliquées, 0 refusée ; `build.py` OK ; `garde_fous.py` : 0 erreur, 0 alerte ; `check_regression.py` OK. Les sorties chiffrées ne changent pas : seuls des textes changent, et la confiance de deux lignes NFP. Pages du site non vérifiées à l'écran.

## Contenu de `corrections_notes.csv`

| Point | Lignes | Fichier, colonne |
|---|---|---|
| G5.1 | 1 | `application_lignes` `rn24_preference_nationale`, `justification` |
| G5.3 | 2 | `paniers` `e_oper`, `note_reference` ; registre `e_oper_e`, `note` (même texte « à arbitrer ») |
| G5.4 | 4 | registre `l_ret62_a`, `l_smic_i`, `l_isf_i`, `rn24_production`, `note` |
| G5.5 | 5 | `mesures_cout` : `note_confiance` de `indemnite_carburant_2023` et `ticfe_prolongation_2023` ; `note` de `isf_reforme_2013`, `stdr_2014`, `us_rachats_1pct_fy2024` |
| G5.8 | 6 | `idees` `annee_blanche`, `desindexation_pensions` (`resume`) ; `paniers` `e_pens`, `e_carence` (`note_reference`) ; registre `e_pens_e`, `e_carence_e` (`note`) |
| G5.9 | 2 | `application_lignes` `nfp_point_indice`, `nfp_indexation_salaires`, `justification` ; confiance high → medium, avec `note_confiance` |

## G5.2

Vérifié : la justification de `rn24_part_fiscale` ne contient plus « Règle discutable » (réécrite en G2.1, famille `impot_revenu_large`). Rien à faire.

## G5.4 : `raison_ecart` de `rn24_production`

Pas ajoutée : `garde_fous.py` ne l'exige pas. La ligne est dans `application_lignes` (jugée par rapport au droit de juin 2024, l'alerte « absente avec montant » ne s'y applique pas), elle n'a pas de `mesure_panier`, et `montant_reference_2027` est vide. Son statut (« absente », facteur 1) est le même que dans `note_reference` : il n'y a pas d'écart à expliquer. Seule la note est réécrite.

## G5.6 : `calibration_instituts.csv` (hors du script, pas de colonne `id`)

Colonne `inclus_stats`, 32 lignes (numéros de ligne du fichier, en-tête = ligne 1). Remplacer, dans chaque ligne :

`non (T21 : test de la médiane des chiffrages, pas encore calculé ; X)` → `non (T21 : test de la médiane des chiffrages non jugeable ; X)`

où X est le motif propre à la ligne, inchangé :

| Ligne | Campagne | Mesure | Chiffreur | X (inchangé) |
|---|---|---|---|---|
| 45 | 2012 | Tranche d'IR à 45 % au-delà de 150 000 € par part | Candidat (PS) | oui |
| 46 | 2012 | Tranche d'IR à 45 % au-delà de 150 000 € par part | Institut Montaigne | oui |
| 47 | 2012 | Tranche d'IR à 45 % au-delà de 150 000 € par part | Terra Nova | oui |
| 48 | 2012 | Abaissement du plafond du quotient familial de 2 336 à 2 000 € par demi-part | Institut Montaigne | oui |
| 49 | 2012 | Retour sur les allègements d'ISF de 2011 | Candidat (PS) | non (périmètre différent ; réalisé calculé) |
| 50 | 2012 | Retour sur les allègements d'ISF de 2011 | Institut Montaigne | non (périmètre différent ; réalisé calculé) |
| 51 | 2012 | Retour sur les allègements d'ISF de 2011 | Terra Nova | non (périmètre différent ; réalisé calculé) |
| 52 | 2012 | Imposer les revenus du capital comme ceux du travail | Candidat (PS) | non (périmètre différent) |
| 53 | 2012 | Imposer les revenus du capital comme ceux du travail | Institut Montaigne | non (périmètre différent) |
| 54 | 2012 | Imposer les revenus du capital comme ceux du travail | Terra Nova | non (périmètre différent) |
| 55 | 2012 | Fin de la défiscalisation et des exonérations sociales des heures supplémentaires, sauf TPE | Candidat (PS) | non (réalisé non trouvé) |
| 56 | 2012 | Fin de la défiscalisation et des exonérations sociales des heures supplémentaires, sauf TPE | Institut Montaigne | non (réalisé non trouvé) |
| 57 | 2012 | Fin de la défiscalisation et des exonérations sociales des heures supplémentaires, sauf TPE | Terra Nova | non (réalisé non trouvé) |
| 58 | 2012 | Abattement en ligne directe ramené à 100 000 € par enfant | Candidat (PS) | non (réalisé non trouvé) |
| 59 | 2012 | Abattement en ligne directe ramené à 100 000 € par enfant | Institut Montaigne | non (réalisé non trouvé) |
| 60 | 2012 | Abattement en ligne directe ramené à 100 000 € par enfant | Terra Nova | non (réalisé non trouvé) |
| 61 | 2012 | Fin de la déductibilité des intérêts d'emprunt liés aux titres de participation | Candidat (PS) | non (périmètre différent ; réalisé = réestimation) |
| 62 | 2012 | Fin de la déductibilité des intérêts d'emprunt liés aux titres de participation | Institut Montaigne | non (périmètre différent ; réalisé = réestimation) |
| 63 | 2012 | Fin de la déductibilité des intérêts d'emprunt liés aux titres de participation | Terra Nova | non (périmètre différent ; réalisé = réestimation) |
| 64 | 2012 | Doublement de la taxe sur les transactions financières | Institut Montaigne | non (réalisé non isolé) |
| 65 | 2012 | Contrat de génération | Candidat (PS) | oui (horizon et dispositif différents : voir note) |
| 66 | 2012 | Contrat de génération | Institut Montaigne | oui (horizon et dispositif différents : voir note) |
| 67 | 2012 | Contrat de génération | Fondation iFRAP | oui (horizon et dispositif différents : voir note) |
| 68 | 2012 | 150 000 emplois d'avenir | Candidat (PS) | non (réalisé non trouvé) |
| 69 | 2012 | 150 000 emplois d'avenir | Institut Montaigne | non (réalisé non trouvé) |
| 70 | 2012 | 150 000 emplois d'avenir | Fondation iFRAP | non (réalisé non trouvé ; périmètre différent) |
| 71 | 2012 | Retraite à 60 ans pour les carrières longues | Candidat (PS) | non (réalisé non trouvé) |
| 72 | 2012 | Retraite à 60 ans pour les carrières longues | Institut Montaigne | non (réalisé non trouvé) |
| 73 | 2012 | Retraite à 60 ans pour les carrières longues | Fondation iFRAP | non (réalisé non trouvé) |
| 74 | 2007 | Heures supplémentaires : exonération de cotisations et d'impôt | Institut de l'entreprise | oui |
| 75 | 2007 | TVA de la restauration à 5,5 % | Institut de l'entreprise | non (réalisé = réestimation) |
| 76 | 2007 | Droits de succession : exonération pour 95 % des Français | Institut de l'entreprise | non (réalisé = réestimation) |

Le texte commence toujours par « non » : `validation.py` (qui teste `startswith("oui")`) garde ces lignes hors statistique. Source : `recherche/T21/rapport.md` § 8 (« hors statistique (test de la médiane non jugeable) ») et journal du 20/10/2026 (ligne 331 de `historique.csv`).

Ligne de journal à ajouter à la main dans `data/raw/historique.csv` (sur le modèle de la ligne 331) :

```
2026-11-01,calibration_instituts,*,inclus_stats,"non (T21 : test de la médiane des chiffrages, pas encore calculé ; …)","non (T21 : test de la médiane des chiffrages non jugeable ; …)","Texte aligné sur T21 § 8 : test de la médiane non jugeable, 32 chiffrages de 2007 et 2012 (T27 G5.6)",recherche/T21/rapport.md
```

## G5.8 : source et lignes laissées de côté

Source du rejet : dossier législatif de l'Assemblée (archive `sources/T26/A/AN_dossier_PLFSS2027.html`), relu : « Projet de loi de financement de la sécurité sociale rejeté par l'Assemblée nationale, pour 2027 le 23 octobre 2026, T.A. n° 358 ». La date du Sénat (09/11) vient d'une source secondaire (Deloitte Avocats, `recherche/T26/parts/notes_A.md`, l. 14) ; le `page` des corrections le dit.

Non modifié, à décider :

- `e_abat` (panier et registre `e_abat_e`) : la mesure est dans le **PLF** 2027 (art. 3), pas dans le PLFSS. Le rejet ne la concerne pas. Sa note dit déjà l'état (article supprimé en commission le 9/10/2026). D'après Deloitte (secondaire), le PLF est encore en première lecture à l'Assemblée.
- `idees` `etrangers_prestations` : même cas que les deux cartes traitées (mesure du PLFSS 2027, art. 37, « proposée pour 2027 »), mais hors de la liste demandée. Par symétrie, proposition : ajouter au `resume`, après la première phrase, « Elle est dans le projet de budget de la Sécurité sociale, rejeté en première lecture à l'Assemblée le 23/10/2026 (T.A. n° 358). Le Sénat l'examine à partir du 09/11/2026. »
- `idees_chiffres.csv` (pas de colonne `id`, hors du script) : libellés « Gels proposés pour 2027… » (`annee_blanche`, 2) et « Un an de résidence avant les aides au logement (proposé pour 2027) » (`etrangers_prestations`, 1). Exacts tels quels ; la carte porte maintenant l'état de la procédure.
- Registre, `l_bandeaux_i` : la note dit « gel 2027, proposée » et « assiette, proposée » (PLFSS 2027, art. 7), mais elle date de T1 (facteur 0,5, borne 0,09 à 0,87), alors que `facteur_suggere` vaut 0,55 et que T26 a remplacé le calcul (§ 6 de `recherche/T26/rapport_integrateur.md`). C'est une note périmée de plus, à réécrire en entier plutôt qu'à compléter.
- Registre, colonne `texte` de `nfp_indexation_pensions`, `nfp_asile`, `nfp_autres_dep` (« proposée, sens inverse ») : source citée, pas l'état de la procédure ; laissés.
- Incohérence à vérifier : le registre (`l_smic_i`, `texte`), `paniers` (`l_smic`, `source_reference`) et `application_lignes` (`nfp_smic`) disent « prolongation proposée par le PLFSS 2027 » pour le gel du SMIC de référence, mais la citation lue vient du **PLF** 2027, art. 49, exposé des motifs (`recherche/T26/parts/notes_A.md` l. 161 : « projet (PLF/PLFSS) »). La nouvelle note de `l_smic_i` cite le PLF, art. 49. Si le gel passe par le PLFSS, il est lui aussi touché par le rejet.

## G5.9

Les deux justifications suivent le modèle de `nfp_cotis_vieillesse` : montant gardé, fragilité dite, règle « Aucune » et facteur 1, donc le solde du NFP ne change pas. Chiffres lus : « un coût de 2Md€ par point » (micro-chiffrages NFP, p. 1) et « 2 x 1,75 % x 3 = 10,5 Md€ » (fiche Montaigne), repris de `recherche/T22/lignes_decoupees.csv`. Le passage de la confiance à medium ne change aucune sortie chiffrée (essai sur la copie). `rn24_heritage` (même point) : déjà fait hors de ce groupe.
