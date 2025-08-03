#from xgboost import XGBRegressor
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import joblib 

df = pd.read_csv("data/player_data.csv")
#features_to_project = df.drop(columns = ["IDfg", "Season", "Team", "Name", "Age", "WAR", "Dol"]).columns.tolist()   #['AVG', 'HR', 'RBI', 'wRC+', 'Hard%']
features_to_project = df.select_dtypes(include=['number']).dropna(axis=1).columns.tolist()
#print(features_to_project)
#model = joblib.load('model/xgboost_model.joblib')

projected_features = []
for name, group in df.groupby('Name'):
    row = {'Name': name, 'Season': 2026}
    group = group.sort_values(by='Season')

    row['Age'] = group['Age'].max() + 1
    for feature in features_to_project:
        x_years = group['Season'].values.reshape(-1, 1)
        y_values = group[feature].values

        if len(y_values) >= 2: 
            model = LinearRegression()
            model.fit(x_years, y_values)
            row[feature] = model.predict(np.array([[2026]]))[0]
        else:
            row[feature] = y_values[-1]  # Use last known value if not enough data

    projected_features.append(row)


results_df = pd.DataFrame(projected_features)
results_df.to_csv("data/predictions.csv", index=False)
print("Predictions saved to data/predictions.csv")