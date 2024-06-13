import pytest
from text_processing import count_words

@pytest.mark.parametrize("text,expected", [
    ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.",
     {'but': 1, 'the': 2, 'raven': 1, 'sitting': 1, 'lonely': 1, 'on': 1, 'placid': 1, 'bust': 1, 'spoke': 1, 'only': 1, 'that': 2, 'one': 2, 'word': 2, 'as': 1, 'if': 1, 'his': 1, 'soul': 1, 'in': 1, 'he': 1, 'did': 1, 'outpour': 1})
])
def test_count_words(text, expected):
    assert count_words(text) == expected, f"Count_words failed on sample text: {text}"

@pytest.mark.xfail
@pytest.mark.parametrize("text,expected", [
    ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.",
     {'But': 1, 'the': 2, 'Raven,': 1, 'sitting': 1, 'lonely': 1, 'on': 1, 'placid': 1, 'bust,': 1, 'spoke': 1, 'only': 1, 'That': 1, 'one': 2, 'word,': 1, 'as': 1, 'if': 1, 'his': 1, 'soul': 1, 'in': 1, 'that': 1, 'word': 1, 'he': 1, 'did': 1, 'outpour.': 1})
])
def test_count_words_fail(text, expected):
    assert count_words(text) == expected, f"Count_words should fail on this test: {text}"

def test_count_words_the_raven():
    with open('the_raven.txt', 'r') as file:
        text = file.read()
    word_counts = count_words(text)
    assert isinstance(word_counts, dict), "Count_words failed on 'The Raven' file"

