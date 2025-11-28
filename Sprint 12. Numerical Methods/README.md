# Used Car Price Prediction - Rusty Bargain

A comprehensive machine learning project for predicting used car prices using various regression models. This project compares multiple algorithms including Linear Regression, Decision Tree, Random Forest, and gradient boosting models (LightGBM, XGBoost, CatBoost) to identify the best-performing model for price prediction.

## 📋 Project Overview

This project analyzes a dataset of used car listings from Rusty Bargain and builds predictive models to estimate car prices. The notebook systematically evaluates different machine learning approaches, comparing their performance based on RMSE (Root Mean Squared Error), training time, and prediction speed.

## 🎯 Objectives

- Build and compare multiple regression models for used car price prediction
- Evaluate model performance using RMSE on validation and test sets
- Measure training time and inference speed for each model
- Identify the best-performing model for production use

## 📊 Dataset

- **Source**: Rusty Bargain used car listings
- **Size**: 354,369 records with 16 features
- **Target Variable**: Price
- **Features**: Includes vehicle characteristics such as:
  - Vehicle type, brand, model
  - Production year, mileage, power
  - Fuel type, gearbox type
  - Registration month, and more

## 🔧 Requirements

### Core Dependencies
- Python 3.x
- NumPy
- Pandas
- Scikit-learn

### Optional Dependencies (for advanced models)
- LightGBM
- XGBoost
- CatBoost

### Installation

```bash
pip install numpy pandas scikit-learn
pip install lightgbm xgboost catboost  # Optional, for gradient boosting models
```

## 📁 Project Structure

```
.
├── Used_Car_Price_Project_RustyBargain_DATA_PINNED (1).ipynb  # Main notebook
├── car_data.csv                                                # Dataset (expected at /datasets/car_data.csv)
└── README.md                                                   # This file
```

## 🚀 Usage

1. **Prepare the Dataset**
   - Ensure `car_data.csv` is located at `/datasets/car_data.csv`
   - The notebook expects the dataset in this specific location

2. **Open the Notebook**
   - Open `Used_Car_Price_Project_RustyBargain_DATA_PINNED (1).ipynb` in Jupyter Notebook or JupyterLab

3. **Run the Cells**
   - Execute cells sequentially from top to bottom
   - The notebook is organized into sections:
     - Setup & Utilities
     - Data Loading & Inspection
     - Data Cleaning & Preprocessing
     - Model Training & Evaluation
     - Model Comparison
     - Final Model Selection & Testing
     - Inference Speed Analysis

## 📈 Models Evaluated

1. **Linear Regression** (with One-Hot Encoding)
   - Baseline model for comparison
   - Fast training and prediction

2. **Decision Tree** (with Ordinal Encoding)
   - Hyperparameter tuning via GridSearchCV
   - Optimized for max_depth, min_samples_split, min_samples_leaf

3. **Random Forest** (with Ordinal Encoding)
   - Ensemble of decision trees
   - Grid search optimization for n_estimators, max_depth, and other parameters

4. **LightGBM** (Native Categorical Support)
   - Gradient boosting framework
   - Manual hyperparameter search
   - Handles categorical features natively

5. **XGBoost** (Optional)
   - Gradient boosting with One-Hot Encoding
   - Grid search optimization

6. **CatBoost** (Optional)
   - Gradient boosting with built-in categorical handling
   - Early stopping for optimization

## 📊 Results

### Best Model: Random Forest

- **Validation RMSE**: 1,597.20
- **Test RMSE**: 1,591.22
- **Training Time**: ~1,216 seconds
- **Inference Speed**:
  - Single-sample latency: ~66ms
  - Batch processing: ~19ms per 1,000 rows

### Model Comparison

The project compares all models based on:
- **RMSE**: Lower is better (measures prediction accuracy)
- **Training Time**: Time required to train the model
- **Prediction Speed**: Time to make predictions (single and batch)

## 🔍 Key Features

- **Comprehensive Data Cleaning**: Handles missing values, outliers, and data quality issues
- **Multiple Encoding Strategies**: One-Hot Encoding for linear models, Ordinal Encoding for tree-based models
- **Hyperparameter Optimization**: Grid search and cross-validation for optimal parameters
- **Performance Benchmarking**: Systematic comparison of training time and inference speed
- **Production-Ready Evaluation**: Final model tested on held-out test set

## 💡 Key Insights

1. **Random Forest** emerged as the best model, balancing accuracy and performance
2. Ensemble methods (Random Forest, gradient boosting) outperformed simpler models
3. Proper preprocessing and hyperparameter tuning significantly improved model performance
4. The final model demonstrates good generalization with consistent performance on validation and test sets

## 🔮 Future Improvements

- Feature engineering to capture more complex relationships
- Ensemble methods combining multiple models
- Further hyperparameter optimization
- Advanced outlier detection and handling
- Exploration of deep learning approaches
- Real-time prediction API development

## 📝 Notes

- The notebook uses `%%time` magic commands for performance profiling
- Memory management techniques (gc.collect()) are used for large datasets
- Models gracefully handle missing optional dependencies (XGBoost, CatBoost, LightGBM)
- The project follows best practices for train/validation/test splitting

## 👤 Author

Numerical Methods Project - Sprint 12

## 📄 License

This project is for educational purposes.

---

**Note**: Make sure the dataset path is correctly configured (`/datasets/car_data.csv`) before running the notebook.

