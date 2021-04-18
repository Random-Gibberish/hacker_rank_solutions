#!/bin/python3


def get_total_x(a_array, b_array):
    """ Returns the number of 'i' such that 'i' is:
         . divisible by all numbers in 'a_array'
         . divides all numbers in 'b_array' """

    end = 101
    a_divides_i = []
    b_divided_by_i = []
    length = len(a_array) + len(b_array)

    for i in range(1, end):         # For all i
        for a in a_array:           # Find all a that divide i
            if i % a == 0:
                a_divides_i.append(i)

        for b in b_array:           # Find all b divisible by i
            if b % i == 0:
                b_divided_by_i.append(i)

    arr_brr = a_divides_i + b_divided_by_i
    count = set()

    # Keep elements that appear 'length' times
    for number in arr_brr:
        if arr_brr.count(number) == length:
            count.add(number)

    return len(count)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    len_arr = int(first_multiple_input[0])      # Length of array a
    len_brr = int(first_multiple_input[1])      # Length of array b

    arr = list(map(int, input().rstrip().split()))  # Array a
    brr = list(map(int, input().rstrip().split()))  # Array b

    total = get_total_x(arr, brr)
    print(total)
