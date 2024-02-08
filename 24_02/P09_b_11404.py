import sys, heapq
sys.stdin = open("../temp/input.txt")

def minicost(num):
    # visited 숫자는 최대치로 설정
    visited = [int(1e9)] * (n + 1)

    # visited[num]까지의 비용 0
    visited[num] = 0
    queue = []
    heapq.heappush(queue, [0, num])

    while queue:
        # 가장 작은 cost 부터 탐색
        cost, x = heapq.heappop(queue)

        # cost 가 visited[x] 보다 크다면 중단
        if cost <= visited[x]:
            # 출발지가 x인 길들의 비용, 목적지
            for add, nx in load[x]:
                # 현재 경로가 최소경로라면 갱신 후 힙 추가
                if visited[nx] > cost + add:
                    visited[nx] = cost + add
                    heapq.heappush(queue, [cost + add, nx])

    # 1 ~ n 까지의 최소비용 출력
    for i in range(1, n + 1):
        print(visited[i] if visited[i] != int(1e9) else 0, end=" ")

    return print()


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
load = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    load[a].append([c, b])

# 1 ~ n 까지 각 출발지에서의 모든 도착지까지 최소 비용 탐색
for i in range(1, n + 1):
    minicost(i)