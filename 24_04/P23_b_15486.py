import sys
sys.stdin = open("../temp/input.txt")

N = int(sys.stdin.readline())
counsel = [(0, 0)]  # 상담정보
dp = [0] * (N + 1)  # 각 일자의 최고 금액

for _ in range(N):
    day, score = map(int, sys.stdin.readline().split())
    counsel.append((day, score))

for i in range(1, N + 1):
    day, score = counsel[i]
    # 현재 저장된 값과 이전 값 중 큰 값을 현재 최대 금액에 재할당
    dp[i] = max(dp[i], dp[i - 1])
    # 퇴사일 전에 해결할 수 있는 상담일 경우,
    # 현재 상담 완료 시 금액과 이미 저장되어 있는 최대 금액 비교 후 큰 값 저장
    if i + day <= N + 1:
        dp[i + day - 1] = max(dp[i + day - 1], dp[i - 1] + score)

# 저장된 값 중 가장 큰 값 출력
print(max(dp))
