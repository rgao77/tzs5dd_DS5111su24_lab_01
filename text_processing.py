import re
from collections import Counter
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_text(text):
    """
    Convert text to lowercase and remove punctuation.

    Args:
        text (str): The input string.

    Returns:
        str: The cleaned string.
    """
    assert isinstance(text, str), "Input must be a string"

    # Remove punctuation and convert to lowercase
    cleaned_text = re.sub(r'\W+', ' ', text).lower()
    
    logging.debug(f"Cleaned text: {cleaned_text}")
    return cleaned_text

def tokenize(text):
    """
    Split cleaned text into a list of words.

    Args:
        text (str): The input string.

    Returns:
        list: A list of words.
    """
    assert isinstance(text, str), "Input must be a string"

    # Clean the text
    cleaned_text = clean_text(text)
    
    # Split the cleaned text into words
    words_list = cleaned_text.split()
    
    logging.debug(f"Tokenized words: {words_list}")
    return words_list

def count_words(text):
    """
    Count the occurrences of each word in the text.

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary with words as keys and their counts as values.
    """
    assert isinstance(text, str), "Input must be a string"

    # Tokenize the text
    words_list = tokenize(text)
    
    # Count the occurrences of each word
    word_counts = dict(Counter(words_list))
    
    logging.debug(f"Word counts: {word_counts}")
    return word_counts

# Example usage
if __name__ == "__main__":
    example_text = "Hello, world! This is a test. Hello again."
    logging.info("Starting text processing")

    # Clean the text
    cleaned = clean_text(example_text)
    assert cleaned is not None, "clean_text returned None"

    # Tokenize the text
    tokens = tokenize(example_text)
    assert isinstance(tokens, list), "tokenize did not return a list"

    # Count the words
    counts = count_words(example_text)
    assert isinstance(counts, dict), "count_words did not return a dictionary"

    logging.info("Text processing completed")

