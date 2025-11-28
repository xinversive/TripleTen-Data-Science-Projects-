# Gold Recovery Prediction Project

A machine learning project to predict gold recovery rates at different stages of the gold extraction process. This project was developed as part of the TripleTen Integrated Project 2.

## Project Overview

This project focuses on building predictive models to estimate gold recovery rates at two critical stages:
- **Rougher stage recovery**: Initial concentration stage
- **Final stage recovery**: Final output recovery rate

The goal is to help mining operations optimize their gold extraction process by accurately predicting recovery rates based on process parameters.

## Objectives

1. **Data Preparation**: Clean, preprocess, and validate the gold recovery dataset
2. **Data Analysis**: Explore metal concentration trends and process characteristics
3. **Model Development**: Build and evaluate machine learning models to predict recovery rates
4. **Performance Evaluation**: Use sMAPE (symmetric Mean Absolute Percentage Error) as the evaluation metric

## Dataset

The project uses three CSV files:

- `gold_recovery_train.csv`: Training dataset with 16,860 samples and 86 features
- `gold_recovery_test.csv`: Test dataset with 5,856 samples and 52 features
- `gold_recovery_full.csv`: Complete dataset with 22,716 samples and 86 features

### Key Features

The dataset includes:
- **Input parameters**: Feed characteristics, reagent dosages, process parameters
- **Output parameters**: Concentrate and tailing compositions for different stages
- **Target variables**: 
  - `rougher.output.recovery` (rougher stage recovery)
  - `final.output.recovery` (final stage recovery)

## Project Structure

```
.
├── Integrated_Project.ipynb    # Main Jupyter notebook with complete analysis
├── gold_recovery_train.csv     # Training dataset
├── gold_recovery_test.csv      # Test dataset
├── gold_recovery_full.csv      # Full dataset
└── README.md                   # This file
```

## Requirements

### Python Packages

- `numpy` - Numerical computing
- `pandas` - Data manipulation and analysis
- `matplotlib` - Data visualization
- `seaborn` - Statistical data visualization
- `scikit-learn` - Machine learning models and utilities

### Installation

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

## Methodology

### 1. Data Preparation

- **Duplicate Removal**: Removed exact duplicate rows
- **Missing Value Handling**: 
  - Forward-fill for time-series data
  - Median imputation for remaining missing values
- **Anomaly Detection**: 
  - Removed physically impossible negative concentrations
  - Filtered extreme outliers using IQR-based method (3.0 multiplier)
  - Result: 2,818 abnormal rows removed (16.71% of training data)

### 2. Data Analysis

- **Metal Concentration Analysis**: Analyzed concentration changes across processing stages
  - Gold (Au): Increases from 7.14 g/t to 39.32 g/t
  - Silver (Ag): Decreases from 7.80 g/t to 4.70 g/t
  - Lead (Pb): Increases from 3.19 g/t to 9.08 g/t
- **Feature Analysis**: Identified 34 features missing from test set (outputs and calculated parameters)
- **Particle Size Comparison**: Compared feed particle size distributions between train and test sets

### 3. Model Development

**Models Evaluated:**
- Linear Regression
- Random Forest Regressor (200 estimators)
- Gradient Boosting Regressor

**Evaluation Method:**
- Time-series cross-validation (5 folds) to prevent data leakage
- sMAPE metric for evaluation
- Final score: Weighted combination (25% rougher + 75% final recovery)

**Preprocessing Pipeline:**
- Median imputation for missing values
- Standard scaling for numerical features
- Feature selection to ensure train/test compatibility

## Results

### Model Performance

| Model | Mean CV sMAPE |
|-------|---------------|
| Linear Regression | **0.119847** (Best) |
| Random Forest | 0.101037 |
| Gradient Boosting | 0.099922 |

### Final Performance

- **Best Model**: Linear Regression
- **Final Weighted sMAPE**: **0.122484**
  - Rougher recovery: 25% weight
  - Final recovery: 75% weight

### Key Findings

1. **Data Quality**: Successfully cleaned and preprocessed 14,042 training samples after anomaly removal
2. **Model Selection**: Linear Regression outperformed ensemble methods, suggesting relatively linear relationships in the data
3. **Recovery Patterns**: Clear enrichment patterns observed for gold and lead, while silver shows selective separation
4. **Feature Engineering**: Proper handling of time-series data and feature availability differences between train and test sets

## Usage

1. **Open the Notebook**:
   ```bash
   jupyter notebook Integrated_Project.ipynb
   ```

2. **Run All Cells**: Execute all cells in sequence to reproduce the analysis

3. **Customize**: Modify parameters, add features, or try different models as needed

## Key Metrics

- **Training Samples**: 14,042 (after preprocessing)
- **Test Samples**: 5,856
- **Features Used**: 52 (common to both train and test sets)
- **Target Variables**: 2 (rougher and final recovery)
- **Final sMAPE**: 0.122484

## Business Impact

The developed model can assist mining operations in:

- **Process Optimization**: Real-time prediction of recovery rates to optimize operating parameters
- **Quality Control**: Early prediction enables proactive adjustments to improve efficiency
- **Resource Planning**: Accurate recovery predictions support better resource allocation and production planning

## Limitations and Future Work

- **Model Improvement**: Potential for feature engineering, hyperparameter tuning, or ensemble methods
- **Domain Knowledge**: Additional process expertise could inform better feature selection
- **Evaluation**: Test set predictions ready for evaluation once true target values are available

## Author

TripleTen Integrated Project 2

## License

This project is part of an educational program.

---

**Note**: This project demonstrates the application of machine learning techniques to industrial process optimization, with emphasis on data quality, appropriate model selection, and rigorous evaluation methodology.

