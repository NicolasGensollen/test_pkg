#!/bin/bash

echo Submitting coverage

set -eu
set -x

COVERAGE_FILE="coverage.xml"

if [ -e "$COVERAGE_FILE" ]; then
    python -m pip install codecov
    python -m codecov --file coverage.xml
fi

set +eux

echo Done submitting coverage
