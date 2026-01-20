"""
Project: SLA Intelligence Dashboard
Description: Analyzes impact of error frequency on SLA breaches
Author: V S M Preetham NAIDU
"""

import pandas as pd

# Load the dataset
df = pd.read_csv("customer_support_data.csv")

# SLA performance by Team (percentage)
sla_by_team = (
    df.groupby("Team")["SLA_Met"]
    .value_counts(normalize=True)
    .mul(100)
    .reset_index(name="Percentage")
)

# Sort for readability
sla_by_team = sla_by_team.sort_values(
    by=["Team", "SLA_Met"],
    ascending=[True, False]
)

print(sla_by_team)

