#!/bin/python3


def factorial(num):
    n_factorial = 1

    for i in range(1, num + 1):
        n_factorial *= i

    return n_factorial


if __name__ == '__main__':
    number = int(input())

    result = factorial(number)
    print(result)
