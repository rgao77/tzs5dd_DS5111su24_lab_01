# Default target to display Makefile content
default:
	@echo "Available targets: lint, test, test-integration"

# Run pylint to lint the code
lint:
	. env/bin/activate && pylint src/pkg_tzs5dd/*.py

# Run tests using pytest
test:
	. env/bin/activate && PYTHONPATH=src pytest -m "not integration" tests/

# Run integration tests
test-integration:
	. env/bin/activate && PYTHONPATH=src pytest -m "integration" tests/




