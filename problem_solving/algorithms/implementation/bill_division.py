#!/bin/python3


def bon_appetit(bill, not_eaten_by_anna, anna_pays):
    """ Returns 'Bon Appetit' if Brian doesn't overcharge Anna
        and the amount Brian must refund to Anna otherwise """

    bill_anna = int((sum(bill) - bill[not_eaten_by_anna]) / 2)

    if bill_anna == anna_pays:
        print('Bon Appetit')
    else:
        print(anna_pays - bill_anna)


if __name__ == '__main__':
    nk = input().rstrip().split()
    n = int(nk[0])
    not_anna = int(nk[1])           # Index of the item Anna did not eat

    item_prices = list(map(int, input().rstrip().split()))
    anna_contribution = int(input().strip())

    bon_appetit(item_prices, not_anna, anna_contribution)
