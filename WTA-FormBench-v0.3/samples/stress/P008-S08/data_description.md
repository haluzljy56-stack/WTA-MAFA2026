# Data Description

Sample `P008-S08` provides public instance data. Field shapes and domains are explicit below.

| Field | Meaning | Type | Shape / keys | Domain | Role |
|---|---|---|---|---|---|
| `targets` | incoming target identifiers | array[string] | unique list | unique identifiers | target index |
| `sensors` | sensor identifiers | array[string] | unique list | unique identifiers | sensor index |
| `weapons` | weapon identifiers | array[string] | unique list | unique identifiers | weapon index |
| `time_horizon` | discrete time identifiers | array[string] | unique ordered list | unique identifiers | time index |
| `attempts_by_target` | possible interception attempts per target | object | target -> list[attempt] | unique attempt ids | attempt index |
| `target_value` | target value weight | object | target -> nonnegative number | number >= 0 | objective weight |
| `sensor_visibility` | sensor visibility by target and time | object | sensor -> target -> time -> 0/1 | 0 or 1 | sensor visibility constraint |
| `sensor_channel_capacity` | tracking channel capacity per sensor | object | sensor -> nonnegative integer | integer >= 0 | sensor capacity constraint |
| `weapon_engagement_envelope` | weapon engagement feasibility by target/time | object | weapon -> target -> time -> 0/1 | 0 or 1 | engagement-envelope constraint |
| `weapon_inventory` | launch inventory per weapon system | object | weapon -> nonnegative integer | integer >= 0 | weapon resource constraint |
| `weapon_reload_time` | reload separation per weapon system | object | weapon -> nonnegative time | number >= 0 | reload constraint |
| `target_impact_time` | predicted target impact time | object | target -> positive time index | positive integer | temporal constraint |
| `weapon_flight_time` | flight time for weapon-target engagements | object | weapon -> target -> nonnegative time | number >= 0 | temporal constraint |
| `sensor_tracking_time` | tracking duration before engagement | object | sensor -> target -> nonnegative time | number >= 0 | tracking-before-engagement constraint |
| `sensor_lock_time` | sensor lock/processing time | object | sensor -> target -> nonnegative time | number >= 0 | timing constraint |
| `kill_probability_coefficients_or_precomputed_values` | precomputed kill probability values for target-attempt-sensor-weapon-time combinations | object | key = target|attempt|sensor|weapon|time -> probability | [0,1] | interception probability input |
