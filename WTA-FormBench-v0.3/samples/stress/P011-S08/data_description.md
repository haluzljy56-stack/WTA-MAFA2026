# Data Description

Sample `P011-S08` provides public instance data. Field shapes and domains are explicit below.

| Field | Meaning | Type | Shape / keys | Domain | Role |
|---|---|---|---|---|---|
| `missiles` | missile identifiers | array[string] | unique list | unique identifiers | defines the missile index |
| `targets` | target identifiers | array[string] | unique list | unique identifiers | defines the target index |
| `missile_cost` | cost of assigning or launching each missile | object | missile -> nonnegative number | number >= 0 | optional cost objective input |
| `missile_destructive_payload` | destructive payload of each missile | object | missile -> positive number | number > 0 | single-missile kill probability input |
| `target_value` | combat value weight for each target | object | target -> nonnegative number | number >= 0 | expected combat effectiveness input |
| `target_health` | health level of each target | object | target -> positive number | number > 0 | single-missile kill probability input |
| `missile_target_penetration_probability` | probability that a missile penetrates adversarial defense for a target | object | missile -> target -> probability | [0,1] | stochastic penetration input |
| `cost_objective_active` | whether the optional combat-cost objective is activated for this stress sample | boolean | scalar | true or false | multiobjective extension flag |
