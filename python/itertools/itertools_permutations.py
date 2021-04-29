from itertools import permutations

if __name__ == '__main__':
    Sk = input().strip()
    S = Sk[:-2]
    k = int(Sk[-1])

    # All permutations in S of length k
    perms = [''.join(_) for _ in permutations(S, k)]

    for perm in sorted(perms):
        print(perm)
