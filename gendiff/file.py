import os.path
import json
import yaml


def get_file(file_path):
    _, extension = os.path.splitext(file_path)
    return parse(file_path, extension)


def parse(path, file_format):
    with open(path, 'r', encoding='utf-8') as f:
        if file_format == 'json':
            return json.load(f)
        if file_format == 'yaml':
            return yaml.safe_load(f)
        raise FileNotFoundError('File or formatter not found')
