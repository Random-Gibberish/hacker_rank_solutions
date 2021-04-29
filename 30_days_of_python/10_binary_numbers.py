#!/bin/python3


def consecutive_1s(n):
    """ Returns the largest number of consecutive 1's """

    binary_n = format(n, 'b')
    count = 1
    maxi = 1

    for i in range(1, len(binary_n)):
        if binary_n[i] == binary_n[i - 1]:  # Check for consecutive 1's
            count += 1
            if count > maxi:                # Update maximum
                maxi = count
        else:
            count = 1

    return maxi


if __name__ == '__main__':
    base_10_number = int(input())

    result = consecutive_1s(base_10_number)
    print(result)
