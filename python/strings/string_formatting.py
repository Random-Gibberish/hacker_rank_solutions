def print_formatted(num):
    """ Print numbers from 1 to 'num' in decimal, octal,
        hexadecimal and binary in four columns formatted
        to the width of the longest binary number """

    for i in range(1, num + 1):
        width = len(bin(num)[2:])
        #           decimal      octal        hexadecimal  binary
        print(f'{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}')


if __name__ == '__main__':
    number = int(input())

    print_formatted(number)
