#!/bin/bash

set -e

pytest -n $CPU_COUNT --pyargs toy_pkg
