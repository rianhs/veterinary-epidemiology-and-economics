---
title: "C13. Disease spread and models"
toc: true
toc-title: Skills
listing:
  - id: m-s13-1
    contents:
      - "../encyclopedia/*.md"
      - "../guides/*.md"
      - "../slides/decks.yml"
    type: table
    fields: [type, title]
    field-display-names:
      type: Type
    sort: type
    sort-ui: false
    filter-ui: false
    include:
      categories: "S13.1"
  - id: m-s13-2
    contents:
      - "../encyclopedia/*.md"
      - "../guides/*.md"
      - "../slides/decks.yml"
    type: table
    fields: [type, title]
    field-display-names:
      type: Type
    sort: type
    sort-ui: false
    filter-ui: false
    include:
      categories: "S13.2"
  - id: m-s13-3
    contents:
      - "../encyclopedia/*.md"
      - "../guides/*.md"
      - "../slides/decks.yml"
    type: table
    fields: [type, title]
    field-display-names:
      type: Type
    sort: type
    sort-ui: false
    filter-ui: false
    include:
      categories: "S13.3"
  - id: m-s13-4
    contents:
      - "../encyclopedia/*.md"
      - "../guides/*.md"
      - "../slides/decks.yml"
    type: table
    fields: [type, title]
    field-display-names:
      type: Type
    sort: type
    sort-ui: false
    filter-ui: false
    include:
      categories: "S13.4"
  - id: m-s13-5
    contents:
      - "../encyclopedia/*.md"
      - "../guides/*.md"
      - "../slides/decks.yml"
    type: table
    fields: [type, title]
    field-display-names:
      type: Type
    sort: type
    sort-ui: false
    filter-ui: false
    include:
      categories: "S13.5"
  - id: m-s13-6
    contents:
      - "../encyclopedia/*.md"
      - "../guides/*.md"
      - "../slides/decks.yml"
    type: table
    fields: [type, title]
    field-display-names:
      type: Type
    sort: type
    sort-ui: false
    filter-ui: false
    include:
      categories: "S13.6"
  - id: m-s13-7
    contents:
      - "../encyclopedia/*.md"
      - "../guides/*.md"
      - "../slides/decks.yml"
    type: table
    fields: [type, title]
    field-display-names:
      type: Type
    sort: type
    sort-ui: false
    filter-ui: false
    include:
      categories: "S13.7"
---

```{=html}
<div class="comp-intro" style="--dc:var(--d3)">
<p class="comp-domain"><a href="../index.html#d3"><span class="dot"></span>Domain 3: What could happen?</a></p>
<p class="comp-lead">Project disease spread in a population with a compartmental model.</p>
<dl class="comp-facts"><div><dt>Skills</dt><dd>7</dd></div><div><dt>Depth</dt><dd>Applied</dd></div></dl>
<div class="comp-links">
<div><h2 class="mini-title">Builds on</h2><ul><li><a href="population-unit-and-case.html"><span class="code">C2</span> Population, unit, and case</a></li><li><a href="patterns-by-animal-place-and-time.html"><span class="code">C6</span> Patterns by animal, place, and time</a></li></ul></div>
<div><h2 class="mini-title">Leads to</h2><ul><li><a href="risk-of-introduction-and-spread.html"><span class="code">C14</span> Risk of introduction and spread</a></li><li><a href="intervention-options.html"><span class="code">C15</span> Intervention options</a></li><li><a href="evaluating-interventions.html"><span class="code">C18</span> Evaluating interventions</a></li><li><a href="integrated-strategy.html"><span class="code">C19</span> Integrated strategy</a></li></ul></div>
</div>
<p class="comp-howto">Learn the skills in order. Each skill shows what it covers, what you need first, and where it leads.</p>
</div>
```

## S13.1 Describe a population as compartments {#s13-1}

```{=html}
<div class="skill-body"><p class="skill-scope">Susceptible, infectious, recovered, and dead compartments, with flows between them.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="population-unit-and-case.html#s2-5"><span class="code">S2.5</span> Choose a method to estimate population size</a></li><li><a href="population-unit-and-case.html#s2-3"><span class="code">S2.3</span> Describe the natural history of a disease</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="disease-spread-and-models.html#s13-2"><span class="code">S13.2</span> Explain and calculate the basic reproduction number</a></li></ul></div></div></div>
```

::: {#m-s13-1 .skill-materials}
:::

## S13.2 Explain and calculate the basic reproduction number {#s13-2}

```{=html}
<div class="skill-body"><p class="skill-scope">Contact rate, transmission probability, and infectious period.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="disease-spread-and-models.html#s13-1"><span class="code">S13.1</span> Describe a population as compartments</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="disease-spread-and-models.html#s13-3"><span class="code">S13.3</span> Distinguish R0 and Re</a></li><li><a href="disease-spread-and-models.html#s13-4"><span class="code">S13.4</span> Explore parameters in a prepared SIR model</a></li><li><a href="disease-spread-and-models.html#s13-5"><span class="code">S13.5</span> Calculate the herd immunity threshold</a></li><li><a href="risk-of-introduction-and-spread.html#s14-5"><span class="code">S14.5</span> Assess the consequences of introduction</a></li></ul></div></div></div>
```

::: {#m-s13-2 .skill-materials}
:::

## S13.3 Distinguish R0 and Re {#s13-3}

```{=html}
<div class="skill-body"><p class="skill-scope">Why a fall in case counts is different from Re below 1.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="disease-spread-and-models.html#s13-2"><span class="code">S13.2</span> Explain and calculate the basic reproduction number</a></li><li><a href="patterns-by-animal-place-and-time.html#s6-7"><span class="code">S6.7</span> Describe trend and seasonality</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="evaluating-interventions.html#s18-5"><span class="code">S18.5</span> Use incidence trends and Re to evaluate</a></li></ul></div></div></div>
```

::: {#m-s13-3 .skill-materials}
:::

## S13.4 Explore parameters in a prepared SIR model {#s13-4}

```{=html}
<div class="skill-body"><p class="skill-scope">Prepared SIR or SIRD model. Effect of a change in each parameter.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-applied">Applied</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="disease-spread-and-models.html#s13-2"><span class="code">S13.2</span> Explain and calculate the basic reproduction number</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="disease-spread-and-models.html#s13-6"><span class="code">S13.6</span> Build a scenario table for a decision</a></li><li><a href="disease-spread-and-models.html#s13-7"><span class="code">S13.7</span> State when a compartmental model fails</a></li></ul></div></div></div>
```

::: {#m-s13-4 .skill-materials}
:::

## S13.5 Calculate the herd immunity threshold {#s13-5}

```{=html}
<div class="skill-body"><p class="skill-scope">Simple form, adjustment for vaccine efficacy, and assumptions.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="disease-spread-and-models.html#s13-2"><span class="code">S13.2</span> Explain and calculate the basic reproduction number</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="disease-spread-and-models.html#s13-6"><span class="code">S13.6</span> Build a scenario table for a decision</a></li></ul></div></div></div>
```

::: {#m-s13-5 .skill-materials}
:::

## S13.6 Build a scenario table for a decision {#s13-6}

```{=html}
<div class="skill-body"><p class="skill-scope">Scenarios with and without intervention.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-applied">Applied</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="disease-spread-and-models.html#s13-4"><span class="code">S13.4</span> Explore parameters in a prepared SIR model</a></li><li><a href="disease-spread-and-models.html#s13-5"><span class="code">S13.5</span> Calculate the herd immunity threshold</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="intervention-options.html#s15-3"><span class="code">S15.3</span> Estimate the expected effect of each option</a></li><li><a href="integrated-strategy.html#s19-1"><span class="code">S19.1</span> Combine evidence into a strategy document</a></li></ul></div></div></div>
```

::: {#m-s13-6 .skill-materials}
:::

## S13.7 State when a compartmental model fails {#s13-7}

```{=html}
<div class="skill-body"><p class="skill-scope">Homogeneous mixing, closed population, and other assumptions.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="disease-spread-and-models.html#s13-4"><span class="code">S13.4</span> Explore parameters in a prepared SIR model</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li>None in this course</li></ul></div></div></div>
```

::: {#m-s13-7 .skill-materials}
:::

```{=html}
<nav class="comp-pager"><a class="prev" href="outbreak-investigation.html"><span>Previous</span><strong>C12 Outbreak investigation</strong></a><a class="next" href="risk-of-introduction-and-spread.html"><span>Next</span><strong>C14 Risk of introduction and spread</strong></a></nav>
```
