# WTA-MAFA — Supplementary Artifact Bundle

Machine-readable artifacts supporting *WTA-MAFA: Domain-Specific Multi-Agent
Automated Modeling for Air and Missile Defense Weapon-Target Assignment*.

The paper's appendix carries curated excerpts. This bundle carries the complete
record: raw agent inputs, generated code, model registries, solver outputs, and
the full per-instance result tables that are too large to typeset.

`MANIFEST.json` indexes every file with its source section and caption.

---

## Layout

```
case_studies/
  case01_swta_success/     complete end-to-end trace of a successful SWTA run
  case02_madra_failure/    complete trace of a MADRA run that exhausted its repair budget
prompts/                   prompt text for the agent roles
tables/                    all 63 supplementary tables as CSV (+ INDEX.json)
figures/                   all 19 supplementary figures as PNG (+ INDEX.json)
diversity/                 cross-family scenario-adaptation analysis
MANIFEST.json              index of every artifact
```

## Cross-family diversity (`diversity/`)

Evidence that the formulations WTA-MAFA produces differ across WTA-FormBench
families, measured from the system's own outputs rather than from any scorer.

| File | Content |
| --- | --- |
| `per_sample.csv` | Per-sample structure: variable/constraint/objective counts, decision index signatures, variable and constraint names, generated-code size |
| `family_similarity.csv` | 18 $\times$ 18 matrix of pairwise Jaccard similarity between family naming vocabularies |
| `family_distinctive_terms.csv` | Per family, the naming tokens that occur in that family and no other |

Vocabulary is built only from the names the model gives its own variables,
constraints and objective contract; free-text descriptions and artifact digests
are excluded, since digests are unique per sample and would manufacture apparent
distinctiveness.

## Case studies

Each directory reconstructs one run in the order the system produced it, so the
chain from raw public input to final artifacts can be replayed step by step.

| File | Stage | What it records |
| --- | --- | --- |
| `raw_public_input_json.json` | Input | The complete public instance handed to the agents |
| `public_problem_description.md` | Input | The natural-language scenario the agents read |
| `planner_output.json` | Design Layer | Task boundary, modeling objects, unsupported assumptions |
| `model_design_card.json` | Design Layer | Variables, objectives, constraints, data bindings |
| `critic_report.json` | Design Layer | Completeness and conflict findings on the Design Card |
| `routing_decision.json` | Error Router | Defect attribution and repair ticket |
| `route_history.json` | Error Router | Full routing sequence across repair rounds |
| `builder_code.py` | Core Modeling | The generated executable Gurobi model |
| `model_registry.json` | Core Modeling | Variable-to-semantics bindings used for decoding |
| `solver_result.json` | Solver | Raw solver return |
| `solution_view.json` | Decoding | Human-readable decoded allocation |
| `mathematical_export_tex.tex` | Export | Mathematical description derived from the same basis |
| `mathematical_export_markdown.md` | Export | Same description in Markdown |
| `failure_report.json` | Audit | *(case 2 only)* Retained failure type and diagnostics |
| `formulation_note.md` | Audit | *(case 2 only)* Partial-output note |

**Case 1** is `MultiSWTA2_Type1_NT50_NS8_NC6_NV8_NW6_O4` (SWTA_MOP1_5, profile
MOP2). It is a *repaired* success: the first Design Card failed the contract
check with `MODEL_DESIGN_SECTION_EMPTY`, the Error Router attributed the defect
to Modeler, one bounded local repair fixed it, and the run then closed the full
loop through build, solve, decode, and replay.

**Case 2** is `MADRA_OPEN_P6_single` (P6, 50 targets). The front end produced a
formulation, but the Builder Team's variable slot returned a response missing
required object fields (`BUILDER_SLOT_MISSING`). After one bounded repair round
the run terminated with its owner, phase, and partial artifacts retained rather
than discarded — the behaviour described in Section 3.5 of the paper.

All JSON files in this bundle parse as valid JSON; `builder_code.py` parses as
valid Python. They are reproduced verbatim from the run records.

## Tables

CSV filenames carry the supplementary table label and caption, for example
`table_A18_formal_family_level_formulation_recovery.csv`. Tables without a
label in the source document are prefixed `table_uNN_` and named by the section
they belong to.

The four largest are the ones the paper cannot typeset:

| File | Size | Content |
| --- | --- | --- |
| `table_9_reference_context_comparison_details.csv` | 911 rows | Per-sample, per-preference reference comparison |
| `table_8_full_preference_profile_results.csv` | 911 rows | Per-sample, per-preference profile scores |
| `table_7_full_per_instance_failure_taxonomy.csv` | 183 rows | Failure type, defect code, owner, phase |
| `table_4_full_182_sample_per_instance_core_results.csv` | 183 rows | Per-instance modeling funnel |

Together with `table_5` (domain quality) and `table_6` (runtime and tokens),
these give the complete 182-sample record behind every aggregate in the paper,
including the failed samples that remain in the denominator.

## Prompts

`prompts/` contains the verbatim prompt text for Planner, Modeler, Critic,
ErrorRouter, Revisor, and Executable Builder. The paper's appendix reproduces
these in full as well; they are duplicated here for programmatic use.

## Notes

- Evaluator-private material (hidden references, answer keys, assessability
  masks) is deliberately excluded. The agents never receive it, and releasing it
  would invalidate the benchmark for later users.
- Figure and table numbering follows the appendix of the submitted manuscript.
- Terminology: the shared construction state is called the Shared Construction
  Workspace (SCW) in the paper. Some artifact records emitted by earlier runs use
  the internal name `EBW` for the same object.
