from gendiff.formaters.json import to_json
from gendiff.formaters.plain import to_plain
from gendiff.formaters.stylish import stylish


def select_format(tree: dict, item: str, ):
    if item == 'stylish':
        return stylish(tree)
    elif item == 'plain':
        return to_plain(tree)
    elif item == 'json':
        return to_json(tree)
    else:
        return tree
