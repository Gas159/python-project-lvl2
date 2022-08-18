import json


def to_json(diff_tree: dict) -> str:
    return json.dumps(diff_tree, sort_keys=True, indent=2)
