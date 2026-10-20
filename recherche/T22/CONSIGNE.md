# T22 : découper les lignes « Autres » des programmes 2024

Consigne préparée le 20/10/2026 (issue #6). Lire d'abord `recherche/CONSIGNES.md` (règles communes ; date d'accès : celle du jour), puis `recherche/T6/rapport.md` (NFP et Ensemble), `recherche/T17/rapport.md` (RN), `recherche/T1/rapport.md` (statut par rapport à la référence 2027) et `recherche/T18/CONSIGNE.md` (attribution à l'aveugle, reprise ici).

## Pourquoi

Les lignes de famille `residu` de `data/raw/application_lignes.csv` reprennent le chiffrage de l'institut sans le tester (règle « Aucune ») :

| Ligne | Montant (Md€, Montaigne) | Contenu annoncé |
|---|---|---|
| `nfp_autres_dep` | −162,7 | point d'indice, SMIC, gel des prix, indexations, gratuités, culture… |
| `nfp_autres_rec` | +18,6 | TTF, cotisations retraite… |
| `rn24_autres_dep` | −21,05 | PTZ 3e enfant, enseignants, transmissions d'entreprises, IR des moins de 30 ans, prisons… |
| `ens_autres_dep` | −11,7 | SNU, agents publics, leasing social, santé, éducation… |
| `rn24_autres_eco` | +1,3 | asile, allocations familiales des parents de mineurs récidivistes |

La ligne NFP est la plus grosse somme non corrigée du site. Tant qu'elle n'est pas découpée, aucune règle ne peut s'appliquer aux mesures qu'elle contient, et la comparaison entre programmes en dépend. `rn24_autres_eco` est sous le seuil de 5 Md€ de l'issue ; elle est traitée quand même, pour que la même règle s'applique à toutes les lignes de famille `residu`.

Cette tâche découpe sans rien calculer : chaque montant vient d'un chiffreur publié. Le résultat peut faire monter ou baisser le coût corrigé de n'importe quel programme ; il est publié pareil.

## 0. Gel

| Élément | Valeur |
|---|---|
| Commit | `e17e777` |
| `data/raw/application_lignes.csv` (sha256) | `6b13f3ffa8a32ca9a092cf577812ffd365c5c1641a5607440170f0a471084b84` |
| `data/raw/familles.csv` (sha256) | `0a32a511404b16a993860f8afaff8c37de5bbd049e2b1e86f79141ef05479932` |
| `data/raw/regles.csv` (sha256) | `bfb4df1bb2c63128642ea68c42a2e69b27cc7d1dbe9d0e9f54f033854aef6074` |
| `data/raw/chiffrages_instituts.csv` (sha256) | `ed27d45230a50d2b7245631cd08caf5ddb7e2da8c2658470a3245d95a32747d7` |

## 1. Règle de découpage (la même pour les cinq lignes)

Elle est fixée avant la collecte. Ne pas la changer en cours de route ; un cas qu'elle règle mal est signalé dans le rapport, pas corrigé.

1. **Chiffreur de référence** : celui de la ligne (`source_independant`, Institut Montaigne pour les cinq). Les montants des lignes découpées sont les siens, lus dans ses publications (synthèse, fiches mesures, tableaux), pour le même horizon que la ligne mère.
2. **Seuil** : est découpée en ligne propre toute mesure à laquelle le chiffreur de référence donne un montant publié d'au moins **1 Md€** en valeur absolue. Les mesures plus petites, non chiffrées ou chiffrées seulement en groupe restent dans le reste.
3. **Une mesure, une ligne** : un montant publié pour un groupe de mesures (« gratuités : 7,6 ») devient une ligne seulement si le chiffreur ne le détaille pas ; le libellé dit alors que c'est un groupe. Ne jamais répartir un montant de groupe entre mesures.
4. **Reste** : chaque ligne mère garde une ligne « Autres » égale au montant de la ligne mère moins la somme des lignes découpées. Le total de la ligne mère ne change pas, même quand les postes listés par le chiffreur ne retombent pas dessus (cas connu : RN, postes listés 33,46 pour un résidu de 21,05, voir `recherche/T17/rapport.md` § 3). Le bandeau fait foi, comme en T6 et T17 ; le reste peut donc être négatif. Le signaler, ne pas le corriger.
5. **Autres chiffreurs** : pour chaque ligne découpée, relever le montant des autres chiffreurs (iFRAP, Asterès, OFCE, La Grande Conversation…) sur le même périmètre, s'il est publié. Ils servent à la fourchette entre chiffreurs, pas au découpage : une mesure que seul l'iFRAP chiffre au-dessus de 1 Md€ reste dans le reste.
6. **Doublons** : vérifier qu'aucune ligne découpée ne recouvre une ligne déjà isolée du même programme (par exemple `nfp_retraites`, qui comprend le minimum contributif au SMIC). En cas de recouvrement, ne pas découper et l'écrire.

## 2. Ce que l'on relève pour chaque ligne découpée

- Libellé, type (`Dépense`, `Recette`, `Économie`), montant (Md€/an, signe du solde : négatif = creuse le déficit), horizon, citation exacte, URL, page ou section, confiance.
- **Statut par rapport à la référence 2027**, avec la méthode de `recherche/T1/rapport.md` : `absente`, `partielle`, `proposée` ou `votée` (valeurs de `recherche/T1/statut_reference.csv`), et sa source. Exemple de question : une hausse du point d'indice est-elle déjà en partie dans la référence ? « Non trouvé » est une réponse admise.
- Pas de famille ni de règle : elles sont attribuées à l'aveugle (§ 3, étape 3).

Les sites de Montaigne sont souvent bloqués (Cloudflare) : passer par web.archive.org, en notant l'horodatage de l'archive. Réutiliser les archives de `sources/T6/` et `sources/T17/` quand elles couvrent la page ; ne pas les recopier, les citer.

## 3. Déroulé

1. **Collecte** : trois agents en parallèle, un par programme (NFP : `nfp_autres_dep` et `nfp_autres_rec` ; RN : `rn24_autres_dep` et `rn24_autres_eco` ; Ensemble : `ens_autres_dep`), chacun dans `recherche/T22/parts/` (`lignes_<P>.csv`, `autres_chiffreurs_<P>.csv`, `notes_<P>.md`, `sources_<P>.csv`), sources dans `sources/T22/<P>/`. Même grille de lecture pour les trois : la synthèse du chiffreur de référence, puis chaque fiche mesure qu'elle cite.
2. **Fusion** : un agent fusionne, contrôle doublons et sha256, recalcule les restes, vérifie que chaque ligne mère retombe sur son montant (tolérance 0,05 Md€), produit `aveugle/`.
3. **Attribution à l'aveugle** : un agent neuf, sans web, sur une copie de `aveugle/` hors du dépôt. Il reçoit, pour chaque ligne découpée, le libellé, le type et le montant, **sans le programme ni le parti**, et la liste des familles (`familles.csv` : famille, libellé, justification). Il choisit une famille par ligne, ou propose une famille nouvelle avec son champ, sans connaître la règle qui y est attachée. Son fichier est conservé tel quel.
4. **Intégration** : hors tâche.

## 4. Livrables (dans `recherche/T22/`)

- `lignes_decoupees.csv` : `id_mere,id,programme,ligne,type,montant,horizon,chiffreur,url,citation,page,confiance,statut_reference,source_reference,note` (une ligne par mesure découpée, plus une ligne « Autres » par ligne mère, avec `citation` vide et `note` = calcul du reste) ;
- `autres_chiffreurs.csv` : format de `data/raw/chiffrages_instituts.csv` (`id_ligne` = id proposé) ;
- `controle_totaux.csv` : `id_mere,montant_mere,somme_decoupees,reste,ecart_postes_listes` ;
- `aveugle/` (`lignes.csv`, `familles.csv`, `consigne.md`), `attribution_agent.csv` (`id,famille,famille_nouvelle,justification,issue_connue`) ;
- `parts/`, `sources.csv`, `rapport.md` : par programme, ce qui a été découpé, ce qui reste et pourquoi (sous le seuil, non chiffré, groupe), les recouvrements évités, les écarts internes du chiffreur, et les décisions laissées à l'intégrateur.

## 5. Critère de réussite, fixé à l'avance

- Pour chaque ligne mère : toutes les mesures chiffrées à 1 Md€ ou plus par le chiffreur de référence sont découpées, ou leur absence est expliquée (source introuvable, recouvrement) ;
- chaque ligne mère retombe sur son montant de départ (`controle_totaux.csv`) ;
- le rapport donne, pour chaque programme, la part de la ligne mère encore dans le reste.

## 6. Pour l'intégrateur (rappel, hors tâche)

- Les totaux « indépendant » des programmes ne changent pas (`scripts/check_regression.py`) ; les totaux corrigés peuvent changer, puisque des règles s'appliquent aux lignes découpées.
- Une famille nouvelle proposée par l'agent d'attribution reçoit sa règle d'après `regles.csv`, la même pour tous les partis ; `garde_fous.py` le vérifie.
- Chaque ligne découpée et chaque reste entre dans `historique.csv` ; la page « Journal des corrections » trace le découpage.
