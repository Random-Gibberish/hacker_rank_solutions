#!/bin/python3

import os


def birthday(numbers, day, month):
    """ Determines the number of ways a chocolate bar can be divided such that:
         . the continuous segment is of 'birth month' length and
         . the numbers on the squares add up to the 'birth day' """

    count = 0

    for i in range(len(numbers)):               # Iterate over chocolate bar
        if sum(numbers[i:i + month]) == day:    # If segment of length 'month' sums to 'day'
            count += 1                          # Number of such segments

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    number_of_squares = int(input().strip())
    numbers_on_squares = list(map(int, input().rstrip().split()))

    day_month = input().rstrip().split()
    birth_day = int(day_month[0])
    birth_month = int(day_month[1])

    result = birthday(numbers_on_squares, birth_day, birth_month)

    fptr.write(str(result) + '\n')
    fptr.close()
