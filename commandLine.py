import csv
import difflib

def read_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def find_closest_name(input_name, players):
    names = [player['Name'] for player in players]
    closest_names = difflib.get_close_matches(input_name, names, n=1, cutoff=0.6)
    return closest_names[0] if closest_names else None

def get_player_data(input_name, players):
    for player in players:
        if player['Name'].lower() == input_name.lower():
            return player
    return None

def calculate(player_data):
    # Implement your calculation logic here
    pass

def main():
    players = read_csv('data/Player_2022.cleaned.csv')
    while True:
        player_name = input("Enter NFL player name: ")
        player_data = get_player_data(player_name, players)

        if player_data:
            calculate(player_data)
            break
        else:
            closest_name = find_closest_name(player_name, players)
            print(f"Player not found. Did you mean: {closest_name}? Try again.")

if __name__ == "__main__":
    main()
