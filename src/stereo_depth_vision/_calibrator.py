"""
FILE: calibrator.py
DESCRIPTION:
    This file calibrates for a given set of left and right images.
USAGE:
"""

__authors__ = ["Sandeep Sen"]
__copyright__ = "Copyright 2023, Sandeep Sen, Sumit Dass"
__date__ = "2023/06/30"
__license__ = "MIT"
__version__ = "0.1.0"

import _constants as constants
import _file_handler as file_handler
import cv2 as cv


class Calibrator():
    def calibrate(self, file_pair_dict):
        pattern_size = (8, 9)
        chessboard_flag = cv.CALIB_CB_NORMALIZE_IMAGE + \
            cv.CALIB_CB_ADAPTIVE_THRESH + \
            cv.CALIB_CB_FILTER_QUADS

        for file_key in file_pair_dict:
            left_image = cv.imread(file_pair_dict.get(file_key).get(constants.LEFT_IMAGE),
                                   cv.IMREAD_UNCHANGED)
            right_image = cv.imread(file_pair_dict.get(file_key).get(constants.RIGHT_IMAGE),
                                    cv.IMREAD_UNCHANGED)

            found_left_cb, left_corners = cv.findChessboardCorners(
                left_image, pattern_size, chessboard_flag)
            
            found_right_cb, right_corners = cv.findChessboardCorners(
                right_image, pattern_size, chessboard_flag)
