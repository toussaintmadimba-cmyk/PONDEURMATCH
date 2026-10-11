#!/usr/bin/env python3
"""Inventory, synchronisation and certification gates. Never verifies facts by itself."""
import argparse
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [2, 2, 5, 5, 4, 5, 4, 5, 5, 5, 10, 5, 5, 5, 4, 5, 4, 5, 1, 10]
STATUSES = {'NON_EXAMINE', 'SOURCE_TROUVEE_NON_VERIFIEE', 'EN_COURS_DE_VERIFICATION',
            'ANOMALIE_CONFIRMEE', 'CORRIGE_A_RECONTROLER', 'FAIT_VERIFIE',
            'ARBITRAGE_VALIDE', 'DOUBLON_CONTROLE', 'VALIDE_FINAL'}

def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def norm(s):
    s = unicodedata.normalize('NFKD', s).casefold()
    return ' '.join(re.findall(r'[a-z0-9]+', ''.join(c for c in s if not unicodedata.combining(c))))

def parse(path):
    text = path.read_text(encoding='utf-8')
    match = int(re.search(r'match-(\d+)', path.name)[1])
    sections = list(re.finditer(r'^## (\d+)\. (.+)$', text, re.M))
    entries, counts = [], []
    for i, s in enumerate(sections):
        chunk = text[s.end():sections[i+1].start() if i+1 < len(sections) else len(text)]
        pairs = re.findall(r'^\*\*Q(\d+)\.\*\*\s*(.*?)\n\*\*R\.\*\*\s*([^\n]+)', chunk, re.M | re.S)
        counts.append((int(s[1]), len(pairs), len(re.findall(r'^\*\*Q\d+\.\*\*', chunk, re.M)), len(re.findall(r'^\*\*R\.\*\*', chunk, re.M))))
        for n, question, answer in pairs:
            entries.append(dict(id=f'M{match:02d}-R{int(s[1]):02d}-Q{int(n):02d}', match=match,
                section_number=int(s[1]), section=s[2], number=int(n), question=question.strip(), answer=answer.strip()))
    return text, entries, counts

def corpus():
    out = []
    for path in sorted((ROOT / 'matchs').glob('niveau-*/match-*.md')):
        out.extend(parse(path)[1])
    return out

def sync():
    historical = json.loads((ROOT/'audit/match-01-validation.json').read_text())
    inherited = {q['id']: q for q in historical['questions']}
    for m in range(1, 11):
        path = ROOT / f'matchs/niveau-1/match-{m:02d}.md'
        text, rows, _ = parse(path)
        target = ROOT / f'registre/certification/match-{m:02d}.json'
        old = {q['id']: q for q in json.loads(target.read_text())['questions']} if target.exists() else {}
        facts = json.loads((ROOT/f'registre/match-{m:02d}.json').read_text())['facts']
        qs = []
        for i, q in enumerate(rows):
            prior = inherited.get(q['id'], {})
            entry = dict(q, fact_id=facts[i], tested_fact=facts[i], accepted_variants=prior.get('accepted_variants', []),
                primary_source=None, secondary_sources=[], corroboration=None, consulted_at=None,
                factual_status='SOURCE_TROUVEE_NON_VERIFIEE' if prior.get('sources') else 'NON_EXAMINE',
                arbitration_status='NON_EXAMINE', deduplication_status='NON_EXAMINE', final_status='NON_EXAMINE',
                response_type=('nom_propre' if prior['proper_name_answer'] else 'autre') if 'proper_name_answer' in prior else None,
                corrections=[], decision='Contrôles obligatoires ouverts.', evidence=[],
                inherited_references=prior.get('sources', []), inherited_status=prior.get('status'))
            if q['id'] in old:
                before = old[q['id']]
                if before['question'] != q['question'] or before['answer'] != q['answer']:
                    raise ValueError(f'{q["id"]}: questionnaire changé; mettre à jour explicitement la fiche avant sync')
                entry.update(before)
            qs.append(entry)
        write_json(target, dict(match=m, level=1, question_count=len(qs), questionnaire_sha256=hashlib.sha256(text.encode()).hexdigest(), questions=qs))
        reader = ROOT / f'editions/travail/lecteur/match-{m:02d}.md'
        arb = ROOT / f'arbitrage/certification/match-{m:02d}.md'
        src = ROOT / f'sources/certification/match-{m:02d}.md'
        for p in (reader, arb, src): p.parent.mkdir(parents=True, exist_ok=True)
        reader.write_text(('> ÉDITION DE TRAVAIL — NON CERTIFIÉE. Questions seules; lecteur uniquement.\n\n'+re.sub(r'^\*\*R\.\*\*[^\n]*\n?', '', text, flags=re.M)).rstrip()+'\n', encoding='utf-8')
        a = [f'# Match {m:02d} — arbitrage en cours', '', '> NON CERTIFIÉ — les décisions absentes restent à examiner.', '']
        sources = [f'# Match {m:02d} — preuves de certification', '', '> Une référence héritée ne constitue pas une preuve nouvellement vérifiée.', '']
        for q in qs:
            a.extend([f'## {q["id"]} — {q["section"]}', q['question'], f'**Réponse :** {q["answer"]}',
                '**Variantes :** '+('; '.join(q['accepted_variants']) or 'Aucune variante consignée.'),
                '**Décision :** '+q['decision'], '**Arbitrage :** '+q['arbitration_status'],
                '**Preuves :** '+('; '.join(ev['url']+' — '+ev['locator'] for ev in q['evidence']) or 'Contrôle documentaire ouvert.'), ''])
            sources.extend([f'## {q["id"]}', '**Statut :** '+q['factual_status'],
                '**Référence héritée :** '+('; '.join(q['inherited_references']) or 'Aucune référence individuelle héritée.')])
            for ev in q['evidence']:
                sources.extend([f'- Source : {ev["url"]}', f'  Repère : {ev["locator"]}',
                    f'  Corroboration (paraphrase) : {ev["support"]}', f'  Consultation : {ev["consulted_at"]}'])
            sources.append('')
        arb.write_text('\n\n'.join(a).rstrip()+'\n', encoding='utf-8')
        src.write_text('\n'.join(sources).rstrip()+'\n', encoding='utf-8')

def candidates():
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    rows = corpus()
    docs = [norm(q['question']+' '+q['answer']) for q in rows]
    normalized_questions = [norm(q['question']) for q in rows]
    normalized_answers = [norm(q['answer']) for q in rows]
    x = TfidfVectorizer(ngram_range=(1, 2), min_df=1).fit_transform(docs)
    sim = cosine_similarity(x[:960], x)
    entity_sets = [{norm(w) for w in re.findall(r'\b[A-ZÀ-Ý][\w-]+', q['question']+' '+q['answer']) if len(w)>3} for q in rows]
    entity_frequency = Counter(w for words in entity_sets for w in words)
    generic = {'quelle','quel','dans','comment','combien','selon','identification','points','theme','qui','quels',
        'siecle','afrique','africain','africaine','europe','france','paris','asie','congo','nobel', 'republique',
        'systeme','universite','national','nationale','guerre','unies','premier','jeux','olympiques'}
    entity_sets = [{w for w in words if w not in generic and entity_frequency[w]<=18} for words in entity_sets]
    alerts = []
    for i in range(960):
        a = rows[i]
        for j in range(i+1, len(rows)):
            b = rows[j]
            reasons = []
            if normalized_questions[i] == normalized_questions[j]: reasons.append('texte_identique')
            if normalized_answers[i] == normalized_answers[j]: reasons.append('reponse_commune_a_examiner')
            if sim[i, j] >= .43: reasons.append('proximite_lexicale')
            # Shared named words also catch inverse relations with different answers.
            shared = entity_sets[i] & entity_sets[j]
            if shared: reasons.append('entite_commune')
            if reasons:
                alerts.append(dict(pair=f'{a["id"]}__{b["id"]}', first=a, second=b, score=round(float(sim[i,j]),4), reasons=reasons,
                    decision='NON_EXAMINE', justification=None))
    target=ROOT/'audit/certification/doublons-candidats.json'
    old={a['pair']:a for a in json.loads(target.read_text())['candidates']} if target.exists() else {}
    for a in alerts:
        if a['pair'] in old:
            o=old[a['pair']]
            if o['first']['question']==a['first']['question'] and o['second']['question']==a['second']['question']:
                a['decision']=o['decision']; a['justification']=o['justification']
                if 'reviewed_at' in o: a['reviewed_at']=o['reviewed_at']
    current={a['pair']:a for a in alerts}
    changed=[o for pair,o in old.items() if pair not in current
             or any(o[side]['question'] != current[pair][side]['question']
                    for side in ('first','second'))]
    if changed:
        archive=ROOT/'audit/certification/historique-candidats.jsonl'
        with archive.open('a',encoding='utf-8') as log:
            for o in changed:
                log.write(json.dumps(dict(archived_at=datetime.now(timezone.utc).isoformat(),candidate=o),ensure_ascii=False)+'\n')
    write_json(target, dict(corpus_count=len(rows), level1_count=960, compared_pairs=sum(len(rows)-i-1 for i in range(960)),
        method='TF-IDF mots/bigrammes >= 0.43, réponses identiques, textes identiques, entités partagées. Générateur de candidats, pas preuve sémantique.', candidates=alerts))
    print(f'{len(rows)} questions; {len(alerts)} paires candidates, examen sémantique requis')

def check(strict=False):
    checks=[]
    def add(name, ok, detail=''): checks.append(dict(test=name, passed=bool(ok), detail=detail))
    all_ids=[]
    for m in range(1,11):
        prefix=f'M{m:02d}'
        path=ROOT/f'matchs/niveau-1/match-{m:02d}.md'
        add(prefix+' fichier', path.exists())
        text, rows, counts=parse(path)
        add(prefix+' rubriques', [c[0] for c in counts]==list(range(1,21)))
        add(prefix+' effectifs Q/R', [(c[1],c[2],c[3]) for c in counts]==[(n,n,n) for n in EXPECTED])
        add(prefix+' 96 associations', len(rows)==96)
        add(prefix+' langages', '## 5. LANGAGE A' in text and '## 7. LANGAGE B' in text)
        for s in (5,7,15,17):
            chunk=re.split(rf'^## {s}\. ',text,flags=re.M)[1].split('\n## ')[0]
            add(prefix+f' thème R{s}', '**THÈME' in chunk)
        ident=next(q for q in rows if q['section_number']==19)
        add(prefix+' quatre indices', all(re.search(rf'{p} points',ident['question']) for p in (40,30,20,10)))
        target=ROOT/f'registre/certification/match-{m:02d}.json'
        reg=json.loads(target.read_text()); qs=reg['questions']
        add(prefix+' synchronisation registre', [(q['id'],q['question'],q['answer']) for q in rows]==[(q['id'],q['question'],q['answer']) for q in qs])
        add(prefix+' empreinte questionnaire',reg['questionnaire_sha256']==hashlib.sha256(text.encode()).hexdigest())
        all_ids.extend(q['id'] for q in qs)
        reader=(ROOT/f'editions/travail/lecteur/match-{m:02d}.md').read_text()
        arb=(ROOT/f'arbitrage/certification/match-{m:02d}.md').read_text()
        src=(ROOT/f'sources/certification/match-{m:02d}.md').read_text()
        add(prefix+' lecture sans réponses', not re.search(r'^\*\*R\.\*\*',reader,re.M) and all(q['question'] in reader for q in qs))
        add(prefix+' arbitrage synchronisé',all(q['id'] in arb and q['question'] in arb and q['answer'] in arb for q in qs))
        add(prefix+' sources 96 fiches',all('## '+q['id'] in src for q in qs))
        add(prefix+' statuts légitimes',all(all(q[k] in STATUSES for k in ('factual_status','arbitration_status','deduplication_status','final_status')) for q in qs))
        add(prefix+' validation sans preuve interdite',all(q['factual_status'] not in ('FAIT_VERIFIE','VALIDE_FINAL') or bool(q['evidence']) for q in qs))
        add(prefix+' finale exige trois volets',all(q['final_status']!='VALIDE_FINAL' or (q['factual_status']=='FAIT_VERIFIE' and q['arbitration_status']=='ARBITRAGE_VALIDE' and q['deduplication_status']=='DOUBLON_CONTROLE') for q in qs))
        known=sum(q['response_type']=='nom_propre' for q in qs)
        classified=sum(q['response_type'] is not None for q in qs)
        add(prefix+' types de réponse calculés', known<=classified<=96, f'{known} noms propres; {classified}/96 classés')
        if strict:
            add(prefix+' 96 validations finales',all(q['final_status']=='VALIDE_FINAL' for q in qs))
            add(prefix+' 96 classifications',classified==96)
            add(prefix+' objectif noms propres',67<=known<=69, f'{known}/96, soit {known/96:.1%}')
            add(prefix+' preuve localisée complète',all(q['primary_source'] and q['consulted_at'] and q['corroboration'] and
                all(e.get('url') and e.get('locator') and e.get('support') and e.get('consulted_at') for e in q['evidence']) for q in qs))
            add(prefix+' variantes consignées',all(q['accepted_variants'] and q['decision'] for q in qs))
    add('960 identifiants distincts', len(all_ids)==960 and len(set(all_ids))==960)
    rows=corpus(); add('2880 questions comparées',len(rows)==2880)
    alerts=json.loads((ROOT/'audit/certification/doublons-candidats.json').read_text())['candidates']
    add('décisions de doublons traçables',all(a['decision']=='NON_EXAMINE' or bool(a['justification']) for a in alerts))
    if strict:
        add('alertes sémantiques fermées',all(a['decision'] not in ('NON_EXAMINE','DOUBLON_CONFIRME') for a in alerts))
    result=dict(command=f'python scripts/certification_niveau1.py check'+(' --strict' if strict else ''), executed_at=datetime.now(timezone.utc).isoformat(),
        mode='certification' if strict else 'intégrité; ne certifie ni faits ni arbitrage', test_count=len(checks),
        passed=sum(c['passed'] for c in checks), failed=sum(not c['passed'] for c in checks), checks=checks)
    write_json(ROOT/('audit/certification/tests-certification.json' if strict else 'audit/certification/tests-integrite.json'),result)
    with (ROOT/'audit/certification/executions.jsonl').open('a',encoding='utf-8') as log:
        log.write(json.dumps(result,ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False))
    for c in checks:
        if not c['passed']: print('ÉCHEC',c['test'],c['detail'])
    return bool(result['failed'])

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('action',choices=['sync','candidates','check']); ap.add_argument('--strict',action='store_true'); args=ap.parse_args()
    if args.action=='sync': sync()
    elif args.action=='candidates': candidates()
    else: sys.exit(check(args.strict))
