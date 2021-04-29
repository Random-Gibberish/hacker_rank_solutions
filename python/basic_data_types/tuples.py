if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    my_tuple = tuple(_ for _ in integer_list)

    print(hash(my_tuple))   # Prints the tuples hash number
