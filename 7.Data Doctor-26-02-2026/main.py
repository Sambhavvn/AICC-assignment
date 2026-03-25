import pandas as pd

df = pd.read_csv("data.csv")

df = df.drop_duplicates()

df = df.fillna({
    "Name": "Unknown",
    "Age": df["Age"].mean(),
    "Math": df["Math"].mean(),
    "Science": df["Science"].mean(),
    "English": df["English"].mean()
})

df["Name"] = df["Name"].str.strip().str.title()

print(df.head())
print("\nMissing values after cleaning:\n", df.isnull().sum())