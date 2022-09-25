from gendiff.formaters.json import to_json
from gendiff.formaters.plain import to_plain
from gendiff.formaters.stylish import stylish


def select_format(tree: dict, item: str, ):
    if item == 'stylish':
        return stylish(tree)
    if item == 'plain':
        return to_plain(tree)
    if item == 'json':
        return to_json(tree)
    return tree
