#!/bin/python3


def plus_minus(arr):
    """ Returns formatted strings with the ratio of positive,
        negative and zero elements in the array """

    num_positive = 0
    num_negative = 0
    num_zeros = 0

    for i in range(n):
        if arr[i] > 0:
            num_positive += 1
        elif arr[i] < 0:
            num_negative += 1
        else:
            num_zeros += 1

    ratio_positive = num_positive / n
    ratio_negative = num_negative / n
    ratio_zeros = num_zeros / n

    print(str.format('{0:.6f}', ratio_positive))
    print(str.format('{0:.6f}', ratio_negative))
    print(str.format('{0:.6f}', ratio_zeros))


if __name__ == '__main__':
    n = int(input())
    array = list(map(int, input().rstrip().split()))

    plus_minus(array)
