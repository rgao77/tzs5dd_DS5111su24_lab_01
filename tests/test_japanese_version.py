import pytest
from text_processing import clean_text, tokenize, count_words

@pytest.mark.skip(reason="Japanese version test not ready yet")
def test_japanese_text():
    text = "日本語のテキスト"
    assert clean_text(text) == text
    assert tokenize(text) == [text]
    assert count_words(text) == {text: 1}

