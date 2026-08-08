"""Data cleaning and harmonization utilities.

This module contains helpers for loading raw source files, applying survey
weighting rules, standardizing state names, and producing an interim analysis
panel before index creation.
"""

from __future__ import annotations

import pandas as pd


def load_raw_data(file_path: str) -> pd.DataFrame:
    """Read a CSV/Excel-style raw source file into a DataFrame."""
    return pd.read_csv(file_path)


def normalize_state_names(df: pd.DataFrame, state_col: str = "state") -> pd.DataFrame:
    """Normalize state labels for Nigerian state-level joins."""
    df = df.copy()
    df[state_col] = df[state_col].astype(str).str.strip().str.title()
    return df


def weighted_aggregation(df: pd.DataFrame, value_col: str, weight_col: str = "weight") -> float:
    """Return a weighted mean for a survey layer."""
    if weight_col not in df.columns:
        return float(df[value_col].mean())
    return float((df[value_col] * df[weight_col]).sum() / df[weight_col].sum())
