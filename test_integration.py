import os
import pytest
from text_processor import clean_text, tokenize, count_words

@pytest.mark.integration
def test_integration_processing():
    files = [
        "books/17192.txt",
        "books/932.txt",
        "books/1063.txt",
        "books/10031.txt"
    ]

    for file_path in files:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                text = f.read()
            cleaned_text = clean_text(text)
            tokens = tokenize(cleaned_text)
            word_counts = count_words(cleaned_text)
            assert len(tokens) > 0, f"Failed to tokenize file: {file_path}"
            assert len(word_counts) > 0, f"Failed to count words in file: {file_path}"
        else:
            pytest.skip(f"{file_path} not found.")

