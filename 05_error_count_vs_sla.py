"""
Project: SLA Intelligence Dashboard
Description: Analyzes impact of error frequency on SLA breaches
Author: V S M Preetham NAIDU
"""

import pandas as pd

# Load the dataset
df = pd.read_csv("customer_support_data.csv")

# Error_Count vs SLA performance (percentage)
error_sla = (
    df.groupby("Error_Count")["SLA_Met"]
    .value_counts(normalize=True)
    .mul(100)
    .reset_index(name="Percentage")
)

# Sort for clean reading
error_sla = error_sla.sort_values(
    by=["Error_Count", "SLA_Met"],
    ascending=[True, False]
)

# Display result
print(error_sla)

