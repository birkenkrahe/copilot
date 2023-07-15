'''
open the csv file called nfl_offensive_stats.csv, then read in the csv data from the file
'''
import csv
with open('fun_with_copilot/nfl_offensive_stats.csv','r',encoding="utf-8") as f:
    nfl_reader = csv.reader(f)
    nfl_data = list(nfl_reader)
    print(nfl_data[0])
