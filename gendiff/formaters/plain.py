import json


# data = {
#     'group2': {'type': 'deleted', 'value':{'abc': 12345, 'deep': {'id': 45}}},
#     'group1': {'type': 'nested', 'children': {
#         'nest': {'type': 'changed', 'value1': {'key': 'value'},
#                  'value2': 'str'}, 'foo': {'type': 'unchanged','value':'bar'},
#         'baz': {'type': 'changed', 'value1': 'bas', 'value2': 'bars'}}},
#     'group3': {'type': 'added',
#                'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}},
#     'common': {'type': 'nested', 'children': {
#         'setting3': {'type': 'changed', 'value1': True, 'value2': None},
#         'setting2': {'type': 'deleted', 'value': 200},
#         'setting4': {'type': 'added', 'value': 'blah blah'},
#         'setting5': {'type': 'added', 'value': {'key5': 'value5'}},
#         'follow': {'type': 'added', 'value': False},
#         'setting1': {'type': 'unchanged', 'value': 'Value 1'},
#         'setting6': {'type': 'nested',
#                      'children': {'ops': {'type': 'added', 'value': 'vops'},
#                                   'key': {'type': 'unchanged',
#                                           'value': 'value'},
#                                   'doge': {'type': 'nested', 'children': {
#                                       'wow': {'type': 'changed', 'value1': '',
#                                               'value2': 'so much'}}}}}}}}


# data = {'group3': {'type': 'added',
#                    'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}


def plain(diff_tree: dict) -> str:
    result = make_row(diff_tree)
    return '\n'.join(result)


# flake8: noqa: 901
def make_row(data: dict, parent_key="") -> list:
    lines = []
    for elem in sorted(data.items()):
        key, value = elem
        if not value.get('type') == 'unchanged':

            type = value.get('type')
            curent_key = key

            if parent_key:
                key = f"{parent_key}.{curent_key}"
            else:
                key = curent_key

            if type == "added":
                lines.append(f"Property '{key}' was added with value:"
                             f" {check_type(value.get('value'))}")

            elif type == "deleted":
                lines.append(f"Property '{key}' was removed")

            elif type == "changed":
                lines.append(f"Property '{key}' was updated. From "
                             f"{check_type(value.get('value1'))} to "
                             f"{check_type(value.get('value2'))}")

            elif type == "nested":
                nested_value = (make_row(value.get('children'), key))
                [lines.append(i) for i in nested_value]

    return lines


def check_type(item: any) -> str:
    # print('item-->', item, type(item))
    if isinstance(item, dict):
        return '[complex value]'
    elif type(item) is bool or item is None:
        q = json.dumps(item)
        # print('q -->', q, item)
        return q
    else:
        return f"'{item}'"
