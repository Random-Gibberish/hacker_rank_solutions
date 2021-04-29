#!/bin/python3

import os


def maximum_toys(prices, budget):
    """ Returns the most toys Mark can buy with a 'k' budget """

    cost, num_toys = 0, 0

    # Sort prices and count until cost >= price
    for price in sorted(prices):
        cost += price

        if cost >= budget:
            break

        num_toys += 1

    return num_toys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    marks_budget = int(nk[1])

    price_tags = list(map(int, input().rstrip().split()))
    result = maximum_toys(price_tags, marks_budget)

    fptr.write(str(result) + '\n')
    fptr.close()
