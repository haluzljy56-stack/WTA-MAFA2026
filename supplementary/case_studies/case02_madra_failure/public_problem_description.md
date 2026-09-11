# MADRA-LIB Public Problem Description

## Scope And Claim Boundary

This document states the public modeling task used by the MADRA-LIB P1-P10
Paper-Spec Open Reconstruction v1. It is a natural-language specification, not
a reference formulation. It intentionally omits equations, decision-variable
encodings, author algorithms, solver implementations, reference solutions, and
evaluator outputs. The reconstructed P1-P10 numerical instances follow the
published scale and physical rules but are not the authors' unreleased exact
P1-P10 files.

## Operational Setting

An air-defense system must coordinate fixed guidance radars and paired
missile-launcher resources against incoming aerial targets over a finite,
discrete-time horizon. Every target follows a known straight-line trajectory
toward the defended region. Target type determines speed and importance.
Radar type determines coverage, field of view, tracking-channel demand, and
guidance accuracy. Launcher type determines inventory, interceptor speed,
engagement geometry, and target-dependent interception effectiveness.

The numerical instance supplies every target trajectory input, all radar and
launcher locations and headings, resource capacities, the time step, and the
physical effectiveness tables. Factorized radar and launcher hit-time
intervals are supplied as public derived geometry data. They identify when an
individual radar can continuously support a target and when an individual
launcher can reach it; a compatible radar-launcher hit opportunity exists only
where the corresponding intervals overlap.

## Required Interception Plan

For each target and each attempt allowed by the selected case protocol, choose
either no engagement or one complete engagement. A complete engagement names
the target, attempt number, launcher, guidance radar, and intended hit step.
An unused attempt consumes no launcher inventory or radar channel capacity.

The `single` protocol permits at most one attempt per target. The `multi3`
protocol permits up to three ordered attempts per target. Used attempt numbers
must be contiguous from the first attempt; a later attempt cannot be used when
an earlier attempt for that target is unused.

## Primary Objective And Reported Metrics

The primary objective is to maximize aggregate interception effectiveness.
For each target, combine the success probabilities of all valid attempts as
independent opportunities and measure the resulting cumulative probability of
intercepting that target. Aggregate effectiveness is the sum of these target
probabilities over the scenario.

The number and rate of targets receiving positive interception probability may
be reported for interpretation. Interception rates broken down by target type
are auxiliary metrics only. They do not replace or alter the primary
aggregate-effectiveness objective.

## Feasibility Requirements

A valid plan must satisfy all applicable requirements simultaneously:

- **Complete assignment:** every used attempt names exactly one known target,
  one known launcher, one known radar, and one valid hit step. Partial and
  duplicate target-attempt records are invalid.
- **Attempt limit and order:** a target uses no more attempts than allowed by
  its case protocol, and used attempt indices are consecutive from the first.
- **Target horizon:** each hit occurs after the required tracking lead time and
  before the target reaches the end of its public trajectory horizon.
- **Launcher reachability:** the launcher can fire early enough for its
  interceptor to arrive at the declared hit step, the target lies in the
  launcher's engagement sector, and the applicable target-dependent kill zone
  has positive effectiveness.
- **Continuous radar support:** the selected radar sees the target at every
  discrete step in the required pre-hit tracking interval, including the hit
  step. Instantaneous visibility at only the final step is insufficient.
- **Positive joint effectiveness:** radar guidance and launcher geometry must
  jointly yield a positive interception probability at the declared hit step.
- **Launcher inventory:** the total number of used attempts assigned to a
  launcher cannot exceed that launcher's missile inventory.
- **Radar channel capacity:** at every time step, the sum of target-type
  tracking-channel demand for all attempts concurrently guided by a radar
  cannot exceed that radar's channel capacity.
- **Repeated-attempt spacing:** consecutive used attempts against the same
  target must respect the protocol's lower and upper hit-time separation.
- **Radar continuity for close attempts:** when consecutive hit times are
  closer than the declared continuity threshold, both attempts must use the
  same guidance radar.

## Public Data Semantics

Entity CSV files contain target, radar, and launcher facts. Interval CSV files
contain inclusive one-based hit-step ranges and remain factorized by resource;
they are public physical facts, not a prebuilt optimization model. The case
files select `single` or `multi3` and state the applicable attempt and timing
rules. The instance JSON supplies physical tables and time conventions. A
modeling system must construct its own mathematical formulation from these
public semantics and data.

## Source Provenance

This description was distilled from the supplied MADRA publications, released
code and data semantics, and the documented open-reconstruction protocol. The
papers remain the authoritative scientific sources. Numerical reconstruction
choices and their evidence status are documented separately in
`MADRA_P1_P10_REPRODUCTION_RULES.md` and `EVIDENCE_ASSUMPTION_MATRIX.md`.