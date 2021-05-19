#!/bin/bash

set -e

if [[ $BUILD_WHEEL != true ]]; then
    bash tools/travis/test_script.sh
fi
