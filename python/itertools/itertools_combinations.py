from itertools import combinations

if __name__ == '__main__':
    Sk = input().split()
    S = Sk[0]
    k = int(Sk[1])

    combs = []

    for i in range(1, k+1):
        # Combinations in S of length i
        combs = [sorted(comb) for comb in combinations(S, i)]

        for comb in sorted(combs):
            print(''.join(comb))
