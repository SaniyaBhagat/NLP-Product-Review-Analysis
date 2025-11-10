# preprocessing.py
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Set NLTK data path (update if different)
nltk.data.path.append(r"C:\Users\bhaga\nltk_data")

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Function to clean text
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Tokenize words
    tokens = word_tokenize(text)
    
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    
    # Lemmatize tokens
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return ' '.join(tokens)

# Load CSV (replace 'reviews.csv' with your file)
df = pd.read_csv(r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\flipkart-reviews.csv")

# Ensure the 'Review' column exists
if 'Review' not in df.columns:
    raise ValueError("CSV file must contain a 'Review' column.")

# Apply preprocessing
df['clean_review'] = df['Review'].astype(str).apply(clean_text)

# Save cleaned data
df.to_csv(r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\clean_reviews.csv", index=False)

print("Preprocessing complete. Cleaned data saved to 'clean_reviews.csv'.")
