"""
Project: SLA Intelligence Dashboard
Description: Analyzes impact of error frequency on SLA breaches
Author: V S M Preetham NAIDU
"""


import pandas as pd

df = pd.read_csv("customer_support_data.csv")

# Basic checks
print(df.shape)
print(df.info())
print(df.isnull().sum())

# Validate SLA logic
df["Calculated_SLA"] = df["TAT_Hours"] <= df["SLA_Hours"]
df["Calculated_SLA"] = df["Calculated_SLA"].map({True:"Yes", False:"No"})

print((df["Calculated_SLA"] == df["SLA_Met"]).value_counts())

