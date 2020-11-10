#!/bin/bash
# This script is meant to be called by the "install" step defined in
# .travis.yml. See http://docs.travis-ci.com/ for more details.
# The behaviour of the script is controlled by the environment variables defined
# in the .travis.yml in the top level folder of the project.
#
# License: 3-clause BSD

set -e

echo_requirements_string() {
    # Echo a requirement string for example
    # "pip pytest python='2.7.3' scikit-learn=*". It has a hardcoded
    # list of possible packages to install and looks at _VERSION
    # environment variables to know whether to install a given package and
    # if yes which version to install. For example:
    #   - for numpy, NUMPY_VERSION is used
    TO_INSTALL_ALWAYS="pytest"
    REQUIREMENTS="$TO_INSTALL_ALWAYS"
    TO_INSTALL_MAYBE="numpy matplotlib flake8"
    for PACKAGE in $TO_INSTALL_MAYBE; do
        # Capitalize package name and add _VERSION
        PACKAGE_VERSION_VARNAME="${PACKAGE^^}_VERSION"
        # replace - by _, needed for scikit-learn for example
        PACKAGE_VERSION_VARNAME="${PACKAGE_VERSION_VARNAME//-/_}"
        # dereference $PACKAGE_VERSION_VARNAME to figure out the
        # version to install
        PACKAGE_VERSION="${!PACKAGE_VERSION_VARNAME}"
        if [[ -n "$PACKAGE_VERSION" ]]; then
            if [[ "$PACKAGE_VERSION" == "*" ]]; then
                REQUIREMENTS="$REQUIREMENTS $PACKAGE"
            else
                REQUIREMENTS="$REQUIREMENTS $PACKAGE==$PACKAGE_VERSION"
            fi
        fi
    done
    echo $REQUIREMENTS
}

create_new_travis_env() {
    REQUIREMENTS=$(echo_requirements_string)
    pip install ${REQUIREMENTS}
    if [[ $MATPLOTLIB_VERSION == "dev" ]]; then
        echo "Install Development version of Matplotlib."
        pip install git+https://github.com/matplotlib/matplotlib.git
    fi
    #pip install --upgrade $PIP_FLAGS $REQUIREMENTS
    echo "next..."
    if [[ $MATPLOTLIB_VERSION == "dev" ]]; then
        echo "Install Development version of Matplotlib."
        pip install git+https://github.com/matplotlib/matplotlib.git
    fi
    pip install --upgrade pytest pytest-cov

    if [[ "$INSTALL_MKL" == "true" ]]; then
        # Make sure MKL is used
        pip install mkl
    fi
}

if [[ "$DISTRIB" == "travisci" ]]; then
    create_new_travis_env
else
    echo "Unrecognized distribution ($DISTRIB); cannot setup CI environment."
fi

pip install psutil memory_profiler

if [[ "$COVERAGE" == true ]]; then
    pip install codecov
fi

# numpy not installed when skipping the tests so we do not want to run
# setup.py install
if [[ "$SKIP_TESTS" != "true" ]]; then
    pip install $PIP_FLAGS .
fi
