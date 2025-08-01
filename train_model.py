from xgboost import XGBRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import numpy as np
import joblib

df = pd.read_csv("data/player_data.csv")

features = ['Age', 'Season', 'AVG', 'HR', 'RBI', 'wRC+', 'Hard%']
target = 'WAR'

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBRegressor()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

df_2026 = pd.read_csv("data/predictions.csv")
df_2026['Predicted_WAR'] = model.predict(df_2026[features])
df_2026 = df_2026.sort_values(by='Predicted_WAR', ascending=False)

df_2026.to_csv("Stat_Pred_with_War.csv", index=False)
print("Predictions with WAR saved to Stat_Pred_with_War.csv")
#joblib.dump(model, 'model/xgboost_model.joblib')