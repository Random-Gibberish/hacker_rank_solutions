
def minion_game(s):
    """ Returns the winner of a game where Stuart count
        the substrings starting with a consonant and
        Kevin counts those starting with a vowel """

    vowels = 'AEIOU'

    total_count = int(len(s) * (len(s) + 1) / 2)
    k_count = sum(len(s) - i for i in range(len(s)) if s[i] in vowels)  # Kevin's count
    s_count = total_count - k_count     # Stuart's count

    if k_count > s_count:       # If Kevin wins
        print('Kevin ' + str(k_count))
    elif s_count > k_count:     # If Stuart wins
        print('Stuart ' + str(s_count))
    else:                       # If it's a draw
        print('Draw')


if __name__ == '__main__':
    my_string = input()
    minion_game(my_string)
