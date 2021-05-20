#!/bin/bash

set -e

if [[ -n "$FLAKE8" ]]; then
    source tools/flake8_diff.sh
fi

TEST_CMD="pytest --pyargs"

if [[ $TRAVIS_CPU_ARCH == arm64 ]]; then
    TEST_CMD="$TEST_CMD -n $CPU_COUNT"
fi

$TEST_CMD toy_pkg
