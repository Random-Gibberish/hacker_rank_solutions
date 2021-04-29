
def print_rangoli(n):
    """ Returns a rangoli with the letter a in the center and
        the following letter of the alphabet around it up to
        the letter at index n """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    top_rangoli = []
    width = (n - 1) * 4 + 1

    for i in range(1, n + 1):
        # Letters from last to first, +1 letter for each loop
        # as we get closer to the center of the design
        start_row = list(alphabet[n - 1 - k] for k in range(i))

        end_row = start_row[:]  # Copy of row
        end_row.reverse()       # Reverse the row
        end_row.__delitem__(0)  # Delete to have a single middle letter

        row = start_row + end_row       # Full row
        full_row = '-'.join(row)        # Join the letter with a dash
        top_rangoli.append(full_row)    # Append rows to have the top of the rangoli

    bot_rangoli = top_rangoli[:]    # The bottom of the rangoli
    bot_rangoli.reverse()           # is the reflection of the top
    bot_rangoli.__delitem__(0)      # Delete to have a single center row

    rangoli = top_rangoli + bot_rangoli     # Full pattern

    for each_row in rangoli:
        print(each_row.center(width, '-'))  # Format and print rows one at a time


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
