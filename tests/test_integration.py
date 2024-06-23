import pytest
from text_processing import clean_text, tokenize, count_words

def test_integration():
    # Sample text
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."

    # Clean the text
    cleaned = clean_text(text)
    assert cleaned is not None, "clean_text returned None"

    # Tokenize the text
    tokens = tokenize(cleaned)
    assert isinstance(tokens, list), "tokenize did not return a list"

    # Count the words
    word_counts = count_words(cleaned)
    assert isinstance(word_counts, dict), "count_words did not return a dictionary"

    # Check for specific word counts
    assert word_counts.get("raven") == 1, "Expected 1 occurrence of 'raven'"
    assert word_counts.get("word") == 2, "Expected 2 occurrences of 'word'"

@pytest.mark.integration
def test_multiple_files():
    # This function should test processing of multiple files
    # Add your test code here
    pass

