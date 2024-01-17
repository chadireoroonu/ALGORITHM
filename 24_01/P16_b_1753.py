import sys, heapq

def dijkstra(n):
    visited[n] = 0
    queue = []
    heapq.heappush(queue, [visited[n], n])

    while queue:
        distance, now = heapq.heappop(queue)

        if distance <= visited[now]:
            for cost, next in load[now]:
                if visited[next] > distance + cost:
                    visited[next] = distance + cost
                    heapq.heappush(queue, [distance + cost, next])
    return

V, E = list(map(int, sys.stdin.readline().split()))
load = [[] for _ in range(V + 1)]
start = int(sys.stdin.readline())
INF = 10 * (V + 1)
visited = [INF for _ in range(V + 1)]

for i in range(E):
    s, e, w = list(map(int, sys.stdin.readline().split()))
    load[s].append([w, e])

dijkstra(start)

for i in range(1, V+1):
    print(visited[i] if visited[i] < INF else "INF")