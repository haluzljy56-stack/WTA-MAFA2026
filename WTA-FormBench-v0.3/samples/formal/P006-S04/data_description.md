# Data Description

Sample `P006-S04` exposes the following agent-facing instance fields. Field shapes, index order and domains are defined explicitly below.

| Field | Meaning | Type | Shape / keys | Domain | Role |
|---|---|---|---|---|---|
| `weapon_types` | six soft-kill or defensive weapon types | array[string] | unique list | exactly six identifiers | defines type index |
| `weapons_by_type` | weapons grouped under each weapon type | object | weapon_type -> list[weapon] | unique weapon identifiers | defines weapon-by-type sets |
| `missiles` | incoming missile identifiers considered in the stage | array[string] | unique list | unique identifiers | defines missile index |
| `dynamic_stages` | dynamic wrapper stage identifiers | array[string] | unique ordered list | unique identifiers | defines wrapper stages |
| `missile_values` | danger level or value weight for each missile | object | missile -> nonnegative number | number >= 0 | objective weight |
| `base_intercept_probability` | base intercept probability before range adjustment | object | weapon_type -> weapon -> missile -> probability | [0,1] | effectiveness input |
| `base_conditional_destroy_probability` | conditional defeat probability after intercept before range adjustment | object | weapon_type -> weapon -> missile -> probability | [0,1] | effectiveness input |
| `weapon_min_range` | minimum usable range for each weapon | object | weapon -> nonnegative distance | number >= 0 | range eligibility input |
| `weapon_max_range` | maximum usable range for each weapon | object | weapon -> nonnegative distance | number >= 0 | range eligibility input |
| `missile_coordinates` | current missile coordinates | object | missile -> {x,y,z} | numeric coordinates | geometry input |
| `weapon_coordinates` | weapon coordinates | object | weapon -> {x,y,z} | numeric coordinates | geometry input |
| `weapon_motion_angles` | weapon orientation angles | object | weapon -> angle fields | angles in degrees | coverage input |
| `weapon_coverage_angles` | weapon coverage half-angles | object | weapon -> horizontal/vertical half-angle | nonnegative angles | coverage input |
| `missile_guidance_type` | guidance class for each missile | object | missile -> guidance type | categorical | compatibility input |
| `guidance_counter_compatibility` | whether a weapon type can counter a guidance class | object | weapon_type -> guidance_type -> 0/1 | 0 or 1 | compatibility input |
| `overkill_threshold` | threshold controlling excessive assignment to one missile | number | scalar | [0,1] | over-assignment control input |
| `stage_setup_time` | setup time for each weapon in a stage | object | weapon -> nonnegative time | number >= 0 | dynamic interval input |
| `stage_destruction_time` | engagement/destruction time by weapon and missile | object | weapon -> missile -> nonnegative time | number >= 0 | dynamic interval input |
| `missile_speed` | missile speed used for coordinate updates | object | missile -> nonnegative speed | number >= 0 | dynamic update input |
| `weapon_missile_distance` | weapon-to-missile distance | object | weapon_type -> weapon -> missile | number >= 0 | range adjustment input |
| `range_adjusted_intercept_probability` | distance-adjusted intercept probability | object | weapon_type -> weapon -> missile | [0,1] | objective/constraint input |
| `range_adjusted_destroy_probability` | distance-adjusted conditional defeat probability | object | weapon_type -> weapon -> missile | [0,1] | objective/constraint input |
| `eligible_weapon_missile_pairs` | allowed assignment triples derived from range, coverage and guidance compatibility | array[object] | list of {weapon_type, weapon, missile} | members must belong to public sets | assignment eligibility input |
| `stage_interval` | computed interval used by the dynamic wrapper | number | scalar | number >= 0 | coordinate update input |
| `updated_missile_coordinates` | scenario-state coordinate update data | object | stage -> missile -> {x,y,z} | numeric coordinates | public dynamic state input |
