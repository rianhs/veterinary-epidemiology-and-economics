"""Generate the home page, the skill map page, and the competency pages from 02-competencies-and-skills.md.

Usage (from the repository root):
    python3 tools/generate_pages.py path/to/02-competencies-and-skills.md .

The script rewrites index.md, skills.md, and every file in competencies/.
Run it after every change to the skill map, then commit the changed files.
"""
import re, math, sys, os, html
ref, site = sys.argv[1], sys.argv[2]
s = open(ref).read()

comps = re.findall(r'^\| (C\d+) \| (D\d|Integration) \| (.+?) \| (.+?) \| (.+?) \| (\d+) \| ([a-z0-9-]+) \|$', s, re.M)
skills = re.findall(r'^\| (S(\d+)\.\d+) \| (.+?) \| (.+?) \| (.+?) \| (Core|Applied|Introduced) \|$', s, re.M)
xs = re.findall(r'^\| (X\d) \| (.+?) \|$', s, re.M)
C = {c[0]: dict(code=c[0], dom=c[1], name=c[2], stmt=c[3], depth=c[4], n=int(c[5]), slug=c[6]) for c in comps}
S = {}
for code, cn, stmt, scope, pre, dep in skills:
    S[code] = dict(code=code, comp='C'+cn, stmt=stmt, scope=scope, pre=[] if pre=='None' else [p.strip() for p in pre.split(',')], depth=dep)
X = dict(xs)
dependents = {k: [] for k in S}
for k, v in S.items():
    for p in v['pre']:
        if p in dependents: dependents[p].append(k)

DOM = [
 ("D0","Domain 0","Why epidemiology?","What epidemiology and veterinary economics are, and how to turn a clinical case into a population question."),
 ("D1","Domain 1","What is happening?","Define the population and the case, collect data, judge tests, and describe the pattern of disease."),
 ("D2","Domain 2","Why is it happening?","Compare groups, analyse several factors together, read reports, design studies, and investigate outbreaks."),
 ("D3","Domain 3","What could happen?","Project spread within a population and assess the risk that disease comes in."),
 ("D4","Domain 4","What should be done?","Choose interventions and compare them on health and economic grounds."),
 ("D5","Domain 5","Did it work?","Judge whether an intervention changed the disease or changed the detection."),
 ("Integration","Integration","All questions together","Combine the evidence into one strategy and defend it."),
]
DV = {"D0":"--d0","D1":"--d1","D2":"--d2","D3":"--d3","D4":"--d4","D5":"--d5","Integration":"--dint"}
def anc(code): return code.lower().replace('.', '-')
def e(t): return html.escape(t, quote=True)
def skill_url(code, here=None):
    if code in X: return ('' if here is None else '../') + 'skills.html#x-skills'
    c = C[S[code]['comp']]
    base = '' if here == 'comp' else 'competencies/'
    if here == 'comp': return f"{c['slug']}.html#{anc(code)}"
    return f"{base}{c['slug']}.html#{anc(code)}"
def comp_url(code, here=None):
    return (f"{C[code]['slug']}.html" if here=='comp' else f"competencies/{C[code]['slug']}.html")
def dom_of(d): return next(x for x in DOM if x[0]==d)

# ---------------- loop diagram ----------------
cx, cy, r = 330, 240, 150
ang = {"D1":-90,"D2":-18,"D3":54,"D4":126,"D5":198}
def pt(a): return (cx+r*math.cos(math.radians(a)), cy+r*math.sin(math.radians(a)))
order = ["D1","D2","D3","D4","D5"]
arcs = []
for i,d in enumerate(order):
    a1 = ang[d]+11; a2 = ang[order[(i+1)%5]]-11
    if a2 < a1: a2 += 360
    (x1,y1),(x2,y2) = pt(a1), pt(a2)
    arcs.append(f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 0 1 {x2:.1f},{y2:.1f}" class="loop-arc" marker-end="url(#arrow)"/>')
lab = {"D1":("middle",0,-48),"D2":("start",20,-6),"D3":("start",8,34),"D4":("end",-8,34),"D5":("end",-20,-6)}
nodes = []
for d,dn,q,_ in DOM[1:6]:
    x,y = pt(ang[d]); a,dx,dy = lab[d]
    nodes.append(f'<a href="#{d.lower()}" class="loop-node"><circle cx="{x:.1f}" cy="{y:.1f}" r="11" style="fill:var({DV[d]})"/>'
                 f'<text x="{x+dx:.1f}" y="{y+dy:.1f}" text-anchor="{a}"><tspan class="loop-code" x="{x+dx:.1f}">{dn}</tspan>'
                 f'<tspan class="loop-q" x="{x+dx:.1f}" dy="20">{q}</tspan></text></a>')
svg = (f'<svg viewBox="0 0 660 460" role="img" aria-labelledby="loop-title"><title id="loop-title">The five questions form a loop around Domain 0</title>'
       f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="loop-head"/></marker></defs>'
       + ''.join(arcs) +
       f'<a href="#d0" class="loop-node"><circle cx="{cx}" cy="{cy}" r="66" class="center-disc"/>'
       f'<text x="{cx}" y="{cy-6}" text-anchor="middle"><tspan class="loop-code" x="{cx}">Domain 0</tspan><tspan class="loop-q" x="{cx}" dy="20">Why epidemiology?</tspan></text></a>'
       + ''.join(nodes) + '</svg>')
mobile = ''.join(f'<li><a href="#{d.lower()}"><span class="dot" style="background:var({DV[d]})"></span><span class="ml-code">{dn}</span><span>{q}</span></a></li>' for d,dn,q,_ in DOM[:6])

# ---------------- home ----------------
ex_c, ex_s = C['C4'], S['S4.3']
chain = f'''<ol class="chain">
<li class="chain-step"><p class="chain-level">Question</p><p class="chain-def">What a veterinarian asks about a population.</p><p class="chain-ex">What is happening?</p></li>
<li class="chain-step"><p class="chain-level">Domain</p><p class="chain-def">One question and the work it needs.</p><p class="chain-ex"><a href="#d1"><span class="dot" style="background:var(--d1)"></span>Domain 1</a></p></li>
<li class="chain-step"><p class="chain-level">Competency</p><p class="chain-def">An ability that the course assesses.</p><p class="chain-ex"><a href="{comp_url('C4')}"><span class="code">C4</span> {e(ex_c['name'])}</a></p></li>
<li class="chain-step"><p class="chain-level">Skill</p><p class="chain-def">A small step that you learn and practise.</p><p class="chain-ex"><a href="{skill_url('S4.3')}"><span class="code">S4.3</span> {e(ex_s['stmt'])}</a></p></li>
</ol>'''

rows = []
for d,dn,q,desc in DOM:
    items = ''.join(f'<li><a href="{comp_url(c["code"])}"><span class="code">{c["code"]}</span><span class="c-name">{e(c["name"])}</span><span class="c-count">{c["n"]} skills</span></a></li>' for c in C.values() if c['dom']==d)
    rows.append(f'<div class="domain" id="{d.lower()}" style="--dc:var({DV[d]})"><div class="domain-head"><p class="domain-code"><span class="dot"></span>{dn}</p><h3>{q}</h3><p class="domain-desc">{desc}</p></div><ol class="comp-list">{items}</ol></div>')

nC, nS = len(C), len(S)
index = f'''---
title: "Veterinary Epidemiology and Economics"
title-block-style: none
page-layout: full
toc: false
---

```{{=html}}
<style>#title-block-header{{display:none}}</style>
<div class="home">
<section class="home-hero">
<div class="hero-text">
<h1>Veterinary Epidemiology and Economics</h1>
<p class="lead">A veterinarian who meets a health problem in an animal population asks five questions. This course teaches you to answer them with evidence and economic reasoning.</p>
<div class="hero-actions"><a class="btn-main" href="{comp_url('C1')}">Start with Domain 0</a><a class="btn-quiet" href="skills.html">Open the skill map</a></div>
<p class="hero-note">For 6th-semester students of the Veterinary Medicine Study Program, Universitas Hasanuddin.</p>
</div>
<figure class="hero-loop">{svg}</figure>
<ol class="loop-mobile">{mobile}</ol>
</section>

<section class="home-section" aria-labelledby="org-title">
<h2 id="org-title">How the course is organized</h2>
<p class="section-lead">The course follows five questions. Each question is one domain. Domain 0 comes first and teaches how to think about populations. Each domain has competencies, and each competency has skills. The course has {nC} competencies and {nS} skills.</p>
{chain}
<div class="org-notes">
<p><strong>Codes.</strong> Each item has a code. D marks a domain, C a competency, and S a skill. S4.3 is the third skill of competency C4.</p>
<p><strong>Order.</strong> Some skills need other skills first. These are prerequisites. Each competency page shows them.</p>
<p><strong>Loop.</strong> The five questions form a loop. You observe a population, interpret the information, decide, act, and observe again. Domain 0 explains the loop.</p>
<p><strong>Start.</strong> Begin with Domain 0. Then follow the domains in order.</p>
</div>
</section>

<section class="home-section" aria-labelledby="materials-title">
<h2 id="materials-title">Three kinds of material</h2>
<p class="section-lead">Each material serves one or more skills.</p>
<div class="materials">
<a class="material" href="encyclopedia/index.html"><h3>Encyclopedia</h3><p>Read what a concept means, how it behaves, and where it fails.</p></a>
<a class="material" href="guides/index.html"><h3>Guides</h3><p>Follow a procedure step by step, with a check after each step.</p></a>
<a class="material" href="slides/index.html"><h3>Slides</h3><p>Explore a topic in class. Move the controls and watch the result change.</p></a>
</div>
</section>

<section class="home-section" aria-labelledby="domains-title">
<h2 id="domains-title">Domains and competencies</h2>
<p class="section-lead">Select a competency to see its skills.</p>
{''.join(rows)}
</section>
</div>
```
'''
open(f'{site}/index.md','w').write(index)

# ---------------- skill map ----------------
out = ['---','title: Skill map','toc: true','toc-depth: 2','toc-title: Domains','---','',
'```{=html}',
'<div class="readme">',
'<h2 class="readme-title" id="how-to-read">How to read this page</h2>',
f'<p>This page lists all {nS} skills of the course. The skills are grouped by competency, and the competencies are grouped by domain.</p>',
'<p>Select a competency or a skill to open its page. The page shows what the skill covers, what you need first, and the materials for it.</p>',
'<dl class="depth-legend"><div><dt>Core</dt><dd>You do it alone.</dd></div><div><dt>Applied</dt><dd>You do it with a template, a tool, or guidance.</dd></div><div><dt>Introduced</dt><dd>You recognize it and explain what it means.</dd></div></dl>',
'</div>','```','']
for d,dn,q,desc in DOM:
    head = f'{dn}. {q}' if d!='Integration' else 'Integration. All questions together'
    out += [f'## {head} {{#{d.lower()} .domain-title style="--dc:var({DV[d]})"}}','',desc,'','```{=html}','<div class="card-grid">']
    for c in C.values():
        if c['dom']!=d: continue
        lis = ''.join(f'<li><a href="{skill_url(k)}"><span class="code">{k}</span><span class="s-text">{e(v["stmt"])}</span><span class="depth depth-{v["depth"].lower()}">{v["depth"]}</span></a></li>' for k,v in S.items() if v['comp']==c['code'])
        out.append(f'<article class="comp-card" style="--dc:var({DV[d]})"><header><p class="card-meta"><span class="dot"></span><span class="code">{c["code"]}</span><span>{c["n"]} skills</span></p><h3><a href="{comp_url(c["code"])}">{e(c["name"])}</a></h3><p class="card-stmt">{e(c["stmt"])}.</p></header><ol class="skill-list">{lis}</ol></article>')
    out += ['</div>','```','']
out += ['## Skills from earlier courses {#x-skills}','','These skills come from Biostatistics and earlier courses. The course uses them without teaching them again.','','| Code | Skill |','|-|-|']
out += [f'| {k} | {v} |' for k,v in X.items()]
open(f'{site}/skills.md','w').write('\n'.join(out)+'\n')

# ---------------- competency pages ----------------
os.makedirs(f'{site}/competencies', exist_ok=True)
for f in os.listdir(f'{site}/competencies'):
    os.remove(f'{site}/competencies/{f}')
clist = list(C.values())
def link_skill(k):
    if k in X: return f'<a href="../skills.html#x-skills"><span class="code">{k}</span> {e(X[k])}</a>'
    return f'<a href="{skill_url(k, "comp")}"><span class="code">{k}</span> {e(S[k]["stmt"])}</a>'
for i,c in enumerate(clist):
    d = dom_of(c['dom'])
    mine = [v for v in S.values() if v['comp']==c['code']]
    ext_pre = sorted({S[p]['comp'] for v in mine for p in v['pre'] if p in S and S[p]['comp']!=c['code']}, key=lambda x:int(x[1:]))
    ext_x = sorted({p for v in mine for p in v['pre'] if p in X})
    ext_next = sorted({S[q]['comp'] for v in mine for q in dependents[v['code']] if S[q]['comp']!=c['code']}, key=lambda x:int(x[1:]))
    def clinks(lst): return ''.join(f'<li><a href="{comp_url(x,"comp")}"><span class="code">{x}</span> {e(C[x]["name"])}</a></li>' for x in lst) or '<li>None</li>'
    xl = ''.join(f'<li><a href="../skills.html#x-skills"><span class="code">{x}</span> {e(X[x])}</a></li>' for x in ext_x)
    lines = ['---', f'title: "{c["code"]}. {c["name"]}"', 'toc: true', 'toc-title: Skills', 'listing:']
    for v in mine:
        lines += [f'  - id: m-{anc(v["code"])}', '    contents:', '      - "../encyclopedia/*.md"', '      - "../guides/*.md"', '      - "../slides/decks.yml"',
                  '    type: table', '    fields: [type, title]', '    field-display-names:', '      type: Type', '    sort: type', '    sort-ui: false', '    filter-ui: false', '    include:', f'      categories: "{v["code"]}"']
    lines += ['---', '',
             '```{=html}',
             f'<div class="comp-intro" style="--dc:var({DV[c["dom"]]})">',
             f'<p class="comp-domain"><a href="../index.html#{c["dom"].lower()}"><span class="dot"></span>{d[1]}: {d[2]}</a></p>',
             f'<p class="comp-lead">{e(c["stmt"])}.</p>',
             f'<dl class="comp-facts"><div><dt>Skills</dt><dd>{c["n"]}</dd></div><div><dt>Depth</dt><dd>{e(c["depth"])}</dd></div></dl>',
             '<div class="comp-links">',
             f'<div><h2 class="mini-title">Builds on</h2><ul>{clinks(ext_pre)}{xl}</ul></div>',
             f'<div><h2 class="mini-title">Leads to</h2><ul>{clinks(ext_next)}</ul></div>',
             '</div>',
             '<p class="comp-howto">Learn the skills in order. Each skill shows what it covers, what you need first, and where it leads.</p>',
             '</div>', '```', '']
    for v in mine:
        pre = ''.join(f'<li>{link_skill(p)}</li>' for p in v['pre']) or '<li>None</li>'
        nxt = ''.join(f'<li>{link_skill(q)}</li>' for q in dependents[v['code']]) or '<li>None in this course</li>'
        lines += [f'## {v["code"]} {v["stmt"]} {{#{anc(v["code"])}}}', '',
                  '```{=html}',
                  f'<div class="skill-body"><p class="skill-scope">{e(v["scope"])}</p>',
                  f'<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-{v["depth"].lower()}">{v["depth"]}</p></div>',
                  f'<div><h3 class="mini-title">Needs first</h3><ul>{pre}</ul></div>',
                  f'<div><h3 class="mini-title">Leads to</h3><ul>{nxt}</ul></div></div></div>',
                  '```', '', f'::: {{#m-{anc(v["code"])} .skill-materials}}', ':::', '']
    prev = clist[i-1] if i>0 else None; nxt = clist[i+1] if i<len(clist)-1 else None
    nav = '<nav class="comp-pager">'
    nav += f'<a class="prev" href="{prev["slug"]}.html"><span>Previous</span><strong>{prev["code"]} {e(prev["name"])}</strong></a>' if prev else '<span></span>'
    nav += f'<a class="next" href="{nxt["slug"]}.html"><span>Next</span><strong>{nxt["code"]} {e(nxt["name"])}</strong></a>' if nxt else '<span></span>'
    nav += '</nav>'
    lines += ['```{=html}', nav, '```', '']
    open(f'{site}/competencies/{c["slug"]}.md','w').write('\n'.join(lines))
print(len(C), len(S), len(X))
