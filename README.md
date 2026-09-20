# WTA-MAFA — Benchmark and Supplementary Material

Release accompanying *WTA-MAFA: Domain-Specific Multi-Agent Automated Modeling
for Air and Missile Defense Weapon-Target Assignment*.

This repository holds two things: the WTA-FormBench benchmark, and the
supplementary material of the paper.

```
WTA-FormBench-v0.3/          the frozen benchmark (18 source families, 144 samples)
WTA-MAFA_supplementary.pdf   Appendixes A-K of the paper
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
| `schemas/`, `validators/` | Contract schemas and the frozen validator |
| `benchmark_card.md` | Frozen specification |
| `leakage_and_boundary_statement.md` | Public / evaluator-private boundary |

Splits are `dev` (54), `formal` (72) and `stress` (18). Each family contributes
controlled variants S01--S08: S01--S03 vary disclosure level, S04--S05 vary scale,
S06--S07 add resource, temporal or constraint pressure, and S08 is a
family-specific stress variant.

Evaluator-private material, namely the reference formulations, validation traces,
assessability masks and the canonical element registry, is withheld: releasing it would let a later system be
tuned against the answers and invalidate the benchmark.

## WTA-MAFA_supplementary.pdf

Appendixes A to K of the paper: protocol and execution settings, agent prompts and
output contracts, artifact coverage, expanded SWTA and MADRA results, the expert
reference comparison, ablation and robustness studies, the WTA-FormBench card and
construction procedure, and two complete end-to-end run traces.

## Notes

- Some artifact records emitted by earlier runs use the internal name `EBW` for
  the object the paper calls the Shared Construction Workspace (SCW).
