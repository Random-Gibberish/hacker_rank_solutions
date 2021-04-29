#!/bin/python3

import os


def solve(rows, cols):
    """ Returns the minimum number of cuts needed to cut a piece
        of paper into 1x1 squares. The paper can't be folded and
        each cut goes from on side all the way to the other """

    return rows * cols - 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    num_rows = int(nm[0])
    num_cols = int(nm[1])
    result = solve(num_rows, num_cols)

    fptr.write(str(result) + '\n')
    fptr.close()
