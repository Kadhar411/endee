import pandas as pd

def analyze_expenses(df):
    total = df['amount'].sum()
    category_spending = df.groupby('category')['amount'].sum()
    
    return total, category_spending
