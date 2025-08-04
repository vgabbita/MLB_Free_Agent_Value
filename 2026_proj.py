#from xgboost import XGBRegressor
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import joblib 

df = pd.read_csv("data/player_data.csv")
features_to_project = df.select_dtypes(include=['number']).dropna(axis=1).columns.tolist()

features_to_project.remove('Season')  # Remove 'Season' as it is not a feature for prediction
features_to_project.remove('IDfg')  # Remove 'IDfg' as it is not a feature for prediction
features_to_project.remove('Age')  # Remove 'Age' as it is not a feature for prediction
features_to_project.remove('WAR')  # Remove 'WAR' as it is the target variable

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
            row[feature] = round(model.predict(np.array([[2026]]))[0], 2)
        else:
            row[feature] = y_values[-1]  # Use last known value if not enough data

    projected_features.append(row)


results_df = pd.DataFrame(projected_features)
results_df.to_csv("predictions.csv", index=False)
print("Predictions saved to predictions.csv")