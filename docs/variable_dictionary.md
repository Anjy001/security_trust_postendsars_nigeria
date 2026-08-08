# Variable Dictionary

This document describes the variables used in the analysis-ready CSTI workflow for this GitHub repository.

## Core panel structure

The final analytic dataset is expected at `data/processed/csti_master_dataset.csv` and should be a state-year panel covering Nigerian states.

## Modeling variables

The repository is designed to support a focused regression analysis using the following variable groups:

- `state`: Nigerian state identifier
- `year`: observation year
- `trust_police`: perceived police trust and confidence
- `security_satisfaction`: citizen security satisfaction measure
- `state_accountability`: accountability or responsiveness indicator
- `conflict_events`: ACLED-derived conflict count
- `fatalities`: conflict-related fatalities
- `budget_transparency`: fiscal accountability or budget transparency indicator
- `service_delivery_index`: service delivery and governance signal
- `csti_index`: normalized Community Security and Trust Index

## Analysis contract

The notebook and source modules should produce stable, reproducible outputs from the final panel without introducing new model-specific columns unless they are reflected in this dictionary.
