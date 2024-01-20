import sys
from collections import deque
sys.stdin = open("../temp/input.txt")

def BFS(n):
    global start
    visited = [-1 for _ in range(V + 1)]
    queue = deque([n])
    visited[n] = 0

    while queue:
        now = queue.popleft()

        for cost, next in tree[now]:
            if visited[next] < 0:
                visited[next] = visited[now] + cost
                queue.append(next)

    start = visited.index(max(visited))
    return max(visited)


V = int(sys.stdin.readline())
tree = [[] for _ in range(V + 1)]
start = 0

for _ in range(V):
    temp = list(map(int, sys.stdin.readline().split()))
    start = temp[0]
    for i in range(1, len(temp)-1):
        if i % 2:
            tree[temp[0]].append([temp[i+1], temp[i]])

BFS(1)
print(BFS(start))