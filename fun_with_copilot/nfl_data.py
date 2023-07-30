"""
Open the csv file called nfl_offensive_stats.csv, 
then read in the csv data from the file
"""
import csv
with open('nfl_offensive_stats.csv','r',encoding="utf-8") as f:
    nfl_reader = csv.reader(f)
    nfl_data = list(nfl_reader)
    print(nfl_data[0])

"""
In the data we just read in, the fourth column is the player's name.
and the 8th column is the number of passing yards for that player.
Get the sum of yards from column 8 where the 4th column value is 
'Aaron Rodgers'.
"""
total_passing_yards = 0
for row in nfl_data:
    if row[3] == "Aaron Rodgers":
        total_passing_yards += int(row[7])
print(total_passing_yards)