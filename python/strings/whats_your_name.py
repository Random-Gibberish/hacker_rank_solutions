def print_full_name(f_name, l_name):
    """ Prints the input in a formatted string """

    return f'Hello {f_name} {l_name}! You just delved into python.'


if __name__ == '__main__':
    first_name = input()
    last_name = input()

    print_full_name(first_name, last_name)
