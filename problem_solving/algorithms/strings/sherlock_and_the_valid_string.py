#!/bin/python3

import os
from collections import Counter


def is_valid(s):
    """ Returns whether or not a string is valid.
        To be considered valid a string:
         . must contain the same number of each character
         or
         . if one character is removed contain the same
           number of each character """

    cnt_s = Counter(s)              # Dict with character counts as keys
    val_s = list(cnt_s.values())
    count = 0

    for i in range(1, len(val_s)):
        if val_s[0] != val_s[i]:    # Count the number of different keys
            count += 1

        # If there are more than two different keys then
        # more than one character will have to be removed
        if count == 2:
            return 'NO'

    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = is_valid(s)

    fptr.write(result + '\n')
    fptr.close()
