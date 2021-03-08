# *- encoding: utf-8 -*-
"""
toy_pkg version, required package versions, and utilities for checking
"""

__version__ = '0.0.2'

_NILEARN_INSTALL_MSG = 'See %s for installation information.' % (
    'http://github.com/NicolasGensollen/toy_pkg')

# This is a tuple to preserve order, so that dependencies are checked
#   in some meaningful order (more => less 'core').
REQUIRED_MODULE_METADATA = (
    ('numpy', {
        'min_version': '1.11',
        'required_at_installation': True,
        'install_info': _NILEARN_INSTALL_MSG}),
    )

def _import_module_with_version_check(
        module_name,
        minimum_version,
        install_info=None):
    """Check that module is installed with a recent enough version
    """
    from distutils.version import LooseVersion

    try:
        module = __import__(module_name)
    except ImportError as exc:
        user_friendly_info = ('Module "{0}" could not be found. {1}').format(
            module_name,
            install_info or 'Please install it properly to use nilearn.')
        exc.args += (user_friendly_info,)
        # Necessary for Python 3 because the repr/str of ImportError
        # objects was changed in Python 3
        if hasattr(exc, 'msg'):
            exc.msg += '. ' + user_friendly_info
        raise

    # Avoid choking on modules with no __version__ attribute
    module_version = getattr(module, '__version__', '0.0.0')

    version_too_old = (not LooseVersion(module_version) >=
                       LooseVersion(minimum_version))

    if version_too_old:
        message = (
            'A {module_name} version of at least {minimum_version} '
            'is required to use nilearn. {module_version} was found. '
            'Please upgrade {module_name}').format(
                module_name=module_name,
                minimum_version=minimum_version,
                module_version=module_version)

        raise ImportError(message)

    return module


def _check_module_dependencies(is_toy_pkg_installing=False):
    """Throw an exception if toy_pkg dependencies are not installed.

    Parameters
    ----------
    is_toy_pkg_installing : boolean
        if True, only error on missing packages that cannot be auto-installed.
        if False, error on any missing package.

    Throws
    -------
    ImportError

    """
    for (module_name, module_metadata) in REQUIRED_MODULE_METADATA:
        if not (is_toy_pkg_installing and
                not module_metadata['required_at_installation']):
            # Skip check only when installing and it's a module that
            # will be auto-installed.
            _import_module_with_version_check(
                module_name=module_name,
                minimum_version=module_metadata['min_version'],
                install_info=module_metadata.get('install_info'))
