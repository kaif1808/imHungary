# Development Status

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
