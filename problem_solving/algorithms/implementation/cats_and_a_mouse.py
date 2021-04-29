#!/bin/python3

import os


def cat_and_mouse(pos_a, pos_b, pos_mouse):
    """ Determines whether cat A or cat B catches
        the mouse or whether it escapes """

    a_to_mouse = abs(pos_a - pos_mouse)      # Distance from cat A to mouse
    b_to_mouse = abs(pos_b - pos_mouse)      # Distance from cat B to mouse

    if a_to_mouse < b_to_mouse:     # Cat A catches the mouse
        return 'Cat A'
    elif a_to_mouse > b_to_mouse:   # Cat B catches the mouse
        return 'Cat B'
    else:                           # The mouse escapes
        return 'Mouse C'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        positions = input().split()

        position_cat_a = int(positions[0])
        position_cat_b = int(positions[1])
        position_mouse = int(positions[2])

        result = cat_and_mouse(position_cat_a, position_cat_b, position_mouse)
        fptr.write(result + '\n')

    fptr.close()
