import os.path
import sys

from gendiff import generate_diff
import pytest

JSON = 'json'
STYLISH = 'stylish'
PLAIN = 'plain'


@pytest.mark.parametrize(
    'first_path, second_path, expected, formatter',
    [
        ('file1.json', 'file2.json', 'result_simply_json', STYLISH),
        ('file1.yaml', 'file2.yaml', 'result_simply_json', STYLISH),
        ('recur_file1.json', 'recur_file2.json', 'result_stylish', STYLISH),
        ('recur_file1.yaml', 'recur_file2.yaml', 'result_stylish', STYLISH),
        ('recur_file1.json', 'recur_file2.json', 'result_recur_json', JSON),
        ('recur_file1.yaml', 'recur_file2.yaml', 'result_recur_json', JSON),
        ('recur_file1.json', 'recur_file2.json', 'result_plain', PLAIN),
        ('recur_file1.yaml', 'recur_file2.yaml', 'result_plain', PLAIN)
    ]
)
def test_generate_diff(first_path: str, second_path: str, expected: str,
                       formatter: str):
    file_1 = get_file_path(first_path)
    file_2 = get_file_path(second_path)
    expected_file_path = get_file_path(expected)
    expected_result = read_path(expected_file_path)

    assert generate_diff(file_1, file_2, formatter) == expected_result
    assert isinstance(generate_diff(file_1, file_2), str)


def read_path(file_path):
    try:
        with open(file_path, 'r') as f:
            res = f.read()
            return res
    except FileNotFoundError:
        print('File not found')
    except Exception:
        print('File open errors!')


def get_file_path(name):
    path = os.path.join('tests/fixtures', name)
    return path
