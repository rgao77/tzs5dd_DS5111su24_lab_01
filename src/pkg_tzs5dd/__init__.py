# Import the functions from text_processor.py
from .text_processor import clean_text, tokenize, count_words

# Define what is available when you import from the package
__all__ = ["clean_text", "tokenize", "count_words"]

