import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("study.csv")

X = df[["Hours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

pred = model.predict([[7.5]])
print("Predicted marks for 7.5 hours:", pred[0])