def to_plain(diff_tree: dict) -> str:
    return make_plain(diff_tree)


def make_plain(data: dict, parent_key=""):
    lines = []
    for elem in sorted(data.items()):
        key, value = elem
        if value.get('type') != 'unchanged':

            value_of_type = value.get('type')
            current_key = key
            key = get_key(parent_key, current_key)

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
                nested_values = (make_plain(value.get('children'), key))
                lines += [nested_values]
    return '\n'.join(lines)


def get_key(value, current_key):
    if value:
        return f"{value}.{current_key}"
    return current_key


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
