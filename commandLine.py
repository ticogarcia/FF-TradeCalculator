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

def find_similar_players(player_data, players):
    total_pts = float(player_data['Total_Pts'])
    prediction = float(player_data['Predictions'])

    similar_players = []
    for player in players:
        player_total_pts = float(player['Total_Pts'])
        player_prediction = float(player['Predictions'])

        if total_pts - 40 <= player_total_pts <= total_pts + 40 and player_prediction > prediction:
            similar_players.append(player)

    # Sort by 'Predictions' in descending order
    similar_players_sorted = sorted(similar_players, key=lambda x: float(x['Predictions']), reverse=True)

    # Select top 10 players adhering to the 'POS' constraint
    top_players = []
    pos_count = 0
    for player in similar_players_sorted:
        if len(top_players) >= 10:
            break
        if player['Pos'] == '1.0':
            if pos_count < 3:
                top_players.append(player)
                pos_count += 1
        else:
            top_players.append(player)

    return [player['Name'] for player in top_players]

def calculate(player_data, players):
    similar_players = find_similar_players(player_data, players)
    if similar_players:
        print("Top 10 players with higher predictions within a 40 point range:")
        for name in similar_players:
            print(name)
    else:
        print("No similar players found.")

def main():
    players = read_csv('data/predictions.csv')
    while True:
        player_name = input("Enter NFL player name: ")
        player_data = get_player_data(player_name, players)

        if player_data:
            calculate(player_data, players)
            break
        else:
            closest_name = find_closest_name(player_name, players)
            if closest_name:
                print(f"Player not found. Did you mean: {closest_name}? Try again.")
            else:
                print("Player not found. Try again.")

if __name__ == "__main__":
    main()
