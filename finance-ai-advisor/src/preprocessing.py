import pandas as pd

def load_data(file_path):
    """
    Load CSV data
    """
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """
    Clean and preprocess the dataset
    """
    # Remove missing values
    df = df.dropna()

    # Convert date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Standardize category names (lowercase)
    df['category'] = df['category'].str.lower().str.strip()

    # Ensure amount is numeric
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

    # Drop rows where amount is still NaN
    df = df.dropna(subset=['amount'])

    return df


def add_features(df):
    """
    Add useful features for analysis
    """
    # Extract month and year
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    # Day of week
    df['day'] = df['date'].dt.day_name()

    return df


def preprocess_pipeline(file_path):
    """
    Full preprocessing pipeline
    """
    df = load_data(file_path)
    df = clean_data(df)
    df = add_features(df)
    
    return df
