#!/bin/python3


def count_swaps(arr):
    """ Returns the number of swaps used to order a list
        as well as the first and last elements of the list """

    num_swaps = 0

    for i in range(len_arr):
        for j in range(len_arr - 1):
            if arr[j] > arr[j + 1]:                      # If next element is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
                num_swaps += 1

    print(f'Array is sorted in {num_swaps} swaps.')
    print(f'First Element: {arr[0]}')
    print(f'Last Element: {arr[-1]}')


if __name__ == '__main__':
    len_arr = int(input())
    array = list(map(int, input().rstrip().split()))

    count_swaps(array)
