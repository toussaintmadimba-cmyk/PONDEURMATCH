# Reprise après incident — 18 octobre 2026

## État enregistré sur GitHub

La branche `qc/niveau-1-certification` était à `d0fc48a645de5f666056e4da02bf6951b3fc175f` au début de cette reprise. Les matchs 01 et 02, leurs 192 fiches et leurs quatre PDF sont conservés. La PR #1 reste ouverte en brouillon; aucune fusion vers main.

## Travail réellement exécuté, encore local au moment de la panne

Le match 03 possède dans l’espace de travail 96/96 preuves factuelles localisées, 96 décisions d’arbitrage et 96 contrôles de répétition. La dernière relecture complète des 96 Q/R a été effectuée. Noms propres: 68/96. Sources: 87 URL distinctes. Modifications: 55 fiches, 61 événements avant/après; il ne s’agit pas de 55 erreurs factuelles.

Sept questions ont été remplacées pour répétition: M03-R03-Q04 (points d’un essai, doublon de M29-R03-Q05), M03-R04-Q04 (guitare et six cordes, relation inversée de M01-R04-Q03), M03-R11-Q09 et M03-R20-Q07 (dénombrement polygonal), M03-R07-Q02 (plus-que-parfait, M12-R07-Q01), M03-R07-Q04 (reconnaissance du subjonctif, M11-R07-Q02 et M29-R07-Q02), M03-R08-Q04 (pH neutre, M09-R08-Q05).

Les nouvelles réponses sont respectivement lignes de touche, cordes, quotient, médiane, deuxième groupe, terminaison/désinence et vessie. Les preuves et variantes sont dans le registre local du match 03. Deux autres corrections importantes: David de Michel-Ange distingué des autres David de Florence; Amundsen identifié comme chef d’expédition et non comme seul Norvégien présent au pôle Sud.

Relecture finale: suppression de l’attribution de l’ensemble des sept voyages de Zheng He au seul règne de Yongle (mort en 1424). Une erreur intermédiaire de ciblage éditorial avait appliqué la question de la Tamise à la fiche de Séoul; celle-ci a été réparée avant les derniers tests et PDF.

Cantonades King et Nightingale, deux relais et quatre indices de Frantz Fanon relus. Pluriels: épellation exigée. Langage B conservé, thème élargi à la conjugaison et à la construction des verbes. Hajj est classé comme nom commun.

PDF effectivement générés et inspectés:
- `output/pdf/match-03-lecteur.pdf`: 6 pages, 96 questions, aucun corrigé; SHA-256 `d45d35b58279730cc9a865f3f424b8161800e286a05b8be8c893d32c33e05414`.
- `output/pdf/match-03-arbitrage.pdf`: 21 pages, 96 questions et 96 identifiants de réponses; SHA-256 `1290ccba03f241dabc6358324b7f2a2eaec1317fb48419273c3e6d6dc82903e1`.

Les 27 pages ont été rendues en PNG, puis examinées sur deux planches de contact; zones de texte contrôlées. Ces deux PDF n’ont pas pu être transférés sur GitHub avant la panne. Ne pas les annoncer disponibles sur la branche distante.

Tests réellement exécutés:
- `python scripts/certification_niveau1.py check`, 2026-10-18T17:17:44.417738+00:00: 193 tests, 193 réussis, 0 échec.
- `python scripts/certification_niveau1.py check --strict`, 2026-10-18T17:17:44.560647+00:00: 274 tests, 217 réussis, 57 échecs.
- Aucun échec propre aux matchs 01, 02 et 03; échecs restants: huit exigences par match pour M04–M10, plus fermeture globale des alertes.
- Aucune répétition physique avec élèves réalisée.

## Blocage technique constaté

Le serveur d’exécution local est devenu indisponible juste avant la création du rapport MATCH_03.md et l’enregistrement du lot sur GitHub. Les commandes renvoient `exec-server transport disconnected`, puis `failed to resume exec-server session: recovery timed out after 25s`. Une tentative de lecture minimale a également échoué. Une tentative de sauvegarde locale par apply_patch est restée sans résultat confirmé et a été interrompue. Le connecteur GitHub fonctionne encore, ce qui permet d’enregistrer le présent journal.

Les fichiers locaux existent après leurs opérations réussies, mais leur accessibilité après récupération de l’environnement n’est pas garantie. Le fichier détaillé MATCH_03.md et la mise à jour complète du journal n’ont pas été créés par la commande qui a échoué au lancement.

**Ne pas confondre les résultats locaux observés et le contenu distant:** le registre de certification M03 et les résultats JSON complets de GitHub restent ceux du précédent checkpoint tant que le diff local n’a pas été récupéré. Le présent compte rendu ne les remplace pas et n’attribue pas de certification distante fictive.

## Point précis de reprise

1. Rétablir l’accès au dossier `/workspace/scratch/16182c810248/PONDEURMATCH`; lire d’abord `git status` et préserver tous les changements locaux.
2. Récupérer en priorité `registre/certification/match-03.json`, `matchs/niveau-1/match-03.md`, `registre/match-03.json`, `sources/certification/match-03.md`, `arbitrage/certification/match-03.md`, `editions/travail/lecteur/match-03.md`, les candidats et leur historique, `relecture-match-03.json`, `pdf-match-03.json`, `doublons-corriges-match-03.json`, les résultats de tests et les deux PDF.
3. Vérifier leurs empreintes et leur cohérence; rédiger le rapport MATCH_03.md à partir des corrections déjà consignées; enregistrer sur la même branche sans écraser ce checkpoint d’incident.
4. Reprendre ensuite à **M04-R01-Q01**, après lecture du match 04. Les matchs 04 à 10 restent 672 fiches non certifiées.
5. Si les fichiers locaux ne sont pas récupérables, exploiter le delta de secours et ce journal; ne pas attribuer aux 96 fiches distantes des preuves qui n’y figurent pas encore.

**Décision globale: NIVEAU 1 NON CERTIFIÉ.** Aucun travail ne continue en arrière-plan après l’arrêt de la session.

---

## Journal précédent conservé pour la continuité

# Journal de reprise — 11 octobre 2026

192/960 faits individuellement vérifiés : matchs 01 et 02. Arbitrage et comparaison sémantique réalisés pour leurs 96 fiches chacun ; 535 et 485 candidats actuels examinés. Dix doublons véritables éliminés (4 + 6). PDF contrôlés, 96 questions lecteur et 96 réponses arbitrage par match. Statut de collection : NON CERTIFIÉE.

Matchs 03 à 10 : 768 fiches NON_EXAMINE, aucun statut final attribué. Match 03 lu intégralement ; reprise documentaire à M03-R01-Q01. Examiner aussi la divulgation de Washington dans la cantonade King et remplacer les exercices triangle/carré répétitifs.

Derniers tests : intégrité 193/193 ; certification 209/274, 65 échecs conservés. Les échecs correspondent aux huit matchs non traités et aux alertes globales.

Commandes : python scripts/certification_niveau1.py sync ; candidates ; check ; check --strict. PDF : python scripts/editions_pdf.py 1 2. Les PDF portent volontairement une mention de revue globale en cours. L’option --official ne sera utilisée qu’après audit de collection.

Les sources sont localisées dans registre/certification et sources/certification. Les corrections avant/après sont préservées dans chaque fiche. Les décisions invalidées par modification d’énoncé ou réponse sont archivées dans historique-candidats.jsonl.

Ne pas fusionner vers main tant que les dix matchs et la collection n’ont pas franchi les contrôles. Niveaux 2 et 3 inchangés.
