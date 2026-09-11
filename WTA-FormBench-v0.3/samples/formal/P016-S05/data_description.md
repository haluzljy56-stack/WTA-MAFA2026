# Data Description for P016-S05

The public instance fields are listed below with their meanings and domains.
- `weapons`: weapon identifiers; structure: unique list; domain: unique identifiers.
- `targets`: target identifiers; structure: unique list; domain: unique identifiers.
- `target_value`: value of each target; structure: target -> nonnegative number; domain: number >= 0.
- `weapon_target_completion_probability`: destroy/completion probability for each weapon-target pair; structure: weapon -> target -> probability; domain: 0 <= p <= 1.
- `model_variant`: declared formulation scope; structure: variant label; domain: discrete/relaxation label.
- `relaxation_requested`: whether continuous relaxation is requested; structure: scalar; domain: true/false.
- `regularization_parameters_if_saddle_form_requested`: optional solver-side regularization constants; structure: parameter -> positive number; domain: number > 0.
