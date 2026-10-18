# Journal de reprise — 18 octobre 2026

288/960 faits individuellement vérifiés : matchs 01, 02 et 03. Chacun possède 96 preuves localisées, variantes, décisions d’arbitrage et contrôles sémantiques. Collection NON CERTIFIÉE; audit final ouvert.

Match 03 : 68 noms propres; sept remplacements pour répétition; 524 paires candidates actuelles relues. Rapport MATCH_03.md, sources et éditions de travail synchronisés. Deux cantonades, deux relais et quatre indices Fanon contrôlés. PDF lecteur 6 pages et arbitrage 21 pages; 27 pages rendues et inspectées, empreintes vérifiées après la panne.

Dix-sept questions remplacées pour répétition sur les trois matchs traités (4 + 6 + 7). Les réponses identiques portant sur des relations différentes ne sont pas assimilées automatiquement à des doublons.

**Incident résolu :** l’accès au serveur local a été rétabli après le checkpoint e1a5a388. Les fichiers du match 03 et les deux PDF ont été retrouvés et conservés. Le rapport d’incident et son delta partiel sont gardés comme historique; ils ne constituent plus le point de reprise actuel.

**Prochain point documentaire : M04-R01-Q01**, après lecture complète du match 04. Matchs 04 à 10 : 672 fiches non certifiées; aucun statut final attribué.

Derniers contrôles : intégrité 193/193; certification 217/274, 57 échecs concernant M04–M10 et les alertes globales. Les sorties horodatées figurent dans tests-integrite.json, tests-certification.json et executions.jsonl. Aucun échec propre à M01–M03.

Commandes : python scripts/certification_niveau1.py sync ; candidates ; check ; check --strict. PDF : python scripts/editions_pdf.py 1 2 3. Les six PDF portent une mention de revue globale en cours. Le générateur utilise les dates réelles des preuves. L’option --official est réservée à la clôture de l’audit de collection.

Preuves dans registre/certification et sources/certification; corrections avant/après conservées; anciennes décisions invalidées archivées dans historique-candidats.jsonl.

Branche qc/niveau-1-certification, PR #1 en brouillon. Ne pas fusionner vers main avant la certification des dix matchs et de la collection. Niveaux 2 et 3 inchangés. Aucune répétition physique avec élèves réalisée.
