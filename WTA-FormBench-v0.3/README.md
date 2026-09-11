# WTA-FormBench v0.3 Frozen

This frozen artifact assembles the accepted v0.3 corrected samples for P001-P018. Agent-facing inputs are under `samples/`; evaluator-private references, masks and registries are separated.

Run `python validators/validate_wta_formbench_v0_3_frozen.py` from this directory to verify the final freeze.

## R7D Formal Freeze Repair
R7D applies two non-semantic formal repairs: it adds minimal evaluator-private `validation_trace.json` files for accepted source batches that did not include per-sample traces, and it uses a non-self-referential manifest hash policy. No public sample, reference model, formulation, source trace, metadata, mask, registry, schema or contract content is modified.

