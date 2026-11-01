# T26, partie A : paniers 2027 (`l_bandeaux`, `e_carence`, `e_oper`, `l_brunes`)

Agent A, 01/11/2026. Gel : commit `a323509`. Tous les liens et empreintes sont dans `sources_A.csv`. Les nouvelles archives sont dans `sources/T26/A/`.

## Résumé

| Ligne | Facteur actuel | Facteur proposé | Fourchette | Voté seul | Confiance |
|---|---|---|---|---|---|
| `l_bandeaux` | 0,5 [0,09 ; 0,87] | **0,4** | [0,26 ; 0,50] | 0,55 [0,44 ; 0,63] (0,5 si le gel vaut pour 2027) | low (modèle) |
| `e_carence` | 0,5 [0 ; 1] | **0,5** (inchangé) | [0 ; 1] | 1 | medium sur les faits, low sur le facteur |
| `e_oper` | 1 | **1** (confirmé) | [1 ; 1] au sens strict | 1 | medium |
| `l_brunes` | 1 | **0,95** | [0,91 ; 0,96] | 0,95 | high |

État des textes au 01/11/2026. Le PLFSS 2027 a été rejeté par l'Assemblée le 23/10/2026 (T.A. n° 358, dossier AN) ; le Sénat examine le texte initial à partir du 09/11 (Deloitte, secondaire). Le PLF 2027 est encore en première lecture à l'AN (délai de 40 jours jusqu'au 17/11, Deloitte). Tout ce qui vient des PLF et PLFSS 2027 reste donc un projet.

## 1. `l_bandeaux`

### 1.1 Ce que mesure la ligne

Bozio-Wasmer (rapport final, chap. 4, p. 202) : le scénario consiste à « supprimer les bandeaux maladie et famille, en prolongeant la courbe de la réduction générale jusqu'à une extinction complète des exonérations à 1,88 Smic ». Il « génère ex ante une économie budgétaire de 12,2 Md€ », 11,4 après effets emploi, avec « un taux marginal inchangé de 59 % jusqu'à 1,6 Smic ». En dessous de 1,6 SMIC, le barème ne change pas. Le rendement est donc la somme des allègements de 2024 situés au-dessus de 1,6 SMIC, moins la queue conservée entre 1,6 et 1,88.

Vérification : avec 7,8 points de bandeaux à 1,6 SMIC, la pente de la réduction générale s'annule à 1,88 si Tmax ≈ 0,314. Le chiffre de 1,88 est donc cohérent avec le barème de 2024.

### 1.2 Ce qui a changé dans la référence (baisses classées par niveau de salaire)

| Mesure | Montant | Où porte-t-elle ? | Statut | Source |
|---|---|---|---|---|
| Abaissement des points de sortie (2,25 et 3,3 SMIC), 2025 | 2,0 brut ; 1,6 net de l'IS | 100 % au-dessus de 2,25 SMIC | voté (LFSS 2025) | CCSS mai 2026, p. 64 ; Insee IP 2106 |
| PPV dans l'assiette de la réduction générale, 2025 | 0,8 (0,6 régimes de base) | 0 % au-dessus de 1,6 SMIC (la réduction s'arrêtait alors à 1,6) | voté | CCSS p. 64 |
| Gel des points de sortie (LFSS 2024) | 0,4 (2024), 0,6 (2025) | au-dessus de 1,6 | voté avant la base | CCSS p. 64 ; caduc en 2026 |
| **RGDU au 1/1/2026** (fusion, sortie à 3 SMIC, plancher 2 %, convexité) | coût total à peu près inchangé ; non ventilé | change tout le profil au-dessus de 1,6 SMIC | **voté** (LFSS 2025 art. 18 ; LFSS 2026 art. 40) | annexe 4 PLFSS 2027 p. 22 et 36 ; CCSS tableau 2 |
| Gel du SMIC de référence (12,02 € au lieu de 12,31 €) | 2,8 (2026) + 2,9 (2027) ; 5,6 pour 2026-2027 | partout, surtout près du SMIC ; environ 15 à 18 % au-dessus de 1,6 (modèle) | 2026 : décret ; 2027 : projet | HCFP 2026-5 tableaux 6 et 7 ; annexe 4 p. 36 ; PLF 2027 (TVA) |
| Compléments de salaire dans la rémunération qui sert au coefficient (art. 7) | 3,7 (3,3 + 0,4 PPV) | 25 à 46 % au-dessus de 1,6 (modèle) | projet | annexe 9 art. 7 p. 41 ; HCFP |

Trois constats changent la lecture de la note actuelle (« 1,6 + 2,8 + 2,9 + 3,7 = 11,0 ; RGDU non comptée ») :

1. **La baisse de 2025 a disparu en 2027.** Les bandeaux ont été supprimés au 1/1/2026 (CCSS : « suppression au 1er janvier 2026 des réductions proportionnelles […] et leur remplacement par une réduction générale dégressive unique »). Les 1,6 (ou 2,0) de 2025 ne s'ajoutent pas à l'effet de 2026 : ils sont remplacés par le profil de la RGDU.
2. **La RGDU, votée, est le principal recoupement.** Elle redistribue les allègements au-dessus de 1,6 SMIC. À 1,6 SMIC, le coefficient vaut 10,9 % (RGDU) contre 7,8 points (bandeaux 2025). À 2 SMIC, il vaut 5,3 % contre 7,8. À 2,5 SMIC, 2,7 % contre 1,8. Il vaut 2 % jusqu'à 3 SMIC, puis 0.
3. **Le gel et l'assiette ne portent qu'en partie au-dessus de 1,6 SMIC.** Le gel abaisse le coefficient sur toute l'échelle. Au SMIC réel, le rapport 3 × 12,02 / 12,31 = 2,93 ramène le coefficient de 0,398 à 0,375. La borne basse 0,09 (tout au-dessus de 1,6) n'est donc pas plausible.

Aucune ventilation officielle par niveau de salaire n'a été trouvée. Ont été lus : annexe 4 PLFSS 2027 (cas-type à 2 SMIC seulement) ; annexe 9 PLFSS 2027 art. 7 (graphique de répartition de l'intéressement et de la participation, cas-types à 1,8, 2, 2,5 et 3 SMIC) ; annexe 9 PLFSS 2026 ; CCSS mai 2026 (fiche 1.6) ; HCFP 2026-5 ; dossier de presse PLFSS 2026. Recherches web sur la répartition de la RGDU entre 1,6 et 3 SMIC : rien.

### 1.3 Modèle (faute de ventilation publiée)

Barème RGDU (FNTP, paramètres 2026, secondaire) : C = Tmin + Tdelta × [½ (3 × SMIC / rémunération − 1)]^P, avec Tmin = 0,02, Tdelta = 0,3781 et P = 1,75. Le SMIC est gelé à 12,02 € au lieu de 12,31 €.

Barème 2024 au-dessus de 1,6 SMIC : bandeaux de 6 points jusqu'à 2,5 SMIC et de 1,8 point jusqu'à 3,5 SMIC (seuils en SMIC courant).

Le scénario de la ligne est transposé à 2027 de deux façons :

- **A** : de C(1,6) à 0 de façon linéaire en 1,88 SMIC, comme la prolongation de pente de Bozio-Wasmer ;
- **B** : RGDU inchangée jusqu'à 1,88 SMIC, puis 0.

Distribution des salariés : Bozio-Wasmer p. 30. Les deux tiers sont sous 1,6 SMIC, 89 % sous 2,5 et 98 % sous 3,5. Pour la masse au SMIC, j'ai retenu 17,3 % ; la ligne de Bozio-Wasmer (« en 2023, 17,3 % des salariés (3,1 millions de personnes) ») n'a pas été relue en entier. Trois profils à l'intérieur des bandes ont été testés : uniforme, décroissant, très décroissant.

Contrôles (le modèle est calibré pour que le rendement 2024 vaille 12,2 Md€) :

| Grandeur | Modèle | Officiel |
|---|---|---|
| Coût total de la RGDU, 2026 | 74 à 90 Md€ | 74,7 (CCSS, tableau 2) |
| Gel en année pleine (écart de 2,4 %) | 4,8 à 5,8 Md€ | 2,8 sur 7 mois en 2026 ; 5,6 pour 2026-2027 |
| Baisse de 2025 / rendement de la ligne | 17 à 25 % | 2,0 / 12,2 = 16 % |
| Cas-types art. 7 (1,8 SMIC + 1 000 € ; 2 SMIC + 2 000 € ; 2,5 SMIC + 2 000 €) | 230 / 319 / 125 € | 213 / 291 / 103 € |
| RGDU / barème 2025, coût total | 1,01 | « neutralité » visée (CCSS) |

Résultats (part du rendement de 2024 restant à gagner en 2027) :

| | A | B |
|---|---|---|
| RGDU seule (votée) | 0,56 à 0,63 | 0,44 à 0,46 |
| + gel en 2027 | 0,51 à 0,58 | 0,40 à 0,42 |
| + assiette art. 7 (−3,7 × [0,25 ; 0,46] / 12,1 = −0,08 à −0,14) | 0,37 à 0,50 | 0,26 à 0,34 |

Facteur proposé : **0,4**, entre le centre de A (0,46) et celui de B (0,31). Fourchette **[0,26 ; 0,50]**. Il s'applique au montant après effets emploi (11,4), comme aujourd'hui.

**Variante « loi votée seule ».** La RGDU est votée et le gel de 2026 est réglementaire. Si le gel s'arrête fin 2026, le facteur vaut environ **0,55** [0,44 ; 0,63]. Le décret 2026-509 remplace dans l'art. D. 241-7 « en vigueur » par « applicable au 1er janvier 2026 », sans date de fin, mais son art. 2 limite l'application « au titre de l'année 2026 ». LégiSocial (29/07/2026) le lit comme valant « pour l'année 2026 mais également pour les années suivantes ». Si cette lecture est la bonne, le gel de 2027 est déjà en vigueur et le facteur vaut environ 0,5. Point juridique à trancher par l'intégrateur.

### 1.4 Réserves

- La distribution des salaires est grossière. C'est elle qui porte l'incertitude, surtout entre 1,6 et 2,2 SMIC.
- La transposition A ou B est un choix de méthode : la ligne a été définie dans le droit de 2024. Un rechiffrage propre de « RGDU éteinte à 1,88 SMIC » (T2) remplacerait ce facteur.
- L'assiette (3,7) est en euros de 2027 et la base (12,1) en euros de 2024 : l'effet est légèrement surestimé.
- Le plafond de la réduction en dessous du SMIC (temps partiel, rémunération sous le SMIC) n'est pas modélisé.

Script (en Python, avec numpy ; à lancer avec `python3 -I`) :

```python
import numpy as np
Tmin,Td,P=0.02,0.3781,1.75
Tmax24=0.6*0.078/(1-1.6/1.88)          # déduit de Bozio-Wasmer (extinction à 1,88)
g=12.02/12.31                            # SMIC gelé / SMIC réel
def rgdu(m,r): x=3*r/m; return 0.0 if x<=1 else Tmin+Td*min(0.5*(x-1),1.0)**P
def law24(m): return (0.06 if m<=2.5 else 0)+(0.018 if m<=3.5 else 0)   # au-dessus de 1,6
def scen24(m): return max(0.078+(Tmax24/0.6)*(1.6/m-1),0.0)
def scenA(m,r): c=rgdu(1.6,r); return max(c*(1.88-m)/0.28,0.0) if m<1.88 else 0.0
def scenB(m,r): return rgdu(m,r) if m<1.88 else 0.0
bands=[(1.6,2.0,0.14),(2.0,2.5,0.083),(2.5,3.0,0.055),(3.0,3.5,0.035)]  # « décroissante »
def integ(f,b): return sum(w*np.mean([f(x)*x for x in np.linspace(a,c,4000)]) for a,c,w in b)
y24=integ(lambda m: law24(m)-scen24(m),bands)
for r in (1.0,g):
    print(r, integ(lambda m: rgdu(m,r)-scenA(m,r),bands)/y24, integ(lambda m: rgdu(m,r)-scenB(m,r),bands)/y24)
```

## 2. `e_carence`

- **PLFSS 2027** (annexe A, II) : « les dépenses d'indemnités journalières d'assurance maladie devraient diminuer de 1 milliard d'euros ». Les seules mesures précisées sont réglementaires et datent de 2026 : prescription limitée à 12 mois (0,1), transports (0,1), plafond des IJ AT-MP (0,2). Aucun article ne porte sur la carence. L'article 20 porte sur la coordination entre médecins, sans chiffrage d'IJ.
- **Instrument : une négociation.** Lettre du ministre du Travail du 07/10/2026, citée par l'AFP (MoneyVox, 08/10). Le gouvernement veut, « plutôt que de procéder immédiatement et par voie réglementaire aux ajustements paramétriques », que les partenaires sociaux négocient « des économies ciblées à 1 milliard d'euros en année pleine », avec « une conclusion […] au plus tard le 19 décembre ». Leviers cités : « durée d'indemnisation, plafond d'indemnisation journalière, complément employeur, taux global de remplacement ». Audition au Sénat (Public Sénat, 15/10) : « moins protéger les arrêts courts, pour moins inciter aux arrêts courts ». Le Medef défend des jours de carence « d'ordre public », non indemnisés ni par la Sécurité sociale ni par les complémentaires (France-Épargne, secondaire).
- **Amendements** : AS1348 (après l'art. 20) a été déclaré irrecevable. Le PLFSS a été rejeté par l'AN le 23/10/2026 ; aucun amendement n'a donc été adopté.
- **Lecture.** Rien n'est voté. L'instrument sera connu au plus tôt le 19/12/2026, et l'issue est incertaine. Un allongement de la carence de la Sécurité sociale reste possible, puisque le gouvernement évoque lui-même la voie réglementaire. Une carence « d'ordre public » visant le complément employeur ne réduirait pas les IJ de la Sécurité sociale. Je garde donc **0,5 [0 ; 1]**, sans base pour le déplacer. **Loi votée seule : 1.** À revoir après le 19/12/2026.
- La lettre originale n'a pas été trouvée : la confiance est medium (dépêche AFP).

## 3. `e_oper`

- **PLF 2027**, exposé général II.4 : « des mesures spécifiques sur les opérateurs ». Il s'agit de France compétences (« baisse des taxes qui lui sont affectées de l'ordre de 1 Md€ », dépense de France compétences −667 M€ selon l'évaluation de l'article apprentissage et CPF), de France Travail (emplois, prestations externalisées) et de −2 209 ETP chez les opérateurs. Aucun de ces postes n'est une fusion ou une suppression d'opérateur.
- **Fusions et suppressions recensées.** Le jaune « Opérateurs » 2027 compte 431 opérateurs l'an dernier et 423 en 2027, d'après Acteurs publics (14/10/2026) :
  - dissolutions : GIP « Les entreprises s'engagent », Comue d'Angers-Le Mans et de Paris-Est ;
  - fusions : les IRA dans le G-ISP, l'IPEV dans l'Ifremer, l'Ensemble intercontemporain dans la Philharmonie.

  Le chiffrage d'économies n'est pas cité. Le jaune lui-même n'a pas été trouvé : il n'est pas lié dans le dossier AN du PLF 2027 et les essais d'identifiants voisins n'ont rien donné.
- **ANDPC** (PLFSS 2027 art. 33, annexe 9) : « une économie comprise entre 1,5 et 3 M€ à compter de 2028 ». Rien en 2027 ; c'est un projet.
- **Conclusion** : aucun recoupement chiffré au sens strict. Facteur **1 confirmé**, y compris pour la loi votée seule. Dans une lecture large (toute économie sur les opérateurs), France compétences suffirait à couvrir la ligne. La consigne écarte cette lecture.

## 4. `l_brunes`

- **Composition des 6 Md€.** Avant-garde (p. 2) : « dépenses fiscales (6 Md€ dans le PLF 2025) ». Le CSV du budget vert du PLF 2025 (data.gouv) donne **6,05 Md€** de dépenses fiscales « défavorables » (prévision 2025, 59 lignes). Principales lignes :
  - TRM 800221 : 1 272 M€ ;
  - outre-mer 800401 : 1 158 M€ ;
  - GNR agricole : 1 135 M€. Le libellé est décalé dans le CSV 2025, sous le code 800229 ;
  - GNR hors agriculture 800201 : 862 M€ ;
  - gaz des installations soumises à l'ETS 830201 : 559 M€ ;
  - Pinel 20 % 110261 : 300 M€ ;
  - outre-mer 710102 : 120 M€ ;
  - TVA 10 % logement social 20 % : 98 M€ ;
  - PTZ 16 % : 96 M€ ;
  - gaz des installations exposées 830202 : 93 M€ ;
  - livret A 5 % : 52 M€ ;
  - taxis : 50 M€.
- **Coût 2027** (budget vert PLF 2027, colonnes 2025 constaté, 2026, 2027) :

  | Dépense fiscale | 2025 constaté | 2026 | 2027 |
  |---|---|---|---|
  | GNR hors agriculture | 646 | 531 | 398 |
  | Pinel/Duflot (20 %) | 298,6 | 269,8 | 239,8 |
  | TRM | 1 259 | 1 306 | 1 306 |
  | Outre-mer 800401 | 1 581 | 1 581 | 1 581 |
  | Gaz ETS | 789 | 470 | 480 |
  | Gaz exposé | 159 | 124 | 125 |
  | Taxis | 58 | 66 | 66 |

  GNR agricole : 1,7 Md€. Ensemble des dépenses fiscales défavorables : « 6,6 Md€ en PLF 2027 » (p. 51).
- **Baisses votées.**
  - GNR hors agriculture : « poursuit sa trajectoire d'alignement avec le gazole routier et passe de 30 […] à 36,79 […] au 1er janvier 2026 » (budget vert 2027, partie II). La baisse est de −248 M€ entre 2025 constaté et 2027. Elle est de −464 M€ si l'on part de la prévision du PLF 2025, réestimation comprise.
  - Pinel : extinction, −60 M€. La part bâtiment compte « 40 % […] de dépenses fiscales qui ont été supprimées » (p. 51).
  - Les autres écarts sont des réestimations (gaz ETS, outre-mer, GNR agricole) ou des changements de quote-part (PTZ, de 16 à 22 %). Ce ne sont pas des recoupements.
- **Facteur** = (6,05 − 0,31) / 6,05 = **0,95** ; [0,91 ; 0,96]. Il est voté en totalité. L'art. 24 du PLF 2027 (nouveaux tarifs réduits sur l'électricité) va dans l'autre sens et n'est pas un recoupement.
- **Point pour l'intégrateur** : le même périmètre coûte davantage en 2027 (6,6 Md€ contre 6,05). Le montant de la ligne pourrait être rechiffré à la hausse, à part du facteur. La trajectoire du GNR n'a pas été lue dans le texte de la LFI 2024 (Légifrance non accessible) ; elle est lue dans le budget vert, document officiel.

## 5. Décisions laissées à l'intégrateur

1. `l_bandeaux` : retenir 0,4 [0,26 ; 0,50] (modèle) ou attendre un rechiffrage T2 de « RGDU éteinte à 1,88 SMIC ». Dans tous les cas, corriger la note : la RGDU votée est le principal recoupement, et la baisse de 2025 ne s'ajoute plus.
2. Gel de 2027 : voté (décret sans terme, lecture LégiSocial) ou projet (PLF/PLFSS) ? Cela change la variante « loi votée seule » de 0,55 à 0,5.
3. `e_carence` : réexaminer après le 19/12/2026.
4. `l_brunes` : rechiffrer éventuellement le statique à 6,6 Md€ (budget vert 2027).
