"""CSTI index-construction logic.

This module implements min-max normalization, weighting, and index assembly
for source-specific state-level indicators.
"""

from __future__ import annotations

import pandas as pd


def minmax_normalize(series: pd.Series) -> pd.Series:
    """Scale a numeric series to a 0-1 range."""
    min_value = series.min()
    max_value = series.max()
    if pd.isna(min_value) or pd.isna(max_value) or max_value == min_value:
        return series.astype(float)
    return (series - min_value) / (max_value - min_value)


def construct_csti_index(df: pd.DataFrame) -> pd.DataFrame:
    """Construct a composite state-level index from indicators."""
    result = df.copy()
    for column in ["trust_police", "security_satisfaction", "accountability", "service_delivery"]:
        if column in result.columns:
            result[f"{column}_norm"] = minmax_normalize(result[column])

    if all(column in result.columns for column in ["trust_police_norm", "security_satisfaction_norm", "accountability_norm", "service_delivery_norm"]):
        result["csti_index"] = (
            result["trust_police_norm"] * 0.25
            + result["security_satisfaction_norm"] * 0.25
            + result["accountability_norm"] * 0.25
            + result["service_delivery_norm"] * 0.25
        )

    return result
