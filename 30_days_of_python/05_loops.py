#!/bin/python3


def multiply(num):
    """ Returns the times table for num """

    for i in range(1, 11):
        m = num * i
        multiple = str(num) + ' x ' + str(i) + ' = ' + str(m)
        print(multiple)


if __name__ == '__main__':
    n = int(input())

    multiply(n)
