# MLB_Free_Agent_Value

This project builds a data-driven system to identify the **most valuable** offensive free agent in Major League Baseabll (MLB), using historical performance data, machine learning models, market valuation techniques, and aging based risk adjustment

## Objective
To estimate which free agents offer the highest **WAR-per-dollar** value and simulate market risk due to age, performance volatility, and contract costs. 
The final output is a ranked list of players with their projected WAR and value


## Project Structrue
MLB_Free_Agent_Value/
├── data/
│   ├── player_name.csv           # Input: first_name, last_name (for all free agents)
│   └── player_data.csv           # Raw performance stats
├── data_loader.py                # Scrapes and merges player stats (outputs player_data.csv)
├── 2026_proj.py 
├── train_model.py                      # Trains WAR projection model
├── market_val.py                  # Converts WAR to dollar value
├── predictions.csv                      # Orchestrates the full pipeline
├── Stat_Pred.csv                  # (Optional) Streamlit dashboard
├── market_val.csv                  #
└── README.md