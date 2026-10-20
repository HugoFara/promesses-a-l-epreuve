# T22, étape 1 : Ensemble 2024, ligne `ens_autres_dep` (−11,7 Md€)

Date d'accès : 2026-10-20. Chiffreur de référence : Institut Montaigne. Règle de découpage appliquée telle qu'écrite au § 1 de la consigne (seuil 1 Md€, pas de répartition de montants de groupe, reste = mère − découpées).

## 1. Grille de lecture

1. Synthèse Ensemble de Montaigne : archive T6 `sources/T6/montaigne_ens_synthese_wb20240710.html` (Wayback 20240710102806), réutilisée. Nouvelle capture du 25/07/2024 (`sources/T22/ENS/montaigne_ens_synthese_wb20240725.html`, Wayback 20240725001837) : texte et montants identiques. Seul ajout : un lien « retrouvez le détail ici » vers le PDF des micro-chiffrages des « Autres mesures ».
2. PDF « Synthèses des micro-chiffrages "Dépenses" », Ensemble (créé le 12/07/2024, Wayback 20241219114407) : détail des 12 « Autres mesures », dont les agents publics.
3. Fiches mesures du Wayback (liste CDX complète du répertoire `ensemble-majorite-presidentielle/`) : SNU et leasing social sont archivés ici. Les autres fiches (notaire, électricité, prime, succession, versement, chômage, rétention) sont dans `sources/T6/`. Il n'existe pas de fiche HTML pour la revalorisation des agents publics.

## 2. Composition de la ligne mère

Bandeau : dépenses −26,9. Les lignes déjà isolées (versement 5, succession 3, notaire 2,8, électricité 2,4, prime 2) font 15,2, ce qui laisse un résidu de 11,7 (T6).

Postes que Montaigne liste dans ce résidu (synthèse) :

| Poste | Md€/an | Traitement |
|---|---|---|
| Revaloriser celles et ceux qui font vivre nos services publics | 4,0 | **découpé** (`ens_agents_publics`) |
| Généraliser le SNU d'ici 2026 | 3,6 | **découpé** (`ens_snu`) |
| Leasing social, 100 000 véhicules/an | 1,3 | **découpé** (`ens_leasing`) |
| Remplacement des absences d'enseignants | 0,7 | reste (sous le seuil) |
| 35 000 logements étudiants | 0,6 (« à horizon 2027 ») | reste |
| Complémentaire santé à 1 €/jour | 0,470 | reste |
| Fauteuils roulants | 0,4 | reste |
| Congé de naissance | 0,4 | reste |
| Retraites agricoles | 0,1 | reste (voir § 4) |
| Numerus clausus | 0,1 | reste |
| Rénovation de 300 000 logements | 0,09 | reste |
| Maisons France services | 30 M€ (−0,03 dans le PDF) | reste |
| Fournitures scolaires | 0,021 | reste |
| Retraite à 65 ans | 0 | reste |
| Effets de seuil | « trop imprécis » | reste (non chiffré) |
| Accès à la santé, garantie Visale | « marginal » | reste (non chiffré) |

**Reste** : −11,7 − (−4,0 − 3,6 − 1,3) = **−2,8 Md€**, soit **23,9 %** de la ligne mère. Les postes restants listés font 2,911. L'écart de 0,11 avec le reste vient de l'écart entre la somme des postes et le bandeau (§ 4). Il est conservé, comme le prévoit la règle 1.4.

Aucun montant de groupe : les trois lignes découpées sont des mesures uniques.

## 3. Recouvrements vérifiés (§ 1.6)

Lignes Ensemble déjà isolées dans `application_lignes.csv` : notaire, électricité, prime, succession, versement, chômage, rétention, fraude, taux. Aucune ne recoupe le point d'indice, le SNU ou le leasing social. Les retraites agricoles (0,1) et la retraite à 65 ans (0) n'ont pas de ligne retraites propre côté Ensemble. Aucun recouvrement, donc rien d'écarté.

À noter pour la fusion : la ligne `ens_autres_dep` de l'iFRAP (−2,36, dans `chiffrages_instituts.csv`) contient déjà le SNU (−1,56) et le leasing (−0,20). Si ces montants sont rattachés aux lignes découpées, il faut les retirer du résidu iFRAP. Le calcul donnerait −0,598 ; je ne l'ai pas saisi, c'est à l'intégrateur de décider.

## 4. Écarts internes chez Montaigne

1. **Somme des postes et bandeau.** Les dépenses listées font 27,011 (5 + 3,6 + 3 + 2,8 + 2,4 + 2 + 1,3 + 0,47 + 0,09 + 0,021 + autres mesures 6,33), alors que le bandeau annonce 26,9. Sur le résidu, cela donne 11,811 de postes pour 11,7. Le texte annonce aussi « 25 Md€ de nouvelles dépenses et moindres recettes sur 3 ans » et « près de 27 Md€ ». Le bandeau fait foi.
2. **Leasing social : coût total ou surcoût.** La fiche annonce un coût de 1,3 Md€ (en tête et dans la synthèse). Elle précise pourtant : « soit 650 M€ additionnels pour 2025 », puisque le dispositif actuel (50 000 véhicules, 650 M€ avec le bonus) existe déjà. J'ai retenu 1,3, le montant publié, comme le veut la règle. Le surcoût de 0,65 passerait sous le seuil : c'est un cas que la règle règle mal, et je le signale sans le corriger. L'iFRAP chiffre −0,2, la campagne 0,1.
3. **Agents publics.** Les 4 Md€ reposent sur une hypothèse de Montaigne, une hausse du point d'indice de 2 points à 2 Md€ le point, « hypothèse non précisée dans le programme ». Ce chiffrage n'a pas de fiche HTML : il figure seulement dans la synthèse et le PDF.
4. **SNU.** La campagne avance 1,4 Md€/an, « dont 0,3 Md€ déjà prévus dans la trajectoire ». Montaigne garde 3,6 (fourchette 1,9-5,4) sans retrancher ces 0,3.
5. **Retraites agricoles.** L'encadré « Estimation » du PDF indique 0,1 Md€ « à horizon 2027 ». Le texte dit pourtant « 0,05 Md€ supplémentaire par an, soit 0,1 Md€ en 2027 et 1 Md€ à horizon 2027 ». Le « 1 Md€ » contredit le calcul et l'encadré : c'est probablement une coquille ou un cumul à un horizon plus lointain. Je n'ai pas découpé ce poste, car le montant publié pour l'horizon de la ligne mère est 0,1. À trancher par l'intégrateur.
6. **France services.** La synthèse indique 30 M€ de coût, le PDF « −0,03 Md€ » (signe ambigu). Le poste reste dans le reste et ne pèse pas sur le découpage.
7. Les versions successives des fiches SNU (28/06 et 25/07) et leasing (27/06 et 25/07) ont un contenu identique. Les deux synthèses (10/07 et 25/07) donnent les mêmes montants.

## 5. Statut par rapport à la référence 2027

- `ens_agents_publics` : **absente**. Le PLF 2027 indique que le point d'indice « ne sera pas revalorisé en 2027 » (archive T1). Confiance high.
- `ens_snu` : **absente**. Le PLF 2026 a supprimé les crédits du SNU (avis du Sénat, action SNU à 0 en 2026 contre 65,9 M€ en 2025), et le texte du PLF 2027 ne le mentionne pas. Je n'ai pas trouvé le PAP 2027 de la mission Sport, jeunesse et vie associative. Confiance medium.
- `ens_leasing` : **partielle**. Un leasing social de 50 000 véhicules existe en 2026, avec une enveloppe de 401 M€ financée par les CEE, hors budget ministériel. L'arrêté du 14/04/2026 est en vigueur jusqu'en 2031. Sources secondaires (presse), arrêté non lu. Confiance medium. Le classement des CEE en dépense publique n'a pas été vérifié.
- Reste : statut T1 de la ligne mère repris (absente).

## 6. Autres chiffreurs

- iFRAP : SNU −1,56 (2026), leasing −0,20. Aucune ligne sur les agents publics.
- OFCE (page Ensemble, `sources/T6/ofce_programmes_ensemble.html`) : il reprend les montants de Montaigne (3,6 ; 1,3) et ceux de la campagne (1,4 ; 0,1). Ce n'est pas une estimation propre : rien n'a été saisi.
- Asterès, La Grande Conversation : aucun chiffrage Ensemble (T6).

## 7. Sites inaccessibles

- institutmontaigne.org en direct : bloqué par Cloudflare, comme en T6. Tout a été lu sur web.archive.org (horodatages ci-dessus et dans `sources_ENS.csv`).
- PAP 2027 « Sport, jeunesse et vie associative » : non trouvé (une recherche web).
- Arrêté du 14/04/2026 sur le leasing social : non lu, cité via la presse.
