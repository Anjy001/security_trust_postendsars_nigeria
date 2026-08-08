# Methodology Note

This repository implements an analysis-based research workflow that constructs a Community Security and Trust Index (CSTI) for Nigerian states following the EndSARS period.

## Data Sources

The analysis combines three main inputs:

- Afrobarometer Round 9 Nigeria survey data
- ACLED Nigeria conflict event data
- BudgIT state fiscal and service delivery indicators

## Index Construction

The CSTI is constructed as a state-year panel and normalized according to the variable dictionary used in the modeling workflow.

## Modeling

The final source code supports OLS-style analysis with state-level covariates. Results are written to reproducible outputs in the results folder.

## GitHub deployment orientation

This project is structured as a data and analysis repository. It is designed to be versioned on GitHub, documented for reproducibility, and executed locally through Python notebooks and scripts.
