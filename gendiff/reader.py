from pathlib import Path
import json
import yaml


def read_path(file_path):
    extension = get_extension(file_path)
    if extension == '.json':
        with open(file_path, 'r') as f:
            return json.load(f)
    if extension in ('.yaml', '.yml'):
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)


def get_extension(item: str):
    return Path(item).suffix
