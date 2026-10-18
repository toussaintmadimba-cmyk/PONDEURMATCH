# Point de reprise actif — étape 2 / M05 en cours

Accord « LANCES » reçu le 18 octobre 2026. M05 : 75/96 faits documentés avec décisions d’arbitrage, 68 noms propres sur 96 réponses classées. Aucun statut final M05 attribué. Les quatre répétitions déjà identifiées ont des remplacements documentés; comparaison sémantique finale encore ouverte.

Incident : le serveur local a perdu sa connexion pendant l’enregistrement du lot suivant. Les 48 fiches déjà écrites localement ont été reconstruites depuis les données vérifiées de cette conversation; 27 autres ont été ajoutées via le connecteur GitHub. Le registre, le questionnaire et les éditions provisoires du présent checkpoint constituent la reprise durable. Ne pas écraser ce commit avec les 48 fiches locales anciennes.

Les tests Python M05 et ses PDF n’ont pas été exécutés à ce stade. Derniers résultats antérieurs, propres au checkpoint M04 : intégrité 193/193 et certification 225/274. Ils ne valident pas les nouvelles modifications M05.

À poursuivre : les 21 fiches dont factual_status diffère de FAIT_VERIFIE, puis déduplication, relecture complète, tests et deux PDF. Ne pas lancer M06 sans un nouvel accord explicite après clôture M05. Collection NON CERTIFIÉE; aucune fusion vers main.

---

# Historique précédent

# Point de reprise actif — étape 1 terminée, accord attendu

18 octobre 2026 : match 04 contrôlé à 96/96, 20 rubriques conservées, Langage A/B inclus. 68 noms propres. Sept remplacements pour répétition; 481 paires candidates actuelles concernant M04 relues contre 2 880 Q/R. Deux cantonades, deux relais, quatre indices Biko vérifiés; rapport MATCH_04.md et registres synchronisés. Deux PDF : lecteur 6 pages, arbitrage 22 pages; 28 pages rendues et inspectées.

**ARRÊT DEMANDÉ PAR L’UTILISATEUR : attendre son accord explicite avant l’étape 2 / match 05. Ne pas commencer M05 sans cet accord.** Voir SUIVI_10_ETAPES.md. Après accord, point exact : M05-R01-Q01.

Acquis : matchs 01–04, 384/960 fiches et huit PDF contrôlés. Restant : matchs 05–10, 576 fiches, puis audit transversal, éditions officielles de collection et contrôles finaux. Aucun statut PRÊT POUR COMPÉTITION; collection NON CERTIFIÉE.

Derniers tests réels : 18 octobre 2026, 18:12:29 UTC; intégrité 193/193, certification 225/274. Zéro échec propre à M01–M04; 49 échecs ouverts (M05–M10 et clôture globale des alertes). Les sorties et dates figurent dans tests-integrite.json, tests-certification.json et executions.jsonl.

Enregistrement sur qc/niveau-1-certification; PR #1 en brouillon, aucune fusion vers main. Niveaux 2/3 inchangés. Espaces insécables ajoutées au générateur PDF pour éviter la ponctuation française isolée; aucune régénération des autres matchs avant l’étape 9. Répétition physique non réalisée.

---

# Historique antérieur — points de reprise remplacés

# Mode actuel : dix étapes avec accord entre étapes

Instruction du 18 octobre : voir SUIVI_10_ETAPES.md. Étape 1 (match 04) EN COURS : 48/96 faits documentés, tous les 96 types de réponse classés, 68 noms propres. Les vérifications factuelles restantes, la déduplication finale, la relecture d’ensemble, les PDF et le rapport M04 restent ouverts. **Ne pas lancer le match 05 avant validation complète de l’étape 1 et accord explicite de l’utilisateur.**

Les quatre indices Biko sont documentés; son lieu de naissance litigieux et son prénom donné en dernier indice ont été retirés. Les dates de la cantonade Earhart ne dévoilent plus l’année de disparition de Q5. Remplacements provisoires pour répétition : racine carrée vers nombre pair; pentagone vers bissectrice; Rê vers Hathor. Contrôle complet de ces remplacements contre les 2 880 Q/R encore à achever.

Accès local rétabli. Dernière intégrité exécutée : 193/193. Les trois matchs précédents restent intacts. Reprendre les fiches M04 dont factual_status diffère de FAIT_VERIFIE; ne pas recommencer les 48 preuves déjà consignées.

---

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
