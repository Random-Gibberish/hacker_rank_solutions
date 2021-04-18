#!/bin/python3


def a_very_big_sum(ar):
    """ Sum of the array elements """

    return sum(ar)


if __name__ == '__main__':
    ar_count = int(input())
    array = list(map(int, input().rstrip().split()))

    result = a_very_big_sum(array)
    print(result)
