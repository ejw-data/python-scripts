# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    date=[]  #index 0 - format string: 'Mmm-YYYY'
    net_income=[]  #index 1 - format double

    #Date,Profit/Losses
    header_row = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        net_income.append(row[1])  
    
    net_income_values = [float(x) for x in net_income]

    # #create dictionary
    # for key in dict:
    #     bank_data = {"month":month, "net_income": net_income}
    #       print(month, '-->', dict[key])
    #

    #list.index(element)

    tot_months = len(date)  
    tot_income = sum(net_income_values)
    aver_change = tot_income/tot_months
    greatest_profit = max(net_income_values)
    greatest_loss = min(net_income_values)

    print(f'')
    print(f'Financial Analysis')
    print(f'------------------------------------------')
    print(f'Total Months: {tot_months}')
    print(f'Total: {tot_income}')
    print(f'Average Change: {aver_change}')
    print(f'Greatest Increase in Profits: {date[net_income_values.index(greatest_profit)]}  {greatest_profit}')
    print(f'Greatest Decrease in Profits: {date[net_income_values.index(greatest_loss)]}  {greatest_loss}')