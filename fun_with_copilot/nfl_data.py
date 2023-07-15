'''
open the csv file called nfl_offensive_stats.csv 
and read in the csv data from the file
'''
import csv  # import the csv module to read in the csv file 

# open the csv file called nfl_offensive_stats.csv
with open('nfl_offensive_stats.csv') as csv_file:
    # read in the csv data from the file
    csv_reader = csv.reader(csv_file, delimiter=',')
    # skip the header row
    next(csv_reader)
    # loop through each row in the csv file
    for row in csv_reader:
        # print out the row
        print(row)
