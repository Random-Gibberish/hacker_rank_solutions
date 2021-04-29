#!/bin/python3

import os
import math

# Strange grid
# ..............    ...
# ..............    odd ...
# 20 22 24 26 28    even 20 to 28
# 11 13 15 17 19    odd 11 to 19
# 10 12 14 16 18    even 10 to 18
#  1  3  5  7  9    odd 1 to 9
#  0  2  4  6  8    even 0 to 8


def strange_grid(row, col):
    """ Returns the integer found at coordinate (row, col) """

    int_at_coord = 2 * (col - 1) + 10 * math.floor((row - 1) / 2)

    if row % 2 == 0:        # If even row add one
        int_at_coord += 1

    return int_at_coord


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rc = input().split()
    r = int(rc[0])
    c = int(rc[1])

    result = strange_grid(r, c)
    fptr.write(str(result) + '\n')
    fptr.close()
