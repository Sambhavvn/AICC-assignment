import re
import pandas as pd

df = pd.read_csv("data.csv", quotechar='"')

sentences = df["text"].tolist()

stop_words = {"i","me","my","we","you","he","she","it","is","are","was","were","a","an","the","and","or","but","if","to","of","in","on","for","with","this","how","from"}

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

df["processed"] = df["text"].apply(preprocess)

for i, row in df.iterrows():
    print(f"\nSentence {i+1}:")
    print("Original:", row["text"])
    print("Processed:", row["processed"])

df.to_csv("processed_data.csv", index=False)