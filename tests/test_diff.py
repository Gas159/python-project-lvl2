import os.path
import pytest
from gendiff import generate_diff


@pytest.mark.parametrize(
    'first_path, second_path, expected, formatter',
    [
        ('file1.json', 'file2.json', 'result_simply_json', 'stylish'),
        ('file1.yaml', 'file2.yaml', 'result_simply_json', 'stylish'),
        ('recur_file1.json', 'recur_file2.json', 'result_stylish', 'stylish'),
        ('recur_file1.yaml', 'recur_file2.yaml', 'result_stylish', 'stylish'),
        ('recur_file1.json', 'recur_file2.json', 'result_recur_json', 'json'),
        ('recur_file1.yaml', 'recur_file2.yaml', 'result_recur_json', 'json'),
        ('recur_file1.json', 'recur_file2.json', 'result_plain', 'plain'),
        ('recur_file1.yaml', 'recur_file2.yaml', 'result_plain', 'plain')
    ]
)
def test_generate_diff(first_path: str, second_path: str, expected: str,
                       formatter: str):
    file_1 = generate_fixture_path(first_path)
    file_2 = generate_fixture_path(second_path)
    expected_file_path = generate_fixture_path(expected)
    with open(expected_file_path, 'r', encoding='utf-8') as f:
        expected_result = f.read()
        assert generate_diff(file_1, file_2, formatter) == expected_result
        assert isinstance(generate_diff(file_1, file_2), str)


def generate_fixture_path(name: str) -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, 'fixtures', name)
    return path
