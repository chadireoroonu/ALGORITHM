import sys
sys.stdin = open("../temp/input.txt")

N, M = map(int, sys.stdin.readline().split())
memories = list(map(int, sys.stdin.readline().split()))
costs = list(map(int, sys.stdin.readline().split()))
dp = [0] * (sum(costs) + 1)  # 각 비용으로 확보할 수 있는 최대 메모리

idx = len(dp)  # M 이상 메모리 확보를 위한 최소 비용
for i in range(N):
    memory, cost = memories[i], costs[i]
    # dp 역순회하며 확보가능한 최대메모리 저장
    for j in range(sum(costs), cost - 1, -1):
        dp[j] = max(dp[j], dp[j - cost] + memory)
        # 현재 최소비용보다 적은 비용으로 M 이상 메모리 확보 가능 시
        if j < idx and dp[j] >= M:
            idx = j

print(idx)
