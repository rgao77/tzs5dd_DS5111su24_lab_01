import pytest
from text_processing import tokenize

@pytest.mark.parametrize("text,expected", [
    ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.",
     ["but", "the", "raven", "sitting", "lonely", "on", "the", "placid", "bust", "spoke", "only", "that", "one", "word", "as", "if", "his", "soul", "in", "that", "one", "word", "he", "did", "outpour"])
])
def test_tokenize(text, expected):
    assert tokenize(text) == expected, f"Tokenizer failed on sample text: {text}"

@pytest.mark.xfail
@pytest.mark.parametrize("text,expected", [
    ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.",
     ["But", "the", "Raven,", "sitting", "lonely", "on", "the", "placid", "bust,", "spoke", "only", "That", "one", "word,", "as", "if", "his", "soul", "in", "that", "one", "word", "he", "did", "outpour."])
])
def test_tokenize_fail(text, expected):
    assert tokenize(text) == expected, f"Tokenizer should fail on this test: {text}"

def test_tokenize_the_raven():
    with open('the_raven.txt', 'r') as file:
        text = file.read()
    tokens = tokenize(text)
    assert isinstance(tokens, list), "Tokenizer failed on 'The Raven' file"

