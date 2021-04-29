#!/bin/python3

import os


def page_count(number_of_pages, page_number):
    """ Returns the minimum number of pages a student
        must turn to open a book to the desired page """

    if page_number % 2 == 0:                            # Even page number
        open_at_page = (page_number, page_number + 1)
    else:                                               # Odd page number
        open_at_page = (page_number - 1, page_number)

    start_count = 0                  # Count from front cover
    end_count = number_of_pages     # Count from back cover

    # Loop until one of the counts matches the page number
    while start_count not in open_at_page and end_count not in open_at_page:
        start_count += 2     # Two pages per page turn
        end_count -= 2

    # Returns the number of pages turned for the count in open_page
    if start_count in open_at_page:
        return int(start_count / 2)
    elif end_count in open_at_page:
        return int((number_of_pages - end_count) / 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    number = int(input())   # Number of pages
    page = int(input())     # Page number

    result = page_count(number, page)

    fptr.write(str(result) + '\n')
    fptr.close()
