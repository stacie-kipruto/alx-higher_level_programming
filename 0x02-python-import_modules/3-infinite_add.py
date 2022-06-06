#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_num = len(argv)
    sum = 0

    if arg_num > 1:
        for i in range(1, arg_num):
            sum += int(argv[i])
    print(sum)
