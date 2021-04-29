#!/bin/python3

from collections import Counter


def check_magazine(mag, note):
    """ Return 'Yes' or 'No' depending on whether a ransom
        not can be formed, given that:
         . full word are cut out of the magazine,
         . each word in the magazine can only be used once
         . the ransom note is case sensitive """

    if Counter(note) - Counter(mag) == {}:   # 'mag' is a superset 'note'
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    magazine = input().rstrip().split()
    ran_note = input().rstrip().split()
    check_magazine(magazine, ran_note)
