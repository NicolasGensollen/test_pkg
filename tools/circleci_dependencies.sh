#!/bin/bash -ef

python -m pip uninstall -y pydata-sphinx-theme
python -m pip install --user --upgrade --progress-bar off pip setuptools
python -m pip install --user --upgrade --progress-bar off --pre sphinx
python -m pip install --user --upgrade --progress-bar off -r requirements.txt -r requirements-build-docs.txt
python -m pip install --user -e .
