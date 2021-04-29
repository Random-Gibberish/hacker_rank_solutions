#!/bin/python3

import os


def summing_series(n):
    """ If Tn = n^2 - (n - 1)^2 and Sn = Sum(T1 to Tn)
        then Sn = n^2. Returns Sn (mod 10^9 + 7) """

    return n ** 2 % (10 ** 9 + 7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = summing_series(n)

        fptr.write(str(result) + '\n')

    fptr.close()

