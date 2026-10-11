# Contrôles de certification du Niveau 1

Les registres détaillés font autorité pour les statuts individuels. Le registre minimal historique est conservé pour la génération.

```bash
python scripts/certification_niveau1.py sync
python scripts/certification_niveau1.py candidates
python scripts/certification_niveau1.py check
python scripts/certification_niveau1.py check --strict
```

`sync` dérive les éditions de travail; `candidates` ne ferme aucun contrôle sémantique. Un succès du contrôle d’intégrité ne constitue pas une certification factuelle. Les échecs et leurs dates sont conservés dans executions.jsonl.

Les anciennes certifications du match 01 ne sont pas reprises sur simple confiance. Voir MATCH_01.md et JOURNAL_REPRISE.md pour le périmètre effectivement vérifié.
