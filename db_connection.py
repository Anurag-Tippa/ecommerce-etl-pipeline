from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), ".env")) # finds and loads the .env file

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
)
if __name__ == "__main__": # the print statement runs only when the current .py is directly runs
    with engine.connect() as connection:
        print("MySQL connection successful!")