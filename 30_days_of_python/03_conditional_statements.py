#!/bin/python3

def weird_not_weird(num):
    """ Determines if the input number is weird """

    if num % 2 == 1 or num in range(6, 21):
        print('Weird')
    elif num % 2 == 0 and num > 0:
        print('Not Weird')
    else:
        print('n out of range! 0 < n < 101')


if __name__ == '__main__':
    n = int(input())

    weird_not_weird(n)
