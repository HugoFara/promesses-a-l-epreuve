# T16, volet C (fiscalité) : rapport de recherche

Date : 14 octobre 2026. Fichiers : `C_chiffres.csv` (68 lignes), `C_sources.csv` (30 sources archivées dans `sources/T16/C/`).

Règles suivies : chaque chiffre du CSV vient d'un document lu et archivé. Une valeur « dérivée » (calcul simple sur un chiffre lu) est marquée comme telle et notée `medium`. Les chiffres lus seulement dans une source qui en cite une autre sont notés `medium`. Les chiffres politiques ou militants sont notés `low`.

Incidents d'accès : ccomptes.fr (certaines pages), vie-publique.fr, ecologie.gouv.fr et strategie-plan.gouv.fr étaient en maintenance ou bloqués ; economie.gouv.fr, ifrap.org et institutmontaigne.org étaient derrière Cloudflare. J'ai lu le rapport HCSP 2026, le guide MTE 2026 et la page Montaigne sur des copies Wayback, et la synthèse de la Cour (fraude, déc. 2025) sur une copie hébergée par un tiers. Le rapport complet de la Cour n'a pas été lu.

---

## 1. Supprimer les aides aux entreprises « sans contrepartie »

### Trouvé

Le total dépend surtout de deux choix : compter ou non les **allègements généraux de cotisations**, et compter ou non les **prêts et garanties** (Bpifrance) et les **dépenses fiscales « déclassées »** (par exemple le régime de groupe).

| Estimation | Année | Md€ | Ce qui est compté |
|---|---|---|---|
| Aides d'État (droit européen) | 2023 | 45 | dispositifs qui faussent la concurrence |
| HCSP 2026, périmètre 1 | 2023 | 82 | aides directes et ciblées, sans les allègements généraux |
| IGF 2024 (cité par le HCSP) | 2022 | 88 (105 avec les collectivités et l'UE) | aides ciblées, sans les allègements |
| Sénat 2025, sens strict | 2023 | 108 | dépenses fiscales 26 + allègements 75 + subventions 7 |
| HCSP 2025 (note Harfi) | 2023 | 112 | sans les exonérations générales |
| Ministre de l'Économie (audition) | n.p. | 150 | dépenses fiscales 40 + budget 30 + allègements 80 |
| Clersé/IRES 2022 (cité) | 2019 | 157 à 205 | sans les prêts ; 205 avec les déclassées |
| HCSP 2026, périmètre 2 | 2023 | 187 | + exonérations générales, TVA sectorielle, collectivités indirectes |
| Sénat 2025, sens large (plancher) | 2023 | 211 | Bpifrance 41 + dépenses fiscales 88 + allègements 75 + subventions 7 |
| France Stratégie 2020 (cité) | 2019 | 139 à 223 | quatre périmètres concentriques |

Le HCSP retient deux périmètres de référence (82 et 187), sans consensus de sa commission de concertation. Il propose de les publier chaque année en annexe du PLF.

### Non trouvé

- **La part « sans contrepartie ou engagement » n'est chiffrée nulle part.** J'ai cherché dans la synthèse et le tome I du Sénat (mots « contrepartie », « conditionnalité ») et dans le rapport HCSP 2026. Le Sénat donne seulement une liste d'exemples d'aides avec contreparties (PGE sans dividendes, clauses anti-délocalisation des aides à finalité régionale, maintien de l'emploi dans certaines régions). Le HCSP présente la conditionnalité comme un point de désaccord (p. 20 du PDF). Piège de vocabulaire : pour le HCSP, une aide est par définition « sans contrepartie équivalente ». Ce critère sert à définir une aide, pas à repérer les aides sans conditions.
- Rapports France Stratégie 2020, Clersé 2022 et IGF 2024 : pas lus directement, chiffres repris des tableaux du Sénat et du HCSP (`medium`).

### Pièges

- **Allègements généraux** (≈ 75 Md€) : selon les sources, c'est la « norme » du coût du travail ou une aide. C'est l'essentiel de l'écart entre 82 et 187, ou entre 108 et 211.
- **Prêts et garanties** : ils sont remboursés et rémunérés. Les compter pour leur montant nominal (41 Md€ chez le Sénat) n'a rien à voir avec un coût budgétaire. Le HCSP les compte en équivalent-subvention.
- **TVA** : le bénéficiaire réel d'un taux réduit sectoriel n'est pas connu (entreprise ou client).
- Le document européen « Mind the Gap » (fiche France, p. 7 du PDF) qualifie à tort les 211 Md€ du Sénat de « tax expenditures » : à ne pas reprendre.
- Supprimer une aide ne rapporte pas son montant : il faut tenir compte des effets sur l'emploi (allègements), sur la R&D (CIR, voir `elasticites.csv` `cir_cnepi`) et des hausses d'impôt induites. Aucune source lue ne chiffre la suppression d'un bloc « sans contrepartie ».

### Proposition pour la carte

« Selon la définition, les aides publiques aux entreprises vont de 82 à 211 milliards d'euros par an (2023). L'écart vient surtout des baisses générales de cotisations sociales (environ 75 milliards). Aucune étude publique ne chiffre la part des aides versées sans contrepartie. »

---

## 2. Lutter contre l'évasion et la fraude fiscales

### Trouvé

**Estimations du manque à gagner** (elles ne s'additionnent pas et ne mesurent pas la même chose) :

- Insee 2022 (document de travail, données 2012) : TVA non recouvrée entre **20 et 25 Md€** (IC 95 % : 19 à 26). Ce chiffre comprend les erreurs de bonne foi. Les auteurs signalent un biais de sélection des contrôles que seuls des contrôles aléatoires lèveraient (`high`).
- Cour des comptes 2019 (citée par l'Insee) : une quinzaine de Md€ pour la même année ; le CPO 2023 cite 12 à 20 Md€.
- Commission européenne (VAT compliance gap) : **12 Md€ en 2023**, soit 6 % de la TVA théorique (5 % en 2022, 4 % en 2021). Ce chiffre comprend les faillites et les erreurs. La moyenne de l'UE est de 9,5 %.
- Solidaires Finances publiques (2018) : 80 à 100 Md€ pour la fraude et l'évasion, tous impôts confondus. C'est une **estimation militante**, dont le rapport original n'a pas été lu (citée dans une question écrite de l'Assemblée). Le Gouvernement répond alors que le manque à gagner n'a « fait l'objet d'aucun chiffrage précis » (`low`).
- **Aucune estimation officielle tous impôts.** La Cour (déc. 2025) juge cette absence « regrettable » : la DGFiP n'a commencé qu'en 2022, sur la TVA, et la Cour demande des estimations TVA, IS et IR d'ici 2027.

**Résultats du contrôle fiscal** (DGFiP, dossier de presse du 7/4/2026) :

| | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Droits et pénalités notifiés (Md€) | 13,4 | 14,6 | 15,2 | 16,7 | 17,1 |
| Encaissés (Md€) | 10,7 | 10,6 | 10,6 | 11,4 | 11,4 |

En 2025, il faut ajouter 8,4 Md€ de crédits d'impôt non remboursés, dont 4,85 Md€ pour une seule société.

La Cour (périmètre un peu différent) : droits rappelés et crédits non remboursés passés de 16,1 Md€ (2015) à 17,4 Md€ (2024), soit +8 %, alors que les recettes fiscales de la DGFiP ont augmenté de 44 %.

**Ce que les plans ont rapporté** : la prévision 2026 comptait 1,5 Md€ de recettes nouvelles grâce à la lutte contre la fraude. Ce rendement a disparu de la prévision révisée, et le HCFP le jugeait déjà « optimiste voire hypothétique ». Il est reconduit à **1,0 Md€ en 2027** (avec la facturation électronique). La loi n° 2026-534 n'a pas d'étude d'impact chiffrée lue ici.

### Non trouvé

- L'estimation DGFiP « 6 à 10 Md€ » d'insuffisances de TVA, citée par la presse, n'a pas été lue dans une publication DGFiP. Elle n'est pas dans le CSV.
- Le rapport complet de la Cour (déc. 2025), le rapport Cour 2019 et l'étude d'impact de la loi de 2026 n'ont pas pu être téléchargés : sites en maintenance.

### Pièges

- **Notifié n'est pas encaissé** : environ deux tiers des montants notifiés sont encaissés, avec plusieurs années de décalage.
- La « contribution totale du contrôle fiscal » de 25,5 Md€ est un agrégat ministériel, pas une recette.
- **Écart de TVA n'est pas fraude** : l'écart comprend les erreurs et les faillites.
- Plus de contrôles ne récupère qu'une partie du manque à gagner, et le rendement marginal décroît. L'expérience 2026 (1,5 Md€ prévus, disparus) va dans le même sens que la règle « effet promis » du moteur.

### Proposition pour la carte

« Personne ne sait combien coûte la fraude fiscale en France : l'État ne publie pas d'estimation. Pour la seule TVA, les estimations vont de 12 à 25 milliards d'euros par an. Le fisc réclame environ 17 milliards par an après contrôle et en encaisse environ 11. »

---

## 3. Taxer davantage les « méga-héritages »

### Trouvé

- **Recettes totales des DMTG** : 22,0 Md€ prévus en 2027 (successions 17,0 et donations 5,0, état A du PLF 2027). 2026 compte 1,6 Md€ de recettes exceptionnelles (HCFP), qui ne seront pas reconduites en 2027. La Cour, citée par LCP, donne 16,6 Md€ en 2023. Le CAE retient 15 Md€ comme base de ses simulations.
- **Concentration** (CAE, note 69) : le top 0,1 % des héritiers d'une génération reçoit environ 13 M€ chacun, mais paie à peine 10 % de droits, alors que le taux marginal est de 45 %. Les successions en ligne indirecte font moins de 10 % du capital transmis mais plus de 50 % des recettes.
- **Mesures ciblées chiffrées** :
  - CAE « assiette 2, barème 4 » : plus de 10 Md€ par an en état stationnaire, et 99 % des héritiers gagnants ou non touchés. C'est le chiffrage le plus proche de l'idée.
  - CAE « assiette 1 » (assurance-vie, démembrement, Dutreil, déjà dans `paniers` `l_succ`) : environ 9 Md€.
  - Coût du pacte Dutreil : environ 5,5 Md€ en 2024 (Cour, cité par le Sénat).

### Non trouvé

- **Aucune répartition officielle des droits par taille de succession.** La DGFiP ne publie plus d'enquête DMTG depuis 2006 (CAE p. 5), et la dernière étude représentative date de 2010 (Sénat, juin 2026). Le Sénat demande des « enquêtes DMTG 2.0 » et la numérisation des déclarations, prévue en 2033 seulement.
- La note France Stratégie 2017 sur l'héritage n'a pas été cherchée plus loin : le CAE 2021 est plus récent et utilise les mêmes données.
- Chiffrages politiques 2026 (15 Md€ pour « les 1 % les plus gros », annoncés par un candidat ; 15 Md€ pour une autre réforme) : déclarations rapportées par la presse, sans méthode publiée (`low`). Ils ne sont pas à utiliser.

### Pièges

- Le rendement est **statique** et vaut en « état stationnaire » : il faut des années pour que les transmissions passent au nouveau régime, et les comportements d'anticipation (donations, assurance-vie, expatriation) jouent. Voir `elasticites.csv` `succession_us` (élasticité 0,16, modeste).
- Les recettes d'une année dépendent de quelques très grosses successions (exemple : +1,6 Md€ en 2026).
- Le patrimoine déclaré est inférieur de 35 à 40 % au flux économique (CAE) : l'assiette est mal connue.
- Repère « peut-on s'y fier ? » sur les très hautes assiettes : la contribution différentielle sur les hauts revenus devait rapporter 2 Md€, elle rapporterait 388 M€ en 2025, soit -81 % (Sénat 2026).

### Proposition pour la carte

« Les droits sur les successions et les donations rapportent environ 22 milliards d'euros par an. Une réforme qui viserait les 1 % des plus gros héritages, en supprimant les principales niches, pourrait rapporter plus de 10 milliards par an à terme selon le Conseil d'analyse économique. Le gain viendrait lentement et reste incertain, car l'État ne publie plus de données sur les héritages par taille. »

---

## 4. Baisser les taxes sur les carburants

### Trouvé

- **Rendement de l'accise** sur les produits pétroliers : 31,6 Md€ bruts en 2024 (31,7 en 2023, 31,4 prévus en 2025). Sur ce total, 11,9 Md€ vont aux collectivités et 1,7 Md€ à l'AFITF, et la part nette de l'État est de 16,0 Md€ (guide MTE 2026, d'après Voies et moyens tome I). Le PLF 2027 prévoit 16,3 Md€ nets pour l'État sur les seuls carburants.
- **Volumes** : 47,5 millions de m³ de carburants routiers livrés en 2025 (CPDP/Ufip), dont environ 32 de gazole et 15,6 d'essence.
- **Coût d'un centime par litre (dérivé)** : 47,5 milliards de litres × 1 centime ≈ **0,48 Md€ par an** hors TVA (gazole ≈ 0,32, essence ≈ 0,16), et ≈ 0,57 Md€ avec la TVA sur l'accise. Ce calcul est statique et majore un peu le coût : les remboursements partiels (transporteurs, taxis) baissent quand le tarif baisse, et la consommation remonte un peu (élasticité −0,3 la première année, `elasticites.csv`).
- **Remise carburant 2022** (point de comparaison) :
  - ex ante en enveloppes successives : 4,6 Md€ en LFR 1 (avec l'indemnité carburant travailleurs), puis 0,4 Md€ pour l'extension (PLFR 2) ;
  - réalisé : 7,6 Md€ pour l'État (Cour, mars 2024), soit 7,854 Md€ d'exécution budgétaire, plus environ 0,83 Md€ de TVA perdue ;
  - la remise a atteint jusqu'à 0,25 €/l hors TVA (18 c TTC, puis 30 c TTC, puis 10 c TTC), et le prix a baissé de 10,8 % en moyenne (CAE-Insee, cité par la Cour).
- **Contexte 2026** : accises sur l'énergie 2026 révisées à -1,9 Md€, et accise des 7 premiers mois en baisse de 6,3 % (HCFP). Au 20 septembre, les recettes carburants de l'État ont baissé de 407 M€ : +710 M€ de TVA, -1,117 Md€ d'accise (déclaration du ministre, AFP). Les aides ciblées 2026 ont été prévues à 1,4 Md€ et projetées à 0,7 Md€, plus 450 M€ de prolongation (HCFP). Pour le Gouvernement, une TVA à 5,5 % sur toutes les énergies coûterait 12 à 15 Md€ et serait contraire au droit de l'UE (AFP, `low`).

### Non trouvé

- Pas de chiffre officiel récent du « coût d'un centime » (Voies et moyens tome I PLF 2027 introuvable en ligne ; amendements anciens de 2015 avec des volumes périmés). D'où la valeur dérivée.
- L'ex ante initial de la remise (≈ 3 Md€ pour avril-juillet 2022) est cité par la presse, pas lu dans le décret. La comparaison prévu/réalisé n'est donc possible que sur l'ensemble de l'année 2022.

### Pièges

- **Part État ou total** : l'État ne touche qu'environ la moitié de l'accise. Une baisse touche aussi les régions, les départements et l'AFITF.
- **Hors TVA ou TTC** : une baisse d'accise de 1 c fait baisser le prix d'environ 1,2 c, et l'État perd aussi la TVA correspondante.
- **Remise ou baisse d'accise** : la remise profitait aussi aux usages à taux réduit (agriculteurs, BTP), ce qui n'est pas le cas d'une baisse d'accise.
- **Pas de « cagnotte »** : la hausse des prix fait perdre de l'accise (un montant par litre) plus qu'elle ne fait gagner de TVA (2026).

### Proposition pour la carte

« Chaque centime de baisse de la taxe sur les carburants coûte environ un demi-milliard d'euros par an, partagé entre l'État et les collectivités. En 2022, la remise à la pompe (jusqu'à 30 centimes) a coûté 7,6 milliards d'euros en neuf mois. »

---

## 5. Baisser la TVA sur les produits de première nécessité

### Trouvé

- **Le taux de 5,5 % sur l'alimentation n'est pas une dépense fiscale** : l'État le considère comme une règle générale (Voies et moyens tome II, p. 10). Il n'a donc **pas de chiffrage annuel officiel**.
- Le CPO (2023) l'évalue à **20,1 Md€ en 2020** par rapport au taux de 20 %. C'est la mesure de TVA la plus coûteuse, sur au moins 47 Md€ de mesures dérogatoires au total.
- **Taux zéro sur toute l'alimentation** : 9,4 Md€ (CPO), soit environ 1,7 Md€ par point de taux (dérivé).
- **Liste restreinte** (pain, céréales, lait, fromage, œufs, huiles, fruits et légumes, hygiène) : 4,7 Md€. **Liste large** (y compris viandes, poissons et produits d'entretien) : 8,8 Md€ (Institut Montaigne 2024, d'après Astérès 2022, euros 2023).
- **Espagne** : 1,3 Md€ par an pour un panier réduit (Montaigne, source non précisée).
- **Répercussion sur les prix (colonne « peut-on s'y fier ? »)** :
  - TVA restauration 2009 (Insee) : environ 20 % répercutés à long terme (prix -2,4 % au lieu de -9,8 %). Benzarti-Carloni trouvent environ 12 % (déjà dans `elasticites.csv`).
  - Portugal 2023, taux zéro sur 46 produits alimentaires : répercussion de 99,8 % à l'impact, et retour symétrique des prix à la fin (Bernardino et al., JPubE 2025).
  - Espagne 2023 : répercussion « presque complète » (Banque d'Espagne, une enseigne en ligne). La CNMC ne trouve pas d'indice de non-répercussion.
  - Le CPO retient une hypothèse de 80 %.
- **Qui y gagne** (CPO) : à coût égal (9,4 Md€), un chèque ciblé relève le niveau de vie du premier décile de 7,3 %, contre 1,5 % pour la suppression de la TVA alimentaire.

### Non trouvé

- Pas de chiffrage officiel récent (PLF 2026 ou 2027) du coût du 5,5 % alimentaire.
- L'étude d'Astérès elle-même n'a pas été lue (citée par Montaigne).
- La note de l'Irish Fiscal Council sur la répercussion n'a pas été téléchargée (accès bloqué).

### Pièges

- **Coût selon le point de départ** : 20,1 Md€ par rapport au taux normal, ou 9,4 Md€ pour passer de 5,5 % à 0. Ne pas confondre les deux.
- **La répercussion dépend du contexte** : faible pour une baisse sectorielle et permanente dans les services (restauration 2009), quasi complète pour une baisse temporaire, très visible, sur l'alimentation en période d'inflation, avec contrôle des prix (Espagne, Portugal). Les baisses sont transmises moins que les hausses (`elasticites.csv` `tva_asym`).
- Le gain va à tous les ménages, et plus en euros aux ménages aisés.

### Proposition pour la carte

« Supprimer la TVA sur toute l'alimentation coûterait environ 9 milliards d'euros par an, et 4 à 5 milliards sur une liste courte de produits de base. Quand l'Espagne et le Portugal l'ont fait en 2023, les prix ont presque entièrement baissé d'autant. La baisse de TVA dans la restauration en 2009, elle, n'avait presque pas fait baisser les prix. »

---

## Décisions laissées à l'intégrateur

1. **Aides aux entreprises** : retenir la fourchette HCSP (82 à 187) comme officielle, ou 108 à 211 (Sénat) ; la carte peut montrer les deux. Pas de chiffre « sans contrepartie » possible.
2. **Fraude** : la carte n'aura pas de « rendement ». Il faut décider si l'on donne la valeur `ens_fraude` du moteur (avec la règle « effet promis ») ou seulement les ordres de grandeur.
3. **Carburants** : la valeur dérivée de 0,48 ou 0,57 Md€ par centime n'est pas lue telle quelle dans une source. La remplacer si le tome I des Voies et moyens PLF 2027 devient accessible.
4. **Héritages** : utiliser le CAE (plus de 10 Md€, état stationnaire) avec la règle `Élasticité succession` des paniers.
5. **Repères** (part du déficit, euros par habitant) : non calculés ici. Ils sont à faire avec `projection_reference.csv`.
