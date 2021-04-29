#!/bin/python3

from bisect import bisect_right
import os


def climbing_leaderboard(ranked, scores):
    """ Returns the rank of a new player in the leaderboard
        after each game (using dense ranking) """

    ranks = []

    for score in scores:
        # Insert player in leaderboard using bisection
        ranks.append(len(ranked) - bisect_right(ranked, score) + 1)

    return ranks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    ranked = sorted(set(map(int, input().split())))

    m = int(input())
    scores = map(int, input().split())

    result = climbing_leaderboard(ranked, scores)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
