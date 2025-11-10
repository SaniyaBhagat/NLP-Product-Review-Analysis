import pandas as pd
from googletrans import Translator

# Load CSV
file_path = r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\flipkart-reviews.csv"

df = pd.read_csv(file_path)

translator = Translator()

def detect_language(text):
    text = str(text).lower()
    hindi_keywords = ["hai","tha","thi","kya","ka ","ki ","mein","hain","mat","nahi","bhi","se","tha ","tha"]
    count = sum([1 for w in hindi_keywords if w in text])
    if count >= 2:
        return "Hindi"
    return "English"


detected_languages = []
translated_reviews = []

for review in df["Review"]:
    if pd.isna(review):
        detected_languages.append("Unknown")
        translated_reviews.append("")
        continue

    lang = detect_language(review)
    detected_languages.append(lang)

    if lang == "Hindi":
        try:
            translated = translator.translate(review, src='hi', dest='en').text
        except:
            translated = ""
        translated_reviews.append(translated)
    else:
        translated_reviews.append(review)  # English stays same


df["Detected_Language"] = detected_languages
df["Translated_Review"] = translated_reviews

output_path = r"C:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\flipkart_reviews_translated.csv"
df.to_csv(output_path, index=False)

print("✅ Translation Completed")
print("Saved at:", output_path)
