#!/bin/python3

import os


def forming_magic_square(square):
    """ Returns the minimum cost required to
        turn a 3x3 grid into a magic square """

    n = [square[i][j] for i in range(3) for j in range(3)]  # 2D array to 1D array
    sums = []
    magic_squares = [                                   # All possible magic squares
                        [8, 1, 6, 3, 5, 7, 4, 9, 2],
                        [6, 1, 8, 7, 5, 3, 2, 9, 4],
                        [4, 9, 2, 3, 5, 7, 8, 1, 6],
                        [2, 9, 4, 7, 5, 3, 6, 1, 8],
                        [8, 3, 4, 1, 5, 9, 6, 7, 2],
                        [4, 3, 8, 9, 5, 1, 2, 7, 6],
                        [6, 7, 2, 1, 5, 9, 8, 3, 4],
                        [2, 7, 6, 9, 5, 1, 4, 3, 8]
                    ]

    # Append the cost of swapping for all squares
    for k in magic_squares:
        sums.append(sum([abs(n[i] - k[i]) for i in range(9)]))

    return min(sums)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    square_to_change = []

    for _ in range(3):
        square_to_change.append(list(map(int, input().rstrip().split())))

    result = forming_magic_square(square_to_change)

    fptr.write(str(result) + '\n')
    fptr.close()
