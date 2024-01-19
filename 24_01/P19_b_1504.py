import sys, heapq
sys.stdin = open("../temp/input.txt")


def djikstra(start, end):
    visited = [int(1e9) for _ in range(N + 1)]
    visited[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        cost, now = heapq.heappop(queue)

        if cost <= visited[now]:
            for add, next in load[now]:
                if visited[next] > cost + add:
                    visited[next] = cost + add
                    heapq.heappush(queue, [cost + add, next])

    return visited[end]


N, E = list(map(int, sys.stdin.readline().split()))
load = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    load[a].append([c, b])
    load[b].append([c, a])

v1, v2 = list(map(int, sys.stdin.readline().split()))

sol1 = djikstra(1, v1) + djikstra(v1, v2) + djikstra(v2, N)
sol2 = djikstra(1, v2) + djikstra(v2, v1) + djikstra(v1, N)

if sol1 >= int(1e9) and sol2 >= int(1e9):
    print(-1)
else:
    print(min(sol1, sol2))