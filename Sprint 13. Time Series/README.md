# Taxi Orders Time Series Forecasting

## Project Description

This project focuses on predicting the number of taxi orders for the next hour using historical data from Sweet Lift Taxi company. The goal is to help attract more drivers during peak hours by accurately forecasting demand.

**Objective**: Build a time series forecasting model that predicts the number of taxi orders for the next hour with an RMSE metric on the test set not exceeding 48.

## Project Structure

```
.
├── taxi.csv                                    # Historical taxi orders data
├── time_series_project_with_your_taxi_data.ipynb  # Main project notebook
└── README.md                                   # This file
```

## Data Description

The dataset (`taxi.csv`) contains:
- **datetime**: Timestamp of the order (10-minute intervals)
- **num_orders**: Number of taxi orders at that timestamp

**Data Period**: March 1, 2018 to August 31, 2018
- Original data: 26,496 entries (10-minute intervals)
- After resampling to hourly: 4,392 hourly observations

## Methodology

### 1. Data Preparation
- Load and resample data from 10-minute intervals to hourly intervals
- Sort data chronologically

### 2. Exploratory Data Analysis
- Analyze patterns by hour of day, day of week, and month
- Visualize time series trends
- Identify seasonal patterns and peak hours

### 3. Feature Engineering
- **Calendar features**: hour, day of week, month
- **Lag features**: Previous 1-24 hours of orders
- **Rolling statistics**: Rolling means over windows of 3, 6, 12, and 24 hours

### 4. Model Training
The project trains and compares multiple models:
- **Linear Regression**: Baseline linear model
- **Random Forest**: Multiple configurations with different depths (5, 10) and estimators (100, 200)
- **Gradient Boosting**: Multiple configurations with different depths (3, 4) and estimators (100, 200)

### 5. Model Evaluation
- **Train/Validation/Test Split**: 
  - Training: ~81% of data
  - Validation: ~9% of data
  - Test: 10% of data (as required)
- **Metric**: Root Mean Squared Error (RMSE)
- **Baseline**: Naive forecast using the previous hour's value

## Results

### Best Model
**Random Forest Regressor** with:
- Max depth: 10
- Number of estimators: 200

### Performance Metrics
- **Validation RMSE**: 32.22
- **Test RMSE**: 45.58 ✅ (meets requirement of ≤ 48)
- **Baseline RMSE**: 58.93

The model successfully meets the project requirement with an RMSE of 45.58 on the test set, which is below the threshold of 48.

## Requirements

### Python Packages
```
pandas
numpy
matplotlib
scikit-learn
jupyter
```

### Installation
```bash
pip install pandas numpy matplotlib scikit-learn jupyter
```

## Usage

1. **Open the Jupyter Notebook**:
   ```bash
   jupyter notebook time_series_project_with_your_taxi_data.ipynb
   ```

2. **Ensure the data file is in the same directory**:
   - The notebook expects `taxi.csv` in the current working directory

3. **Run all cells**:
   - Execute cells sequentially to reproduce the analysis and model training

## Key Features

- Time-based train/validation/test split to prevent data leakage
- Comprehensive feature engineering including lag and rolling statistics
- Multiple model comparison with hyperparameter tuning
- Visualization of predictions vs actual values
- Detailed exploratory data analysis

## Project Checklist

- [x] Jupyter Notebook is open
- [x] The code is error-free
- [x] The cells with the code have been arranged in order of execution
- [x] The data has been downloaded and prepared
- [x] The data has been analyzed
- [x] The model has been trained and hyperparameters have been selected
- [x] The models have been evaluated. Conclusion has been provided
- [x] RMSE for the test set is not more than 48

## Conclusion

The Random Forest model successfully predicts taxi orders for the next hour with an RMSE of 45.58, meeting the project requirement. The model significantly outperforms the naive baseline (previous hour prediction) and can be used to help optimize driver allocation during peak hours.

