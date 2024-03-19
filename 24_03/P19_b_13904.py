import sys, heapq
sys.stdin = open("../temp/input.txt")

N = int(sys.stdin.readline())
queue = []  # 마감일 우선 과제 정보 정렬
dp = []  # 점수 낮은순 정렬

for _ in range(N):
    limit, score = map(int, sys.stdin.readline().split())
    heapq.heappush(queue, (limit, score))

while queue:
    limit, score = heapq.heappop(queue)
    # 마감일 내에 할 수 있는 일이라면 추가
    if len(dp) < limit:
        heapq.heappush(dp, score)
    # 마감일까지 과제 일정이 차있는 경우, 제일 낮은 점수와 비교 후 교체
    else:
        if dp[0] < score:
            heapq.heappop(dp)
            heapq.heappush(dp, score)

print(sum(dp))