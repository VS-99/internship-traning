import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv("expenses.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Show total spent per category
category_summary = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
print("💰 Total spent by category:\n")
print(category_summary)

# Plot Pie Chart
plt.figure(figsize=(6, 6))
category_summary.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title("Expense Distribution by Category")
plt.ylabel("")  # Hide y-label
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()

# Plot Bar Chart
plt.figure(figsize=(8, 5))
category_summary.plot(kind='bar', color='skyblue')
plt.title("Total Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()
