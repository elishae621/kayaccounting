from pathlib import Path, PurePath
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# conf_location = BASE_DIR / 'config.json'

conf_location = '/etc/kayaccounting.json'

# Load config file from config json file
with open(conf_location) as config_json:
    config = json.load(config_json)
