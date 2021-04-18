#!/bin/python3

import os


def diagonal_difference(array):
    """ Returns the absolute difference between
        the sums of the diagonal elements """

    diagonal = sum(array[i][i] for i in range(n))
    off_diagonal = sum(array[i][n - (i + 1)] for i in range(n))

    abs_diff = abs(diagonal - off_diagonal)

    return abs_diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())    # Array size
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonal_difference(arr)

    fptr.write(str(result) + '\n')
    fptr.close()
