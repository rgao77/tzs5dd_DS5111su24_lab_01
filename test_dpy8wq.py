from pkg_dpy8wq.text_processor import clean_text, tokenize, count_words

def test_clean_text():
    assert clean_text("Hello, World!") == "Hello, World!"

def test_tokenize():
    assert tokenize("Hello, World!") == ["Hello,", "World!"]

def test_count_words():
    assert count_words("Hello, World! Hello!") == {"Hello,": 1, "World!": 1, "Hello!": 1}

