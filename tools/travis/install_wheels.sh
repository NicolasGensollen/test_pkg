#!/bin/bash

set -e

#python -m pip install cibuildwheel
#python -m cibuildwheel --output-dir wheelhouse
python -m pip wheel -w wheelhouse .
echo "Listing wheels:";
echo "$(ls ./wheelhouse)";
