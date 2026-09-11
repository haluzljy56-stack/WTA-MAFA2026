# Data Description

Sample `P010-S07` provides public instance data. Field shapes and domains are explicit below.

| Field | Meaning | Type | Shape / keys | Domain | Role |
|---|---|---|---|---|---|
| `weapons` | weapon identifiers | array[string] | unique list | unique identifiers | defines the weapon index |
| `targets` | target identifiers | array[string] | unique list | unique identifiers | defines the target index |
| `weapon_target_kill_probability` | kill probability for each weapon-target pair | object | weapon -> target -> probability | [0,1] | destruction probability input |
| `target_value` | reward value for destroying each target | object | target -> nonnegative number | number >= 0 | destroyed-target reward input |
| `target_kill_threshold` | minimum combined kill probability required to count target destruction | object | target -> probability | [0,1] | destruction threshold input |
