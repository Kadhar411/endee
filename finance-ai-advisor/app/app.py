import streamlit as st
import pandas as pd
from src.analysis import analyze_expenses
from src.model import financial_score
from src.advisor import generate_advice

st.title("💰 Personal Finance AI Advisor")

uploaded_file = st.file_uploader("Upload your expense CSV")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    income = st.number_input("Enter your monthly income")
    
    total, category_spending = analyze_expenses(df)
    score = financial_score(income, total)
    advice = generate_advice(category_spending, total)
    
    st.write("### Financial Health Score:", score)
    st.write("### Advice:")
    for a in advice:
        st.write("-", a)
