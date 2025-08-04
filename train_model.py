from xgboost import XGBRegressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("data/player_data.csv")

features = df.select_dtypes(include=['number']).dropna(axis=1).columns.tolist()
features.remove('IDfg')  # Remove 'IDfg' as it is not a feature for prediction
features.remove('Season')  # Remove 'Season' as it is not a feature for prediction
features.remove('WAR')  # Remove 'WAR' as it is the target variable
target = 'WAR'

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = XGBRegressor()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

df_2026 = pd.read_csv("predictions.csv")
df_2026['Predicted_WAR'] = model.predict(df_2026[features])
df_2026 = df_2026.sort_values(by='Predicted_WAR', ascending=False)


df_2026.to_csv("Stat_Pred.csv", index=False)
print("Predictions with WAR saved to Stat_Pred.csv")