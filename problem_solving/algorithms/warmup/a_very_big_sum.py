#!/bin/python3

import os


def a_very_big_sum(ar):
    """ Sum of the array elements """

    return sum(ar)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())
    array = list(map(int, input().rstrip().split()))

    result = a_very_big_sum(array)

    fptr.write(str(result) + '\n')
    fptr.close()
