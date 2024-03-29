def to_plain(diff_tree: dict) -> str:
    return build_plain(diff_tree)


def build_plain(data: dict, parent_key=""):
    lines = []
    for elem in sorted(data.items()):
        key, value = elem
        if value.get('type') != 'unchanged':

            value_of_type = value.get('type')
            current_key = key
            if parent_key:
                key = f'{parent_key}.{current_key}'
            else:
                key = current_key

            if value_of_type == "added":
                lines.append(f"Property '{key}' was added with value:"
                             f" {to_str(value.get('value'))}")

            elif value_of_type == "deleted":
                lines.append(f"Property '{key}' was removed")

            elif value_of_type == "changed":
                lines.append(f"Property '{key}' was updated. From "
                             f"{to_str(value.get('value_old'))} to "
                             f"{to_str(value.get('value_new'))}")

            elif value_of_type == "nested":
                nested_values = (build_plain(value.get('children'), key))
                lines += [nested_values]
    return '\n'.join(lines)


def to_str(item: any) -> str:
    if isinstance(item, dict):
        return '[complex value]'
    if isinstance(item, str):
        return f"'{item}'"
    if isinstance(item, bool):
        return str(item).lower()
    if item is None:
        return 'null'
    return str(item)
