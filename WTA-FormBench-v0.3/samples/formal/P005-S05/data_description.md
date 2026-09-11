# Data Description

Sample `P005-S05` exposes the following agent-facing instance fields. Field shapes, index order and domains are defined explicitly below.

| Field | Meaning | Type | Shape / keys | Domain | Role |
|---|---|---|---|---|---|
| `weapon_categories` | weapon category identifiers | array[string] | unique list | unique identifiers | defines weapon index set |
| `targets` | target identifiers | array[string] | unique list | unique identifiers | defines target index set |
| `stages` | attack stage identifiers | array[string] | unique ordered list | unique identifiers | defines stage index set |
| `weapon_unit_cost` | unit cost for each weapon category | object | weapon_category -> nonnegative number | number >= 0 | objective cost input |
| `weapon_target_destroy_probability` | destroy probability for one weapon against one target | object | weapon_category -> target -> probability | [0,1] | damage accumulation input |
| `stage_weapon_inventory` | available weapon count per stage and category | object | stage -> weapon_category -> nonnegative integer inventory | integer >= 0 | stage capacity input |
| `target_stage_availability` | whether each target can be engaged in each stage | object | target -> stage -> binary availability | 0 or 1 | stage reachability input |
| `target_damage_threshold` | required accumulated damage probability for each target | object | target -> required damage probability | [0,1] | threshold constraint input |
