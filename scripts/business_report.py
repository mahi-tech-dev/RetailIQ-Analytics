# ==========================================
# RetailIQ Analytics
# Business Report
# ==========================================

import pandas as pd

df = pd.read_csv("data/processed/clean_superstore.csv")

report = []

report.append("===== RETAILIQ ANALYTICS REPORT =====\n")

report.append(f"Total Sales : {round(df['Sales'].sum(),2)}")
report.append(f"Total Profit : {round(df['Profit'].sum(),2)}")
report.append(f"Total Orders : {df['Order ID'].nunique()}")

report.append("\nHighest Sales Category:")
report.append(df.groupby('Category')['Sales'].sum().idxmax())

report.append("\nHighest Profit Region:")
report.append(df.groupby('Region')['Profit'].sum().idxmax())

report.append("\nTop Customer:")
report.append(df.groupby('Customer Name')['Sales'].sum().idxmax())


with open("reports/business_report.txt","w") as f:
    for line in report:
        f.write(str(line))
        f.write("\n")

print("Business report generated successfully.")