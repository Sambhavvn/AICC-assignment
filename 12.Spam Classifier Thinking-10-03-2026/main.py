import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

df = pd.read_csv("spam.csv")

X = df["text"]
y = df["label"]

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

while True:
    msg = input("\nEnter message (or type 'exit'): ")
    if msg.lower() == "exit":
        break

    msg_vec = vectorizer.transform([msg])
    pred = model.predict(msg_vec)

    print("Prediction:", pred[0])