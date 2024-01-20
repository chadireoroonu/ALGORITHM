import sys, heapq
sys.stdin = open("../temp/input.txt")

N, M = list(map(int, sys.stdin.readline().split()))

# 먼저 거쳐야 하는 문제 수
previous = [0 for _ in range(N + 1)]

# 다음에 풀 문제 번호
next = [[] for _ in range(N + 1)]

for _ in range(M):
    p, s = list(map(int, sys.stdin.readline().split()))
    previous[s] += 1
    next[p].append(s)

queue = []
for i in range(1, N + 1):
    # 먼저 풀어야하는 문제가 없는 번호를 큐에 추가
    if not previous[i]:
        heapq.heappush(queue, i)

while queue:
    # 힙큐로 가장 작은 번호를 반환, 출력
    now = heapq.heappop(queue)
    print(now, end=" ")

    # 해당 문제 후 풀 문제들의 선행문제 조건 변경
    # 먼저 풀어야 하는 문제를 다 풀었다면, 큐에 추가
    if next[now]:
        for j in next[now]:
            previous[j] -= 1
            if not previous[j]:
                heapq.heappush(queue, j)