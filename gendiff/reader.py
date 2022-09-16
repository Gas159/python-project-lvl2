from pathlib import Path
import json
import yaml


def read_path(file_path):
    extension = get_extension(file_path)
    if extension == '.json':
        return json.load(open(file_path))
    elif extension == '.yaml' or extension == '.yml':
        return yaml.safe_load(open(file_path))


def get_extension(item: str):
    return Path(item).suffix
