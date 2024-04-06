import sys
sys.stdin = open("../temp/input.txt")

n, k = map(int, sys.stdin.readline().split())
coins = []
dp = [float('inf')] * (k + 1)  # 초기값 무한
dp[0] = 0  # 0 만드는 동전 개수

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

# 각 coin에 대해 coin부터 k + 1까지
# dp[i], dp[i - coin] + 1 중 작은 값 저장
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

# 가지고 있는 동전으로 만들 수 있다면 최소 개수 출력
print(dp[k] if dp[k] < float('inf') else -1)
