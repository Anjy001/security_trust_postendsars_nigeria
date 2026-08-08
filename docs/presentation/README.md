<div align="center">

# 🛡️ Security Sector Accountability & Citizen Trust in Post-EndSARS Nigeria
### A Cross-State Econometric Analysis of Reform Implementation and Impunity Reduction

*Does spending money on security actually buy public trust — or does accountability matter more?*

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Statsmodels](https://img.shields.io/badge/Statsmodels-OLS%20Regression-orange?style=flat-square)](https://www.statsmodels.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Research-brightgreen?style=flat-square)]()
[![Award](https://img.shields.io/badge/ASSON--ASA%202026-🥈%202nd%20Place-blueviolet?style=flat-square)]()

</div>

---

## 📌 Table of Contents
- [🛡️ Security Sector Accountability \& Citizen Trust in Post-EndSARS Nigeria](#️-security-sector-accountability--citizen-trust-in-post-endsars-nigeria)
    - [A Cross-State Econometric Analysis of Reform Implementation and Impunity Reduction](#a-cross-state-econometric-analysis-of-reform-implementation-and-impunity-reduction)
  - [📌 Table of Contents](#-table-of-contents)
  - [🧭 Overview](#-overview)
  - [🎯 Context \& Research Objective](#-context--research-objective)
  - [🗂️ Data Sources](#️-data-sources)
  - [🔬 Methodology](#-methodology)
  - [🛠️ Tech Stack](#️-tech-stack)
  - [📊 Key Findings](#-key-findings)
    - [🔑 Headline Insight](#-headline-insight)
  - [⚙️ Installation \& Setup](#️-installation--setup)
    - [Prerequisites](#prerequisites)
    - [1. Clone the repository](#1-clone-the-repository)

---

## 🧭 Overview

The **October 2020 EndSARS protests** exposed a deep accountability crisis within Nigeria's security architecture, prompting the enactment of the **Police Act 2020** and sweeping institutional reform promises. Six years on, a critical empirical question remains unanswered:

> **Have these reforms translated into measurably higher public trust — or does money alone fail to buy legitimacy?**

This project answers that question using a **cross-sectional econometric model** spanning Nigeria's **36 states and the FCT**, integrating citizen survey data, conflict event records, and public finance data into a single, reproducible analytical pipeline built entirely in Python.

---

## 🎯 Context & Research Objective

**Objective:** Determine whether localized state security budgets, security incident exposure, or statutory compliance with the Police Act 2020 is the strongest driver of subnational citizen trust in security institutions.

**Guiding Hypothesis:** Increasing security expenditure *without* corresponding accountability infrastructure will fail to move the needle on public trust — implying that Nigeria's reform bottleneck is one of **implementation**, not **legislation** or **funding**.

This research was developed as part of my work at the **Laboratory for Interdisciplinary Statistical Analysis (LISA), University of Ibadan**, and was awarded **2nd Place at the 2026 ASSON–ASA Students' Workshop** (theme: *"Justice, Accountability, and Security Sector Reform in Nigeria"*), presented in collaboration with the American Statistical Association (ASA).

---

## 🗂️ Data Sources

| Dataset | Source | Role in Study |
|---|---|---|
| **Afrobarometer Round 9 Nigeria Microdata** | [afrobarometer.org](https://www.afrobarometer.org) | Constructs the dependent variable — the **Citizen Security Trust Index (CSTI)** — from individual-level trust and perceived-corruption items (n = 1,647), aggregated to state level using survey design weights |
| **ACLED Nigeria Conflict Event Data (2022–2025)** | [acleddata.com](https://acleddata.com) | Provides geocoded security incident records used to compute **incident density per 100,000 people** by state |
| **BudgIT 2022 State of States Report** | [budgit.org](https://budgit.org) | Source of absolute "Public Order and Safety" fiscal allocations across states |
| **NBS Subnational Population Projections** | [nigerianstat.gov.ng](https://nigerianstat.gov.ng) | Used as the denominator to compute **per-capita security expenditure** |

> ⚠️ **Note on Data Access:** Raw microdata (particularly Afrobarometer respondent-level files) are **not included** in this repository due to licensing restrictions. See [`docs/methodology_note.md`](docs/methodology_note.md) for instructions on requesting access and replicating the raw data pull.

---

## 🔬 Methodology

The analytical pipeline follows five stages:

**1. Weighted Index Construction**
State-level trust scores were built from Afrobarometer microdata using **within-country survey weights** to correct for unequal selection probabilities across rural/urban strata and enumeration clusters — avoiding naive unweighted averaging that would bias state-level estimates.

**2. Feature Engineering**
- `Budget_i` — Per-capita security expenditure (Public Order & Safety allocation ÷ NBS population projection)
- `Incidents_i` — Security incident density per 100,000 people (ACLED, 2022–2025)
- `Compliance_i` — Composite statutory compliance score benchmarked against Police Act 2020 provisions

**3. Model Specification**

The relationship is estimated via **Ordinary Least Squares (OLS)** regression at the state level (N = 37):

$$
\text{CSTI}_i = \beta_0 + \beta_1(\text{Budget})_i + \beta_2(\text{Incidents})_i + \beta_3(\text{Compliance})_i + \varepsilon_i
$$

**4. Diagnostics**
Model fit was assessed via R², F-statistics, and residual diagnostics (heteroskedasticity, multicollinearity via VIF).

**5. Visualization**
Coefficient plots, scatter/trend visualizations, and correlation heatmaps were generated using Seaborn/Matplotlib to communicate findings for both technical and policy audiences.

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python 3.10+ |
| **Data Wrangling** | Pandas, NumPy |
| **Statistical Modeling** | Statsmodels (OLS), SciPy |
| **Visualization** | Matplotlib, Seaborn |
| **Environment** | Jupyter Notebook, VS Code |
| **Version Control** | Git & GitHub |

---

## 📊 Key Findings

| Predictor | Standardized β | Significance |
|---|---|---|
| **Statutory Compliance** (Police Act 2020) | **+0.847** | p < 0.01 ** |
| **Security Incident Density** | −0.312 | p < 0.05 * |
| **Per-Capita Security Budget** | ≈ 0.00 | Not significant |

**Model Fit:** R² = 0.71 | F-statistic significant at p < 0.001

### 🔑 Headline Insight
> **Statutory compliance with the Police Act 2020 is ~17x more predictive of citizen trust than per-capita security spending.**

This suggests that **reform implementation — not budget expansion — is the binding constraint** on rebuilding public trust in Nigeria's security sector post-EndSARS. States with strong, visible statutory compliance show materially higher trust scores *even after* holding violent-incident levels constant, while pouring more naira into security budgets shows no measurable trust dividend absent functional oversight.

**Policy Implication:** Before scaling security budgets — or decentralizing policing via State Police — Nigeria should prioritize enforceable, auditable compliance mechanisms (complaint response units, arrest/detention registers, judicial panels, community policing committees) across all 36 states.

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip or conda
- Git

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/security-trust-postendsars-nigeria.git
cd security-trust-postendsars-nigeria