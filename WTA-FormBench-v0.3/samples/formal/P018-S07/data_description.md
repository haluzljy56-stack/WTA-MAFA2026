# Data Description for P018-S07

The public instance fields are listed below with their meanings and domains.
- `targets`: target identifiers; structure: unique list; domain: unique identifiers.
- `launchers`: launcher identifiers; structure: unique list; domain: unique identifiers.
- `time_slots`: discrete firing slots; structure: ordered unique list; domain: slot identifiers.
- `launcher_positions`: launcher coordinate positions; structure: launcher -> coordinate vector; domain: 2D coordinates.
- `target_pip_positions_by_launcher_time`: predicted intercept point by target, launcher and slot; structure: target -> launcher -> slot -> coordinate; domain: 2D coordinates.
- `launcher_orientation`: launcher orientation vectors; structure: launcher -> vector; domain: 2D vectors.
- `heading_vectors`: heading vectors toward predicted intercept points; structure: target -> launcher -> slot -> vector; domain: 2D vectors.
- `distance_pk_parameters`: distance-effect PK parameters; structure: parameter -> number; domain: positive parameters.
- `heading_error_pk_parameters`: heading-error PK parameters; structure: parameter -> number; domain: angle parameters.
- `engagement_distance_bounds`: minimum and maximum engagement distances; structure: r_min/r_max; domain: positive bounds.
- `target_max_interceptors`: target-level interceptor upper bound; structure: target -> integer; domain: positive integer.
- `launcher_interceptor_capacity`: launcher interceptor capacity; structure: launcher -> integer; domain: nonnegative integer.
- `firing_delay`: minimum delay between successive firings; structure: scalar; domain: nonnegative integer.
- `feasible_firing_slots`: allowed firing slots for each target-launcher pair; structure: target -> launcher -> slots; domain: subset of time_slots.
- `strategy_type`: RF or R strategy flag; structure: scalar; domain: RF or R.
