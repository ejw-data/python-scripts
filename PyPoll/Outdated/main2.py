##########################################################################################
################################### Imports ##############################################

import os    # Module to create file paths across operating systems
import csv   # Module to read CSV files

##########################################################################################
######################### Data Extract / Create Dict #####################################

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Header row:  Voter ID,County,Candidate
    header_row = next(csvreader)
    dict_final={}

    # 
    for row in csvreader:
        k = row[2]   #index 2 - Candidate
        n = 1
        if k in dict_final.keys():
            dict_final[k] = dict_final[k] + n
        else:
            dict_final[k] = n  #dict_add could be replaced with 1
        
    ###################################################################
    ####################### Printout Dict #############################

    x_p = [] 
    x_p0 = '\nElection Results'
    x_p1 = '------------------------------------------'
    x_p2 = f'Total Votes:'
    x_p3 = '------------------------------------------'

    # print all key-value pairs via a loop
    for k, v in dict_final.items():
        print(f'{k}:  {v}', file=f)

    x_p5 = '------------------------------------------'
    
    # find and print the key of the max vote count
    max_value = max(dict_final.values())
    max_keys = [k for k, v in dict_final.items() if v == max_value] 
    if len(max_keys)>1:
        x_p6 = f'There was a tie with:  {max_keys}'
    else:
        x_p6 = f'Winner: {max_keys[0]}'
    x_p7 = '------------------------------------------'

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

###################################################################
######################## Data Check ###############################

# Module to do math calculations and check above calculation
# import pandas as pd 
# import numpy as np

# file_one = "Resources/election_data.csv"
# file_one_df = pd.read_csv(file_one, encoding="ISO-8859-1")

# output=file_one_df["Candidate"].value_counts()

# print(f'')
# print(f'Election Results')
# print(f'------------------------------------------')
# print(f'Total Votes:')
# print(f'------------------------------------------')
# print(output)
# print(f'------------------------------------------')
