# !/usr/bin/env python3
from gendiff.make_tree import make_tree
from gendiff.reader import read_path
from gendiff.formaters.get_format import select_format


def generate_diff(source1, source2, format='stylish'):
    first = read_path(source1)
    second = read_path(source2)
    tree = make_tree(first, second)
    return select_format(tree, format)
