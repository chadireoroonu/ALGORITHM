import sys
sys.stdin = open("../temp/input.txt")

N, K = list(map(int, sys.stdin.readline().split()))
info = [[0, 0]]

for _ in range(N):
    W, V = list(map(int, sys.stdin.readline().split()))
    info.append([W, V])

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(K + 1):
        weight = info[i][0]
        value = info[i][1]
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[N][K])

# 틀린 코드
# import sys
# sys.stdin = open("input.txt")
#
# N, K = list(map(int, sys.stdin.readline().split()))
# info = []
#
# for _ in range(N):
#     W, V = list(map(int, sys.stdin.readline().split()))
#     info.append([W, V])
#
# dp = [[0] * (K + 1) for _ in range(N)]
#
# for i in range(N):
#     for j in range(K + 1):
#         weight = info[i][0]
#         value = info[i][1]
#         if j < weight:
#             dp[i][j] = dp[i - 1][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
#
# print(dp[N - 1][K] if dp else 0)
