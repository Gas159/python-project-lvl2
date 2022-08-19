#! usr/bin/env python3
from gendiff.gendiff1 import generate_diff
from gendiff.parse_args import parse


def main():
    args = parse()
    # print('this is args -->>', args)
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)
    # def summ(a,b):
    #     print(a+b)
    # summ(args.a, args.b)


if __name__ == "__main__":
    main()
# poetry run python -m gendiff.scripts.gendiff
