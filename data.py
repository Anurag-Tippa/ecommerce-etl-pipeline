import pandas as pd

def pipeline_summary(clean_df):

    # Create a summary of the processed dataset
    summary = {
        "rows": len(clean_df),
        "columns": len(clean_df.columns),
        "total_revenue": round(clean_df["Net_Amount"].sum(), 2),
        "total_discount": round(clean_df["Discount_Amount"].sum(), 2),
        "total_units_sold": clean_df["Quantity"].sum()
    }

    return summary


def process_data():

    df = pd.read_csv("ecommerce_orders_raw_500.csv")

    # create a copy of the original dataset to clean
    clean_df = df.copy()


    # Handling invalid quantity
    clean_df = clean_df[clean_df["Quantity"] > 0]


    # Handling invalid unit_price
    clean_df = clean_df[clean_df["Unit_Price"] > 0]


    # Handling invalid discounts
    clean_df = clean_df[
        clean_df["Discount"].isna() |
        clean_df["Discount"].between(0, 1)
    ]

    # Handling missing discounts
    clean_df["Discount"] = clean_df["Discount"].fillna(0)


    # Clean Text cols

    # Inspect City
    # standardise capitalisation
    clean_df["City"] = clean_df["City"].str.title()

    # Handle missing city
    clean_df["City"] = clean_df["City"].fillna("Unknown")


    # Inspect Product col
    clean_df["Product"] = clean_df["Product"].str.strip()


    # Inspect Category


    # Inspect Payment_method
    # standardise both NAN and Unknown as Unknown
    clean_df["Payment_Method"] = clean_df["Payment_Method"].fillna("Unknown")


    # Inspect order_status


    # Inspect Customer name

    # There are different names for the same ID here which we cannot fill blindly,
    # hence filling the common id's
    name_mapping = {
        "CUST0093": "Aisha Khan",
        "CUST0107": "Sneha Iyer",
        "CUST0028": "Aisha Khan",
        "CUST0026": "Arjun Rao"
    }

    clean_df["Customer_Name"] = (
        clean_df["Customer_Name"]
        .fillna(clean_df["Customer_ID"].map(name_mapping))
        .fillna("Unknown")
    )


    # Check Order_date column for invalid date and data types

    clean_df["Order_Date"] = pd.to_datetime(
        clean_df["Order_Date"],
        errors="coerce"
    )

    # Remove rows wher the date is missing or invalid
    clean_df = clean_df.dropna(subset=["Order_Date"])


    # Check for duplicate orders

    # Drop duplicates
    clean_df = clean_df.drop_duplicates()




    ## TRANSFORMATION PHASE

    # Create a new column called as Total amount which has price with discount applied
    # Original Amount = Quantity × Unit_Price
    # Discount Amount = Original Amount × Discount
    # Total Amount    = Original Amount - Discount Amount

    clean_df["Discount_Amount"] = (
        clean_df["Quantity"]
        * clean_df["Unit_Price"]
        * clean_df["Discount"]
    )

    clean_df["Total_Amount"] = (
        clean_df["Quantity"]
        * clean_df["Unit_Price"]
        - clean_df["Discount_Amount"]
    )

    clean_df["Discount_Amount"] = clean_df["Discount_Amount"].round(2)
    clean_df["Total_Amount"] = clean_df["Total_Amount"].round(2)


    # Create Order_month column to check the sales of each month
    clean_df["Order_Month"] = clean_df["Order_Date"].dt.month


    # Create Order_Year column
    clean_df["Order_Year"] = clean_df["Order_Date"].dt.year


    # Create Month name instead of 1, 2 , 3... so that it becomes easier to understand
    clean_df["Order_Month_Name"] = (
        clean_df["Order_Date"].dt.month_name()
    )


    # Create year month column
    clean_df["Year_Month"] = (
        clean_df["Order_Date"].dt.to_period("M")
    )


    # Create a Column named as net amount
    clean_df["Net_Amount"] = clean_df["Total_Amount"]

    validate_data(clean_df)

    summary = pipeline_summary(clean_df)

    print("Pipeline Summary:")
    print(summary)

    return clean_df

def validate_data(clean_df):

    # Final Data Quality Validation
    missing_values = clean_df.isnull().sum()
    duplicate_rows = clean_df.duplicated().sum()

    # Validate Quantity
    invalid_quantity = (clean_df["Quantity"] <= 0).sum()

    # Validate Unit_Price
    invalid_unit_price = (clean_df["Unit_Price"] <= 0).sum()

    # Validate Discount
    invalid_discount = (
        (clean_df["Discount"] < 0) |
        (clean_df["Discount"] > 1)
    ).sum()

    # Check Total Amount calculation
    expected_total = (
        clean_df["Quantity"]
        * clean_df["Unit_Price"]
        * (1 - clean_df["Discount"])
    ).round(2)

    incorrect_total = (
        clean_df["Total_Amount"] != expected_total
    ).sum()

    # Check Net Amount calculation
    incorrect_net_amount = (
        clean_df["Net_Amount"] != clean_df["Total_Amount"]
    ).sum()

    # Data Quality Gate
    if (
        missing_values.sum() > 0
        or duplicate_rows > 0
        or incorrect_total > 0
        or incorrect_net_amount > 0
        or invalid_quantity > 0
        or invalid_unit_price > 0
        or invalid_discount > 0
    ):
        raise ValueError("Data quality validation failed")

    

    # Final Pipeline Health Check
    print("Data quality validation passed.")
    print("Data processing completed.")
    print("Rows:", len(clean_df))
    print("Columns:", len(clean_df.columns))
    print("Missing values:", missing_values.sum())
    print("Duplicate rows:", duplicate_rows)
    print("Invalid Quantity:", invalid_quantity)
    print("Invalid Unit_Price:", invalid_unit_price)
    print("Invalid Discounts:", invalid_discount)
    print("Incorrect Total Amounts:", incorrect_total)
    print("Incorrect Net Amounts:", incorrect_net_amount)

    

if __name__ == "__main__":
    process_data()