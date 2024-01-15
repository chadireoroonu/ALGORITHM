import sys
from collections import deque
sys.stdin = open("../temp/input.txt")

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

load = [[] for _ in range(N+1)]
result = []

for i in range(M):
    S, E, M = list(map(int, sys.stdin.readline().split()))
    load[S].append([E, M])

s, e = list(map(int, sys.stdin.readline().split()))

queue = deque()
queue.append([s, 0])
visited = [100001 * N for _ in range(N + 1)]
visited[s] = 0

for i in range(N+1):
    if load[i]:
        load[i].sort(key=lambda x: x[1])

while queue:
    now, count = queue.popleft()
    if count <= visited[now]:
        for i in load[now]:
            if visited[i[0]] > visited[now] + i[1]:
                visited[i[0]] = visited[now] + i[1]
                if i[0] == e:
                    result.append(visited[i[0]])
                queue.append([i[0], count + i[1]])

print(min(result))
