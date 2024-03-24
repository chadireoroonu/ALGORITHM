import sys, heapq
sys.stdin = open("input.txt")

def sol(n):
    for i in range(1, n+1):
        if djikstra(i) < 0:
            return print("YES")

    return print("NO")


def djikstra(n):
    visited = [int(1e9) for _ in range(N + 1)]
    queue = []
    heapq.heappush(queue, [0, n])

    while queue:
        cost, now = heapq.heappop(queue)

        if cost <= visited[now]:
            for add, next in load[now]:
                if visited[next] > cost + add:
                    visited[next] = cost + add
                    heapq.heappush(queue, [cost + add, next])

    return visited[n]



TC = int(sys.stdin.readline())

for _ in range(TC):
    N, M, W = list(map(int, sys.stdin.readline().split()))
    load = [[] for _ in range(N + 1)]

    for _ in range(M):
        S, E, T = list(map(int, sys.stdin.readline().split()))
        load[S].append([T, E])
        load[E].append([T, S])

    for _ in range(W):
        S, E, T = list(map(int, sys.stdin.readline().split()))
        load[S].append([-T, E])

    sol(N)