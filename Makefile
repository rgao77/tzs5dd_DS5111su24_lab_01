# Run linting
lint:
	. env/bin/activate && pylint src/pkg_tzs5dd/*.py || true


# Run tests
test:
	. env/bin/activate && PYTHONPATH=src pytest -m "not integration" tests/

