import pytest
import sys
from text_processing import clean_text

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8 or higher")
def test_python_version_specific():
    text = "This is a test"
    expected = "this is a test"
    assert clean_text(text) == expected

