#!/usr/bin/python


def next_move(row_m, col_m, grid):
    """ Displays a move 'm' can take to get closer to 'p'.
        User must update the position of 'm' and rerun. """

    pos_m = [row_m, col_m]

    for i in grid:
        if 'p' in i:
            pos_p = [grid.index(i), i.index('p')]

    row_dif = pos_m[1] - pos_p[1]  # horizontal diff between m and p
    col_dif = pos_m[0] - pos_p[0]  # vertical   diff

    if row_dif > 0:
        move = 'LEFT'
    elif row_dif < 0:
        move = 'RIGHT'
    elif col_dif > 0:
        move = 'UP'
    else:
        move = 'DOWN'

    return move


if __name__ == '__main__':
    board_size = int(input())
    bot_row, bot_col = [int(i) for i in input().strip().split()]
    board = [input() for _ in range(board_size)]

    print(next_move(bot_row, bot_col, board))
