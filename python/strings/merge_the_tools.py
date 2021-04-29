
def merge_the_tools(string, k):
    """ . s is split into n/k substrings t_i
        . form strings u_i from each t_i with
          repeated characters removed
        Returns each string u_i """

    n = len(string)

    for num_str in range(n // k):                   # For each substring
        t = string[num_str * k:num_str * k + k]     # Form the substring t_i
        u = []

        for letter in t:
            if letter not in u:
                u.append(letter)    # Append letters to u_i if not repeated

        u = ''.join(u)      # Form string
        print(u)            # Print for each substring


if __name__ == '__main__':
    my_string, divisor = input(), int(input())
    merge_the_tools(my_string, divisor)
