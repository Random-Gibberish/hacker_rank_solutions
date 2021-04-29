#!/bin/python3


def bubble_sort_num_swaps(length, arr):
    """ Returns the number of swaps required to sort a
        list using bubble sort, as well as the first
        and last elements of the sorted list """

    num_swaps = 0

    for i in range(length):
        for j in range(length - 1):
            if arr[j] > arr[j+1]:                    # If an element is greater than the next one
                arr[j], arr[j+1] = arr[j+1], arr[j]  # swap (using tuple assignment swapping)
                num_swaps += 1

        if num_swaps == 0:  # If the number of swaps is zero on the first sweep
            break           # the array is already sorted

    return num_swaps


if __name__ == '__main__':
    len_arr = int(input().strip())
    array = list(map(int, input().strip().split(' ')))

    swaps = bubble_sort_num_swaps(len_arr, array)

    print('Array is sorted in ' + str(swaps) + ' swaps.')
    print('First Element: ' + str(array[0]))
    print('Last Element: ' + str(array[-1]))
