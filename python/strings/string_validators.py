if __name__ == '__main__':
    s = input()
    is_isnt = [False] * 5   # Default False for all 5 values

    # Determines what is in the string
    for char in s:
        if char.isalnum():          # Letter or digit
            is_isnt[0] = True
        if char.isalpha():          # Letter
            is_isnt[1] = True
        if char.isdigit():          # Digit
            is_isnt[2] = True
        if char.islower():          # Lower case letter
            is_isnt[3] = True
        if char.isupper():          # Upper case letter
            is_isnt[4] = True

    for ans in is_isnt:
        print(ans)          # Print for each case
