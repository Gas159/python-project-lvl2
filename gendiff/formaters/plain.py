def to_plain(diff_tree: dict) -> str:
    result = conversion(make_plain(diff_tree))
    return result


def make_plain(data: dict, parent_key="") -> list:
    lines = []
    for elem in sorted(data.items()):
        key, value = elem
        if value.get('type') != 'unchanged':

            value_of_type = value.get('type')
            curent_key = key

            if parent_key:
                key = f"{parent_key}.{curent_key}"
            else:
                key = curent_key

            if value_of_type == "added":
                lines.append(f"Property '{key}' was added with value:"
                             f" {to_str(value.get('value'))}")

            elif value_of_type == "deleted":
                lines.append(f"Property '{key}' was removed")

            elif value_of_type == "changed":
                lines.append(f"Property '{key}' was updated. From "
                             f"{to_str(value.get('value1'))} to "
                             f"{to_str(value.get('value2'))}")

            elif value_of_type == "nested":
                nested_value = (make_plain(value.get('children'), key))
                [lines.append(i) for i in nested_value]

    return lines


def conversion(data: list) -> str:
    return '\n'.join(data)


def to_str(item: any) -> str:
    if isinstance(item, dict):
        return '[complex value]'
    if isinstance(item, str):
        return f"'{item}'"
    if item is True:
        return 'true'
    if item is False and item == 0:
        return 'false'
    if item is None:
        return 'null'
    return str(item)
