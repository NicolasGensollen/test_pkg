#!/bin/bash

set -e

if [[ $BUILD_WHEEL == true ]]; then
    source tools/travis/install_wheels.sh
else
    source tools/travis/install_main.sh
fi
