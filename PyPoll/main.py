# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    id=[]  #index 0 - number
    county=[]  #index 1 - Singlestring
    candidate=[]  #index 2 - Lastname

    header_row = next(csvreader)

    for row in csvreader:
        id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
   #create dictionary of candidates and add each time they get a vote
   #https://www.geeksforgeeks.org/python-sum-list-of-dictionaries-with-same-key/
   #https://www.quora.com/How-do-I-sum-the-values-of-each-key-in-a-Python-dictionary-and-then-display-the-result-as-key-summed-value 


    print(f'')
    print(f'Election Results')
    print(f'------------------------------------------')
    print(f'Total Votes:')
    print(f'------------------------------------------')
    # replace this section with for loop
    print(f'Khan:')
    print(f'Correy:')
    print(f'Li:')
    print(f"O'Tooley:")
    print(f'------------------------------------------')
    print(f'Winner:')
    print(f'------------------------------------------')
