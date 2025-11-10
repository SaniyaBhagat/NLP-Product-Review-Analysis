import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import AgglomerativeClustering
import numpy as np

csv_path = r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\flipkart_reviews_translated.csv"
df = pd.read_csv(csv_path)

if 'clean_review' not in df.columns:
    print("Error: 'clean_review' column not found in CSV")
    exit()

reviews = df['clean_review'].astype(str).tolist()

vectorizer = TfidfVectorizer(stop_words='english')
review_vectors = vectorizer.fit_transform(reviews)

similarity_matrix = cosine_similarity(review_vectors)

n_clusters = 5  
clustering = AgglomerativeClustering(
    n_clusters=n_clusters,
    metric='cosine',  
    linkage='average'
)
cluster_labels = clustering.fit_predict(review_vectors.toarray())
df['cluster'] = cluster_labels

representative_reviews = []

for cluster in range(n_clusters):
    cluster_indices = np.where(cluster_labels == cluster)[0]
    cluster_vectors = review_vectors[cluster_indices]
    # Sum similarities within the cluster
    similarity_sums = cluster_vectors.dot(cluster_vectors.T).toarray().sum(axis=1)
    best_idx = cluster_indices[np.argmax(similarity_sums)]
    representative_reviews.append({
        'cluster': cluster,
        'representative_review': reviews[best_idx],
        'num_reviews_in_cluster': len(cluster_indices)
    })

# Save representative reviews to a separate DataFrame
summary_df = pd.DataFrame(representative_reviews)
summary_csv_path = r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\review_summary.csv"
summary_df.to_csv(summary_csv_path, index=False)

print(f"Review summarization completed. Summary saved at:\n{summary_csv_path}")
