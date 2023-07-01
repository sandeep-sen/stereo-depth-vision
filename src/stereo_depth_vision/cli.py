"""
FILE: cli.py
DESCRIPTION:
    This is the cli files and handles cli for the app.
USAGE:
"""

__authors__ = ["Sandeep Sen"]
__copyright__ = "Copyright 2023, Sandeep Sen, Sumit Dass"
__date__ = "2023/06/15"
__license__ = "MIT"
__version__ = "0.1.0"

from typer import Typer
import _file_handler as file_handler
import _constants as constants
from _data_validator import DataValidator
from _calibrator import Calibrator
import logging
from datetime import datetime

app = Typer()


def logging_setup():
    file_handler.make_dir(constants.DEFAULT_OUTPUT_DIR)
    logging.basicConfig(filename=file_handler.join_path(
        constants.DEFAULT_OUTPUT_DIR,
        datetime.now().strftime('logfile-%Y-%m-%d-%H-%M-%S.log')),
        format='%(asctime)s - %(levelname)s : %(message)s',
        datefmt="%Y-%m-%dT%H:%M:%SZ",
        filemode='w')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

def _validate_and_read_config_file(config):
    if not file_handler.is_file(config):
        raise FileNotFoundError(
            'Configuration file does not exist: %s' % config)

    return file_handler.read_json_file(config)
    

def _validate_config_file_data(json_data, check_calibrate, check_rectify):
    error_string = 'JSON.Parse expected property:%s not found in config file'
    if check_calibrate:
        if constants.JSON_CALIBRATE not in json_data:
            raise SyntaxError(error_string % constants.JSON_CALIBRATE)
        if constants.JSON_DIRECTORY_PATH not in json_data[constants.JSON_CALIBRATE]:
            raise SyntaxError(error_string % constants.JSON_DIRECTORY_PATH)
    if check_rectify:
        if constants.JSON_RECTIFY not in json_data:
            raise SyntaxError(error_string % constants.JSON_RECTIFY)
        if constants.JSON_DIRECTORY_PATH not in json_data[constants.JSON_RECTIFY]:
            raise SyntaxError(error_string % constants.JSON_DIRECTORY_PATH)


@app.command()
def calibrate(config: str = constants.DEFAULT_CONFIG_FILE):
    try:
        logging_setup()
        json_data = _validate_and_read_config_file(config)
        _validate_config_file_data(json_data, True, False)
        calibrate_path = json_data[constants.JSON_CALIBRATE][constants.JSON_DIRECTORY_PATH]

        dv = DataValidator()
        file_pair_dict = dv.validate_calibration_data(calibrate_path)

        cb = Calibrator()
        cb.calibrate(file_pair_dict)
    except Exception as e:
        logging.exception(e)
        print(e)


@app.command()
def rectify(config: str = constants.DEFAULT_CONFIG_FILE):
    try:
        logging_setup()
        json_data = _validate_and_read_config_file(config)
        _validate_config_file_data(json_data, True, False)
        calibrate_path = json_data[constants.JSON_RECTIFY][constants.JSON_DIRECTORY_PATH]

        # dv = DataValidator()
        # file_pair_dict = dv.validate_calibration_data(calibrate_path)

        # rf = Rectifier()
        # rf.rectify(file_pair_dict)
    except Exception as e:
        logging.exception(e)
        print(e)

if __name__ == "__main__":
    app()
