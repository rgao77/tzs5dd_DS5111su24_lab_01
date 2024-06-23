import pytest
import platform
from text_processing import clean_text

@pytest.mark.skipif(platform.system() != 'Linux', reason="Test runs only on Linux")
def test_os_specific():
    text = "This is a test"
    expected = "this is a test"
    assert clean_text(text) == expected

