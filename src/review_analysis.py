import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import ne_chunk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
import re
import numpy as np
from textblob import TextBlob


csv_path = r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\flipkart_reviews_translated.csv"
df = pd.read_csv(csv_path)

if 'Translated_Review' not in df.columns:
    raise KeyError("Column 'Translated_Review' not found in CSV.")

print("Creating 'clean_review' column...")
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # remove punctuation
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(t) for t in tokens if t not in stop_words]
    return ' '.join(tokens)

df['clean_review'] = df['Translated_Review'].fillna('').astype(str).apply(clean_text)


print("Performing POS tagging...")
all_tokens = [word_tokenize(r) for r in df['clean_review']]
all_tags = [pos_tag(tokens) for tokens in all_tokens]

# POS distribution
pos_counts = {}
for tags in all_tags:
    for word, tag in tags:
        pos_counts[tag] = pos_counts.get(tag, 0) + 1

pos_df = pd.DataFrame(list(pos_counts.items()), columns=['POS', 'Count']).sort_values(by='Count', ascending=False)
print("\nTop POS tags:\n", pos_df.head(10))

print("\n Performing NER...")
ner_results = [ne_chunk(tags) for tags in all_tags]


entities = []
for tree in ner_results:
    for subtree in tree:
        if hasattr(subtree, 'label'):
            entity = " ".join([token for token, pos in subtree.leaves()])
            entities.append((entity, subtree.label_))

entity_df = pd.DataFrame(entities, columns=['Entity', 'Type'])
print("\nTop entities:\n", entity_df['Entity'].value_counts().head(10))

print("Creating BoW and TF-IDF matrices...")
bow_vectorizer = CountVectorizer()
bow_matrix = bow_vectorizer.fit_transform(df['clean_review'])

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df['clean_review'])


print("Building Word2Vec embeddings...")
w2v_model = Word2Vec(sentences=all_tokens, vector_size=100, window=5, min_count=1, workers=4)

# Example: semantic similarity between two words
try:
    print("\nSemantic similarity between 'good' and 'excellent':", w2v_model.wv.similarity('good', 'excellent'))
except KeyError:
    print("Words not in vocabulary.")

print("Performing sentiment analysis...")
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df['sentiment_score'] = df['clean_review'].apply(get_sentiment)
print("\nSentiment distribution:\n", df['sentiment_score'].describe())


print("Performing LSA topic modeling...")
lsa_model = TruncatedSVD(n_components=5, random_state=42)
lsa_topic_matrix = lsa_model.fit_transform(tfidf_matrix)

terms = tfidf_vectorizer.get_feature_names_out()
for i, comp in enumerate(lsa_model.components_):
    terms_in_topic = [terms[idx] for idx in comp.argsort()[-10:][::-1]]
    print(f"Topic {i+1}: {', '.join(terms_in_topic)}")

print("Finding most similar words for key features...")
key_features = ['battery', 'camera', 'screen', 'price', 'performance']  # example
for feature in key_features:
    if feature in w2v_model.wv.key_to_index:
        similar_words = [word for word, score in w2v_model.wv.most_similar(feature, topn=5)]
        print(f"Top words similar to '{feature}': {similar_words}")


df.to_csv(csv_path, index=False)
print("\nAnalysis complete and CSV updated.")
