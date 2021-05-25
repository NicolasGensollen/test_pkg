#!/bin/bash

set -e

if [[ $BUILD_WHEEL == true && $TRAVIS_EVENT_TYPE != pull_request ]]; then
    if [[ $TRAVIS_EVENT_TYPE == cron ]]; then
        ANACONDA_ORG="toy_pkg-wheels-nightly"
        ANACONDA_TOKEN="$TOY_PKG_NIGHTLY_UPLOAD_TOKEN"
    else
        ANACONDA_ORG="toy_pkg-wheels-staging"
        ANACONDA_TOKEN="$TOY_PKG_STAGING_UPLOAD_TOKEN"
    fi

    MINICONDA_URL="https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-aarch64.sh"
    wget $MINICONDA_URL -O miniconda.sh
    MINICONDA_PATH=$HOME/miniconda
    chmod +x miniconda.sh && ./miniconda.sh -b -p $MINICONDA_PATH

    export PATH=$MINICONDA_PATH/bin:$PATH
    conda create -n upload -y python=3.8
    source activate upload
    conda install -y anaconda-client

    # Force a replacement if the remote file already exists
    anaconda -t $ANACONDA_TOKEN upload --force -u $ANACONDA_ORG wheelhouse/*.whl
    echo "Index: https://pypi.anaconda.org/$ANACONDA_ORG/simple"
fi
