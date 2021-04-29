def split_and_join(s):
    split_s = s.split()             # Split words according to whitespace
    dashed_s = "-".join(split_s)    # Join words with dashed line

    return dashed_s


if __name__ == '__main__':
    my_string = input()
    result = split_and_join(my_string)

    print(result)
