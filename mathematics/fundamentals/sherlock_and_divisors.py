#!/bin/python3

import os
import math


def divisors(num):
    """ Returns the number of divisors of 'num'
        that are even """

    count = 0

    if num % 2 == 1:    # Odd numbers have no even divisors
        return 0

    else:
        # Check divisor pairs up to the square root of 'num'
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0 and i % 2 == 0:     # If divisor and even
                i_pair = num // i               # If i is a divisor of num, so is (num // i)
                count += 1

                if i_pair % 2 == 0 and i != i_pair:  # If i_pair even and not i
                    count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        number = int(input())

        result = divisors(number)

        fptr.write(str(result) + '\n')

    fptr.close()
