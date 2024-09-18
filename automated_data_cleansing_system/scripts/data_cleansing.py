import pandas as pd
import sqlalchemy

# Define connection string for SQL database
DATABASE_URI = 'sqlite:///data.db'

def fetch_data():
    query = "SELECT * FROM raw_data;"
    engine = sqlalchemy.create_engine(DATABASE_URI)
    return pd.read_sql(query, engine)

def cleanse_data(df):
    df = df.drop_duplicates()
    df = df.fillna(method='ffill')
    return df

def transform_data(df):
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    return df

def save_data(df):
    engine = sqlalchemy.create_engine(DATABASE_URI)
    df.to_sql('cleaned_data', engine, if_exists='replace', index=False)

if __name__ == "__main__":
    data = fetch_data()
    cleaned_data = cleanse_data(data)
    transformed_data = transform_data(cleaned_data)
    save_data(transformed_data)
