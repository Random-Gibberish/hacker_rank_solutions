def count_substring(string, sub_string):
    """ Counts how many times sub_string appears in string """

    count = 0

    for i in range(len(string) - len(sub_string) + 1):
        if sub_string == string[i:i+len(sub_string)]:   # If substring is found
            count += 1

    return count


if __name__ == '__main__':
    my_string = input().strip()
    my_sub_string = input().strip()

    cnt = count_substring(my_string, my_sub_string)
    print(cnt)
