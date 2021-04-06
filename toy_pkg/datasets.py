
import numpy as np
import pandas as pd
from sklearn.utils import check_random_state, Bunch
from utils import _get_dataset_dir, _fetch_files

def fetch_fake_dataset_1(data_dir=None, verbose=1):
    """Download dataset 'fake_dataset_1'.

    Parameters
    ----------
    data_dir : string, optional
        Path of the data directory. Used to force data storage in a specified
        location. Default: None

    verbose : int, optional
        Verbosity level (0 means no message). Default=1.

    Returns
    -------
    data : sklearn.datasets.base.Bunch
        Dictionary-like object

    """
    dataset_name = 'fake_dataset_1'
    print("dataset name = {}".format(dataset_name))
    data_dir = _get_dataset_dir(dataset_name, data_dir=data_dir,
                                verbose=verbose)
    print("dataset dir = {}".format(data_dir))
    url = 'https://www.fake_datasets.com/fake_dataset_1/fake_dataset_1.csv'
    data_file = _fetch_files(data_dir, [('fake_dataset_1.csv', url, {})],
                                verbose=verbose)[0]
    print("dataset file = {}".format(data_file))
    description = """Fake dataset 1.\nGarbage data with two terms."""
    return Bunch(description=description,
                 data=data_file)


def fetch_fake_dataset_2(data_dir=None, verbose=1):
    """Download dataset 'fake_dataset_2'.

    Parameters
    ----------
    data_dir : string, optional
        Path of the data directory. Used to force data storage in a specified
        location. Default: None

    verbose : int, optional
        Verbosity level (0 means no message). Default=1.

    Returns
    -------
    data : sklearn.datasets.base.Bunch
        Dictionary-like object

    """
    dataset_name = 'fake_dataset_2'
    print("dataset name = {}".format(dataset_name))
    data_dir = _get_dataset_dir(dataset_name, data_dir=data_dir,
                                verbose=verbose)
    print("dataset dir = {}".format(data_dir))
    url1 = 'https://www.fake_datasets.com/fake_dataset_2/fake_dataset_2_part1.csv'
    url2 = 'https://www.fake_datasets.com/fake_dataset_2/fake_dataset_2_part2.csv'
    data_files = _fetch_files(data_dir, [('fake_dataset_2_part1.csv', url1, {}),
                                         ('fake_dataset_2_part2.csv', url2, {})],
                                verbose=verbose)
    print("dataset files = {}".format(data_files))
    description = """Fake dataset 2.\nGarbage data with two files."""
    return Bunch(description=description,
                 data=data_files)


def fetch_fake_dataset_3(data_dir=None, verbose=1):
    """Download dataset 'fake_dataset_3'.

    Parameters
    ----------
    data_dir : string, optional
        Path of the data directory. Used to force data storage in a specified
        location. Default: None

    verbose : int, optional
        Verbosity level (0 means no message). Default=1.

    Returns
    -------
    data : sklearn.datasets.base.Bunch
        Dictionary-like object

    """
    dataset_name = 'fake_dataset_3'
    print("dataset name = {}".format(dataset_name))
    data_dir = _get_dataset_dir(dataset_name, data_dir=data_dir,
                                verbose=verbose)
    print("dataset dir = {}".format(data_dir))
    url = 'https://www.fake_datasets.com/fake_dataset_3/fake_dataset_3.csv'
    data_file = _fetch_files(data_dir, [('fake_dataset_3.csv', url, {})],
                                verbose=verbose)[0]
    print("dataset file = {}".format(data_file))
    description = """Fake dataset 3.\nGarbage data with two terms."""
    return Bunch(description=description,
                 data=data_file)
