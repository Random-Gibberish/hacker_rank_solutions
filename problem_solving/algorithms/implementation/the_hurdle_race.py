#!/bin/python3

import os


def hurdle_race(jump, height):
    """ Given the height a person can jump and the heights
        of the hurdles. How many potions must the person take
        to bo able to pass all the hurdles (1 potion = +1 height) """

    return max(max(height) - jump, 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    jump_height = int(nk[1])

    hurdle_height = list(map(int, input().rstrip().split()))

    result = hurdle_race(jump_height, hurdle_height)

    fptr.write(str(result) + '\n')
    fptr.close()
