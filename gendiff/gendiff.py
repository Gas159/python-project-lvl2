from gendiff.diff_tree import make_tree
from gendiff.reader import read_path
from gendiff.formaters.format import select_format


def generate_diff(source1, source2, format_file='stylish'):
    data1 = read_path(source1)
    data2 = read_path(source2)
    tree = make_tree(data1, data2)
    return select_format(tree, format_file)
