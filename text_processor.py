"""
Text processing module for cleaning text, tokenizing, and counting word occurrences.
"""

import re
import logging

# Configure logging to display debug level messages
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

def clean_text(text):
    """
    Clean the input text by removing punctuation and converting to lowercase.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    assert isinstance(text, str), "Input must be a string"
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
    logging.debug("Cleaned text: %s...", cleaned_text[:50])
    return cleaned_text

def tokenize(text):
    """
    Tokenize the input text into a list of words.

    Args:
        text (str): The input text to be tokenized.

    Returns:
        list: A list of words.
    """
    assert isinstance(text, str), "Input must be a string"
    tokens = text.split()
    logging.debug("Tokens: %s...", tokens[:10])
    return tokens

def count_words(text):
    """
    Count the occurrences of each word in the input text.

    Args:
        text (str): The input text to count words from.

    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """
    assert isinstance(text, str), "Input must be a string"
    tokens = tokenize(clean_text(text))
    word_counts = {}
    for token in tokens:
        word_counts[token] = word_counts.get(token, 0) + 1
    logging.debug("Word counts: %s", dict(list(word_counts.items())[:10]))
    return word_counts
