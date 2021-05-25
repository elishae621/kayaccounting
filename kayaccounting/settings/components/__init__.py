from pathlib import Path, PurePath
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Load config file from config json file
with open(BASE_DIR / 'config.json') as config_json:
    config = json.load(config_json)
