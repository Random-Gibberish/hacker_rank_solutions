#!/bin/python3

import os
from collections import Counter


def two_strings(s1, s2):
    """ Return 'Yes' or 'No' depending on whether
        s2 is in s1. Case sensitive """

    if Counter(s1) - Counter(s2) == Counter(s1):    # If s1 is unchanged, it doesn't contain s2
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()

        result = two_strings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
