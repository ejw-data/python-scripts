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

    #For Large Datasets:  to shorten I could sum the income in the loop by adding 'income = sum(row[1])' and count = sum(1 for row)'

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

    #Add code to print to text file
    #https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file-in-python-3/36571602
    #https://stackoverflow.com/questions/24204898/python-output-on-both-console-and-file/24206109#24206109
    #File_object = open(r"PyBank_Results","w")
    #file.write()
    #file.close()