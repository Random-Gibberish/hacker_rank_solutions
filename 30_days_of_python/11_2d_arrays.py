#!/bin/python3


def hourglass(arr):
    """ Calculates the sum of every      ###
        hourglass shape in the 2D array   #
        and returns the maximum sum      ### """

    maxi = None

    for i in range(4):
        for j in range(4):
            # Calculated each row separately then sum
            first_row = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            center_piece = arr[i+1][j+1]
            third_row = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            hourglass_sums = first_row + center_piece + third_row

            if maxi is None or hourglass_sums > maxi:
                maxi = hourglass_sums

    return maxi


if __name__ == '__main__':
    array = []

    for _ in range(6):
        array.append(list(map(int, input().rstrip().split())))

    max_sum = hourglass(array)
    print(max_sum)
