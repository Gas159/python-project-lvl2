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


# data = {'group3': {'type': 'added',
#                    'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}}


def plain(diff_tree: dict) -> str:
    lines = []
    for key, val in sorted(diff_tree.items()):
        # if not 'type' in val :
        #     lines.append(f"Property '{key}' was added with value:"
        #                  f"{'[complex value]' if isinstance(val.get('value'), dict) else val.get('value')}")


        if val.get("type") == "added":
            lines.append(f"Property '{key}' was added with value:"
                         f"{'[complex value]' if isinstance(val.get('value'), dict) else val.get('value')}")

        elif val.get("type") == "deleted":
            lines.append(f"Property '{key}' was removed")


        elif val.get("type") == "changed":
            lines.append(
                f"Property '{key}' was update. From "
                f"{'[complex value]' if isinstance(val.get('value'), dict) else val.get('value')}"
            )
        elif val.get("type") == "nested":
            lines.append(
                f"Property '{key}.{plain(val.get('children'))}'")

    return '\n'.join(lines)


def make_row(item, value):
    # if f"Property '{item}' was {} with value: [complex value]" not isinstance(value,dict)
    pass


print(plain(data))
