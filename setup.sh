#!/bin/bash

echo "Downloading NLTK stopwords..."
python -m nltk.downloader stopwords

echo "Downloading spaCy English model..."
python -m spacy download en_core_web_sm
