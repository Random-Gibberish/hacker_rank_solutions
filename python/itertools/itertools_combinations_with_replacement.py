from itertools import combinations_with_replacement

if __name__ == '__main__':
    Sk = input().strip()
    S = Sk[:-2]
    k = int(Sk[-1])

    # Combinations of S of length k with replacement
    combs_r = [sorted(comb_r) for comb_r in combinations_with_replacement(S, k)]
    combs_r = [''.join(_) for _ in combs_r]

    for comb in sorted(combs_r):
        print(comb)
