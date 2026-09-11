# Data Description

Sample `P013-S04` provides public instance data. Field shapes and domains are explicit below.

| Field | Meaning | Type | Shape / keys | Domain | Role |
|---|---|---|---|---|---|
| `uavs` | UAV identifiers | array[string] | unique list | unique identifiers | defines UAV index |
| `far_radars` | frequency-agile radar identifiers | array[string] | unique list | unique identifiers | defines FAR index |
| `frames` | dynamic frame identifiers | array[string] | unique list | ordered frame identifiers | defines frame index |
| `far_working_bandwidth` | working bandwidth that must be covered for each radar | object | FAR -> positive number | number > 0 | bandwidth coverage input |
| `uav_far_jsr` | jamming-to-signal ratio by frame, UAV and radar | object | frame -> UAV -> FAR -> nonnegative number | number >= 0 | jamming reward input |
| `effect_function_parameters` | parameters for the suppressive jamming effect function | object | parameter name -> number | positive numbers | effect function input |
| `cost_factor` | cost factor for UAV participation | number | scalar | number >= 0 | participation cost input |
| `uav_far_feasibility` | whether each UAV can suppress each radar at each frame | object | frame -> UAV -> FAR -> 0/1 | 0 or 1 | assignment feasibility input |
| `dynamic_frame_data` | frame-dependent radar and environment observations | object | frame -> public frame data | scenario data | dynamic per-frame data input |
