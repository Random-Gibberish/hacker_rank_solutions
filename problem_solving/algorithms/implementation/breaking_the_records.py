#!/bin/python3

import os


def breaking_records(scores):
    """ Given the scores for a season, return
        the number of times a player breaks
        their (best, worst) records """

    max_count = 0
    min_count = 0
    max_record = scores[0]
    min_record = scores[0]

    for i in range(1, n):
        if scores[i] > max_record:      # New max score
            max_count += 1
            max_record = scores[i]
        elif scores[i] < min_record:    # New min score
            min_count += 1
            min_record = scores[i]

    return max_count, min_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())        # Number of scores
    player_scores = list(map(int, input().rstrip().split()))

    result = breaking_records(player_scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
