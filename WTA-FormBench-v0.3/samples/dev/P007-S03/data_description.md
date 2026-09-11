# Data Description

Sample `P007-S03` provides public instance data. Field shapes and domains are explicit below.

| Field | Meaning | Type | Shape / keys | Domain | Role |
|---|---|---|---|---|---|
| `platforms` | attack platform identifiers | array[string] | unique list | unique identifiers | defines platform index |
| `targets` | target identifiers | array[string] | unique list | unique identifiers | defines target index |
| `hit_probability` | probability that a platform attack hits a target | object | platform -> target -> probability | [0,1] | objective residual input |
| `target_value` | target value weight | object | target -> nonnegative number | number >= 0 | first objective input |
| `target_threat_degree` | target threat degree weight | object | target -> nonnegative number | number >= 0 | second objective input |
| `weapon_cost` | resource cost per platform assignment | object | platform -> nonnegative number | number >= 0 | third objective input |
| `platform_weapon_capacity` | maximum number of assignments per platform | object | platform -> nonnegative integer | integer >= 0 | platform capacity constraint |
| `target_max_assigned_weapons` | upper bound on weapons assigned to each target | object | target -> positive integer | integer >= 1 | target upper-bound constraint |
| `range_feasibility` | whether each platform-target pair is reachable | object | platform -> target -> 0/1 | 0 or 1 | range constraint input |
