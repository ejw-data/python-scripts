# import modules
import os
import csv

# add file path
path = os.path.join("Resources", "budget_data.csv")

# open file
with open(path) as file:
    # create rows as lists with values separated by commas
    csvreader = csv.reader(file, delimiter=",")

    # skip header row
    header = next(csvreader)

    # collect first row and initialize variables
    row1 = next(csvreader)
    prior_profit_loss = int(row1[1])
    prior_date = row1[0]

    # initilize datae and increase/decrease trackers
    greatest_increase = 0
    date_of_greatest_increase = prior_date
    greatest_decrease = 0
    date_of_greatest_decrease = prior_date

    # set aggregation variables
    total_months = 1
    total_profit_loss = prior_profit_loss
    total_changes = 0

    # loop through csv reader starting row 3
    for row in csvreader:

        # collect date and profit/loss
        current_date = row[0]
        current_profit_loss = int(row[1])
        
        # totalize profit/loss
        total_profit_loss += current_profit_loss

        # calculate month-to-month change
        change_profit_loss = current_profit_loss - prior_profit_loss

        # totalize month and change in profit/loss
        total_months += 1
        total_changes += change_profit_loss

        # re-initialize prior for next calculation
        prior_profit_loss = current_profit_loss
        
        # identify if current calc is new greatest increase
        if change_profit_loss > greatest_increase:
            greatest_increase = change_profit_loss
            date_of_greatest_increase = current_date

        # identify if current calc is new greatest decrease
        if change_profit_loss < greatest_decrease:
            greatest_decrease = change_profit_loss
            date_of_greatest_decrease = current_date  

# create summary 
output = (f'\n\nTotal Months: {total_months} \n'
          f'Average Profit Loss Changes: ${total_changes/(total_months-1):,.2f} \n'
          f'Total Profit Loss:  ${total_profit_loss:,} \n'
          f'Greatest Increase:  ${greatest_increase:,} on {date_of_greatest_increase} \n'
          f'Greatest Decrease: ${greatest_decrease:,} on {date_of_greatest_decrease} \n'
        )

# print summary
print(output)

with open('output.txt', 'w+') as file:
    file.write(output)
