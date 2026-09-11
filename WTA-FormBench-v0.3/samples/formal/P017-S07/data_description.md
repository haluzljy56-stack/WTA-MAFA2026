# Data Description for P017-S07

The public instance fields are listed below with their meanings and domains.
- `weapons`: defensive weapon identifiers; structure: unique list; domain: unique identifiers.
- `current_missile_storage_list`: missiles currently selectable at sampling time; structure: list or time -> list; domain: missile identifiers.
- `missile_distance_to_asset`: distance from missile to protected asset; structure: missile -> positive number, optionally time-indexed; domain: number > 0.
- `missile_damage_intensity`: damage intensity of each missile; structure: missile -> nonnegative number, optionally time-indexed; domain: number >= 0.
- `weapon_missile_destroy_probability`: destroy probability by weapon and missile; structure: weapon -> missile -> probability, optionally time-indexed; domain: 0 <= p <= 1.
- `missile_availability_mask`: whether a missile is selectable; structure: missile -> 0/1, optionally time-indexed; domain: 0 or 1.
- `sampling_interval`: fixed sampling interval and optional time keys; structure: seconds or metadata; domain: positive.
- `switching_penalty_if_reward_style_sample`: optional target-switching penalty; structure: scalar; domain: nonpositive.
- `previous_weapon_action_if_switching_penalty_active`: previous weapon selections for switching penalty; structure: weapon -> missile or 0; domain: valid prior action.
