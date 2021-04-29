import os


def solve(s):
    """ Capitalises the first letter of each word """

    name = list(s)              # Make a list out of the word
    name[0] = name[0].upper()   # Capitalise the first word

    for i in range(len(name)):
        if name[i] == ' ':                  # If there is a whitespace at i
            name[i+1] = name[i+1].upper()   # Capitalise the next letter

    s = ''.join(name)       # Rejoin the words

    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    my_string = input()

    result = solve(my_string)

    fptr.write(result + '\n')
    fptr.close()
