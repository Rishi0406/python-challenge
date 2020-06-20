#import libraries
import os
import csv

#csvpath to get data and output_path to publish result
csvpath = os.path.join('Resources','budget_data.csv')
output_path = os.path.join("analysis", "Financial Analysis.txt")

#define all variables
total_months = []
total_profit = []
monthly_change = []
greatest_increase_profit = []
greatest_decrease_profit = []
greatest_increase_month = ""
greatest_decrease_month = ""

#read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

#ignore header in counting
    header = next(csvreader)

    print("Financial Analysis")
    print("----------------------------")

#loop to read through each row and increase count of values
    #final_total to get total of all values from profits/losses

    for row in csvreader:
         
        months = row[0]
        profit = int(row[1])
         
        total_months.append(months)
        total_profit.append(profit)

        final_total = sum(total_profit)

#another loop to calculate change between each month and add them to obtain total value of change
    #calculate average change by dividing total of change with number of changes

    for i in range(len(total_profit)-1):

        change = total_profit[i+1]-total_profit[i]
         
        monthly_change.append(change) 

        average_change = sum(monthly_change)/len(monthly_change)

#calculate highest and lowest change and the month when it happened
    greatest_increase_profit = max(monthly_change)
    greatest_decrease_profit = min(monthly_change)

    greatest_increase_month = monthly_change.index(max(monthly_change))
    greatest_decrease_month = monthly_change.index(min(monthly_change))

#print results
print(f"Total Months: {len(total_months)}")
print(f"Total: {final_total}")
print(f"Average Change: {round(average_change,2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month+1]} (${greatest_increase_profit})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month+1]} (${greatest_decrease_profit})")

#write output in text file
with open(output_path, 'w') as txtfile:

    txtfile.writelines("Financial Analysis" + "\n")
    txtfile.writelines("----------------------------" + "\n")
    txtfile.writelines(f"Total Months: {len(total_months)} \n")
    txtfile.writelines(f"Total: {final_total} \n")
    txtfile.writelines(f"Average Change: {round(average_change,2)} \n")
    txtfile.writelines(f"Greatest Increase in Profits: {total_months[greatest_increase_month+1]} (${greatest_increase_profit}) \n")
    txtfile.writelines(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month+1]} (${greatest_decrease_profit}) \n")