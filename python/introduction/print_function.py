if __name__ == '__main__':
    n = int(input())
    m = 0

    # Print the integers from 1 to n on a single line
    for i in range(1, n + 1):
        if 10 <= i < 100:
            m *= 10
        elif i >= 100:
            m *= 100

        m += i * 10 ** (n - i)
    print(m)
