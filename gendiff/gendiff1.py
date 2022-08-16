# !/usr/bin/env python3
import json
from pathlib import Path
import yaml
from pprint import pprint  # noqa

from gendiff.formaters.stylish import stylish


def generate_diff(source1, source2, format='stylish'):
    first = read_path(source1)
    second = read_path(source2)
    tree = make_tree(first, second)
    if format == 'stylish':
        return stylish(tree)
    # if format == 'plain':
    #     return plain(tree)
    return tree


def read_path(file_path):
    # q = os.path.basename(file_path)
    # w = os.path.abspath(file_path)
    extension = Path(file_path).suffix
    # t = Path(Path.home(), file_path)
    # print(w, '===== it is abspath')
    # print(q, ' ====== it is basename')
    # print('extension', extension, sep='\n', end='\n\n')
    # print(extension)
    # print(e.suffix)
    # print(t)
    # json.load(open('path/to/file.json'))
    # return json.load(open(file_path))
    # path = Path(__file__)
    # print(path)
    # file = open(file_path)
    if extension == '.json':
        return json.load(open(file_path))
    elif extension == '.yaml' or extension == '.yml':
        return yaml.safe_load(open(file_path))


def make_tree(data1: dict, data2: dict) -> dict: # noqa 901
    result = {}
    set1 = set(data1)
    set2 = set(data2)
    # com_keys = set(set1 & set2)
    # print(com_keys)
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

# '/home/gastello/python-project-lvl2/gendiff/test/fixtures/file1.json'

# q = generate_diff(
#     '/home/gastello/python-project-lvl2/tests/fixtures/file1.json',
#     '/home/gastello/python-project-lvl2/tests/fixtures/file2.json')
#
# q =generate_diff(
# '/home/gastello/python-project-lvl2/tests/fixtures/file1.yaml',
# '/home/gastello/python-project-lvl2/tests/fixtures/file2.yaml')
# print(q)

q = generate_diff(
    '/home/gastello/python-project-lvl2/tests/fixtures/recur_file1.json',
    '/home/gastello/python-project-lvl2/tests/fixtures/recur_file2.json')
# print('\n\n')
# print(type(q), q)
print(q)

# poetry run gendiff
# /home/gastello/python-project-lvl2/gendiff/tests/fixtures/file1.json
# /home/gastello/python-project-lvl2/gendiff/tests/fixtures/file2.json
