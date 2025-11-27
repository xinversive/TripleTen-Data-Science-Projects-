# Megaline Telecom Plans Revenue Analysis

## Project Overview

This project performs a statistical data analysis for **Megaline**, a telecom operator offering two prepaid plans: **Surf** and **Ultimate**. The goal is to determine which plan generates more revenue by analyzing user behavior, usage patterns, and billing data from 500 clients in 2018.

## Objectives

- Analyze client behavior patterns across both plans
- Compare revenue generation between Surf and Ultimate plans
- Identify usage differences (calls, messages, internet data)
- Test statistical hypotheses about revenue differences
- Provide data-driven recommendations for marketing budget allocation

## Dataset Description

The project uses five CSV files containing client data from 2018:

### Data Files

1. **`megaline_users.csv`** - User information
   - 500 users with demographics, registration dates, plan subscriptions, and churn dates

2. **`megaline_calls.csv`** - Call records
   - 137,735 call records with timestamps and durations
   - Call durations are rounded up to the nearest minute per Megaline policy

3. **`megaline_messages.csv`** - Text message records
   - 76,051 message records with timestamps

4. **`megaline_internet.csv`** - Internet session data
   - 104,825 internet sessions with data usage in MB
   - Monthly usage is rounded up to the nearest GB per Megaline policy

5. **`megaline_plans.csv`** - Plan details and pricing
   - **Surf Plan**: $20/month, 500 min, 50 messages, 15 GB included
   - **Ultimate Plan**: $70/month, 3000 min, 1000 messages, 30 GB included
   - Overage rates for each plan

## Plan Details

| Plan     | Monthly Fee | Minutes Included | Messages Included | Data Included | Cost per Extra Min | Cost per Extra Message | Cost per Extra GB |
|----------|-------------|------------------|-------------------|---------------|-------------------|------------------------|-------------------|
| **Surf** | $20         | 500              | 50                | 15 GB         | $0.03             | $0.03                  | $10               |
| **Ultimate** | $70      | 3000             | 1000              | 30 GB         | $0.01             | $0.01                  | $7                |

## Methodology

### Data Preprocessing
- Converted date columns to datetime format
- Rounded call durations up to nearest minute
- Aggregated monthly usage per user (calls, messages, internet)
- Calculated monthly revenue including base fees and overage charges
- Enriched data with additional features (churn status, region, total usage)

### Analysis Steps
1. **Data Exploration**: Examined each dataset for missing values, data types, and quality issues
2. **Data Cleaning**: Fixed data types, handled missing values, and applied business rules
3. **Data Aggregation**: Created monthly usage summaries per user
4. **Revenue Calculation**: Computed monthly revenue including overages
5. **Behavioral Analysis**: Compared usage patterns between plans
6. **Statistical Testing**: Performed hypothesis tests on revenue differences

## Key Findings

### User Behavior
- **Ultimate plan users** consistently use more minutes, messages, and internet data
- **Surf plan users** show higher variability, with many exceeding plan limits
- Ultimate users demonstrate more consistent, heavier usage patterns

### Revenue Insights
- Surf plan can generate higher revenue per user when overage charges apply
- Ultimate plan provides stable, predictable income with unlimited services
- Heavy users on Surf plan generate significant additional revenue through overages

### Statistical Conclusions
- Significant difference in average monthly revenue between Surf and Ultimate users
- No significant difference in revenue between NY-NJ region users and other regions

## Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualizations
- **SciPy** - Statistical hypothesis testing

## Project Structure

```
Sprint 3. Statistical Data Analysis Project/
│
├── README.md                          # Project documentation
├── prjctX 3_notebook vscode.ipynb    # Main analysis notebook
│
├── megaline_users.csv                 # User data
├── megaline_calls.csv                 # Call records
├── megaline_messages.csv              # Message records
├── megaline_internet.csv              # Internet usage data
└── megaline_plans.csv                 # Plan details and pricing
```

## How to Use

1. **Prerequisites**: Ensure you have Python 3.x and required libraries installed:
   ```bash
   pip install pandas numpy matplotlib seaborn scipy
   ```

2. **Open the Notebook**: Launch `prjctX 3_notebook vscode.ipynb` in Jupyter Notebook or VS Code

3. **Update File Paths**: If needed, update the CSV file paths in the notebook to match your directory structure

4. **Run Analysis**: Execute cells sequentially to:
   - Load and prepare data
   - Perform exploratory analysis
   - Calculate revenue metrics
   - Generate visualizations
   - Run statistical tests

## Business Recommendations

1. **For Heavy Users**: Promote the Ultimate plan to reduce churn and improve satisfaction
2. **For Casual Users**: Continue offering the Surf plan, but monitor overage patterns
3. **Regional Strategy**: Current data does not support region-specific campaigns
4. **Revenue Optimization**: Balance between Surf plan overages and Ultimate plan stability

## Notes

- Call durations are rounded up to the nearest minute per Megaline billing policy
- Monthly data usage is rounded up to the nearest GB
- Analysis covers 500 users from 2018
- Churn date is null for active users

## Author

Statistical Data Analysis Project - Sprint 3

---

*This analysis helps Megaline's commercial department make informed decisions about advertising budget allocation between the two prepaid plans.*

