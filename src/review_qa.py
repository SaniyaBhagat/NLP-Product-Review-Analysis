# # review_qa.py

# import pandas as pd
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from collections import Counter
# import numpy as np

# # Load cleaned and translated reviews
# csv_path = r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\flipkart_reviews_translated.csv"
# df = pd.read_csv(csv_path)

# # Ensure 'Translated_Review' column exists
# if 'Translated_Review' not in df.columns:
#     raise ValueError("Column 'Translated_Review' not found in CSV.")

# reviews = df['Translated_Review'].dropna().astype(str).tolist()

# # Example sentiment scores column (assume you have it from previous analysis)
# # If not present, we'll simulate sentiment with random values for demonstration
# if 'sentiment_score' not in df.columns:
#     np.random.seed(42)
#     df['sentiment_score'] = np.random.uniform(low=-1, high=1, size=len(df))

# stop_words = set(stopwords.words('english'))

# # Define 5 customer questions and keywords
# qa_questions = {
#     "Is the battery life good?": ["battery", "charge", "charging"],
#     "Is the product durable?": ["durable", "sturdy", "scratch", "break"],
#     "Does it support fast charging?": ["fast", "quick", "charger", "charging"],
#     "How is the performance of the product?": ["performance", "speed", "slow", "lag"],
#     "Is the product value for money?": ["price", "expensive", "cheap", "worth", "value"]
# }

# qa_results = []

# for question, keywords in qa_questions.items():
#     # Filter reviews containing any keyword
#     relevant_reviews = []
#     sentiments = []
    
#     for review, score in zip(reviews, df['sentiment_score']):
#         tokens = [w.lower() for w in word_tokenize(review) if w.isalpha() and w.lower() not in stop_words]
#         if any(k in tokens for k in keywords):
#             relevant_reviews.append(review)
#             sentiments.append(score)
    
#     if relevant_reviews:
#         # Most common phrases (simple frequency-based summary)
#         all_tokens = [word for review in relevant_reviews for word in word_tokenize(review.lower()) if word.isalpha() and word not in stop_words]
#         most_common_words = [w for w, _ in Counter(all_tokens).most_common(10)]
#         summary_text = " ".join(most_common_words[:20])  # top 20 words as simple summary

#         avg_sentiment = np.mean(sentiments)
#     else:
#         summary_text = "No relevant reviews found."
#         avg_sentiment = np.nan
    
#     qa_results.append({
#         "Question": question,
#         "Answer": summary_text,
#         "Avg_Sentiment": avg_sentiment
#     })

# # Save QA results to CSV
# output_csv = r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\review_qa_results.csv"
# pd.DataFrame(qa_results).to_csv(output_csv, index=False)

# print(f"QA results saved to {output_csv}")



# review_qa.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load cleaned reviews with sentiment
csv_path = r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\flipkart_reviews_translated.csv"
df = pd.read_csv(csv_path)

# Ensure 'clean_review' and 'sentiment_score' exist
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
