# -*- coding: utf-8 -*-

import os
import sys
import time
import warnings
import hashlib
import urllib
import pickle
import shutil
import pandas as pd
from sklearn.utils import check_random_state


docdict = dict()

# Verbose
docdict['verbose'] = """
verbose : bool, str, int, or None
    Verbosity level.
"""

docdict_indented = dict()


def indentcount_lines(lines):
    """ Minimum indent for all lines in line list
    >>> lines = [' one', '  two', '   three']
    >>> indentcount_lines(lines)
    1
    >>> lines = []
    >>> indentcount_lines(lines)
    0
    >>> lines = [' one']
    >>> indentcount_lines(lines)
    1
    >>> indentcount_lines(['    '])
    0
    """
    indentno = sys.maxsize
    for line in lines:
        stripped = line.lstrip()
        if stripped:
            indentno = min(indentno, len(line) - len(stripped))
    if indentno == sys.maxsize:
        return 0
    return indentno


def fill_doc(f):
    """Fill a docstring with docdict entries.

    Parameters
    ----------
    f : callable
        The function to fill the docstring of. Will be modified in place.

    Returns
    -------
    f : callable
        The function, potentially with an updated ``__doc__``.
    """
    docstring = f.__doc__
    if not docstring:
        return f
    lines = docstring.splitlines()
    if len(lines) < 2:
        icount = 0
    else:
        icount = indentcount_lines(lines[1:])
    try:
        indented = docdict_indented[icount]
    except KeyError:
        indent = ' ' * icount
        docdict_indented[icount] = indented = {}
        for name, dstr in docdict.items():
            lines = dstr.splitlines()
            try:
                newlines = [lines[0]]
                for line in lines[1:]:
                    newlines.append(indent + line)
                indented[name] = '\n'.join(newlines)
            except IndexError:
                indented[name] = dstr
    try:
        f.__doc__ = docstring % indented
    except (TypeError, ValueError, KeyError) as exp:
        funcname = f.__name__
        funcname = docstring.split('\n')[0] if funcname is None else funcname
        raise RuntimeError('Error documenting %s:\n%s'
                           % (funcname, str(exp)))
    return f


def get_data_dirs(data_dir=None):
    """Returns the directories in which to look for data.
    This is typically useful for the end-user to check where the data is
    downloaded and stored.

    Parameters
    ----------
    data_dir : string, optional
        Path of the data directory. Used to force data storage in a specified
        location. Default: None

    Returns
    -------
    paths : list of strings
        Paths of the dataset directories.

    Notes
    -----
    This function retrieves the datasets directories using the following
    priority :

        1. defaults system paths
        2. the keyword argument data_dir
        3. the global environment variable TOY_PKG_SHARED_DATA
        4. the user environment variable TOY_PKG_DATA
        5. nilearn_data in the user home folder

    """""
    # We build an array of successive paths by priority
    # The boolean indicates if it is a pre_dir: in that case, we won't add the
    # dataset name to the path.
    paths = []

    # Check data_dir which force storage in a specific location
    if data_dir is not None:
        paths.extend(data_dir.split(os.pathsep))

    # If data_dir has not been specified, then we crawl default locations
    if data_dir is None:
        global_data = os.getenv('TOY_PKG_SHARED_DATA')
        if global_data is not None:
            paths.extend(global_data.split(os.pathsep))

        local_data = os.getenv('TOY_PKG_DATA')
        if local_data is not None:
            paths.extend(local_data.split(os.pathsep))

        paths.append(os.path.expanduser('~/toy_pkg_data'))
    return paths


def _get_dataset_dir(dataset_name, data_dir=None, default_paths=None,
                     verbose=1):
    """Creates if necessary and returns data directory of given dataset.

    Parameters
    ----------
    dataset_name : string
        The unique name of the dataset.

    data_dir : string, optional
        Path of the data directory. Used to force data storage in a specified
        location. Default: None

    default_paths : list of string, optional
        Default system paths in which the dataset may already have been
        installed by a third party software. They will be checked first.

    verbose : int, optional
        Verbosity level (0 means no message). Default=1.

    Returns
    -------
    data_dir : string
        Path of the given dataset directory.

    Notes
    -----
    This function retrieves the datasets directory (or data directory) using
    the following priority :

        1. defaults system paths
        2. the keyword argument data_dir
        3. the global environment variable TOY_PKG_SHARED_DATA
        4. the user environment variable TOY_PKG_DATA
        5. toy_pkg_data in the user home folder

    """
    paths = []
    # Search possible data-specific system paths
    if default_paths is not None:
        for default_path in default_paths:
            paths.extend([(d, True) for d in default_path.split(os.pathsep)])

    paths.extend([(d, False) for d in get_data_dirs(data_dir=data_dir)])

    if verbose > 2:
        print('Dataset search paths: %s' % paths)

    # Check if the dataset exists somewhere
    for path, is_pre_dir in paths:
        if not is_pre_dir:
            path = os.path.join(path, dataset_name)
        if os.path.islink(path):
            # Resolve path
            path = readlinkabs(path)
        if os.path.exists(path) and os.path.isdir(path):
            if verbose > 1:
                print('\nDataset found in %s\n' % path)
            return path

    # If not, create a folder in the first writeable directory
    errors = []
    for (path, is_pre_dir) in paths:
        if not is_pre_dir:
            path = os.path.join(path, dataset_name)
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                if verbose > 0:
                    print('\nDataset created in %s\n' % path)
                return path
            except Exception as exc:
                short_error_message = getattr(exc, 'strerror', str(exc))
                errors.append('\n -{0} ({1})'.format(
                    path, short_error_message))

    raise OSError('toy_pkg tried to store the dataset in the following '
                  'directories, but:' + ''.join(errors))


def movetree(src, dst):
    """Move an entire tree to another directory. Any existing file is
    overwritten"""
    names = os.listdir(src)

    # Create destination dir if it does not exist
    if not os.path.exists(dst):
        os.makedirs(dst)
    errors = []

    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.isdir(srcname) and os.path.isdir(dstname):
                movetree(srcname, dstname)
                os.rmdir(srcname)
            else:
                shutil.move(srcname, dstname)
        except (IOError, os.error) as why:
            errors.append((srcname, dstname, str(why)))
        # catch the Error from the recursive movetree so that we can
        # continue with other files
        except Exception as err:
            errors.extend(err.args[0])
    if errors:
        raise Exception(errors)


def _fetch_files(data_dir, files, resume=True, verbose=1):
    """Load requested dataset, downloading it if needed or requested.
    This function retrieves files from the hard drive or download them from
    the given urls. Note to developpers: All the files will be first
    downloaded in a sandbox and, if everything goes well, they will be moved
    into the folder of the dataset. This prevents corrupting previously
    downloaded data. In case of a big dataset, do not hesitate to make several
    calls if needed.

    Parameters
    ----------
    data_dir : string
        Path of the data directory. Used for data storage in a specified
        location.

    files : list of (string, string, dict)
        List of files and their corresponding url with dictionary that contains
        options regarding the files. Eg. (file_path, url, opt). If a file_path
        is not found in data_dir, as in data_dir/file_path the download will
        be immediately cancelled and any downloaded files will be deleted.
        Options supported are:
            * 'move' if renaming the file or moving it to a subfolder is needed
            * 'uncompress' to indicate that the file is an archive
            * 'md5sum' to check the md5 sum of the file
            * 'overwrite' if the file should be re-downloaded even if it exists

    resume : bool, optional
        If true, try resuming download if possible. Default=True.

    verbose : int, optional
        Verbosity level (0 means no message). Default=1.

    Returns
    -------
    files : list of string
        Absolute paths of downloaded files on disk.

    """
    # There are two working directories here:
    # - data_dir is the destination directory of the dataset
    # - temp_dir is a temporary directory dedicated to this fetching call. All
    #   files that must be downloaded will be in this directory. If a corrupted
    #   file is found, or a file is missing, this working directory will be
    #   deleted.
    files = list(files)
    files_pickle = pickle.dumps([(file_, url) for file_, url, _ in files])
    files_md5 = hashlib.md5(files_pickle).hexdigest()
    temp_dir = os.path.join(data_dir, files_md5)

    # Create destination dir
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Abortion flag, in case of error
    abort = None

    files_ = []
    for file_, url, opts in files:
        # 3 possibilities:
        # - the file exists in data_dir, nothing to do.
        # - the file does not exists: we download it in temp_dir
        # - the file exists in temp_dir: this can happen if an archive has been
        #   downloaded. There is nothing to do

        # Target file in the data_dir
        target_file = os.path.join(data_dir, file_)
        # Target file in temp dir
        temp_target_file = os.path.join(temp_dir, file_)
        # Whether to keep existing files
        overwrite = opts.get('overwrite', False)
        if (abort is None and (overwrite or (not os.path.exists(target_file) and not
                os.path.exists(temp_target_file)))):

            # We may be in a global read-only repository. If so, we cannot
            # download files.
            if not os.access(data_dir, os.W_OK):
                raise ValueError('Dataset files are missing but dataset'
                                 ' repository is read-only. Contact your data'
                                 ' administrator to solve the problem')

            if not os.path.exists(temp_dir):
                os.mkdir(temp_dir)
            dl_file = _fetch_file(url, temp_dir, resume=resume,
                                  verbose=verbose,
                                  overwrite=overwrite)

        if (abort is None and not os.path.exists(target_file) and not
                os.path.exists(temp_target_file)):
            warnings.warn('An error occured while fetching %s' % file_)
            abort = ("Dataset has been downloaded but requested file was "
                     "not provided:\nURL: %s\n"
                     "Target file: %s\nDownloaded: %s" %
                     (url, target_file, dl_file))
        if abort is not None:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
            raise IOError('Fetching aborted: ' + abort)
        files_.append(target_file)
    # If needed, move files from temps directory to final directory.
    if os.path.exists(temp_dir):
        # XXX We could only moved the files requested
        # XXX Movetree can go wrong
        movetree(temp_dir, data_dir)
        shutil.rmtree(temp_dir)
    return files_


def _fetch_file(url, data_dir, resume=True, overwrite=False,
                md5sum=None, verbose=1):
    """Load requested file, downloading it if needed or requested.

    Parameters
    ----------
    url : string
        Contains the url of the file to be downloaded.

    data_dir : string
        Path of the data directory. Used for data storage in the specified
        location.

    overwrite : bool, optional
        If true and file already exists, delete it. Default=False.

    md5sum : string, optional
        MD5 sum of the file. Checked if download of the file is required.

    verbose : int, optional
        Verbosity level (0 means no message). Default=1.

    Returns
    -------
    files : string
        Absolute path of downloaded file.

    Notes
    -----
    If, for any reason, the download procedure fails, all downloaded files are
    removed.

    """
    # Determine data path
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    # Determine filename using URL
    parse = urllib.parse.urlparse(url)
    file_name = os.path.basename(parse.path)
    full_name = os.path.join(data_dir, file_name)
    if not os.path.exists(full_name):
        _fake_download(full_name)
    return full_name


def _fake_download(name):
    """

    """
    datasets_gen_params = {'fake_dataset_1.csv':
                                {'dataset_number': 1,
                                 'number_of_lines': 206,
                                 'random_state': 0,
                                 'sleep_time': 10,
                                },
                           'fake_dataset_2_part1.csv':
                                {'dataset_number': 2,
                                 'number_of_lines': 500,
                                 'random_state': 42,
                                 'sleep_time': 30,
                                 },
                           'fake_dataset_2_part2.csv':
                                {'dataset_number': 2,
                                 'number_of_lines': 600,
                                 'random_state': 66,
                                 'sleep_time': 40,
                                 },
                           'fake_dataset_3.csv':
                                {'dataset_number': 3,
                                 'number_of_lines': 800,
                                 'random_state': 37,
                                 'sleep_time': 120,
                                 },
                           }
    short_name = os.path.basename(name)
    if short_name not in datasets_gen_params:
        raise ValueError("Unknown dataset {}".format(name))
    else:
        data = _dataset_gen(**datasets_gen_params[short_name])
        data.to_csv(name)


def _dataset_gen(dataset_number=1, number_of_lines=200, random_state=0, sleep_time=0):
    """

    """
    print("Downloading dataset {}...".format(dataset_number))
    rand_gen = check_random_state(random_state)
    _data = rand_gen.randint(0, 1000, (number_of_lines, 2))
    data = pd.DataFrame(_data, columns=['first term', 'second term'])
    time.sleep(sleep_time) # Sleep to simulate download...
    return data
