# Data Description

Sample `P004-S08` exposes the following agent-facing instance fields. Field shapes, index order and domains are defined explicitly below.

| Field | Meaning | Type | Shape / keys | Domain | Role |
|---|---|---|---|---|---|
| `threats` | incoming threat identifiers | array[string] | unique list | unique identifiers | defines threat index set |
| `ships` | friendly ship/platform identifiers | array[string] | unique list | unique identifiers | defines platform index set |
| `fire_channels` | fire-channel identifiers available for engagements | array[string] | unique list | unique identifiers | defines engagement resource set |
| `weapon_systems` | weapon-system identifiers carrying fire channels | array[string] | unique list | unique identifiers | defines round/setup resource set |
| `radars` | radar identifiers that can support illumination | array[string] | unique list | unique identifiers | defines radar support set |
| `time_slots` | discrete planning time slots | array[string] | unique ordered list | unique identifiers | defines temporal index |
| `engageable_pairs` | feasible threat and fire-channel pairs before timing filters | array[object] | objects with threat and fire_channel | members must belong to threats and fire_channels | public feasibility input |
| `engagement_windows` | earliest start and latest end for each threat-channel pair | object | key = threat|fire_channel; value has earliest_start/latest_end | time slot identifiers | limits engagement starts |
| `engagement_duration` | duration of an engagement by threat-channel pair and start time | object | key = threat|fire_channel; value = time_slot -> duration | positive integer duration | occupies scheduling resources |
| `weapon_rounds` | available rounds per weapon system | object | weapon_system -> nonnegative integer | integer >= 0 | weapon capacity input |
| `weapon_setup_times` | setup time between consecutive fires from each weapon system | object | weapon_system -> nonnegative integer | integer >= 0 | scheduling conflict input |
| `radar_setup_times` | setup time needed by each radar between support tasks | object | radar -> nonnegative integer | integer >= 0 | radar conflict input |
| `threat_values` | importance weight of each incoming threat | object | threat -> nonnegative number | number >= 0 | objective weight |
| `threat_hit_probabilities` | baseline probability that each threat hits its target without further defense | object | threat -> probability | [0,1] | objective risk input |
| `single_shot_kill_probabilities` | kill probability for one scheduled engagement | object | key = threat|fire_channel|time_slot | [0,1] | engagement effectiveness input |
| `target_ship` | targeted ship for each threat | object | threat -> ship | ship identifier | links threats to platforms |
| `threat_hit_times` | time slot at which each threat reaches its target ship | object | threat -> time_slot | time slot identifier | timing input for survival logic |
| `initial_ship_heading` | initial true heading of each ship | object | ship -> angle | 0 to 359 | heading state input |
| `ship_turn_rate` | maximum turn per time slot for each ship | object | ship -> nonnegative angle | number >= 0 | maneuver constraint input |
| `threat_bearings` | true bearing of threats from ships over time | object | ship -> threat -> time_slot -> angle | 0 to 359 | bearing input for blind sectors |
| `blind_sector_bounds` | fire-channel blind-sector angular intervals | object | fire_channel -> list of intervals with start/end angles | 0 to 359 degree bounds | exclusion input |
| `platform_survival_probability` | survival probability of the platform carrying a fire channel until engagement completion; source-derived trace, not a candidate solution | object | key = threat|fire_channel|time_slot -> probability | [0,1] | public risk-coupling input |
| `relative_bearing` | relative threat bearing after ship heading is considered | object | ship -> threat -> time_slot -> angle | 0 to 359 | supports blind-sector logic |
| `heading_wrap_auxiliaries` | precomputed heading wrap trace used to expose heading continuity data | object | planned_heading and wrap indicators by ship/time | angles and binary indicators | public geometry trace |
| `blind_sector_auxiliaries` | boolean precomputed blind-sector membership for threat-channel-time triples | object | key = threat|fire_channel|time_slot -> boolean | true/false | public exclusion trace |
| `fixed_previous_engagements` | engagements already committed before a dynamic update | array[object] | list of fixed engagement records | valid identifiers and times | fixed-decision input |
| `available_fire_channels` | fire channels available under resource stress | array[string] | unique list | subset of fire_channels | resource availability input |
| `radar_capacity` | maximum concurrent support capacity per radar | object | radar -> nonnegative integer | integer >= 0 | radar capacity input |
| `fire_channel_ship` | ship carrying each fire channel | object | fire_channel -> ship | ship identifier | platform mapping input |
| `fire_channel_weapon_system` | weapon system associated with each fire channel | object | fire_channel -> weapon_system | weapon_system identifier | round/setup mapping input |
| `fire_channel_radar` | primary radar associated with each fire channel | object | fire_channel -> radar | radar identifier | illumination mapping input |
| `radar_illumination_alternatives` | precomputed feasible radar illumination alternatives | object | key = threat|fire_channel|time_slot -> list[radar] | radar identifiers | public illumination feasibility input |
| `dynamic_update_event` | source-supported battlefield update event for stress sample | object | event record | valid event metadata | dynamic update input |
| `weapon_or_radar_breakdown_event` | resource degradation event for dynamic stress | object | event record | valid resource metadata | dynamic resource input |
