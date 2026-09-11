# Benchmark Card

## Purpose
WTA-FormBench v0.3 evaluates formulation recovery for weapon-target-assignment families using controlled public inputs and hidden references.

## Scope
- 18 paper families, P001-P018.
- 8 sample variants per paper.
- Splits: dev 54, formal 72, stress 18.

## Public Input Format
Each sample exposes only `scenario_nl.md`, `data_description.md`, and `instance_data.json` to agents.

## Hidden Reference Usage
Hidden references are evaluator-private and contain reference formulations, source traces, metadata and validation traces.

## Assessability Mask Policy
Masks define required, optional, withheld and unsupported elements and must resolve against the corresponding element registry.

## Can Evaluate
Model-structure recovery, public/private boundary compliance, stress/pressure variant handling and source-faithful formulation choices.

## Cannot Evaluate
It is not a solver leaderboard, policy-training benchmark, or license to inspect hidden references during agent inference.

## Known Limitations
The benchmark is assembled from accepted batch artifacts; final freeze does not reinterpret papers or regenerate samples.

## Contamination Statement
No method outputs, agents, judges or solvers were invoked or read during final freeze assembly.

## R7D Formal Freeze Repair
R7D applies two non-semantic formal repairs: it adds minimal evaluator-private `validation_trace.json` files for accepted source batches that did not include per-sample traces, and it uses a non-self-referential manifest hash policy. No public sample, reference model, formulation, source trace, metadata, mask, registry, schema or contract content is modified.

