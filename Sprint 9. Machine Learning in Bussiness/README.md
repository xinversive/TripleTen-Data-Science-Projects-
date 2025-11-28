# Machine Learning in Business — OilyGiant Project

## Project Overview

This project uses machine learning to identify the best region for new oil well development. The goal is to maximize profit while minimizing risk by analyzing three potential regions using linear regression and bootstrap risk analysis.

**Goal:** Find the best region for a new oil well development using linear regression and risk analysis with bootstrapping.

## Project Structure

```
.
├── README.md                              # This file
├── Machine Learning in Business.ipynb     # Main project notebook
├── oilygiant_project x.ipynb              # Alternative/backup notebook
├── geo_data_0.csv                         # Dataset for Region 0
├── geo_data_1.csv                         # Dataset for Region 1
├── geo_data_2.csv                         # Dataset for Region 2
└── oilygiant_outputs/                     # Output directory
    ├── region_0_valid_preds.csv          # Validation predictions for Region 0
    ├── region_1_valid_preds.csv          # Validation predictions for Region 1
    └── region_2_valid_preds.csv          # Validation predictions for Region 2
```

## Data Sources

The datasets are available from:
- Region 0: `https://practicum-content.s3.us-west-1.amazonaws.com/datasets/geo_data_0.csv`
- Region 1: `https://practicum-content.s3.us-west-1.amazonaws.com/datasets/geo_data_1.csv`
- Region 2: `https://practicum-content.s3.us-west-1.amazonaws.com/datasets/geo_data_2.csv`

### Dataset Structure

Each dataset contains:
- `id` — well identifier
- `f0, f1, f2` — geological features
- `product` — target variable (thousand barrels of oil)

Each region dataset contains 100,000 exploration points.

## Business Parameters

- **Budget:** $100,000,000 USD
- **Wells to develop:** 200 (top 200 wells by predicted reserves)
- **Revenue per unit:** $4,500 per thousand barrels
- **Cost per well:** $500,000 (implied from budget)
- **Break-even average product:** 111.11 thousand barrels per well
- **Points per region:** 500 (for bootstrap sampling)
- **Bootstrap samples:** 1,000

## Methodology

### 1. Data Preparation
- Load three regional datasets (with automatic download if files are missing)
- Verify data structure and basic statistics

### 2. Model Training
- Split data: 75% training, 25% validation
- Train Linear Regression models for each region
- Evaluate using RMSE (Root Mean Squared Error)
- Calculate average predicted reserves

### 3. Profit Calculation
- Select top 200 wells based on predicted reserves
- Calculate total product (thousand barrels) from selected wells
- Compute profit: `(total_product × revenue_per_unit) - budget`

### 4. Risk Analysis (Bootstrap)
- Perform 1,000 bootstrap samples of 500 points per region
- For each sample:
  - Predict reserves using trained model
  - Select top 200 wells
  - Calculate profit
- Compute statistics:
  - Average profit
  - 95% confidence interval
  - Loss risk (percentage of samples with negative profit)

### 5. Visualization
- Profit distribution histograms for each region
- Combined comparison plots
- Risk-return scatter plots

## Results

### Model Performance (RMSE)

| Region | RMSE | Avg Predicted Reserves |
|--------|------|----------------------|
| Region 0 | 37.757 | 92.399 |
| Region 1 | 0.890 | 68.713 |
| Region 2 | 40.146 | 94.771 |

### Bootstrap Analysis Results

| Region | Avg Profit | 95% CI | Loss Risk |
|--------|-----------|--------|-----------|
| Region 0 | $4,294,219 | [-$627,398, $9,213,546] | 4.20% |
| **Region 1** | **$4,446,808** | **[$282,909, $8,395,043]** | **1.70%** |
| Region 2 | $3,783,845 | [-$1,857,058, $8,910,235] | 8.50% |

## Final Recommendation

**Recommended Region: Region 1**

### Justification:
1. **Highest Average Profit:** $4,446,808 (highest among all regions)
2. **Lowest Loss Risk:** 1.70% (well below the 2.5% threshold)
3. **Positive Confidence Interval:** The 95% CI lower bound is positive ($282,909), indicating high confidence in profitability
4. **Best Risk-Return Profile:** Optimal balance between profit potential and risk

### Decision Criteria:
- Loss risk must be < 2.5%
- Among eligible regions, select the one with highest average profit

Region 1 is the only region that meets both criteria, making it the optimal choice for oil well development.

## Technologies Used

- **Python 3**
- **NumPy** — Numerical computations
- **Pandas** — Data manipulation
- **Scikit-learn** — Machine learning (Linear Regression, train_test_split, metrics)
- **Matplotlib** — Data visualization
- **Seaborn** — Enhanced visualizations

## Key Functions

- `load_region(path)` — Loads and validates regional datasets
- `train_validate_region(df)` — Trains linear regression model and returns validation results
- `calculate_profit(y_true, y_pred)` — Calculates profit from top 200 wells
- `bootstrap_region_profit(df, model)` — Performs bootstrap analysis for risk assessment

## Running the Project

1. Ensure all required packages are installed:
   ```bash
   pip install numpy pandas scikit-learn matplotlib seaborn
   ```

2. Open the Jupyter notebook:
   ```bash
   jupyter notebook "Machine Learning in Business.ipynb"
   ```

3. Run all cells sequentially. The notebook will:
   - Automatically download datasets if they're missing
   - Train models for all three regions
   - Perform bootstrap analysis
   - Generate visualizations
   - Save validation predictions to `oilygiant_outputs/`

## Notes

- The project uses a random state of 42 for reproducibility
- All monetary values are in USD
- Product is measured in thousand barrels
- The break-even point is 111.11 thousand barrels per well on average

## Author

TripleTen Machine Learning Project

## Date

2025-10-16

