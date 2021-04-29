#!/bin/python3


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())

        if (k - 1) | k <= n:    # If bitwise AND of k - 1 and k <= n
            print(k - 1)
        else:
            print(k - 2)
