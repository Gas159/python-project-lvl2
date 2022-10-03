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
                             f"{to_str(value.get('old'))} to "
                             f"{to_str(value.get('new'))}")

            elif value_of_type == "nested":
                nested_values = (make_plain(value.get('children'), key))
                # [lines.append(i) for i in nested_values]
                lines.append([nested_values])
    return '\n'.join(lines)


# def make_plain(data: dict):
#     def inner(data, parent_key="") -> list:
#         lines = []
#         for elem in sorted(data.items()):
#             key, value = elem
#             if value.get('type') != 'unchanged':
#
#                 value_of_type = value.get('type')
#                 current_key = key
#                 key = get_key(parent_key, current_key)
#
#                 if value_of_type == "added":
#                     lines.append(f"Property '{key}' was added with value:"
#                                  f" {to_str(value.get('value'))}")
#
#                 elif value_of_type == "deleted":
#                     lines.append(f"Property '{key}' was removed")
#
#                 elif value_of_type == "changed":
#                     lines.append(f"Property '{key}' was updated. From "
#                                  f"{to_str(value.get('old'))} to "
#                                  f"{to_str(value.get('new'))}")
#
#                 elif value_of_type == "nested":
#                     nested_values = (inner(value.get('children'), key))
#                     [lines.append(i) for i in nested_values]
#
#         return lines
#
#     return '\n'.join(inner(data))
def get_key(value, current_key):
    if value:
        return f"{value}.{current_key}"
    return current_key


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
