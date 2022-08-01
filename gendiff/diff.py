#!/usr/bin/env python3
import json
import os
import pathlib


def read_path(file_path):
    q = os.path.basename(file_path)
    w = os.path.abspath(q)
    print(w, '===== it is abspath')
    print(q, ' ====== it is basename')
    # json.load(open('path/to/file.json'))
    # return json.load(open(file_path))
    path = pathlib.Path(__file__)
    return path
    # print('Read path\n',first_file)


def make_row(dictionary, key, operator=" "):
    return f'  {operator} {key} : {str(dictionary.get(key)).lower()}\n'


def generate_diff(source1, source2):
    first = json.load(open(source1))
    second = json.load(open(source2))
    # second = read_path(source2)
    print('it"s first', first, second, sep="\n", end='\n\n')

    common = first.keys() & second.keys()
    only_first = set(first) - set(second)
    only_second = set(second) - set(first)
    array_sorted = sorted(common | only_second | only_first)
    # print(f'Common:     {common} \nOnly_first: {only_first}\nOnly_second:'
    #       f'{only_second} \narr_sorted {array_sorted}')

    result = "{\n"
    for key in array_sorted:
        if key in common:
            if first.get(key) == second.get(key):
                result += make_row(first, key)
            else:
                result += make_row(first, key, "-")
                result += make_row(second, key, "+")
        elif key in only_first:
            result += make_row(first, key, '-')
        else:
            result += make_row(second, key, '+')
    result += '}'
    print(result)
    return result

# '/home/gastello/python-project-lvl2/gendiff/test/fixtures/file1.json'

q = generate_diff('/home/gastello/python-project-lvl2/gendiff/tests/fixtures/file1.json',
'/home/gastello/python-project-lvl2/gendiff/tests/fixtures/file2.json')

# poetry run gendiff
# /home/gastello/python-project-lvl2/gendiff/tests/fixtures/file1.json
# /home/gastello/python-project-lvl2/gendiff/tests/fixtures/file2.json
