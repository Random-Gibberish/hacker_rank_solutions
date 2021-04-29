#!/bin/python3

import os


def alternating_characters(s):
    """ Returns the minimum number of deletions required in a string
        so that there are no identical adjacent characters """

    count = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:        # Next character identical to current
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternating_characters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
