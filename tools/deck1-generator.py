#!/usr/bin/env python3
"""Build slides/explain-epidemiology.html from templates/slide-shell.html (shell version 2).

Usage: python3 build_deck1.py <repo_root> <output_file>
The script keeps every tooltip text in one dictionary, so a term has the same text on every slide.
"""
import re, sys, html

repo, out = sys.argv[1], sys.argv[2]
shell = open(f'{repo}/templates/slide-shell.html', encoding='utf-8').read()

# ------------------------------------------------------------------ tooltips
TIP = {
 'hen': 'An adult female chicken.',
 'flock': 'A group of birds, such as hens, kept together.',
 'layer farm': 'A farm that keeps hens to produce eggs.',
 'pen': 'A small fenced area or house section where a group of animals is kept.',
 'water inlet': 'The place where water enters the house, for example from a pipe or a tank.',
 'Salmonella': 'A group of bacteria. They cause disease in animals and can reach people through eggs and meat.',
 'production animal veterinarian': 'One of the graduate profiles of this study program. This veterinarian protects the health and production of farm animals, for example on poultry or dairy farms.',
 'companion animal veterinarian': 'One of the graduate profiles of this study program. This veterinarian gives medical care and surgery to pets such as dogs and cats, for example in a clinic or an animal hospital.',
 'necropsy': 'An examination of a dead animal to find the cause of death.',
 'clinical question': 'A question about the diagnosis and treatment of one sick animal.',
 'clinician': 'A veterinarian who examines and treats sick animals.',
 'epidemiologist': 'A scientist who studies health events in groups of animals.',
 'health-related events': 'Anything that happens to the health of animals: a disease, a death, an injury, an accident, or a pregnancy.',
 'populations': 'Groups of animals that share a place or a system, such as all hens on one farm or all dogs in one village.',
 'study': 'Careful work with a clear method that uses data.',
 'distribution': 'How often a health event occurs, and where, when, and in which animals it occurs.',
 'determinants': 'Factors that change how often a health event occurs, such as the feed, the water, or the management.',
 'health-related states or events': 'A state is a condition that lasts, such as being pregnant or being protected by a vaccine. An event happens at one time, such as a death or an injury.',
 'specified populations': 'Groups of animals that the investigator defines clearly: which animals, in which place, and in which period.',
 'application': 'Using the results of the study in practice to prevent and control health problems.',
 'anamnesis': 'The history of the sick animal, told by the owner or keeper.',
 'diagnostic tests': 'Tests that help find the cause of a disease, such as blood tests or X-rays.',
 'statistical analysis': 'Using numbers and calculations to find patterns in data.',
 'epidemiological studies': 'Planned investigations that count health events in groups of animals and compare the groups.',
 'interventions': 'Actions that aim to prevent or control a disease, such as vaccination or separating sick animals.',
 'policies': 'Rules or plans made by an authority, such as a rule that sick animals must not be sold.',
 'neighbourhood': 'A part of a town where people live close to each other.',
 'diarrhoea': 'Frequent loose and watery stool.',
}
used_tips = []
def T(key, text=None):
    assert key in TIP, key
    used_tips.append(key)
    return f'<span class="term" data-tip="{html.escape(TIP[key], quote=True)}">{text or key}</span>'

# ------------------------------------------------------------------ meta
META = '''<script type="application/json" id="deck-meta">
{
  "title": "Explain epidemiology",
  "domain": "D0",
  "competency": "C1",
  "skills": {
    "primary": "S1.1",
    "secondary": [
      "S1.2"
    ]
  },
  "minutes": 15,
  "articles": [
    "epidemiology"
  ],
  "guides": [],
  "status": "draft",
  "updated": "2026-11-08"
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
.fig .bar-hot { fill: var(--d2); }
.fig .bar-n { fill: var(--muted); }
.fig .hen { fill: var(--surface); stroke: var(--muted); stroke-width: 2; }
.fig .hen-comb { fill: var(--d2); }
.fig .hen-beak { fill: var(--d5); }

.vcenter { justify-content: center; }
.big-def { font-size: 2.5rem; line-height: 1.3; font-weight: 600; letter-spacing: -0.01em; margin-top: 0.6rem; }
.def-case { display: grid; gap: 0.5rem; margin-top: 1.4rem; font-size: 1.4rem; padding: 1rem 1.2rem; border: 1px solid var(--line); border-radius: var(--radius); background: var(--surface); max-width: 46rem; }
.def-full { font-size: 1.95rem; line-height: 1.5; font-weight: 500; margin-top: 0.4rem; }
.def-labels { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; margin-top: 1.2rem; }
.def-labels div { border-top: 2px solid var(--muted); padding-top: 0.5rem; color: var(--muted); font-weight: 600; font-size: 1.1rem; }

.cmp { border-collapse: collapse; width: 100%; font-size: 1.2rem; }
.cmp th, .cmp td { text-align: left; padding: 0.65rem 0.9rem; border-bottom: 1px solid var(--line); vertical-align: top; }
.cmp thead th { border-bottom: 2px solid var(--muted); font-weight: 600; }
.cmp tbody th { font-weight: 600; color: var(--muted); width: 8rem; }
.cmp.ex tbody th { width: 17rem; }
.after-table { font-size: 1.25rem; margin-top: 0.6rem; }

.qsort { display: grid; gap: 0.9rem; align-content: start; }
.qsort [hidden] { display: none !important; }
.qs-top { display: flex; justify-content: space-between; color: var(--muted); font-size: 0.9rem; }
.qs-q { font-size: 1.5rem; font-weight: 600; line-height: 1.3; min-height: 4.2rem; }
.qs-hint { color: var(--muted); }
.qs-btns { display: flex; gap: 0.7rem; flex-wrap: wrap; }
.qs-btn { padding: 0.75rem 1.2rem; font-size: 1.05rem; }
.qs-btn:disabled { cursor: default; }
.qs-btn.is-correct { border: 2px solid var(--ok); }
.qs-btn.is-wrong { border: 2px solid var(--bad); }
.qs-why { color: var(--muted); min-height: 3rem; }

.build { font-size: 1.5rem; line-height: 2.3; margin-top: 0.4rem; }
.build select { font: inherit; font-size: 1.15rem; padding: 0.3rem 0.5rem; border: 1.5px solid var(--muted); border-radius: 8px; background: var(--surface); color: var(--ink); max-width: 100%; }
.build select.is-correct { border-color: var(--ok); }
.build select.is-wrong { border-color: var(--bad); }
.build select#b1 { width: 18.5rem; } .build select#b2 { width: 15rem; } .build select#b3 { width: 10.5rem; }
.map-why { font-size: 1.05rem; color: var(--muted); }
.map-why[hidden] { display: none; }
.build-actions { display: flex; flex-wrap: wrap; gap: 0.6rem; align-items: center; }
.build-why { display: grid; gap: 0.35rem; color: var(--muted); }
.q-label { font-weight: 600; font-size: 1.15rem; }
.quote { font-size: 1.3rem; line-height: 1.45; }
.practice-note { color: var(--muted); font-size: 0.95rem; }

@media (max-width: 900px) {
  .case-layout { grid-template-columns: 1fr; }
  .def-labels { grid-template-columns: 1fr; }
}
</style>'''

# ------------------------------------------------------------------ slides
S = []

# 1 Title
S.append(f'''
<!-- Slide 1: Title -->
<section class="slide" data-type="title" data-title="Explain epidemiology">
  <p class="code">C1 Epidemiological and economic thinking</p>
  <h1>Explain epidemiology</h1>
  <p class="lead">Why does a veterinarian look at the whole {T('flock')} when one {T('hen')} is sick?</p>
  <ul class="meta-list">
    <li><span class="code">S1.1</span><span>Explain the definition of epidemiology</span></li>
    <li><span class="code">S1.2</span><span>Distinguish clinical questions from population questions</span></li>
    <li><span class="code">Time</span><span>About 15 minutes</span></li>
  </ul>
  <div class="notes">Read the guiding question aloud. Ask the class for a first answer in one sentence. Students will return to this answer at the end of the deck.</div>
</section>''')

# 2 Recap
S.append(f'''
<!-- Slide 2: Recap of the anchor case -->
<section class="slide" data-type="recap" data-title="The case">
  <h2>The case: Salmonella on a layer farm</h2>
  <div class="case-layout">
    <div>
      <p>In one week, 120 of the 8,000 hens on a {T('layer farm')} die. Most of the dead hens come from the two {T('pen', 'pens')} next to the {T('water inlet')}.</p>
      <p>The laboratory later finds {T('Salmonella')} in the hens, and eggs from these pens have already reached buyers.</p>
      <p>You are the {T('production animal veterinarian')} of this farm.</p>
    </div>
    <figure class="penfig" data-detail="d-pens" tabindex="0" aria-label="Deaths in one week by pen. Pens A1 and B1, next to the water inlet, had 90 of the 120 deaths. Select for details.">
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
    </figure>
  </div>
  <div class="notes">Ask the class what they would do first. Most students name the necropsy. Use that answer on the next slide.</div>
</section>''')

# 3 Question
S.append(f'''
<!-- Slide 3: Question, predict -->
<section class="slide" data-type="question" data-title="Predict first">
  <h2>You do a {T('necropsy')} on five hens. Does this tell the farm owner what to do?</h2>
  <p>Choose your prediction.</p>
  <ul class="choices" data-choice="predict">
    <li><button class="choice" data-value="a"><span class="key">A</span>Yes. The necropsy results of five hens explain the problem in the whole flock.</button></li>
    <li><button class="choice" data-value="b"><span class="key">B</span>Partly. It gives the cause of death of five hens. It does not show which pens have the most deaths.</button></li>
    <li><button class="choice" data-value="c"><span class="key">C</span>No. A necropsy gives the farm owner no information about the problem in the flock.</button></li>
  </ul>
  <p class="verdict" id="predict-note" aria-live="polite"></p>
</section>''')

# 4 Simple definition
S.append(f'''
<!-- Slide 4: Concept, the simple definition -->
<section class="slide vcenter" data-type="concept" data-title="The simple definition">
  <h2>The simple definition</h2>
  <p class="big-def">Epidemiology is the study of {T('health-related events')} in {T('populations')}.</p>
  <div class="notes">Hover over the two dotted terms. Ask: which other health-related events could the veterinarian count on this farm? Accept answers such as a fall in egg production.</div>
</section>''')

# 5 One hen and one flock
def bars():
    deaths = [('A1', 50), ('A2', 5), ('A3', 5), ('A4', 5), ('B1', 40), ('B2', 5), ('B3', 5), ('B4', 5)]
    parts = []
    x0, w, gap, base = 392, 28, 8, 184
    for i, (name, n) in enumerate(deaths):
        x = x0 + i * (w + gap); h = n * 2
        cls = 'bar-hot' if n >= 40 else 'bar-n'
        parts.append(f'<rect class="{cls}" x="{x}" y="{base - h}" width="{w}" height="{h}" rx="3"/>')
        parts.append(f'<text x="{x + w/2}" y="{base - h - 6}" text-anchor="middle">{n}</text>')
        parts.append(f'<text x="{x + w/2}" y="{base + 20}" text-anchor="middle" class="t-muted">{name}</text>')
    parts.append(f'<line class="f-line" x1="{x0 - 6}" y1="{base}" x2="{x0 + 8*(w+gap) - gap + 6}" y2="{base}"/>')
    return '\n        '.join(parts)

S.append(f'''
<!-- Slide 5: Concept, one hen and a flock -->
<section class="slide" data-type="concept" data-title="One hen and a flock">
  <h2>The same disease raises two kinds of question</h2>
  <div class="fig-wrap">
    <svg class="fig" viewBox="0 0 720 300" role="img" aria-label="Left: one hen with the clinical questions about her illness. Right: a bar chart of deaths in one week by pen, with the population questions about the flock. Pens A1 and B1 have 50 and 40 deaths. The other six pens have 5 each.">
      <g>
        <rect class="f-soft" x="10" y="8" width="340" height="284" rx="12"/>
        <text x="30" y="40" class="t-strong">Clinical question: one animal</text>
        <ellipse class="hen" cx="150" cy="140" rx="52" ry="38"/>
        <circle class="hen" cx="212" cy="104" r="22"/>
        <polygon class="hen-beak" points="232,100 252,108 232,114"/>
        <circle class="hen-comb" cx="212" cy="80" r="7"/>
        <line class="f-line" x1="140" y1="178" x2="140" y2="204"/>
        <line class="f-line" x1="166" y1="178" x2="166" y2="204"/>
        <text x="150" y="226" text-anchor="middle" class="t-muted">One hen</text>
        <text x="30" y="258">What is wrong with her?</text>
        <text x="30" y="280">Which treatment does she need?</text>
      </g>
      <g>
        <rect class="f-soft" x="370" y="8" width="340" height="284" rx="12"/>
        <text x="390" y="40" class="t-strong">Population question: a group</text>
        {bars()}
        <text x="540" y="230" text-anchor="middle" class="t-muted">Deaths in one week, by pen</text>
        <text x="390" y="258">How many hens died, and where?</text>
        <text x="390" y="280">What do the sick hens share?</text>
      </g>
    </svg>
  </div>
  <p>A {T('clinical question', 'clinical question')} concerns one animal. A population question concerns a group of animals. The veterinarian needs both.</p>
  <div class="notes">Point to the left panel, then to the right panel. Ask which panel the necropsy belongs to. Then ask which panel tells the farm where to act first.</div>
</section>''')

# 6 Full definition
S.append(f'''
<!-- Slide 6: Concept, the full definition in three steps -->
<section class="slide vcenter" data-type="concept" data-title="The full definition">
  <h2>The full definition</h2>
  <p class="def-full">
    <span>Epidemiology is the {T('study')} of the {T('distribution')} and {T('determinants')} of {T('health-related states or events')}</span>
    <span>in {T('specified populations')},</span>
    <span>and the {T('application')} of this study to the control of health problems.</span>
  </p>
  <p class="small-note">Hover over or tap a dotted word. Definition after Last (2001).</p>
  <div class="notes">Read the definition in three parts. After each part, ask a student to explain it in simple words. Point out that the simple definition on the last slide is a short form of this sentence.</div>
</section>''')

# 7 Example, elements in the case (one table)
S.append(f'''
<!-- Slide 7: Example, the six elements in the case -->
<section class="slide" data-type="example" data-title="The elements in the case">
  <h2>The six elements in the layer farm</h2>
  <table class="cmp ex">
    <thead><tr><th scope="col">Element</th><th scope="col">In the layer farm</th></tr></thead>
    <tbody>
      <tr><th scope="row">{T('study', 'Study')}</th><td>The veterinarian works from records and counts.</td></tr>
      <tr><th scope="row">{T('health-related states or events', 'Health-related states or events')}</th><td>Deaths of hens and a fall in egg production.</td></tr>
      <tr><th scope="row">{T('specified populations', 'Specified populations')}</th><td>The 8,000 hens in 8 pens.</td></tr>
      <tr><th scope="row">{T('distribution', 'Distribution')}</th><td>90 of the 120 deaths were in pens A1 and B1, in one week.</td></tr>
      <tr><th scope="row">{T('determinants', 'Determinants')}</th><td>Pens A1 and B1 are next to the water inlet, so the water is a factor to test. The laboratory finds {T('Salmonella')}.</td></tr>
      <tr><th scope="row">{T('application', 'Application')}</th><td>The veterinarian separates the two pens, asks for daily records of deaths by pen, and finds the buyers of the eggs.</td></tr>
    </tbody>
  </table>
  <div class="notes">For each row, ask the class where they saw this fact on the case slide. Ask which element the manager had already used before the veterinarian arrived. A good answer is distribution, because the manager had counted the deaths.</div>
</section>''')

# 9 Comparison table
S.append(f'''
<!-- Slide 8: Concept, clinician and epidemiologist -->
<section class="slide" data-type="concept" data-title="Two ways of working">
  <h2>Two ways of working with the same disease</h2>
  <table class="cmp">
    <thead><tr><th scope="col">Comparison</th><th scope="col">{T('clinician', 'Clinician')}</th><th scope="col">{T('epidemiologist', 'Epidemiologist')}</th></tr></thead>
    <tbody>
      <tr><th scope="row">Focus</th><td>Individuals</td><td>Populations</td></tr>
      <tr><th scope="row">Objective</th><td>Curing the sick individual</td><td>Preventing and controlling disease in populations</td></tr>
      <tr><th scope="row">Diagnosis</th><td>Based on {T('anamnesis')}, physical examination, and {T('diagnostic tests')}</td><td>Based on {T('statistical analysis')} and {T('epidemiological studies')}</td></tr>
      <tr><th scope="row">Treatment</th><td>Giving medical or surgical treatment and care</td><td>Implementing animal health and public health {T('interventions')} and {T('policies')}</td></tr>
    </tbody>
  </table>
  <div class="notes">Ask which row describes the necropsy and which row describes the count by pen.</div>
</section>''')

# 10 Build the definition
def sel(i, opts):
    o = '<option value="">Choose</option>' + ''.join(f'<option value="{k}">{v}</option>' for k, v in opts)
    return f'<select id="b{i}" aria-label="Part {i} of the definition">{o}</select>'
S.append(f'''
<!-- Slide 9: Practice with support, build the definition -->
<section class="slide" data-type="practice" data-title="Build the definition">
  <h2>Build the definition</h2>
  <p class="practice-note">Choose one phrase for each gap. Think about the layer farm: what did the veterinarian describe, explain, and do?</p>
  <p class="build">Epidemiology is the study of the {sel(1, [('x', 'history and examination'), ('c', 'distribution and determinants'), ('y', 'diagnosis and treatment')])} of {T('health-related states or events')} in {sel(2, [('x', 'individual patients'), ('y', 'sick animals'), ('c', 'specified populations')])}, and the {sel(3, [('c', 'application'), ('x', 'publication'), ('y', 'calculation')])} of this study to the control of health problems.</p>
  <div class="build-actions">
    <button class="btn btn-main" id="b-check">Check the sentence</button>
    <button class="btn" id="b-reset">Start again</button>
    <span class="verdict" id="b-verdict" aria-live="polite"></span>
  </div>
  <div class="build-why" id="b-why"></div>
  <div class="notes">Let students choose alone first, then compare with a neighbour. Ask them to say the correct sentence aloud.</div>
</section>''')

# 11 Sort statements (one by one)
S.append('''
<!-- Slide 10: Practice with support, clinical or population question -->
<section class="slide" data-type="practice" data-title="Clinical or population?" data-panel="controls">
  <h2>Is it a clinical question or a population question?</h2>
  <div class="qsort">
    <div class="qs-top"><span class="num" id="qs-pos"></span><span class="num" id="qs-score"></span></div>
    <p class="qs-q" id="qs-q"></p>
    <p class="qs-hint" id="qs-hint" hidden>Ask: does the question concern one animal or a group of animals?</p>
    <div class="qs-btns" id="qs-btns">
      <button class="btn qs-btn" data-answer="C">Clinical question</button>
      <button class="btn qs-btn" data-answer="P">Population question</button>
    </div>
    <p class="verdict" id="qs-verdict" aria-live="polite"></p>
    <p class="qs-why" id="qs-why"></p>
    <div><button class="btn btn-main" id="qs-next" hidden>Show the next statement</button></div>
  </div>
  <div class="notes">Read each statement aloud and ask the class to vote before you reveal the answer. Statement 5 about the buyers of eggs is the one that students often place wrongly. Ask why eggs belong to the population.</div>
</section>''')

# 12 Card sorter, elements
S.append('''
<!-- Slide 11: Practice without support, match the case to the elements -->
<section class="slide" data-type="practice" data-title="Match the case to the elements">
  <h2>Put each fact from the case under the right element</h2>
  <div class="sorter" data-sorter id="map-sorter">
    <div class="sorter-pool" aria-label="Cards to sort">
      <button class="sort-card" data-target="events">Hens die and egg production falls</button>
      <button class="sort-card" data-target="populations">The 8,000 hens in 8 pens</button>
      <button class="sort-card" data-target="distribution">90 of 120 deaths in pens A1 and B1</button>
      <button class="sort-card" data-target="determinants">The water may be a factor</button>
      <button class="sort-card" data-target="application">The two pens are separated</button>
      <button class="sort-card" data-target="study">Records and counts, with a clear method</button>
    </div>
    <div class="sorter-bins">
      <div class="sort-bin" data-bin="study" data-capacity="1"><h3>Study</h3><div class="sort-drop"></div></div>
      <div class="sort-bin" data-bin="events" data-capacity="1"><h3>Health-related states or events</h3><div class="sort-drop"></div></div>
      <div class="sort-bin" data-bin="populations" data-capacity="1"><h3>Specified populations</h3><div class="sort-drop"></div></div>
      <div class="sort-bin" data-bin="distribution" data-capacity="1"><h3>Distribution</h3><div class="sort-drop"></div></div>
      <div class="sort-bin" data-bin="determinants" data-capacity="1"><h3>Determinants</h3><div class="sort-drop"></div></div>
      <div class="sort-bin" data-bin="application" data-capacity="1"><h3>Application</h3><div class="sort-drop"></div></div>
    </div>
    <div class="sorter-actions">
      <button class="btn btn-main" data-sorter-check>Check the sorting</button>
      <button class="btn" data-sorter-reset>Start again</button>
      <span class="verdict" role="status" aria-live="polite"></span>
    </div>
  </div>
  <p class="map-why" id="map-why" hidden>Each fact matches one element. The elements follow the steps of an investigation: define the population, describe the distribution, look for determinants, and apply the findings.</p>
  <p class="practice-note">Drag a card into a box. On a phone or with the keyboard, select a card and then select a box.</p>
  <div class="notes">Students work in pairs. If a pair places a card wrongly, ask them to read the definition of the element on slide 6 and decide again.</div>
</section>''')

# 13 Find the error
S.append(f'''
<!-- Slide 12: Practice, find the error -->
<section class="slide" data-type="practice" data-title="Find the error">
  <h2>Find the error</h2>
  <p>A student summarises the farm case in one note.</p>
  <p class="quote">"The veterinarian did a {T('necropsy')} on five hens. The laboratory result showed Salmonella. This completes the epidemiology of the problem."</p>
  <p class="q-label">What is missing from the note?</p>
  <div>
    <ul class="choices" data-check="q0" data-answer="c" data-explain="d-q0">
      <li><button class="choice" data-value="a"><span class="key">A</span>A second necropsy of the same five hens</button></li>
      <li><button class="choice" data-value="b"><span class="key">B</span>A dose of medicine for every hen in the flock</button></li>
      <li><button class="choice" data-value="c"><span class="key">C</span>The deaths by pen, and action based on the findings</button></li>
    </ul>
    <p class="verdict" aria-live="polite"></p>
  </div>
  <div class="notes">The note describes the cause in five hens. It has no distribution, no determinants, and no application.</div>
</section>''')

# 14 Check 1
S.append('''
<!-- Slide 13: Check, element of the definition -->
<section class="slide" data-type="check" data-title="Check: the element">
  <h2>The veterinarian separates the two pens with many deaths from the other pens. Which element of the definition is this?</h2>
  <div>
    <ul class="choices" data-check="q1" data-answer="b" data-explain="d-q1">
      <li><button class="choice" data-value="a"><span class="key">A</span>Distribution</button></li>
      <li><button class="choice" data-value="b"><span class="key">B</span>Application</button></li>
      <li><button class="choice" data-value="c"><span class="key">C</span>Determinants</button></li>
    </ul>
    <p class="verdict" aria-live="polite"></p>
  </div>
</section>''')

# 15 Check 2
S.append(f'''
<!-- Slide 14: Check, health-related event -->
<section class="slide" data-type="check" data-title="Check: the event">
  <h2>Which of these is a {T('health-related events', 'health-related event')} in a layer {T('flock')}?</h2>
  <div>
    <ul class="choices" data-check="q2" data-answer="a" data-explain="d-q2">
      <li><button class="choice" data-value="a"><span class="key">A</span>A fall in egg production</button></li>
      <li><button class="choice" data-value="b"><span class="key">B</span>A rise in the price of eggs</button></li>
      <li><button class="choice" data-value="c"><span class="key">C</span>A change in the number of pens</button></li>
    </ul>
    <p class="verdict" aria-live="polite"></p>
  </div>
</section>''')

# 16 Check 3 (transfer)
S.append(f'''
<!-- Slide 15: Check, transfer to a new case -->
<section class="slide" data-type="check" data-title="Check: a new case">
  <h2>A new case: sick dogs in one neighbourhood</h2>
  <p>Several dogs in one {T('neighbourhood')} of Makassar have vomiting and bloody {T('diarrhoea')} in one week. A {T('companion animal veterinarian')} in a clinic treats each dog.</p>
  <p class="q-label">Which question is a population question?</p>
  <div>
    <ul class="choices" data-check="q3" data-answer="c" data-explain="d-q3">
      <li><button class="choice" data-value="a"><span class="key">A</span>Which diagnosis fits the vomiting and bloody diarrhoea of the first dog?</button></li>
      <li><button class="choice" data-value="b"><span class="key">B</span>Which medicine and dose should the clinic give to the first dog?</button></li>
      <li><button class="choice" data-value="c"><span class="key">C</span>How many dogs are sick, and in which streets do they live?</button></li>
    </ul>
    <p class="verdict" aria-live="polite"></p>
  </div>
</section>''')

# 17 Summary
S.append('''
<!-- Slide 16: Summary -->
<section class="slide" data-type="summary" data-title="Summary">
  <h2>Key points</h2>
  <ul>
    <li>Epidemiology is the study of health-related events in populations.</li>
    <li>The full definition adds what the study looks at, which is distribution and determinants, and what it is for, which is the control of health problems.</li>
    <li>A clinical question concerns one animal. A population question concerns a group of animals or the animal products that come from it.</li>
    <li>The same disease raises both kinds of question, and the veterinarian needs both.</li>
    <li>The six elements of the definition follow the steps of an investigation, from the first count to the action.</li>
  </ul>
  <div class="links">
    <a class="btn" href="../encyclopedia/epidemiology.html">Read the article: Epidemiology</a>
    <a class="btn btn-main" href="./match-population-status-to-objective.html">Open the next deck: Match population status to objective</a>
  </div>
</section>''')

DETAILS = '''
<!-- Details: one template per element with data-detail or data-explain -->
<template id="d-pens">
  <h3>About these data</h3>
  <p>The flock has 8,000 hens in 8 pens. In a flock of this size, about 10 hens normally die in one week.</p>
  <p>Pens A1 and B1 are next to the water inlet. They had 90 of the 120 deaths. The other six pens had 5 deaths each.</p>
  <p>The necropsy of five hens tells the veterinarian what killed those hens. The count of deaths by pen tells her where the problem is.</p>
</template>
<template id="d-q0">
  <h3>Answer: C</h3>
  <p>The necropsy gives a cause of death for five hens. The note has no count of deaths by pen, so it does not describe the distribution in the flock.</p>
  <p>The note also has no action. The veterinarian must use the findings, for example by separating the pens.</p>
</template>
<template id="d-q1">
  <h3>Answer: B, Application</h3>
  <p>Application means using the results to prevent and control a health problem. Separating the pens protects the other hens.</p>
  <p>Counting the deaths by pen describes the distribution. Testing the water looks for a determinant.</p>
</template>
<template id="d-q2">
  <h3>Answer: A</h3>
  <p>A fall in egg production is a production problem in the hens. It is a health-related event.</p>
  <p>The price of eggs and the number of pens are not events in the health of the hens.</p>
</template>
<template id="d-q3">
  <h3>Answer: C</h3>
  <p>Question C concerns the group of dogs. It asks for the number of sick dogs and the places where they live.</p>
  <p>Questions A and B concern one dog. The veterinarian still treats each dog, so both kinds of question are needed.</p>
</template>
'''

CONTROLS = '''<!-- Controls: one block per slide with data-panel="controls". data-for-slide is the slide number. -->
<div class="controls" data-for-slide="10" hidden>
  <div class="control"><label for="in-hint">Show a hint <input type="checkbox" id="in-hint"></label></div>
  <button class="btn" id="qs-reset" data-reset>Reset the sorting</button>
</div>
'''

SCRIPT = '''<script id="deck-script">
(function () {
  const $ = id => document.getElementById(id);

  // Slide 3: reveal the best answer after a prediction
  const note = $('predict-note');
  document.querySelectorAll('[data-choice="predict"] .choice').forEach(b => b.addEventListener('click', () => {
    note.className = 'verdict';
    note.textContent = 'Option B is the best answer. A necropsy answers a clinical question about five hens. It does not show how many hens died in each pen, so the farm owner still does not know where to act.';
  }));

  // Slide 10: build the definition
  const sels = [$('b1'), $('b2'), $('b3')];
  const bWhy = {
    1: 'Part 1: epidemiology describes how often health events occur (distribution) and what changes it (determinants). Diagnosis and treatment belong to the clinician.',
    2: 'Part 2: epidemiology studies groups of animals that the investigator defines clearly. These are specified populations.',
    3: 'Part 3: the study is used in practice to prevent and control problems. This use is the application.'
  };
  function bClear() {
    sels.forEach(s => s.classList.remove('is-correct', 'is-wrong'));
    $('b-verdict').textContent = ''; $('b-verdict').className = 'verdict'; $('b-why').innerHTML = '';
  }
  sels.forEach(s => s.addEventListener('change', bClear));
  $('b-check').addEventListener('click', () => {
    if (sels.some(s => !s.value)) { $('b-verdict').textContent = 'Choose a phrase for every gap first.'; $('b-verdict').className = 'verdict bad'; return; }
    let ok = 0; const why = $('b-why'); why.innerHTML = '';
    sels.forEach((s, i) => {
      const right = s.value === 'c';
      s.classList.toggle('is-correct', right); s.classList.toggle('is-wrong', !right);
      if (right) ok++; else { const p = document.createElement('p'); p.textContent = bWhy[i + 1]; why.appendChild(p); }
    });
    const all = ok === 3;
    $('b-verdict').textContent = all ? 'All 3 parts are correct.' : ok + ' of 3 parts are correct. Change the parts marked in red and check again.';
    $('b-verdict').className = 'verdict ' + (all ? 'ok' : 'bad');
  });
  $('b-reset').addEventListener('click', () => { sels.forEach(s => { s.value = ''; }); bClear(); });

  // Slide 12: show the summary after a correct sorting
  const ms = $('map-sorter'), mw = $('map-why');
  ms.querySelector('[data-sorter-check]').addEventListener('click', () => {
    mw.hidden = !ms.querySelector('.verdict').classList.contains('ok');
  });
  ms.querySelector('[data-sorter-reset]').addEventListener('click', () => { mw.hidden = true; });

  // Slide 11: sort six statements
  const items = [
    { q: 'Hen 14 breathes with difficulty and her head is swollen. What is wrong with her?', a: 'C', why: 'The question concerns one hen. The answer comes from her examination and tests.' },
    { q: 'How many hens died in each pen this week?', a: 'P', why: 'The question counts events in a group of animals, pen by pen. This describes the distribution of deaths.' },
    { q: 'Do more hens die in the pens next to the water inlet than in the other pens?', a: 'P', why: 'The question compares groups of pens. It looks for a determinant of the deaths.' },
    { q: 'Which medicine should the veterinarian give to this sick hen?', a: 'C', why: 'The decision concerns the treatment of one animal.' },
    { q: 'Which buyers received eggs from the pens with many deaths?', a: 'P', why: 'Eggs are animal products of the specified population. The question concerns the egg chain, which reaches beyond one hen.' },
    { q: 'Does the damage in the liver explain why this hen died?', a: 'C', why: 'The question concerns the cause of death of one animal.' }
  ];
  const label = { C: 'clinical question', P: 'population question' };
  const qEl = $('qs-q'), posEl = $('qs-pos'), scoreEl = $('qs-score'), verdict = $('qs-verdict'),
        why = $('qs-why'), next = $('qs-next'), btns = $('qs-btns'), hint = $('qs-hint'), hintBox = $('in-hint');
  const buttons = Array.from(btns.querySelectorAll('.qs-btn'));
  let idx = 0, score = 0, answered = false, finished = false;

  function render() {
    finished = false; answered = false;
    qEl.textContent = items[idx].q;
    posEl.textContent = 'Statement ' + (idx + 1) + ' of ' + items.length;
    scoreEl.textContent = 'Correct so far: ' + score;
    verdict.textContent = ''; verdict.className = 'verdict'; why.textContent = '';
    next.hidden = true; btns.hidden = false;
    buttons.forEach(b => { b.disabled = false; b.classList.remove('is-correct', 'is-wrong'); });
  }
  function reset() { idx = 0; score = 0; render(); }
  function showResult() {
    finished = true;
    posEl.textContent = 'Result';
    scoreEl.textContent = '';
    qEl.textContent = 'You sorted ' + score + ' of ' + items.length + ' statements correctly.';
    verdict.textContent = ''; verdict.className = 'verdict';
    why.textContent = 'A question about one animal is a clinical question. A question about a group, a comparison between groups, or the animal products of a group is a population question.';
    btns.hidden = true;
    next.textContent = 'Reset the sorting'; next.hidden = false;
  }
  buttons.forEach(b => b.addEventListener('click', () => {
    if (answered) return;
    answered = true;
    const item = items[idx], ok = b.dataset.answer === item.a;
    if (ok) score++;
    buttons.forEach(x => { x.disabled = true; });
    b.classList.add(ok ? 'is-correct' : 'is-wrong');
    if (!ok) buttons.find(x => x.dataset.answer === item.a).classList.add('is-correct');
    verdict.textContent = ok ? 'Correct.' : 'Not correct. This is a ' + label[item.a] + '.';
    verdict.className = 'verdict ' + (ok ? 'ok' : 'bad');
    why.textContent = item.why;
    scoreEl.textContent = 'Correct so far: ' + score;
    next.textContent = idx === items.length - 1 ? 'Show the result' : 'Show the next statement';
    next.hidden = false;
  }));
  next.addEventListener('click', () => {
    if (finished) { reset(); return; }
    if (idx === items.length - 1) { showResult(); return; }
    idx++; render();
  });
  $('qs-reset').addEventListener('click', reset);
  function syncHint() { hint.hidden = !hintBox.checked; }
  hintBox.addEventListener('input', syncHint); hintBox.addEventListener('change', syncHint);
  render(); syncHint();
})();
</script>'''

slides_html = ''.join(S) + '\n' + DETAILS

# ------------------------------------------------------------------ splice into the shell
t = shell
t = re.sub(r'<title>.*?</title>', '<title>Explain epidemiology</title>', t, count=1)
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
unused = sorted(set(TIP) - set(used_tips))
print('unused tooltips:', unused)
