# Champ de la règle et consigne d'attribution

Texte repris tel quel de la consigne de la tâche (§ 1, puis § 3, étape 4).

## 1. Champ de la règle (fixé avant la recherche)

Ne pas le changer en cours de route. Un cas qu'il règle mal se signale dans le rapport, il ne se corrige pas.

Une mesure est **dans le champ** si, **à la date où elle est votée (cas passés) ou annoncée (programmes)**, l'un des deux critères est rempli :

- **J1, jurisprudence** : une décision antérieure du Conseil constitutionnel, du Conseil d'État, de la Cour de justice de l'Union européenne ou de la Cour européenne des droits de l'homme a déclaré contraire à la Constitution, au droit de l'Union ou à la Convention une disposition **de même nature**. Même nature : même mécanisme (par exemple, condition de nationalité ou de durée de résidence pour une prestation ; impôt qui traite différemment les résidents d'autres États membres) et même motif de censure (égalité, liberté d'établissement, droit de propriété…).
- **J2, le texte le dit** : le programme ou le projet fait lui-même dépendre la mesure d'une révision de la Constitution ou d'un changement de traité (par exemple « par référendum si nécessaire »).

**Hors champ** :

- une censure de procédure (cavalier législatif, « entonnoir », vice de forme) : elle ne dit rien de la mesure elle-même ;
- l'avis d'un chiffreur, d'un juriste ou d'un parti, sans décision J1 ni texte J2 ;
- une décision **postérieure** au vote ou à l'annonce : le champ se juge avec ce qui était connu à la date de la mesure, pas après coup ;
- une mesure qui dépend d'une négociation (budget européen, accord international) sans exiger un changement de traité : c'est un risque de mise en œuvre, pas un risque juridique.

## Consigne d'attribution (§ 3, étape 4)

4. **Attribution à l'aveugle** : un agent neuf, sans web, sur une copie de `aveugle/` hors du dépôt. Pour chaque cas passé et chaque ligne, il dit si la mesure est dans le champ (J1, J2, aucun) d'après le seul texte du § 1. Pour chaque ligne dans le champ, il choisit une famille existante ou en propose une nouvelle, définie par la nature juridique de la mesure (par exemple « prestation conditionnée à la nationalité »), sans connaître la règle qui y sera attachée. Il répond à `issue_connue` (`oui` s'il pense connaître l'issue d'un cas passé). Son fichier `attribution_agent.csv` (`fichier,id,critere,famille,famille_nouvelle,justification,issue_connue`) est conservé tel quel.
