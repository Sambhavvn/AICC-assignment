import re
import pandas as pd
import emoji

df = pd.read_csv("sentences.csv")

sentences = df["text"].tolist()

slang_dict = {
"omg":"oh my god","idk":"i do not know","brb":"be right back","lol":"laugh",
"af":"very","wtf":"what the hell","pls":"please","plz":"please","gr8":"great",
"hv":"have","nyc":"nice","u":"you","r":"are","d":"the","tmrw":"tomorrow",
"smh":"disappointed","rn":"right now","thx":"thanks","k":"okay"
}

stop_words = {"i","me","my","we","you","he","she","it","is","are","was","were","a","an","the","and","or","but","if","to","of","in","on","for","with"}

def simple_spell(word):
    corrections = {
        "gud":"good","beleive":"believe","happend":"happened","doin":"doing",
        "tiredd":"tired","ths":"this","nt":"not","wrking":"working",
        "dis":"this","vry":"very","luv":"love","mrng":"morning","cm":"come"
    }
    return corrections.get(word, word)

def preprocess(text):
    text = text.lower()
    text = emoji.demojize(text)
    text = re.sub(r':[a-z_]+:', ' ', text)
    words = text.split()
    words = [slang_dict[w] if w in slang_dict else w for w in words]
    words = [simple_spell(w) for w in words]
    text = " ".join(words)
    text = re.sub(r'[^a-z\s]', ' ', text)
    tokens = text.split()
    tokens = [w for w in tokens if w not in stop_words]
    return tokens

df["processed"] = df["text"].apply(preprocess)

for i, row in df.iterrows():
    print(f"\nSentence {i+1}:")
    print("Original:", row["text"])
    print("Processed:", row["processed"])