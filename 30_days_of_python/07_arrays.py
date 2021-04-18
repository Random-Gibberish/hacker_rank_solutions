#!/bin/python3


def reverse_array(array):
    """ Returns the input array in
        reverse on a single line """

    array.reverse()
    print(*array)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    reverse_array(arr)
