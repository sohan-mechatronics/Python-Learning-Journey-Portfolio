import pandas as pd

data = {
    "Name": ["Sohan", "Rahul", "Amit"],
    "Age": [20, 21, 22]
}

df = pd.DataFrame(data)

print(df.iloc[0])

print()

print(df.iloc[1])

print()

print(df.iloc[2])