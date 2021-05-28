#!/bin/bash -x

pwd

python -m pytest --pyargs toy_pkg --cov-report=xml --cov=toy_pkg

