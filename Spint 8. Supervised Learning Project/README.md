# Beta Bank Churn Prediction - Supervised Learning Project

## Project Overview

This project focuses on predicting customer churn for Beta Bank using supervised learning techniques. The goal is to build a machine learning model that can accurately identify customers who are likely to exit the bank, enabling proactive retention strategies.

**Objective**: Achieve an **F1 score ≥ 0.59** on the test set.

## Dataset

- **Source**: `Churn.csv`
- **Size**: 10,000 customer records
- **Features**: 14 columns including customer demographics, account information, and behavioral data
- **Target Variable**: `Exited` (binary: 0 = retained, 1 = churned)
- **Class Distribution**: Approximately 20% churn rate (imbalanced dataset)

### Features

- `CreditScore`: Customer's credit score
- `Geography`: Customer's country (France, Germany, Spain)
- `Gender`: Customer's gender
- `Age`: Customer's age
- `Tenure`: Number of years with the bank
- `Balance`: Account balance
- `NumOfProducts`: Number of bank products used
- `HasCrCard`: Whether customer has a credit card (0/1)
- `IsActiveMember`: Whether customer is an active member (0/1)
- `EstimatedSalary`: Estimated salary

## Methodology

### 1. Data Preprocessing
- Handled missing values in `Tenure` column (909 missing values) by filling with median
- Removed non-predictive columns: `RowNumber`, `CustomerId`, `Surname`
- One-hot encoded categorical variables (`Geography`, `Gender`)
- Standardized numerical features using `StandardScaler`
- Split data into training (70%) and test (30%) sets with stratification

### 2. Model Development

#### Baseline Model
- **Logistic Regression**: Used as a baseline to establish performance benchmarks
  - F1 Score: 0.299
  - ROC-AUC: 0.788

#### Improved Models
- **Random Forest with Manual Upsampling**: 
  - Addressed class imbalance by upsampling the minority class (3x repetition)
  - F1 Score: 0.641
  - ROC-AUC: 0.877

- **Hyperparameter-Tuned Random Forest**:
  - Used `GridSearchCV` to optimize hyperparameters
  - Best parameters: `max_depth=15`, `n_estimators=200`
  - F1 Score: 0.624
  - ROC-AUC: 0.868

## Results

### Final Model Performance

The tuned Random Forest classifier achieved the following metrics:

| Metric | Value |
|--------|-------|
| **F1 Score** | **0.624** ✅ |
| **ROC-AUC Score** | 0.868 |
| **Precision (Churn)** | 0.67 |
| **Recall (Churn)** | 0.58 |
| **Overall Accuracy** | 86% |

### Classification Report

```
              precision    recall  f1-score   support

           0       0.90      0.93      0.91      2389
           1       0.67      0.58      0.62       611

    accuracy                           0.86      3000
   macro avg       0.79      0.75      0.77      3000
weighted avg       0.85      0.86      0.85      3000
```

**Goal Achievement**: ✅ **F1 Score = 0.624 ≥ 0.59** (Target Met)

## Key Findings

1. **Class Imbalance**: The dataset showed significant class imbalance (~20% churn rate), requiring upsampling techniques to improve model performance on the minority class.

2. **Feature Engineering**: Removing non-predictive identifiers and one-hot encoding categorical variables improved model performance.

3. **Model Selection**: Random Forest outperformed Logistic Regression, particularly after addressing class imbalance through upsampling.

4. **Hyperparameter Tuning**: Grid search optimization improved model stability and performance.

## Requirements

### Python Libraries

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
```

### Installation

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Usage

1. **Load the notebook**: Open `supervised_learning.ipynb` in Jupyter Notebook or JupyterLab

2. **Update file path**: Modify the data path in Cell 2:
   ```python
   df = pd.read_csv('Churn.csv')  # Update path as needed
   ```

3. **Run all cells**: Execute the notebook cells sequentially to reproduce the analysis

4. **View results**: The final model performance metrics and classification report will be displayed in the output cells

## Project Structure

```
.
├── Churn.csv                    # Dataset
├── supervised_learning.ipynb   # Main analysis notebook
└── README.md                    # This file
```

## Recommendations

The Random Forest model with upsampling and hyperparameter tuning successfully predicts customer churn and can be deployed to help Beta Bank:

1. **Identify at-risk customers**: The model correctly identifies 58% of churning customers (recall)
2. **Optimize retention efforts**: With 67% precision, the model minimizes false positives
3. **Proactive intervention**: Enable targeted retention campaigns for high-risk customers

## Future Improvements

- Experiment with additional ensemble methods (Gradient Boosting, XGBoost)
- Feature engineering: Create interaction features or polynomial features
- Advanced sampling techniques: Try SMOTE or ADASYN for better class balancing
- Model interpretability: Use SHAP values to understand feature importance
- Cross-validation: Implement k-fold cross-validation for more robust evaluation

## Author

Supervised Learning Project - Sprint 8

## License

This project is for educational purposes.

