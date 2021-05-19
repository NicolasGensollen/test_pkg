#!/bin/bash

set -e

echo "CPU Arch: $TRAVIS_CPU_ARCH."

source tools/shared.sh

conda init bash
conda create -n testenv
conda install -n testenv -yq python=3.8 numpy scipy scikit-learn
source activate testenv
python -m pip install --user --upgrade --progress-bar off pip setuptools
python -m pip install .
