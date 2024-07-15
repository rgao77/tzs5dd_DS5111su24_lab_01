"""
text_processor module.

This module provides functions to clean text, tokenize text, and count words in a text.
"""

def clean_text(text):
    """
    Cleans the input text by converting to lowercase and removing non-alphanumeric characters.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    text = text.lower()
    cleaned_text = ''.join(char for char in text if char.isalnum() or char.isspace())
    return cleaned_text

def tokenize(text):
    """
    Tokenizes the input text into a list of words.

    Args:
        text (str): The input text to be tokenized.

    Returns:
        list: A list of words from the input text.
    """
    return text.split()

def count_words(text):
    """
    Counts the occurrences of each word in the input text.

    Args:
        text (str): The input text to count words from.

    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """
    words = tokenize(text)
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

