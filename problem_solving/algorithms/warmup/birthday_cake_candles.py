#!/bin/python3

import os


def birthday_cake_candles(candles):
    """ Determines the number of candles
        of maximum height """

    sorted_candles = sorted(candles)    # Sorts candles by height
    count = 0

    for i in sorted_candles:
        if i == sorted_candles[-1]:     # If element equals max height
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())
    candle_sizes = list(map(int, input().rstrip().split()))

    result = birthday_cake_candles(candle_sizes)

    fptr.write(str(result) + '\n')
    fptr.close()
