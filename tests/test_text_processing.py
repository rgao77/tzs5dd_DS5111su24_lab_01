import pytest
from text_processing import clean_text, tokenize, count_words

@pytest.mark.parametrize("file", [
    '17192.txt',
    '932.txt',
    '1063.txt',
    '10031.txt',
    '14082.txt'
])
def test_clean_text_files(file):
    with open(file, 'r') as f:
        text = f.read()
    cleaned_text = clean_text(text)
    assert cleaned_text is not None, f"Clean_text failed on file: {file}"

@pytest.mark.parametrize("file", [
    '17192.txt',
    '932.txt',
    '1063.txt',
    '10031.txt',
    '14082.txt'
])
def test_tokenize_files(file):
    with open(file, 'r') as f:
        text = f.read()
    tokens = tokenize(text)
    assert isinstance(tokens, list), f"Tokenizer failed on file: {file}"

@pytest.mark.parametrize("file", [
    '17192.txt',
    '932.txt',
    '1063.txt',
    '10031.txt',
    '14082.txt'
])
def test_count_words_files(file):
    with open(file, 'r') as f:
        text = f.read()
    word_counts = count_words(text)
    assert isinstance(word_counts, dict), f"Count_words failed on file: {file}"

