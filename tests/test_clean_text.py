import pytest
from text_processing import clean_text

@pytest.mark.parametrize("text,expected", [
    ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.",
     "but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour")
])
def test_clean_text(text, expected):
    assert clean_text(text) == expected, f"Clean_text failed on sample text: {text}"

@pytest.mark.xfail
@pytest.mark.parametrize("text,expected", [
    ("But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.",
     "but the raven, sitting lonely on the placid bust, spoke only that one word, as if his soul in that one word he did outpour")
])
def test_clean_text_fail(text, expected):
    assert clean_text(text) == expected, f"Clean_text should fail on this test: {text}"

def test_clean_text_the_raven():
    with open('the_raven.txt', 'r') as file:
        text = file.read()
    cleaned_text = clean_text(text)
    assert cleaned_text is not None, "Clean_text failed on 'The Raven' file"

