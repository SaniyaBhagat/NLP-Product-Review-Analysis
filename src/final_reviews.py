import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import pos_tag, word_tokenize
import spacy

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")


CSV_PATH =  r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\flipkart_reviews_translated.csv"
OUTPUT_CSV = r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\final_reviews.csv"
nltk.download("vader_lexicon")

nlp = spacy.load("en_core_web_sm")

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("vader_lexicon")

sia = SentimentIntensityAnalyzer()



def polarity_label(txt):
    txt = str(txt)            
    s = sia.polarity_scores(txt)["compound"]
    if s >= 0.05:
        return "Positive"
    elif s <= -0.05:
        return "Negative"
    else:
        return "Neutral"

def pos_counts(text):
    tokens = word_tokenize(str(text))
    tags = pos_tag(tokens)
    nn = sum(1 for t in tags if t[1].startswith("NN"))
    jj = sum(1 for t in tags if t[1].startswith("JJ"))
    vb = sum(1 for t in tags if t[1].startswith("VB"))
    return f"NN:{nn}, JJ:{jj}, VB:{vb}"


def ner_extract(text):
    doc = nlp(str(text))
    ents = [(ent.text, ent.label_) for ent in doc.ents]
    return str(ents)

df = pd.read_csv(CSV_PATH)

df["clean_review"] = df["clean_review"].astype(str).fillna("")


df["sentiment"] = df["clean_review"].apply(polarity_label)

df["pos_counts"] = df["clean_review"].apply(pos_counts)


df["ner"] = df["clean_review"].apply(ner_extract)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

NUM_TOPICS = 5
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["clean_review"])
svd = TruncatedSVD(n_components=NUM_TOPICS)
topic_matrix = svd.fit_transform(X)

df["topic_id"] = topic_matrix.argmax(axis=1)
df["topic_label"] = df["topic_id"].apply(lambda i: f"topic_{i}")

df.to_csv(OUTPUT_CSV, index=False)
print("DONE >> saved:", OUTPUT_CSV)
