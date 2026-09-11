# Data Description

Sample `P015-S02` provides public instance data. Field shapes and domains are explicit below.

| Field | Meaning | Type | Shape / keys | Domain | Role |
|---|---|---|---|---|---|
| `air_defense_systems` | air-defense system identifiers | array[string] | unique list | unique identifiers | defines deployment system index |
| `candidate_positions` | candidate deployment positions | array[object] | list of id/x/y records | candidate coordinates | deployment candidate set |
| `position_suitability` | whether a candidate position is suitable | object | candidate -> 0/1 | 0 or 1 | deployment feasibility input |
| `defense_radius` | defense radius of each deployed system | number | scalar | number > 0 | fire-threat range input |
| `drone_start_point` | drone swarm start point | object | x/y coordinate | coordinate | path response input |
| `drone_entry_point` | drone swarm entry or terminal point | object | x/y coordinate | coordinate | path response input |
| `terrain_or_grid_cost_data` | terrain and grid cost data for path planning | object | candidate keyed cost maps | nonnegative costs | path cost input |
| `path_cost_weights` | weights for path cost components | object | component -> nonnegative number | number >= 0 | path response objective input |
| `swarm_interval_delta` | distance or interval update after interception | number | scalar | number > 0 | replanning response input |
| `path_planning_graph` | public path graph for drone path response | object | nodes and weighted edges | graph data | lower-level path response input |
