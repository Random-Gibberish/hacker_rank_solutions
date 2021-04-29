import math as ma


def mean_median_mode(len_arr, arr):
    """ Returns the mean, median and mode of a an array """

    sorted(arr)
    mean = sum(arr) / len_arr   # Determine mean

    if len_arr % 2 == 0:    # If len_arr is even the median is the average of the middle two values
        median = (arr[int(len_arr / 2 - 1)] + arr[int(len_arr / 2)]) / 2
    else:                   # If len_arr is odd the median is the middle value
        median = arr[ma.floor(len_arr / 2)]

    mode = 0
    max_count = 0

    for num in set(arr):
        # The mode is the most frequent number
        if arr.count(num) > max_count:
            max_count = arr.count(num)
            mode = num

        # If numbers occur the same amount of times, pick the smallest
        elif arr.count(num) == max_count and num < mode:
            mode = num

    return mean, median, mode


if __name__ == '__main__':
    length = int(input().strip())
    array = sorted([int(_) for _ in input().split()])

    mmm = mean_median_mode(length, array)

    for m in mmm:
        print(m)
