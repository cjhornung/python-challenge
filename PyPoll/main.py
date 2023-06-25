# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Variable set up

ballot_id=[]
county=[]
candidate=[]
candidate_unique=[]
total_votes=0
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #Skip Headers
        next(csvreader, None)
        #Place CSV data into lists
        for row in csvreader:
            ballot_id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])
        for i in range(len(candidate))
            total_votes=total_votes+1
            

str_total_months="Total Months: "+str(total_months)
total_votes="Total: $"+str(total)
str_average_change="Average Change: $"+str(average_change)
str_greatest_increase="Greatest Increase in Profits: "+ greatest_increase_date[1] +"-" + greatest_increase_date[0] + " ($"+str(greatest_increase)+")"
str_greatest_decrease="Greatest Decrease in Profits: "+greatest_decrease_date[1]+"-"+greatest_decrease_date[0]+" ($"+str(greatest_decrease)+")"
output=[str_total_months,str_total,str_average_change,str_greatest_increase,str_greatest_decrease]
for line in range(len(output)):
    print(output[line])
#Txt File Outupt
output_file = os.path.join("analysis","output.txt")
with open(output_file, "w") as datafile:
    
        for line in range(len(output)):
                datafile.write(output[line])
                datafile.write('\n')