"""
FILE: data_validator.py
DESCRIPTION:
    This file validates if all data needed to process is available.
USAGE:
"""

__authors__ = ["Sandeep Sen"]
__copyright__ = "Copyright 2023, Sandeep Sen, Sumit Dass"
__date__ = "2023/06/19"
__license__ = "MIT"
__version__ = "0.1.0"

import _file_handler as file_handler
import _constants as constants


class DataValidator():
    def validate_calibration_data(self, dir_path):
        # checking if calibration directory is present
        if not file_handler.is_dir(dir_path):
            return False
        # getting the list of directories which match
        # left and right pattern from calibration directory
        left_dir_list = file_handler.get_matched_dir_list(
            dir_path, constants.DEFAULT_LEFT_SUFFIX)
        right_dir_list = file_handler.get_matched_dir_list(
            dir_path, constants.DEFAULT_RIGHT_SUFFIX)
        # checking if calibration left directory is present
        if left_dir_list.__len__() < 1:
            return False
        # checking if calibration right directory is present
        if right_dir_list.__len__() < 1:
            return False
        # check if files are present
        left_file_dict = file_handler.get_matched_file_dict(
            left_dir_list[0].absolute(),
            constants.DEFAULT_FILE_EXTENSION,
            constants.DEFAULT_FILE_MATCH_PATTERN)
        right_file_dict = file_handler.get_matched_file_dict(
            right_dir_list[0].absolute(),
            constants.DEFAULT_FILE_EXTENSION,
            constants.DEFAULT_FILE_MATCH_PATTERN)

        # check if file pairs are present
        file_pair_dict = {}
        for left_file in left_file_dict:
            if left_file in right_file_dict:
                file_pair_dict[left_file] = {
                    constants.LEFT_IMAGE: str(left_file_dict.get(left_file)), 
                    constants.RIGHT_IMAGE: str(right_file_dict.get(left_file))}

        return file_pair_dict
