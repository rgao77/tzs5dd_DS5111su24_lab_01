# DS5111su24 Lab Project

This repository contains the code and resources for the DS5111su24 lab project. The project involves downloading texts from Project Gutenberg, processing the texts, and performing various analyses.

## Project Structure

tzs5dd_DS5111su24_lab_01/
├── .gitignore
├── Dockerfile
├── Makefile
├── README.md
├── get_the_books.sh
├── raven_counts.sh
├── raven_line_count.sh
├── raven_word_count.sh
├── requirements.txt
├── text_processing.py
├── total_lines.sh
└── total_words.sh


## Setup Instructions

### Clone the Repository

```sh
git clone https://github.com/rgao77/tzs5dd_DS5111su24_lab_01.git
cd tzs5dd_DS5111su24_lab_01

## Create and Switch to the tokenizer Branch
git checkout -b tokenizer

## Install Dependencies
Create a virtual environment and install the required packages:
make setup_env

## Usage
### Download the Books
To download the books from Project Gutenberg, run:
make get_texts

### Count the Number of Lines in The Raven
To count the number of lines in "The Raven", run:
make raven_line_count

### Count the Number of Words in The Raven
To count the number of words in "The Raven", run:
make raven_word_count

### Count Occurrences of 'raven' in The Raven
To count occurrences of 'raven' in "The Raven", run:
make raven_counts


### Count the Total Number of Lines in All Files
To count the total number of lines in all downloaded files, run:
make total_lines

### Count the Total Number of Words in All Files
To count the total number of words in all downloaded files, run:
make total_words

## Text Processing Functions
The text_processing.py file contains functions for text processing:

clean_text: Convert text to lowercase and remove punctuation.
tokenize: Split cleaned text into a list of words.
count_words: Count the occurrences of each word in the text.


### Example Usage
import logging
from text_processing import clean_text, tokenize, count_words

example_text = "Hello, world! This is a test. Hello again."
logging.info("Starting text processing")

# Clean the text
cleaned = clean_text(example_text)
assert cleaned is not None, "clean_text returned None"

# Tokenize the text
tokens = tokenize(example_text)
assert isinstance(tokens, list), "tokenize did not return a list"

# Count the words
counts = count_words(example_text)
assert isinstance(counts, dict), "count_words did not return a dictionary"

logging.info("Text processing completed")
