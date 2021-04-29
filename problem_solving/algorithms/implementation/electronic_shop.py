#!/bin/python3

import os


def get_money_spent(keyboards, usbs, budget):
    """ Returns the maximum a person can spend on
        a keyboard and USB drive given a budget,
        or -1 if the budget is too small """

    max_spend = 0

    for keyboard in keyboards:
        for usb in usbs:
            if max_spend < keyboard + usb <= budget:  # If current keyboard+USB is greater than current
                max_spend = keyboard + usb            # maximum but within budget update the maximum

    if max_spend == 0:   # If no combination was within budget
        return -1
    else:
        return max_spend


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()
    b = int(bnm[0])         # budget
    n = int(bnm[1])         # number of keyboard choices
    m = int(bnm[2])         # number of USB choices

    k_boards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    moneySpent = get_money_spent(k_boards, drives, b)

    fptr.write(str(moneySpent) + '\n')
    fptr.close()
