# Data Description

Sample `P012-S02` provides public instance data. Field shapes and domains are explicit below.

| Field | Meaning | Type | Shape / keys | Domain | Role |
|---|---|---|---|---|---|
| `targets` | aerial target identifiers | array[string] | unique list | unique identifiers | defines target index |
| `radars` | radar identifiers | array[string] | unique list | unique identifiers | defines radar index |
| `missile_vehicles` | missile vehicle identifiers | array[string] | unique list | unique identifiers | defines missile vehicle index |
| `interception_attempts_by_target` | candidate interception attempts for each target | object | target -> array[attempt] | unique attempt identifiers per target | defines attempt index |
| `time_slots` | discrete planning time slots | array[string] | unique list | ordered time identifiers | defines time index |
| `target_value` | interception value of each target | object | target -> nonnegative number | number >= 0 | expected value input |
| `target_max_interception_count` | maximum planned interception attempts for each target | object | target -> positive integer | integer >= 1 | target attempt count input |
| `missile_vehicle_load` | available missile load for each vehicle | object | vehicle -> nonnegative integer | integer >= 0 | missile load constraint input |
| `missile_vehicle_cost` | operational cost per missile vehicle assignment | object | vehicle -> nonnegative number | number >= 0 | unsaturated-mode cost input |
| `radar_detection_feasibility` | whether a radar can detect a target at a time slot | object | target -> radar -> time -> 0/1 | 0 or 1 | radar detection feasibility |
| `radar_channel_capacity` | maximum radar channels per radar | object | radar -> positive integer | integer >= 1 | radar capacity constraint input |
| `radar_channel_requirement` | channels required to track one target | number | scalar | number > 0 | radar occupancy input |
| `radar_accuracy_factor` | radar accuracy factor by target, radar and time | object | target -> radar -> time -> probability | [0,1] | interception probability input |
| `missile_engagement_feasibility` | whether a missile vehicle can engage a target at a time slot | object | target -> vehicle -> time -> 0/1 | 0 or 1 | missile reachability input |
| `interception_probability_table_or_generation_inputs` | precomputed interception probabilities for target, attempt, vehicle, radar and time choices | object | target -> attempt -> vehicle -> radar -> time -> probability | [0,1] | scheduled interception probability input |
| `interception_timing_windows` | tracking, launch and end timing windows for each target attempt | object | target -> attempt -> timing fields | time identifiers and gap bounds | timing constraint input |
| `firepower_mode` | objective mode determined by target count and missile load | string | scalar | unsaturated or saturated | selects value-minus-cost or value-only objective |
