import sys
sys.stdin = open("../temp/input.txt")

n, k = map(int, sys.stdin.readline().split())
coins = []

for _ in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)

dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    # 해당 동전으로 만들 수 있는 경우의 수 추가
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

# k 값이 되는 경우의 수
print(dp[k])
