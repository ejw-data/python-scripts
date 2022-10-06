##########################################################################################
################################### Imports ##############################################

import os   # Module creates file paths across operating systems
import csv  # Module for reading CSV files

##########################################################################################
######################### Data Extract / Prep ############################################

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Header row:  Date,Profit/Losses
    header_row = next(csvreader)

    # Initialize lists
    date=[]  #index 0 - format string: 'Mmm-YYYY', Date
    net_income=[]  #index 1 - format double, Profit/Loss
    change_profit=[]  #difference between profit per month

    for row in csvreader:
        date.append(row[0])
        net_income.append(float(row[1]))    #convert strings to numbers
    #For Large Datasets I should calc in the for row loop and only use row[1] to calc everything

    #This code determines the difference between profits per month
    #If I was to manually calculate difference it would look like:  [0, #, #, #, #, etc.]
    #So if I grab the first value and subtract it from first value and then reset the next value
    #then I get the desired list.
    prev_val=net_income[0]
    for x in net_income:
        change = x - prev_val
        change_profit.append(change)
        prev_val=x 


    ######################################################################################
    ############################# Calculations ###########################################

    tot_months = len(date)  
    tot_income = sum(net_income)
    tot_change_profit = sum(change_profit)
    aver_change = round(tot_change_profit/(tot_months-1),1)
    greatest_profit = max(change_profit)
    greatest_loss = min(change_profit)

    #####################################################################################
    ########################### Setup Messaging Text ####################################
    x_p = []
    x_p0 = '\nFinancial Analysis'
    x_p1 = '------------------------------------------'
    x_p2 = f'Total Months:  {tot_months}'
    x_p3 = f'Total:  ${tot_income}'
    x_p4 = f'Average Change:  ${aver_change}'
    x_p5 = f'Greatest Increase in Profits:  {(date[change_profit.index(greatest_profit)])} (${greatest_profit})'
    x_p6 = f'Greatest Decrease in Profits:  {(date[change_profit.index(greatest_loss)])} (${greatest_loss})'
    
    # List of print text
    x_p = [x_p0, x_p1, x_p2, x_p3, x_p4, x_p5, x_p6]
 
    ####################################################################################
    ########################## Print Outputs ###########################################

    # Print to terminal
    for x in x_p:
        print(x)

    # Print to text document
    f = open('output.txt',"w+")
    for x in x_p:
        print(x, file=f)
    f.close()