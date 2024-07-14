import re
from collections import Counter

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Replace accented characters
    text = re.sub(r'[àáâãäå]', 'a', text)
    text = re.sub(r'[èéêë]', 'e', text)
    text = re.sub(r'[ìíîï]', 'i', text)
    text = re.sub(r'[òóôõö]', 'o', text)
    text = re.sub(r'[ùúûü]', 'u', text)
    text = re.sub(r'[ç]', 'c', text)
    text = re.sub(r'[ñ]', 'n', text)
    text = re.sub(r'[œ]', 'oe', text)
    text = re.sub(r'[æ]', 'ae', text)
    return text

def tokenize(text):
    # Split text into tokens
    tokens = text.split()
    return tokens

def count_words(text):
    # Clean the text
    text = clean_text(text)
    # Tokenize the text
    tokens = tokenize(text)
    # Count the frequency of each word
    word_count = Counter(tokens)
    return word_count

