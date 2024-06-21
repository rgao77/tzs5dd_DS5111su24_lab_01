
import logging
from text_processing import clean_text, tokenize, count_words

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
