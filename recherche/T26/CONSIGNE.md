# T26 : recoupements avec la référence et bases fragiles encore ouverts

Consigne préparée le 01/11/2026. Elle couvre les points du « groupe 1 » du croisement des décisions non tranchées : ceux qui peuvent changer un chiffre publié. Ne sont retenus ici que les points qui demandent une source nouvelle ; les autres sont analysés par l'intégrateur (`rapport_integrateur.md`).

Lire d'abord `recherche/CONSIGNES.md` (règles communes ; date d'accès : celle du jour), `CONTRIBUTING.md` (règle 4, pas de double compte avec la référence), `recherche/T1/convention_application_2024.md` (référence des programmes 2024 : droit de juin 2024 et programme de stabilité d'avril 2024) et `recherche/audit/rapport.md` (§ 1.5).

## Pourquoi

Une mesure déjà votée ou déjà inscrite dans la référence n'est comptée que pour la part qui n'y est pas (`statut_reference`, `facteur_reference`). Pour plusieurs lignes, cette part a été fixée au milieu d'un intervalle ou à 1 « par défaut, à arbitrer », faute de source. D'autres lignes reposent sur un montant dont la méthode n'est pas connue. Le résultat peut être favorable ou défavorable à n'importe quel parti : il est publié pareil.

## 0. Gel

| Élément | Valeur |
|---|---|
| Commit | `a323509` (plus les corrections de notes du 01/11/2026, sans effet sur les montants) |
| `data/raw/paniers.csv` (sha256) | `4ad446d724509b058d749d44cbbfd5959687f6b0a5b3d16eadb0dc9b77f3b01c` (avant la correction de la note de `l_bandeaux`) |
| `data/raw/application_lignes.csv` (sha256) | `2b57739de812586ca97625dedab7cd60c318a7322a533587ae039e759849679b` |

## 1. Critère (fixé avant la recherche)

Pour une ligne des paniers 2027, la référence est « loi votée + PLF/PLFSS 2027 déposés ». Pour une ligne des programmes 2024, c'est le droit au 30/06/2024 et le programme de stabilité d'avril 2024.

- **Recoupement chiffré** : facteur = (montant de la ligne − montant déjà dans la référence) / montant de la ligne, les deux sur le même champ et la même année.
- **Recoupement identifié mais non chiffré** : le dire, avec l'intervalle [borne basse documentée ; 1].
- **Variante « loi votée seule »** : pour chaque recoupement, dire quelle part vient d'un texte voté et quelle part d'un projet (PLF/PLFSS 2027).

Hors champ : l'opportunité des mesures ; leur risque juridique (T23) ; les règles de comportement.

## 2. Ce que l'on cherche

### A. Paniers 2027 (agent A)

1. **`l_bandeaux`** (suppression des bandeaux maladie et famille, extinction des allègements à 1,88 SMIC ; 11,4 Md€ après effets emploi, 12,1 en statique ; facteur de référence 0,5 dans [0,09 ; 0,87]). Lire la `note_reference` de la ligne. Chercher la **répartition par niveau de salaire** des baisses d'allègements de la référence : LFSS 2025 (reprofilage), LFSS 2026 art. 40 (réduction générale dégressive unique), décret n° 2026-509 (gel), PLFSS 2027 art. 7 (assiette). Sources possibles : évaluations préalables et annexe 9 des PLFSS, rapports des commissions des affaires sociales, HCFP, Insee, DARES, rapport Bozio-Wasmer. L'important est la part de ces baisses qui porte au-dessus de 1,6 SMIC (zone des bandeaux), et ce qui en est voté.
2. **`e_carence`** (7 jours de carence, 0,95 Md€ ; facteur 0,5 entre 0 et 1). L'ONDAM 2027 intègre 1,0 Md€ d'économies sur les indemnités journalières, instrument non précisé. Chercher l'instrument : articles du PLFSS 2027, annexe 9, rapport des commissions, amendements adoptés, accord ou négociation des partenaires sociaux annoncés, et leur état à la date du jour.
3. **`e_oper`** (fusion ou suppression d'opérateurs de l'État, 1 Md€ ; facteur 1 « non chiffrable »). Chercher dans le PLF 2027 (exposé général, jaune « Opérateurs de l'État », évaluations préalables) les économies **chiffrées** sur les opérateurs par fusion ou suppression, et les distinguer des baisses de taxes affectées (France compétences) ou d'emplois.
4. **`l_brunes`** (suppression des niches défavorables à l'environnement, 6 Md€ : « environ 6 Md€ dans le PLF 2025 », Institut Avant-garde, `sources/T26/avantgarde_budget_vert_plf2025.pdf`, p. 2-3). Identifier les dépenses fiscales qui forment ces 6 Md€ (rapport sur l'impact environnemental du budget, « budget vert », annexé au PLF 2025), puis leur coût **2027** dans le PLF 2027 (Voies et moyens, tome II, ou budget vert 2027). Le recoupement est la baisse de coût déjà votée entre l'année du chiffrage et 2027 (par exemple la trajectoire du GNR hors agriculture, dépense fiscale 800201 : 0,713 Md€ en 2024, 0,466 au PLF 2026 ; extinction du Pinel).

### B. Programmes 2024 (agent B)

1. **`rn24_asile`** (+1,2 Md€, Montaigne 2024 ; la fiche Montaigne 2022 donnait 1,6, de 1 à 2,5 : `sources/T22/RN/montaigne_mlp2022_asile_wb20260821171655.html`). Chercher pourquoi le montant passe à 1,2 (PDF ou page Montaigne 2024, `sources/T17/`), et si une part de l'économie était déjà dans le droit ou la trajectoire de juin 2024 : pacte européen sur la migration et l'asile (règlements adoptés en mai 2024 ; date d'application), loi n° 2024-42.
2. **`ens_leasing`** (−1,3 Md€ ; part comprise 0, T25). La 2e édition du leasing social (septembre 2025) a été financée par les certificats d'économies d'énergie. Chercher comment la comptabilité nationale (Insee, Eurostat) classe les CEE : dépense et prélèvement publics, ou hors administrations publiques. Cela ne change pas la lecture au 30/06/2024 ; dire seulement si une mesure financée par CEE peut être comptée comme dépense publique.
3. **`nfp_niches`** (5 Md€, iFRAP ; `data/raw/application_lignes.csv`) et les **exemptions d'assiette** des cotisations (lignes NFP de « Autres recettes » découpées en T22). Lire ce que chaque chiffreur met dans chaque ligne (`sources/T6/`, `sources/T17/ifrap_*`, `recherche/T22/`) et dire si un même dispositif est compté deux fois. Les montants que tu lis doivent venir de la source archivée.

## 3. Livrables

Dans `recherche/T26/` : `parts/notes_A.md` ou `parts/notes_B.md`, `parts/lignes_A.csv` ou `parts/lignes_B.csv` (colonnes `id,constat,montant_reference,champ,annee,vote_ou_projet,facteur_propose,facteur_bas,facteur_haut,url,citation,page,confiance,note`) et `parts/sources_A.csv` ou `parts/sources_B.csv`. Ne rien modifier hors de `recherche/T26/` et `sources/T26/`. Ne pas toucher `rapport_integrateur.md` ni `rapport.md`.
