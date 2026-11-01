# T29 : programmes 2027 des partis à partir de leur dernier programme publié

Consigne du 01/11/2026. Décision de l'utilisateur (01/11/2026) : aucun parti n'a encore publié de programme pour 2027 ; on se sert de leur dernier programme, grands partis d'abord, dans l'ordre RN, LR, PS.

Lire d'abord `AGENTS.md`, `CONTRIBUTING.md`, `recherche/CONSIGNES.md`, `recherche/T1/convention_application_2024.md`, `recherche/T1/rapport.md`, les gabarits `modeles/programme_2027.csv`, `modeles/programme_2027_entete.csv`, `modeles/montee_en_charge_2027.csv`, et `scripts/garde_fous.py` (règles « FAMILLE », « PROFIL », « RÉFÉRENCE »).

## Règles communes (fixées avant la recherche, les mêmes pour chaque parti)

1. **Source.** Le dernier programme national chiffrable du parti, tel que publié. Pour chaque mesure, le montant d'un chiffreur indépendant (Institut Montaigne, iFRAP, Asterès…), comme pour les programmes 2024 ; à défaut, la mesure va dans une ligne « non chiffrée » (montant 0, dite dans la justification). Jamais de chiffrage fait par nous, sauf calcul mécanique sourcé et dit comme tel.
2. **Libellé du programme.** « <Parti> 2027 (programme <année>) », par exemple « RN 2027 (programme 2024) ». En-tête (`application_programmes.csv`) : scrutin « Présidentielle 2027 », `deficit_reference` = `prevision_2027_actuelle`, `biais_reference` = `biais_t1` ; `position_parti` dit que le programme est antérieur et qu'aucun programme 2027 n'est publié.
3. **Référence.** Loi votée + PLF/PLFSS 2027 déposés (comme les paniers). Pour chaque ligne : `statut_reference`, `facteur_reference` (et bornes si incertain), `source_reference`, `note_reference`. Une mesure déjà votée ou inscrite au budget 2027 ne compte que pour sa part restante. Si le registre `data/raw/statut_reference_2027.csv` a déjà la mesure (lignes `rn24_*`, `nfp_*`…), reprendre son statut et son facteur ; sinon, le chercher (textes de T1).
4. **Annulation de la référence.** Si le parti s'est engagé à annuler une économie inscrite dans la référence 2027 (sous-indexation des pensions, gels, abattement des retraités, jours fériés…), une ligne `annulation_economie_reference` au montant de l'économie (gabarit). Il faut une déclaration publique sourcée du parti (programme, proposition de loi, vote ou amendement à l'Assemblée en 2025-2026, déclaration d'un responsable national). Sans source, pas de ligne.
5. **Familles et règles.** Famille de `data/raw/familles.csv` et sa règle, comme pour tous les partis ; un écart s'explique dans `exception_symetrie`. Pour une mesure déjà présente dans un programme 2024, reprendre sa famille.
6. **Montée en charge.** Si la famille d'une ligne a un profil ailleurs (`montee_en_charge.csv`, ex. `retraites_age`), la ligne doit en avoir un (garde-fou PROFIL) : profil sourcé, ou celui de la ligne de même nature si le mécanisme est le même (dit dans la note).
7. **Horizon.** Le montant retenu est un montant annuel ; dire son horizon (colonne `horizon` de `chiffrages_instituts.csv`).

## Livrables du sous-agent (par parti, dans `recherche/T29/<parti>/`)

- `lignes.csv` : lignes au format de `modeles/programme_2027.csv`, ids `<parti>27_…` ;
- `entete.csv` : ligne au format de `modeles/programme_2027_entete.csv` ;
- `montee_en_charge.csv` si besoin ; `registre.csv` : lignes à ajouter à `statut_reference_2027.csv` (une par ligne du programme) ;
- `notes.md` (ce qui a été lu, décisions, lacunes) et `sources.csv` (sources archivées dans `sources/T29/<parti>/`, avec sha256).

Ne rien modifier dans `data/`, `scripts/` ni `web/`. L'intégrateur applique, lance `TEST_WEB_STRICT=1 bash scripts/run_all.sh`, vérifie à l'écran et commite.
