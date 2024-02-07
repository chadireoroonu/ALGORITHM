import sys
sys.stdin = open("../temp/input.txt")

N, K = list(map(int, sys.stdin.readline().split()))

# 물건 정보 저장
info = [[0, 0]]
for _ in range(N):
    W, V = list(map(int, sys.stdin.readline().split()))
    info.append([W, V])

# 각 무게의 최대 가치 저장
dp = [[0] * (K + 1) for _ in range(N + 1)]

# 물건의 개수 + 1 만큼 반복하며 무게, 가치 저장
for i in range(N + 1):
    weight = info[i][0]
    value = info[i][1]
    # 무게만큼 반복
    for j in range(K + 1):
        # 현재 무게 가방에 넣을 수 없다면, i-1의 최대가치 저장
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        # 현재 무게 가방에 넣을 수 있다면,
        # i-1의 최대가치와 현재 물건을 넣은 최대 가치 중 큰 값 저장
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[N][K])

# 틀린 코드
# import sys
# sys.stdin = open("../temp/input.txt")
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
#     weight = info[i][0]
#     value = info[i][1]
#     for j in range(K + 1):
#         if j < weight:
#             dp[i][j] = dp[i - 1][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
#
# print(dp[N - 1][K] if dp else 0)
