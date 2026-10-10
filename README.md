# Customer Personality & Shopping Behavior Analyzer

## Project Overview

This project analyzes customer purchasing behavior and segments customers into meaningful groups using RFM Analysis and K-Means Clustering.

The project also provides marketing recommendations for each customer segment through an interactive Streamlit dashboard.

## Objective

- Analyze customer purchasing behavior.
- Perform Exploratory Data Analysis (EDA).
- Calculate RFM metrics.
- Apply feature transformation and scaling.
- Use K-Means Clustering for customer segmentation.
- Profile and name the resulting customer segments.
- Provide suitable marketing recommendations.
- Build an interactive Streamlit dashboard.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

## Dataset

The project uses transaction-level customer data containing:

- CustomerID
- InvoiceDate
- Product
- Category
- Quantity
- UnitPrice

A `TotalAmount` column is created using:

`TotalAmount = Quantity × UnitPrice`

## Project Workflow

### 1. Data Loading and Inspection

The transaction dataset is loaded using Pandas and checked for:

- Shape
- Columns
- Data types
- Missing values
- Duplicate records
- Basic statistics

### 2. Data Cleaning

The dataset is cleaned by:

- Removing duplicate records.
- Converting `InvoiceDate` to datetime.
- Removing rows with missing `CustomerID` or `UnitPrice`.
- Removing invalid negative Quantity and UnitPrice values.
- Creating the `TotalAmount` column.

### 3. Exploratory Data Analysis

EDA is performed to understand:

- Number of customers
- Number of transactions
- Total revenue
- Average transaction value
- Category distribution
- Product distribution

### 4. RFM Analysis

Three customer-level metrics are calculated:

- **Recency** – number of days since the customer's latest purchase.
- **Frequency** – number of transactions made by the customer.
- **Monetary** – total spending by the customer.

### 5. Feature Transformation

`log1p()` transformation is applied to RFM features to reduce skewness and compress large values.

### 6. Feature Scaling

`StandardScaler` is used so that RFM features are on a comparable scale before applying K-Means.

### 7. K-Means Clustering

Different values of K are evaluated using:

- Elbow Method
- Silhouette Score
- Cluster size
- RFM profile differences
- Business interpretability

The final project uses **K = 4** clusters.

### 8. Customer Segment Profiling

The four clusters are interpreted using their average RFM values.

The resulting business segment names are:

- Recent High-Value Customers
- At-Risk Loyal Customers
- VIP High-Value Customers
- Low-Engagement Customers

### 9. Marketing Recommendations

Each segment receives a suitable marketing recommendation based on its customer behavior.

Examples include:

- Loyalty rewards
- Personalized product recommendations
- Re-engagement offers
- Personalized discounts
- Exclusive offers
- Premium rewards
- Early access to new products

## Streamlit Dashboard

The Streamlit dashboard provides:

- KPI cards
- Customer segment distribution
- RFM analysis charts
- Customer ID selection
- Selected customer RFM profile
- Cluster information
- Customer segment
- Marketing recommendation
- Customer-level segmentation table

The customer table displays all customer records.

## Project Files

```text
python project/
│
├── transactions.csv
├── cleaned_transactions.csv
├── rfm_customer_segments.csv
├── Untitled-1.ipynb
├── app.py
└── requirements.txt