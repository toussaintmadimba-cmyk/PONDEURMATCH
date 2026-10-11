# Rapport de certification du Match 01 — 11 octobre 2026

## Décision

**STATUT : PRÊT POUR COMPÉTITION SUR LE PLAN ÉDITORIAL ET DOCUMENTAIRE — essai oral avec de vrais participants recommandé avant l'événement.**

Les corrections éditoriales et plusieurs vérifications factuelles sont réalisées sur la branche `qc/match-01-2026-10-11`. La branche `main` n'a pas été modifiée par cette passe.

## Structure testée après modification

| Contrôle | Résultat |
|---|---|
| Matchs contrôlés | 01 / 30 |
| Niveau | 1 |
| Questions détectées | 96 / 96 |
| Réponses détectées | 96 / 96 |
| Rubriques détectées | 20 / 20 |
| Quotas précis des rubriques | CONFORMES |
| Langage A et Langage B | OUI — 4 questions chacun |
| Cantonades | 2 × 5 |
| Relais | 2 × 4 |
| Identification | quatre indices 40/30/20/10 présents |
| Identifiants de faits du registre existant | 96 / 96 |
| Réponses littéralement répétées dans ce match | 1 paire(s) ; contrôle de sens distinct |
| Noms propres | **67/96 (69,8 %)**, reclassification individuelle des réponses accomplie, incluant le statut de nom commun de « négritude » |

## Vérification documentaire individuelle

- **96 / 96** Q/R rattachées à une référence spécifique consultée dans cette passe ; statut `DOCUMENTE_SOURCE_DIRECTE`.
- **0 / 96** Q/R à confirmer par une source spécifique ; statut `A_VERIFIER_SOURCE`.
- Les sources antérieures et la connaissance courante ne sont pas comptées comme preuve vérifiée lorsqu'une référence précise n'a pas été examinée.
- Inventaire nominatif des 96 questions et statuts : [match-01-validation.json](match-01-validation.json).
- Tableau des références précises : [sources/match-01-sources.md](../sources/match-01-sources.md).

## Corrections appliquées au questionnaire

1. Le total de 68 noms propres est désormais présenté comme une **classification provisoire** et non comme une certification.
2. Le thème de **Langage A** devient « familles de mots et homophonie », en accord avec les quatre exercices effectivement posés.
3. La question de la première cantonade relative à l'**ANC** précise le mandat de Nelson Mandela (1991-1997).
4. La question des **continents** ne donne plus dans son propre énoncé le nombre attendu.
5. La formule de **dioxygène O₂** remplace une présentation impropre de O₂ comme « symbole chimique » du gaz ; réponse officielle **Dioxygène**.
6. La question sur **Patrice Émery Lumumba** ne donne plus rétrospectivement à l'État de 1960 une dénomination introduite ultérieurement.
7. L'identification de **Thomas Sankara** est structurée en quatre indices autonomes, gradés et recoupés avec la Présidence du Faso.

**Aucune question n'a été supprimée ou ajoutée.** Les identifiants de faits sont conservés, car les corrections ne changent pas les connaissances testées, sauf une précision de dénomination chimique sans changement de substance.

## Sources primaires et institutionnelles particulièrement importantes

- Présidence du Ghana, 6 octobre 2026 : https://presidency.gov.gh/ghana-is-open-for-business-says-mahama-as-he-courts-indian-pharma-vaccine-investments/
- Présidence du Mexique, 2 octobre 2026 : https://www.gob.mx/presidencia/articulos/version-estenografica-conferencia-de-prensa-de-la-presidenta-claudia-sheinbaum-pardo-del-02-de-octubre-de-2026
- World Athletics, records d'Usain Bolt : https://worldathletics.org/athletes/jamaica/usain-bolt-14201847
- World Rugby, finale 2023 : https://www.world.rugby/news/888593/nzl-11-12-rsa-south-africa-win-tense-final-to-claim-fourth-rugby-world-cup
- Fondation Nelson Mandela, biographie : https://www.nelsonmandela.org/biography
- Gouvernement sud-africain, investiture 1994 : https://www.gov.za/news/speeches/president-nelson-mandela-1994-presidential-inauguration-10-may-1994
- Académie française, Senghor : https://www.academie-francaise.fr/les-immortels/leopold-sedar-senghor?election=02-06-&fauteuil=16
- Présidence du Faso, Thomas Sankara : https://www.presidencedufaso.bf/thomas-sankara/
- Bureau international des poids et mesures, ohm : https://www.bipm.org/fr/-/resolution-cgpm-11-12

## Vérification transversale ciblée

Des réponses identiques apparaissent dans plusieurs matchs, mais les connaissances testées peuvent différer :

- **Albert Einstein** : théorie de la relativité générale (Match 01) contre formule `E = mc²` (Match 10) ; même personne, **fait distinct**.
- **Afrique du Sud** : vainqueur du rugby 2023 (Match 01) contre pays de l'activité de Gandhi ou de Mandela (autres matchs) ; **faits distincts**.
- **Piano** : instrument de 88 touches (Match 01) et indication italienne de nuance « piano » (Match 06) ; **sens distincts**.

Ces cas ne doivent pas être supprimés mécaniquement. Il reste à achever la recherche sémantique **sur les trente questionnaires**, au-delà de cet échantillon.

## Arbitrage

Des équivalents ont été consignés dans `audit/match-01-validation.json` pour ANC/Congrès national africain, dioxygène/oxygène, Patrice Lumumba, Galilée/Galileo Galilei, ONU/Nations unies et les graphies géographiques usuelles. Ce registre de variantes doit subir une relecture d'arbitre avant validation.

## Bloqueurs avant certification

1. Les 96 références individuelles sont rattachées ; contrôler toute réserve résiduelle de concordance source/affirmation lors de la relecture finale.
2. Faire la **déduplication sémantique complète** contre les 29 autres matchs, avec décisions documentées.
3. Revoir la **convention de classification des noms propres** avec l'arbitre : 67/96 ont été classées individuellement, contre 68 déclarées initialement.
4. Vérifier finement la cohérence et l'absence de divulgations **indirectes** des deux cantonades ; faire relire les formulations par un arbitre.
5. Mettre à l'épreuve **l'identification** et la difficulté orale du Niveau 1.
6. Réaliser une relecture finale après toutes les modifications et constituer la version arbitre prête à l'emploi.

## Point de reprise

Poursuivre la relecture des règles d'arbitrage dans le JSON `audit/match-01-validation.json`, en priorité celles dont le statut est `A_VERIFIER_SOURCE`. Ne repasser à `VALIDÉ` qu'après source exacte, arbitrage et anti-doublon complet. Ne pas commencer la certification finale du Match 02 tant que le Match 01 n'est pas clos si la stratégie du projet est strictement « un match à la fois ».

## Complément d'audit documentaire

Les sources directes ont été étendues, notamment grâce à la Comédie-Française (Molière), au musée Reina Sofía (Guernica), au dictionnaire Larousse (négritude, homophones, adverbe « dehors », thermomètre, photosynthèse), au Portail linguistique du Canada (pronom) et à Parcs Canada (Ottawa). Le quota reclassé est de **67 réponses-noms propres sur 96 (69,8 %)**, la « négritude » étant un nom commun féminin.


## Addendum documentaire

Les 96 questions sont désormais toutes dotées de références dans `audit/match-01-validation.json`. Deux répétitions inversées ont été corrigées : Sénégal/Dakar et Tanzanie/Kilimandjaro.


Le tableau intermédiaire de `sources/match-01-sources.md` (44 sources) représente une photographie antérieure à la présente passe. Pour l'intégralité des 96 références, consulter le catalogue JSON. La préparation des documents pour arbitre est en cours.
