#!/usr/bin/env python3
"""Build slides/match-population-status-to-objective.html from templates/slide-shell.html (shell version 2).

Usage: python3 deck2-generator.py <repo_root> <output_file>
The script keeps every tooltip text in one dictionary, so a term has the same text on every slide.
Tooltip texts that also appear in deck 1 are copied word for word from tools/deck1-generator.py.
"""
import re, sys, html, random

repo, out = sys.argv[1], sys.argv[2]
shell = open(f'{repo}/templates/slide-shell.html', encoding='utf-8').read()

TITLE = 'Match the disease status of a population to an objective'

# ------------------------------------------------------------------ tooltips
TIP = {
 # copied from deck 1
 'layer farm': 'A farm that keeps hens to produce eggs.',
 'pen': 'A small fenced area or house section where a group of animals is kept.',
 'Salmonella': 'A group of bacteria. They cause disease in animals and can reach people through eggs and meat.',
 'populations': 'Groups of animals that share a place or a system, such as all hens on one farm or all dogs in one village.',
 'interventions': 'Actions that prevent or control a disease, such as vaccination or separating sick animals.',
 # new in deck 2
 'population': 'A defined group of animals that share a place or a system, such as all hens on one farm or all dogs in one village.',
 'program coordinator': 'One of the graduate profiles of this study program. This veterinarian plans and runs animal health programs, for example for a regency government or a company.',
 'regency': 'An area of a province with its own local government. Most regencies are rural, so many farms are there.',
 'objective': 'What the work wants to achieve.',
 'state': 'How things are at one moment, for example whether a disease is present or absent.',
 'case': 'An animal that has the disease or health problem that you count.',
 'expected level': 'The usual level of disease in this population, based on earlier weeks or years. It is also called the baseline.',
 'evidence': 'Facts that show that something is true. For a disease, this is often a set of laboratory test results.',
 'agent': 'A living thing that causes disease, such as a bacterium or a virus.',
 'defined area': 'A place with clear borders, such as a farm, a regency, or a country.',
 'irregularly': 'Not in a fixed pattern. The cases come now and then.',
 'endemic': 'A disease that is always present at an expected level. Some texts about animals call this enzootic.',
 'epidemic': 'Many more cases than expected in a wide area. Some texts about animals call this an epizootic.',
 'pandemic': 'An epidemic that spreads across several countries or continents. Some texts about animals call this a panzootic.',
 'contain': 'To keep something inside a limit so that it cannot spread.',
 'trace': 'To follow the path of something to find where it came from or where it went.',
 'shelter': 'A place that cares for stray or unwanted animals until they find a home.',
 'canine distemper': 'A virus disease of dogs. It affects the lungs, the gut, and the nerves.',
 'signs': 'What an observer can see or measure in a sick animal, such as fever or a cough.',
 'test positive': 'The test result shows that the agent is present.',
 'objective of the work': 'What the veterinarian wants to achieve for the animals of this population.',
}
used_tips = []
def T(key, text=None):
    assert key in TIP, key
    used_tips.append(key)
    return f'<span class="term" data-tip="{html.escape(TIP[key], quote=True)}">{text or key}</span>'

# ------------------------------------------------------------------ meta
META = '''<script type="application/json" id="deck-meta">
{
  "title": "Match the disease status of a population to an objective",
  "domain": "D0",
  "competency": "C1",
  "skills": {
    "primary": "S1.3",
    "secondary": []
  },
  "minutes": 20,
  "articles": [
    "population-status-of-disease"
  ],
  "guides": [],
  "status": "draft",
  "updated": "2026-11-09"
}
</script>'''

# ------------------------------------------------------------------ styles
STYLES = '''<style id="deck-styles">
.case-layout { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.1fr); gap: 2.2rem; align-items: start; flex: 1; min-height: 0; padding-top: 0.6rem; }
.case-layout p + p { margin-top: 0.9rem; }
.case-layout p { font-size: 1.15rem; }
.small-note { color: var(--muted); font-size: 0.9rem; }
.penfig { margin: 0; padding: 0.4rem; display: grid; gap: 0.6rem; }
.penfig figcaption { color: var(--muted); font-size: 0.9rem; }
.penmap { display: grid; grid-template-columns: auto 1fr; gap: 0.6rem; align-items: stretch; }
.inlet { writing-mode: vertical-rl; transform: rotate(180deg); text-align: center; padding: 0.5rem 0.4rem; border: 1px solid var(--line); border-radius: 8px; background: var(--surface-2); font-weight: 600; font-size: 0.85rem; }
.pens { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0.5rem; }
.pen { border: 1px solid var(--line); border-radius: 8px; background: var(--surface); padding: 0.5rem 0.6rem; display: grid; gap: 0.1rem; }
.pen.hot { border: 2px solid var(--d2); background: var(--surface-2); }
.pen-id { font-size: 0.8rem; color: var(--muted); font-weight: 600; }
.pen-n { font-size: 1.6rem; font-weight: 700; font-variant-numeric: tabular-nums; line-height: 1.2; }

.fig-wrap { flex: 1; min-height: 0; display: flex; }
.fig-wrap .fig { height: 100%; width: 100%; }
.fig .dot-non { fill: var(--d1); }
.fig .dot-case { fill: var(--d2); stroke: var(--ink); stroke-width: 2; }
.fig .box-on { fill: var(--surface); stroke: var(--ink); stroke-width: 4; }
.fig .box-off { fill: var(--surface-2); stroke: var(--line); stroke-width: 1.5; }
.fig .bar-hot { fill: var(--d2); stroke: var(--ink); stroke-width: 2; }
.fig .bar-n { fill: var(--d1); }
.fig .exp-line { fill: none; stroke: var(--ink); stroke-width: 2; stroke-dasharray: 6 5; }
.fig .dim { opacity: 0.38; }

.vcenter { justify-content: center; }
.big-def { font-size: 2.5rem; line-height: 1.3; font-weight: 600; letter-spacing: -0.01em; margin-top: 0.6rem; }
.under-fig { font-size: 1.15rem; }

.st-row { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.4rem; }
.st-row > div { border-top: 2px solid var(--muted); padding-top: 0.5rem; display: grid; gap: 0.25rem; align-content: start; }
.st-row h3 { margin: 0; font-size: 1.1rem; font-weight: 600; }
.st-row p { font-size: 1.05rem; }

.ex-layout { display: grid; grid-template-columns: minmax(0, 0.8fr) minmax(0, 1.4fr); gap: 1.6rem; flex: 1; min-height: 0; align-items: start; }
.ex-layout .fig { width: 100%; height: auto; max-height: 100%; }
.ex-table { border-collapse: collapse; width: 100%; font-size: 1.02rem; }
.ex-table th, .ex-table td { text-align: left; padding: 0.45rem 0.7rem; border-bottom: 1px solid var(--line); vertical-align: top; }
.ex-table thead th { border-bottom: 2px solid var(--muted); font-weight: 600; }
.ex-table tbody th { font-weight: 600; color: var(--muted); width: 7.2rem; }

.practice-note { color: var(--muted); font-size: 0.95rem; }
.sorter { flex: none; }
.sorter-pool { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); }
.sorter-pool .sort-card { font-size: 0.9rem; }
.sort-why { font-size: 1.02rem; color: var(--muted); }

.bd-rows { display: grid; gap: 0.9rem; }
.bd-row { display: grid; gap: 0.35rem; padding-bottom: 0.7rem; border-bottom: 1px solid var(--line); }
.bd-row p { font-size: 1.1rem; }
.bd-fill { line-height: 2.2; }
.bd-fill select { font: inherit; font-size: 1.05rem; padding: 0.25rem 0.5rem; border: 1.5px solid var(--muted); border-radius: 8px; background: var(--surface); color: var(--ink); max-width: 100%; }
.bd-fill select.is-correct { border-color: var(--ok); }
.bd-fill select.is-wrong { border-color: var(--bad); }
.bd-given { font-weight: 600; }
.bd-actions { display: flex; flex-wrap: wrap; gap: 0.6rem; align-items: center; }
.bd-why { display: grid; gap: 0.35rem; color: var(--muted); font-size: 1rem; }
.quote { font-size: 1.3rem; line-height: 1.45; }
.q-label { font-weight: 600; font-size: 1.15rem; }

.xp-layout { display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr); gap: 1.8rem; flex: 1; min-height: 0; align-items: center; }
.xp-layout .fig { width: 100%; height: auto; max-height: 100%; }
.xp-read { display: grid; gap: 0.8rem; align-content: center; }
.xp-chips { display: grid; gap: 0.4rem; }
.xp-chip { border: 1.5px solid var(--line); border-radius: 8px; padding: 0.35rem 0.7rem; color: var(--muted); font-size: 0.98rem; }
.xp-chip.is-on { border: 3px solid var(--ink); color: var(--ink); font-weight: 600; padding: 0.3rem 0.65rem; }
.xp-stage { color: var(--muted); font-size: 0.95rem; }
.xp-status { font-size: 2rem; font-weight: 700; line-height: 1.15; letter-spacing: -0.01em; }
.xp-line { font-size: 1.1rem; }
.xp-label { font-weight: 600; }
.xp-work { color: var(--muted); font-size: 1rem; }

@media (max-width: 900px) {
  .case-layout, .ex-layout, .xp-layout { grid-template-columns: 1fr; }
  .st-row { grid-template-columns: 1fr; }
}
</style>'''

# ------------------------------------------------------------------ figures
def dots(x, y, w, h, cols, rows, ncase, seed, sp=28, r=9):
    n = cols * rows
    cases = set(random.Random(seed).sample(range(n), ncase))
    bw, bh = (cols - 1) * sp + 2 * r, (rows - 1) * sp + 2 * r
    x0, y0 = x + (w - bw) / 2, y + (h - bh) / 2
    parts = []
    for i in range(n):
        cx = x0 + r + (i % cols) * sp
        cy = y0 + r + (i // cols) * sp
        parts.append(f'<circle class="{"dot-case" if i in cases else "dot-non"}" cx="{cx:.1f}" cy="{cy:.1f}" r="{r}"/>')
    return ''.join(parts)

def label(x, y, lines, cls='', anchor='middle'):
    out = []
    for i, ln in enumerate(lines):
        out.append(f'<text x="{x}" y="{y + i*20}" text-anchor="{anchor}" class="{cls}">{ln}</text>')
    return ''.join(out)

def figure(mode, hl=None, obj=False, alt=''):
    """mode 'two' or 'three'. hl: index of the highlighted box. obj: draw the objective labels."""
    by, bh = 54, 190
    if mode == 'two':
        boxes = [(0, 340, 'Disease absent', ['Disease absent'], 0, 11, 6),
                 (380, 340, 'Disease present', ['Disease present'], 14, 11, 6)]
        cols_rows = (11, 6)
    else:
        boxes = [(0, 226, '', ['Disease absent'], 0, 7, 6),
                 (247, 226, '', ['Present at an expected', 'or low level'], 4, 7, 6),
                 (494, 226, '', ['Present above the', 'expected level'], 20, 7, 6)]
    parts = []
    for i, (x, w, _, title, nc, cols, rows) in enumerate(boxes):
        dim = hl is not None and i != hl
        cls = 'box-on' if (hl is not None and i == hl) else ('box-off' if hl is not None else 'f-soft')
        g = [f'<rect class="{cls}" x="{x}" y="{by}" width="{w}" height="{bh}" rx="12"/>', dots(x, by, w, bh, cols, rows, nc, 11 + i)]
        head = label(x + w / 2, 36 if len(title) == 1 else 20, title, 't-strong')
        parts.append(f'<g class="{"dim" if dim else ""}">{"".join(g)}</g>{head}')
    h = 292
    if obj:
        if mode == 'two':
            parts.append(f'<path class="f-line" d="M0 252 V260 H340 V252"/>' + label(170, 283, ['Objective: prevent any case']))
            parts.append(f'<path class="f-line" d="M380 252 V260 H720 V252"/>' + label(550, 283, ['Objective: reduce the cases,', 'and eliminate the disease if possible']))
        else:
            parts.append(f'<path class="f-line" d="M0 252 V260 H226 V252"/>' + label(113, 283, ['Objective:', 'prevent any case']))
            parts.append(f'<path class="f-line" d="M247 252 V260 H720 V252"/>' + label(483, 283, ['Objective: reduce the cases,', 'and eliminate the disease if possible']))
        ky = 338; h = 350
    else:
        ky = 276
    key = (f'<circle class="dot-case" cx="12" cy="{ky-5}" r="9"/><text x="28" y="{ky}">Case</text>'
           f'<circle class="dot-non" cx="100" cy="{ky-5}" r="9"/><text x="116" y="{ky}">Non-case</text>')
    return (f'<svg class="fig" viewBox="0 0 720 {h}" role="img" aria-label="{html.escape(alt, quote=True)}">'
            + ''.join(parts) + key + '</svg>')

ALT3 = 'Three boxes of circles. Each circle is one animal. Left box: no animal is a case. Middle box: a few animals are cases. Right box: many animals are cases.'
ALT3H = ALT3 + ' One box has a thick border and shows the group of this slide.'

def pen_fig():
    return '''<figure class="penfig" data-detail="d-pens" tabindex="0" aria-label="Deaths in one week by pen. Pens A1 and B1, next to the water inlet, had 90 of the 120 deaths. Select for details.">
      <div class="penmap">
        <div class="inlet">Water inlet</div>
        <div class="pens">
          <div class="pen hot"><span class="pen-id">Pen A1</span><span class="pen-n">50</span></div>
          <div class="pen"><span class="pen-id">Pen A2</span><span class="pen-n">5</span></div>
          <div class="pen"><span class="pen-id">Pen A3</span><span class="pen-n">5</span></div>
          <div class="pen"><span class="pen-id">Pen A4</span><span class="pen-n">5</span></div>
          <div class="pen hot"><span class="pen-id">Pen B1</span><span class="pen-n">40</span></div>
          <div class="pen"><span class="pen-id">Pen B2</span><span class="pen-n">5</span></div>
          <div class="pen"><span class="pen-id">Pen B3</span><span class="pen-n">5</span></div>
          <div class="pen"><span class="pen-id">Pen B4</span><span class="pen-n">5</span></div>
        </div>
      </div>
      <figcaption>Deaths in one week, by pen</figcaption>
    </figure>'''

def week_chart():
    vals = [9, 11, 10, 8, 12, 10, 120]
    base, x0, w, gap, sc = 250, 40, 34, 8, 1.6
    p = []
    for i, v in enumerate(vals):
        x = x0 + i * (w + gap); hh = v * sc
        p.append(f'<rect class="{"bar-hot" if v > 100 else "bar-n"}" x="{x}" y="{base-hh:.1f}" width="{w}" height="{hh:.1f}" rx="3"/>')
        if v > 100: p.append(f'<text x="{x+w/2}" y="{base-hh-6:.1f}" text-anchor="middle">{v}</text>')
        p.append(f'<text x="{x+w/2}" y="{base+20}" text-anchor="middle" class="t-muted">{i+1}</text>')
    ey = base - 10 * sc
    p.append(f'<line class="f-line" x1="{x0-6}" y1="{base}" x2="{x0+7*(w+gap)-gap+6}" y2="{base}"/>')
    p.append(f'<line class="exp-line" x1="{x0-6}" y1="{ey}" x2="{x0+7*(w+gap)-gap+6}" y2="{ey}"/>')
    p.append(f'<text x="{x0}" y="{ey-12}" class="t-strong">Expected level: about 10</text>')
    p.append(f'<text x="{x0+ (7*(w+gap)-gap)/2}" y="{base+44}" text-anchor="middle" class="t-muted">Deaths per week, weeks 1 to 7</text>')
    return ('<svg class="fig" viewBox="0 0 360 300" role="img" '
            'aria-label="Bar chart of deaths per week on the layer farm. Weeks 1 to 6 have between 8 and 12 deaths, close to the expected level of about 10. Week 7 has 120 deaths.">'
            + ''.join(p) + '</svg>')

# ------------------------------------------------------------------ slides
S = []

S.append(f'''
<!-- Slide 1: Title -->
<section class="slide" data-type="title" data-title="Match the disease status of a population to an objective">
  <p class="code">C1 Epidemiological and economic thinking</p>
  <h1>{TITLE}</h1>
  <p class="lead">What should a veterinarian work toward when a disease is in a {T('population')}, and when it is not?</p>
  <ul class="meta-list">
    <li><span class="code">S1.3</span><span>Match the population status of a disease to an objective</span></li>
    <li><span class="code">Time</span><span>About 20 minutes</span></li>
    <li><span class="code">Before</span><span><a href="./explain-epidemiology.html">Explain epidemiology</a></span></li>
  </ul>
  <div class="notes">Read the guiding question aloud. Ask for a first answer in one sentence. Students return to this answer at the end of the deck.</div>
</section>''')

S.append(f'''
<!-- Slide 2: Recap of the anchor case -->
<section class="slide" data-type="recap" data-title="The case">
  <h2>The case: Salmonella on a layer farm</h2>
  <div class="case-layout">
    <div>
      <p>In one week, 120 of the 8,000 hens on a {T('layer farm')} die. 90 of the dead hens come from {T('pen', 'pens')} A1 and B1, next to the water inlet.</p>
      <p>The laboratory later finds {T('Salmonella')} in the hens, and eggs from these pens have already reached buyers.</p>
      <p>You are the {T('program coordinator')} at the animal health service of the {T('regency')}.</p>
    </div>
    {pen_fig()}
  </div>
  <div class="notes">Ask what the coordinator should work toward on the farm. Keep the answers for the next slide.</div>
</section>''')

S.append(f'''
<!-- Slide 3: Question, predict -->
<section class="slide" data-type="question" data-title="Predict first">
  <h2>Salmonella is now on the farm. Which {T('objective')} fits the farm?</h2>
  <p>Choose your prediction.</p>
  <ul class="choices" data-choice="predict">
    <li><button class="choice" data-value="a"><span class="key">A</span>Prevent any case of Salmonella on the farm</button></li>
    <li><button class="choice" data-value="b"><span class="key">B</span>Reduce the cases and stop the spread to other pens</button></li>
    <li><button class="choice" data-value="c"><span class="key">C</span>Show with tests that the farm is free of Salmonella</button></li>
  </ul>
  <p class="verdict" id="predict-note" aria-live="polite"></p>
  <div class="notes">Let students choose, then ask a student to explain the choice. Options A and C are the two usual mistakes: they treat a farm with the disease like a farm without it.</div>
</section>''')

S.append(f'''
<!-- Slide 4: Concept, the definition -->
<section class="slide vcenter" data-type="concept" data-title="Population status">
  <h2>Population status</h2>
  <p class="big-def">The population status of a disease is the {T('state')} of that disease in a {T('population')} at a given time.</p>
  <p class="small-note">Hover over or tap a dotted word.</p>
  <div class="notes">Read the definition aloud. The next slides show what a state can be, using boxes of animals.</div>
</section>''')

S.append(f'''
<!-- Slide 5: Concept, two boxes -->
<section class="slide" data-type="concept" data-title="Absent or present">
  <h2>A disease is absent or present in a population</h2>
  <div class="fig-wrap">{figure('two', alt='Two boxes of circles. Each circle is one animal. Left box, disease absent: no animal is a case. Right box, disease present: some animals are cases.')}</div>
  <p class="under-fig">Each box is one {T('population')}, and each circle is one animal. In the left box, no animal is a {T('case')}. In the right box, some animals are cases.</p>
  <div class="notes">Point to the two kinds of circle in the key. Ask which box looks like the farm on the case slide.</div>
</section>''')

S.append(f'''
<!-- Slide 6: Concept, the two objectives -->
<section class="slide" data-type="concept" data-title="Two objectives">
  <h2>The objective depends on whether the disease is there</h2>
  <div class="fig-wrap">{figure('two', obj=True, alt='The same two boxes as before, with an objective under each box. Disease absent: prevent any case. Disease present: reduce the cases, and eliminate the disease if possible.')}</div>
  <p class="under-fig">The {T('objective of the work')} in a population follows from the box. To eliminate a disease means to remove it from an area, so that no case occurs there.</p>
  <div class="notes">Ask students to say each objective aloud in their own words. Return to the prediction on slide 3 and ask which box the farm belongs to.</div>
</section>''')

S.append(f'''
<!-- Slide 7: Concept, present splits in two -->
<section class="slide" data-type="concept" data-title="Present: two kinds">
  <h2>Present at the expected level, or above it</h2>
  <div class="fig-wrap">{figure('three', obj=True, alt=ALT3 + ' Under the left box: prevent any case. Under the other two boxes: reduce the cases, and eliminate the disease if possible.')}</div>
  <p class="under-fig">The box on the right has more cases than the {T('expected level')} for this population. The box in the middle has the expected number of cases or fewer.</p>
  <div class="notes">Ask: which box is the farm in the week with 120 deaths? Why does the expected level matter for the answer?</div>
</section>''')

def stat(name, desc):
    return f'<div><h3>{name}</h3><p>{desc}</p></div>'

S.append(f'''
<!-- Slide 8: Concept, group 1 -->
<section class="slide" data-type="concept" data-title="Statuses: disease absent">
  <h2>Statuses: disease absent or not established</h2>
  <div class="fig-wrap" data-detail="d-g1">{figure('three', hl=0, obj=True, alt=ALT3H + ' The left box is the group of this slide. Select for details.')}</div>
  <div class="st-row">
    {stat('Free', f'The disease is absent, and {T("evidence")} shows it.')}
    {stat('Exposed, disease not established', f'The {T("agent")} has entered the population, but the disease does not keep spreading.')}
    {stat('Eliminated', f'The disease is removed from a {T("defined area")}. {T("interventions", "Interventions")} continue to prevent its return.')}
  </div>
  <div class="notes">Ask which of the three statuses needs the most evidence. Free and eliminated both need tests that would find the disease.</div>
</section>''')

S.append(f'''
<!-- Slide 9: Concept, group 2 -->
<section class="slide" data-type="concept" data-title="Statuses: expected or low level">
  <h2>Statuses: present at an expected or low level</h2>
  <div class="fig-wrap" data-detail="d-g2">{figure('three', hl=1, obj=True, alt=ALT3H + ' The middle box is the group of this slide. Select for details.')}</div>
  <div class="st-row">
    {stat('Sporadic', f'Single cases or small groups of cases occur {T("irregularly")}.')}
    {stat(T('endemic', 'Endemic'), 'The disease is always present at the expected level.')}
    {stat('Under control', f'{T("interventions", "Interventions")} keep the cases at a low level. The work goes on until the disease is eliminated.')}
  </div>
  <div class="notes">Sporadic and endemic describe a pattern of occurrence. Under control describes the result of interventions.</div>
</section>''')

S.append(f'''
<!-- Slide 10: Concept, group 3 -->
<section class="slide" data-type="concept" data-title="Statuses: above the expected level">
  <h2>Statuses: present above the expected level</h2>
  <div class="fig-wrap" data-detail="d-g3">{figure('three', hl=2, obj=True, alt=ALT3H + ' The right box is the group of this slide. Select for details.')}</div>
  <div class="st-row">
    {stat('Outbreak', f'Cases are above the {T("expected level")} in a limited place and a limited time.')}
    {stat(T('epidemic', 'Epidemic'), 'Cases are clearly above the expected level in a wider area or a larger population.')}
    {stat(T('pandemic', 'Pandemic'), 'An epidemic spreads across several countries or continents.')}
  </div>
  <div class="notes">The three statuses differ in the size of the place and the time. All three need a comparison with the expected level.</div>
</section>''')

S.append(f'''
<!-- Slide 11: Example -->
<section class="slide" data-type="example" data-title="Work through the farm case">
  <h2>Work through the farm case</h2>
  <div class="ex-layout">
    {week_chart()}
    <table class="ex-table">
      <thead><tr><th scope="col">Step</th><th scope="col">What the coordinator does, and why</th></tr></thead>
      <tbody>
        <tr><th scope="row">Population</th><td>The hens of the layer farm in the last week. A status belongs to one population and one time.</td></tr>
        <tr><th scope="row">Compare</th><td>120 hens die, and the {T('expected level')} is about 10. A status compares the present with the expected level.</td></tr>
        <tr><th scope="row">Status</th><td>Outbreak. The cases are above the expected level, in one farm and one week.</td></tr>
        <tr><th scope="row">Objective</th><td>Reduce the cases: {T('contain')} the disease and find the source. The disease is present.</td></tr>
        <tr><th scope="row">Action</th><td>Separate pens A1 and B1, test the water, and {T('trace')} the buyers of the eggs.</td></tr>
        <tr><th scope="row">Other farms</th><td>The status is unknown until the laboratory tests them. A lack of reports does not show that they are free.</td></tr>
      </tbody>
    </table>
  </div>
  <div class="notes">Go through the six rows from top to bottom. At row 2, point to week 7 in the chart and to the dashed line. A reliable expected level needs several years of good data from the same population.</div>
</section>''')

S.append('''
<!-- Slide 12: Practice with support, sort scenarios into three groups -->
<section class="slide" data-type="practice" data-title="Sort the scenarios">
  <h2>Drag each scenario into the right box</h2>
  <div class="sorter" data-sorter data-explain="d-sort" data-explain-always="1">
    <div class="sorter-pool" aria-label="Cards to sort">
      <button class="sort-card" data-target="c2">Laboratory tests find Salmonella in hens of Regency B every year, at about the same level.</button>
      <button class="sort-card" data-target="c3">In one farm of Regency C, 100 hens die in a week. The expected number is 10.</button>
      <button class="sort-card" data-target="c1">In Regency A, veterinarians test layer farms every year. For five years, all results are negative.</button>
      <button class="sort-card" data-target="c3">Salmonella spreads to farms in many parts of Regency F. Deaths are clearly above the expected number.</button>
      <button class="sort-card" data-target="c2">Two farms in Regency D had Salmonella in two years. The farms are far apart and have no link.</button>
      <button class="sort-card" data-target="c1">Many farms in Regency E had Salmonella. After a control program, no case has occurred for five years, and veterinarians continue to test.</button>
    </div>
    <div class="sorter-bins">
      <div class="sort-bin" data-bin="c1"><h3>Disease absent or not established</h3><div class="sort-drop"></div></div>
      <div class="sort-bin" data-bin="c2"><h3>Present at an expected or low level</h3><div class="sort-drop"></div></div>
      <div class="sort-bin" data-bin="c3"><h3>Present above the expected level</h3><div class="sort-drop"></div></div>
    </div>
    <div class="sorter-actions">
      <button class="btn btn-main" data-sorter-check>Check the sorting</button>
      <button class="btn" data-sorter-reset>Start again</button>
      <span class="verdict" role="status" aria-live="polite"></span>
    </div>
  </div>
  <div class="notes">Students work in pairs. If a pair places a card wrongly, ask them to read the box title and the card again, and to look for the expected level.</div>
</section>''')

STATUS_OPTS = [('free', 'Free'), ('exposed', 'Exposed, disease not established'), ('sporadic', 'Sporadic'), ('endemic', 'Endemic'),
               ('outbreak', 'Outbreak'), ('epidemic', 'Epidemic'), ('pandemic', 'Pandemic'), ('under', 'Under control'), ('elim', 'Eliminated')]
OBJ_OPTS = [('prevent', 'Prevent any case'), ('reduce', 'Reduce the cases')]
def select(id_, opts, label):
    o = '<option value="">Choose</option>' + ''.join(f'<option value="{k}">{v}</option>' for k, v in opts)
    return f'<select id="{id_}" aria-label="{label}">{o}</select>'

S.append(f'''
<!-- Slide 13: Practice, complete the statements -->
<section class="slide" data-type="practice" data-title="Complete the statements">
  <h2>Complete each statement</h2>
  <div class="bd-rows">
    <div class="bd-row">
      <p>1. Laboratory tests find Salmonella in chicks that arrive at one farm of Regency G. The farm owner removes all the chicks at once, and no hen gets the disease.</p>
      <p class="bd-fill">The status is <span class="bd-given">exposed, disease not established</span>. The objective is {select('r1o', OBJ_OPTS, 'Objective for statement 1')}.</p>
    </div>
    <div class="bd-row">
      <p>2. The number of Salmonella cases in Regency H stays low because of a control program. Cases still occur.</p>
      <p class="bd-fill">The status is {select('r2s', STATUS_OPTS, 'Status for statement 2')}. The objective is {select('r2o', OBJ_OPTS, 'Objective for statement 2')}.</p>
    </div>
    <div class="bd-row">
      <p>3. Veterinarians removed Salmonella from all layer farms of Regency K three years ago. Tests continue, and all results are negative.</p>
      <p class="bd-fill">The status is {select('r3s', STATUS_OPTS, 'Status for statement 3')}. The objective is {select('r3o', OBJ_OPTS, 'Objective for statement 3')}.</p>
    </div>
  </div>
  <div class="bd-actions">
    <button class="btn btn-main" id="bd-check">Check the statements</button>
    <button class="btn" id="bd-reset">Start again</button>
    <span class="verdict" id="bd-verdict" aria-live="polite"></span>
  </div>
  <div class="bd-why" id="bd-why"></div>
  <div class="notes">In statement 1 the status is given, so students only choose the objective. In statements 2 and 3 they choose both. Statement 2 is the usual mistake: the disease is present, so the objective is to reduce the cases.</div>
</section>''')

S.append(f'''
<!-- Slide 14: Practice, find the error -->
<section class="slide" data-type="practice" data-title="Find the error">
  <h2>Find the error</h2>
  <p>A student writes a note about Regency C.</p>
  <p class="quote">"No farm of Regency C has reported Salmonella in five years. The status of Regency C is free."</p>
  <p class="q-label">What does the student need before writing that the status is free?</p>
  <div>
    <ul class="choices" data-check="q0" data-answer="a" data-explain="d-q0">
      <li><button class="choice" data-value="a"><span class="key">A</span>Tests that would find Salmonella if it were present</button></li>
      <li><button class="choice" data-value="b"><span class="key">B</span>Reports from farm owners that their hens look healthy</button></li>
      <li><button class="choice" data-value="c"><span class="key">C</span>A list of farms that bought chicks from other regencies</button></li>
    </ul>
    <p class="verdict" aria-live="polite"></p>
  </div>
  <div class="notes">The note takes a lack of reports as evidence. Ask students who would report if no one tests.</div>
</section>''')

S.append('''
<!-- Slide 15: Explore, one farm in five stages -->
<section class="slide" data-type="explore" data-title="Follow one farm" data-panel="controls">
  <h2>Follow one farm through five stages</h2>
  <div class="xp-layout">
    <svg class="fig" id="xp-fig" viewBox="0 0 420 300" role="img" aria-label="A box of circles that shows one layer farm. Each circle is one animal. The number of cases changes with the stage."></svg>
    <div class="xp-read" aria-live="polite">
      <div class="xp-chips" id="xp-chips">
        <span class="xp-chip" data-g="0">Disease absent</span>
        <span class="xp-chip" data-g="1">Present at an expected or low level</span>
        <span class="xp-chip" data-g="2">Present above the expected level</span>
      </div>
      <p class="xp-stage" id="xp-stage"></p>
      <p class="xp-status" id="xp-status"></p>
      <p class="xp-line"><span class="xp-label">Objective: </span><span id="xp-obj"></span></p>
      <p class="xp-work" id="xp-work"></p>
      <p class="xp-line" id="xp-text"></p>
    </div>
  </div>
  <p class="practice-note">Move the slider in the panel. Before you read the status, say the objective.</p>
  <div class="notes">Move the slider one stage at a time. At each stage, ask the class for the status and the objective first. Point out that the status goes up and then down.</div>
</section>''')

S.append('''
<!-- Slide 16: Check 1 -->
<section class="slide" data-type="check" data-title="Check: the status">
  <div>
    <h2>Salmonella spreads from the farm. Deaths are far above the expected number on 12 farms in many parts of the regency. Which status fits?</h2>
    <ul class="choices" data-check="q1" data-answer="c" data-explain="d-q1">
      <li><button class="choice" data-value="a"><span class="key">A</span>Outbreak</button></li>
      <li><button class="choice" data-value="b"><span class="key">B</span>Endemic</button></li>
      <li><button class="choice" data-value="c"><span class="key">C</span>Epidemic</button></li>
    </ul>
    <p class="verdict" aria-live="polite"></p>
  </div>
</section>''')

S.append(f'''
<!-- Slide 17: Check 2 -->
<section class="slide" data-type="check" data-title="Check: the objective">
  <div>
    <h2>Regency C is free of Salmonella, and test results show it. A truck brings chicks from Regency A, where Salmonella is {T('endemic')}. Which objective fits Regency C?</h2>
    <ul class="choices" data-check="q2" data-answer="a" data-explain="d-q2">
      <li><button class="choice" data-value="a"><span class="key">A</span>Prevent any case of Salmonella in Regency C</button></li>
      <li><button class="choice" data-value="b"><span class="key">B</span>Reduce the cases of Salmonella in Regency C</button></li>
      <li><button class="choice" data-value="c"><span class="key">C</span>Find the source of the cases in Regency C</button></li>
    </ul>
    <p class="verdict" aria-live="polite"></p>
  </div>
</section>''')

S.append(f'''
<!-- Slide 18: Check 3, transfer -->
<section class="slide" data-type="check" data-title="Check: a new case">
  <h2>A new case: an animal shelter</h2>
  <p>A {T('shelter')} has had no case of {T('canine distemper')} for two years. In four days, 6 of its 50 dogs show {T('signs')} of the disease, and 3 {T('test positive')}.</p>
  <p class="q-label">Which status and objective fit best?</p>
  <div>
    <ul class="choices" data-check="q3" data-answer="b" data-explain="d-q3">
      <li><button class="choice" data-value="a"><span class="key">A</span>Free. Prevent any case of the disease in the shelter.</button></li>
      <li><button class="choice" data-value="b"><span class="key">B</span>Outbreak. Contain the disease and find the source.</button></li>
      <li><button class="choice" data-value="c"><span class="key">C</span>Endemic. Reduce the cases over the next few years.</button></li>
    </ul>
    <p class="verdict" aria-live="polite"></p>
  </div>
</section>''')

S.append('''
<!-- Slide 19: Summary -->
<section class="slide" data-type="summary" data-title="Summary">
  <h2>Key points</h2>
  <ul>
    <li>The population status of a disease is the state of that disease in a population at a given time.</li>
    <li>When the disease is absent, the objective is to prevent any case. When it is present, the objective is to reduce the cases and, where possible, to eliminate the disease.</li>
    <li>A disease that is present is at an expected or low level, or above the expected level. The nine statuses give each group more exact names.</li>
    <li>A status compares the present with the expected level of one population, and it can change in both directions.</li>
    <li>A lack of reports does not show that a disease is absent. Free needs evidence from tests.</li>
  </ul>
  <div class="links">
    <a class="btn" href="../encyclopedia/population-status-of-disease.html">Read the article: Population status of disease</a>
    <a class="btn btn-main" href="./explain-veterinary-economics.html">Open the next deck: Explain veterinary economics</a>
  </div>
</section>''')

DETAILS = '''
<!-- Details: one template per element with data-detail or data-explain -->
<template id="d-pens">
  <h3>About these data</h3>
  <p>The flock has 8,000 hens in 8 pens. In a flock of this size, about 10 hens normally die in one week.</p>
  <p>Pens A1 and B1 are next to the water inlet. They had 90 of the 120 deaths. The other six pens had 5 deaths each.</p>
</template>
<template id="d-g1">
  <h3>Typical work for each status</h3>
  <p>Free: prevent the introduction of the disease and keep the population free.</p>
  <p>Exposed, disease not established: prevent the disease from becoming established.</p>
  <p>Eliminated: prevent the disease from coming back.</p>
  <p>In all three statuses the disease is absent or not established, so the objective is to prevent any case.</p>
</template>
<template id="d-g2">
  <h3>Typical work for each status</h3>
  <p>Sporadic: reduce the cases and find the source of each case.</p>
  <p>Endemic: reduce the cases, control the disease, and work toward elimination.</p>
  <p>Under control: keep the gains and complete the elimination.</p>
  <p>Sporadic and endemic describe a pattern of occurrence. Under control describes the result of interventions.</p>
</template>
<template id="d-g3">
  <h3>Typical work for each status</h3>
  <p>Outbreak: contain the disease, find the source, and stop the spread.</p>
  <p>Epidemic: control the spread and reduce the impact.</p>
  <p>Pandemic: control the spread and coordinate the work across countries.</p>
  <p>Outbreak and epidemic describe a change from the expected level. The words for animals, epizootic and panzootic, have the same meaning.</p>
</template>
<template id="d-sort">
  <h3>The status of each scenario</h3>
  <p>Regency A: free. The test results are negative, so the disease is absent.</p>
  <p>Regency E: eliminated. The disease is removed, and the tests continue to find any return.</p>
  <p>Regency B: endemic. The disease is always present at the expected level.</p>
  <p>Regency D: sporadic. The cases are single and have no link.</p>
  <p>Regency C: outbreak. The deaths are above the expected number in one farm and one week.</p>
  <p>Regency F: epidemic. The deaths are above the expected number in many parts of the regency.</p>
</template>
<template id="d-q0">
  <h3>Answer: A</h3>
  <p>A status of free needs evidence. A lack of reports can mean that no farm has the disease, or that no one tests and no one reports.</p>
  <p>Only tests that would find Salmonella if it were present show that the disease is absent.</p>
</template>
<template id="d-q1">
  <h3>Answer: C, Epidemic</h3>
  <p>The cases are above the expected level in a wide area. An outbreak has a limited place and time.</p>
  <p>Endemic means that the disease is always present at the expected level. That does not fit deaths far above the expected number.</p>
</template>
<template id="d-q2">
  <h3>Answer: A</h3>
  <p>Regency C is free, so the disease is absent. The objective is to prevent any case, for example by checking the chicks that arrive.</p>
  <p>Reducing the cases and finding the source of cases fit a population in which the disease is present.</p>
</template>
<template id="d-q3">
  <h3>Answer: B, Outbreak</h3>
  <p>The shelter was free for two years, so the expected level was zero. Now cases appear in one place and one week, which is an outbreak.</p>
  <p>The disease is present, so the objective is to reduce the cases: contain the disease and find the source. Free and endemic do not fit.</p>
</template>
'''

CONTROLS = '''<!-- Controls: one block per slide with data-panel="controls". data-for-slide is the slide number. -->
<div class="controls" data-for-slide="15" hidden>
  <div class="control"><label for="in-stage">Stage <output id="out-stage">1</output></label><input type="range" id="in-stage" min="1" max="5" step="1" value="1"></div>
  <button class="btn" data-reset>Reset the controls</button>
</div>
'''

SCRIPT = '''<script id="deck-script">
(function () {
  const $ = id => document.getElementById(id);

  // Slide 3: explain the best answer after a prediction
  const note = $('predict-note');
  document.querySelectorAll('[data-choice="predict"] .choice').forEach(b => b.addEventListener('click', () => {
    note.className = 'verdict';
    note.textContent = 'Option B is the best answer. Salmonella is already on the farm, so the work is to reduce the cases and stop the spread. Options A and C fit a population in which the disease is absent.';
  }));

  // Slide 13: complete the statements
  const rows = [
    { sel: ['r1o'], ans: ['prevent'], why: 'Statement 1: Salmonella has entered, but no hen has the disease and it does not spread. The disease is absent or not established, so the objective is to prevent any case.' },
    { sel: ['r2s', 'r2o'], ans: ['under', 'reduce'], why: 'Statement 2: the status is under control. Cases still occur at a low level, so the disease is present. The objective is to reduce the cases until the disease is eliminated.' },
    { sel: ['r3s', 'r3o'], ans: ['elim', 'prevent'], why: 'Statement 3: the status is eliminated. The disease is removed and the tests continue, so the disease is absent. The objective is to prevent it from coming back.' }
  ];
  const allSel = rows.flatMap(r => r.sel.map($));
  function bdClear() {
    allSel.forEach(s => s.classList.remove('is-correct', 'is-wrong'));
    $('bd-verdict').textContent = ''; $('bd-verdict').className = 'verdict'; $('bd-why').innerHTML = '';
  }
  allSel.forEach(s => s.addEventListener('change', bdClear));
  $('bd-check').addEventListener('click', () => {
    if (allSel.some(s => !s.value)) { $('bd-verdict').textContent = 'Choose an answer for every gap first.'; $('bd-verdict').className = 'verdict bad'; return; }
    const why = $('bd-why'); why.innerHTML = ''; let okRows = 0;
    rows.forEach(r => {
      let rowOk = true;
      r.sel.forEach((id, i) => {
        const el = $(id), right = el.value === r.ans[i];
        el.classList.toggle('is-correct', right); el.classList.toggle('is-wrong', !right);
        if (!right) rowOk = false;
      });
      if (rowOk) okRows++; else { const p = document.createElement('p'); p.textContent = r.why; why.appendChild(p); }
    });
    const all = okRows === rows.length;
    $('bd-verdict').textContent = all ? 'All 3 statements are correct.' : okRows + ' of 3 statements are correct. Change the gaps marked in red and check again.';
    $('bd-verdict').className = 'verdict ' + (all ? 'ok' : 'bad');
  });
  $('bd-reset').addEventListener('click', () => { allSel.forEach(s => { s.value = ''; }); bdClear(); });

  // Slide 15: one farm in five stages
  const stages = [
    { status: 'Free', g: 0, obj: 'Prevent any case', work: 'Typical work: prevent the introduction of the disease and keep the farm free.', n: 0, text: 'Tests of the farm are all negative. No hen has Salmonella.' },
    { status: 'Exposed, disease not established', g: 0, obj: 'Prevent any case', work: 'Typical work: prevent the disease from becoming established.', n: 1, text: 'Salmonella enters with new chicks. One hen is a case, and the disease does not keep spreading.' },
    { status: 'Outbreak', g: 2, obj: 'Reduce the cases', work: 'Typical work: contain the disease, find the source, and stop the spread.', n: 20, text: 'Many hens are cases. The number of cases is far above the expected level.' },
    { status: 'Under control', g: 1, obj: 'Reduce the cases', work: 'Typical work: keep the gains and complete the elimination.', n: 4, text: 'Interventions bring the cases down to a low level and keep them there.' },
    { status: 'Eliminated', g: 0, obj: 'Prevent any case', work: 'Typical work: prevent the disease from coming back.', n: 0, text: 'No case occurs. Veterinarians continue to test to find any return of Salmonella.' }
  ];
  function rng(a) { return function () { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  const COLS = 12, ROWS = 7, N = COLS * ROWS, order = Array.from({ length: N }, (_, i) => i);
  const rand = rng(7);
  for (let i = N - 1; i > 0; i--) { const j = Math.floor(rand() * (i + 1)); [order[i], order[j]] = [order[j], order[i]]; }
  const fig = $('xp-fig'), inStage = $('in-stage');
  function drawFarm(n) {
    const cases = new Set(order.slice(0, n)), sp = 28, r = 9, bw = 400, bh = 234, x = 10, y = 50;
    const gw = (COLS - 1) * sp + 2 * r, gh = (ROWS - 1) * sp + 2 * r, x0 = x + (bw - gw) / 2, y0 = y + (bh - gh) / 2;
    let s = '<rect class="f-soft" x="' + x + '" y="' + y + '" width="' + bw + '" height="' + bh + '" rx="12"/>';
    s += '<text x="' + (x + bw / 2) + '" y="34" text-anchor="middle" class="t-strong">One layer farm</text>';
    for (let i = 0; i < N; i++) {
      s += '<circle class="' + (cases.has(i) ? 'dot-case' : 'dot-non') + '" cx="' + (x0 + r + (i % COLS) * sp) + '" cy="' + (y0 + r + Math.floor(i / COLS) * sp) + '" r="' + r + '"/>';
    }
    s += '<circle class="dot-case" cx="22" cy="291" r="9"/><text x="38" y="296">Case</text><circle class="dot-non" cx="110" cy="291" r="9"/><text x="126" y="296">Non-case</text>';
    fig.innerHTML = s;
  }
  function renderStage() {
    const i = Number(inStage.value) - 1, st = stages[i];
    drawFarm(st.n);
    $('out-stage').textContent = String(i + 1);
    $('xp-stage').textContent = 'Stage ' + (i + 1) + ' of 5';
    $('xp-status').textContent = st.status;
    $('xp-obj').textContent = st.obj;
    $('xp-work').textContent = st.work;
    $('xp-text').textContent = st.text;
    document.querySelectorAll('#xp-chips .xp-chip').forEach(c => c.classList.toggle('is-on', Number(c.dataset.g) === st.g));
  }
  inStage.addEventListener('input', renderStage);
  document.addEventListener('deckreset', () => setTimeout(renderStage, 0));
  renderStage();
})();
</script>'''

slides_html = ''.join(S) + '\n' + DETAILS

# ------------------------------------------------------------------ splice into the shell
t = shell
t = re.sub(r'<title>.*?</title>', f'<title>{TITLE}</title>', t, count=1)
t = re.sub(r'<script type="application/json" id="deck-meta">.*?</script>', lambda m: META, t, count=1, flags=re.S)
t = re.sub(r'^<style id="deck-styles">.*?^</style>', lambda m: STYLES, t, count=1, flags=re.S | re.M)
a = t.index('<!-- ===================== CONTENT (edit for each deck) ===================== -->')
b = t.index('  </div><!-- /card -->')
t = t[:a] + '<!-- ===================== CONTENT (edit for each deck) ===================== -->\n' + slides_html + '\n' + t[b:]
c = t.index('<!-- Controls: one block per slide')
d = t.index('<!-- ===================== END OF CONTENT ===================== -->')
t = t[:c] + CONTROLS + '\n' + t[d:]
t = re.sub(r'^<script id="deck-script">.*?^</script>', lambda m: SCRIPT, t, count=1, flags=re.S | re.M)
open(out, 'w', encoding='utf-8').write(t)

print('slides:', len(S))
print('tooltips used:', len(used_tips), 'distinct:', len(set(used_tips)))
print('unused tooltips:', sorted(set(TIP) - set(used_tips)))
