# stereo-depth-vision
Depth mapping library with images in Python

## Dev environment setup

##### Prerequisite

- Python 3.11 or higher
- Pip is installed
- Virtual env is installed
    ```bash
    pip install virtualenv
    ``````

#### macOS or Linux including WSL2
```bash
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

#### Windows
```dos
virtualenv .env
source .env/Scripts/activate
pip install -r requirements.txt
```

## Debugging
Debug setup is already done in `launch.json` in `.vscode` directory. Use it to debug.
Configuration file is required to run this application create a `._data` directory and in it create `test_config.json`

JSON for testing and debugging.
```json
{
    "calibrate": {
        "directoryPath": "<path to your calibartion directory>"
    },
    "rectify": {
        "directoryPath": "path to image directory"
    },
    "leftDirPattern": "_left",
    "rightDirPattern": "_right",
    "imageExtension": ".tiff"
}
```