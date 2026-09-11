# Data Description

Sample `P009-S06` provides public instance data. Field shapes and domains are explicit below.

| Field | Meaning | Type | Shape / keys | Domain | Role |
|---|---|---|---|---|---|
| `targets` | target identifiers | array[string] | unique list | unique identifiers | target index |
| `sensors` | sensor identifiers | array[string] | unique list | unique identifiers | sensor tuple component |
| `weapon_vehicles` | weapon vehicle identifiers | array[string] | unique list | unique identifiers | weapon tuple component |
| `time_moments` | interception moment identifiers | array[string] | unique ordered list | unique identifiers | time tuple component |
| `mop_type` | source-defined benchmark type setting | string | categorical scalar | SWTA_MOP1..SWTA_MOP5 or configurable stress | benchmark configuration |
| `target_value` | interception value of each target | object | target -> nonnegative number | number >= 0 | F1 input |
| `detection_probability` | detection probability for tuple sensor/time/target | object | sensor -> time -> target -> probability | [0,1] | tuple probability input |
| `interception_probability` | interception probability for tuple weapon/time/target | object | weapon vehicle -> time -> target -> probability | [0,1] | tuple probability input |
| `sensor_cost` | tracking cost per sensor | object | sensor -> nonnegative number | number >= 0 | F2 input |
| `weapon_cost` | usage cost per weapon vehicle | object | weapon vehicle -> nonnegative number | number >= 0 | F2 input |
| `target_interception_duration` | time required after chosen moment to complete interception | object | target -> nonnegative duration | number >= 0 | G1 input |
| `target_flight_time` | latest allowable target flight/impact time | object | target -> positive time | positive number | G1 input |
| `target_channel_requirement` | sensor channels required by a target | object | target -> nonnegative integer | integer >= 0 | G2 input |
| `target_detection_persistence_time` | time required for consistent detection | object | target -> nonnegative duration | number >= 0 | G2 input |
| `sensor_channel_capacity` | sensor channel capacity | object | sensor -> nonnegative integer | integer >= 0 | G2 input |
| `weapon_vehicle_capacity` | weapon vehicle capacity | object | weapon vehicle -> nonnegative integer | integer >= 0 | G3 input |
| `weapon_firing_interval` | minimum firing interval per weapon vehicle | object | weapon vehicle -> nonnegative time | number >= 0 | G4 input |
