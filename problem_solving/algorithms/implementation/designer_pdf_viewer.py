#!/bin/python3

import os


def designer_pdf_viewer(height, word):
    """ Returns the area a PDF viewer will highlight
        if a word is selected """

    # Height of the tallest letter in the word
    max_height = max(height[ord(letter) - ord('a')] for letter in word)

    return max_height * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    character_heights = list(map(int, input().rstrip().split()))
    my_word = input()

    result = designer_pdf_viewer(character_heights, my_word)

    fptr.write(str(result) + '\n')
    fptr.close()
