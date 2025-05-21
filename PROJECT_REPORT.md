# Solar Data Discovery Challenge – Project Report

## Introduction

This project addresses the Solar Data Discovery Challenge, focusing on the analysis of solar farm data from Benin, Sierra Leone, and Togo. The main objective is to profile, clean, and explore environmental and solar irradiance data to identify trends, outliers, and actionable insights for MoonLight Energy Solutions. The project is structured in three main tasks: environment setup, country-level EDA and cleaning, and cross-country comparison, with an optional Streamlit dashboard for visualization.

---

## Methodology

### Environment Setup
- Initialized a GitHub repository and set up a Python virtual environment.
- Created a standardized folder structure and added a `.gitignore` to exclude data and environment files.
- Established CI/CD using GitHub Actions to ensure reproducibility and code quality.

### Data Profiling, Cleaning & EDA
- For each country (Benin, Sierra Leone, Togo), a dedicated Jupyter notebook was created in the `notebooks/` folder.
- Data was loaded and profiled using summary statistics and missing value analysis.
- Outliers were detected using Z-scores (|Z| > 3) for key columns (GHI, DNI, DHI, ModA, ModB, WS, WSgust).
- Missing values in key columns were imputed using the median; outliers were removed for cleaner analysis.
- Cleaned datasets were exported (not committed to git) for further analysis.
- Exploratory Data Analysis included:
  - Time series plots for solar metrics (GHI, DNI, DHI, Tamb)
  - Analysis of cleaning events on sensor performance
  - Correlation heatmaps and scatter plots
  - Wind and distribution analysis (histograms, wind rose)
  - Temperature and humidity relationships
  - Bubble charts (GHI vs Tamb, bubble=RH)
- Observations and next steps were documented in each notebook.

### Cross-Country Comparison
- Loaded cleaned datasets for all countries in `compare_countries.ipynb`.
- Compared key metrics (GHI, DNI, DHI) using boxplots and summary tables.
- Performed statistical tests (ANOVA/Kruskal–Wallis) to assess significance of differences.
- Synthesized findings and visualized results in a dedicated notebook.

### Streamlit Dashboard (Bonus)
- Developed an interactive dashboard (`app/main.py`) to visualize and compare solar data across countries.
- The dashboard allows users to select countries, metrics, and view boxplots, summary tables, and time series plots interactively.

---

## Challenges & Solutions
- **Data Quality:** Some datasets had significant missing values and outliers. Solution: Used robust imputation (median) and Z-score filtering.
- **Data Consistency:** Ensured consistent cleaning and EDA workflow across all countries for fair comparison.
- **Version Control:** Managed multiple branches for each major task, ensuring clean merges and reproducibility.
- **CI/CD:** Initial issues with workflow configuration were resolved by updating the GitHub Actions YAML and requirements.
- **Data Accessibility:** Ensured all required data files were available locally for analysis and dashboard use.

---

## Recommendations
- For future work, consider automating the EDA and cleaning process with reusable scripts.
- Integrate more advanced statistical or machine learning models to predict solar potential.
- Expand the dashboard to include more interactive features and region-level drill-downs.
- Collaborate with domain experts to interpret findings and guide actionable business decisions.

---

## Conclusion

Significant progress has been made in setting up the environment, profiling, cleaning, and analyzing the solar datasets for Benin, Sierra Leone, and Togo. The project is complete, with a clear workflow for cross-country comparison and dashboard development. The standardized workflow ensures reproducibility and comparability, and the team is confident in delivering actionable insights and a professional final deliverable.

---

## Appendix: Project Structure

```
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── __init__.py
│   ├── benin_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── compare_countries.ipynb
│   └── README.md
├── data/           # (ignored in git)
│   ├── benin-malanville.csv
│   ├── benin_clean.csv
│   ├── sierraleone-bumbuna.csv
│   ├── sierraleone_clean.csv
│   ├── togo-dapaong_qc.csv
│   └── togo_clean.csv
├── tests/
│   ├── __init__.py
│   └── README.md
├── scripts/
│   ├── __init__.py
│   └── README.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
```

---

## References
- [Python Testing](https://realpython.com/python-testing/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [GitHub Actions](https://docs.github.com/en/actions)
