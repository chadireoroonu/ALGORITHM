import sys, heapq
sys.stdin = open("../temp/input.txt")

def dijkstra(num):
    visited = [100001 * N for _ in range(N+1)]
    visited[num] = 0
    queue = []
    heapq.heappush(queue, [visited[num], num])

    while queue:
        count, now = heapq.heappop(queue)

        if count <= visited[now]:
            for i in load[now]:
                if visited[i[0]] > count + i[1]:
                    heapq.heappush(queue, [count + i[1], i[0]])
                    visited[i[0]] = count + i[1]

    return visited


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

load = [[] for _ in range(N+1)]

for i in range(M):
    S, E, M = list(map(int, sys.stdin.readline().split()))
    load[S].append([E, M])

start, end = list(map(int, sys.stdin.readline().split()))

result = dijkstra(start)

print(result[end])
