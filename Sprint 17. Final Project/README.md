# Sprint 17: Interconnect Customer Churn Prediction — Final Project

## Project Overview

This project builds a machine learning model to predict customer churn for Interconnect, a telecommunications company. The goal is to identify customers at high risk of terminating their contracts so that the company can proactively offer promotional codes and special plan options to retain them.

**Business Value:** By predicting churn early, Interconnect can:
- Reduce customer attrition
- Improve customer retention rates
- Optimize marketing spend by targeting high-risk customers
- Increase revenue through proactive customer engagement

## Dataset

The project uses four CSV files that are merged on `customerID`:

1. **`contract.csv`** (7,043 rows, 8 columns)
   - Contract information including start/end dates, contract type, billing, and payment methods
   - Key features: `BeginDate`, `EndDate`, `Type`, `PaperlessBilling`, `PaymentMethod`, `MonthlyCharges`, `TotalCharges`

2. **`personal.csv`** (7,043 rows, 5 columns)
   - Personal demographic information
   - Key features: `gender`, `SeniorCitizen`, `Partner`, `Dependents`

3. **`internet.csv`** (5,517 rows, 8 columns)
   - Internet service details (not all customers have internet service)
   - Key features: `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`

4. **`phone.csv`** (6,361 rows, 2 columns)
   - Phone service information (not all customers have phone service)
   - Key features: `MultipleLines`

**Total Dataset:** 7,043 customers after merging all tables

## Target Variable

**Churn Definition:**
- `churn = 1`: Customer has ended their contract (`EndDate` is not `'No'`)
- `churn = 0`: Customer is still active (`EndDate == 'No'`)

This binary classification problem aims to predict which customers will churn.

## Project Structure

```
Sprint 17. Final Project/
├── README.md
├── Sprint 17. Interconnect_Churn_Final_PRJCT.ipynb  # Main project notebook
├── contract.csv                                       # Contract data
├── personal.csv                                       # Personal/demographic data
├── internet.csv                                       # Internet service data
└── phone.csv                                          # Phone service data
```

## Methodology

### 1. Data Loading and Merging
- Loaded all four CSV files
- Merged tables on `customerID` using left joins to preserve all customers
- Handled missing values from customers without internet or phone services

### 2. Exploratory Data Analysis (EDA)
- Analyzed target distribution (churn vs. non-churn)
- Examined missing value patterns
- Explored feature distributions and relationships
- Identified numerical and categorical features

### 3. Data Preprocessing
- **Missing Value Handling:**
  - Numeric features: Median imputation
  - Categorical features: Constant imputation with 'missing' category
- **Feature Engineering:**
  - Converted `TotalCharges` from string to numeric
  - Identified numerical and categorical features for separate preprocessing
- **Preprocessing Pipeline:**
  - Numeric features: `SimpleImputer` (median) → `StandardScaler`
  - Categorical features: `SimpleImputer` (constant) → `OneHotEncoder`
  - Combined using `ColumnTransformer` for consistent preprocessing

### 4. Train/Validation/Test Split
- **Split Strategy:** 60% train / 20% validation / 20% test
- Stratified splitting to maintain class distribution
- Random state set to 42 for reproducibility

### 5. Model Training and Evaluation

**Models Tested:**
1. **Logistic Regression** (Baseline)
   - Linear model with class balancing
   - Fast and interpretable
   - Validation AUC-ROC: 0.830

2. **Random Forest**
   - Ensemble method with 300 trees
   - Captures non-linear relationships
   - Validation AUC-ROC: 0.806

3. **Gradient Boosting** ⭐ (Best Model)
   - Sequential ensemble method
   - Best validation performance
   - Validation AUC-ROC: 0.837

**Evaluation Metrics:**
- **Primary:** AUC-ROC (Area Under the ROC Curve)
- **Secondary:** Accuracy

### 6. Model Selection
- Selected best model based on validation AUC-ROC
- Retrained selected model on full training set (train + validation)
- Final evaluation on held-out test set

## Results

### Final Model Performance

**Selected Model:** Gradient Boosting Classifier

**Test Set Results:**
- **AUC-ROC:** 0.843
- **Accuracy:** 0.803
- **Precision (Churn):** 0.67
- **Recall (Churn):** 0.52
- **F1-Score (Churn):** 0.58

### Performance Assessment

Based on the project's assessment thresholds:
- **AUC-ROC: 0.843** falls in the **0.81–0.85** range
- **Score: 4.5 SP** ✅

The model successfully meets the project requirements and demonstrates good predictive capability for identifying customers at risk of churning.

## Key Findings

1. **Model Performance:** Gradient Boosting achieved the best balance between AUC-ROC and accuracy, making it suitable for production use.

2. **Class Imbalance:** The dataset shows class imbalance (more non-churners than churners), which is why AUC-ROC is preferred over accuracy as the primary metric.

3. **Feature Importance:** The model leverages multiple data sources (contract, personal, internet, phone) to make predictions, indicating that comprehensive customer data improves churn prediction.

4. **Business Application:** The model can rank customers by churn probability, allowing Interconnect to:
   - Target high-risk customers with retention offers
   - Allocate marketing resources efficiently
   - Reduce customer acquisition costs

## Technologies Used

- **Python 3.x**
- **Libraries:**
  - `pandas` - Data manipulation and analysis
  - `numpy` - Numerical computing
  - `matplotlib` - Data visualization
  - `scikit-learn` - Machine learning:
    - `LogisticRegression`
    - `RandomForestClassifier`
    - `GradientBoostingClassifier`
    - `Pipeline`, `ColumnTransformer`
    - `SimpleImputer`, `StandardScaler`, `OneHotEncoder`
    - `train_test_split`
    - `roc_auc_score`, `accuracy_score`, `classification_report`

## Usage

### Running the Notebook

1. **Prerequisites:**
   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```

2. **Data Files:**
   - Ensure all CSV files (`contract.csv`, `personal.csv`, `internet.csv`, `phone.csv`) are in the same directory as the notebook

3. **Execution:**
   - Open `Sprint 17. Interconnect_Churn_Final_PRJCT.ipynb` in Jupyter Notebook or JupyterLab
   - Run cells sequentially from top to bottom
   - The notebook includes:
     - Data loading and merging
     - Exploratory data analysis
     - Preprocessing pipeline setup
     - Model training and evaluation
     - Model comparison and selection
     - Final test set evaluation

### Key Code Sections

**Preprocessing Pipeline:**
```python
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, num_features),
        ('cat', categorical_transformer, cat_features)
    ]
)
```

**Model Training:**
```python
gb_clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', GradientBoostingClassifier(random_state=42))
])
```

## Project Workflow

1. **Data Collection & Merging** → Combined multiple data sources
2. **Exploratory Data Analysis** → Understood data patterns and relationships
3. **Data Preprocessing** → Handled missing values, encoded features, scaled data
4. **Model Development** → Trained and evaluated multiple models
5. **Model Selection** → Chose best model based on validation performance
6. **Final Evaluation** → Assessed model on test set
7. **Business Application** → Model ready for deployment to identify at-risk customers

## Future Improvements

Potential enhancements for the model:
- Feature engineering (e.g., customer tenure from dates)
- Hyperparameter tuning for Gradient Boosting
- Experimentation with advanced models (XGBoost, LightGBM, CatBoost)
- Feature importance analysis to identify key churn drivers
- Cost-benefit analysis for retention campaigns

## Author

TripleTen Data Science Bootcamp - Sprint 17 Final Project

## License

This project is part of the TripleTen Data Science Bootcamp curriculum.

