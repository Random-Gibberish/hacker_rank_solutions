
def book_fine(returned, due):
    """ Returns the fine that must be paid for
        returning a book late """

    if returned[2] > due[2]:    # If year returned > due year
        return 10000

    elif returned[2] == due[2]:     # If year returned == due year
        if returned[1] > due[1]:    # If month returned > due month
            return (returned[1] - due[1]) * 500         # Fine is 500 * month_difference

        elif returned[1] == due[1]:     # If month returned == month due
            if returned[0] > due[0]:    # If day returned > day due
                return (returned[0] - due[0]) * 15      # Fine is 15 * day_difference

    return 0        # Returned on or before due date


if __name__ == '__main__':
    return_date = [int(_) for _ in input().split()]
    due_date = [int(_) for _ in input().split()]

    fine = book_fine(return_date, due_date)
    print(fine)
