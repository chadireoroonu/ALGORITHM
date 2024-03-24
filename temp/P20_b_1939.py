import sys, heapq
sys.stdin = open("input.txt")

N, M = list(map(int, sys.stdin.readline().split()))
load = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C = list(map(int, sys.stdin.readline().split()))
    load[A].append([-C, B])
    load[B].append([-C, A])

S, E = list(map(int, sys.stdin.readline().split()))

queue = []
visited = [-int(1e9)] * (N + 1)
heapq.heappush(queue, [0, S])
visited[S] = 0

while queue:
    cost, x = heapq.heappop(queue)
    if x == E:
        break
    if visited[x] <= cost:
        for add, nx in load[x]:
            if cost + add > visited[nx]:
                visited[nx] = cost + add
                heapq.heappush(queue, [cost + add, nx])

print(-visited[E])