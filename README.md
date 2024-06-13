# Text Processing Functions

This repository contains a set of text processing functions designed to clean text, tokenize it, and count word occurrences. These functions are useful for preparing text data for natural language processing tasks.

## Functions

- `clean_text(text)`: Converts text to lowercase and removes punctuation.
- `tokenize(text)`: Splits cleaned text into a list of words.
- `count_words(text)`: Counts the occurrences of each word in the text.

## Example Usage

```python
from text_processing import clean_text, tokenize, count_words

text = "But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour."

cleaned = clean_text(text)
print(cleaned)
# Output: "but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour"

tokens = tokenize(text)
print(tokens)
# Output: ['but', 'the', 'raven', 'sitting', 'lonely', 'on', 'the', 'placid', 'bust', 'spoke', 'only', 'that', 'one', 'word', 'as', 'if', 'his', 'soul', 'in', 'that', 'one', 'word', 'he', 'did', 'outpour']

word_counts = count_words(text)
print(word_counts)
# Output: {'but': 1, 'the': 2, 'raven': 1, 'sitting': 1, 'lonely': 1, 'on': 1, 'placid': 1, 'bust': 1, 'spoke': 1, 'only': 1, 'that': 2, 'one': 2, 'word': 2, 'as': 1, 'if': 1, 'his': 1, 'soul': 1, 'in': 1, 'he': 1, 'did': 1, 'outpour': 1}


