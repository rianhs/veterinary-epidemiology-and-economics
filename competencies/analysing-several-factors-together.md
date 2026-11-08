---
title: "C9. Analysing several factors together"
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
    categories: "C9"
---

```{=html}
<div class="comp-intro" style="--dc:var(--d2)">
<p class="comp-domain"><a href="../index.html#d2"><span class="dot"></span>Domain 2: Why is it happening?</a></p>
<p class="comp-lead">Analyse several factors together and interpret adjusted measures of association.</p>
<dl class="comp-facts"><div><dt>Skills</dt><dd>7</dd></div><div><dt>Depth</dt><dd>Core for interpretation, Applied for running models</dd></div></dl>
<div class="comp-links">
<div><h2 class="mini-title">Builds on</h2><ul><li><a href="comparing-groups-and-association.html"><span class="code">C8</span> Comparing groups and association</a></li><li><a href="../skills.html#x-skills"><span class="code">X5</span> Enter, clean, and summarize data in a spreadsheet</a></li><li><a href="../skills.html#x-skills"><span class="code">X7</span> Read a two-by-two contingency table and a chi-square test result</a></li><li><a href="../skills.html#x-skills"><span class="code">X8</span> Interpret a simple linear regression output</a></li></ul></div>
<div><h2 class="mini-title">Leads to</h2><ul><li><a href="appraising-analytical-reports.html"><span class="code">C10</span> Appraising analytical reports</a></li><li><a href="designing-observational-studies.html"><span class="code">C11</span> Designing observational studies</a></li><li><a href="evaluating-interventions.html"><span class="code">C18</span> Evaluating interventions</a></li></ul></div>
</div>
<p class="comp-howto">Learn the skills in order. Each skill shows what it covers, what you need first, and where it leads.</p>
</div>
```

## S9.1 Explain confounding {#s9-1}

```{=html}
<div class="skill-body"><p class="skill-scope">A third factor related to both the exposure and the outcome distorts the association.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="comparing-groups-and-association.html#s8-4"><span class="code">S8.4</span> Calculate risk ratio, odds ratio, and risk difference</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="analysing-several-factors-together.html#s9-2"><span class="code">S9.2</span> Distinguish confounding from effect modification</a></li><li><a href="analysing-several-factors-together.html#s9-3"><span class="code">S9.3</span> Explain why one-factor tests can mislead</a></li><li><a href="designing-observational-studies.html#s11-3"><span class="code">S11.3</span> Plan bias control in a study design</a></li><li><a href="evaluating-interventions.html#s18-3"><span class="code">S18.3</span> Identify alternative explanations for a change</a></li></ul></div></div></div>
```

## S9.2 Distinguish confounding from effect modification {#s9-2}

```{=html}
<div class="skill-body"><p class="skill-scope">Distortion of an association compared with a real difference between groups.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="analysing-several-factors-together.html#s9-1"><span class="code">S9.1</span> Explain confounding</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="analysing-several-factors-together.html#s9-4"><span class="code">S9.4</span> Calculate an adjusted odds ratio by stratification</a></li></ul></div></div></div>
```

## S9.3 Explain why one-factor tests can mislead {#s9-3}

```{=html}
<div class="skill-body"><p class="skill-scope">A chi-square or Fisher exact test for each factor alone ignores the other factors.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="analysing-several-factors-together.html#s9-1"><span class="code">S9.1</span> Explain confounding</a></li><li><a href="../skills.html#x-skills"><span class="code">X7</span> Read a two-by-two contingency table and a chi-square test result</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="analysing-several-factors-together.html#s9-5"><span class="code">S9.5</span> Explain what a logistic regression model does</a></li></ul></div></div></div>
```

## S9.4 Calculate an adjusted odds ratio by stratification {#s9-4}

```{=html}
<div class="skill-body"><p class="skill-scope">Stratum-specific odds ratios and the Mantel-Haenszel odds ratio, compared with the crude odds ratio.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-applied">Applied</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="analysing-several-factors-together.html#s9-2"><span class="code">S9.2</span> Distinguish confounding from effect modification</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li>None in this course</li></ul></div></div></div>
```

## S9.5 Explain what a logistic regression model does {#s9-5}

```{=html}
<div class="skill-body"><p class="skill-scope">A model for a two-category outcome with several factors at once. Coefficients and odds ratios.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="analysing-several-factors-together.html#s9-3"><span class="code">S9.3</span> Explain why one-factor tests can mislead</a></li><li><a href="../skills.html#x-skills"><span class="code">X8</span> Interpret a simple linear regression output</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="analysing-several-factors-together.html#s9-6"><span class="code">S9.6</span> Interpret crude and adjusted odds ratios</a></li></ul></div></div></div>
```

## S9.6 Interpret crude and adjusted odds ratios {#s9-6}

```{=html}
<div class="skill-body"><p class="skill-scope">Odds ratios and confidence intervals from a logistic regression table.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-core">Core</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="analysing-several-factors-together.html#s9-5"><span class="code">S9.5</span> Explain what a logistic regression model does</a></li><li><a href="comparing-groups-and-association.html#s8-6"><span class="code">S8.6</span> Interpret the precision of a measure of association</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li><a href="analysing-several-factors-together.html#s9-7"><span class="code">S9.7</span> Run a logistic regression on prepared data</a></li><li><a href="appraising-analytical-reports.html#s10-3"><span class="code">S10.3</span> Judge how a report handled confounding</a></li></ul></div></div></div>
```

## S9.7 Run a logistic regression on prepared data {#s9-7}

```{=html}
<div class="skill-body"><p class="skill-scope">Fit the model in software and report adjusted odds ratios.</p>
<div class="skill-grid"><div><h3 class="mini-title">Depth</h3><p class="depth depth-applied">Applied</p></div>
<div><h3 class="mini-title">Needs first</h3><ul><li><a href="analysing-several-factors-together.html#s9-6"><span class="code">S9.6</span> Interpret crude and adjusted odds ratios</a></li><li><a href="../skills.html#x-skills"><span class="code">X5</span> Enter, clean, and summarize data in a spreadsheet</a></li></ul></div>
<div><h3 class="mini-title">Leads to</h3><ul><li>None in this course</li></ul></div></div></div>
```

## Materials {#materials-section}

Articles, guides, and slide decks for C9 appear here when they are published.

::: {#materials}
:::

```{=html}
<nav class="comp-pager"><a class="prev" href="comparing-groups-and-association.html"><span>Previous</span><strong>C8 Comparing groups and association</strong></a><a class="next" href="appraising-analytical-reports.html"><span>Next</span><strong>C10 Appraising analytical reports</strong></a></nav>
```
