import sys, heapq
sys.stdin = open("../temp/input.txt")

def minicost(num):
    visited = [int(1e9)] * (n + 1)
    visited[num] = 0
    queue = []
    heapq.heappush(queue, [0, num, [num]]) # 비용, 다음 목적지, 거쳐간 도시

    # 각 도착지까지의 최소 비용으로 거쳐간 도시 저장
    temp = [[] for _ in range(n + 1)]

    while queue:
        cost, x, past = heapq.heappop(queue)
        if cost <= visited[x]:
            for add, nx in load[x]:
                # 최소 비용 경로 발견 시, temp 재할당
                if visited[nx] > cost + add:
                    visited[nx] = cost + add
                    temp[nx] = past + [nx]
                    heapq.heappush(queue, [cost + add, nx, past + [nx]])
    # result 배열에 최종 temp 반영
    result.append(temp)

    # 각 도착지까지의 최소 비용 출력
    for i in range(n):
        print(visited[i + 1] if visited[i + 1] < int(1e9) else 0, end=" ")

    return print()


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
load = [[] for _ in range(n + 1)]
result = []

# 정보 입력
for _ in range(m):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    load[a].append([c, b])

# 각 출발지에서 모든 도착지로 최소 비용 경로 탐색
for i in range(n):
    minicost(i + 1)

# 각 출발지에서 최소 비용 거리로 이동 시 경로 출력
for i in range(n):
    for j in range(1, len(result[i])):
        # 경로의 길이
        print(len(result[i][j]), end=" ")
        # 거쳐간 도시
        for k in result[i][j]:
            print(k, end=" ")
        print()