print("Financial Analysis")
print("----------------------------")
total_months=0
total=0
average_change=0
greatest_increase=0
greatest_decrease=0



str_total_months="Total Months: "+str(total_months)
str_total="Total: $"+str(total_months)
str_average_change="Average Change: $"+str(average_change)
str_greatest_increase="Greatest Increase in Profits: ($"+str(greatest_increase)+")"
str_greatest_decrease="Greatest Decrease in Profits: ($"+str(greatest_decrease)+")"
output=[str_total_months,str_total,str_average_change,str_greatest_increase,str_greatest_decrease]
for line in range(len(output)):
    print(output[line])
#print(f"Greatest Increase in Profits: "+str(total_months")
#print(f"Greatest Decrease in Profits: {total_months}")
#with open('pybank_results.txt', 'w') as f:
 #   f.write()
  #  close('pybank_results.txt')