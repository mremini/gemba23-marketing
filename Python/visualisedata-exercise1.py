annual_income_usd = [100000, 130000, 40000, 50000, 120000, 48000, 50000,78000, 150000]
age_yrs = [60, 24, 32, 36, 28, 36, 32, 60, 68]
plt.scatter(age_yrs, annual_income_usd, marker="p", c="g")
plt.xlabel("Age (yrs)")
plt.ylabel("Annual Income (USD)")
plt.title("Annual Income vs. Age")