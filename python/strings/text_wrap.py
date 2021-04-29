
def wrap(string, width):
    """ Returns the input string as a paragraph of
        width 'width' """

    short_strings = []
    i = 0

    while i < len(string):
        if i + width < len(string):
            short_strings.append(string[i:i + width])    # Segments of size 'width'
        else:
            short_strings.append(string[i:len(string)])  # End of string

        i += width      # Increment i by width

    s = '\n'.join(short_strings)    # Rejoin into a single formatted string

    return s


if __name__ == '__main__':
    my_string, max_width = input(), int(input())

    result = wrap(my_string, max_width)
    print(result)
