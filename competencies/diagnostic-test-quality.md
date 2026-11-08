---
title: "C4. Diagnostic test quality"
toc: true
toc-title: Skills
listing:
  id: materials
  contents:
    - "../encyclopedia/*.md"
    - "../guides/*.md"
    - "../slides/decks.yml"
  type: table
  fields: [title, categories]
  sort: title
  include:
    categories: "C4"
---

```{=html}
<div class="comp-intro" style="--dc:var(--d1)">
<p class="comp-domain"><a href="../index.html#d1"><span class="dot"></span>Domain 1: What is happening?</a></p>
<p class="comp-lead">Judge the quality of diagnostic tests and interpret test results at animal and population level.</p>
<dl class="comp-facts"><div><dt>Skills</dt><dd>10</dd></div><div><dt>Depth</dt><dd>Core</dd></div></dl>
<div class="comp-links">
<div><h2 class="mini-title">Builds on</h2><ul><li><a href="population-unit-and-case.html"><span class="code">C2</span> Population, unit, and case</a></li><li><a href="data-sources-and-sampling.html"><span class="code">C3</span> Data sources and sampling</a></li></ul></div>
<div><h2 class="mini-title">Leads to</h2><ul><li><a href="surveillance-systems.html"><span class="code">C7</span> Surveillance systems</a></li><li><a href="appraising-analytical-reports.html"><span class="code">C10</span> Appraising analytical reports</a></li><li><a href="risk-of-introduction-and-spread.html"><span class="code">C14</span> Risk of introduction and spread</a></li></ul></div>
</div>
<p class="comp-howto">Learn the skills in order. Each skill shows what it covers, what you need first, and where it leads.</p>
</div>
```

## S4.1 Distinguish validity, reliability, and precision {#s4-1}

```{=html}
<div class="skill-body"><p class="skill-scope">Validity: test sensitivity and specificity. Reliability: repeatability and agreement. Precision: uncertainty of an estimate.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="population-unit-and-case.html#s2-6"><span class="code">S2.6</span> Define the health event, exposure, and outcome</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="diagnostic-test-quality.html#s4-2"><span class="code">S4.2</span> Build a diagnostic two-by-two table</a></li></ul></div></div></div>
```

## S4.2 Build a diagnostic two-by-two table {#s4-2}

```{=html}
<div class="skill-body"><p class="skill-scope">Test result against true status from a reference test.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="diagnostic-test-quality.html#s4-1"><span class="code">S4.1</span> Distinguish validity, reliability, and precision</a></li><li><a href="population-unit-and-case.html#s2-8"><span class="code">S2.8</span> Write a case definition</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="diagnostic-test-quality.html#s4-3"><span class="code">S4.3</span> Calculate and interpret sensitivity and specificity</a></li><li><a href="diagnostic-test-quality.html#s4-6"><span class="code">S4.6</span> Calculate and interpret kappa</a></li></ul></div></div></div>
```

## S4.3 Calculate and interpret sensitivity and specificity {#s4-3}

```{=html}
<div class="skill-body"><p class="skill-scope">Calculation from a two-by-two table and meaning for a test user.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="diagnostic-test-quality.html#s4-2"><span class="code">S4.2</span> Build a diagnostic two-by-two table</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="diagnostic-test-quality.html#s4-4"><span class="code">S4.4</span> Calculate and interpret predictive values</a></li><li><a href="diagnostic-test-quality.html#s4-5"><span class="code">S4.5</span> Estimate true prevalence from apparent prevalence</a></li><li><a href="diagnostic-test-quality.html#s4-7"><span class="code">S4.7</span> Predict the effect of serial and parallel testing</a></li><li><a href="diagnostic-test-quality.html#s4-9"><span class="code">S4.9</span> Link test timing to natural history</a></li><li><a href="diagnostic-test-quality.html#s4-10"><span class="code">S4.10</span> Adjust a detection sample size for an imperfect test</a></li><li><a href="surveillance-systems.html#s7-3"><span class="code">S7.3</span> Assess the attributes of a surveillance system</a></li><li><a href="appraising-analytical-reports.html#s10-2"><span class="code">S10.2</span> Identify selection bias and information bias</a></li></ul></div></div></div>
```

## S4.4 Calculate and interpret predictive values {#s4-4}

```{=html}
<div class="skill-body"><p class="skill-scope">Positive and negative predictive values and their change with prevalence.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="diagnostic-test-quality.html#s4-3"><span class="code">S4.3</span> Calculate and interpret sensitivity and specificity</a></li><li><a href="population-unit-and-case.html#s2-10"><span class="code">S2.10</span> Calculate a prevalence</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="diagnostic-test-quality.html#s4-8"><span class="code">S4.8</span> Choose a testing strategy for a purpose</a></li></ul></div></div></div>
```

## S4.5 Estimate true prevalence from apparent prevalence {#s4-5}

```{=html}
<div class="skill-body"><p class="skill-scope">Correction with test sensitivity and specificity. Conditions under which the correction fails.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="diagnostic-test-quality.html#s4-3"><span class="code">S4.3</span> Calculate and interpret sensitivity and specificity</a></li><li><a href="population-unit-and-case.html#s2-10"><span class="code">S2.10</span> Calculate a prevalence</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="risk-of-introduction-and-spread.html#s14-3"><span class="code">S14.3</span> Assess the likelihood of release</a></li></ul></div></div></div>
```

## S4.6 Calculate and interpret kappa {#s4-6}

```{=html}
<div class="skill-body"><p class="skill-scope">Observed and expected agreement. Dependence of kappa on prevalence.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="diagnostic-test-quality.html#s4-2"><span class="code">S4.2</span> Build a diagnostic two-by-two table</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li>None in this course</li></ul></div></div></div>
```

## S4.7 Predict the effect of serial and parallel testing {#s4-7}

```{=html}
<div class="skill-body"><p class="skill-scope">Change in sensitivity and specificity of the combined result.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="diagnostic-test-quality.html#s4-3"><span class="code">S4.3</span> Calculate and interpret sensitivity and specificity</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="diagnostic-test-quality.html#s4-8"><span class="code">S4.8</span> Choose a testing strategy for a purpose</a></li></ul></div></div></div>
```

## S4.8 Choose a testing strategy for a purpose {#s4-8}

```{=html}
<div class="skill-body"><p class="skill-scope">Screening, confirmation, and herd-level decisions.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="diagnostic-test-quality.html#s4-4"><span class="code">S4.4</span> Calculate and interpret predictive values</a></li><li><a href="diagnostic-test-quality.html#s4-7"><span class="code">S4.7</span> Predict the effect of serial and parallel testing</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="risk-of-introduction-and-spread.html#s14-7"><span class="code">S14.7</span> Propose risk management measures</a></li></ul></div></div></div>
```

## S4.9 Link test timing to natural history {#s4-9}

```{=html}
<div class="skill-body"><p class="skill-scope">Detection windows for tests that find the agent and tests that find antibodies.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="population-unit-and-case.html#s2-7"><span class="code">S2.7</span> Describe the natural history of a disease</a></li><li><a href="diagnostic-test-quality.html#s4-3"><span class="code">S4.3</span> Calculate and interpret sensitivity and specificity</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li>None in this course</li></ul></div></div></div>
```

## S4.10 Adjust a detection sample size for an imperfect test {#s4-10}

```{=html}
<div class="skill-body"><p class="skill-scope">Herd sensitivity at concept level.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-applied">Applied</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="data-sources-and-sampling.html#s3-9"><span class="code">S3.9</span> Calculate sample size to detect disease</a></li><li><a href="diagnostic-test-quality.html#s4-3"><span class="code">S4.3</span> Calculate and interpret sensitivity and specificity</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="surveillance-systems.html#s7-6"><span class="code">S7.6</span> Interpret a freedom-from-disease claim</a></li></ul></div></div></div>
```

## Materials {#materials-section}

Articles, guides, and slide decks for C4 appear here when they are published.

::: {#materials}
:::

```{=html}
<nav class="comp-pager"><a class="prev" href="data-sources-and-sampling.html"><span>Previous</span><strong>C3 Data sources and sampling</strong></a><a class="next" href="occurrence-and-burden.html"><span>Next</span><strong>C5 Occurrence and burden</strong></a></nav>
```
