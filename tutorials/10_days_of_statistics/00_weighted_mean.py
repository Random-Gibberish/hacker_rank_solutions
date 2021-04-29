#!/bin/python3


def weighted_mean(vals, wei):
    """ Returns the weighted mean of an array """

    w_mean = sum([x * w for x, w in zip(vals, wei)]) / sum(wei)

    print('%0.1f' % w_mean)


if __name__ == '__main__':
    n = int(input().strip())
    values = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))

    weighted_mean(values, weights)
