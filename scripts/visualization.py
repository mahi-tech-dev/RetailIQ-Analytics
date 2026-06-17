# ==========================================
# RetailIQ Analytics
# Visualization Script
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("data/processed/clean_superstore.csv")

# ---------------------------
# Sales by Category
# ---------------------------

sales_by_category = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(8,5))
sales_by_category.plot(kind='bar')

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("charts/sales_by_category.png")
plt.close()


# ---------------------------
# Region-wise Sales
# ---------------------------

region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind='bar')

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("charts/region_sales.png")

plt.close()


# ---------------------------
# Sales Distribution
# ---------------------------

plt.figure(figsize=(8,5))

sns.histplot(df['Sales'], bins=30)

plt.title("Sales Distribution")

plt.tight_layout()

plt.savefig("charts/sales_distribution.png")

plt.close()

print("Charts generated successfully.")