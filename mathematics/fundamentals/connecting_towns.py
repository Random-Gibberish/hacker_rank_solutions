#!/bin/python3

import os


def connecting_towns(n, routes):
    """ Returns the number of routes form city 0
        to the last city modulo 1234567 """

    num_routes = routes[0]      # Number of routes from city 0 to city 1

    for i in range(1, len(routes)):
        # Multiply by the number of routes from city i to city i + 1
        num_routes *= routes[i]

    mod_routes = num_routes % 1234567   # Total number of routes modulo 1234567

    return mod_routes


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())
        all_routes = list(map(int, input().rstrip().split()))

        result = connecting_towns(n, all_routes)

        fptr.write(str(result) + '\n')

    fptr.close()
