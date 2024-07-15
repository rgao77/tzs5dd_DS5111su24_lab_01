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

# Setup virtual environment and install dependencies
setup:
        python3 -m venv env
        . env/bin/activate && pip install --upgrade pip
        . env/bin/activate && pip install -r requirements.txt

# Run linting
lint:
        . env/bin/activate && pylint src/pkg_dpy8wq/*.py tests/*.py

# Run tests
test: lint
        . env/bin/activate && pytest -m "not integration" tests/

# Run integration tests
test-integration:
        . env/bin/activate && pytest -m "integration" tests/


