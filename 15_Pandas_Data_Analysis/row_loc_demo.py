import pandas as pd

data = {
    "Name": ["Sohan", "Rahul", "Amit"],
    "Age": [20, 21, 22]
}

df = pd.DataFrame(data)

print(df.loc[0])

print()

print(df.loc[1])

print()

print(df.loc[2])