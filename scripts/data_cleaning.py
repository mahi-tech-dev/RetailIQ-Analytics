# ==========================================
# RetailIQ Analytics
# Data Cleaning Script
# ==========================================

import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/superstore.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove completely empty rows
df = df.dropna(how='all')

# Save cleaned dataset
df.to_csv("data/processed/clean_superstore.csv", index=False)

print("Data cleaning completed successfully!")
print("Shape:", df.shape)