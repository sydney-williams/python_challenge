#import python imports
import csv
import os

#read the csv and convert into a list
with open('Resources/budget_data.csv') as csvfile:
    data_reader = csv.reader(csvfile)
#read the header
    header = next(data_reader)
    data = list(data_reader)

 
 #calculate the total numbr of months 
months = len(data)

#calculate the net total amount 
net_total = 0
for x in data:
    net_total += int(x[1])

#calculate the average of the changes in "Profit/Losses" over the entire period
total_change = 0
revenue_list = []
for x in range(len(data)-1):
    month1 = int(data[x][1])
    month2 = int(data[x+1][1])
    change = month2 - month1 
    revenue_list.append(change)
    total_change += change 
average = total_change / (months - 1)

#calculate the increase of profits and decrease of losses 
max_profits = max(revenue_list)

min_profits = min(revenue_list)


Analysis = f"""Financial Analysis
----------------------------
Total Months: {months}
Total: {net_total}
Average  Change: {average}
Greatest Increase in Profits: {max_profits}
Greatest Decrease in Profits: {min_profits}"""
print(Analysis)