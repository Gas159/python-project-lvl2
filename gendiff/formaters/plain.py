def to_plain(diff_tree: dict) -> str:
    result = conversion(make_plain(diff_tree))
    return result


def make_plain(data: dict, parent_key="") -> list:
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
                             f" {to_str(value.get('value'))}")

            elif type == "deleted":
                lines.append(f"Property '{key}' was removed")

            elif type == "changed":
                lines.append(f"Property '{key}' was updated. From "
                             f"{to_str(value.get('value1'))} to "
                             f"{to_str(value.get('value2'))}")

            elif type == "nested":
                nested_value = (make_plain(value.get('children'), key))
                [lines.append(i) for i in nested_value]

    return lines


def conversion(data: list) -> str:
    return '\n'.join(data)


def to_str(item: any) -> str:
    if isinstance(item, dict):
        return '[complex value]'
    elif isinstance(item, str):
        return f"'{item}'"
    elif item is True:
        return 'true'
    elif item is False:
        return 'false'
    elif item is None:
        return 'null'
    else:
        return str(item)
