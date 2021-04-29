#!/bin/python3

import os


def hourglass_sum(arr):
    """ Returns the maximum sum of hourglass shapes
        in an array with negative values """

    h_max = None

    for i in range(len(arr[0]) - 2):
        for j in range(len(arr[0]) - 2):
            first_row = sum(arr[i][j:j + 3])
            third_row = sum(arr[i + 2][j:j + 3])

            # Add rows + the middle piece
            h_sum = first_row + third_row + arr[i + 1][j + 1]

            # Initialise max value and check subsequent values
            if not h_sum or h_sum > h_max:
                h_max = h_sum

    return h_max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    array = []

    for _ in range(6):
        array.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(array)

    fptr.write(str(result) + '\n')
    fptr.close()
