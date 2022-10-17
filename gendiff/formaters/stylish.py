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
        # if not isinstance(val, dict) or "type" not in val:
        #     lines.append(built_line(indent, key, val, UNCHANGED, depth))

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
            # print('some')

    res = chain('{', lines, [indent + '}'])
    return '\n'.join(res)


def to_str(item, depth=0):
    if isinstance(item, bool):
        return str(item).lower()
    if str(item) == 'None':
        return 'null'
    if isinstance(item, dict):
        list_str = ['{']
        for key, nested_value in item.items():
            # print('key, nested value ----', key, nested_value)
            if isinstance(nested_value, dict):
                new_value = to_str(nested_value, depth + 1)
                list_str.append(f"{'    ' * depth}    {key}: {new_value}")
            else:
                list_str.append(f"{'    ' * depth}    {key}: {nested_value}")
        list_str.append(f'{"    " * depth}}}')
        # list_str
        # print('list_str ---', list_str)

        test_str = '\n'.join(list_str)
        return test_str

    return item


def built_line(indent, key, value, types='', depth=0):
    return f"{indent}{types}{key}: {to_str(value, depth + 1)}"


# tree =  {'group2': {'type': 'deleted', 'value':
# {'abc': 12345, 'deep': {'id': 45}}},
#  'group3': {'type': 'added',
#             'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}
#
# q = built_stylish(tree)
# print('it is result  ', '\n', q)
# #
