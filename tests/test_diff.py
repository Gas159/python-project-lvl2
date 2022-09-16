from gendiff import generate_diff
import pytest

JSON = 'json'
STYLISH = 'stylish'
PLAIN = 'plain'

pytestmark = pytest.mark.parametrize(
    'first_path, second_path, expected, formatter',
    [
        ('tests/fixtures/file1.json', 'tests/fixtures/file2.json',
         'tests/fixtures/result_simply_json', STYLISH
         ),
        ('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml',
         'tests/fixtures/result_simply_json', STYLISH
         ),
        ('tests/fixtures/recur_file1.json', 'tests/fixtures/recur_file2.json',
         'tests/fixtures/result_stylish', STYLISH
         ),
        ('tests/fixtures/recur_file1.yaml', 'tests/fixtures/recur_file2.yaml',
         'tests/fixtures/result_stylish', STYLISH
         ),

        ('tests/fixtures/recur_file1.json', 'tests/fixtures/recur_file2.json',
         'tests/fixtures/result_recur_json', JSON
         ),
        ('tests/fixtures/recur_file1.yaml', 'tests/fixtures/recur_file2.yaml',
         'tests/fixtures/result_recur_json', JSON
         ),
        ('tests/fixtures/recur_file1.json', 'tests/fixtures/recur_file2.json',
         'tests/fixtures/result_plain', PLAIN
         ),
        ('tests/fixtures/recur_file1.yaml', 'tests/fixtures/recur_file2.yaml',
         'tests/fixtures/result_plain', PLAIN
         )
    ]
)


def test_generate_diff(first_path: str, second_path: str, expected: str,
                       formatter: str):
    result = open(expected).read()
    assert generate_diff(first_path, second_path, formatter) == result
    assert isinstance(generate_diff(first_path, second_path), str)
