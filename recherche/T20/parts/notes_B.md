# T20, groupe B : ce que consomment les foyers (notes de collecte)

Date d'accès de toutes les sources : 2026-10-20. Sources archivées dans `sources/T20/B/` (40 fichiers, sha256 dans `sources_B.csv`). Valeurs recopiées dans `consommation_B.csv` (5 755 lignes, environ 2,9 Mo). Rien n'y est interpolé vers la grille.

## 1. Quelle est la dernière édition de Budget de famille ?

- **La dernière édition publiée est celle de 2017** (collecte 2016-2017, résultats parus le 15/09/2020). Le communiqué Insee du 02/01/2026 : « Le 2 janvier 2026, l'Insee lance la nouvelle édition de l'enquête Budget de famille » et « La précédente enquête sur ce thème a eu lieu en 2016-2017 » (`insee_bdf_lancement_2026.html`). La fiche source (`insee_bdf_source_s1194.html`, page datée 20/10/2026) liste les millésimes 2006, 2011, 2017 et 2026. L'édition 2026 est en cours de collecte : elle n'a donc aucun résultat.
- Données plus récentes, mais de comptabilité nationale (comptes nationaux distribués, CND) : 2022 (Insee Focus 338 et Insee Première 2022, novembre 2024) et 2023 (Insee Analyses 118 et 119, 2026). Les tableaux détaillés des CND sur 2023 « seront publiés en novembre 2026 » (`insee_cnd_8988803.html`). Ils ne sont donc pas encore disponibles à la date d'accès.

## 2. Ce qui a été trouvé et recopié

| Bloc (préfixe `id`) | Source | Données | Découpage | Base de prix |
|---|---|---|---|---|
| `B_bdf17_TF106_*` | BdF 2017, TF106 | Dépense moyenne par ménage, 180 postes (COICOP jusqu'à 4 caractères, plus le total CTOTALE et le hors-champ 13) | Décile de niveau de vie D1 à D10, plus l'ensemble | € 2017 |
| `B_bdf17_TF107_*` | BdF 2017, TF107 | Mêmes postes | Statut d'occupation (propriétaires P, locataires L) × quintile | € 2017 |
| `B_bdf17_TF105_*` | BdF 2017, TF105 | Postes jusqu'à 3 caractères, plus énergie et loyers (0411, 0450-0453, 045A, 0722) | Type de ménage (seul, monoparental, couple sans ou avec enfants, autres) | € 2017 |
| `B_bdf17_TF102_*` | BdF 2017, TF102 | Idem | Âge de la personne de référence (7 tranches) | € 2017 |
| `B_ip1815_*`, `B_cor25_*` | Insee Première 1815 (CN base 2014, BdF 2017, ERFS 2017) | Taux d'épargne brut, consommation par ménage et par UC, structure en 12 postes ; consommation et RDB par UC selon l'âge | Quintile de RDB/UC ; âge de la personne de référence | € 2017 |
| `B_if338_*` | Insee Focus 338 (CND 2022) | Consommation par UC en 12 postes, RDN par UC, taux d'épargne nette | Cinquième de niveau de vie ; groupe de niveau de vie, configuration familiale, âge, CSP | € 2022 |
| `B_ia119_rdn_*` | Insee Analyses 119 (CND 2023) | RDN par UC | Décile | € 2023 |
| `B_ia118_*` | Insee Analyses 118 (CND 2023) | Prélèvements sur la production et la consommation (€/UC, par décile) ; taxes sur les produits et RDN (Md€, par vingtième) | Décile, vingtième | € 2023 |
| `B_cpo15_*` | CPO 2015, rapport particulier (Ines, BdF 2011, législation 2014) | Tableau 4 : écart au taux normal dû à l'exonération et à chaque taux réduit, et taux apparent par décile ; taux d'effort D1 et D10 ; épargne par quintile et par âge ; part des loyers ; répartition des recettes par taux | Décile, quintile, âge | sans objet (parts) |
| `B_es522_*` | André et Biotteau, Economie et Statistique 522-523 (Ines 2016) | Part de la consommation TTC et de la TVA par taux : normal 52,2 %, intermédiaire 13,3 %, réduit 15,4 %, 2,1 % 0,6 %, exonéré 18,5 % | Ensemble seulement | € 2016 |
| `B_cpo23n_*`, `B_cpo23r_*` | CPO, note n° 6 (2023) et rapport TVA (2023) | Gains des taux réduits (712 € pour D1, 2 089 € pour D10) ; écarts de part de consommation aux taux de 5,5 % et 10 % ; part consommée du revenu ; part de l'énergie D1 et D10 | Décile ou groupes de déciles | € 2017 (probable, non dit) |
| `B_sdes26_*` | SDES, Chiffres clés de l'énergie 2026 (données 2024) | Dépense moyenne par ménage en énergie du logement (2 071 €) et en carburants (1 673 €), avec la part des taxes énergétiques, de la TVA et le hors taxes ; totaux en Md€ ; part de l'énergie dans le budget (9,3 %) | Ménage moyen seulement | € 2024 |

### Remarques sur le contenu

- **Énergie dans BdF 2017** : les postes 0451 (électricité), 0452 (gaz), 0453 (fioul), 045A (combustibles solides) et 0450 (factures électricité et gaz non séparables, 111 € pour D1 et 394 € pour D10) sont des montants TTC. Le poste 0722 couvre les carburants, l'électricité des véhicules et les lubrifiants. À partir de TF106 : (045 + 0722) / CTOTALE ≈ 9,9 % pour D1 (967 + 622 sur 16 123) et 6,8 % pour D10 (1 925 + 1 375 sur 48 353). Ce calcul est le mien, il ne vient pas d'une source publiée. Il diffère des 12,7 % et 9,5 % que cite le rapport CPO 2023 sans en donner la source (ligne `B_cpo23r_*`, confiance `medium`).
- **Tableau 4 du CPO 2015** : la note du tableau dit que l'écart dû à un taux réduit vaut part de consommation × (20 % − taux). On peut donc en déduire les parts de consommation par taux et par décile. Exemple pour D1 : exonéré 2,9 / 20 ≈ 14,5 % ; 5,5 % : 3,0 / 14,5 ≈ 20,7 % ; 10 % : 1,4 / 10 = 14 % (consommation hors loyers, BdF 2011). Le calcul est laissé à l'intégrateur et ces parts ne sont pas écrites dans le CSV.
- Les tableaux TF202, TF205, TF206 et TF207 (coefficients budgétaires) sont archivés mais pas recopiés : ils se déduisent des tableaux de montants.

## 3. Non trouvé (avec les endroits cherchés)

1. **Part de la dépense par taux de TVA, par décile, sur une enquête récente** : non trouvé. Seul le tableau 4 du CPO 2015 (BdF 2011, législation 2014) la donne indirectement. La note CPO 2023 (BdF 2017) n'a que des graphiques 2 et 3 dont les valeurs ne sont pas lisibles dans le PDF, et trois chiffres dans le texte. Cherché dans la note et le rapport CPO 2023, ES 522-523 (agrégat seul) et WebSearch (IPP, Insee Ines).
2. **Correspondance entre les postes BdF et les taux de TVA** (l'annexe 5 citée par le CPO 2015) : non trouvée dans le PDF du rapport particulier. Le module « taxes indirectes » d'Ines n'est pas publié sous forme de table. L'intégrateur devra construire cette correspondance en citant le CGI : ce n'est pas une donnée publiée.
3. **Charge de TVA et d'accises en part du revenu par décile, sur données récentes** : pas de série publiée sur la seule TVA et les seules accises. Les seules valeurs lisibles sont celles du CPO 2015 (D1 12,5 %, D10 4,7 %). Pour contrôle, les CND 2023 donnent « taxes sur les produits (TVA, TICPE, accises, DMTO, etc.) » par vingtième (`B_ia118_taxprod_*`) et le RDN : la notion est plus large (DMTO, taxes sur l'investissement des ménages).
4. **Volumes d'énergie (kWh, litres) par décile ou par type de ménage** : non trouvés. Cherché dans le Théma SDES « Les ménages et la consommation d'énergie » (2017, Phébus 2013 : taux d'équipement automobile et taux d'effort seulement, pas de kWh par décile), les Chiffres clés de l'énergie 2024 et 2026 (moyennes nationales en euros) et WebSearch. Il ne reste que les montants TTC (BdF 2017 par décile ; SDES 2024 pour le ménage moyen). Pour appliquer une accise, il faudra diviser par un prix unitaire, qui n'a pas été collecté.
5. **Dépense par niveau de vie croisée avec la composition et l'âge** (la grille) : aucun tableau croisé publié. BdF 2017 ne croise que le statut d'occupation et le quintile (TF107).
6. **Accises détaillées** (TICPE, TICFE, accise sur le gaz, tabac, alcool) **par décile** : non trouvées. Le SDES 2024 donne le total « taxes énergétiques » du ménage moyen. Pour le tabac et l'alcool, il ne reste que les montants TTC de BdF (021, 022).
7. **Taux d'épargne par décile (et non par quintile)** sur données récentes : non trouvé. Les CND 2022 sont par cinquième. Les CND 2023 (IA 118 et 119) donnent le revenu par décile mais pas la consommation.
8. **Publications IPP (TAXIPP)** sur l'incidence de la fiscalité indirecte : les seules repérées datent de 2012 (rapport « Fiscalité et redistribution », mémoire Dauvergne). Elles n'ont pas été lues ni recopiées, car elles sont plus anciennes que le CPO 2015.

## 4. Points de vigilance pour l'intégrateur

- **Les concepts ne sont pas comparables entre sources.** BdF compte la dépense par ménage, TTC, sans loyers imputés (loyers nets des aides au logement). Les CND comptent par unité de consommation (UC), loyers imputés compris, champ S14 (tous ménages), avec un recalage sur les comptes nationaux. L'IP 1815 donne un taux d'épargne brut par quintile de RDB/UC ; le Focus 338, un taux d'épargne nette par cinquième de niveau de vie. La présentation de l'Insee au COR en 2025 (`cor_2026-02_insee_conso_epargne.pdf`) dit explicitement que ces séries sont « non directement comparables ».
- **Le taux d'épargne des plus modestes dépend de la source** : −29 % pour C1 en 2022 (CND, épargne nette), +2,7 % pour Q1 en 2017 (IP 1815, brut, après le redressement de la consommation « au-delà de 1,2 fois le revenu »), −23,6 % pour Q1 en 2011 (BdF via Ines). Pour Q5, le CPO 2015 donne 40,2 % dans son texte et 42,0 % dans son graphique 9.
- **Retraités de 71 ans dans la grille** : les tranches publiées sont 65-74 ans (BdF TF102), 70 ans ou plus (IP 1815) et 65 ans ou plus (CND). Le CND 2023 classe par âge moyen des adultes, et non par âge de la personne de référence.
- **La grille est « sans loyer »**. TF107 (propriétaires par quintile) est donc le tableau BdF le plus proche. Le poste 041 des propriétaires n'est pas nul (83 € en moyenne : loyers d'autres résidences, par exemple).
- **Base de prix** : BdF est en € 2017, le Focus 338 en € 2022, les CND 2023 en € 2023, le SDES en € 2024. Les indices de prix pour ramener ces montants à 2026 n'ont pas été collectés (hors périmètre du groupe B).
- **Structure des taux** : BdF 2017 reflète les dépenses de 2017. Les changements de taux depuis (par exemple les abonnements d'électricité et de gaz, cités dans la consigne T20) jouent sur les taux à appliquer, pas sur les montants dépensés. Le groupe C doit vérifier ces changements sur source.
- **CND, taxes sur les produits** : la ligne inclut des taxes que les ménages ne paient pas au moment de consommer (DMTO, TVA sur le logement neuf). Elle sert de borne haute de contrôle, pas de cible.

## 5. Ce qui manque pour passer à la grille

1. Une table de correspondance entre les postes BdF et les taux de TVA 2026, à construire depuis le CGI. Ce n'est pas une donnée publiée (voir § 3.2).
2. Une convention pour situer chaque foyer de la grille sur un décile de niveau de vie BdF 2017 : seuils de déciles de 2017, niveau de vie OpenFisca en € 2026 déflaté. Les seuils des déciles BdF 2017 n'ont pas été trouvés dans les fichiers téléchargés (`cad01_fe.xlsx` ne donne que des effectifs).
3. Une convention pour combiner l'effet du niveau de vie (TF106 ou TF107) avec celui de la composition (TF105) et de l'âge (TF102), qui ne sont publiés que séparément.
4. Des prix unitaires (€/kWh, €/litre) pour convertir les montants TTC d'énergie en volumes.
5. Des indices de prix entre 2017 et 2026 par poste.

## 6. Sites et tentatives

- `www.statistiques.developpement-durable.gouv.fr/edition-numerique/...` : contenu chargé en JavaScript. Le lien « pdf/Chiffres-cles-energie-2026.pdf » renvoie une page HTML. Contournement : les fichiers `media/9748` (xlsx) et `media/9771` (infographie) de la page de l'édition 2026.
- `ecologie.gouv.fr/.../Théma - Les ménages et la consommation d'énergie.pdf` : erreur 404. Contournement : `media/358` sur le site du SDES.
- `ecologie.gouv.fr/.../statistiques_sdes_essentiel_08_precarite_energetique_2024_sept 2026.pdf` : PDF vide (0 page), non exploitable, supprimé.
- `insee.fr/.../version-html/8973957/ia119.pdf` : PDF vide (0 page). Contournement : `ia119.xlsx`.
- Fichiers téléchargés puis supprimés parce qu'ils n'ont pas été lus : Insee Analyses 43, Insee Analyses 88 (et ses xlsx), Revenus et patrimoine 2021 dossier 2.
- senat.fr : non sollicité.
- Le quota de recherche n'a pas été épuisé.
