import json
from itertools import chain

ADD = "  + "
DELETED = '  - '
UNCHANGED = '    '
CHANGED = '    '
COMMON = '    '


# flake8: noqa: C901
def stylish(diff_tree, depth=0, replacer='    '):
    lines = []
    res = ''
    indent = depth * replacer
    # print('begin', diff_tree, indent, type(indent))

    for key, val in sorted(diff_tree.items()):
        # print("key and value -->", key, val, indent)
        # if not isinstance(val, dict) or "type" not in val:
        #     # print('clear -- >', key, val)
        #     lines.append(f"{indent}{UNCHANGED}{key}: {cor(val)}") \
        #         if not isinstance(val, dict) else lines.append(
        #         f"{indent}{UNCHANGED}{key}: {stylish(val, depth + 1)}")
        if not isinstance(val, dict) or "type" not in val:
            # print('clear -- >', key, val)
            lines.append(make_row(indent, key, val, UNCHANGED, depth))

        elif val.get("type") == "added":
            # print("added", key, val)
            lines.append(make_row(
                indent, key, val.get('value'), ADD, depth))
            # lines.append(
            #     f"{indent}{ADD}{key}: {cor(val.get('value'))}") \
            #     if not isinstance(
            #     val.get('value'), dict) else lines.append(
            #     f"{indent}{ADD}{key}: {stylish(val.get('value'), depth + 1)}")

        elif val.get("type") == "deleted":
            # print("added", key, val)
            lines.append(make_row(
                indent, key, val.get('value'), DELETED, depth))
            # lines.append(
            #     f"{indent}{DELETED}{key}: {cor(val.get('value'))}") if not \
            #     isinstance(
            #         val.get('value'), dict) else lines.append(
            #     f"{indent}{DELETED}{key}: {stylish(val.get('value'), depth + 1)}")

        elif val.get("type") == "unchanged":
            # print("added", key, val)
            lines.append(make_row(
                indent, key, val.get('value'), UNCHANGED, depth))
            # lines.append(
            #     f"{indent}{UNCHANGED}{key}: {cor(val.get('value'))}") \
            #     if not isinstance(
            #     val.get('value'), dict) else lines.append(
            #     f"{indent}{DELETED}{key}: {stylish(val.get('value'), depth + 1)}")

        elif val.get("type") == "changed":
            # lines.append(make_row(indent, key, val, replacer, depth))
            lines.append(make_row(
                indent, key, val.get('value1'), DELETED, depth))
            # lines.append(
            #     f"{indent}{DELETED}{key}: {cor(val.get('value1'))}") if \
            #     not isinstance(val.get('value1'), dict) else lines.append(
            #     f"{indent}{DELETED}{key}: "
            #     f"{stylish(val.get('value1'), depth + 1)}")

            lines.append(make_row(
                indent, key, val.get('value2'), ADD, depth))
            # lines.append(
            # f"{indent}{ADD}{key}: {cor(val.get('value2'))}") if \
            # not isinstance(
            #     val.get('value2'), dict) else lines.append(
            # f"{indent}{ADD}{key}: "
            # f"{stylish(val.get('value2'), depth + 1)}")

        elif val.get("type") == "nested":
            lines.append(make_row(
                indent, key, val.get('children'), COMMON, depth))
            # lines.append(f"{indent}{COMMON}{key}: {cor(val)}") if not \
            #     isinstance(val, dict) else lines.append(
            #     f"{indent}{COMMON}{key}: "
            #     f"{stylish(val.get('children'), depth + 1)}")

    # print('it\'s res', res, type(res), lines, indent, type(indent))
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
    # print(key, value, type(value), types)

    return f'{indent}{types}{key}: {convert(value)}' \
        if not isinstance(value, dict) \
        else f"{indent}{types}{key}: {stylish(value, depth + 1)}"


# data = {'group3': {'type': 'added',
#                    'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}
data = {"1": "one", "2": "True", "3": {"4": "four", "5": "five"}}
data = {
    'group2': {'type': 'deleted', 'value': {'abc': 12345, 'deep': {'id': 45}}},
    'group1': {'type': 'nested', 'children': {
        'nest': {'type': 'changed', 'value1': {'key': 'value'},
                 'value2': 'str'}, 'foo': {'type': 'unchanged', 'value': 'bar'},
        'baz': {'type': 'changed', 'value1': 'bas', 'value2': 'bars'}}},
    'group3': {'type': 'added',
               'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}},
    'common': {'type': 'nested', 'children': {
        'setting3': {'type': 'changed', 'value1': True, 'value2': None},
        'setting2': {'type': 'deleted', 'value': 200},
        'setting4': {'type': 'added', 'value': 'blah blah'},
        'setting5': {'type': 'added', 'value': {'key5': 'value5'}},
        'follow': {'type': 'added', 'value': False},
        'setting1': {'type': 'unchanged', 'value': 'Value 1'},
        'setting6': {'type': 'nested',
                     'children': {'ops': {'type': 'added', 'value': 'vops'},
                                  'key': {'type': 'unchanged',
                                          'value': 'value'},
                                  'doge': {'type': 'nested', 'children': {
                                      'wow': {'type': 'changed', 'value1': '',
                                              'value2': 'so much'}}}}}}}}
q = stylish(data)
#
print(q)
