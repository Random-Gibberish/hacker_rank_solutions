
def find_dirty_squares(grid):
    """ Returns a list of tuples containing
        the coordinates of dirty squares """

    dirty_squares = []

    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == 'd':               # If square is dirty
                dirty_squares.append((row, col))

    return dirty_squares


def next_move(row, col, dirty_board):
    """ Returns the next move the bot should take """

    row_move, col_move = 0, 0
    min_distance = None

    if (row, col) in dirty_board:   # If bot is on a dirty square
        print('CLEAN')
        return

    # Find the closest dirty squares using Euclidean distance
    for square in dirty_board:
        distance = abs(square[0] - row) + abs(square[1] - col)

        if not min_distance or distance < min_distance:
            min_distance = distance
            col_move = square[0] - row
            row_move = square[1] - col

    if col_move > 0:
        print('DOWN')
    elif col_move < 0:
        print('UP')
    elif row_move < 0:
        print('LEFT')
    elif row_move > 0:
        print('RIGHT')


if __name__ == "__main__":
    bot_row, bot_col = tuple(int(_) for _ in input().strip().split())
    board = [[j for j in input().strip()] for i in range(5)]
    dirty = find_dirty_squares(board)
    next_move(bot_row, bot_col, dirty)
