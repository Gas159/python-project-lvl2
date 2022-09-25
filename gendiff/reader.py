import os.path
import json
import yaml


def read_path(file_path):
    root, extension = os.path.splitext(file_path)
    if extension == '.json':
        return to_json(file_path)
    if extension in ('.yaml', '.yml'):
        return to_yaml(file_path)
    raise FileNotFoundError


def to_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        file = json.load(f)
        return file


def to_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        file = yaml.safe_load(f)
        return file
