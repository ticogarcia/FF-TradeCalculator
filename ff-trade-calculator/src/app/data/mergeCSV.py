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



import pandas as pd

# Load the CSV files into dataframes
player_df = pd.read_csv('Player.2022_modified.csv')
season_df = pd.read_csv('PlayerSeason.2022.csv')

# Perform a full outer join on 'PlayerId'
merged_df = pd.merge(player_df, season_df, on='PlayerID', how='outer')
filtered_df = merged_df[merged_df['SeasonType'] == 1.0]

# Save the merged dataframe to a new CSV file
filtered_df.to_csv('Player.2022_merged.csv', index=False)






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



import pandas as pd

def transform_position_column(csv_file_path, output_file_path):

    # Load the CSV file
    data = pd.read_csv(csv_file_path)

    # Define the mapping for the 'Position' column
    position_mapping = {'QB': 1.0, 'RB': 2.0, 'WR': 3.0, 'TE': 4.0}

    # Apply the transformation
    data['Pos'] = data['Pos'].map(position_mapping)

    # Save the modified DataFrame to a new CSV file
    data.to_csv(output_file_path, index=False)

    print(f"File saved successfully to {output_file_path}")

# Example usage
input_csv_file = 'Player_2022_cleaned_copy.csv'  # Replace with your input CSV file path
output_csv_file = 'Player_2022_cleaned_copy.csv'  # Replace with your desired output file name

transform_position_column(input_csv_file, output_csv_file)


"""

import pandas as pd


def remove_low_scoring_players(csv_input_path, csv_output_path, score_column='FantasyPoints', min_score=30):
    # Load the CSV file
    df = pd.read_csv(csv_input_path)

    # Filter out rows where the score is less than the minimum threshold
    df_filtered = df[df[score_column] >= min_score]

    # Save the filtered DataFrame to a new CSV file
    df_filtered.to_csv(csv_output_path, index=False)
    print(f"Filtered data saved to {csv_output_path}")


# Example usage
input_csv_file = 'Player_2022_cleaned_copy.csv'  # Replace with your input CSV file path
output_csv_file = 'Player_2022_cleaned_copy.csv'  # Replace with your desired output file name

remove_low_scoring_players(input_csv_file, output_csv_file, score_column='Total_Pts', min_score=30)
