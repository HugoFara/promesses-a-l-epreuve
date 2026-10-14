# Validation de la méthode : protocole

**Question.** Notre chiffrage corrigé (chiffrage de départ × facteur de la règle) est-il plus proche du coût réalisé que le chiffrage de départ ? C'est l'indicateur de confiance de la méthode, règle par règle.

**Échantillon.** 25 chiffrages officiels avant adoption (couche 1), 10 effets annoncés chiffrables, 22 chiffrages d'instituts sur les programmes Macron 2017 et 2022 (T10b).

**Attribution à l'aveugle.** Un agent séparé a reçu une copie isolée de `aveugle/` (libellé de la mesure, année, sens, chiffrage annoncé, auteur ; liste des règles et de leur champ), sans le réalisé ni la cause de l'écart, avec consigne de choisir la règle d'après la seule nature de la mesure. Son fichier est conservé tel quel (`attribution_agent.csv`, copié dans `data/raw/validation_attribution.csv`) ; aucune attribution n'a été retouchée après coup, y compris les cas limites qu'il signale (CIR et CITE en « Taux de recours », boucliers énergie en « Aucune »…).

**Limite principale.** L'agent reconnaissait l'issue de 60 cas sur 83 (colonne `issue_connue`). Le test n'est donc aveugle qu'en intention. Les 23 cas « issue inconnue » sont presque tous des coûts mécaniques (facteur 1) : ils ne testent pas la méthode.

**Circularité.** Deux paramètres sont calibrés sur des mesures de l'échantillon : `facteur_reforme` (retraites 2010 et 2023) et `ratio_effet_promis` (CICE, TEPA, ISF, PFU). Pour ces mesures, le facteur est recalculé sans elles (leave-one-out). L'élasticité du capital (0,77) a été estimée sur 2008-2017 : le PFU de 2018 est hors échantillon.

**Statuts** (`data/validation_regles.csv`) : confirmée (plus d'améliorations que de dégradations et erreur médiane réduite), contredite (l'inverse), mitigée, non concluante (réalisés qui ne sont pas des observations), non testée.

Code : `scripts/validation.py`. Sorties : `data/validation_mesures.csv`, `validation_resume.csv`, `validation_regles.csv`, `confiance_programmes.csv`.
