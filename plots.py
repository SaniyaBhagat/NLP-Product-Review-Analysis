import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"c:\Users\bhaga\OneDrive\Desktop\NLP\NLP-Project\src\final_reviews.csv", encoding='utf-8')

#  1 — SENTIMENT PIE CHART

sent_counts = df['sentiment'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(sent_counts.values, labels=sent_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Sentiment Distribution (Pie Chart)")
plt.tight_layout()
plt.show()

### 2 — TOPIC BAR CHART
df['topic_id'].value_counts().plot(kind='bar')
plt.title("Topic Distribution")
plt.xlabel("Topic ID")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
