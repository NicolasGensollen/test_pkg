#!/bin/bash

set -e

if [[ $BUILD_WHEEL == true && $TRAVIS_EVENT_TYPE != pull_request ]]; then

