import os
import csv

budget_datacsv = os.path.join("..","Resources","budget_data.csv").replace('\\','/')

# Creating PyBank Analysis Title
print("Financial Analysis")
print("----------------------------------")

with open(budget_datacsv) as budget_sheet:
    
# Creating Total Months line
    budgetdata_reader = csv.reader(budget_sheet)
    heading = next(budgetdata_reader)

print(budget_sheet)

# Creating Net Total Amount line
   
# Creating Average Change line
# Creating Greatest Increase in Profits line
# Creating Greatest Decrease in Profits line
