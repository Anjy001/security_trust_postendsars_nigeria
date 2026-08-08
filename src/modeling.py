"""Econometric modeling and diagnostics.

The workflow produces reproducible OLS output and summary tables.
"""

from __future__ import annotations

import pandas as pd
import statsmodels.api as sm


def run_ols_model(data: pd.DataFrame, dependent: str, regressors: list[str]) -> object:
    """Fit a standard OLS regression model with statsmodels."""
    X = data[regressors].copy()
    X = sm.add_constant(X)
    y = data[dependent]
    model = sm.OLS(y, X)
    return model.fit()


def export_summary(model_fit: object, output_path: str) -> None:
    """Write regression summary to a text file."""
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(model_fit.summary().as_text())
