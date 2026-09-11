# SWTA MOP1-5 Public Problem Description

## Scope

This document states the public modeling task shared by the SWTA MOP1-5 benchmark suite. It is a natural-language task specification, not a reference formulation. It intentionally omits equations, decision-variable encodings, author algorithms, solver implementations, reference solutions, and evaluator outputs.

## Operational Setting

An air-defense system must coordinate a finite set of sensors and weapon vehicles against multiple incoming targets. Targets follow predictable trajectories over a finite engagement horizon. Sensors provide target detection and tracking, while weapon vehicles conduct interceptions. The benchmark considers both centralized attacks against one protected location and decentralized attacks against multiple protected locations.

The public benchmark assumptions are:

- the engagement takes place in a two-dimensional plane;
- targets and interceptor flights use uniform linear-motion assumptions within the planning horizon;
- sensor and weapon-vehicle locations remain fixed during an engagement;
- resource availability, trajectories, coverage, timing, and effectiveness data are supplied by each instance;
- a target may be left unengaged when no admissible or selected interception is available.

## Required Interception Plan

For every target, construct either no engagement or one internally consistent engagement that identifies a sensor, a weapon vehicle, and a weapon launch time. The launch time is the plan decision; the resulting hit time is a distinct, derived event. A selected engagement must use a sensor-weapon-target combination that remains operationally compatible from the required tracking interval through the resulting hit time.

## Launch-to-Hit Timing Semantics

The following timing semantics apply to all five MOP variants:

- an interceptor starts at its selected weapon vehicle's fixed position at the selected launch time;
- from the launch time onward, its cumulative travel capability advances according to that vehicle's public weapon-speed value and the instance's discrete time steps;
- the resulting hit time is the earliest future target-trajectory step at which the interceptor's cumulative travel capability can reach the target position stored for that step;
- if no such future step exists before the target's valid trajectory ends, the selected engagement is not kinematically reachable;
- the target flight-window check, pre-hit sensor tracking interval, sensor-channel occupancy, detection effectiveness, and interception effectiveness are evaluated using the resulting hit time where applicable;
- weapon inventory usage and minimum separation between repeated firings are attached to launch events, not silently shifted to the later hit events.

These statements define public operational semantics only. They do not prescribe decision-variable encodings, equations, linearizations, or a solver implementation.

## Geometry and Effectiveness Data Semantics

Kinematic reachability and interception effectiveness are related but distinct public concepts:

- the stored target trajectory is the authoritative target position at each discrete step; start/end coordinates may summarize a trajectory but must not replace the supplied stepwise trace;
- weapon position, weapon speed, launch time, the future target trace, and elapsed discrete steps determine whether and when an interceptor can physically reach a target;
- the supplied detection-probability and interception-probability arrays are authoritative effectiveness coefficients for the MOP variant that generated them;
- in spatially dependent variants, those probability arrays already encode the corresponding author-defined spatial effectiveness calculation at each stored target-trajectory step;
- the effectiveness coefficients are sampled at the applicable tracking or resulting-hit steps and retained when evaluating expected remaining target value;
- a zero effectiveness coefficient means that the selected resource provides no expected effect at that step. It does not replace, prove, or disprove the separate launch-to-hit travel calculation;
- therefore a formulation must neither use a positive probability as a substitute for interceptor travel-time feasibility nor discard the probability arrays from an objective that explicitly requires detection/interception effectiveness.

These distinctions expose public input semantics, not a reference equation or decision-variable encoding.

## Objective Requirements

The benchmark defines four conflicting performance criteria. Preserve them as separate raw objectives unless an experiment explicitly declares a subset or a documented scalarization.

1. **Expected remaining target value - minimize.** Prefer plans that reduce the value expected to remain after accounting for target importance and the supplied sensor-detection and weapon-interception effectiveness coefficients at the applicable resulting-hit step.
2. **Resource usage cost - minimize.** Minimize the total operating cost of the sensors and weapon vehicles assigned to engagements. An unengaged target contributes no resource usage cost.
3. **Launch makespan - minimize.** Complete the planned launch scheme as early as possible by minimizing the latest selected weapon launch time. This objective does not redefine launch time as hit time; every derived hit must still remain inside its target's flight window.
4. **Operational concentration risk - minimize.** Avoid relying too heavily on any single sensor or weapon vehicle. Balance engagements across available resources so that the loss or overload of one resource does not compromise many targets.

These objectives are not interchangeable: a high-effectiveness plan may cost more, a low-cost plan may be slower, and concentrating assignments on the strongest resources may increase operational risk.

## Feasibility Requirements

A valid plan must satisfy all applicable requirements simultaneously:

- **Assignment consistency:** each target is either unengaged or assigned one complete sensor-weapon-time engagement; partial or conflicting assignments are invalid.
- **Target flight window:** the resulting hit, rather than only the earlier launch decision, must occur while the target is still within its valid trajectory and allowed flight horizon.
- **Sensor detectability and tracking:** the selected sensor must be able to detect the target at the relevant times and must sustain the required tracking period immediately before the resulting hit.
- **Sensor channel capacity:** at every relevant time, the sum of channel demand from concurrently tracked targets must not exceed that sensor's available channels.
- **Weapon reachability:** after launch, the selected weapon vehicle's interceptor must be able to reach a future target-trajectory position using its public speed and the elapsed discrete travel steps; the earliest reachable future step determines the resulting hit time.
- **Weapon inventory:** the number of engagements assigned to a weapon vehicle must not exceed its carried weapon capacity.
- **Weapon firing interval:** consecutive uses of the same weapon vehicle must respect its minimum firing-time separation.
- **Joint compatibility:** the target, sensor, weapon vehicle, launch time, derived hit time, and their corresponding effectiveness coefficients must refer to one internally consistent engagement. Effectiveness and kinematic reachability remain separate checks and measurements.

## MOP1-5 Variant Semantics

The five variants share the preceding objectives and feasibility framework but progressively change spatial and probability semantics:

- **MOP1:** baseline co-located defense resources and simplified full-coverage/unit-effectiveness assumptions.
- **MOP2:** introduces spatially distributed target scenarios while retaining the simplified detection and interception effectiveness assumptions.
- **MOP3:** introduces spatially dependent sensor detection effectiveness; weapon interception effectiveness remains simplified.
- **MOP4:** introduces spatially dependent weapon interception effectiveness, supplied by the interception-probability array evaluated along the target trace; sensor detection effectiveness remains simplified.
- **MOP5:** combines spatially dependent sensor detection and weapon interception effectiveness, supplied by their respective probability arrays along the target trace, producing the most strongly coupled variant.

Instance scale, attack type, resource sufficiency, and the number of active objectives may vary independently of the MOP identifier.

## Public Data Semantics

An instance can provide target counts and trajectories, sensor and weapon-vehicle counts and locations, time discretization and engagement horizon, target values, resource costs, sensor channel capacities and per-target channel demand, weapon inventories, weapon speeds and firing intervals, detection/interception coverage, and effectiveness data. Instance data determines numerical values; this document supplies only the shared business semantics.

## Source Provenance

This description was distilled from the public problem-description, objective, constraint, and benchmark-suite sections of the supplied SWTA main paper and supplementary material. The PDFs remain the authoritative scientific sources.