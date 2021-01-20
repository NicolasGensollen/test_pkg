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

test-doc:
	pytest --doctest-glob='*.rst' `find doc/ -name '*.rst'`

test-code:
	python -m pytest --pyargs toy_pkg --cov=toy_pkg

test-coverage:
	rm -rf coverage .coverage
	pytest --pyargs toy_pkg --showlocals --cov=toy_pkg --cov-report=html:coverage

test: test-code
