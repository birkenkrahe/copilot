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

#print(qb_passing_yards)

'''
print the sum of the passing yards qb_passing_yards 
sorted by sum of passing yards in descending order  
Do not include Tom Brady because he wins too much
'''

# Initialize a dictionary to store the passing yards for each quarterback
qb_passing_yards = {}

# Loop over the rows in the data
for row in data:
    # Check if the player's position is "QB"
    if row['position '] == 'QB':
        # If the player is not yet in the dictionary, add them with their passing yards
        # If they are already in the dictionary, add their passing yards to their current total
        qb_passing_yards[row['player']] = qb_passing_yards.get(row['player'], 0) + row['pass_yds']

# Print the sum of the passing yards for each quarterback, sorted by sum of passing yards in descending order
# Do not include Tom Brady because he wins too much
qb_passing_yards = {k: v for k, v in sorted(qb_passing_yards.items(), key=lambda item: item[1], reverse=True)}
#print(qb_passing_yards)

# print only the top 5 (without Tom Brady) one per line
for i, (k, v) in enumerate(qb_passing_yards.items()):
    if i < 5 and k != 'Tom Brady':
        print(f'{k}: {v}')

# print the top 5 (without Tom Brady) in a table
import pandas as pd

# Create a DataFrame from the dictionary
df = pd.DataFrame.from_dict(qb_passing_yards, orient='index', columns=['pass_yds'])

# Sort the DataFrame by passing yards in descending order
df = df.sort_values(by='pass_yds', ascending=False)

# Print the top 5 (without Tom Brady) in a table
df[df.index != 'Tom Brady'].head()
