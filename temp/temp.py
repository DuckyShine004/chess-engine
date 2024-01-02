from functools import cache


def getWays(n, c):
    res = 0

    def dp(x):
        nonlocal res

        if x >= n:
            if x == n:
                res += 1

            return

        for coin in c:
            dp(x + coin)

    dp(0)

    print(res)

    return 1


c = [1, 2, 3]
n = 4
getWays(n, c)
