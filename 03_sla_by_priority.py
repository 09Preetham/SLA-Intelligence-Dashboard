import pandas as pd
df = pd.read_csv("customer_support_data.csv")



sla_priority = (
    df.groupby("Priority")["SLA_Met"]
    .value_counts(normalize=True)
    .rename("percentage")
    .mul(100)
    .reset_index()
)

print(sla_priority)
