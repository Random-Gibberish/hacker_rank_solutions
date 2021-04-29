#!/bin/python3

import os


def prime_count(num):
    """ Returns the maximum number of distinctive primes
        such that their multiplication is <= num """

    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 57]
    prime_mult = 1
    count = 0

    for i in primes:
        # If the multiplication of the first 'count' primes
        # is greater than 'num', then only the multiplication
        # of 'count - 1' primes will by smaller than 'num'
        if num < prime_mult:
            return count - 1
        else:                   # If 'num' has not been reached
            prime_mult *= i     # multiply by the next prime
            count += 1          # and add one to the count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries = int(input())

    for query in range(queries):
        number = int(input())

        result = prime_count(number)

        fptr.write(str(result) + '\n')

    fptr.close()
