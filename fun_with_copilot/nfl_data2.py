'''
Code obtained from ChatGPT/GPT-4/Code Interpreter:
https://shareg.pt/h1hmCjr
'''

import pandas as pd

# Read the CSV file
nfl_data = pd.read_csv('nfl_offensive_stats.csv')
nfl_data.head()

# Convert the DataFrame to a list of dictionaries, each representing a row
data = nfl_data.to_dict('records')
data[:5]  # Display the first 5 rows

# Convert the DataFrame to a list of dictionaries, each representing a row
data = nfl_data.to_dict('records')
data[:5]  # Display the first 5 rows

# Initialize a dictionary to store the passing yards for each quarterback
qb_passing_yards = {}

# Loop over the rows in the data
for row in data:
    # Check if the player's position is "QB"
    if row['position '] == 'QB':
        # If the player is not yet in the dictionary, add them with their passing yards
        # If they are already in the dictionary, add their passing yards to their current total
        qb_passing_yards[row['player']] = qb_passing_yards.get(row['player'], 0) + row['pass_yds']

print(qb_passing_yards)

'''
This addition by Copilot:
sort the qb_passing_yards dictionary by the values (passing yards) in descending order
'''
sorted_qb_passing_yards = sorted(qb_passing_yards.items(), key=lambda x: x[1], reverse=True)
'''
print the top 10 quarterbacks by passing yards one per line and their passing yards
'''
for i in range(10):\
    print(sorted_qb_passing_yards[i][0], sorted_qb_passing_yards[i][1])