# Machine Learning for Texts: Sentiment Classification Project

This project builds a sentiment classifier for IMDB movie reviews to automatically detect negative reviews for the **Film Junky Union**. The goal is to classify movie reviews as positive or negative with an F1 score of at least 0.85.

## Project Overview

The project implements multiple machine learning models to classify IMDB movie reviews into positive (1) or negative (0) sentiment categories. The dataset contains 47,331 labeled reviews that are already split into training and test sets.

## Dataset

- **File**: `imdb_reviews.tsv`
- **Size**: 47,331 reviews
- **Target Variable**: `pos` (0 = negative, 1 = positive)
- **Split**: Pre-split into train (23,796) and test (23,535) sets via the `ds_part` column
- **Class Balance**: Approximately 50/50 in both train and test sets

### Dataset Columns

The dataset includes the following columns:
- `tconst`: Title identifier
- `title_type`: Type of title (movie, short, etc.)
- `primary_title`: Primary title of the movie
- `original_title`: Original title
- `start_year`: Release year
- `end_year`: End year (if applicable)
- `runtime_minutes`: Runtime in minutes
- `is_adult`: Adult content flag
- `genres`: Movie genres
- `average_rating`: Average rating
- `votes`: Number of votes
- `review`: The review text (main feature)
- `rating`: Review rating
- `sp`: Sentiment polarity
- `pos`: Target variable (0 = negative, 1 = positive)
- `ds_part`: Dataset partition (train/test)
- `idx`: Index

## Models Implemented

Three different machine learning models were trained and evaluated:

### 1. Logistic Regression (Best Performer)
- **Features**: TF-IDF with 20,000 unigrams, English stop-word removal
- **F1 Score**: 0.879
- **Accuracy**: 0.879
- **Status**: ✅ Exceeds requirement (F1 ≥ 0.85)

### 2. Linear Support Vector Classifier (LinearSVC)
- **Features**: TF-IDF with 20,000 unigrams, English stop-word removal
- **F1 Score**: 0.860
- **Accuracy**: 0.862
- **Status**: ✅ Exceeds requirement (F1 ≥ 0.85)

### 3. Gradient Boosting Classifier
- **Features**: Count Vectorizer (5,000 features) + TruncatedSVD (150 components)
- **F1 Score**: 0.785
- **Accuracy**: 0.782
- **Status**: ❌ Below requirement

## Key Findings

1. **Simple linear models on TF-IDF features are highly effective** for movie review sentiment analysis
2. **Logistic Regression performed best** among all tested models
3. **Class balance is nearly perfect** (50/50), so no special resampling techniques were needed
4. **TF-IDF with unigrams** provides sufficient features for this task
5. **Tree-based models** (Gradient Boosting) are less efficient on high-dimensional text data compared to linear classifiers

## Requirements

The project uses the following Python libraries:

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
```

## Usage

1. **Open the Jupyter Notebook**:
   ```bash
   jupyter notebook "Sprint 14. Machine Learning for Project.ipynb"
   ```

2. **Ensure the dataset is in the same directory**:
   - The notebook expects `imdb_reviews.tsv` to be in the current working directory

3. **Run all cells** to:
   - Load and explore the data
   - Preprocess text using TF-IDF vectorization
   - Train and evaluate all three models
   - Classify sample reviews

## Project Structure

```
.
├── README.md                                    # This file
├── Sprint 14. Machine Learning for Project.ipynb  # Main project notebook
└── imdb_reviews.tsv                            # Dataset file
```

## Results Summary

| Model | F1 Score | Accuracy | Status |
|-------|----------|----------|--------|
| Logistic Regression | 0.879 | 0.879 | ✅ Pass |
| LinearSVC | 0.860 | 0.862 | ✅ Pass |
| Gradient Boosting | 0.785 | 0.782 | ❌ Fail |

## Notes

- The project uses traditional ML models on TF-IDF features rather than deep learning (BERT) due to computational constraints
- All models were evaluated on the pre-defined test set
- The Logistic Regression model is recommended for production use based on its superior performance

## Author

Machine Learning for Texts - Sprint 14 Project

