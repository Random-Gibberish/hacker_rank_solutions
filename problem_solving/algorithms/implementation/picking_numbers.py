#!/bin/python3

import os


def picking_numbers(arr):
    """ Returns the longest sub-array of numbers with maximum
        absolute different less than or equal to 1 """

    max_len = None

    for i in arr:
        c = arr.count(i)        # Count the occurrences of each digit
        d = arr.count(i - 1)    # Count the occurrences of the previous digit
        c = c + d               # Sum th two

        if not max_len or c > max_len:  # Update the maximum length
            max_len = c

    return max_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    array = list(map(int, input().rstrip().split()))

    result = picking_numbers(array)

    fptr.write(str(result) + '\n')
    fptr.close()
