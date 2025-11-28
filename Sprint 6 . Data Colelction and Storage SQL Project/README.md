# Sprint 6: Data Collection and Storage (SQL Project)

## Overview
This project analyzes Chicago taxi trip data from November 2017 to identify key patterns in taxi company performance, neighborhood drop-off locations, and the impact of weather conditions on ride durations. The analysis combines SQL query results with Python data analysis and visualization to provide actionable insights for taxi service operations.

## Project Objectives
1. **Identify top-performing taxi companies** by analyzing trip volumes
2. **Analyze neighborhood drop-off patterns** to understand demand distribution
3. **Test the hypothesis** that weather conditions significantly affect ride durations from the Loop to O'Hare International Airport

## Data Sources
The project uses three CSV files generated from SQL queries:
- `project_sql_result_01.csv` - Taxi company trip counts (64 companies)
- `project_sql_result_04.csv` - Neighborhood drop-off averages (94 neighborhoods)
- `project_sql_result_07.csv` - Loop to O'Hare trips with weather conditions and durations

## Technologies Used
- **Python** - Data analysis and statistical testing
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical data visualization
- **SciPy** - Statistical hypothesis testing
- **Jupyter Notebook** - Interactive analysis environment

## Key Findings

### 1. Taxi Company Performance (November 15-16, 2017)
- **Flash Cab** dominated the market with nearly 20,000 trips, far exceeding competitors
- The top 4 companies (Flash Cab, Taxi Affiliation Services, Medallion Leasing, Yellow Cab) handled a significant portion of total trips
- Market concentration: A small number of large operators dominated, with many smaller companies handling fewer than 3,000 trips each

### 2. Neighborhood Drop-off Patterns (November 2017)
- **The Loop** led with over 10,000 average drop-offs, confirming its status as Chicago's central business district
- **River North** and **Streeterville** followed closely, reflecting high activity in entertainment and hospitality zones
- **O'Hare International Airport** ranked 5th, showing substantial airport-bound traffic
- Urban core and entertainment districts generated the majority of taxi activity

### 3. Weather Impact on Ride Durations
**Hypothesis Test Results:**
- **Null Hypothesis (H₀):** Average ride durations on "Bad" weather Saturdays = "Good" weather Saturdays
- **Alternative Hypothesis (H₁):** Average ride durations differ between weather conditions
- **Test:** Welch two-sample t-test (α = 0.05)
- **Result:** **Rejected H₀** (p-value < 0.001, t-statistic = -7.19)

**Key Insight:** Ride durations from the Loop to O'Hare are significantly longer during bad weather conditions, requiring operational adjustments for taxi services.

## Project Structure
```
Sprint 6 . Data Collection and Storage SQL Project/
│
├── Sprint 6. Data Collection and Storage_(SQL).ipynb.ipynb  # Main analysis notebook
├── project_sql_result_01.csv                                # Taxi company data
├── project_sql_result_04.csv                                # Neighborhood data
├── project_sql_result_07.csv                                # Weather and duration data
└── README.md                                                 # This file
```

## How to Run
1. Ensure you have Python 3.x installed with the following packages:
   ```bash
   pip install pandas matplotlib seaborn scipy jupyter
   ```

2. Open the Jupyter Notebook:
   ```bash
   jupyter notebook "Sprint 6. Data Collection and Storage_(SQL).ipynb.ipynb"
   ```

3. Update the CSV file paths in the notebook if needed (currently set to `/datasets/`)

4. Run all cells sequentially to reproduce the analysis

## Visualizations
The project includes two main visualizations:
1. **Top 15 Taxi Companies Bar Chart** - Horizontal bar chart showing trip volumes by company
2. **Top 10 Neighborhoods Bar Chart** - Horizontal bar chart showing average drop-offs by neighborhood
3. **Duration Distribution Plot** - Overlapping histograms comparing trip durations under good vs. bad weather conditions

## Business Implications
The analysis reveals several actionable insights for taxi service operations:
- **Market Concentration:** Focus partnership and resource allocation on top-performing companies
- **Demand Forecasting:** Prioritize driver positioning in high-traffic neighborhoods (Loop, River North, Streeterville)
- **Weather-Aware Operations:** Implement weather-responsive staffing and routing policies, especially for airport routes
- **Customer Communication:** Proactively communicate potential delays during adverse weather conditions

## Conclusion
This analysis demonstrates that weather conditions significantly impact ride durations, particularly for airport-bound trips. Combined with the identified market concentration and neighborhood demand patterns, these findings suggest that implementing weather-aware dispatch systems, strategic driver positioning, and proactive customer communication could substantially improve service efficiency and customer satisfaction during adverse conditions.

## Author
Data Analysis Project - Sprint 6

## Date
November 2017 Data Analysis

