import pytest
from text_processor import tokenize, clean_text

def test_tokenize():
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    cleaned_text = clean_text(text)
    expected = ['but', 'the', 'raven', 'sitting', 'lonely', 'on', 'the', 'placid', 'bust', 'spoke', 'only', 'that', 'one', 'word', 'as', 'if', 'his', 'soul', 'in', 'that', 'one', 'word', 'he', 'did', 'outpour']
    result = tokenize(cleaned_text)
    assert result == expected, f"Failed to tokenize text: {result}"

@pytest.mark.parametrize("file_path, expected_count", [
    ("books/17192.txt", 10178),
    ("books/932.txt", 10093),
    ("books/1063.txt", 5334),
    ("books/10031.txt", 0),
    ("books/14082.txt", 0)
])
def test_tokenize_file(file_path, expected_count):
    with open(file_path, 'r') as f:
        text = f.read()
    cleaned_text = clean_text(text)
    tokens = tokenize(cleaned_text)
    assert len(tokens) == expected_count, f"Failed to tokenize file: {file_path}"

