import sys
from collections import deque
sys.stdin = open("../temp/input.txt")

def BFS(s):
    global start
    visited = [-1 for _ in range(n + 1)]
    visited[s] = 0
    queue = deque([s])

    while queue:
        now = queue.popleft()

        for cost, next in load[now]:
            if visited[next] < 0:
                visited[next] = visited[now] + cost
                queue.append(next)

    start = visited.index(max(visited))
    return max(visited)

n = int(sys.stdin.readline())
load = [[] for _ in range(n + 1)]
start = 0

for _ in range(n-1):
    p, r, c = list(map(int, sys.stdin.readline().split()))
    load[p].append([c, r])
    load[r].append([c, p])

BFS(1)
print(BFS(start))
