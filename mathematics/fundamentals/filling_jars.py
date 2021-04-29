#!/bin/python3

import os
import math


def solve(jars, ops):
    """ For each operation (op), k sweets are added to the
        jars with indices in [operation[0], operation[1]].
        Returns the average number of sweets """

    candy_sum = 0

    for op in ops:
        # candy_sum = Sum(number_jars * sweets_added)
        candy_sum += (op[1] - op[0] + 1) * op[2]

    return math.floor(candy_sum / jars)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()
    num_jars = int(nm[0])
    num_ops = int(nm[1])

    operations = []

    for _ in range(num_ops):
        operations.append(list(map(int, input().rstrip().split())))

    result = solve(num_jars, operations)

    fptr.write(str(result) + '\n')

    fptr.close()
