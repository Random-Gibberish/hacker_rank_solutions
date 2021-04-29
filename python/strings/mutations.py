def mutate_string(string, pos_i, char):
    """ Swaps character a 'pos_i' with 'char' """

    string = string[:pos_i] + char + string[pos_i + 1:]

    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)

    print(s_new)
