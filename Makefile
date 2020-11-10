# simple makefile to simplify repetitive build env management tasks under posix

PYTHON ?= python
#CYTHON ?= cython
#CTAGS ?= ctags

all: clean test

clean-pyc:
	find . -name "*.pyc" | xargs rm -f
	find . -name "__pycache__" | xargs rm -rf

clean-so:
	find . -name "*.so" | xargs rm -f
	find . -name "*.pyd" | xargs rm -f

clean-build:
	rm -rf build

clean-ctags:
	rm -f tags

clean: clean-build clean-pyc clean-so clean-ctags

in: inplace # just a shortcut

test-code:
	python -m pytest --pyargs test_pkg --cov=test_pkg

test-coverage:
	rm -rf coverage .coverage
	pytest --pyargs test_pkg --showlocals --cov=test_pkg --cov-report=html:coverage

test: test-code
