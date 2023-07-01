"""
FILE: constants.py
DESCRIPTION:
    Constants for the app.
"""

__authors__ = ["Sandeep Sen"]
__copyright__ = "Copyright 2023, Sandeep Sen, Sumit Dass"
__date__ = "2023/06/15"
__license__ = "MIT"
__version__ = "0.1.0"

# Defaults
DEFAULT_CONFIG_FILE = 'config.json'
DEFAULT_CALIBRATION_FILE = 'calibration.json'
DEFAULT_OUTPUT_DIR = 'output'
DEFAULT_LEFT_SUFFIX = '_left'
DEFAULT_RIGHT_SUFFIX = '_right'
DEFAULT_FILE_EXTENSION = '.tiff'
DEFAULT_FILE_MATCH_PATTERN = r"-\d{14}-\d{1,3}"

# Json schema
JSON_CALIBRATE = 'calibrate'
JSON_RECTIFY = 'rectify'
JSON_DIRECTORY_PATH = 'directoryPath'

# Identifiers
LEFT_IMAGE = "left_image"
RIGHT_IMAGE = "right_image"
