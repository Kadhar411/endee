def generate_advice(category_spending, total):
    advice = []
    
    for category, amount in category_spending.items():
        percent = (amount / total) * 100
        
        if percent > 30:
            advice.append(f"High spending on {category}: {percent:.1f}%")
    
    return advice
