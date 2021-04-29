#!/bin/python3

import os


def rotate_left(arr, r):
    """ One rotation involves taking the last element
        and pushing it to the front of the array.
        Return the list after 'r' rotations """

    # Assuming r <= len(arr)
    return arr[r:] + arr[:r]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    array = list(map(int, input().rstrip().split()))

    result = rotate_left(d, array)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
