import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

avg_marks = df[["Math", "Science", "English"]].mean()

plt.figure()
avg_marks.plot(kind="bar")
plt.title("Average Marks per Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.show()

plt.figure()
avg_marks.plot(kind="pie", autopct="%1.1f%%")
plt.title("Subject Contribution")
plt.ylabel("")
plt.show()

plt.figure()
df["Math"].plot(kind="hist", bins=5)
plt.title("Distribution of Math Marks")
plt.xlabel("Marks")
plt.show()