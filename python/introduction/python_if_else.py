#!/bin/python3


def weirdness(n):
    """ Returns whether a number is weird. It is considered weird
        if it is odd or if it is even and in [6:20] inclusive """

    if n % 2 == 1:
        n_weird = 'Weird'
    elif n % 2 == 0 and n in range(2, 6):
        n_weird = 'Not Weird'
    elif n % 2 == 0 and n in range(6, 21):
        n_weird = 'Weird'
    else:
        n_weird = 'Not Weird'

    return n_weird


if __name__ == '__main__':
    n = int(input().strip())
    weird = weirdness(n)
    print(weird)

