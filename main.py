# ==========================================
# RetailIQ Analytics
# Main Program
# ==========================================

import os

print("\n===================================")
print(" RetailIQ Analytics ")
print("===================================\n")

print("Step 1 : Running Data Cleaning...")
os.system("python scripts/data_cleaning.py")

print("\nStep 2 : Running Analysis...")
os.system("python scripts/analysis.py")

print("\nStep 3 : Generating Visualizations...")
os.system("python scripts/visualization.py")

print("\nStep 4 : Generating Business Report...")
os.system("python scripts/business_report.py")

print("\n===================================")
print(" Project Executed Successfully ")
print("===================================")