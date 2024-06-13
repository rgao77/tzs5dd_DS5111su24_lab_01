import pytest
import subprocess
from text_processing import clean_text

def test_bash_comparison():
    text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."
    expected = "but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour"
    
    result = subprocess.run(['echo', text, '|', 'tr', '-d', '[:punct:]', '|', 'tr', '[:upper:]', '[:lower:]'], capture_output=True, text=True, shell=True)
    bash_output = result.stdout.strip()
    
    assert clean_text(text) == bash_output

