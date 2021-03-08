#! /usr/bin/env python

import os
import sys
import setuptools


def load_version():
    """Executes toy_pkg/version.py in a globals dictionary and return it."""
    globals_dict = {}
    with open(os.path.join('toy_pkg', 'version.py')) as fp:
        exec(fp.read(), globals_dict)
    return globals_dict


def is_installing():
    # Allow command-lines such as "python setup.py build install"
    install_commands = set(['install', 'develop'])
    return install_commands.intersection(set(sys.argv))


def list_required_packages():
    required_packages = []
    required_packages_orig = ['%s>=%s' % (mod, meta['min_version'])
                              for mod, meta
                              in _VERSION_GLOBALS['REQUIRED_MODULE_METADATA']
                              ]
    for package in required_packages_orig:
        if package.startswith('sklearn'):
            package = package.replace('sklearn', 'scikit-learn')
        required_packages.append(package)
    return required_packages

# Make sources available using relative paths from this file's directory.
os.chdir(os.path.dirname(os.path.abspath(__file__)))

_VERSION_GLOBALS = load_version()
DISTNAME = 'toy_pkg'
DESCRIPTION = 'A small and useless example package'
with open('README.rst') as fp:
    LONG_DESCRIPTION = fp.read()
MAINTAINER = 'Nicolas Gensollen'
MAINTAINER_EMAIL = 'nicolas.gensollen@gmail.com'
URL = 'http://github.com/NicolasGensollen/toy_pkg'
LICENSE = 'none'
DOWNLOAD_URL = 'http://github.com/NicolasGensollen/toy_pkg'
VERSION = _VERSION_GLOBALS['__version__']

if __name__ == "__main__":
    if is_installing():
        module_check_fn = _VERSION_GLOBALS['_check_module_dependencies']
        module_check_fn(is_toy_pkg_installing=True)

    setuptools.setup(
        name=DISTNAME,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        long_description=LONG_DESCRIPTION,
        zip_safe=False,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        packages=setuptools.find_packages(),
        install_requires=list_required_packages(),
        python_requires='>=3.6',
    )
