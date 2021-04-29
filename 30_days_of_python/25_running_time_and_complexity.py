import random


def is_prime(num):
    if num in [0, 1, 4, 6, 8, 9]:   # Not prime
        return False

    if num in [2, 3, 5, 7]:         # Prime
        return True

    # Miller-Rabin test for prime
    s = 0
    d = num - 1
    while d % 2 == 0:
        d >>= 1
        s += 1

    # Witness Loop
    for _ in range(8):
        a = random.randrange(2, num - 2)    # Pick random number in range [2, num - 2]

        if pow(a, d, num) == 1:     # If a^d = 1 (mod num)
            return True             # then 'num' is a strong probable prime

        for i in range(s):
            if pow(a, 2 ** i * d, num) == num - 1:  # If a^(2^i * d) = num - 1 (mod num)
                return True                         # then num is a strong probable prime

        # If neither condition is triggered 'num' is definitely not prime
        return False


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        number = int(input())

        if is_prime(number):
            print("Prime")
        else:
            print("Not prime")
