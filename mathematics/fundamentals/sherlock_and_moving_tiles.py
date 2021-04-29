#!/bin/python3

import os
import math as m


def moving_tiles(len_sqr, vel_s1, vel_s2, queries):
    """ Returns the time taken for the overlapping area of two equal
        tiles to be equal to the query number for each query """

    times = []

    for query in queries:
        time = (m.sqrt(2) * len_sqr - m.sqrt(2 * query)) / abs(vel_s1 - vel_s2)
        times.append(time)

    return times


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lS1S2 = input().split()
    side_length = int(lS1S2[0])
    velocity_square_1 = int(lS1S2[1])
    velocity_square_2 = int(lS1S2[2])

    queries_count = int(input())
    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = moving_tiles(side_length, velocity_square_1,
                          velocity_square_2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
