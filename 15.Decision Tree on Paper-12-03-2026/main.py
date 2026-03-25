import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

df = pd.read_csv("tennis.csv")

le = LabelEncoder()

for col in df.columns:
    df[col] = le.fit_transform(df[col])

X = df.drop("Play", axis=1)
y = df["Play"]

model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

plt.figure(figsize=(10,6))
plot_tree(model, feature_names=X.columns, class_names=["No","Yes"], filled=True)
plt.show()

print(model.predict([[2,1,0,1]]))