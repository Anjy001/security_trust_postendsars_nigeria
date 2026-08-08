"""Reusable plotting utilities for the research workflow."""

from __future__ import annotations

import matplotlib.pyplot as plt
import seaborn as sns


def style_plots() -> None:
    """Apply a consistent visual style for project charts."""
    sns.set_theme(style="whitegrid")


def plot_csti_distribution(data, column: str = "csti_index") -> None:
    """Generate a histogram of the CSTI distribution."""
    style_plots()
    plt.figure(figsize=(8, 5))
    sns.histplot(data[column], kde=True)
    plt.title("Distribution of CSTI")
    plt.xlabel("CSTI")
    plt.ylabel("Frequency")
    plt.tight_layout()
