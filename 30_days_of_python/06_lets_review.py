
def even_odd_letters(word):
    """ Returns two strings containing the even and odd
        indexed letters in a word on separate lines """

    even_letters = ''
    odd_letters = ''

    for j in range(len(word)):
        if j % 2 == 0:
            even_letters += word[j]
        else:
            odd_letters += word[j]

    string_letters = '{} {}'.format(even_letters, odd_letters)

    return string_letters


if __name__ == '__main__':
    words = int(input())

    for _ in range(words):
        complete_word = input()

        letters = even_odd_letters(complete_word)
