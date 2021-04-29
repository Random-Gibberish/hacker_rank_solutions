#!/bin/python3

import os


def matching_strings(strings, queries):
    """ Returns the number of times each query
        occurs in the list of strings """

    string_counts = []

    for query in queries:
        string_counts.append(strings.count('%s' % query))   # Append the count of each query

    return string_counts


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())
    my_strings = []

    for _ in range(strings_count):
        strings_item = input()
        my_strings.append(strings_item)

    queries_count = int(input())
    my_queries = []

    for _ in range(queries_count):
        queries_item = input()
        my_queries.append(queries_item)

    res = matching_strings(my_strings, my_queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')
    fptr.close()
