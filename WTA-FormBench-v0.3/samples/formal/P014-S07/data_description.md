# Data Description

Sample `P014-S07` provides public instance data. Field shapes and domains are explicit below.

| Field | Meaning | Type | Shape / keys | Domain | Role |
|---|---|---|---|---|---|
| `weapon_platforms` | weapon or interceptor platform identifiers | array[string] | unique list | unique identifiers | defines weapon index |
| `sensor_platforms` | sensor platform identifiers | array[string] | unique list | unique identifiers | defines sensor index |
| `targets` | UAV target identifiers | array[string] | unique list | unique identifiers | defines target index |
| `weapon_target_destruction_probability` | destruction probability for weapon-target pairs | object | weapon -> target -> probability | [0,1] | destruction probability input |
| `sensor_target_tracking_probability` | tracking probability for sensor-target pairs | object | sensor -> target -> probability | [0,1] | tracking probability input |
| `target_threat_value` | threat value of each target | object | target -> nonnegative number | number >= 0 | threat elimination objective input |
| `weapon_usage_cost` | cost of using each weapon platform | object | weapon -> nonnegative number | number >= 0 | cost objective input |
| `sensor_activation_cost` | cost of activating each sensor platform | object | sensor -> nonnegative number | number >= 0 | cost objective input |
| `total_ammunition_baseline` | baseline ammunition for reserved-strength objective | number | scalar | number > 0 | reserved-strength objective denominator |
| `sensor_capacity` | tracking capacity for each sensor platform | object | sensor -> positive integer | integer >= 1 | sensor capacity constraint input |
