import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("final_reviews.csv", encoding='utf-8')

# 1) Sentiment distribution
df['sentiment'].value_counts().plot(kind='bar')
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment Class")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 2) Topic distribution
df['topic_id'].value_counts().plot(kind='bar')
plt.title("Topic Distribution")
plt.xlabel("Topic ID")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# 3) Wordcloud for adjectives
# assuming you stored top adjectives in column 'clean_review'
text = " ".join(df['clean_review'].astype(str))
wc = WordCloud(width=1200, height=600).generate(text)

plt.figure(figsize=(12,6))
plt.imshow(wc)
plt.axis("off")
plt.tight_layout()
plt.show()
