#!/bin/python3

import os


def day_of_programmer(year):
    """ Returns the date (day.month.year) of
        the day of the programmer (256th day
        of the year) depending on the year """

    if 1700 <= year < 1918:             # Julian calendar
        if year % 4 == 0:               # Leap year
            programmer_day = '12.09.'
        else:                           # Not leap year
            programmer_day = '13.09.'

    elif year == 1918:                  # Transition year
        programmer_day = '26.09.'

    else:                               # Gregorian calendar
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):  # Leap year
            programmer_day = '12.09.'
        else:                           # Not leap year
            programmer_day = '13.09.'

    return programmer_day + str(year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    current_year = int(input().strip())
    result = day_of_programmer(current_year)

    fptr.write(result + '\n')
    fptr.close()
