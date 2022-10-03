from gendiff.diff_tree import make_tree
from gendiff.file import get_file
from gendiff.formaters import build_format_diff_tree


def generate_diff(source1, source2, format_file='stylish'):
    data1 = get_file(source1)
    data2 = get_file(source2)
    tree = make_tree(data1, data2)
    return build_format_diff_tree(tree, format_file)
