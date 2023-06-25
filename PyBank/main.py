# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Variable set up
total_months=0
total=0
average_change=0
greatest_increase=0
greatest_increase_date=""
greatest_decrease=0
greatest_decrease_date=""
changetotal=0
date_list=[]
profit_losses_list=[]
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #Store Headers
        headers=next(csvreader)
        #Place CSV data into lists
        for row in csvreader:
                date_list.append(row[0])
                profit_losses_list.append(row[1])
        #Set up intial variable for comparison 
        pastvalue=int(profit_losses_list[0])
        #Loop to populate variables with total and change data
        for i in range(len(profit_losses_list)):
                currentvalue=int(profit_losses_list[i])
                changetotal=currentvalue-pastvalue+changetotal
                if currentvalue-pastvalue>greatest_increase:
                       greatest_increase=currentvalue-pastvalue
                       greatest_increase_date=date_list[i]
                if currentvalue-pastvalue<greatest_decrease:
                       greatest_decrease=currentvalue-pastvalue
                       greatest_decrease_date=date_list[i]
                total_months=total_months + 1
                total=total+int(profit_losses_list[i])
                pastvalue=int(profit_losses_list[i])
        average_change=round(changetotal/(total_months-1),2)                     

#Reformat Date Strings
greatest_increase_date=greatest_increase_date.split("-")
greatest_decrease_date=greatest_decrease_date.split("-")
#Terminal Output
title=("Financial Analysis")
linebreak=("----------------------------")
str_total_months="Total Months: "+str(total_months)
str_total="Total: $"+str(total)
str_average_change="Average Change: $"+str(average_change)
str_greatest_increase="Greatest Increase in Profits: "+ greatest_increase_date[1] +"-" + greatest_increase_date[0] + " ($"+str(greatest_increase)+")"
str_greatest_decrease="Greatest Decrease in Profits: "+greatest_decrease_date[1]+"-"+greatest_decrease_date[0]+" ($"+str(greatest_decrease)+")"
output=[title,linebreak,str_total_months,str_total,str_average_change,str_greatest_increase,str_greatest_decrease]
for line in range(len(output)):
    print(output[line])
#Txt File Outupt
output_file = os.path.join("analysis","output.txt")
with open(output_file, "w") as datafile:
    
        for line in range(len(output)):
                datafile.write(output[line])
                datafile.write('\n')


