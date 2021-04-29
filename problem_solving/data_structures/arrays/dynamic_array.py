#!/bin/python3

import os


def dynamic_array(n, queries):
    """ There are 2 types of queries, given as an array of strings for you to parse:
        Query 1: Input -> '1 x y'
                    . Let idx = ((x XOR last_answer) % n).
                    . Append the integer y to arr[idx].
        Query 2: Input -> '2 x y'
                    . Let idx = ((x XOR last_answer) % n).
                    . Assign the value arr[idx][y % len(arr[idx])] to last_answer.
                    . Store the new value of last_answer to an answers array.

        Return the answers to each type 2 query
    """

    arr = [[] for _ in range(n)]
    last_answer = 0     # Default last answer
    answer_list = []    # List of all last_answers

    for query in queries:
        idx = (query[1] ^ last_answer) % n      # Calculate index for each query

        if query[0] == 1:               # If query 1
            arr[idx].append(query[2])   # Append 'y' to the list at index 'idx'

        else:                                       # If query 2
            position = query[2] % len(arr[idx])     # Find position
            last_answer = arr[idx][position]        # new last answer at (idx, position) of arr
            answer_list.append(last_answer)         # Append it to the answer list

    return answer_list


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    num = int(first_multiple_input[0])    # Number of empty arrays in arr
    q = int(first_multiple_input[1])    # Number of queries

    my_queries = []

    for _ in range(q):
        my_queries.append(list(map(int, input().rstrip().split())))

    result = dynamic_array(num, my_queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
