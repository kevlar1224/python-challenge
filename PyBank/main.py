import os
import csv

file_path = os.path.join("..","Files","02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")

date = []
profits_losses = []

with open(file_path,newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        date.append(row[0])
        profits_losses.append(row[1])

print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(len(date)-1))

sum_of_profits = 0
for i in range(1,len(profits_losses)):
    sum_of_profits += int(profits_losses[i])
print("Net Profits: $" + str(sum_of_profits))

sum_of_change = 0
list_of_change = []
for i in range(2,len(profits_losses)):
    monthly_change = int(profits_losses[i]) - int(profits_losses[i-1])
    sum_of_change += monthly_change
    list_of_change.append(monthly_change)
average_change = round(sum_of_change/(len(profits_losses)-2),2)
print("Average Monthly Change in Profits: $" + str(average_change))

max_change = max(list_of_change)
min_change = min(list_of_change)
month_of_max = date[list_of_change.index(max_change)+2]
month_of_min = date[list_of_change.index(min_change)+2]

print("Greatest Monthly Increase in Profits: " + str(month_of_max) + ", $" + str(max(list_of_change)))
print("Greatest Monthly Decrease in Profits: " + str(month_of_min) + ", $" + str(min(list_of_change)))

with open("Analysis Results.txt", "w+") as export_file:
    export_file.write("Financial Analysis\n")
    export_file.write("--------------------------\n")
    export_file.write("Total Months: " + str(len(date)-1) + "\n")
    export_file.write("Net Profits: $" + str(sum_of_profits) + "\n")
    export_file.write("Average Monthly Change in Profits: $" + str(average_change) + "\n")
    export_file.write("Greatest Monthly Increase in Profits: " + str(month_of_max) + ", $" + str(max(list_of_change)) + "\n")
    export_file.write("Greatest Monthly Decrease in Profits: " + str(month_of_min) + ", $" + str(min(list_of_change)) + "\n")