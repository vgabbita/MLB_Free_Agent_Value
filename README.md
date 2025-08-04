# MLB_Free_Agent_Value

This project builds a data-driven system to identify the **most valuable** offensive free agent in Major League Baseabll (MLB), using historical performance data, machine learning models, market valuation techniques, and aging based risk adjustment

## Objective
To estimate which free agents offer the highest **WAR-per-dollar** value and simulate market risk due to age, performance volatility, and contract costs. 
The final output is a ranked list of players with their projected WAR and value

## Key Features
- **Automated data collection** using `pybaseball`
- **XGBoost model** project WAR from recent performance trends
- **Market value modeling** using $8M/WAR minimum market rate
- **U-shaped aging risk model** to simulate player age-related decline 
- **Ranked CSV output** of projected values

## Project Structrue
MLB_Free_Agent_Value/
├── data/
│   ├── player_name.csv           # Input: first_name, last_name (for all free agents)
│   └── player_data.csv           # Raw performance stats
├── data_loader.py                # Scrapes and merges player stats (outputs player_data.csv)
├── 2026_proj.py                  # From the collected raw data, utiizes linear regression to predict the raw offensive stats for the 2026 season
├── train_model.py                # Trains WAR projection model; Uses that model to predict WAR values for the 2026 season
├── market_val.py                 # Converts predicted WAR to minimum 1 year salary per player with age adjusted risk
├── predictions.csv               # Contains each player's 2026 projections
├── Stat_Pred.csv                 # 2026 player projections with predicted WAR included
├── market_val.csv                # Ranked list of players based on their predicted WAR, with minimum 1 year salary included
└── README.md


## How to run
1. Input all free agents names into player_name.csv in the form `first_name, last_name`
2. Run `data_loader.py`
3. Run `2026_proj.py`
4. Run `train_model.py`
5. Run `market_val.py`
6. View `market_val.csv` to get the final list of most valuable offensive free agents