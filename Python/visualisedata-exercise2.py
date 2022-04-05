churn_df = pd.read_csv("data/employee-churn.csv")
plt.scatter(churn_df['gpa'], churn_df['aptitude.score'], marker="*")
plt.show()