import pandas as pd
import sqlite3
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define SQLite database path
DATABASE_PATH = 'my_database.db'

def fetch_data():
    try:
        query = "SELECT * FROM raw_data;" 
        # Establish a connection to the SQLite database
        conn = sqlite3.connect(DATABASE_PATH)
        df = pd.read_sql(query, conn)
        conn.close() 
        logger.info("Data fetched successfully.")
        return df
    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        raise

def cleanse_data(df):
    try:
        df = df.drop_duplicates()
        df = df.fillna(method='ffill')
        logger.info("Data cleaned successfully.")
        return df
    except Exception as e:
        logger.error(f"Error cleansing data: {e}")
        raise

def transform_data(df):
    try:
        df.columns = [col.lower().replace(' ', '_') for col in df.columns]
        logger.info("Data transformed successfully.")
        return df
    except Exception as e:
        logger.error(f"Error transforming data: {e}")
        raise

def save_data(df):
    try:
        # Save the cleaned and transformed data back into the SQLite database
        conn = sqlite3.connect(DATABASE_PATH)
        df.to_sql('cleaned_data', conn, if_exists='replace', index=False)
        conn.close()
        logger.info("Data saved successfully.")
    except Exception as e:
        logger.error(f"Error saving data: {e}")
        raise

def export_data_to_csv(df):
    df.to_csv('../data/cleaned_data.csv', index=False)

if __name__ == "__main__":  
    try:
        data = fetch_data()
        cleaned_data = cleanse_data(data)
        transformed_data = transform_data(cleaned_data)
        save_data(transformed_data)
        
        export_data_to_csv(transformed_data)

    except Exception as e:
        logger.error(f"Script execution failed: {e}")
