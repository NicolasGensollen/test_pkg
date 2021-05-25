#!/bin/bash

set -e

if [[ -n "$FLAKE8" ]]; then
    source tools/flake8_diff.sh
fi

TEST_CMD="pytest"

if [[ $TRAVIS_CPU_ARCH == arm64 ]]; then
    TEST_CMD="$TEST_CMD --pyargs"
fi

$TEST_CMD toy_pkg
