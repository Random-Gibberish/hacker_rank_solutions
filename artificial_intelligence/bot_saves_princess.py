#!/usr/bin/python


def display_path_to_princess(grid):
    """ Displays the moves 'm' must take to
        rescue 'p', one move per line. """

    for i in grid:
        if 'm' in i:
            pos_m = [grid.index(i), i.index('m')]
        elif 'p' in i:
            pos_p = [grid.index(i), i.index('p')]

    row_dif = pos_m[1] - pos_p[1]  # horizontal diff between m and p
    col_dif = pos_m[0] - pos_p[0]  # vertical   diff

    while row_dif != 0 or col_dif != 0:
        if row_dif > 0:
            print('LEFT')
            row_dif -= 1
        elif row_dif < 0:
            print('RIGHT')
            row_dif += 1
        elif col_dif > 0:
            print('UP')
            col_dif -= 1
        else:
            print('DOWN')
            col_dif += 1


if __name__ == '__main__':
    board_size = int(input())    # Size of board
    board = [input() for _ in range(board_size)]

    display_path_to_princess(board)
