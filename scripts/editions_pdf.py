#!/usr/bin/env python3
"""Render reader/arbitration PDFs from the individual register; never certify facts."""
import argparse
import hashlib
import json
import re
from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf'
NAVY = colors.HexColor('#15354A')
GRAY = colors.HexColor('#51616B')
for name, file in [('Body', 'DejaVuSans.ttf'), ('Strong', 'DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, '/usr/share/fonts/truetype/dejavu/' + file))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='Strong', italic='Body', boldItalic='Strong')
STYLES = {
    'title': ParagraphStyle('title', fontName='Strong', fontSize=23, leading=29, textColor=NAVY, spaceAfter=13),
    'sub': ParagraphStyle('sub', fontName='Body', fontSize=10, leading=15, textColor=GRAY, spaceAfter=12),
    'section': ParagraphStyle('section', fontName='Strong', fontSize=12, leading=17, textColor=NAVY, spaceBefore=14, spaceAfter=8),
    'question': ParagraphStyle('question', fontName='Body', fontSize=10.5, leading=15.5, spaceAfter=9),
    'answer': ParagraphStyle('answer', fontName='Body', fontSize=10, leading=15, spaceAfter=5),
    'note': ParagraphStyle('note', fontName='Body', fontSize=9, leading=13, textColor=GRAY, spaceAfter=5),
    'source': ParagraphStyle('source', fontName='Body', fontSize=7.7, leading=10.8, textColor=GRAY, spaceAfter=5, splitLongWords=True),
}

def safe(s):
    # Unicode fonts retain French accents; normalise uncommon dashes for print.
    return escape(re.sub('[\u2010-\u2015\u2212]', '-', s)).replace('\n', '<br/>')

def para(s, style='question'):
    return Paragraph(s, STYLES[style])

def question_text(q):
    s = safe(q['question'].replace('**', ''))
    if q['section_number'] == 19:
        s = re.sub(r'\s*(40|30|20|10) points\s*[:-]', r'<br/><b>\1 points :</b>', s).removeprefix('<br/>')
    return '<b>Q' + str(q['number']) + '.</b> ' + s

def build(mid, mode, official=False):
    register = ROOT / f'registre/certification/match-{mid:02d}.json'
    data = json.loads(register.read_text())
    assert len(data['questions']) == 96
    assert all(q['final_status'] == 'VALIDE_FINAL' for q in data['questions']), 'Unverified questions: no printable edition.'
    source = ROOT / f'matchs/niveau-1/match-{mid:02d}.md'
    assert data['questionnaire_sha256'] == hashlib.sha256(source.read_bytes()).hexdigest()
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / f'match-{mid:02d}-{mode}.pdf'
    story = [para('PONDEURMATCH', 'title'), para(f'NIVEAU 1 · MATCH {mid:02d} · '+('LECTEUR' if mode=='lecteur' else 'ARBITRAGE'), 'section')]
    status = 'Édition officielle' if official else 'Édition contrôlée - revue globale en cours'
    story += [para(safe(status)+'<br/>96 questions · 20 rubriques · Consultation documentaire : 11 octobre 2026', 'sub')]
    if mode == 'lecteur':
        story += [para('Équipe A : ____________________ &nbsp; Équipe B : ____________________<br/>Date : ________________________ &nbsp; Lecteur : ______________________', 'note')]
    else:
        story += [para('La réponse officielle et ses variantes sont admissibles. Demander une précision sans indice pour une réponse partielle. Consulter la décision individuelle en cas de contestation.', 'note')]
    current = None
    source_text = source.read_text()
    for q in data['questions']:
        if current != q['section_number']:
            current = q['section_number']
            if current == 12:
                story += [para('MI-TEMPS', 'section')]
            title = para(str(current)+'. '+safe(q['section']), 'section')
            chunk = re.split(rf'^## {current}\. ', source_text, flags=re.M)[1].split('\n## ')[0]
            theme = re.search(r'^\*\*THÈME\s*:\s*(.*?)\*\*', chunk, re.M)
            pre = [title]
            if theme:
                pre.append(para('Thème : '+safe(theme[1]), 'note'))
            pre.append(para(question_text(q)))
            if mode == 'arbitrage':
                pre.append(para('<b>'+q['id']+' - Réponse :</b> '+safe(q['answer']), 'answer'))
            story.append(KeepTogether(pre))
        else:
            group = [para(question_text(q))]
            if mode == 'arbitrage':
                group.append(para('<b>'+q['id']+' - Réponse :</b> '+safe(q['answer']), 'answer'))
            story.append(KeepTogether(group))
        if mode == 'arbitrage':
            story.append(para('<b>Variantes :</b> '+safe('; '.join(q['accepted_variants'])), 'note'))
            story.append(para('<b>Décision :</b> '+safe(q['decision']), 'note'))
            for i, ev in enumerate(q['evidence'], 1):
                url = safe(ev['url'])
                story.append(para(f'<b>Source {i} :</b> <link href="{url}">{url}</link><br/><b>Repère :</b> '+safe(ev['locator'])+'<br/><b>Preuve :</b> '+safe(ev['support']), 'source'))
            story.append(Spacer(1, 7))
    def page(canvas, doc):
        canvas.saveState()
        canvas.setFont('Body', 7.5)
        canvas.setFillColor(GRAY)
        canvas.drawString(43, 818, f'PONDEURMATCH | NIVEAU 1 | MATCH {mid:02d}')
        canvas.drawRightString(552, 818, 'Lecteur - sans corrigé' if mode=='lecteur' else 'Arbitrage - accès réservé')
        canvas.setStrokeColor(colors.HexColor('#DCE4E8'))
        canvas.line(43, 810, 552, 810)
        canvas.line(43, 40, 552, 40)
        canvas.drawString(43, 28, status)
        canvas.drawRightString(552, 28, f'Page {doc.page}')
        canvas.restoreState()
    doc = SimpleDocTemplate(str(target), pagesize=A4, rightMargin=43, leftMargin=43, topMargin=47, bottomMargin=53,
                            title=f'PONDEURMATCH Niveau 1 Match {mid:02d} - {mode}', author='PONDEURMATCH')
    doc.build(story, onFirstPage=page, onLaterPages=page)
    print(target.relative_to(ROOT))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('matches', type=int, nargs='+')
    parser.add_argument('--official', action='store_true')
    args = parser.parse_args()
    for m in args.matches:
        for mode in ('lecteur', 'arbitrage'):
            build(m, mode, args.official)
