# Run linting
lint:
	. env/bin/activate && pylint src/pkg_tzs5dd/*.py

# Run tests
test:
	. env/bin/activate && PYTHONPATH=src pytest -m "not integration" tests/

