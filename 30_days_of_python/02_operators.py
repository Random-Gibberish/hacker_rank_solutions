#!/bin/python3


def solve(meal_cost, tip_percent, tax_percent):
    """ Returns the total cost of a meal """

    unrounded_total = meal_cost * (1 + (tip_percent + tax_percent) / 100)
    total_cost = round(unrounded_total)

    return total_cost


if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())

    cost = solve(meal_cost, tip_percent, tax_percent)
    print(cost)
