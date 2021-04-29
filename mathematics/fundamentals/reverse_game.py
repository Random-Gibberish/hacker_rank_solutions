#!/bin/python3


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        # For n balls numbered 0 to n - 1, the order is reversed
        # then keep index 0 and reverse the rest, do the same again
        # keeping indices 0, 1 and reversing the rest. Continue until
        # the end of the list
        print(min(1 + 2 * k, 2 * (n - 1 - k)))  # Ball at index k after n swaps
