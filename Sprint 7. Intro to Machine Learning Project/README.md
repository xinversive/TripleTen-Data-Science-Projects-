# Megaline Plan Recommendation - Machine Learning Project

## Project Overview

This project builds a machine learning classifier to recommend mobile plans for Megaline subscribers. The model predicts whether a customer should be recommended the **Ultra** plan (premium) or the **Smart** plan (standard) based on their monthly usage behavior.

**Author:** Bilal R  
**Date:** September 4, 2025

## Goal

Build a classifier that predicts `is_ultra` (Ultra=1, Smart=0) with **accuracy ≥ 0.75** on the held-out test set.

## Dataset

**File:** `users_behavior.csv`

**Features:**
- `calls` — number of calls
- `minutes` — total call duration (minutes)
- `messages` — number of SMS messages
- `mb_used` — internet traffic (MB)
- `is_ultra` — target variable (Ultra=1, Smart=0)

**Dataset Statistics:**
- Total samples: 3,214
- Class distribution: 69.4% Smart (0), 30.6% Ultra (1)
- No missing values
- All features are numeric

## Project Structure

1. **Data Loading & Exploration**
   - Load and inspect the dataset
   - Check for missing values
   - Analyze target distribution

2. **Data Splitting**
   - Train set: 60% (1,928 samples)
   - Validation set: 20% (643 samples)
   - Test set: 20% (643 samples)
   - Stratified splitting to maintain class balance

3. **Baseline Model**
   - Dummy classifier (most frequent class): 69.4% accuracy

4. **Model Training & Hyperparameter Tuning**
   - **Logistic Regression** (with StandardScaler)
     - Tested C values: [0.1, 1.0, 10.0]
     - Best validation accuracy: 0.7387
   
   - **Decision Tree**
     - Grid search over max_depth (2-20) and min_samples_leaf [1, 2, 3, 5]
     - Best validation accuracy: ~0.8025
   
   - **Random Forest**
     - Grid search over n_estimators [50, 100, 200, 300], max_depth [None, 5, 10, 15, 20], min_samples_split [2, 5]
     - Best validation accuracy: 0.8149

5. **Final Model Selection**
   - Best model: **Random Forest**
   - Best hyperparameters:
     - `n_estimators`: 50
     - `max_depth`: 10
     - `min_samples_split`: 5

6. **Final Evaluation**
   - Retrained on combined train+validation set
   - Evaluated on held-out test set

7. **Sanity Checks**
   - Shuffled labels test to verify model learns real signal

## Results

### Final Test Performance

- **Test Accuracy: 0.8243** ✅ (exceeds 0.75 requirement)

**Classification Report (Test Set):**
```
              precision    recall  f1-score   support

           0      0.828     0.942     0.881       446
           1      0.809     0.558     0.661       197

    accuracy                          0.824       643
   macro avg      0.819     0.750     0.771       643
weighted avg      0.822     0.824     0.814       643
```

### Key Findings

- Random Forest outperformed Logistic Regression and Decision Tree
- The model shows good precision for both classes
- Higher recall for Smart plan (0) than Ultra plan (1)
- Sanity check with shuffled labels confirmed the model learns meaningful patterns

## Requirements

### Python Packages

```
numpy
pandas
scikit-learn
matplotlib
```

### Installation

```bash
pip install numpy pandas scikit-learn matplotlib
```

## Usage

1. Ensure `users_behavior.csv` is in the same directory as the notebook
2. Open `Megaline_IntroML_Project.ipynb` in Jupyter Notebook or JupyterLab
3. Run all cells sequentially

The notebook will:
- Load and explore the data
- Split into train/validation/test sets
- Train and compare multiple models
- Select the best model based on validation performance
- Evaluate the final model on the test set
- Perform sanity checks

## Model Performance Summary

| Model | Validation Accuracy | Test Accuracy |
|-------|-------------------|---------------|
| Baseline (Dummy) | 0.694 | - |
| Logistic Regression | 0.7387 | - |
| Decision Tree | ~0.8025 | - |
| **Random Forest** | **0.8149** | **0.8243** |

## Notes

- **Stratified splitting** ensures class balance across all splits
- **Feature scaling** (StandardScaler) is applied for Logistic Regression
- **Random state** (12345) is fixed for reproducibility
- Trees/forests perform well on tabular data with non-linear relationships
- The model successfully exceeds the 0.75 accuracy requirement

## Files

- `Megaline_IntroML_Project.ipynb` - Main project notebook
- `users_behavior.csv` - Dataset with user behavior and plan labels
- `README.md` - This file

