import sys
sys.stdin = open("../temp/input.txt")

C, N = map(int, sys.stdin.readline().split())
ad = []
# 비용 정보 없음, 고객의 수 최대 100명
dp = [int(1e9)] * (C + 100)
dp[0] = 0  # 0 초기화

for _ in range(N):
    cost, people = map(int, sys.stdin.readline().split())
    ad.append([cost, people])

for cost, people in ad:
    for i in range(people, C + 100):
        # dp[i - people] : i - people 명을 모을 때 최소비용
        dp[i] = min(dp[i], dp[i - people] + cost)

print(min(dp[C:]))
