#!/bin/python3

import re


if __name__ == '__main__':
    N = int(input())            # Solved without using regular expressions

    firstNames = []

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        if emailID[-10:] == '@gmail.com':
            firstNames.append(firstName)

    firstNames.sort()

    for name in firstNames:
        print(name)
