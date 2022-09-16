def make_tree(data1: dict, data2: dict) -> dict:
    result = {}
    set1 = set(data1)
    set2 = set(data2)
    add_keys = set(set2 - set1)
    del_keys = set(set1 - set2)

    for key in set1 | set2:
        if key in add_keys:
            result[key] = {'type': 'added', 'value': data2.get(key)}

        elif key in del_keys:
            result[key] = {'type': 'deleted', 'value': data1.get(key)}

        else:
            if isinstance(data1.get(key), dict) and isinstance(data2.get(
                    key), dict):
                result[key] = {
                    'type': 'nested',
                    'children': make_tree(data1.get(key), data2.get(key))
                }

            elif data1.get(key) == data2.get(key):
                result[key] = {'type': 'unchanged', 'value': data1.get(key)}

            else:
                result[key] = {'type': 'changed', 'value1': data1.get(key),
                               'value2': data2.get(key)}

    return result
