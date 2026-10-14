# Audit d'accessibilité du site public (web/index.html)

14 octobre 2026. Référentiel : WCAG 2.2, niveaux A et AA (base du RGAA 4.1), plus les bonnes pratiques d'axe-core.

## Méthode

1. **Contrôle automatique** : axe-core 4.10.3 (copié dans `scripts/vendor/`, intégrité vérifiée contre le registre npm). Il est lancé sur les 8 vues et la page introuvable, sur écran large (1280 px) et téléphone (390 px), en thème clair et sombre, avec tous les accordéons ouverts. Il couvre aussi la fenêtre « Pourquoi ce chiffre ? », le panneau Affichage et le menu mobile.
2. **Clavier** : parcours complet à la touche Tab (ordre, focus visible), flèches dans les groupes de boutons radio, fenêtre de dialogue (focus à l'ouverture, focus piégé, Échap, retour au bouton d'origine).
3. **Lecteur d'écran** : lecture de l'arbre d'accessibilité de Chromium (ce que reçoivent NVDA, JAWS, VoiceOver ou Orca) pour les vues Programmes, Foyer et Hier : noms, rôles, titres, listes, graphiques.
4. **Adaptation de l'affichage** : largeur de 320 px (équivalent d'un zoom à 400 %, critère 1.4.10), texte « très grand », espacement du texte imposé (critère 1.4.12 : interligne 1,5, lettres 0,12 em, mots 0,16 em, paragraphes 2 em), à 320 et 1 280 px.

## Résultats et corrections

| Constat | Critère | Correction |
|---|---|---|
| Tableaux plus larges que l'écran (surtout sur téléphone) impossibles à faire défiler au clavier | 2.1.1 | Le cadre d'un tableau qui défile devient atteignable (`tabindex="0"`), nommé (« Tableau défilant : … ») et a un focus visible. Les tableaux qui tiennent dans l'écran restent hors de l'ordre de tabulation ; l'état est recalculé à l'affichage, au redimensionnement et à l'ouverture d'un accordéon |
| Liens « avant » / « après » de la colonne Sources : 20 px de haut | 2.5.8 | Liens des tableaux d'au moins 24 px de haut |
| Bandeau « Site d'étude indépendant » hors de toute zone de repère | bonne pratique | `<aside aria-label="Avertissement">` |
| Boutons « Pourquoi ce chiffre ? » des cartes : même nom pour tous les programmes et scénarios | 2.4.6, 4.1.2 | Nom accessible complété : « Pourquoi ce chiffre ? (total : NFP 2024 (LFI)) ». Il commence par le texte visible (2.5.3). Les boutons des lignes avaient déjà un nom propre |
| Séparateur « › » du fil d'Ariane et « + » / « − » des accordéons lus à voix haute | 1.1.1 | Contenu CSS avec texte alternatif vide (`content: "›" / ""`), avec une déclaration de repli pour les navigateurs anciens |
| Résultats du simulateur « Mon foyer » lus comme un bloc continu | 1.3.1 | Liste « Effet de chaque mesure », une entrée par mesure |
| Légendes des graphiques sans nom | 1.3.1 | Listes nommées « Légende » |
| Badge « Sous-estimé (surprise positive) » qui déborde de 2 px à 320 px avec l'espacement imposé | 1.4.12 | Les badges passent à la ligne sur petit écran |

## Ce qui était déjà conforme

- **Contraste** : aucune erreur, en thème clair comme en thème sombre (critère 1.4.3).
- **Langue, titres, structure** : `lang="fr"`, un `h1` par vue, des niveaux de titre sans saut, et des zones de repère (en-tête, navigation, contenu, pied de page). Un lien d'évitement mène au contenu. Le titre de la page change avec la vue.
- **Clavier** : l'ordre de tabulation suit l'ordre visuel, et le focus est visible sur chaque élément. Les choix sont de vrais boutons radio : les flèches les parcourent. La fenêtre est une `<dialog>` modale native : le focus y entre à l'ouverture, y reste piégé, et revient sur le bouton d'origine après Échap.
- **Graphiques** : chacun est une image nommée par une phrase qui en donne le résultat. Il est doublé d'un tableau de données, et la couleur n'est jamais seule à porter l'information (signes, libellés, légendes).
- **Formulaires** : chaque champ a une étiquette, et chaque groupe de boutons a une légende (`fieldset` / `legend`). Les résultats sont annoncés par une zone `aria-live="polite"`.
- **Préférences** : la taille du texte est réglable, les animations sont coupées si `prefers-reduced-motion` est actif, et le thème sombre suit le système.

## Contrôle continu

`scripts/test_web.py` (lancé par `run_all.sh` et en CI) lance axe-core sur chaque vue, aux deux tailles d'écran et dans les deux thèmes, ainsi que sur la fenêtre « Pourquoi ce chiffre ? ». Le test échoue au premier défaut relevé. Un défaut injecté à la main (un bouton sans nom) est bien détecté.

## Limites

- **Lecteurs d'écran** : aucun test avec un vrai lecteur d'écran (NVDA, JAWS, VoiceOver, TalkBack), seulement l'arbre d'accessibilité de Chromium. Un test avec un vrai lecteur reste à faire, idéalement avec des utilisateurs, en même temps que le test avec des novices (recommandation 2).
- **Navigateurs** : contrôles faits dans Chromium seulement ; Firefox et Safari ne sont pas testés.
- **Automatique contre manuel** : axe-core détecte environ un tiers à la moitié des défauts possibles. La compréhension des textes, la pertinence des noms des graphiques et la charge cognitive ont été relues, sans être mesurées.
- **Graphiques SVG** : leur nom résume le résultat, mais on ne peut pas les parcourir point par point. Le tableau de données qui les accompagne est la version accessible complète.
- **Tableau de bord complet** (`web/complet.html`, pour spécialistes) : non audité.
