#!/bin/bash -x

if [[ -n "$FLAKE8" ]]; then
    echo "running flake8 diff script...";
    source tools/github/flake8_diff.sh
fi
pwd
python -m pytest --pyargs toy_pkg --cov-report=xml --cov=toy_pkg
