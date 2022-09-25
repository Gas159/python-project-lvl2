from pathlib import Path
import json
import yaml


def read_path(file_path):
    extension = get_extension(file_path)
    if extension == '.json':
        with open(file_path, 'r', encoding='utf-8') as file:
            res = json.load(file)
            return res
    if extension in ('.yaml', '.yml'):
        with open(file_path, 'r', encoding='utf-8') as file:
            res = yaml.safe_load(file)
            return res
    else:
        return None


def get_extension(item: str):
    return Path(item).suffix
