# Contrôle qualité transversal — 30 matchs — 11 octobre 2026

## Objet et niveau de garantie

Corpus : `matchs/niveau-1/match-01.md` à `match-10.md`, `matchs/niveau-2/match-11.md` à `match-20.md` et `matchs/niveau-3/match-21.md` à `match-30.md`, sur `main`.

**CONCLUSION : contrôle structurel passé ; certification factuelle intégrale NON acquise.** Le projet comporte **30 × 96 = 2 880 questions**, accompagnées de réponses, sous réserve de la validité du format retenu. La présence des réponses est contrôlée ; cela ne démontre pas leur véracité. Ne pas diffuser ces jeux comme « sans erreur » ou « sans doublon » avant la validation documentaire complète.

## Tests exécutés

1. **Structure** : lecture des 30 Markdown ; les dix matchs de chacun des trois niveaux comportent **96 marques de questions et 20 rubriques** chacun. Les Matchs 01–20 disposent de 96 réponses chacun lors des contrôles détaillés. Les Matchs 21–30 ont aussi été validés à 96 Q/R dans le contrôle précédent de la même livraison.
2. **Cantonades** : test sur les 60 cantonades (rubriques 6 et 16) ; recherche de toute réponse des Q2–Q5 déjà écrite littéralement dans la question Q1, après normalisation des accents et de la ponctuation. **0 occurrence résiduelle détectée** après les corrections (dont une correction complémentaire au Match 26 sur Radama Ier).
3. **Doublons** : rapprochement des réponses normalisées dans les trois niveaux. De nombreuses reprises ont été identifiées au cours des passes d'audit et plusieurs ont été corrigées. Les premières analyses du Niveau 1 ont signalé des reprises exactes : Johannes Kepler, Angélique Kidjo, Bichkek, etc. Une consultation ultérieure des versions courantes a constaté que les formulations précédemment signalées n'étaient plus présentes aux emplacements concernés. L'absence de doublon textuel n'implique pas l'absence de doublon sémantique.
4. **Contrôles factuels ciblés** : l'identité et les principales dates de Mary Somerville (1780, Jedburgh ; 1872, Naples) ont été recoupées avec la Royal Astronomical Society et MacTutor. Ce contrôle porte sur des faits ciblés et ne constitue pas une vérification de toutes les réponses.
5. **Identification** : les Matchs 21–30 disposent des quatre indices de 40/30/20/10 points ; leur progression est plus travaillée que celle du format précédent. Leur exactitude et caractère véritablement discriminant restent à valider individuellement avec une preuve de chaque assertion.

## Sources consultées dans la présente revue

- Royal Astronomical Society, Mary Somerville : https://ras.ac.uk/news-and-press/news/mary-somerville-features-google-doodle
- MacTutor, université de Saint Andrews, Mary Somerville : https://mathshistory.st-andrews.ac.uk/Biographies/Somerville/
- Les fichiers individuels `sources/match-NN-sources.md` fournissent d'autres points de départ. **La présence de liens ne prouve pas à elle seule qu'ils soutiennent chaque affirmation.**

## Risques restant ouverts — à traiter avant la compétition

- **Priorité critique :** vérifier **une par une les 2 880 associations Q/R** contre des références vérifiables, avec source exacte, ambiguïté, variantes acceptées et décision d'arbitrage.
- Faire un contrôle sémantique transversal des questions, non limité à la même réponse orthographiée pareil, et exclure les répétitions de faits entre niveaux.
- Corriger les erreurs historiques, scientifiques et sportives restantes ; l'étiquette « noms propres » doit être recalculée après toutes les réécritures.
- Auditer les **60 cantonades** au-delà du seul dévoilement littéral (une réponse peut être révélée indirectement).
- Pour les **30 identifications**, vérifier chaque indice séparément et calibrer la difficulté (40, 30, 20, 10 points).
- Préparer une version arbitre avec graphies équivalentes et cas de réponses multiples.

## Décision

| Critère | Statut |
|---|---|
| 30 matchs rédigés | OUI |
| 96 Q/R et 20 rubriques par match | OUI, contrôle structurel |
| Dévoilement littéral par Q1 des cantonades | Aucun cas résiduel détecté par l'algorithme |
| Zéro question répétée sur 2 880 | NON DÉMONTRÉ |
| Justification factuelle de chaque réponse | NON ACHEVÉE |
| Documents prêts à être arbitrés sans autre vérification | **NON** |

Ce rapport vise à garder des critères vérifiables et à ne pas confondre **travail réalisé** et **garantie totale**.
