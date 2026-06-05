import pandas as pd

df = pd.read_csv("students.csv")

print(df.sort_values("Age"))

print()

print(df.sort_values("Age", ascending=False))