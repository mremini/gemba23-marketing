my_linear_model = None
my_linear_model = linear_model.LinearRegression()
my_linear_model.fit(customer_annual_income_usd, avg_monthly_spending_usd)
predicted_values = my_linear_model.predict(customer_annual_income_usd)
plt.scatter(customer_annual_income_usd, avg_monthly_spending_usd, color="b")
plt.plot(customer_annual_income_usd, predicted_values, color="r")
plt.show()
r_squared = my_linear_model.score(customer_annual_income_usd, avg_monthly_spending_usd)