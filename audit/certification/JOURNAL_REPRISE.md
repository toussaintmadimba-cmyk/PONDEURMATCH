# Journal de reprise de certification

Point enregistré le 2026-10-11T21:24:43.508039+00:00.

Mission active : certification individuelle de 10 matchs / 960 Q/R, aucun certificat global délivré.

## État réel

| Match | Faits vérifiés | Arbitrage validé | Fiches finales | Documents de compétition |
|---|---:|---:|---:|---|
| 01 | 96/96 | 96/96 | 96/96 | En préparation |
| 02 | 16/96 | 16/96 | 0/96 | En préparation |
| 03 | 0/96 | 0/96 | 0/96 | En préparation |
| 04 | 0/96 | 0/96 | 0/96 | En préparation |
| 05 | 0/96 | 0/96 | 0/96 | En préparation |
| 06 | 0/96 | 0/96 | 0/96 | En préparation |
| 07 | 0/96 | 0/96 | 0/96 | En préparation |
| 08 | 0/96 | 0/96 | 0/96 | En préparation |
| 09 | 0/96 | 0/96 | 0/96 | En préparation |
| 10 | 0/96 | 0/96 | 0/96 | En préparation |

Total vérifié : 112/960. Les statuts sont recalculés à partir des registres, sans compter les URL héritées comme des preuves.

## Tests exécutés

- python scripts/certification_niveau1.py sync : dérivations lecteur/arbitre/sources synchronisées.
- python scripts/certification_niveau1.py candidates : 2 880 questions, comparaison de 2 303 520 paires; génération d’alertes, pas certification automatique.
- python scripts/certification_niveau1.py check : 193/193.
- python scripts/certification_niveau1.py check --strict : 200/244; 44 échecs liés aux volets ouverts. Historique complet : executions.jsonl.

## Reprise précise

- Poursuivre le match 02. La lecture des 96 Q/R et celle de ses rapprochements automatiques ont été faites; contrôles documentaires incomplets.
- Prochaine fiche non vérifiée : M02-R03-Q01.
- Répétitions à traiter : M02-R11-Q04 / M08-R20-Q01 (Helsinki–Finlande), M02-R20-Q02 / M07-R09-Q05 (Lima–Pérou), M02-R20-Q10 / M10-R11-Q01 (Reykjavík–Islande); relation Aristote–Alexandre recoupée dans M05-R09-Q01 à remplacer par un autre fait discriminant.
- Doublons numériques M02-R11-Q07 (angle droit / M19) et M02-R20-Q06 (multiplication / M08 et M09) remplacés par rayon et produit; nouvelles preuves consultées.
- Identification Diop : quatre indices prouvés; musée remplacé par université, naissance reprise sous la graphie UCAD Caytou, laboratoire carbone14 ajouté.
- Sources bloquées ne comptent pas comme vérifiées : anciennes pages Nobel en 403, europarl page JavaScript vide, ancienne URL World Rugby inaccessible. Des alternatives documentaires ont été trouvées pour Maathai et la règle rugby.
- Restent les preuves des autres questions M02, la déduplication finale M02, les rapports M02–M10, les contrôles transversaux et les 21 PDF officiels.
- Ne modifier aucun questionnaire des Niveaux 2 et 3.
- Branches déjà examinées : main acc13d401eb35e85a6ba4eff5045e316c4ff63a4; QC match01 ba27c9a32dd8da388856bf556cf7842f336a9c98. Branche de travail : qc/niveau-1-certification. Aucune fusion autorisée/exécutée.
- scripts/certification_niveau1.py contient parse, sync, candidates et check. /tmp/pm_review.py est une aide temporaire; pour reprise durable, modifier explicitement questionnaire et fiche correspondante avant sync.
