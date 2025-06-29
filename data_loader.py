import pandas as pd
import pybaseball as pyb

df = pd.read_csv("data/player_name.csv")
data = pyb.batting_stats(2025, qual=50) # Load batting stats for 2025 season with a minimum of 50 at-bats
results = [] 

for index, row in df.iterrows():
    last_name = row['last_name']
    first_name = row['first_name']
    # Lookup player ID using pybaseball
    player_id = pyb.playerid_lookup(last_name, first_name)['key_mlbam']
    player_data = data[data['Name'] == f"{first_name} {last_name}"]
    pd.set_option('display.max_columns', None)
    if not player_data.empty:
        #player = player_data[['Name', 'AVG', 'HR', 'RBI', 'WAR']]
        results.append(player_data.iloc[0])

if results:
    results_df = pd.DataFrame(results)
    results_df.to_csv("data/player_data.csv", index=False)
    print("Saved qualified players to data/player_data.csv")