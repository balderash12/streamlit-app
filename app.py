
import streamlit as st
import re
import spacy
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

# Ensure stopwords are downloaded
nltk.download('stopwords')

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# --- Streamlit App UI ---
st.title("Text Processing App")
st.write("This app performs text normalization, sentiment analysis, and named entity recognition.")

# User input
raw_text = st.text_area("Enter text for analysis:", height=200)

# Normalize text
def normalize_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+|#\w+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
    return text

if raw_text:
    st.subheader("Normalized Text")
    normalized = normalize_text(raw_text)
    st.write(normalized)

    st.subheader("Sentiment Analysis")
    blob = TextBlob(raw_text)
    st.write(f"Polarity: {blob.sentiment.polarity:.2f}")
    st.write(f"Subjectivity: {blob.sentiment.subjectivity:.2f}")

    st.subheader("Named Entity Recognition")
    doc = nlp(raw_text)
    if doc.ents:
        for ent in doc.ents:
            st.markdown(f"- **{ent.text}** → *{ent.label_}*")
    else:
        st.write("No named entities found.")
