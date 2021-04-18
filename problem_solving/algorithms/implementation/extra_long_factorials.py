#!/bin/python3


def extra_long_factorials(num):
    n_factorial = 1

    for i in range(1, num + 1):
        n_factorial *= i

    return n_factorial


if __name__ == '__main__':
    n = int(input())    # Number

    long_fact = extra_long_factorials(n)
    print(long_fact)
