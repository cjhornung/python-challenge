# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Variable set up
total_months=0
total=0
average_change=0
greatest_increase=0
greatest_increase_date=""
greatest_decrease=0
greatest_decrease_date=""

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader, None)
        for row in csvreader:
                total_months=total_months + 1
                total=total+int(row[1])
                             



print("Financial Analysis")
print("----------------------------")
str_total_months="Total Months: "+str(total_months)
str_total="Total: $"+str(total)
str_average_change="Average Change: $"+str(average_change)
str_greatest_increase="Greatest Increase in Profits: ($"+str(greatest_increase)+")"
str_greatest_decrease="Greatest Decrease in Profits: ($"+str(greatest_decrease)+")"
output=[str_total_months,str_total,str_average_change,str_greatest_increase,str_greatest_decrease]
for line in range(len(output)):
    print(output[line])
