import pandas as pd
import re
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


nltk.data.path.append(r"C:\Users\bhaga\nltk_data")

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
 
    text = text.lower()
  
    text = re.sub(r'http\S+|www\S+', '', text)
    
    text = re.sub(r'[^a-z\s]', '', text)
   
    text = re.sub(r'\s+', ' ', text).strip()
    
    tokens = word_tokenize(text)
  
    tokens = [word for word in tokens if word not in stop_words]

    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return ' '.join(tokens)


df = pd.read_csv(r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\flipkart-reviews.csv")


if 'Review' not in df.columns:
    raise ValueError("CSV file must contain a 'Review' column.")

# Apply preprocessing
df['clean_review'] = df['Review'].astype(str).apply(clean_text)

# Save cleaned data
df.to_csv(r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\clean_reviews.csv", index=False)

print("Preprocessing complete. Cleaned data saved to 'clean_reviews.csv'.")
