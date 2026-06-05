import pandas as pd

data = {
    "Name": ["Sohan", "Rahul", "Amit"],
    "Age": [20, 21, 22]
}

df = pd.DataFrame(
    data,
    index=["A", "B", "C"]
)

print(df)

print()

print(df.loc["B"])