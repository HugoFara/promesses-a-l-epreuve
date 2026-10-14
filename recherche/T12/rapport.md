# T12 — Rachats d'actions et évaluations préalables (14 octobre 2026)

## 1. Taxe sur les rachats d'actions : chiffrage avant adoption

**Question** (point ouvert du HANDOFF) : confirmer le chiffrage d'avant adoption de la taxe sur les réductions de capital (0,2 Md€ selon la presse) et le comparer aux 0,5 Md€ encaissés en 2025.

**Trois chiffres, deux périmètres.**

| Chiffre | Version de la taxe | Source (lue) |
|---|---|---|
| « au moins 200 M€ » en 2025, reconduit en 2026-2027 | PLF 2025, art. 26 : opérations à partir du 10/10/2024, 8 % du nominal et des primes | Évaluation préalable, § 4.2.1 et 4.3, p. 265-266 du PDF (`sources/T12/PLF2025_evaluations_prealables.pdf`) |
| **400 M€ en 2025** | Loi votée : taxe pérenne à partir du 1/3/2025 **plus** taxe temporaire sur les opérations du 1/3/2024 au 28/2/2025 (art. 95 de la loi n° 2025-127, lu sur Légifrance) | État A, ligne 1796, texte de la CMP n° 873, p. 401 du PDF ; l'amendement n° 23 du Gouvernement, qui actualise l'état A, ne modifie pas cette ligne (amendements nos 1 à 23 sur ce texte vérifiés) |
| **0,5 Md€ encaissé en 2025** | Loi votée | Cour des comptes, note recettes fiscales 2025, tableau 13, « Adoption de la taxe sur les rachats d'actions + 0,5 » |

Le chiffre de la presse (0,2) est bien celui de l'évaluation préalable, mais pour une version qui ne taxait pas les opérations de mars à octobre 2024. Le chiffrage comparable au réalisé est celui de la loi votée : **0,4 prévu, 0,5 encaissé (+25 %)**. Un amendement du PLF 2026 (I-2741) cite aussi un rendement attendu « ne dépass[ant] pas les 400 M€ » (source secondaire, conforme).

**Ajout à la couche 1** : mesure `rachats_2025` (confiance high, réalisé observé : impôt nouveau, donc la mesure nouvelle est la recette ; arrondi de la Cour à 0,1 Md€ → bornes 0,45-0,55). La statistique principale passe à 26 mesures, erreur médiane 11,2 % (10,0 % avant) ; non-régression mise à jour.

**Attribution à l'aveugle** (agent 3, `recherche/validation/attribution_agent_3_rachats.csv`, protocole inchangé : libellé, année, sens, chiffrage et liste des règles seulement) : « Nouvelle assiette : risque juridique » (facteur 0,8), issue déclarée inconnue. Corrigé 0,32 pour 0,5 réalisé : la règle passe de « non testée » à **« contredite » sur un cas**. Elle s'applique aussi à la taxe Zucman du panier LFI (`l_zucman`) ; un seul cas ne suffit pas à la changer, mais il va dans le sens d'une décote trop forte pour une assiette nouvelle qui a tenu juridiquement.

**Conséquence pour `l_rachats`** (8,4 Md€, confiance low) : inchangée. Le réalisé à 8 % du nominal ne dit rien de la réaction à 33 % de la valeur d'acquisition. Les prévisions 2026-2027 de l'État reviennent à 0,2 (LFI 2026, PLF 2027), conformément au « rendement décroissant à périmètre de rachat constant » annoncé par l'évaluation préalable : le 0,5 de 2025 contient la taxe temporaire.

## 2. Évaluations préalables des PLF (mesures de la couche 1 en confiance medium)

Lecture dans le navigateur (budget.gouv.fr bloque les robots ; PDF lus avec pdf.js dans la page, sha256 calculé dans la page, fiches d'extraits dans `sources/T12/`).

| Mesure | Document lu | Résultat | Confiance |
|---|---|---|---|
| `ip_2021` impôts de production | Évaluations préalables PLF 2021, art. 3-4 | « coût brut pour l'État […] estimé à 10 Md€ à compter de 2021 » (p. 31 et 53) ; CVAE 7,2, CFE 1,54, TFPB 1,75 ; interaction −0,4. Identique au rapport général AN | **medium → high** (ex post de la Cour cité directement : 10,3) |
| `ir_baisse_2020` baisse de l'IR | Évaluations préalables PLF 2020, art. 2 | État −5 Md€ par an 2020-2023 (p. 23), « environ 5 Mds€ » après coefficient de recouvrement 0,985 | medium inchangé : l'ex post reste une microsimulation Ines |
| `th_20` taxe d'habitation, 20 % restants | Évaluations préalables PLF 2020, art. 5 | État −2,3 / −5,1 / −7,8 Md€ en 2021-2023 (p. 91), identique au rapport AN | medium inchangé : ex ante et ex post restent des différences ou sommes calculées |
| `cite_2015` CITE | Évaluations préalables PLF 2015, art. 3 | Seul le surcoût par rapport au CIDD est chiffré : 700 M€ en année pleine (330 + 360 + 10 + 1,5), 230 M€ sur 2014. Le total de 1,4 Md€ attribué à ce document par le rapporteur général n'y figure pas | medium inchangé (signalé) |
| `cir_2008` CIR | PLF 2008 (AN n° 189), exposé des motifs de l'art. 39 | Aucun chiffrage ; pas d'évaluation préalable avant le PLF 2010 ; dossier de presse PLF 2008 non archivé sur budget.gouv.fr | medium inchangé |
| `apl_contemp_2021` APL en temps réel | PAP 2021, programme 109 (version de 22 p.) | Réforme mentionnée, sans chiffrage (0,746 Md€ toujours lu dans le rapport spécial AN et la Cour) | medium inchangé |
| `is_25` baisse de l'IS | non relu | Le rapporteur général indique que la consolidation 33⅓ → 25 % « n'est pas fournie par l'évaluation préalable » ; l'ex post est une somme calculée | medium inchangé |

Les autres mesures medium (`pacte_2015`, chèques énergie, bouclier gaz) le sont pour des raisons propres à l'ex post (sommes calculées, exécution non définitive, estimation CRE) qu'aucune évaluation préalable ne lève.

**Bilan** : 10 mesures restent en confiance medium (11 avant). Les évaluations préalables confirment les chiffres repris de seconde main ; aucun ex ante n'est modifié.
