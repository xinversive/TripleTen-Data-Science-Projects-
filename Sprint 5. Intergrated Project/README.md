# Video Game Sales Forecasting Analysis

**Project:** Ice Store - Video Game Sales Analysis & Forecasting  
**Analysis Window:** 2013–2016  
**Purpose:** Data-driven insights to inform 2017 strategic planning

---

## 📋 Overview

This project analyzes historical video game sales data to identify market trends, platform performance, genre profitability, and regional preferences. The analysis provides actionable insights for inventory management, marketing strategy, and regional customization for Ice Store's 2017 business planning.

## 🎯 Objectives

1. **Platform Analysis**: Identify leading, growing, and declining gaming platforms
2. **Review Metrics**: Determine which review metrics (critic vs. user scores) better predict sales
3. **Genre Performance**: Analyze genre sales by total volume and average per-title performance
4. **Regional Profiling**: Build comprehensive profiles for North America, Europe, and Japan markets
5. **Statistical Testing**: Conduct hypothesis tests to validate assumptions about user satisfaction
6. **Strategic Recommendations**: Provide data-driven recommendations for 2017 strategy

## 📊 Dataset

- **Source**: `games.csv`
- **Size**: 16,715 records with 11 features
- **Features Include**:
  - Game name, platform, genre, ESRB rating
  - Year of release
  - Regional sales (NA, EU, JP, Other)
  - Critic scores (0-100)
  - User scores (0-10)

## 🛠️ Requirements

### Python Libraries
```python
numpy
pandas
matplotlib
scipy
```

### Installation
```bash
pip install numpy pandas matplotlib scipy
```

## 📁 Project Structure

```
Sprint 5. Integrated Project/
│
├── games.csv                          # Dataset
├── project 5 notebook .ipynb         # Main analysis notebook
└── README.md                          # This file
```

## 🔍 Analysis Sections

### 1. Data Preparation
- Column standardization (lowercase)
- Data type corrections (numeric conversions, handling missing values)
- Computation of `total_sales` from regional sales
- Missing data analysis

### 2. Temporal Analysis
- Game releases by year
- Platform sales trends over time
- Identification of growing vs. declining platforms

### 3. Platform Performance (2013-2016)
- Leading platforms by total sales
- Growth trends (slope analysis)
- Boxplot analysis of sales distribution by platform

### 4. Review Metrics vs. Sales
- Correlation analysis: Critic scores vs. Sales (PS4)
- Correlation analysis: User scores vs. Sales (PS4)
- **Key Finding**: Critic scores (r = 0.407) show stronger correlation than user scores (r = -0.032)

### 5. Cross-Platform Comparison
- Analysis of multi-platform game releases
- Platform-specific sales performance for same titles

### 6. Genre Analysis
- Total sales by genre
- Average sales per title by genre
- Identification of high-volume vs. high-margin genres

### 7. Regional Market Profiles
Comprehensive analysis of three key markets:

#### North America
- **Top Platforms**: PS4, Xbox One, Xbox 360
- **Top Genres**: Action, Shooter, Sports
- **ESRB Preference**: M-rated content dominant

#### Europe
- **Top Platforms**: PS4, PS3, Xbox One
- **Top Genres**: Action, Shooter, Sports
- **ESRB Preference**: M-rated content dominant

#### Japan
- **Top Platforms**: 3DS, PS3, PS Vita
- **Top Genres**: Role-Playing, Action, Misc
- **ESRB Preference**: More balanced, T-rated slightly leading

### 8. Hypothesis Testing
Two statistical tests using Welch's t-test (α = 0.05):

1. **H0A**: Mean user scores on Xbox One = PC
   - **Result**: p = 0.1476 → Fail to reject (no significant difference)

2. **H0B**: Mean user scores for Action = Sports
   - **Result**: p < 0.0001 → Reject (significant difference)

## 📈 Key Findings

### Platform Trends
- **Growing**: PS4, Xbox One (eighth-generation consoles)
- **Stable**: Nintendo 3DS (especially strong in Japan)
- **Declining**: PS3, Xbox 360, Wii (seventh-generation consoles)

### Review Metrics
- **Critic scores** are more reliable predictors of sales than user scores
- Professional reviews align better with commercial performance

### Genre Insights
- **Volume Leaders**: Action, Shooter genres
- **Profitability Leaders**: Shooter, Sports (highest per-title sales)
- Genre choice significantly impacts user satisfaction

### Regional Differences
- **NA/EU**: Similar preferences (console-focused, Action/Shooter, M-rated)
- **Japan**: Distinct market (handheld-focused, Role-Playing, more balanced ratings)

## 💡 Strategic Recommendations

1. **Platform Focus**: Prioritize PS4 and Xbox One inventory and marketing
2. **Review Strategy**: Use critic scores as primary performance indicator
3. **Genre Mix**: Balance high-volume (Action) with high-margin (Shooter, Sports) titles
4. **Regional Customization**: 
   - NA/EU: Console Action/Shooter titles
   - Japan: Handheld Role-Playing games
5. **User Satisfaction**: Consider genre impact on customer retention

## 🚀 How to Run

1. **Ensure dataset is available**:
   - Place `games.csv` in the project directory
   - Or update the path in the notebook if using a different location

2. **Open the notebook**:
   ```bash
   jupyter notebook "project 5 notebook .ipynb"
   ```

3. **Run all cells**:
   - Execute cells sequentially from top to bottom
   - All visualizations will display inline

4. **Alternative paths** (handled automatically):
   - `/datasets/games.csv`
   - `games.csv` (current directory)
   - `./datasets/games.csv`
   - `/mnt/data/games.csv`

## 📝 Notes

- The analysis focuses on the 2013-2016 window to capture recent trends leading into 2017
- Missing values in subjective measures (scores, ratings) are preserved as NaN (not imputed)
- All sales figures are in millions of USD
- Statistical tests use Welch's t-test (unequal variances assumed)

## 📊 Visualizations

The notebook includes multiple visualizations:
- Game releases by year (bar chart)
- Platform sales trends over time (line plots)
- Sales distribution by platform (boxplots)
- Review scores vs. sales (scatter plots)
- Genre sales distribution (bar charts)
- Regional sales profiles (multi-panel bar charts)

## 🔬 Methodology

- **Data Cleaning**: Standardized formats, corrected data types, handled missing values
- **Exploratory Analysis**: Descriptive statistics, trend analysis, distribution analysis
- **Statistical Testing**: Welch's t-test for comparing means with unequal variances
- **Correlation Analysis**: Pearson correlation coefficients for review-sales relationships
- **Growth Analysis**: Linear regression slopes to identify platform trends

---

## 📄 License

This project is for educational/analytical purposes.

## 👤 Author

Sprint 5 - Integrated Project

---

**Last Updated**: 2024

