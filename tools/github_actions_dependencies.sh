#!/bin/bash -ef

if [ ! -z "$CONDA_ENV" ]; then
	pip uninstall -yq toy_pkg
elif [ ! -z "$CONDA_DEPENDENCIES" ]; then
	conda install -y $CONDA_DEPENDENCIES
else # pip
	python -m pip install --progress-bar off --upgrade pip setuptools wheel
	pip uninstall -yq numpy
	pip install --progress-bar off --upgrade --pre --only-binary ":all:" joblib numpy scipy pandas scikit-learn matplotlib lxml pytest pytest-cov coverage
fi
#pip install --progress-bar off --upgrade -r requirements_testing.txt
