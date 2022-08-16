from itertools import chain

ADD = "  + "
DELETED = '  - '
UNCHANGED = '    '
CHANGED = '    '
COMMON = '    '


# flake8: noqa: C901
def stylish(diff_tree, replacer='    '):  # noqa
    def iter(data, depth):
        lines = []
        res = ''
        indent = depth * replacer

        for key, val in sorted(data.items()):
            # print("key and value -->", key, val)
            if not isinstance(val, dict) or "type" not in val:
                # print('clear -- >', key, val)
                lines.append(f"{indent}{UNCHANGED}{key}: {cor(val)}") \
                    if not isinstance(
                    val, dict) else lines.append(
                    f"{indent}{UNCHANGED}{key}: {iter(val, depth + 1)}")

            elif val.get("type") == "added":
                # print("added", key, val)
                lines.append(
                    f"{indent}{ADD}{key}: {cor(val.get('value'))}") \
                    if not isinstance(
                    val.get('value'), dict) else lines.append(
                    f"{indent}{ADD}{key}: {iter(val.get('value'), depth + 1)}")

            elif val.get("type") == "deleted":
                # print("added", key, val)
                lines.append(
                    f"{indent}{DELETED}{key}: {cor(val.get('value'))}") if not \
                    isinstance(
                        val.get('value'), dict) else lines.append(
                    f"{indent}{DELETED}{key}: {iter(val.get('value'), depth + 1)}")

            elif val.get("type") == "unchanged":
                # print("added", key, val)
                lines.append(
                    f"{indent}{UNCHANGED}{key}: {cor(val.get('value'))}") \
                    if not isinstance(
                    val.get('value'), dict) else lines.append(
                    f"{indent}{DELETED}{key}: {iter(val.get('value'), depth + 1)}")

            elif val.get("type") == "changed":
                lines.append(
                    f"{indent}{DELETED}{key}: {cor(val.get('value1'))}") if \
                    not isinstance(val.get('value1'), dict) else lines.append(
                    f"{indent}{DELETED}{key}: "
                    f"{iter(val.get('value1'), depth + 1)}")

                lines.append(
                    f"{indent}{ADD}{key}: {cor(val.get('value2'))}") if \
                    not isinstance(
                        val.get('value2'), dict) else lines.append(
                    f"{indent}{ADD}{key}: "
                    f"{iter(val.get('value2'), depth + 1)}")

            elif val.get("type") == "nested":
                lines.append(f"{indent}{COMMON}{key}: {cor(val)}") if not \
                    isinstance(val, dict) else lines.append(
                    f"{indent}{COMMON}{key}: "
                    f"{iter(val.get('children'), depth + 1)}")

        res = chain('{', lines, [indent + '}'])
        return '\n'.join(res)

    return iter(diff_tree, 0)


def cor(item):
    if str(item) == "True":
        return "true"
    elif str(item) == 'None':
        return 'null'
    elif str(item) == 'False':
        return 'false'
    else:
        return item


def make_row(key, value, operator=" "):
    return f'  {operator} {key} : {str(value.get(key))}\n'

# def unpack(dictionary, depth=0, space_count=1, replacer='----'):
#     lines = []
#     res = ''
#     indent = replacer * (depth + 1)
#     indent = depth * replacer
#     print('!!!', dictionary)
#
#     for key, val in dictionary.items():
#         print('key', key, 'val', val)
#         if isinstance(val, dict) and val.get('type') == 'added':
#             replacer = ' +  '
#         else:
#             replacer = '----'
#         lines.append(f'{replacer}{key}:{val}') if not isinstance(
#             val,
#             dict) else \
#             lines.append(f'{indent}{key}: {{\n{unpack(val, depth + 1)}\n{indent}}}')
#
#         res = chain(lines)
#     print(res)
#     return '\n'.join(res)


# data = {'group3': {'type': 'added',
#                    'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}
# data1 = {"1": "one", "2": "True", "3": {"4": "four", "5": "five"}}
# data ={'group2': {'type': 'deleted', 'value': {'abc': 12345, 'deep': {'id': 45}}}, 'group1': {'type': 'nested', 'children': {'nest': {'type': 'changed', 'value1': {'key': 'value'}, 'value2': 'str'}, 'foo': {'type': 'unchanged', 'value': 'bar'}, 'baz': {'type': 'changed', 'value1': 'bas', 'value2': 'bars'}}}, 'group3': {'type': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}, 'common': {'type': 'nested', 'children': {'setting3': {'type': 'changed', 'value1': True, 'value2': None}, 'setting2': {'type': 'deleted', 'value': 200}, 'setting4': {'type': 'added', 'value': 'blah blah'}, 'setting5': {'type': 'added', 'value': {'key5': 'value5'}}, 'follow': {'type': 'added', 'value': False}, 'setting1': {'type': 'unchanged', 'value': 'Value 1'}, 'setting6': {'type': 'nested', 'children': {'ops': {'type': 'added', 'value': 'vops'}, 'key': {'type': 'unchanged', 'value': 'value'}, 'doge': {'type': 'nested', 'children': {'wow': {'type': 'changed', 'value1': '', 'value2': 'so much'}}}}}}}}
# q = stylish(data)
#
# print( q)
