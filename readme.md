# E-Commerce ETL Pipeline

## Project Overview

This project is a Python-based ETL pipeline built using Pandas, SQLAlchemy, and MySQL.

The pipeline reads raw e-commerce order data from a CSV file, cleans and transforms the data, performs data quality validation, and loads the processed data into a MySQL database for analysis.

## ETL Workflow

```text
Raw CSV
   ↓
Python / Pandas
   ↓
Data Cleaning
   ↓
Data Transformation
   ↓
Data Quality Validation
   ↓
SQLAlchemy
   ↓
MySQL
   ↓
SQL Analysis
```

## Technologies Used

* Python
* Pandas
* SQLAlchemy
* PyMySQL
* MySQL
* Python-dotenv

## Project Structure

```text
Project/
│
├── ecommerce_orders_raw_500.csv
├── data.py
├── db_connection.py
├── load_to_db.py
├── read_from_db.py
├── main.py
├── .env
└── README.md
```

## Data Cleaning

The pipeline performs the following cleaning operations:

* Removes invalid quantities
* Removes invalid unit prices
* Removes invalid discount values
* Replaces missing discounts with `0`
* Standardizes city names
* Removes extra spaces from product names
* Handles missing payment methods
* Handles missing customer names using customer ID mappings
* Converts order dates into datetime format
* Removes invalid dates
* Removes duplicate rows

## Data Transformation
678
The pipeline creates additional columns for analysis:

* `Discount_Amount`
* `Total_Amount`
* `Order_Month`
* `Order_Year`
* `Order_Month_Name`
* `Year_Month`
* `Net_Amount`

## Data Quality Validation

Before loading the data into MySQL, the pipeline checks:

* Missing values
* Duplicate rows
* Invalid quantities
* Invalid unit prices
* Invalid discounts
* Incorrect total amount calculations
* Incorrect net amount calculations

The pipeline contains a data quality gate that stops the load when validation fails.

## Final Dataset

After processing:

```text
Rows: 478
Columns: 19
Missing values: 0
Duplicate rows: 0
Invalid Quantity: 0
Invalid Unit_Price: 0
Invalid Discounts: 0
Incorrect Total Amounts: 0
Incorrect Net Amounts: 0
```

## Database Loading

The cleaned DataFrame is loaded into the MySQL `orders` table using Pandas `to_sql()` and SQLAlchemy.

The pipeline also verifies that the number of rows in MySQL matches the number of rows loaded from Python.

## SQL Analysis

The MySQL data was analyzed using queries for:

* Total revenue
* Revenue by category
* Revenue by product
* Revenue by city
* Monthly revenue
* Orders by status
* Orders by payment method
* Units sold by category
* Average order value
* Revenue per unit
* Top customers by revenue

## How to Run

Make sure MySQL is running and the database credentials are configured in `.env`.

Run the complete ETL pipeline using:

```bash
python main.py
```

`main.py` acts as the entry point and automatically runs the data processing and database loading steps.

## Key Learning Outcomes

This project helped build practical experience with:

* Python and Pandas
* SQL
* MySQL
* SQLAlchemy
* ETL pipeline design
* Data cleaning
* Data transformation
* Data quality validation
* Parameterized SQL queries
* Database interaction from Python
* Basic pipeline error handling
* Python logging
* Reusable functions
