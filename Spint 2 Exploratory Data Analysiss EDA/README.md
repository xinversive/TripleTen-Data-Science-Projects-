# Instacart Market Basket Analysis

## 📋 Project Overview

This project performs an exploratory data analysis (EDA) on Instacart's grocery delivery dataset to understand customer shopping habits and identify purchasing trends. The dataset was publicly released by Instacart in 2017 for a Kaggle competition.

**Instacart** is a grocery delivery platform where customers can place grocery orders and have them delivered, similar to Uber Eats and DoorDash.

## 🎯 Objective

To explore the datasets and identify how customers are purchasing products and identifying trends using various methods of data exploration and visualization.

## 📊 Datasets

The project uses five main datasets:

1. **`instacart_orders.csv`** - Contains order information including order IDs, user IDs, order times, and days since prior order
2. **`products.csv`** - Contains product information including product IDs, names, aisle IDs, and department IDs
3. **`order_products.csv`** - Links orders to products, including add-to-cart order and reorder information
4. **`aisles.csv`** - Contains aisle information
5. **`departments.csv`** - Contains department information

## 🛠️ Technologies Used

- **Python 3**
- **pandas** - Data manipulation and analysis
- **matplotlib** - Data visualization
- **seaborn** - Statistical data visualization

## 📁 Project Structure

```
.
├── README.md
├── Sprint 2. Exploratory Data Analysis_(EDA).ipynb
├── instacart_orders.csv
├── products.csv
├── order_products.csv
├── aisles.csv
└── departments.csv
```

## 🔍 Analysis Sections

### 1. Data Preparation

#### Duplicate Value Removal
- **Orders**: Identified and removed duplicate orders
- **Products**: Checked for duplicate product IDs and names
- **Departments**: Verified no duplicates in department IDs
- **Aisles**: Verified no duplicates in aisle IDs
- **Order Products**: Checked for duplicate order-product combinations

#### Missing Value Handling
- **Products**: Filled missing product names with 'Unknown'
- **Orders**: Analyzed missing values in `days_since_prior_order` (expected for first orders)
- **Order Products**: Handled missing values in `add_to_cart_order` column

### 2. Exploratory Data Analysis

#### Section A: Easy Analysis
- **A1**: Verified data quality (order hours: 0-23, days of week: 0-6)
- **A2**: Analyzed shopping patterns by time of day
- **A3**: Analyzed shopping patterns by day of week
- **A4**: Examined time between orders

#### Section B: Medium Analysis
- **B1**: Compared order hour distributions between Wednesdays and Saturdays
- **B2**: Analyzed distribution of orders per customer
- **B3**: Identified top 20 most popular products

#### Section C: Advanced Analysis
- **C1**: Analyzed distribution of items per order
- **C2**: Identified top 20 most frequently reordered items
- **C3**: Calculated reorder proportion for each product
- **C4**: Calculated reorder proportion for each customer
- **C5**: Identified top 20 items customers add to cart first

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3 installed along with the required libraries:

```bash
pip install pandas matplotlib seaborn jupyter
```

### Running the Analysis

1. Clone or download this repository
2. Ensure all CSV files are in the same directory as the notebook
3. Open the Jupyter notebook:
   ```bash
   jupyter notebook "Sprint 2. Exploratory Data Analysis_(EDA).ipynb"
   ```
4. Run all cells to execute the complete analysis

## 📈 Key Findings

The analysis reveals several important insights about customer shopping behavior:

- **Peak Shopping Times**: Most orders occur between 10 AM and 2 PM, with peak activity on Sundays and Mondays
- **Reorder Patterns**: Most customers reorder within 7 days, with a significant spike at 30 days
- **Popular Products**: Fresh produce, especially bananas and organic fruits, dominate the top ordered items
- **Cart Behavior**: Customers tend to add fresh produce and staple items (like bananas and milk) to their carts first
- **Order Size**: Most orders contain fewer than 10 items

## 📝 Notes

- The dataset uses semicolons (`;`) as delimiters in CSV files
- Some missing values are expected (e.g., `days_since_prior_order` for first-time orders)
- The analysis includes data quality checks to ensure reliable results

## 📄 License

This project uses the Instacart dataset, which was publicly released for a Kaggle competition in 2017.

## 👤 Author

Exploratory Data Analysis project for understanding customer shopping patterns.

---

*For questions or issues, please refer to the notebook for detailed analysis and code.*

