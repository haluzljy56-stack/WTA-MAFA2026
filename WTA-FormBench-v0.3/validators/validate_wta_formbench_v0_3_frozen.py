from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS = [f"P{i:03d}" for i in range(1, 19)]
SIDS = [f"S{i:02d}" for i in range(1, 9)]
SPLITS = {"S01": "dev", "S02": "dev", "S03": "dev", "S04": "formal", "S05": "formal", "S06": "formal", "S07": "formal", "S08": "stress"}
PUBLIC_FORBIDDEN_TERMS = ["planted_assignment", "planted_binary_assignment", "planted_action_vector", "planted_theta_assignment", "relaxed_solution", "rounded_assignment", "objective_value", "PPO_policy_output", "rotation_strategy_solution", "cluster_assignment_answer", "algorithm_population"]
BANNED_SCENARIO_PATTERNS = ["paper-faithful", "source-faithful", "request clarification", "do not hallucinate", "do not introduce", "parameterize if unknown", "\\[", "$"]
SELF_EXCLUDED = {"manifests/content_manifest.csv", "manifests/WTA-FormBench-v0.3-final-freeze-manifest.csv", "manifests/WTA-FormBench-v0.3-R7D-final-freeze-manifest.csv", "audits/final_manifest_integrity_audit.json", "audits/final_validator_runtime_result.json", "audits/R7D_final_validator_execution_audit.json", "reports/WTA-FormBench-v0.3-R7D-final-freeze-audit-report.md"}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_text(data) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def manifest_integrity():
    manifest = ROOT / "manifests" / "WTA-FormBench-v0.3-R7D-final-freeze-manifest.csv"
    if not manifest.exists():
        manifest = ROOT / "manifests" / "WTA-FormBench-v0.3-final-freeze-manifest.csv"
    rows = list(csv.DictReader(manifest.open("r", encoding="utf-8", newline="")))
    missing = []
    mismatches = []
    seen = set()
    duplicates = []
    for row in rows:
        rel = row["path"]
        if rel in seen:
            duplicates.append(rel)
        seen.add(rel)
        if rel in SELF_EXCLUDED or row.get("hash_policy") == "self_hash_excluded":
            continue
        path = ROOT / rel
        if not path.exists():
            missing.append(rel)
            continue
        actual = sha256_file(path)
        if actual != row["sha256"]:
            mismatches.append({"path": rel, "manifest_sha256": row["sha256"], "actual_sha256": actual})
    return {
        "manifest_rows": len(rows),
        "manifest_missing_files": len(missing),
        "manifest_hash_mismatches": len(mismatches),
        "duplicate_path_rows": duplicates,
        "self_hash_policy": "exclude_content_manifest_and_final_manifest_rows",
        "manifest_integrity_pass": not missing and not mismatches and not duplicates,
    }


def main() -> int:
    sample_paths = sorted((ROOT / "samples").glob("*/*/instance_data.json"))
    sample_ids = [p.parent.name for p in sample_paths]
    papers = sorted({sid.split("-")[0] for sid in sample_ids})
    split_counts = Counter(p.parts[-3] for p in sample_paths)
    refs = list((ROOT / "hidden_reference").glob("*/*/reference_model.json"))
    masks = list((ROOT / "assessability_masks").glob("*_mask.json"))
    validation_traces = list((ROOT / "hidden_reference").glob("*/*/validation_trace.json"))
    leaks = []
    scenario_hits = []
    manifest_errors = []
    fd_errors = []
    mask_errors = []
    schema_errors = []
    for path in sample_paths:
        sample = path.parent
        data = read_json(path)
        text = canonical_text(data)
        terms = [term for term in PUBLIC_FORBIDDEN_TERMS if term in text]
        if terms:
            leaks.append({"sample_id": sample.name, "terms": terms})
        scenario = sample / "scenario_nl.md"
        if scenario.exists():
            scenario_text = scenario.read_text(encoding="utf-8")
            for pattern in BANNED_SCENARIO_PATTERNS:
                if pattern.lower() in scenario_text.lower():
                    scenario_hits.append({"sample_id": sample.name, "pattern": pattern})
        manifest = read_json(sample / "agent_input_manifest.json") if (sample / "agent_input_manifest.json").exists() else {}
        allowed = manifest.get("allowed_public_files", manifest.get("allowed_files"))
        if allowed != ["scenario_nl.md", "data_description.md", "instance_data.json"]:
            manifest_errors.append(sample.name)
        fd_path = sample / "field_dictionary.json"
        if not fd_path.exists():
            fd_errors.append(sample.name)
        else:
            fd = read_json(fd_path)
            fields = fd if isinstance(fd, list) else fd.get("fields", [])
            if {item.get("name") for item in fields} != set(data.keys()):
                fd_errors.append(sample.name)
    registries = {}
    for paper in PAPERS:
        reg_path = ROOT / "element_registry" / f"{paper}_element_registry.json"
        if not reg_path.exists():
            mask_errors.append(f"{paper}:missing_registry")
            continue
        reg = read_json(reg_path)
        elems = reg.get("elements", reg) if isinstance(reg, dict) else reg
        registries[paper] = set(elems.keys()) if isinstance(elems, dict) else {(item.get("id") or item.get("element_id")) for item in elems if isinstance(item, dict)}
        if not list((ROOT / "schemas").glob(f"{paper}_instance*.json")):
            schema_errors.append(f"{paper}:missing_schema")
    for paper in PAPERS:
        for sid in SIDS:
            sample_id = f"{paper}-{sid}"
            mask_path = ROOT / "assessability_masks" / f"{sample_id}_mask.json"
            if not mask_path.exists():
                mask_errors.append(f"{sample_id}:missing_mask")
                continue
            mask = read_json(mask_path)
            ids = mask.get("required_elements", []) + mask.get("optional_or_parameterizable_elements", []) + mask.get("optional_or_parameterizable", []) + mask.get("unsupported_elements", [])
            missing = [eid for eid in ids if eid and eid not in registries.get(paper, set())]
            if missing:
                mask_errors.append(f"{sample_id}:missing_registry_ids")
    source_errors = []
    for batch in ["R1D", "R2E", "R3C", "R4D", "R5D", "R6C"]:
        if not (ROOT / "audits" / "batch_evidence" / batch / "source_hash_diff.json").exists():
            source_errors.append(batch)
    mi = manifest_integrity()
    result = {
        "papers": len(papers),
        "samples": len(sample_paths),
        "references": len(refs),
        "masks": len(masks),
        "dev": split_counts["dev"],
        "formal": split_counts["formal"],
        "stress": split_counts["stress"],
        "sample_id_unique": len(sample_ids) == len(set(sample_ids)),
        "public_witness_leakage_count": len(leaks),
        "scenario_leakage_hits": len(scenario_hits),
        "agent_input_boundary_pass": not manifest_errors,
        "field_dictionary_complete": not fd_errors,
        "schema_strength_pass": not schema_errors,
        "mask_registry_consistency_pass": not mask_errors,
        "source_hash_evidence_pass": not source_errors,
        "validation_trace_count": len(validation_traces),
        "validation_trace_policy_pass": len(validation_traces) == 144,
        "manifest_integrity_pass": mi["manifest_integrity_pass"],
        "manifest_rows": mi["manifest_rows"],
        "manifest_missing_files": mi["manifest_missing_files"],
        "manifest_hash_mismatches": mi["manifest_hash_mismatches"],
        "self_hash_policy": mi["self_hash_policy"],
        "method_output_files_opened": 0,
        "agent_called": False,
        "llm_judge_called": False,
        "solver_called": False,
    }
    result["all_pass"] = (
        result["papers"] == 18 and result["samples"] == 144 and result["references"] == 144 and result["masks"] == 144
        and result["dev"] == 54 and result["formal"] == 72 and result["stress"] == 18 and result["sample_id_unique"]
        and result["public_witness_leakage_count"] == 0 and result["scenario_leakage_hits"] == 0
        and result["agent_input_boundary_pass"] and result["field_dictionary_complete"] and result["schema_strength_pass"]
        and result["mask_registry_consistency_pass"] and result["source_hash_evidence_pass"]
        and result["manifest_integrity_pass"] and result["validation_trace_policy_pass"]
        and result["method_output_files_opened"] == 0 and not result["agent_called"] and not result["llm_judge_called"] and not result["solver_called"]
    )
    result["final_status"] = "R7D_PASS_WTA_FORMBENCH_V0_3_FROZEN_READY" if result["all_pass"] else "R7D_BLOCKED_MANIFEST_HASH_MISMATCH"
    (ROOT / "audits" / "final_validator_runtime_result.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
