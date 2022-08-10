# !/usr/bin/env python3
import json
from pathlib import Path
import yaml
from itertools import chain
from pprint import pprint


def generate_diff(source1, source2, format='Stylish'):
    first = read_path(source1)
    second = read_path(source2)
    tree = make_tree(first, second)
    return stylish(tree, format)


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


def make_tree(data1: dict, data2: dict) -> dict:
    # print(data1, data2, sep='\n')
    result = {}
    set1 = set(data1)
    set2 = set(data2)
    com_keys = set(set1 & set2)
    add_keys = set(set2 - set1)
    del_keys = set(set1 - set2)
    # print(com_keys, add_keys, del_keys)
    for key in sorted(set1 | set2):
        if key in add_keys:
            result[key] = {'type': 'added', 'value': data2.get(key)}
            # print('Added -- ', key, result[key])
        elif key in del_keys:
            result[key] = {'type': 'deleted', 'value': data1.get(key)}
            # print('Remove --', key, result[key])
        else:
            if isinstance(data1.get(key), dict) and isinstance(data2.get(
                    key), dict):
                result[key] = {'type': 'Nested', 'value': make_tree(
                    data1.get(key), data2.get(key))}
                # print('Nested', key, result[key])

            elif data1.get(key) == data2.get(key):
                result[key] = {'type': 'unchanged', 'value': data1.get(key)}
                # print('Unchage', key, result[key])
            else:  # data1.get(key) != data2.get(key):
                result[key] = {'type': 'Changed', 'value1': data1.get(key),
                               'value2': data2.get(key)}
                # print('Change', key, result[key])
    # print(result)
    return result


def stylish(diff_tree, format='stylish'):
    lines = []
    for key, value in diff_tree.items():
        if value.get('type') == 'added':
            lines.append(f'{unpack({key : value.get("value")})[:]}')

    print(lines)
    return '\n'.join(lines)





def unpack(dictionary,  depth = 0, space_count=1, replacer='----' ):
    lines = []
    res = ''
    cur = replacer * (depth + 1)
    indent = depth * replacer
    print('!!!',dictionary)

    for key,value in dictionary.items():
        print('key',key,'value',value)
        if isinstance(value,dict)  and value.get('type') == 'added':
            replacer = ' +  '
        else:
            replacer = '----'
        lines.append(f'{replacer}{key}:{value}') if not isinstance(
            value,
                                                               dict) else \
            lines.append(f'{cur}{key}: {{\n{unpack(value,depth +1)}\n{cur}}}')

        res = chain( lines )
    print(res)
    return '\n'.join(res)

q = stylish(
    {'group3': {'type': 'added', 'value': {'deep': {'id': {'number': 45}},
                                           'fee': 100500}}})
print('\n\n', q, sep='')

def make_row(key, value, operator=" "):
    return f'  {operator} {key} : {str(value.get(key))}\n'

    print('it"s first', first, second, type(first), sep="\n", end='\n\n')

    # common = first.keys() & second.keys()
    # only_first = set(first) - set(second)
    # only_second = set(second) - set(first)
    # array_sorted = sorted(common | only_second | only_first)
    #
    # result = "{\n"
    # for key in array_sorted:
    #     if key in common:
    #         if first.get(key) == second.get(key):
    #             result += make_row(first, key)
    #         else:
    #             result += make_row(first, key, "-")
    #             result += make_row(second, key, "+")
    #     elif key in only_first:
    #         result += make_row(first, key, '-')
    #     else:
    #         result += make_row(second, key, '+')
    # result += '}'
    # # print(result)
    # return result

# '/home/gastello/python-project-lvl2/gendiff/test/fixtures/file1.json'

# q = generate_diff(
#     '/home/gastello/python-project-lvl2/tests/fixtures/file1.json',
#     '/home/gastello/python-project-lvl2/tests/fixtures/file2.json')

# q = generate_diff(
#     '/home/gastello/python-project-lvl2/tests/fixtures/file1.yaml',
#     '/home/gastello/python-project-lvl2/tests/fixtures/file2.yaml')

# q = generate_diff(
#     '/home/gastello/python-project-lvl2/tests/fixtures/recur_file1.json',
#     '/home/gastello/python-project-lvl2/tests/fixtures/recur_file2.json')
# print('\n\n')
# print(type(q), q)

# poetry run gendiff
# /home/gastello/python-project-lvl2/gendiff/tests/fixtures/file1.json
# /home/gastello/python-project-lvl2/gendiff/tests/fixtures/file2.json
