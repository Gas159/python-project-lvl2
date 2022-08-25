from itertools import chain

ADDED = "  + "
DELETED = '  - '
UNCHANGED = '    '
CHANGED = '    '
COMMON = '    '


# flake8: noqa: C901
def stylish(diff_tree, depth=0, replacer='    '):
    lines = []
    res = ''
    indent = depth * replacer

    for key, val in sorted(diff_tree.items()):
        if not isinstance(val, dict) or "type" not in val:
            lines.append(make_row(indent, key, val, UNCHANGED, depth))

        elif val.get("type") == "added":
            lines.append(make_row(
                indent, key, val.get('value'), ADDED, depth))

        elif val.get("type") == "deleted":
            # print("added", key, val)
            lines.append(make_row(
                indent, key, val.get('value'), DELETED, depth))

        elif val.get("type") == "unchanged":
            lines.append(make_row(
                indent, key, val.get('value'), UNCHANGED, depth))

        elif val.get("type") == "changed":
            lines.append(make_row(
                indent, key, val.get('value1'), DELETED, depth))

            lines.append(make_row(
                indent, key, val.get('value2'), ADDED, depth))

        elif val.get("type") == "nested":
            lines.append(make_row(
                indent, key, val.get('children'), COMMON, depth))

    res = chain('{', lines, [indent + '}'])
    return '\n'.join(res)


def convert(item):
    if str(item) == "True":
        return "true"
    elif str(item) == 'None':
        return 'null'
    elif str(item) == 'False':
        return 'false'
    else:
        return item


def make_row(indent, key, value, types='', depth=0):
    return f'{indent}{types}{key}: {convert(value)}' \
        if not isinstance(value, dict) \
        else f"{indent}{types}{key}: {stylish(value, depth + 1)}"
