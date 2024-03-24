import sys
from collections import deque
sys.stdin = open("input.txt")


def lca(n, m):
    while depth[n] != depth[m]:
        if depth[n] > depth[m]:
            n = parent[n]
        else:
            m = parent[m]
    while n != m:
        n, m = parent[n], parent[m]
    return print(n)


N = int(sys.stdin.readline())
tree = [[] for _ in range(N + 1)]
parent = [[0] * N for _ in range(N + 1)]
depth = [-1] * (N + 1)

for _ in range(N - 1):
    a, b, = list(map(int, sys.stdin.readline().split()))
    tree[a].append(b)
    tree[b].append(a)

queue = deque([1])
depth[1] = 1
while queue:
    x = queue.popleft()
    for nx in tree[x]:
        if depth[nx] == -1:
            parent[nx][0] = x
            depth[nx] = depth[x] + 1
            queue.append(nx)

M = int(sys.stdin.readline())

for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    lca(a, b)