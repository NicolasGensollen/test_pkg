#!/bin/bash -x

python -m pip install --progress-bar off --upgrade pip setuptools wheel
pip install --progress-bar off --upgrade --pre --only-binary ":all:" joblib numpy scipy pandas scikit-learn matplotlib lxml pytest pytest-cov coverage

if [ ! -z "$DEV_VERSION" ]; then
    pip install git+https://github.com/matplotlib/matplotlib.git
fi
#pip install --progress-bar off --upgrade -r requirements_testing.txt
