import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data.csv")

df.columns = df.columns.str.strip()

print(df.columns)

X = df[["Size", "Bedrooms", "Age", "Distance"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

new_house = pd.DataFrame([[1500, 3, 2, 3]], columns=["Size", "Bedrooms", "Age", "Distance"])
pred = model.predict(new_house)

print("Predicted Price:", pred[0])