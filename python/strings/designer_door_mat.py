
def designer_door_mat(n, m):
    """ Returns the design for a doormat of size nxm """

    rows = []

    for i in range(1, int(n / 2) + 1):
        row1_3 = '-' * int((m - 3 * (2 * i - 1)) / 2)   # Dashes on left and right
        row_2_ = '.|.' * (2 * i - 1)                    # Pattern in middle

        row = row1_3 + row_2_ + row1_3      # Complete rows symmetrically
        rows.append(row)                    # Loop completes the top half

    mat = rows[:]       # Keep a copy
    mid_row = '-' * int((m - 7) / 2) + 'WELCOME' + '-' * int((m - 7) / 2)   # Middle row of the mat
    mat.append(mid_row)

    rev_rows = list(reversed(rows))  # Reverse the order of the rows in the top

    for rev_row in rev_rows:
        mat.append(rev_row)     # Append the rows in reverse order to the mat

    return '\n'.join(mat)       # Join with a new line to complete the mat


if __name__ == '__main__':
    width = int(input().strip())
    length = 3 * width

    door_mat = designer_door_mat(width, length)
    print(door_mat)
