import pkgutil
import inspect
from importlib import import_module
from pathlib import Path
from .utils import fill_doc, get_data_dirs, movetree

__all__ = ['fill_doc', 'get_data_dirs', 'movetree']


def all_modules(modules_to_ignore=None):
    """Get a list of all modules from toy_pkg."""
    if modules_to_ignore is None:
        modules_to_ignore = {
            "tests",
        }
    all_modules = []
    root = str(Path(__file__).parent.parent)
    for importer, modname, ispkg in pkgutil.walk_packages(
        path=[root], prefix="toy_pkg."
    ):
        mod_parts = modname.split(".")
        if any(part in modules_to_ignore for part in mod_parts) or "._" in modname:
            continue
        all_modules.append(modname)
    return all_modules


def all_functions(return_private=False, modules_to_ignore=None):
    """Get a list of all functions from toy_pkg."""
    all_functions = []
    for modname in all_modules(modules_to_ignore=modules_to_ignore):
        module = import_module(modname)
        functions = [
            (name, func) for name, func in inspect.getmembers(module, inspect.isfunction)
            if func.__module__ == module.__name__
        ]
        if not return_private:
            functions = [
                (name, func) for name, func in functions if not name.startswith("_")
            ]
        all_functions.extend(functions)
    return all_functions


def all_classes(return_private=False, modules_to_ignore=None):
    """Get a list of all classes from toy_pkg."""
    all_classes = []
    for modname in all_modules(modules_to_ignore=modules_to_ignore):
        module = import_module(modname)
        classes = [
            (name, cls) for name, cls in inspect.getmembers(module, inspect.isclass)
            if cls.__module__ == module.__name__
        ]
        if not return_private:
            classes = [
                (name, cls) for name, cls in classes if not name.startswith("_")
            ]
        all_classes.extend(classes)
    return all_classes

