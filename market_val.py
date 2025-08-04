import pandas as pd
import numpy as np

DOL_PER_WAR = 8000000  # 2024 Offseason Average 
AVG_SAL = 4000000  # Average Salary in MLB
THRESHOLD_AGE = 29  # Age considered prime for baseball players


def age_adjusted_risk(age):
    """    Calculate risk based on age.
    The risk increases quadratically after a certain age threshold. Plateau at 0.7 after age 35.
    Args:
        age (int): Age of the player.
    """
    return min(0.02*(age - THRESHOLD_AGE) ** 2 + 0.05, 0.7) 

df = pd.read_csv("Stat_Pred.csv")

df['market_val'] = df['Predicted_WAR'] * DOL_PER_WAR

# Replace negative market values with the average salary adjusted for risk
df['market_val'] = np.where(df['market_val'] < 0, AVG_SAL, df['market_val'])  

df['risk'] = df["Age"].apply(age_adjusted_risk)  

# Calculate age adjusted market value
df['1_year_salary'] = df['market_val'] * (1 - df['risk'])

df_Salary= df[['Name', 'Age', 'Predicted_WAR', '1_year_salary']].round(2).copy()

print("The most valuable player is", df_Salary.loc[0, 'Name'], "with a minimum 1 year salary of $", df_Salary.loc[0, '1_year_salary'])

df_Salary.to_csv("market_val.csv", index=False)
print("\nMarket value predictions saved to market_val.csv")

