import pandas as pd

df = pd.read_csv("classroom.csv")

print(df.head())

numeric_cols = df.select_dtypes(include="number")
highest_col = numeric_cols.max().idxmax()
print("\nColumn with highest value:", highest_col)

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nBasic statistics:")
print(df.describe())