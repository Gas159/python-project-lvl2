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
    result = built_stylish(diff_tree)
    return result


def built_stylish(tree: dict, depth=0, replacer='    '):
    lines = []
    res = ''
    indent = depth * replacer

    for key, val in sorted(tree.items()):

        if not isinstance(val, dict) or "type" not in val:
            lines.append(built_line(indent, key, val, UNCHANGED, depth))

        elif val.get("type") == "added":
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
                indent, key, val.get('old'), DELETED, depth))

            lines.append(built_line(
                indent, key, val.get('new'), ADDED, depth))

        elif val.get("type") == "nested":
            lines.append(built_line(
                indent, key, val.get('children'), COMMON, depth))

    res = chain('{', lines, [indent + '}'])
    return '\n'.join(res)


def to_str(item):
    if str(item) == "True":
        return "true"
    if str(item) == 'None':
        return 'null'
    if str(item) == 'False':
        return 'false'
    return item


def built_line(indent, key, value, types='', depth=0):
    return f'{indent}{types}{key}: {to_str(value)}' \
        if not isinstance(value, dict) \
        else f"{indent}{types}{key}: {built_stylish(value, depth + 1)}"
