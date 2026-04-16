def financial_score(income, expenses):
    savings = income - expenses
    
    savings_ratio = savings / income
    
    score = savings_ratio * 100
    
    return round(score, 2)
