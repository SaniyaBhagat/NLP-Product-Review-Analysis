# import nltk

# nltk.download('wordnet', download_dir=r"C:\Users\bhaga\nltk_data")
# nltk.download('omw-1.4', download_dir=r"C:\Users\bhaga\nltk_data")

# print("✅ wordnet installed")


# import nltk

# # Optional: set a custom path for nltk_data
# nltk.data.path.append(r"C:\Users\bhaga\nltk_data")

# # Force download WordNet and Open Multilingual WordNet (required by lemmatizer)
# nltk.download('wordnet', download_dir=r"C:\Users\bhaga\nltk_data")
# nltk.download('omw-1.4', download_dir=r"C:\Users\bhaga\nltk_data")

# import nltk

# # Use custom download folder to avoid conflicts
# nltk.data.path.append(r"C:\Users\bhaga\nltk_data")

# # Force download WordNet and Open Multilingual WordNet
# nltk.download('wordnet', download_dir=r"C:\Users\bhaga\nltk_data")
# nltk.download('omw-1.4', download_dir=r"C:\Users\bhaga\nltk_data")

# Test WordNet
# from nltk.corpus import wordnet
# print(wordnet.synsets('good'))

# import nltk

# # Download required corpora and tokenizer
# nltk.download('punkt')      # sentence/token tokenizer
# nltk.download('stopwords')  # English stopwords
# nltk.download('wordnet')    # WordNet for lemmatizer

# preprocessing.py

# import nltk
# nltk.data.path.append(r"C:\Users\bhaga\nltk_data")

# from nltk.corpus import stopwords, wordnet

# print(stopwords.words('english')[:10])
# print(wordnet.synsets('good')[:5])


# import nltk
# nltk.data.path.append(r"C:\Users\bhaga\nltk_data\tokenizers")

# from nltk.tokenize import word_tokenize

# print(word_tokenize("Hello world! This is a test."))


# import nltk
# from nltk.tokenize import word_tokenize, sent_tokenize
# nltk.data.path.append(r"C:\Users\bhaga\nltk_data")

# text = "Hello world! This is a test."
# print(word_tokenize(text))
# print(sent_tokenize(text))
# from nltk.corpus import wordnet
# print(wordnet.synsets('good'))  # Should print synsets without errors

# import pandas as pd

# df = pd.read_csv(r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\flipkart_reviews_translated.csv")
# print(df.columns)


import nltk

# Download the POS tagger
nltk.download('averaged_perceptron_tagger')

# Optional: also download 'punkt' if not already done
nltk.download('punkt')

# Optional: for lemmatizer, if used
nltk.download('wordnet')
nltk.download('omw-1.4')
