# Default task: display the contents of the Makefile
default:
	cat Makefile

# Task to download the books
get_texts:
	bash get_the_books.sh

# Task to count the number of lines in The Raven
raven_line_count:
	bash raven_line_count.sh

# Task to count the number of words in The Raven
raven_word_count:
	bash raven_word_count.sh

# Task to count occurrences of 'raven' in The Raven
raven_counts:
	@echo "Count of 'raven':" && grep -o 'raven' books/15951.txt | wc -l
	@echo "Count of 'Raven':" && grep -o 'Raven' books/15951.txt | wc -l
	@echo "Count of 'raven' (case insensitive):" && grep -i -o 'raven' books/15951.txt | wc -l

# Task to count the total number of lines in all files
total_lines:
	bash total_lines.sh

# Task to count the total number of words in all files
total_words:
	bash total_words.sh

# Task to set up the Python virtual environment and install required packages
setup_env:
    python3 -m venv env
    ./env/bin/pip install --upgrade pip
    ./env/bin/pip install -r requirements.txt

# Task to run tests
test:
    ./env/bin/pytest

# Task to run pylint
lint:
    ./env/bin/pylint text_processing.py


