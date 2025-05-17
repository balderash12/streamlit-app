# %%
#%pip uninstall -y numpy thinc spacy torch


# %%
%pip install numpy==1.26.4
%pip install torch==2.2.2
%pip install spacy==3.7.2 thinc==8.2.2
%pip install nltk textblob


# %%
!python -m spacy download en_core_web_sm


# %%
import re
import spacy
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

# Download nltk stopwords if not already done
nltk.download('stopwords')

# Load spaCy model for NER
nlp = spacy.load('en_core_web_sm')

# Sample raw text (e.g. customer review or tweet)
raw_text = """
I LOVE this product!!! 😍😍 It's amazing. Bought it from Amazon last week. 
Delivery was quick. Highly recommended. #happycustomer @amazon
"""

# 1. Text Normalization
def normalize_text(text):
    # Lowercase
    text = text.lower()
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    # Remove emojis and special characters (basic)
    text = re.sub(r'[^\w\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in text.split() if w not in stop_words]
    return ' '.join(filtered_words)

normalized_text = normalize_text(raw_text)
print("Normalized Text:", normalized_text)

# 2. Named Entity Recognition (NER)
doc = nlp(normalized_text)
entities = [(ent.text, ent.label_) for ent in doc.ents]
print("Named Entities:", entities)

# 3. Sentiment Analysis
sentiment = TextBlob(normalized_text).sentiment
print(f"Sentiment Polarity: {sentiment.polarity:.3f}, Subjectivity: {sentiment.subjectivity:.3f}")

# Validate sentiment
if sentiment.polarity > 0:
    print("Overall Sentiment: Positive")
elif sentiment.polarity < 0:
    print("Overall Sentiment: Negative")
else:
    print("Overall Sentiment: Neutral")


# %%
import re
import spacy
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Text normalization function
def normalize_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+|#\w+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in text.split() if w not in stop_words]
    return ' '.join(filtered_words)

# Interactive loop
while True:
    print("\n--- Text Analytics Interactive Tool ---")
    user_input = input("Enter your text (or type 'exit' to quit):\n> ")

    if user_input.lower() == 'exit':
        break

    normalized_text = normalize_text(user_input)
    print("\nNormalized Text:", normalized_text)

    doc = nlp(normalized_text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print("Named Entities:", entities if entities else "No named entities found.")

    sentiment = TextBlob(normalized_text).sentiment
    print(f"Sentiment Polarity: {sentiment.polarity:.3f}, Subjectivity: {sentiment.subjectivity:.3f}")

    if sentiment.polarity > 0:
        print("Overall Sentiment: Positive")
    elif sentiment.polarity < 0:
        print("Overall Sentiment: Negative")
    else:
        print("Overall Sentiment: Neutral")


# %%



