#!/bin/python3


def migratory_birds(array):
    """ Returns the id of the most sighted bird type or
        the smallest id in case of equal sightings """

    max_sightings = 0
    current_count = 1       # Current sightings count
    max_id = 0
    sorted_arr = sorted(array)

    for i in range(1, len(array)):
        if sorted_arr[i] == sorted_arr[i-1]:    # If current id == previous id
            current_count += 1

            if current_count > max_sightings:
                max_sightings = current_count   # New most sighted
                max_id = sorted_arr[i]          # id of most sighted

        else:
            current_count = 1

    return max_id


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = migratory_birds(arr)
    print(result)
