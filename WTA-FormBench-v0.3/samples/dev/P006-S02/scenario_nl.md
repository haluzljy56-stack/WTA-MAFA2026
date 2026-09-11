# Scenario

Build a soft-kill weapon-target assignment model for one defensive stage, with a dynamic wrapper for repeated stages. Weapons are grouped into six defensive types. Assignment probabilities depend on distance. Non-jammer weapons can be used against at most one missile at a time; each missile should receive at least one eligible defense. Respect range, jammer coverage, guidance compatibility and over-assignment control, then repeat after updating missile positions and surviving missiles.

Scale: P006-S02 uses the dev split and disclosure level L2. The accompanying JSON file provides all public instance data needed for this sample.
