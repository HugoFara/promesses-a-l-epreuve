# Contribuer à Promesses à l'épreuve

Merci de votre intérêt. Ce projet compare le coût annoncé de mesures budgétaires à leur coût réel, puis applique les écarts observés aux programmes des partis. Sa crédibilité tient à quelques règles, valables pour tous les contributeurs, humains ou agents.

## Signaler une erreur

- **Un chiffre du site vous semble faux** : ouvrez « Pourquoi ce chiffre ? » à côté de lui, puis « Contestez-le avec une source ». Le formulaire [« Contester un chiffre »](https://github.com/HugoFara/promesses-a-l-epreuve/issues/new?template=contester-un-chiffre.yml) exige une source et la page où lire la valeur. Une contestation n'est retenue qu'après relecture de cette source ; si elle est acceptée, elle apparaît dans le journal des corrections du site.
- **Un problème du site** (affichage, accessibilité, lien cassé) : ouvrez un ticket ordinaire.

Le traitement est le même que la demande vienne d'un particulier, d'un parti ou d'une équipe de campagne ; le formulaire demande seulement de le dire, par transparence.

## Les règles

1. **Aucun chiffre sans source lue.** Chaque valeur porte son URL, une citation courte, la page ou la section, et un niveau de confiance :
   - `high` : lu sur la source primaire (texte de loi, rapport officiel, publication de l'organisme lui-même) ;
   - `medium` : lu dans une source secondaire, avec la raison dans `note_confiance` ;
   - `low` : estimation ou source fragile.

   Une valeur calculée est marquée comme telle (`source_type = calcul`, ou une note qui donne le calcul). Un chiffre introuvable s'écrit « non trouvé », jamais de mémoire.
2. **Traitement symétrique.** Une règle de correction s'applique à toute mesure du même type, quel que soit le parti. Chaque ligne de programme déclare sa famille (`data/raw/familles.csv`, par exemple « accise sur l'électricité ») et reçoit la règle de cette famille, sauf écart expliqué dans `exception_symetrie`. `scripts/garde_fous.py` le vérifie. Une nouvelle application est relue par quelqu'un qui n'a pas produit le chiffrage.
3. **Séparer les faits des préférences.** Ce qui relève d'un choix politique (par exemple un déficit voulu pour investir) est dans une colonne à part, jamais mêlé au solde.
4. **Pas de double compte avec la référence.** Une mesure déjà votée ou déjà inscrite au budget 2027 n'est comptée que pour la part qui n'y est pas (`statut_reference`, `facteur_reference`).
5. **Garder l'historique.** Toute modification d'une valeur existante est inscrite dans `data/raw/historique.csv` : date, fichier, ligne, colonne, ancienne valeur, nouvelle, raison, source. Utiliser `scripts/appliquer_corrections.py`, qui refuse une correction si la valeur actuelle ne correspond pas à l'ancienne annoncée. Ce fichier est publié sur le site (« Journal des corrections »).
6. **N'éditer que `data/raw/`.** Les fichiers de `data/*.csv` sont générés par le pipeline.
7. **Aucun chiffre en dur dans le site.** Tout ce que `web/` affiche vient des CSV de `data/`.

## Règles de présentation

Elles visent un site qui ne prend pas parti :

- **Pas de verdict** (« financé », « non financé ») : on montre le solde, sa fourchette et la part des corrections qui repose sur une règle confirmée.
- **Pas de version « corrigée » d'un programme.** Réduire une mesure ou ajouter une recette pour améliorer un solde est un choix parmi d'autres, qui revient aux partis et aux électeurs.
- **Ordre neutre.** Partis, programmes et scénarios sont rangés par ordre alphabétique, jamais par résultat. Même formulaire et même fiche pour tous.
- **Dire les limites.** Les résultats défavorables à la méthode sont publiés au même titre que les autres.
- **Accessibilité.** Le site vise le niveau WCAG 2.2 AA ; `scripts/test_web.py` lance axe-core sur chaque vue.

## Travailler sur le code

```bash
pip install -r requirements.txt -r requirements-web.txt
playwright install chromium
TEST_WEB_STRICT=1 bash scripts/run_all.sh
```

Tout doit afficher OK et « garde-fous : 0 erreur(s), 0 alerte(s) ». Le contrôle du site tourne en CI avec d'autres polices qu'en local : un débordement peut n'apparaître qu'en CI.

- **Messages de commit** : [conventional commits](https://www.conventionalcommits.org/fr/), en français (`feat(web): …`, `fix: …`, `docs: …`).
- **Publication** : chaque push sur `main` dont les contrôles passent met le site en ligne (GitHub Pages). Passer par une branche et une demande de fusion.

## Licence

En contribuant, vous acceptez que votre contribution soit publiée sous la licence MIT pour le code et CC BY 4.0 pour les données et les textes (voir `README.md`).
