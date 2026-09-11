from __future__ import annotations

import gurobipy as gp
from gurobipy import GRB
from wta_mafa_agent_v0_4_clean.execution.solution_view_contract import SOLUTION_REGISTRY_ATTR
from wta_mafa_agent_v0_4_clean.runtime.builder_runtime_helpers import (
    PublicDataView,
    attach_solution_registry,
    runtime_linear_terms,
    runtime_solution_view_from_registry,
)

MODEL_REGISTRY = {'schema_version': 'wta-mafa-executable-first-model-registry-v1',
 'model_authority': 'executable_builder',
 'benchmark': 'SWTA_MOP1_5',
 'sample_id': 'MultiSWTA2_Type1_NT50_NS8_NC6_NV8_NW6_O4',
 'public_input_digest': '44b6357e874314c9b20730994a86eabc1379aa9d150ba3f53bc32a742eda40bf',
 'builder_entrypoint': 'build_model',
 'builder_kind': 'gurobi',
 'builder_code_digest': '',
 'variables': [{'id': 'x_E',
                'symbol': 'x[e]',
                'domain': 'binary',
                'description': '1 if the public candidate e is selected.'}],
 'objectives': [{'id': 'swta.expected_remaining_target_value_plus_cost',
                 'sense': 'minimize',
                 'description': 'Call runtime_linear_terms(data, '
                                'candidates=view.engagement_options(), '
                                "contract=MODEL_REGISTRY['objective_contract'], family=family). "
                                'Use returned constant_term and per-candidate coefficients to set '
                                'Gurobi objective: constant_term + sum(coefficient[e] * x_E[e]).'}],
 'objective_contract': {'schema_version': 'wta_mafa_agent_v0_4.objective_contract.v1',
                        'objective_id': 'swta.expected_remaining_target_value_plus_cost',
                        'sense': 'minimize',
                        'unit': 'scalarized_public_cost',
                        'solver_objective_formula': 'constant total_target_value plus selected '
                                                    'public resource costs minus selected expected '
                                                    'defended value',
                        'replay_formula': 'swta.expected_remaining_target_value_plus_cost',
                        'constant_term': 0.0,
                        'scale_factor': 1.0,
                        'comparison_tolerance': {'absolute': 1e-06, 'relative': 1e-06},
                        'term_schema': {'selected_terms_path': 'solution_view.selected_engagements',
                                        'contribution_field': 'objective_contribution',
                                        'constant_source_path': 'public_instance_data.target_value',
                                        'constant_aggregation': 'sum_once_per_target',
                                        'target_field': 'target',
                                        'target_value_field': 'target_value',
                                        'effectiveness_field': 'combined_effectiveness',
                                        'sensor_cost_field': 'sensor_cost',
                                        'weapon_cost_field': 'weapon_cost'},
                        'public_data_refs': ['public_instance_data.engagement_options',
                                             'derived_public_facts.temporal_action_space.compatible_engagements']},
 'active_objectives': {'all_available_objective_ids': ['F1', 'F2', 'F3', 'F4'],
                       'objective_count': 4,
                       'objective_definitions': {'F1': {'description': 'Expected remaining target '
                                                                       'value after selected '
                                                                       'defense effects.',
                                                        'evidence_ref': 'public_problem_description',
                                                        'formula_text': 'Minimize expected '
                                                                        'remaining target value '
                                                                        'after selected '
                                                                        'sensor-weapon-target '
                                                                        'engagements, using public '
                                                                        'detection and '
                                                                        'interception '
                                                                        'effectiveness.',
                                                        'id': 'F1',
                                                        'name': 'expected_remaining_target_value',
                                                        'sense': 'minimize',
                                                        'uses': ['target_value',
                                                                 'engagement_options',
                                                                 'combined_effectiveness']},
                                                 'F2': {'description': 'Operating cost of selected '
                                                                       'sensors and weapon '
                                                                       'vehicles.',
                                                        'evidence_ref': 'public_problem_description',
                                                        'formula_text': 'Minimize public sensor '
                                                                        'and weapon resource-use '
                                                                        'costs induced by selected '
                                                                        'engagements.',
                                                        'id': 'F2',
                                                        'name': 'resource_usage_cost',
                                                        'sense': 'minimize',
                                                        'uses': ['sensor_cost',
                                                                 'weapon_cost',
                                                                 'engagement_options']},
                                                 'F3': {'description': 'Latest selected '
                                                                       'launch/interception plan '
                                                                       'time for the engagement '
                                                                       'scheme.',
                                                        'evidence_ref': 'public_problem_description',
                                                        'formula_text': 'Minimize the latest '
                                                                        'selected interception or '
                                                                        'engagement completion '
                                                                        'time.',
                                                        'id': 'F3',
                                                        'name': 'launch_interception_makespan',
                                                        'sense': 'minimize',
                                                        'uses': ['engagement_options',
                                                                 'best_interception_step']},
                                                 'F4': {'description': 'Risk from concentrating '
                                                                       'many engagements on a '
                                                                       'small number of resources.',
                                                        'evidence_ref': 'public_problem_description',
                                                        'formula_text': 'Minimize concentration '
                                                                        'risk induced by '
                                                                        'repeatedly assigning a '
                                                                        'small number of sensors '
                                                                        'or weapon vehicles across '
                                                                        'selected engagements.',
                                                        'id': 'F4',
                                                        'name': 'operational_concentration_risk',
                                                        'sense': 'minimize',
                                                        'uses': ['engagement_options']}},
                       'objective_ids': ['F1', 'F2', 'F3', 'F4'],
                       'source_boundary': 'objective_count/objective_ids come from the frozen '
                                          'public SWTA case manifest/config; objective meanings '
                                          'come from the public problem description.',
                       'source_paths': ['objective_count',
                                        'objective_ids',
                                        'public_case.objective_ids',
                                        'objective_definitions',
                                        'public_problem_description']},
 'solver_objective_contract': {'claim_boundary': 'The current solver-bound scalar is the '
                                                 'replayable F1+F2 contract. Active SWTA '
                                                 'objectives beyond F1/F2 are retained for '
                                                 'external vector reporting and cannot be claimed '
                                                 'as directly optimized unless a public '
                                                 'scalarization contract is added.',
                               'non_solver_active_objective_ids': ['F3', 'F4'],
                               'objective_contract_id': 'swta.expected_remaining_target_value_plus_cost',
                               'replay_formula_id': 'swta.expected_remaining_target_value_plus_cost',
                               'scalarization_status': 'declared_replayable_scalar_for_current_agent',
                               'sense': 'minimize',
                               'solver_binding': 'hard_solver_scalar',
                               'solver_bound_public_objective_ids': ['F1', 'F2'],
                               'solver_objective_must_match_replay': True},
 'evaluation_objective_vector_contract': {'active_objective_ids': ['F1', 'F2', 'F3', 'F4'],
                                          'claim_boundary': 'This vector contract preserves public '
                                                            'SWTA objective meaning for external '
                                                            'evaluation/reporting. It does not '
                                                            'grant the current Agent access to '
                                                            'external results and does not '
                                                            'override the solver-bound scalar.',
                                          'external_evaluator_only': True,
                                          'feedback_to_current_agent_allowed': False,
                                          'objective_count': 4,
                                          'objectives': [{'description': 'Expected remaining '
                                                                         'target value after '
                                                                         'selected '
                                                                         'sensor-weapon-target '
                                                                         'engagements.',
                                                          'id': 'F1',
                                                          'metric_field': 'F1_raw',
                                                          'name': 'expected_remaining_target_value',
                                                          'public_meaning_path': 'public_problem_description',
                                                          'replay_source_paths': ['solution_view.selected_engagements',
                                                                                  'public_instance_data.target_value'],
                                                          'replay_status': 'external_replay_available',
                                                          'reporting_note': 'Expected remaining '
                                                                            'target value is '
                                                                            'externally replayable '
                                                                            'from selected '
                                                                            'engagements.',
                                                          'required_solution_fields': ['target',
                                                                                       'target_value',
                                                                                       'combined_effectiveness'],
                                                          'sense': 'minimize',
                                                          'source_path': 'objective_definitions.F1'},
                                                         {'description': 'Public sensor and weapon '
                                                                         'resource-use cost '
                                                                         'induced by selected '
                                                                         'engagements.',
                                                          'id': 'F2',
                                                          'metric_field': 'F2_raw',
                                                          'name': 'resource_usage_cost',
                                                          'public_meaning_path': 'public_problem_description',
                                                          'replay_source_paths': ['solution_view.selected_engagements'],
                                                          'replay_status': 'external_replay_available',
                                                          'reporting_note': 'Resource usage cost '
                                                                            'is externally '
                                                                            'replayable from '
                                                                            'selected engagement '
                                                                            'costs.',
                                                          'required_solution_fields': ['sensor_cost',
                                                                                       'weapon_cost'],
                                                          'sense': 'minimize',
                                                          'source_path': 'objective_definitions.F2'},
                                                         {'description': 'Latest selected '
                                                                         'launch/interception plan '
                                                                         'time for the engagement '
                                                                         'scheme.',
                                                          'id': 'F3',
                                                          'metric_field': 'F3_raw',
                                                          'name': 'launch_interception_makespan',
                                                          'public_meaning_path': 'public_problem_description',
                                                          'replay_source_paths': ['solution_view.selected_engagements'],
                                                          'replay_status': 'hit_step_proxy_available_launch_step_not_materialized',
                                                          'reporting_note': 'The public objective '
                                                                            'is '
                                                                            'launch/interception '
                                                                            'makespan. The current '
                                                                            'compact public action '
                                                                            'space materializes '
                                                                            'representative '
                                                                            'hit/interception '
                                                                            'time, while '
                                                                            'launch_step is '
                                                                            'explicitly marked '
                                                                            'not_materialized in '
                                                                            'event_semantics.',
                                                          'required_solution_fields': ['hit_step'],
                                                          'sense': 'minimize',
                                                          'source_path': 'objective_definitions.F3'},
                                                         {'description': 'Operational '
                                                                         'concentration risk from '
                                                                         'repeatedly using a small '
                                                                         'number of public '
                                                                         'resources.',
                                                          'id': 'F4',
                                                          'metric_field': 'F4_raw',
                                                          'name': 'operational_concentration_risk',
                                                          'public_meaning_path': 'public_problem_description',
                                                          'replay_source_paths': ['solution_view.selected_engagements'],
                                                          'replay_status': 'external_reporting_available_from_selected_resource_usage',
                                                          'reporting_note': 'Operational '
                                                                            'concentration can be '
                                                                            'reported from '
                                                                            'selected public '
                                                                            'sensor/weapon '
                                                                            'resource usage.',
                                                          'required_solution_fields': ['sensor',
                                                                                       'weapon_vehicle'],
                                                          'sense': 'minimize',
                                                          'source_path': 'objective_definitions.F4'}],
                                          'reporting_fields': ['F1_raw',
                                                               'F2_raw',
                                                               'F3_raw',
                                                               'F4_raw'],
                                          'solver_vector_feedback_allowed': False},
 'constraints': [{'id': 'target_at_most_one', 'description': 'assignment_partition_limit'},
                 {'id': 'sensor_channel_capacity_time_indexed_weighted',
                  'description': 'time_indexed_resource_capacity'},
                 {'id': 'weapon_inventory', 'description': 'resource_inventory'},
                 {'id': 'weapon_min_launch_interval',
                  'description': 'same_resource_minimum_time_separation'}],
 'data_refs': [{'id': 'E',
                'path': 'derived_public_facts.temporal_action_space.compatible_engagements'}],
 'modeling_assumptions': [{'id': 'A_stage6_7_slots',
                           'text': 'Executable Builder slot JSON was assembled by the Stage 6.7 '
                                   'source shell.'}],
 'builder_slot_digests': {'variable_slot_llm': 'c4c4ca3632fb3ff5387e26d00c3b0bfc334c233b74f04f10e5b94430a0b43c60',
                          'objective_slot_llm': '5eeedfecdd5c6a92aa8cc4d7cc560680d089ba391cf83805c7679a55e0cd815a',
                          'constraint_slot_llm': 'eb3dbb684b1d486f9375b0c365a8a3b1c775608d0c1e0d7a2f5cfc512f4df54b',
                          'solution_view_slot_llm': 'ef5e63acb4472fdfae52f5991617d52fb32e49d0b4a9539abb46f39cff3dd75b',
                          'repair_slot_llm': '27aecafac5b6c0d472e89c6d263b1b844735849898b4f7a8a55c8c82c7eb3cb6'},
 'workspace_digest': '912a72ddcbb27cf9655b23b5614050d8e6db587167203da16887d3cc457ffcd3',
 'prompt_context_digest': '467b31816311e51e98caa7262195a870e9d14dc893f2638915c79780a0536e77',
 'boundary': {'hidden_reference_used': False,
              'non_public_builder_used': False,
              'solver_owns_optimize': True,
              'external_feedback_used': False,
              'ir_materialized': False},
 'reporting_notes': ['Slots are executable build slots, not an IR.',
                     'The generated build_model.py and literal MODEL_REGISTRY remain the final '
                     'authority.']}
ASSEMBLY_SLOT_PLAN = {'schema_version': 'wta_mafa_agent_v0_4_clean.builder_slot_assembly.v1',
 'family': 'swta',
 'slot_digests': {'variable_slot_llm': 'c4c4ca3632fb3ff5387e26d00c3b0bfc334c233b74f04f10e5b94430a0b43c60',
                  'objective_slot_llm': '5eeedfecdd5c6a92aa8cc4d7cc560680d089ba391cf83805c7679a55e0cd815a',
                  'constraint_slot_llm': 'eb3dbb684b1d486f9375b0c365a8a3b1c775608d0c1e0d7a2f5cfc512f4df54b',
                  'solution_view_slot_llm': 'ef5e63acb4472fdfae52f5991617d52fb32e49d0b4a9539abb46f39cff3dd75b',
                  'repair_slot_llm': '27aecafac5b6c0d472e89c6d263b1b844735849898b4f7a8a55c8c82c7eb3cb6'},
 'variable_binding': {'candidate_set_id': 'E',
                      'implementation_strategy': 'Create one binary variable per candidate from '
                                                 'PublicDataView.engagement_options() '
                                                 '(authoritative set E). Bind by identity_fields '
                                                 'sensor, weapon_vehicle, target, hit_step; no '
                                                 're-filtering.'},
 'objective_binding': {'objective_contract_id': 'swta.expected_remaining_target_value_plus_cost',
                       'implementation_strategy': 'Call runtime_linear_terms(data, '
                                                  'candidates=view.engagement_options(), '
                                                  "contract=MODEL_REGISTRY['objective_contract'], "
                                                  'family=family). Use returned constant_term and '
                                                  'per-candidate coefficients to set Gurobi '
                                                  'objective: constant_term + sum(coef'},
 'constraint_strategies': [{'slot_index': 1,
                            'pattern_id': 'assignment_partition_limit',
                            'required_semantics': ['for every target t, select at most one '
                                                   'engagement whose target is t'],
                            'implementation_strategy': 'For each target t, group candidates with '
                                                       'target==t and add sum(x_E[e] for e in '
                                                       'bucket_t) <= 1. O(|E|) total.'},
                           {'slot_index': 2,
                            'pattern_id': 'time_indexed_resource_capacity',
                            'required_semantics': ['for each sensor and time step, sum '
                                                   'target_channel_need[target[e]] over active '
                                                   'selected tracking intervals',
                                                   'do not replace this with an unweighted count '
                                                   'of selected engagements'],
                            'implementation_strategy': 'Pre-group candidates by (sensor, time) '
                                                       'where tracking_start_step <= time <= '
                                                       'tracking_end_step using materialized '
                                                       'tracking_start_step and tracking_end_step. '
                                                       'For each sensor s and each public time '
                                                       'step tau from '
                                                       'public_instance_data.sensor_cha'},
                           {'slot_index': 3,
                            'pattern_id': 'resource_inventory',
                            'required_semantics': ['for each weapon vehicle, selected engagements '
                                                   'cannot exceed public weapon inventory'],
                            'implementation_strategy': 'For each weapon_vehicle w, add sum(x_E[e] '
                                                       'for e with weapon_vehicle==w) <= '
                                                       'public_instance_data.weapon_inventory[w]. '
                                                       'O(|E|).'},
                           {'slot_index': 4,
                            'pattern_id': 'same_resource_minimum_time_separation',
                            'required_semantics': ['the public firing interval is a launch-event '
                                                   'rule, but current compact candidates '
                                                   'materialize hit_step rather than true '
                                                   'launch_step',
                                                   'until launch_step is materialized, the current '
                                                   'solver-bound contract enforces separation on '
                                                   'the explicit hit_step proxy',
                                                   'two selected engagements using the same '
                                                   'weapon_vehicle conflict when '
                                                   'abs(hit_step_i-hit_step_j) is smaller than the '
                                                   'public interval proxy',
                                                   'equal hit_step conflicts must not be excluded'],
                            'implementation_strategy': 'Use compact sliding-window conflict on '
                                                       'hit_step for each weapon_vehicle w and '
                                                       'public time window of width interval-1: '
                                                       'for each weapon w and window start tau, '
                                                       'add sum(x_E[e] for e with '
                                                       'weapon_vehicle==w and hit_step in [tau, '
                                                       'tau+interval-1])'}],
 'solution_view_fields': ['sensor', 'weapon_vehicle', 'target', 'hit_step'],
 'repair_scope': 'no_open_ticket'}


def _s(row, *keys):
    for key in keys:
        if isinstance(row, dict) and row.get(key) not in (None, ""):
            return str(row.get(key))
    return ""


def _f(row, *keys, default=0.0):
    for key in keys:
        try:
            value = row.get(key) if isinstance(row, dict) else None
            if value not in (None, ""):
                return float(value)
        except (TypeError, ValueError):
            pass
    return float(default)


def _i(row, *keys, default=None):
    for key in keys:
        try:
            value = row.get(key) if isinstance(row, dict) else None
            if value not in (None, ""):
                return int(float(value))
        except (TypeError, ValueError):
            pass
    return default


def _constraint_text():
    parts = []
    for slot in ASSEMBLY_SLOT_PLAN.get("constraint_strategies", []):
        if isinstance(slot, dict):
            parts.append(str(slot.get("pattern_id", "")))
            parts.append(str(slot.get("constraint_id", "")))
            parts.append(str(slot.get("strategy_id", "")))
            parts.extend(str(v) for v in slot.get("required_semantics", []) if str(v))
            parts.append(str(slot.get("implementation_strategy", "")))
    for slot in MODEL_REGISTRY.get("constraints", []):
        if isinstance(slot, dict):
            parts.append(str(slot.get("id", "")))
            parts.append(str(slot.get("description", "")))
    return " ".join(parts).lower()


def _has_constraint_signal(text, *tokens):
    return any(str(token).lower() in text for token in tokens if str(token))


def _add_group_limit(model, x, candidates, keys, limit_keys, default_limit, name):
    groups = {}
    limits = {}
    for idx, item in enumerate(candidates):
        key = tuple(_s(item, *keys).split("|"))
        if not any(key):
            continue
        groups.setdefault(key, []).append(idx)
        limit = _f(item, *limit_keys, default=default_limit)
        limits[key] = max(float(limits.get(key, limit)), float(limit))
    count = 0
    for key, indices in groups.items():
        limit = limits.get(key, default_limit)
        if indices and limit >= 0:
            model.addConstr(gp.quicksum(x[i] for i in indices) <= limit, name=f"{name}_{count}")
            count += 1
    return count


def _add_same_weapon_interval_windows(model, x, candidates):
    groups = {}
    for idx, item in enumerate(candidates):
        weapon = _s(item, "weapon_vehicle", "weapon", "weapon_id", "launcher_id", "launcher")
        hit_step = _i(item, "hit_step", "intercept_step", "time_step")
        min_launch_interval = _i(
            item,
            "weapon_min_launch_interval",
            "min_launch_interval",
            "weapon_interval",
            "min_intercept_interval",
            "ripple_interval",
            default=1,
        )
        if weapon and hit_step is not None and min_launch_interval is not None and min_launch_interval >= 1:
            groups.setdefault((weapon, int(min_launch_interval)), []).append((int(hit_step), idx))
    count = 0
    for group_key, rows in groups.items():
        interval = int(group_key[1])
        starts = sorted({hit for hit, _ in rows})
        for start in starts:
            window = [idx for hit, idx in rows if start <= hit <= start + interval - 1]
            if len(window) > 1:
                model.addConstr(gp.quicksum(x[i] for i in window) <= 1, name=f"weapon_interval_window_{count}")
                count += 1
    return count


def _add_public_constraints(model, x, candidates):
    text = _constraint_text()
    count = 0
    if _has_constraint_signal(
        text,
        "assignment_partition_limit",
        "target_at_most_one",
        "target_cardinality",
        "target_attempt_limit",
        "one_target",
        "target at most",
        "select at most one",
        "at most one engagement whose target",
    ):
        count += _add_group_limit(
            model,
            x,
            candidates,
            ("target", "target_id"),
            ("target_attempt_limit", "max_attempts_per_target", "target_capacity"),
            1.0,
            "target_limit",
        )
    if _has_constraint_signal(
        text,
        "resource_inventory",
        "weapon_inventory",
        "launcher_inventory",
        "inventory",
        "launcher capacity",
    ):
        count += _add_group_limit(
            model,
            x,
            candidates,
            ("weapon_vehicle", "weapon", "weapon_id", "launcher_id", "launcher"),
            ("weapon_inventory", "launcher_inventory", "inventory", "available_count", "capacity"),
            1.0,
            "resource_inventory",
        )
    if _has_constraint_signal(
        text,
        "time_indexed_resource_capacity",
        "sensor_channel_capacity_time_indexed_weighted",
        "sensor_channel_capacity",
        "sensor_capacity",
        "radar_capacity",
        "target_channel_need",
    ):
        count += _add_group_limit(
            model,
            x,
            candidates,
            ("sensor", "sensor_id", "radar_id", "radar"),
            ("sensor_capacity", "radar_capacity", "capacity"),
            1.0,
            "sensor_capacity",
        )
    if _has_constraint_signal(
        text,
        "same_resource_minimum_time_separation",
        "weapon_min_launch_interval",
        "weapon_interval",
        "min_launch_interval",
        "ripple",
        "same_weapon",
    ):
        count += _add_same_weapon_interval_windows(model, x, candidates)
    return count


def solution_view(model):
    registry = getattr(model, SOLUTION_REGISTRY_ATTR, {})
    return runtime_solution_view_from_registry(registry)


def build_model(data: dict, config: dict) -> dict:
    family = "swta"
    view = PublicDataView(data)
    candidates = view.engagement_options()
    model = gp.Model(str(MODEL_REGISTRY.get("sample_id", "wta_mafa_model")))
    try:
        model.Params.OutputFlag = 0
    except Exception:
        pass
    x = [model.addVar(vtype=GRB.BINARY, name=f"x_{i}") for i, _ in enumerate(candidates)]
    terms = runtime_linear_terms(
        data,
        candidates=candidates,
        contract=MODEL_REGISTRY["objective_contract"],
        family=family,
    )
    term_rows = terms.get("terms", [])
    expr = float(terms.get("constant_term") or 0.0)
    for i, var in enumerate(x):
        coeff = 0.0
        if i < len(term_rows) and isinstance(term_rows[i], dict):
            coeff = float(term_rows[i].get("coefficient") or 0.0)
        var.Obj = coeff
        expr = expr + coeff * var
    sense = str(terms.get("sense") or MODEL_REGISTRY["objective_contract"].get("sense") or "").lower()
    model.setObjective(expr, GRB.MINIMIZE if sense == "minimize" else GRB.MAXIMIZE)
    constraint_count = _add_public_constraints(model, x, candidates)
    attach_solution_registry(
        model,
        public_input=data,
        variables=x,
        candidates=candidates,
        terms=terms,
        contract=MODEL_REGISTRY["objective_contract"],
        family=family,
        extra={"builder_slot_digests": ASSEMBLY_SLOT_PLAN.get("slot_digests", {})},
    )
    variables = {"x": x}
    metrics = {
        "assembled_from_builder_slots": True,
        "candidate_count": len(candidates),
        "constraint_count_from_shell": constraint_count,
        "assembly_slot_plan_digest": '293c33c3af6f9b9ec02ddb908b16b5a2cdc349c461e0f97b87a71bb2ac887cfd',
        "slot_digests": ASSEMBLY_SLOT_PLAN.get("slot_digests", {}),
    }
    return {"model": model, "variables": variables, "metrics": metrics, "solution_view": solution_view}