# T24 : lignes 2024 dont le montant porte sur une disposition absente du droit de juin 2024

Rapport d'intégration du 22/10/2026 (issue #9). Consigne : `CONSIGNE.md`. Détail : `parts/nfp_asile.md` (partie A, intégrateur) et `parts/notes_agent.md` (partie B, agent). Une ligne par ligne de programme dans `lignes_2024.csv` (89 lignes) ; sources dans `sources.csv` et `sources/T24/`.

## 1. Résultat

Sur 89 lignes, deux remplissent le critère :

| Ligne | Montant | Critère | Disposition | Confiance |
|---|---|---|---|---|
| `nfp_asile` | −1,3 | R1, censurée | Loi n° 2024-42, art. 19 (condition de 5 ans de résidence ou 30 mois d'activité pour les prestations), censuré par 2023-863 DC le 25/01/2024, jamais promulgué | high |
| `rn24_chomage` | −4,5 | R3, pas encore adoptée | Réforme de l'assurance chômage annoncée pour le 01/07/2024 : aucun décret au 30/06/2024 ; le décret n° 2024-648 du 30/06/2024 prolonge les règles de 2019 | medium |

Les 87 autres sont `aucun` : 59 mesures nouvelles, résidus ou charges d'intérêts (`sans objet`), 27 portant sur une disposition en vigueur, une (`ens_chomage`) qui chiffre l'adoption de la même réforme chômage.

## 2. `nfp_asile`

Le 1,3 Md€ de Montaigne (micro-chiffrages NFP, p. 5) est calculé en entier sur la condition de résidence de l'article 19. Cet article a été censuré avant promulgation (2023-863 DC, § 94-96 et dispositif) ; la version JORF de la loi ne porte que la mention de la censure. La même condition, proposée par référendum, a été jugée contraire à la Constitution sur le fond (2024-6 RIP, 11/04/2024). En juin 2024, abroger la loi ne change donc rien à l'accès des étrangers aux prestations familiales et aux APL.

La fiche mesure de Montaigne juge par ailleurs un chiffrage de l'abrogation « même approximatif » impossible ; l'iFRAP et Asterès laissent la mesure dans leur résidu. Les articles en vigueur des lois de 2018 et 2024 n'ont de chiffrage chez personne.

## 3. Réforme de l'assurance chômage de 2024 : trois lignes, deux traitements

Le constat dépasse `rn24_chomage` : la même réforme est traitée de deux façons selon le programme.

| Ligne | Promesse | Au site aujourd'hui | Lecture sous-jacente |
|---|---|---|---|
| `ens_chomage` | Conserver la réforme | +4,5 × 0 (règle « Déjà dans la référence ») = 0 | réforme dans la référence |
| `rn24_chomage` | Annuler la réforme | −4,5 | réforme dans la référence |
| NFP (dans `nfp_autres_dep_reste`) | « Abroger immédiatement […] les réformes de l'assurance-chômage » | 0 (Montaigne, micro-chiffrages p. 11) | réforme hors référence |

RN et NFP font la même promesse et ne sont pas comptés pareil : c'est un écart de symétrie, quelle que soit la lecture retenue.

Sources sur la place de la réforme dans la référence :

- **Droit au 30/06/2024** : pas de décret ; le décret n° 2024-648 (JO du 01/07/2024) prolonge les règles de 2019 jusqu'au 31/07/2024 (`sources/T24/agent/wb_decret_2024-648.html`).
- **Programme de stabilité d'avril 2024** (`sources/T24/agent/pstab_2024-2027.pdf`), encadré sur l'assurance chômage : économies de la réforme de la contracyclicité « estimées à 4,2 Md€ en régime de croisière », puis « De plus, une nouvelle réforme de l'assurance chômage a été annoncée afin de contribuer à l'atteinte du plein emploi à horizon 2027 », sans montant. Ailleurs, mention qualitative dans le scénario d'emploi (« réforme de l'assurance chômage annoncée pour 2024 »). Le texte ne dit pas si l'économie est dans la trajectoire chiffrée.
- **Montaigne**, chiffreur des trois montants : fiche Ensemble, « la réforme, qui n'est pas entrée en vigueur, n'est pas intégrée dans le tendanciel » (`sources/T20/integration/montaigne_ens_chomage.html`) ; micro-chiffrages NFP, p. 11 : « La réforme n'étant pas entrée en vigueur, nous avons fait le choix de ne chiffrer que les mesures déjà en application » ; synthèse RN : 0 Md€.
- **iFRAP** : la dit « déjà inscrite au budget », mais la compte en économie dans son tableau Ensemble (`recherche/T6/rapport.md`).
- **Non trouvé** : l'avis du HCFP sur le programme de stabilité 2024, qui aurait pu trancher.

Deux lectures possibles, à appliquer aux trois lignes :

- **A. Hors référence** (droit au 30/06/2024, Montaigne, programme de stabilité sans montant) : `ens_chomage` compte +4,5 (facteur 1) ; `rn24_chomage` compte 0 (`facteur_reference` 0, comme `nfp_asile`) ; NFP inchangé. Effet sur les soldes : Ensemble +4,5, RN +4,5, NFP 0.
- **B. Dans la référence** (lecture actuelle, iFRAP) : `ens_chomage` et `rn24_chomage` inchangés ; une ligne NFP « Abroger la réforme de l'assurance chômage » à −4,5 est découpée du résidu. Effet : NFP −4,5, les autres inchangés.

La convention de référence 2024 retient « le droit de juin 2024, celui des chiffreurs ». Les deux critères désignent la lecture A : décret non publié, chiffreur des trois montants qui la laisse hors de sa base. La lecture B repose sur une phrase de l'iFRAP que son propre tableau contredit.

## 4. Cas limites relevés (hors critère, à suivre à part)

- `rn24_rente_infra` (+3) : contribution en vigueur en 2024 (LFI 2024, art. 80) mais limitée au 31/12/2024 ; le programme de stabilité inscrit déjà « Mesures fiscales énergéticiens et autres mesures sur les rentes 3,0 » (tableau 7, p. 41). Si la mesure du RN recoupe cette annonce, double compte possible avec la référence.
- `rn24_prisons` : plan de 15 000 places déjà programmé ; texte de programmation non lu.
- `ens_autres_dep_reste` : l'iFRAP dit certaines mesures « déjà inscrites au budget » ; non vérifié dans le programme de stabilité.
- `ens_elec`, `nfp_taxe_macron` : tarif réduit de l'accise en vigueur jusqu'au 31/01/2025 et retour au tarif normal prévu par le programme de stabilité ; les deux lignes coûtent bien (pas de critère).
- `nfp_retraites`, `rn24_retraites` : les calculs portent sur l'âge et la durée, conformes (2023-849 DC) ; les articles censurés n'y entrent pas.

## 5. Lacunes

Légifrance refuse les accès automatisés ; l'état des dispositions permanentes (PFU, TTF, IFI, RLS, AME, donations…) est établi à partir de documents officiels datés ou du texte du chiffreur de juin 2024, en confiance medium. Détail : `parts/notes_agent.md` § 5.

## 6. Décisions de l'intégrateur

Lecture A retenue pour le chômage (choix de l'utilisateur, 22/10/2026). Traitement de `nfp_asile` proposé, en attente de validation. Corrections préparées dans `corrections.csv` (13 valeurs, pour `scripts/appliquer_corrections.py`), non appliquées :

1. `nfp_asile` : `statut_reference` `partielle`, `facteur_reference` 0, `source_reference` (décision 2023-863 DC, loi n° 2024-42), `confiance_reference` `high`. Le montant de Montaigne reste affiché ; la ligne compte pour 0.
2. `ens_chomage` : règle « Aucune » (celle de la famille), facteur 1, `statut_reference` `absente`. Compte +4,5.
3. `rn24_chomage` : `statut_reference` `votée` (les règles qu'elle veut garder sont celles du droit de juin 2024), `facteur_reference` 0. Compte 0, comme la promesse identique du NFP.

Effet sur les soldes centraux à économie constante : NFP 2024 +1,3 ; Ensemble 2024 +4,5 ; RN 2024 +4,5.

À faire en même temps (hors `corrections.csv`) :

- `data/raw/chiffrages_instituts.csv` : notes de `rn24_chomage` (Montaigne) et `ens_chomage` (iFRAP), qui décrivent l'ancien écart avec le site ;
- `data/raw/non_chiffre_foyer.csv`, NFP n° 22 : libellé sans « accès aux prestations » ;
- `recherche/T1/convention_application_2024.md` : `ens_chomage` n'est plus l'exception ; ajouter les lignes annulées par la référence ;
- `web/index.html` (comparaison par organisme) : la phrase sur la réforme chômage « déjà décidée » ne vaut plus ;
- `web/site.js`, fiche d'une ligne : pour une ligne 2024, le facteur de référence se lit « par rapport au droit de juin 2024 », pas « déjà prévue par les budgets 2027 » ;
- `scripts/check_regression.py` : totaux attendus des trois programmes.
