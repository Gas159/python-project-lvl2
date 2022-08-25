# !/usr/bin/env python3
import json
from pathlib import Path
import yaml

from gendiff.formaters.json import to_json
from gendiff.formaters.plain import to_plain
from gendiff.formaters.stylish import stylish


def generate_diff(source1, source2, format='stylish'):
    first = read_path(source1)
    second = read_path(source2)
    tree = make_tree(first, second)
    if format == 'stylish':
        return stylish(tree)
    elif format == 'plain':
        return to_plain(tree)
    elif format == 'json':
        return to_json(tree)
    else:
        return tree


def read_path(file_path):
    extension = Path(file_path).suffix
    if extension == '.json':
        return json.load(open(file_path))
    elif extension == '.yaml' or extension == '.yml':
        return yaml.safe_load(open(file_path))


def make_tree(data1: dict, data2: dict) -> dict:
    result = {}
    set1 = set(data1)
    set2 = set(data2)
    add_keys = set(set2 - set1)
    del_keys = set(set1 - set2)

    for key in set1 | set2:
        if key in add_keys:
            result[key] = {'type': 'added', 'value': data2.get(key)}

        elif key in del_keys:
            result[key] = {'type': 'deleted', 'value': data1.get(key)}

        else:
            if isinstance(data1.get(key), dict) and isinstance(data2.get(
                    key), dict):
                result[key] = {
                    'type': 'nested',
                    'children': make_tree(data1.get(key), data2.get(key))
                }

            elif data1.get(key) == data2.get(key):
                result[key] = {'type': 'unchanged', 'value': data1.get(key)}

            else:
                result[key] = {'type': 'changed', 'value1': data1.get(key),
                               'value2': data2.get(key)}

    return result
