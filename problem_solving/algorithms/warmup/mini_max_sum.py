#!/bin/python3


def mini_max_sum(array):
    """ Returns the minimum and maximum sums
        from 4 out 5 elements in a list """

    sorted_arr = sorted(array)
    mini = sum(sorted_arr[:-1])
    maxi = sum(sorted_arr[1:])

    return mini, maxi


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    mm_sum = mini_max_sum(arr)
    print(mm_sum)
