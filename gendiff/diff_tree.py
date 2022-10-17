# import json
# from pprint import pprint


def make_diff_tree(data1: dict, data2: dict) -> dict:
    result = {}
    collect_1 = set(data1)
    collect_2 = set(data2)
    add_keys = set(collect_2 - collect_1)
    del_keys = set(collect_1 - collect_2)

    for key in collect_1 | collect_2:
        if key in add_keys:
            result[key] = {'type': 'added', 'value': data2.get(key)}

        elif key in del_keys:
            result[key] = {'type': 'deleted', 'value': data1.get(key)}

        else:
            if isinstance(data1.get(key), dict) and isinstance(data2.get(
                    key), dict):
                result[key] = {
                    'type': 'nested',
                    'children': make_diff_tree(data1.get(key), data2.get(key))
                }

            elif data1.get(key) == data2.get(key):
                result[key] = {'type': 'unchanged', 'value': data1.get(key)}

            else:
                result[key] = {'type': 'changed', 'value_old': data1.get(key),
                               'value_new': data2.get(key)}

    return result

# with open('/home/gas/projects/
# python-project-lvl2/tests/fixtures/recur_file1.json', 'r') as f:
#     file1 = json.load(f)
#     with open('/home/gas/projects/
#     python-project-lvl2/tests/fixtures/recur_file2.json', 'r') as f2:
#         file2 = json.load(f2)
#         pprint(make_diff_tree(file1,file2))

# data1 = 'tests/fixtures/recur_file1.json'
# data2 = 'tests/fixtures/recur_file2.json'
# print( make_diff_tree(data1,data2))
