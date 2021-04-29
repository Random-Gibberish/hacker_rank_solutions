if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # All permutations of i, j, k in ranges x, y, z
    permutations = [[i, j, k] for i in range(x + 1)
                              for j in range(y + 1)
                              for k in range(z + 1)]

    # Keep all permutations that don't sum to n
    result = [permutation for permutation in permutations
              if sum(permutation) != n]

    print(result)
