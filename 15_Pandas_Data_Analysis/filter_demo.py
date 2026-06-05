import pandas as pd

df = pd.read_csv("students.csv")

result = df[df["Age"] > 20]

print(result)