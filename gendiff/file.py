import os.path
import json
import yaml


def get_file_content(path):
    _, extension = os.path.splitext(path)
    with open(path, 'r', encoding='utf-8') as file:
        return parse(file, extension[1:])


def parse(content, format):
    if format == 'json':
        return json.load(content)
    if format in ('yaml', 'yml'):
        return yaml.safe_load(content)
    raise Exception('content or formatter not found')
