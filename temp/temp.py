cost = [-1, 1]
n = len(cost)

A = [0] * (n + 1)
B = [0] * (n + 1)

for i in range(1, n + 1):
    # We make the ith position a 1 or a -1
    A[i] = min(A[i - 1] + abs(1 - cost[i - 1]), B[i - 1] + abs(-1 - cost[i - 1]))
    B[i] = min(A[i - 1] + abs(1 - cost[i - 1]), B[i - 1] + abs(-1 - cost[i - 1]))

print(A[i])
