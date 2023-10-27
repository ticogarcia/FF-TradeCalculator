"""
import csv
from datetime import datetime

# Input and output CSV filenames
input_filename = 'Player.2022.csv'
output_filename = 'Player.2022_modified.csv'
allowed_positions = ["QB", "RB", "TE", "WR"]
desired_columns = ['PlayerID', 'Name', 'Age', 'Team', 'Position']

def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, '%m/%d/%Y %I:%M:%S %p').date()
    today = datetime.today().date()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age - 1

# Read the CSV data
with open(input_filename, 'r') as infile:
    reader = csv.DictReader(infile)

    # Write the modified CSV data
    with open(output_filename, 'w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=desired_columns)
        writer.writeheader()
        
        for row in reader:
            # Check the allowed positions and status
            if row.get('Position') in allowed_positions and row.get('Status') != 'Inactive':
                # Create a new dictionary for the desired columns
                new_row = {col: row[col] if col != 'Name' and col != 'Age' else '' for col in desired_columns}
                new_row['Name'] = f"{row['FirstName']} {row['LastName']}"
                new_row['Age'] = calculate_age(row['BirthDate'])
                writer.writerow(new_row)

print(f"File '{input_filename}' was modified to '{output_filename}' with merged names.")
"""

"""
import pandas as pd

# Load the CSV files into dataframes
player_df = pd.read_csv('Player.2022_modified.csv')
season_df = pd.read_csv('PlayerSeason.2022.csv')

# Perform a full outer join on 'PlayerId'
merged_df = pd.merge(player_df, season_df, on='PlayerID', how='outer')
filtered_df = merged_df[merged_df['SeasonType'] == 1.0]

# Save the merged dataframe to a new CSV file
filtered_df.to_csv('Player.2022_merged.csv', index=False)

"""




import csv

input_filename = 'Player.2022_merged.csv'
output_filename = 'Player_2022.cleaned.csv'

# List of columns you want to keep
columns_to_keep = ['PlayerID', 'Name_x', 'Team_x', 'Position_x', 'Age', 'Played', 'Started', 'PassingCompletions', 'PassingAttempts', 'PassingYards', 'PassingTouchdowns', 
                   'PassingInterceptions', 'RushingAttempts', 'RushingYards', 'RushingYardsPerAttempt', 'RushingTouchdowns', 'ReceivingTargets', 'Receptions', 
                   'ReceivingYards', 'ReceivingYardsPerReception', 'ReceivingTouchdowns', 'FantasyPoints']  # Adjust this list as needed

rename_map = {
    'Name_x': 'Name',
    'Team_x': 'Team',
    'Position_x': 'Position'
}

with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=[rename_map.get(col, col) for col in columns_to_keep])

    writer.writeheader()
    for row in reader:
        # Skip rows where Name_x is empty
        if not row['Name_x'].strip():
            continue
        
        # Use dictionary comprehension to filter only the desired columns and rename them directly within the comprehension
        filtered_row = {rename_map.get(col, col): row[col] for col in columns_to_keep if col in row}
        writer.writerow(filtered_row)

print(f"Filtered columns saved to '{output_filename}'")



