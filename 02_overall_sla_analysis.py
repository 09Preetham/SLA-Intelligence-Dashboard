"""
Project: SLA Intelligence Dashboard
Description: Analyzes impact of error frequency on SLA breaches
Author: V S M Preetham NAIDU
"""

import pandas as pd

df = pd.read_csv("customer_support_data.csv")

sla_dist = df["SLA_Met"].value_counts(normalize=True) * 100
print(sla_dist)

