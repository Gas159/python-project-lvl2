from gendiff.formaters.json import to_json
from gendiff.formaters.plain import to_plain
from gendiff.formaters.stylish import to_stylish


def build_format_diff_tree(tree: dict, format_name: str, ) -> object:
    if format_name == 'stylish':
        return to_stylish(tree)
    if format_name == 'plain':
        return to_plain(tree)
    if format_name == 'json':
        return to_json(tree)
    raise ValueError(f'{format_name} notFoundError ')
