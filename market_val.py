import pandas as pd
import numpy as np

DOL_PER_WAR = 8000000  # 2024 Offseason Average 
THRESHOLD_AGE = 29  # Age considered prime for baseball players


def age_adjusted_risk(age):
    return min(0.02*(age - THRESHOLD_AGE) ** 2 + 0.05, 0.7) 

df = pd.read_csv("Stat_Pred.csv")

df['market_val'] = df['Predicted_WAR'] * DOL_PER_WAR

df['market_val'] = np.where(df['market_val'] < 0, 0, df['market_val'])  # FIX THIS

df['risk'] = df["Age"].apply(age_adjusted_risk)   #age_adjusted_risk(df["Age"])  

# Calculate age adjusted market value
df['adjusted_val'] = df['market_val'] * (1 - df['risk'])

df_Salary= df[['Name', 'Age', 'Predicted_WAR', 'market_val', 'risk', 'adjusted_val']].round(2).copy()

df_Salary.to_csv("market_val.csv", index=False)
print("Market value predictions saved to market_val.csv")

