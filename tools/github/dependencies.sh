#!/bin/bash

python --version
python -m pip install --upgrade pip setuptools wheel
pip install joblib numpy scipy pandas scikit-learn matplotlib lxml pytest pytest-cov coverage

if [[ ! -z "$DEV_VERSION" ]]; then
    pip install git+https://github.com/matplotlib/matplotlib.git
fi

if [[ -n "$FLAKE8" ]]; then
    echo "Installing Flake8";
    pip install flake8
fi
#pip install --progress-bar off --upgrade -r requirements_testing.txt
