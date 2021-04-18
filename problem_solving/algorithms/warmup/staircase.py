#!/bin/python3


def staircase(num):
    """ Return a formatted '#' staircase """

    for i in range(1, num + 1):
        print(str((num - i) * ' ' + i * '#'))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
