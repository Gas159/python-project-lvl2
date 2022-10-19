from itertools import chain

ADDED = "  + "
DELETED = '  - '
UNCHANGED = '    '
CHANGED = '    '
COMMON = '    '


def to_stylish(diff_tree):
    """
    Reformat a diff tree to style it.
    """
    return built_stylish(diff_tree)


def built_stylish(tree: dict, depth=0, replacer='    '):
    lines = []
    indent = depth * replacer

    for key, val in sorted(tree.items()):

        if val.get("type") == "added":
            lines.append(built_line(
                indent, key, val.get('value'), ADDED, depth))

        elif val.get("type") == "deleted":
            lines.append(built_line(
                indent, key, val.get('value'), DELETED, depth))

        elif val.get("type") == "unchanged":
            lines.append(built_line(
                indent, key, val.get('value'), UNCHANGED, depth))

        elif val.get("type") == "changed":
            lines.append(built_line(
                indent, key, val.get('value_old'), DELETED, depth))

            lines.append(built_line(
                indent, key, val.get('value_new'), ADDED, depth))

        elif val.get("type") == "nested":
            new_value = built_stylish(val.get('children'), depth + 1)
            lines.append(f'{indent}{COMMON}{key}: {new_value}')

    res = chain('{', lines, [indent + '}'])
    return '\n'.join(res)


def to_str(item, depth=0):
    if isinstance(item, bool):
        return str(item).lower()
    if str(item) == 'None':
        return 'null'
    if isinstance(item, dict):
        lines = ['{']
        for key, nested_value in item.items():
            if isinstance(nested_value, dict):
                new_value = to_str(nested_value, depth + 1)
                lines.append(f"{'    ' * depth}    {key}: {new_value}")
            else:
                lines.append(f"{'    ' * depth}    {key}: {nested_value}")
        lines.append(f'{"    " * depth}}}')

        return '\n'.join(lines)
    return item


def built_line(indent, key, value, types='', depth=0):
    return f"{indent}{types}{key}: {to_str(value, depth + 1)}"
