import logging
import pandas as pd

from data import process_data
from db_connection import engine


# Load database into SQL
def load_data():

    clean_df = process_data()

    if clean_df.empty:
        raise ValueError("No data available to load into the database")

    clean_df.to_sql(
        "orders",
        con=engine,
        if_exists="replace",
        index=False
    )

    # Check number of rows loaded into the database
    result = pd.read_sql(
        "SELECT COUNT(*) AS row_count FROM orders",
        con=engine
    )

    db_row_count = result["row_count"].iloc[0]

    # Compare DataFrame row count with database row count
    if db_row_count != len(clean_df):
        raise ValueError("Row count mismatch after loading")

    logging.info(
        "Loaded %d rows into orders table",
        db_row_count
    )


if __name__ == "__main__":
    load_data()