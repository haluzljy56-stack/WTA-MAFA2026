# WTA-MAFA — Benchmark and Supplementary Artifacts

Anonymous release accompanying *WTA-MAFA: Domain-Specific Multi-Agent Automated
Modeling for Air and Missile Defense Weapon-Target Assignment*.

This repository holds two things: the WTA-FormBench benchmark, and the
machine-readable artifacts behind the paper's results.

```
WTA-FormBench-v0.3/    the frozen benchmark (18 source families, 144 samples)
supplementary/         case traces, prompts, result tables, figures, diversity analysis
```

## WTA-FormBench-v0.3

A source-disjoint formulation benchmark assembled from 18 air and missile defense
papers, used in the paper to test how far the modeling process transfers across
scenarios. No optimizer is executed on it: the public material for these source
papers does not supply enough parameters to instantiate solvable models, so each
sample terminates at a validated formulation bundle.

| Directory | Contents |
| --- | --- |
| `samples/` | Agent-visible input per sample: `scenario_nl.md`, `data_description.md`, `instance_data.json` |
| `hidden_reference/` | Evaluator-private reference formulations, source traces, validation traces |
| `assessability_masks/` | Required / optional / withheld / unsupported element registration per sample |
| `element_registry/` | Canonical element definitions per source family |
| `schemas/`, `validators/` | Contract schemas and the frozen validator |
| `benchmark_card.md` | Frozen specification |
| `leakage_and_boundary_statement.md` | Public / evaluator-private boundary |

Splits are `dev` (54), `formal` (72) and `stress` (18). Each family contributes
controlled variants S01--S08: S01--S03 vary disclosure level, S04--S05 vary scale,
S06--S07 add resource, temporal or constraint pressure, and S08 is a
family-specific stress variant.

**Please keep `hidden_reference/` and `assessability_masks/` out of any system's
input.** They are released so results can be reproduced and audited; feeding them
to a model under evaluation invalidates the benchmark.

## supplementary/

Artifacts supporting the paper's claims: two complete end-to-end case traces
(one repaired success, one bounded-repair failure), the agent prompts, all
supplementary tables and figures, the per-instance records for all 182 SWTA and
MADRA samples, and the cross-family diversity analysis. See
`supplementary/README.md` for the full index.

## Reproducing the diversity analysis

`supplementary/diversity/` contains the measurement reported in the paper's
scenario-breadth section: per-sample model structure, the pairwise family
similarity matrix, and family-distinctive naming. It is computed from the
system's own outputs and does not depend on any scorer.

## Notes

- All content is released under the anonymity requirements of double-blind review.
- Some artifact records emitted by earlier runs use the internal name `EBW` for
  the object the paper calls the Shared Construction Workspace (SCW).
