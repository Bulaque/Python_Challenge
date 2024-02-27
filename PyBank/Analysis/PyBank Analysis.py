import csv
import os

budget_data = os.path.join("..", "Resources","budget_data.csv").replace('\\','/')

with open(budget_data) as budget_sheet:
    
    budgetdata_reader = csv.reader(budget_sheet)
    heading = next(budgetdata_reader)

total_months = 0
monthly_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]
net_total = 0

with open(budget_data) as fin_data:
    reader = csv.reader(fin_data)

    header = next(reader)

    first_row = next(reader)
    total_months += 1
    net_total += int(first_row[1])
    prev_net = int(first_row[1])


    for row in reader:

        total_months += 1 
        net_total += int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        monthly_change += [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Average Change
net_monthly_avg = sum(net_change_list)/len(net_change_list)

print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {net_total}")
print(f"Average Change: {round(net_monthly_avg,2)}")
print(f"Greatest Increase in profits: {greatest_increase}")
print(f"Greatest Decrease in profits: {greatest_decrease}")













