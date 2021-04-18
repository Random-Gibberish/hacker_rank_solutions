#!/bin/python3

import os


def compare_triplets(alice, bob):
    """ Compares the ratings for Alice and Bob's
        challenges and returns their win tallies """

    alice_wins = 0
    bob_wins = 0

    for i in range(3):
        if alice[i] > bob[i]:     # Alice wins
            alice_wins += 1
        elif alice[i] < bob[i]:   # Bob wins
            bob_wins += 1

    return [alice_wins, bob_wins]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))    # Alice's ratings
    b = list(map(int, input().rstrip().split()))    # Bob's ratings

    result = compare_triplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
