"""
FILE: file_handler.py
DESCRIPTION:
    This file performs read and write on a file in a disk.
USAGE:
"""

__authors__ = ["Sandeep Sen"]
__copyright__ = "Copyright 2023, Sandeep Sen, Sumit Dass"
__date__ = "2023/06/15"
__license__ = "MIT"
__version__ = "0.1.0"

import json
import re
from pathlib import Path


def read_file(path):
    try:
        with open(path, 'r') as f:
            data = f.read()
        return data
    except Exception as e:
        e.args = ('Error while trying to read file: %s' % path, *e.args)
        raise


def make_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def write_to_file(path, data):
    # TODO: Error handling
    with open(path, 'w') as f:
        f.write(data)

def read_json_file(path):
    try:
        data = read_file(path)
        return json.loads(data)
    except Exception as e:
        e.args = ('Error while trying to read json file: %s' % path, *e.args)
        raise

def join_path(path_leading, path_trailing):
    return str(Path(path_leading).joinpath(path_trailing))

def is_dir(path):
    try:
        return Path(path).is_dir()
    except Exception as e:
        e.args = ('Error while verifying status of directory: %s' %
                  path, *e.args)
        raise


def is_file(path):
    try:
        return Path(path).is_file()
    except Exception as e:
        e.args = ('Error while verifying status of file: %s' % path, *e.args)
        raise


def get_matched_dir_list(path, suffix=None):
    try:
        return list(filter(Path.is_dir, Path(path).glob(f"*{'' if suffix is None else suffix}")))
    except Exception as e:
        e.args = ('Error while getting list of subdirectories from: %s, pattern: %s' 
                  %path % suffix, *e.args)
        raise


def get_matched_file_dict(path, suffix=None, match_pattern=None):
    try:
        file_dict = {}
        file_pattern = any
        if match_pattern is not None:
            file_pattern = re.compile(str(match_pattern))
        for item in Path(path).glob(f"*{'' if suffix is None else suffix}"):
            if item.is_file():
                if match_pattern is not None:
                    match = file_pattern.search(item.name)
                    if match:
                        file_dict[match.group()] = item.absolute()
                else:
                    file_dict[item.name] = item.absolute()
        return file_dict
    except Exception as e:
        e.args = ('Error while getting list of files in directory: %s, extension:%s, pattern:%s' 
                  %path % suffix % match_pattern, *e.args)
        raise
