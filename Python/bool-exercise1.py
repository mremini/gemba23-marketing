def get_loyalty_program(customer_spending_usd):
    status = "no status"
    if customer_spending_usd > 20000 and customer_spending_usd < 50000:
        status="gold"
    elif customer_spending_usd > 50000:
        status="platinum"
    else:
        status = "no status"
    return status