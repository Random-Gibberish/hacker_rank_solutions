from itertools import groupby

if __name__ == '__main__':
    S = input().strip()

    # Returns (character, occurrences) tuples from string S
    comp_S = [(len([*times]), int(num)) for num, times in groupby(S)]

    print(*comp_S)  # Unpack the list and print each tuple on a single line
