from gendiff import generate_diff
# from gendiff.diff import read_path
from tests.fixtures.expected_result import simply


def test_generate_diff():
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == simply
