from gendiff.formaters.json import to_json
from gendiff.formaters.plain import to_plain
from gendiff.formaters.stylish import to_stylish


def build_format_diff_tree(tree: dict, name_format: str, ) -> object:
    if name_format == 'stylish':
        return to_stylish(tree)
    if name_format == 'plain':
        return to_plain(tree)
    if name_format == 'json':
        return to_json(tree)
    raise ValueError(f'{name_format} notFoundError ')
