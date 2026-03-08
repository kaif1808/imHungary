# Development Status

## Hungary Growth Accounting LaTeX Conversion

**Status**: Implemented (2025-03-08)

### Completed
- **Imputation section rewrite (2025-03-08)**: Replaced NNM+LASSO ensemble with XGBoost backcasting; per-sector LOO RMSE (H, O-Q, L most reliable; J, F, M-N highest uncertainty); hyperparameter table in appendix
- `convert_md_to_latex.py` created to convert `Hungary_Growth_Accounting.md` to LaTeX
- Extracts 12 embedded base64 PNG figures to `output/figures/hungary_ga_fig01.png` … `fig12.png`
- Produces `Hungary_Growth_Accounting.tex` (standalone, compilable with pdflatex)
- Converts markdown tables to LaTeX tabular (booktabs)
- Handles Unicode math (α, gᵧ, ≈, etc.), inline formatting (*italic*, **bold**), and special chars
- PDF compiles successfully (21 pages)
- **Figure path fix (2025-03-08)**: Added `\graphicspath{{../}}` so figures resolve when compiling from `Latex/`; replaced Figs 3–9, 11–12 with contextually matched notebook figures (labqi_imputed_vs_observed_full, lp_decomposition_aggregate_3f_and_2f, sectoral_lp_decomposition_3f_and_2f, implied_capital_share_by_sector, tfp_alpha_comparison_3f_and_2f, growth_accounting_3f_and_2f_line)
- **Figure 12 replacement (2025-03-08)**: Replaced aggregate line chart with Finance sector (K) 3-factor decomposition time-series chart; new cell in backcast_labqi.ipynb; `scripts/generate_finance_figure.R` for standalone regeneration; figure saved to `output/figures/finance_sector_K_3f_decomposition.png`
- **Figure markers (2025-03-08)**: lp_decomposition_aggregate_3f_and_2f: red shaded pre-2008 imputed region + solid darkred imputation line (3-factor panel only); growth_accounting_3f_and_2f_line and finance_sector_K_3f_decomposition: three event lines (EU Accession 2004, GFC 2008, Orban gov 2010) with labels; `scripts/generate_growth_figures.R` for standalone regeneration of growth_accounting and lp_decomposition figures
- **LaTeX table replacement (2025-03-08)**: Replaced 6 inline tabular environments with `\input{../output/tables/<file>.tex}`: year_tally_2f, year_tally_3f, sectoral_tally_2f, sectoral_tally_3f, lab_share_alpha, tfp_compare. Table 7 (aggregation match) left inline (no output file).
- **Industry names and print-ready labels (2025-03-08)**: Tables now use full sector names (e.g. "B – Mining & quarrying") and human-readable column headers. Added `sector_display_names` in backcast_labqi.ipynb; notebook exports year_tally_2f/3f, sectoral_tally_2f/3f directly. Removed NACE/column footnotes from LaTeX. `scripts/apply_table_labels.py` applies labels to raw tables; `scripts/generate_table_subsets.py` deprecated for subset generation (notebook exports directly)
- **Table centre justification and 2f/3f value corrections (2025-03-08)**: All tables wrapped in `\begin{center}...\end{center}` for proper centring. Narrative text updated to match corrected values from sectoral_tally_2f, sectoral_tally_3f, and tfp_compare: J sector (TFP 6.64 pp, HC -0.96 pp), C (HC 0.47 pp), K (TFP -5.34 pp, HC 0.94 pp), top TFP (B 5.96, A 3.83, C 2.08 pp), agriculture/real estate sector-specific α values from tfp_compare

## LAB_QI XGBoost Backcasting Notebook

**Status**: Implemented (2025-03-08)

### Completed
- `backcast_labqi.ipynb` created:
  - XGBoost backcasting using only predictors with >=80% pre-2008 coverage
  - No median imputation (XGBoost handles NA natively)
  - Industry-specific LAB_QI for pre-2008 (broad sectors only)
  - Predictor normalisation (z-score); prediction clipping to observed range
  - **Hyperparameter tuning (Section 3b)**: Random search over max_depth (2–8), eta, subsample, colsample_bytree, min_child_weight; 5-fold CV with early stopping; top 5 combos printed
  - 5-fold CV RMSE on observed (2008+) data (uses tuned params)
  - Growth accounting (c): decomposition capital / HC / TFP, evolution over time; fixed cap_contrib formula (α/(1−α)); measurement discussion (capital, HC, labour); period 1995–2011; aggregate stacked bar chart
  - Growth accounting (d): sectoral decomposition by broad sector; highest/lowest LP growth and TFP; sectoral stacked bar chart
  - Growth accounting (e): labour share by sector, sector-specific α, TFP comparison α=1/3 vs sector-α; labour share bar chart; TFP comparison bar chart; fixed round() on tibbles
  - **Tally tables and 2-factor decomposition**: aggregate tally table (3-factor and 2-factor); year-by-year tally; sectoral tally with 2-factor; sectoral 2-factor vs 3-factor comparison; 2-factor with sector-specific α in tfp_compare; line plot comparing TFP vs 2-factor residual by year
  - **Per-sector LOO RMSE (Section 5c)**: Leave-one-sector-out CV for per-sector RMSE; exports `sector_rmse_xgb.tex`
  - **LaTeX exports**: all 8 tables exported to `output/tables/` (aggregate_tally, year_tally, sectoral_tally, sectoral_2f_vs_3f, lab_share_alpha, tfp_compare, hyperparameter_top5, sector_rmse_xgb)
  - **Graph exports**: all figures saved to `output/figures/` with descriptive filenames; decomposition graphs include 2-factor vs 3-factor comparison (growth_accounting_3f_and_2f_line, tfp_vs_2f_residual_by_year, lp_decomposition_aggregate_3f_and_2f, sectoral_lp_decomposition_3f_and_2f, implied_capital_share_by_sector, tfp_alpha_comparison_3f_and_2f, labqi_*); Finance sector (K) 3-factor decomposition (finance_sector_K_3f_decomposition.png)
  - Four LAB_QI graphs: levels by sector, transition zoom (2005–2012), g_LABQI distribution, aggregate mean
  - Exports `Data/panel_with_labqi_backcast.csv`

## Backcasting Quality Test Notebook

**Status**: Implemented (2025-03-08)

### Completed
- `backcasting_quality_test.ipynb` created with full implementation:
  - Setup & load `Data/final_panel.csv`
  - Data prep: map columns, compute growth rates (g_LABQI, g_LAB, g_CAP_QI, etc.)
  - NNM backcasting (softImpute) with augmented matrix (LAB_QI + LP1ConLC, LAB, CAP_QI, LP1_G, VAadj_G)
  - LASSO backcasting (glmnet) with sector dummies + LP1ConLC + year trend
  - Ensemble (average of NNM and LASSO levels)
  - LOO-CV for lambda selection and quality metrics
  - Five quality graphs: time series, transition at 2008, distribution, predicted vs actual, sector RMSE

### Data
- Uses 14 broad sectors (A, B, C, D-E, F, G, H, I, J, K, L, M-N, O-Q, R-S)
- LAB_QI observed 2008–2021; imputed 1995–2007
- Covariates: LP1ConLC, LAB, CAP_QI, LP1_G, VAadj_G
