import pytest
from pkg_tzs5dd import clean_text, tokenize, count_words

def test_clean_text():
    text = "Hello, World!"
    cleaned = clean_text(text)
    assert cleaned == "hello world"

def test_tokenize():
    text = "hello world"
    tokens = tokenize(text)
    assert tokens == ["hello", "world"]

def test_count_words():
    text = "hello hello world"
    word_count = count_words(text)
    assert word_count == {"hello": 2, "world": 1}
