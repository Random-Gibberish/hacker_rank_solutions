#!/bin/python3

import os
import math


def restaurant(length, breadth):
    """ Returns the number of the largest squares a loaf of
        bread can be cut into with no left over pieces """

    gcd = math.gcd(length, breadth)     # Greatest common divisor

    if length == breadth:   # Already a square
        return 1
    elif gcd == 1:          # No common divisors so 1x1 squares are the largest
        return length * breadth
    else:                   # GCD sized squares
        return length * breadth // (gcd ** 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()
        len_bread = int(lb[0])
        bre_bread = int(lb[1])

        result = restaurant(len_bread, bre_bread)
        fptr.write(str(result) + '\n')

    fptr.close()
