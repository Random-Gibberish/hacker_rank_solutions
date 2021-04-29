if __name__ == '__main__':
    N = int(input())
    my_list = []

    # The following loop performs the following actions
    # if present in the input:
    # insert, print, remove, append, sort, pop, reverse
    for _ in range(N):
        input_string = input().split()

        if input_string[0] == 'insert':
            my_list.insert(int(input_string[1]), int(input_string[2]))

        if input_string[0] == 'print':
            print(my_list)

        if input_string[0] == 'remove':
            my_list.remove(int(input_string[1]))

        if input_string[0] == 'append':
            my_list.append(int(input_string[1]))

        if input_string[0] == 'sort':
            my_list.sort()

        if input_string[0] == 'pop':
            my_list.pop()

        if input_string[0] == 'reverse':
            my_list.reverse()

    print(my_list)
