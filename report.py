import pandas as pd

df = pd.read_csv('cost_table.csv')

summary = df.groupby(df.columns[0]).sum()

summary.to_excel('report.xlsx')

print("Report generated")
