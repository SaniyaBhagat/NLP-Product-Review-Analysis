import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

csv_path = r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\flipkart_reviews_translated.csv"
df = pd.read_csv(csv_path)

if 'clean_review' not in df.columns:
    raise ValueError("'clean_review' column not found in CSV")
if 'sentiment_score' not in df.columns:
    raise ValueError("'sentiment_score' column not found in CSV")

reviews = df['clean_review'].astype(str).tolist()
sentiments = df['sentiment_score'].tolist()

# Define diverse questions
questions = [
    "Does the product last long?",              # durability
    "How is the user experience?",              # usability/interface
    "Does it deliver good value for the price?",# value/pricing
    "Are there frequent technical issues?",     # issues/bugs
    "Would you recommend this product to others?" # overall recommendation
]

# Vectorize reviews using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(reviews)

# Function to get answer based on cosine similarity
def get_answer(question, tfidf_matrix, reviews, sentiments):
    q_vec = vectorizer.transform([question])
    cos_sim = cosine_similarity(q_vec, tfidf_matrix).flatten()
    
    # Take top 5 most similar reviews
    top_idx = cos_sim.argsort()[-5:][::-1]
    top_reviews = [reviews[i] for i in top_idx]
    avg_sentiment = np.mean([sentiments[i] for i in top_idx])
    
    # Create a concise answer by joining top review phrases
    answer = " | ".join(top_reviews)
    return answer, round(avg_sentiment, 2)

# Generate answers
results = []
for q in questions:
    answer, avg_sentiment = get_answer(q, tfidf_matrix, reviews, sentiments)
    results.append({
        "Question": q,
        "Answer": answer,
        "Avg_Sentiment": avg_sentiment
    })

# Save to CSV
output_path = r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\review_qa_results.csv"
df_results = pd.DataFrame(results)
df_results.to_csv(output_path, index=False)

print(f"QA results saved to {output_path}")
print(df_results)
