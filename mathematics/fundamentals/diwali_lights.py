#!/bin/python3

import os


def lights(num):
    """ Returns the numbers of ways n light bulbs can
        be lit (i.e. permutations of n) modulo 10 000 """

    return (2 ** num - 1) % 100000


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = lights(n)

        fptr.write(str(result) + '\n')

    fptr.close()
