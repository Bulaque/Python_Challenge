import os
import csv
import pandas as pd

budget_datacsv = os.path.join("..", "Resources","budget_data.csv").replace('\\','/')

print(f"current working dir: {os.getcwd()}")
print(f"csv path: {budget_datacsv}")
with open(budget_datacsv) as budget_sheet:
    
    budgetdata_reader = csv.reader(budget_sheet)
    heading = next(budgetdata_reader)

budget_df = pd.read_csv(budget_datacsv)

print(budget_df.head(5))

# Creating PyBank Analysis Title
print("Financial Analysis")
print("----------------------------------")

# Creating total months line

n_months = budget_df["Date"].nunique()
print(f"Total Months: {n_months}")

# Creating net total amount line

total_pnl = budget_df["Profit/Losses"].sum()
print(f"Total: {total_pnl}")

# Creating average change line

print("Average Change: No answer yet")

# Creating Greatest Increase in Profits line

print("Greatest Increase in Profits: No answer yet")

# Creating Greatest Decrease in Profits line

print("Greatest Decrease in Profits: No answer yet")
