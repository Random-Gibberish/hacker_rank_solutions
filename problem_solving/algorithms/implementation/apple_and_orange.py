#!/bin/python3


def count_apples_and_oranges(start, end, app_tree, org_tree, apples, oranges):
    count_apples = 0
    count_oranges = 0

    for apple in apples:        # Apples between start and end
        if start <= apple + app_tree <= end:
            count_apples += 1

    for orange in oranges:      # Oranges between start and end
        if start <= orange + org_tree <= end:
            count_oranges += 1

    print(count_apples)
    print(count_oranges)


if __name__ == '__main__':
    house = input().split()     # start and end of house
    start_h = int(house[0])
    end_h = int(house[1])

    tree_positions = input().split()     # apple and orange tree positions
    apple_tree = int(tree_positions[0])
    orange_tree = int(tree_positions[1])

    number_of = input().split()     # number of apples and oranges
    num_apples = int(number_of[0])
    num_oranges = int(number_of[1])

    apple_positions = list(map(int, input().rstrip().split()))   # where apples fall
    orange_positions = list(map(int, input().rstrip().split()))  # where oranges fall

    count_apples_and_oranges(start_h, end_h,
                             apple_tree, orange_tree,
                             apple_positions, orange_positions)
