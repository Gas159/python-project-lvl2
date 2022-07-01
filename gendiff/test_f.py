import os.path
import pathlib


def test_f(path1):
    w = os.path.abspath(path1)
    q = os.path.basename(path1)
    e = pathlib.Path(path1)

    print(q, w, e, sep='\n')


q = test_f(
    "/home/gastello/python-project-lvl2/gendiff/tests/fixtures/file1.json'")
