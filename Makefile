lint:
	. env/bin/activate && pylint src/pkg_tzs5dd/*.py

test:
	. env/bin/activate && PYTHONPATH=src pytest -m "not integration" tests/

