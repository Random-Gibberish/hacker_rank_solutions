#!/bin/python3

import math
import os


def repeated_string(init_str, idx):
    """ A string is repeated infinitely many times.
        Return the number of times 'a' appears in the
        first 'n' characters given the initial string """

    a_per_str = init_str.count('a')                         # count 'a' in initial string
    num_strs = math.floor(idx / len(init_str))              # number of whole strings up to 'idx'
    a_in_rest = init_str[:idx % len(init_str)].count('a')   # count 'a' in last segment

    return a_per_str * num_strs + a_in_rest     # Total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    initial_string = input()
    index = int(input())

    result = repeated_string(initial_string, index)

    fptr.write(str(result) + '\n')
    fptr.close()
