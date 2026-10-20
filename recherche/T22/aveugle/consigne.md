# Attribution des familles à l'aveugle

Tu travailles seul, sans accès au web, sur une copie de ce dossier. Tu n'as pas besoin d'autres fichiers que ceux-ci :

- `lignes.csv` : 39 mesures budgétaires tirées de programmes politiques français, chiffrées par un institut. Colonnes : `id_aveugle`, `ligne` (libellé de la mesure), `type` (`Dépense`, `Recette` ou `Économie`), `montant` (Md€ par an, en impact sur le solde public : négatif = creuse le déficit ; une baisse d'impôt est donc une `Recette` de montant négatif).
- `familles.csv` : les familles de mesures disponibles. Colonnes : `famille` (identifiant), `libelle`, `champ` (précision sur le champ, quand il y en a une).

## Ce que tu fais

1. Pour chaque ligne de `lignes.csv`, choisis **une seule famille** de `familles.csv`, d'après **la seule nature de la mesure** (ce qu'elle change : une prestation, un impôt, une rémunération publique, un prix…). Le montant, le parti ou l'opportunité de la mesure n'entrent pas dans le choix.
2. Si aucune famille ne convient, **propose une famille nouvelle** : un identifiant court en minuscules avec des tirets bas (par exemple `nom_de_famille`) et son champ en une phrase (quelles mesures elle couvre). Une même famille nouvelle peut servir à plusieurs lignes ; garde alors le même identifiant et le même champ.
3. Un libellé qui commence par « Groupe : » désigne un montant publié pour plusieurs mesures ensemble, non détaillé. Choisis la famille qui convient au groupe pris comme un tout, ou propose-en une.
4. Écris une **justification d'une phrase** par ligne.
5. Réponds honnêtement à `issue_connue` : `oui` si tu sais (ou crois savoir) de quel parti ou de quel programme vient la mesure, `non` sinon. Cette colonne ne juge pas ta réponse : elle mesure si le test est vraiment aveugle.

Ne cherche pas à deviner une règle de calcul attachée aux familles : il n'y en a aucune dans ce dossier, et ton choix ne doit pas en dépendre.

## Format de sortie

Un fichier `attribution_agent.csv` (UTF-8, virgule, une ligne par `id_aveugle`, les 39 lignes, dans l'ordre de `lignes.csv`) :

```
id_aveugle,famille,famille_nouvelle,justification,issue_connue
```

- `famille` : l'identifiant choisi dans `familles.csv`, ou l'identifiant de la famille nouvelle que tu proposes ;
- `famille_nouvelle` : vide si la famille existe dans `familles.csv` ; sinon, le champ de la famille proposée (une phrase) ;
- `justification` : une phrase ;
- `issue_connue` : `oui` ou `non`.

Mets entre guillemets les champs qui contiennent une virgule. Ne modifie pas `lignes.csv` ni `familles.csv`. Ton fichier sera conservé tel quel : aucune attribution ne sera retouchée après coup.
