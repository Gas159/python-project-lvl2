from gendiff import generate_diff
# from gendiff.diff import read_path
from tests.fixtures.expected_result import simply
from gendiff.scripts.gendiff import main



def test_generate_diff_good():
    simply = open('tests/fixtures/result_json').read()
    # print('!!!!!!!!!!!!!!!!!!! ...........',simply)
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == simply
    assert generate_diff('tests/fixtures/file1.yaml',
                         'tests/fixtures/file2.yaml') == simply



def test_generate_diff_type():
    assert isinstance( generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json'), str), '!!!!'


# def test_gendiff():
#     simply = open('tests/fixtures/result_json').read()
#     print('!!!!!!!!!!!!!!!!!!! ...........', simply)
#     assert main('tests/fixtures/file1.json',
#                          'tests/fixtures/file2.json') == simply
