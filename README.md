# Text Processing Streamlit App

This Streamlit app performs:

- Text normalization
- Sentiment analysis (using TextBlob)
- Named Entity Recognition (using spaCy)

## 🚀 How to Run

This app is deployed on [Streamlit Cloud](https://streamlit.io/cloud).

To run it locally:

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo

Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Run setup script:
bash setup.sh

Launch the app:
streamlit run app.py

🧠 Tech Stack
Streamlit
NLTK
TextBlob
spaCy