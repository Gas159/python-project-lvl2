import os.path
import json
import yaml


def get_file_content(file_path):
    _, extension = os.path.splitext(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        return parse(file, extension)


def parse(file, file_format):
    if file_format == '.json':
        return json.load(file)
    if file_format in ('.yaml', '.yml'):
        return yaml.safe_load(file)
    raise FileNotFoundError('File or formatter not found')
