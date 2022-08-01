#! usr/bin/env python3
import argparse
from gendiff.diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration '
                    'files and shows a difference.')

    parser.add_argument('first_file', help='foo help')
    parser.add_argument('second_file')
    parser.add_argument("-f", '--format', dest='format', help='set format of '
                                                              'output')
    args = parser.parse_args()
    # print(args)
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)
    # def summ(a,b):
    #     print(a+b)
    # summ(args.first11_file, args.second_file)


if __name__ == "__main__":
    main()
# poetry run python -m gendiff.scripts.gendiff
# q = generate_diff
# /home/gastello/python-project-lvl2/gendiff/tests/fixtures/file1.json
