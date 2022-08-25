import json


def to_plain(diff_tree: dict) -> str:
    result = make_row(diff_tree)
    return '\n'.join(result)


# flake8: noqa: 901
def make_row(data: dict, parent_key="") -> list:
    lines = []
    for elem in sorted(data.items()):
        key, value = elem
        if not value.get('type') == 'unchanged':

            type = value.get('type')
            curent_key = key

            if parent_key:
                key = f"{parent_key}.{curent_key}"
            else:
                key = curent_key

            if type == "added":
                lines.append(f"Property '{key}' was added with value:"
                             f" {check_type(value.get('value'))}")

            elif type == "deleted":
                lines.append(f"Property '{key}' was removed")

            elif type == "changed":
                lines.append(f"Property '{key}' was updated. From "
                             f"{check_type(value.get('value1'))} to "
                             f"{check_type(value.get('value2'))}")

            elif type == "nested":
                nested_value = (make_row(value.get('children'), key))
                [lines.append(i) for i in nested_value]

    return lines


def check_type(item: any) -> str:
    if isinstance(item, dict):
        return '[complex value]'
    elif type(item) is bool or item is None:
        return json.dumps(item)
    elif isinstance(item, str):
        return f"'{item}'"
    else:
        return item
