from gendiff.diff import generate_diff
# from gendiff.diff import read_path
from gendiff.tests.fixtures.expected_result import simply


def test_generate_diff():
    assert generate_diff(
        '/home/gastello/python-project-lvl2/gendiff/tests/fixtures/file1.json',
        '/home/gastello/python-project-lvl2/gendiff/tests/fixtures/file2.json')\
        == simply
