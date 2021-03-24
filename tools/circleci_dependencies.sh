#!/bin/bash -ef

conda init bash
echo "conda version = $(conda --version)"
conda create -n testenv
conda install -n testenv python=3.8 numpy lxml mkl sphinx numpydoc pillow -yq
conda install -n testenv sphinx-gallery junit-xml -c conda-forge -yq
source activate testenv
python -m pip install pydata-sphinx-theme
python -m pip install --user --upgrade --progress-bar off pip setuptools
python -m pip install --user -e .
