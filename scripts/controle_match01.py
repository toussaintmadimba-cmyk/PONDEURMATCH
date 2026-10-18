#!/usr/bin/env python3
"""Contrôles structurels du Match 01. Ne certifie PAS la véracité."""
from collections import Counter
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "matchs/niveau-1/match-01.md"
REG = ROOT / "registre/match-01.json"
AUDIT = ROOT / "audit/match-01-validation.json"
SOURCES = ROOT / "sources/match-01-sources.md"

EXPECTED = [2,2,5,5,4,5,4,5,5,5,10,5,5,5,4,5,4,5,1,10]

def check():
    text = DOC.read_text(encoding="utf-8")
    reg = json.loads(REG.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT.read_text(encoding="utf-8"))
    source_text = SOURCES.read_text(encoding="utf-8")
    errors = []
    sections = list(re.finditer(r"^## (\d+)\. (.+)$", text, re.MULTILINE))
    if len(sections) != 20:
        errors.append(f"Rubriques : {len(sections)}, attendu 20")
    entries = []
    for ix, match in enumerate(sections):
        number = int(match.group(1))
        end = sections[ix + 1].start() if ix + 1 < len(sections) else len(text)
        chunk = text[match.end():end]
        qs = re.findall(r"^\*\*Q\d+\.\*\*", chunk, re.MULTILINE)
        rs = re.findall(r"^\*\*R\.\*\*", chunk, re.MULTILINE)
        if number != ix + 1:
            errors.append(f"Ordre de rubrique incohérent : {number}")
        if len(qs) != EXPECTED[ix] or len(rs) != EXPECTED[ix]:
            errors.append(f"Rubrique {number}: {len(qs)} Q et {len(rs)} R ; attendu {EXPECTED[ix]}")
        entries.extend((number, j) for j in range(1, len(qs)+1))
    if sum(EXPECTED) != 96 or len(entries) != 96:
        errors.append("Total Q/R différent de 96")
    if len(reg.get("facts", [])) != 96 or len(set(reg.get("facts", []))) != 96:
        errors.append("Registre de faits : 96 identifiants distincts requis")
    qs = audit.get("questions", [])
    if len(qs) != 96:
        errors.append(f"Entrées audit : {len(qs)}, attendu 96")
    ids = [q.get("id") for q in qs]
    if len(set(ids)) != 96:
        errors.append("Identifiants des questions dupliqués")
    pairs = [(q["section_number"], q["number"]) for q in qs]
    if pairs != entries:
        errors.append("Ordre et positions audit / questionnaire non synchronisés")
    proper = sum(bool(q.get("proper_name_answer")) for q in qs)
    if proper != reg.get("proper_name_answers"):
        errors.append(f"Noms propres audit={proper} registre={reg.get('proper_name_answers')}")
    for q in qs:
        if not q.get("answer") or not q.get("question"):
            errors.append(f"Q/R manquante {q.get('id')}")
        if not q.get("sources"):
            errors.append(f"Source absente {q.get('id')}")
        if f"| {q['id']} |" not in source_text:
            errors.append(f"Table de sources non synchronisée {q['id']}")
    if "## 5. LANGAGE A" not in text or "## 7. LANGAGE B" not in text:
        errors.append("Langage A ou B manquant")
    for n in (40,30,20,10):
        if f"**{n} points" not in text:
            errors.append(f"Indice à {n} points absent")
    print(f"Q/R : {len(entries)}/96 ; rubriques : {len(sections)}/20 ; noms propres : {proper}/96")
    print(f"Liens sources : {sum(bool(q.get('sources')) for q in qs)}/96")
    print("ATTENTION : tests structurels uniquement ; pas de certification factuelle ou d'arbitrage.")
    for err in errors:
        print("ERREUR :", err, file=sys.stderr)
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(check())
