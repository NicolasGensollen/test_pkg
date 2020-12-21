#!/bin/bash -x

pwd
python -m pytest --pyargs toy_pkg --cov=toy_pkg
