#!/bin/python3

import os


def sock_merchant(n, array):
    """ Returns the number of matching pairs of socks
        (represented as integers) in the array """

    pairs = 0

    for i in range(1, max(array) + 1):  # Iterate over the values in the array
        pairs += (array.count(i) // 2)  # Add number of 'i' coloured socks

    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)

    fptr.write(str(result) + '\n')
    fptr.close()
