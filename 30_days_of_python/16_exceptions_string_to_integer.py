#!/bin/python3


S = input().strip()

try:
    print(int(S))
except ValueError:      # Raise error if string isn't a number
    print('Bad String')
