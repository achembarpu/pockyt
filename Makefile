all:

setup:
	@echo "setting up virtual environment"
	virtualenv .venv
	@echo "\nREADY! remember to run:\n source .venv/bin/activate\n\n"

install:
	python setup.py install

teardown:
	@echo "removing virtual environment"
	rm -rf .venv

test:
	python tests.py

run:
	@pockyt get -s unread -f '{title} | {tags}'
