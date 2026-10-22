# T24, partie B : notes de l'agent

Date : 22/10/2026. Gel : commit `2c0948c`. Les sha256 de `data/raw/application_lignes.csv` (`efc51b91…`) et de `chiffrages_instituts.csv` (`62c8bc03…`) ont été vérifiés : ils sont identiques à ceux de la consigne. Périmètre : les 88 lignes 2024, sans `nfp_asile`.

Fichiers :

- `lignes_agent.csv` : une ligne par id, dans l'ordre du fichier source ;
- `sources_agent.csv` : 9 fichiers nouveaux, archivés dans `sources/T24/agent/`. Les sources déjà archivées (T6, T17, T20, T22) sont citées par leur chemin, sans copie.

## 1. Méthode

1. Pour chaque ligne, j'ai lu le texte du chiffreur dont le montant est retenu :
   - Montaigne : fiches, synthèses Wayback, PDF des micro-chiffrages NFP et RN (`sources/T20/integration/`) ;
   - iFRAP : pages et tableaux (`sources/T6`, `sources/T17`).

   J'ai noté la disposition sur laquelle porte le calcul.
2. Quand le calcul porte sur une disposition existante (abroger, maintenir, rehausser, remplacer, prolonger), j'ai établi son état au 30/06/2024 sur une source datée :
   - Légifrance (JORF), lu via Wayback (`id_`), car le site renvoie un 403 Cloudflare à curl ;
   - décision du Conseil constitutionnel ;
   - programme de stabilité 2024-2027 (PStab, DG Trésor, avril 2024, archivé) ;
   - Voies et moyens, tomes I et II, déjà archivés en T20.
3. Lignes de mesure entièrement nouvelle : `critere = aucun`, avec le motif « mesure nouvelle ». Ces lignes reçoivent `etat = sans objet`. La valeur `en vigueur` est réservée aux lignes dont le calcul part d'un paramètre ou d'un dispositif existant.

Confiance :

- `high` : état lu sur source primaire datée (JORF, décision, PStab, Voies et moyens) ;
- `medium` : état lu dans le texte du chiffreur (juin 2024) ou dans une source officielle datée d'une autre année ;
- `low` : `rn24_prisons`, texte de programmation non lu.

## 2. Lignes concernées

### `rn24_chomage` : R3, part concernée 4,5 Md€ (confiance medium)

- **Ce que suppose le montant.** Le −4,5 est l'économie de la réforme de l'assurance chômage de juillet 2024, reprise de la fiche Ensemble de Montaigne. L'annuler ne coûte que si la réforme est dans la référence.
- **État au 30/06/2024 : pas encore adoptée.** Le décret de réforme n'a jamais été publié. Le décret n° 2024-648 du 30/06/2024 (JORF n° 0154 du 01/07/2024) prolonge les règles du décret n° 2019-797 jusqu'au 31/07/2024. Sa notice dit : « le texte prolonge les dispositions réglementaires relatives aux règles d'indemnisation du régime d'assurance chômage jusqu'au 31 juillet 2024 ». Archive : `sources/T24/agent/wb_decret_2024-648.html`.
- **Ce que dit le PStab d'avril 2024.**
  - Encadré 7, p. 38 : « La prévision intègre deux réformes structurelles majeures », c'est-à-dire les retraites 2023 et la contracyclicité (décret du 31/01/2023, 4,2 Md€ en régime de croisière). Puis : « De plus, une nouvelle réforme de l'assurance chômage a été annoncée afin de contribuer à l'atteinte du plein emploi à horizon 2027 ». Aucun montant.
  - Scénario macroéconomique 2026-2027, p. 13 : parmi les mesures qui soutiennent l'emploi, « réforme de l'assurance chômage annoncée pour 2024 ».
  - Tableau 7 (p. 41) et texte sur le solde des administrations de sécurité sociale (p. 30, « réformes structurelles déjà mises en place ») : aucune trace chiffrée.
- **Ce que disent les chiffreurs.**
  - Montaigne : « la réforme, qui n'est pas entrée en vigueur, n'est pas intégrée dans le tendanciel » (fiche Ensemble). Et dans la synthèse RN : « Revenir sur cette réforme, comme le proposent le RN et le NFP, ne coûte donc rien ».
  - iFRAP, en sens inverse : « déjà inscrites au budget […] la réforme de l'indemnisation chômage au 1er juillet (génératrice de 4,4 milliards d'économies) ». Mais son tableau la compte quand même.
- **Lecture retenue : R3.** La réforme n'était pas adoptée. Le PStab ne l'intègre pas dans sa prévision chiffrée : il la distingue explicitement des deux réformes qu'il dit intégrer. Réserve : la mention qualitative dans le scénario d'emploi peut être lue comme une présence dans la trajectoire. C'est le seul point d'interprétation de la tâche ; il revient à l'intégrateur.

## 3. Conséquence de symétrie (à trancher ensemble)

La même disposition apparaît dans trois programmes, sous une même référence obligatoire :

| Ligne | Traitement actuel | Si la réforme est absente de la référence (R3) | Si elle est dans la référence |
|---|---|---|---|
| `ens_chomage` (+4,5) | facteur 0, « Déjà dans la référence » | mesure nouvelle, +4,5 compté | inchangé (0) |
| `rn24_chomage` (−4,5) | −4,5 compté | 0 (comme Montaigne) | inchangé (−4,5) |
| NFP, « Abroger […] les réformes de l'assurance-chômage » | 0, dans `nfp_autres_dep_reste` (Montaigne : « ne chiffrer que les mesures déjà en application ») | inchangé (0) | il faudrait −4,5 pour le NFP aussi |

Aujourd'hui, le site est incohérent dans les deux lectures : il retient la réforme dans la référence pour Ensemble et RN, mais pas pour le NFP. Quelle que soit la décision, les trois lignes doivent suivre la même règle.

## 4. Cas limites (pas concernés, mais notés)

- **Régimes temporaires en vigueur au 30/06/2024, avec une échéance votée :**
  - `ens_elec` et `nfp_taxe_macron` : accise sur l'électricité au tarif dérogatoire, art. 92 LFI 2024, « entre le 1er février 2024 et le 31 janvier 2025 ». Le PStab prévoit un « rétablissement complet prévu en février 2025 » (p. 20). La référence contient donc le tarif normal : maintenir le taux réduit ou abolir la hausse coûte. Aucun critère. Pour `nfp_taxe_macron`, Montaigne chiffre lui-même à partir du PStab (p. 21) et suppose que la « dernière partie du chemin » n'est pas faite.
  - `rn24_rente_infra` : contribution sur les rentes inframarginales, prorogée du 01/01/2024 au 31/12/2024 par l'art. 80 LFI 2024. Elle est en vigueur au 30/06/2024, donc pas de R2. Mais elle expire fin 2024 ; sa prolongation en 2025 n'a été votée qu'en LFI 2025. Une « hausse » en 2025-2027 revient donc à créer une taxe sur une base de référence nulle. De plus, le PStab inscrit en 2024 « Mesures fiscales énergéticiens et autres mesures sur les rentes 3,0 » (tableau 7, p. 41) : ces mesures sont annoncées, non votées, mais déjà dans la trajectoire. Si la « hausse de la taxe sur les énergéticiens (3 milliards) » du RN est la même mesure, c'est un double compte avec la référence, du type `ens_chomage`. Cela relève d'une autre règle que R1-R3. L'iFRAP ne publie pas de méthode.
- **Dispositions votées, pas encore en vigueur, et dans la trajectoire :** `rn24_production`. La baisse de la CVAE est votée par l'art. 79 LFI 2024 (taux 2024, 2025, 2026) et figure dans le PStab. Le montant retenu (5,1) est le rendement de la C3S, en vigueur : la partie CVAE n'est pas comptée. Aucun critère.
- **Réformes des retraites (`nfp_retraites`, `rn24_retraites`) : aucun critère.** Les calculs Montaigne portent sur l'âge et la durée (art. 10 LFRSS 2023, réformes 2003, 2010, 2014). La décision 2023-849 DC déclare conformes ces mots de l'article L. 161-17-2. Elle censure les art. 2, 3, 6, 10-III-6° et XXVIII, 17-III-A-7° et 27, qui n'entrent dans aucun des deux calculs.
- **Rétablissement de dispositions abrogées :**
  - `rn24_autres_dep_reste` : demi-part des veufs (0,5) et loi Ciotti (« marginal ») ;
  - `nfp_gul` : GUL de la loi ALUR, jamais appliquée.

  Le coût est compté en entier, comme celui d'une mesure nouvelle. Le montant ne suppose pas que la disposition existe encore : ce n'est pas un R2.
- **`rn24_preference_nationale` :** mesure proche de l'art. 19 censuré de la loi 2024-42. Mais la ligne crée la condition, elle ne l'abroge pas : le calcul porte sur les AF et le RSA en vigueur. Le risque juridique relève de T23, hors champ.
- **Double compte possible avec la référence (hors R1-R3, signalé seulement) :**
  - `rn24_prisons` : Montaigne chiffre 12 000 places du « plan 15 000 places », déjà programmé ; texte de programmation non lu ;
  - `ens_autres_dep_reste` : l'iFRAP dit fauteuils roulants et remplacements « déjà inscrits au budget » ; non vérifié dans le PStab.
- **`ens_leasing` :** Montaigne compte le coût total (2 × 650 M€). Il ne suppose donc pas que l'opération de début 2024 se poursuit. Aucun critère. Je n'ai pas lu de source primaire sur la clôture de l'opération.

## 5. Ce qui n'a pas été trouvé ou lu

- **Légifrance, version consolidée « à date » des codes** (CGI art. 200 A, 235 ter ZD, 779, 784, 964 ; CCH L. 442-2-1 ; CASF L. 251-1 ; CSS L. 161-25) : curl reçoit un 403 Cloudflare, et je n'ai pas les identifiants LEGIARTI pour passer par Wayback. Les états de ces dispositions sont pris :
  - soit dans des documents officiels datés : Voies et moyens I (PLF 2026, recettes 2024 constatées) et II (PLF 2025, « fin du fait générateur : non borné ») ; amendement du Gouvernement II-3232 au PLF 2023 pour la RLS ;
  - soit dans la description du chiffreur, datée de juin 2024. Confiance `medium` dans ce cas.

  Aucune de ces dispositions n'est un cas douteux : il s'agit d'impôts et de prestations permanents.
- **Avis du HCFP sur le PStab 2024** : cherché par WebSearch (« avis 2024-2 », assurance chômage), sans résultat utile. Il aurait pu dire si la réforme chômage est intégrée à la prévision.
- **Programmation des 15 000 places de prison** (loi d'orientation et de programmation Justice 2023-2027) : non lue.
- **Clôture du leasing social 2024** : non lue sur source primaire. Sans effet sur le critère.
- **Fiche Montaigne propre à `rn24_asile`** : absente du PDF RN et de la synthèse, comme déjà noté en T22. La fiche 2022 chiffre un durcissement nouveau.

## 6. Points pour l'intégrateur

1. Décider la lecture du PStab sur la réforme chômage 2024. Cela fixe ensemble `ens_chomage`, `rn24_chomage` et l'abrogation NFP (voir § 3).
   - Si R3 est retenu : `rn24_chomage` passe à 0 et `ens_chomage` est compté +4,5. Cela inverse la règle « Déjà dans la référence » actuelle. Montaigne et la consigne T24 (cas de `ens_chomage`) n'ont pas la même convention : le choix doit être écrit dans la méthode.
2. `rn24_rente_infra` : vérifier si la mesure RN recoupe les « mesures fiscales énergéticiens » (3,0) inscrites dans le PStab. C'est une question de double compte, pas de R1-R3.
3. `rn24_prisons` : lire la programmation du plan 15 000 places, pour un éventuel double compte avec la référence.
4. Les autres lignes 2024 (86) ne reposent sur aucune disposition censurée, abrogée, expirée ou non adoptée au 30/06/2024.
