from gendiff.diff_tree import make_diff_tree
from gendiff.file import get_file_content
from gendiff.formaters import build_format_diff_tree


def generate_diff(source1, source2, format_file='stylish'):
    data1 = get_file_content(source1)
    data2 = get_file_content(source2)
    tree = make_diff_tree(data1, data2)
    return build_format_diff_tree(tree, format_file)
