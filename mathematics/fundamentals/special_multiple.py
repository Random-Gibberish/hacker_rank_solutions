#!/bin/python3

import os


def solve(n):
    """ X is made up of at least one 9 and at least zero 0's
        find the smallest such number divisible by n """

    # Multiply a binary sequence by 9 to get only 9's and 0's
    for i in range(1, 10000):
        # The first number to trigger the if-statement bellow is the answer
        if (9 * int(bin(i)[2:])) % n == 0:
            return str(9 * int(bin(i)[2:]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        number = int(input())

        result = solve(number)

        fptr.write(result + '\n')

    fptr.close()
