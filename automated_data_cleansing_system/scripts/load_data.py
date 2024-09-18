import pandas as pd
import sqlite3

# Define the path to your SQLite database
DATABASE_PATH = 'my_database.db'

# Define the path to your CSV file
CSV_FILE_PATH = '../data/raw_data.csv'

def load_csv_to_sqlite():
    # Read the CSV file into a DataFrame
    df = pd.read_csv(CSV_FILE_PATH)
    
    # Connect to SQLite database
    conn = sqlite3.connect(DATABASE_PATH)
    
    # Load DataFrame into SQLite database
    df.to_sql('raw_data', conn, if_exists='replace', index=False)
    
    conn.close()
    print("Data loaded successfully.")

if __name__ == "__main__":
    load_csv_to_sqlite()
