from math import floor, ceil


def calc(n):
    k = n // 10
    u = str(11 * n)


def is_palindrome(n):
    s = str(n)

    return s[::-1] == s


for i in range(1, 10000000):
    if is_palindrome(i) and len(str(i)) % 2 == 0:
        print(i)
