from gendiff import generate_diff


def test_generate_diff():
    simply = open('tests/fixtures/result_simply_json').read()
    assert generate_diff('tests/fixtures/file1.json',
                         'tests/fixtures/file2.json') == simply
    assert generate_diff('tests/fixtures/file1.yaml',
                         'tests/fixtures/file2.yaml') == simply


def test_generate_diff_type():
    assert isinstance(generate_diff('tests/fixtures/file1.json',
                                    'tests/fixtures/file2.json'), str)


def test_generate_diff_recursive_stylish():
    stylish = open('tests/fixtures/result_stylish').read()
    assert generate_diff('tests/fixtures/recur_file1.json',
                         'tests/fixtures/recur_file2.json') == stylish
    assert generate_diff('tests/fixtures/recur_file1.yaml',
                         'tests/fixtures/recur_file2.yaml') == stylish


def test_generate_diff_recursive_plain():
    plain = open('tests/fixtures/result_plain').read()

    assert generate_diff('tests/fixtures/recur_file1.json',
                         'tests/fixtures/recur_file2.json', 'plain') == plain
    assert generate_diff('tests/fixtures/recur_file1.yaml',
                         'tests/fixtures/recur_file2.yaml', 'plain') == plain


def test_generate_diff_recursive_json():
    json = open('tests/fixtures/result_recur_json').read()

    assert generate_diff('tests/fixtures/recur_file1.json',
                         'tests/fixtures/recur_file2.json', 'json') == json
    assert generate_diff('tests/fixtures/recur_file1.yaml',
                         'tests/fixtures/recur_file2.yaml', 'json') == json
