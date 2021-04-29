#!/bin/python3

import os
import math


def halloween_party(cuts):
    """ Returns the maximum number of 1x1 pieces of chocolate
        that can be cut from the corner of an infinite chocolate
        bar given a specific number of allowed cuts k """

    return math.floor(cuts / 2) * math.ceil(cuts / 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        num_cuts = int(input())

        result = halloween_party(num_cuts)

        fptr.write(str(result) + '\n')

    fptr.close()
