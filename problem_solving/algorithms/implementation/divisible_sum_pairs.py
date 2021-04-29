#!/bin/python3

import os


def divisible_sum_pairs(len_arr, div, array):
    """ Returns the number of (i, j) pairs such that
        i < j and ar[i] + ar[j] is divisible by k """

    array.sort()
    counter = 0

    for i in range(len_arr - 1):        # For all i
        for j in range(i+1, len_arr):   # For j > i
            if (array[i] + array[j]) % div == 0:
                counter += 1

    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    len_and_div = input().split()
    len_array = int(len_and_div[0])
    divisor = int(len_and_div[1])

    arr = list(map(int, input().rstrip().split()))
    result = divisible_sum_pairs(len_array, divisor, arr)

    fptr.write(str(result) + '\n')
    fptr.close()
