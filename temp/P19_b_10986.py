import sys
sys.setrecursionlimit(10 ** 9)
sys.stdin = open("input.txt")



def dp(n, total):
    global count
    if total and not total % M:
        count += 1
    if n == N:
        return
    dp(n + 1, total + nums[n])
    return

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
count = 0

# dp = [[0] * N for _ in range(N)]

# for i in range(N):
#     for j in range(i, N):
#         dp[i][j] = dp[i][j - 1] + nums[j]
#         if not dp[i][j] % M:
#             count += 1

for i in range(N):
    dp(i, 0)

print(count)
