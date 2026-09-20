# Leakage and Boundary Statement

Agent-facing files only:

- `scenario_nl.md`
- `data_description.md`
- `instance_data.json`

Evaluator-private files:

- `hidden_reference/`
- `assessability_masks/`
- `element_registry/`
- `metadata.json`
- `validation_trace.json`

Evaluator-private files are not part of this public release.

The final validator checks public witness leakage, scenario leakage, agent input manifests and mask/registry consistency.

## R7D Formal Freeze Repair
R7D applies two non-semantic formal repairs: it adds minimal evaluator-private `validation_trace.json` files for accepted source batches that did not include per-sample traces, and it uses a non-self-referential manifest hash policy. No public sample, reference model, formulation, source trace, metadata, mask, registry, schema or contract content is modified.

