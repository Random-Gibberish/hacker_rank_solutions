from itertools import product

if __name__ == '__main__':
    A = [int(i) for i in input().split()]
    B = [int(j) for j in input().split()]

    # Unpack and print the cartesian product of A and B
    print(*product(A, B))
