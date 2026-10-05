import logging
from load_to_db import load_data

# Config logging

logging.basicConfig(
    level=logging.INFO, 
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():

    logging.info("ETL Pipeline has Started")

    try:
        load_data()
        logging.info("ETL Pipeline Completed")

    except Exception as e:
        logging.error("ETL Pipeline failed")
        logging.error("Error: %s", e)

if __name__ == "__main__":
    run_pipeline()