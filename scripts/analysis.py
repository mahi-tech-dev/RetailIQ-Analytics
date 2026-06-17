# ==========================================
# RetailIQ Analytics
# Sales Analysis
# ==========================================

import pandas as pd

df = pd.read_csv("data/processed/clean_superstore.csv")

print("========== BUSINESS METRICS ==========")

print("Total Sales:", round(df['Sales'].sum(), 2))

print("Total Profit:", round(df['Profit'].sum(), 2))

print("Total Orders:", df['Order ID'].nunique())

print("Top Category:")
print(df.groupby('Category')['Sales'].sum().sort_values(ascending=False))

print("\nTop Region:")
print(df.groupby('Region')['Sales'].sum().sort_values(ascending=False))