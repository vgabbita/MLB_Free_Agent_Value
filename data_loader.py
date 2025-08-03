import pandas as pd
import pybaseball as pyb

df = pd.read_csv("data/player_name.csv")
data_2023 = pyb.batting_stats(2023, qual=50) # Load batting stats for 2023 season with a minimum of 50 at-bats
data_2024 = pyb.batting_stats(2024, qual=50) # Load batting stats for 2024 season with a minimum of 50 at-bats
data_2025 = pyb.batting_stats(2025, qual=50) # Load batting stats for 2025 season with a minimum of 50 at-bats
results = [] 

for index, row in df.iterrows():
    last_name = row['last_name']
    first_name = row['first_name']
    # Lookup player ID using pybaseball
    player_id = pyb.playerid_lookup(last_name, first_name)['key_mlbam']
    player_data_2023 = data_2023[data_2023['Name'] == f"{first_name} {last_name}"]
    player_data_2024 = data_2024[data_2024['Name'] == f"{first_name} {last_name}"]
    player_data_2025 = data_2025[data_2025['Name'] == f"{first_name} {last_name}"]
    pd.set_option('display.max_columns', None)
    if not player_data_2025.empty and not player_data_2024.empty and not player_data_2023.empty:
        # player_2023 = player_data_2023[['Name', 'Season', 'Age', 'AVG', 'HR', 'RBI', 'WAR', 'wRC+', 'Hard%']]
        # player_2024 = player_data_2024[['Name', 'Season', 'Age', 'AVG', 'HR', 'RBI', 'WAR', 'wRC+', 'Hard%']]
        # player_2025 = player_data_2025[['Name', 'Season', 'Age', 'AVG', 'HR', 'RBI', 'WAR', 'wRC+', 'Hard%']]
        results.append(player_data_2023.iloc[0])
        results.append(player_data_2024.iloc[0])
        results.append(player_data_2025.iloc[0])

if results:
    results_df = pd.DataFrame(results)
    results_df.to_csv("data/player_data.csv", index=False)
    print("Saved qualified players to data/players_data.csv")