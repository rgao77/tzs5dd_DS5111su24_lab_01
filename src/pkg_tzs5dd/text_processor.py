"""
This module provides basic text processing functions such as cleaning text,
tokenizing text, and counting word occurrences.
"""

import re
from collections import Counter

def clean_text(text):
    """
    Clean the input text by removing punctuation and converting to lowercase.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    text = re.sub(r'[^\w\s]', '', text).lower()
    return text

def tokenize(text):
    """
    Tokenize the input text into a list of words.

    Args:
        text (str): The input text to be tokenized.

    Returns:
        list: A list of words.
    """
    return text.split()

def count_words(text):
    """
    Count the occurrences of each word in the input text.

    Args:
        text (str): The input text to count words from.

    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """
    words = tokenize(clean_text(text))
    return Counter(words)
