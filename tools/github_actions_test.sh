#!/bin/bash -ef

echo 'python -m pytest --pyargs toy_pkg --cov=toy_pkg'
python -m pytest --pyargs toy_pkg --cov=toy_pkg
