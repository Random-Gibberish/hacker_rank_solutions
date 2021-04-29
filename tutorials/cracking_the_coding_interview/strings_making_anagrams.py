#!/bin/python3

import os
from collections import Counter


def make_anagram(a, b):
    """ Returns the number of deletions required to make
        strings a and b anagrams of each other """

    deletions = Counter(a) - Counter(b)
    del_count = 0

    for value in deletions.values():
        del_count += abs(value)

    return del_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()
    b = input()

    res = make_anagram(a, b)

    fptr.write(str(res) + '\n')
    fptr.close()
