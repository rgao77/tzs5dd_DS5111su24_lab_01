import pytest
from text_processor import clean_text, tokenize, count_words

def test_clean_text():
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    expected = 'but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour'
    result = clean_text(text)
    assert result == expected, f"Failed to clean text: {result}"

@pytest.mark.xfail(reason="Known issue with accented characters")
def test_clean_text_fail():
    text = 'Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait.'
    expected = 'this should fail'
    result = clean_text(text)
    assert result == expected, f"Expected failure did not occur: {result}"


