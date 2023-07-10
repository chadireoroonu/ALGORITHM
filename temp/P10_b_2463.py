import sys
sys.stdin = open('input.txt')

def check(n):
    if parent[n] != n:
        parent[n] = check(parent[n])
    return parent[n]

N, M = map(int, sys.stdin.readline().split())
road = []
result = 0

for _ in range(M):
    x, y, w = map(int, sys.stdin.readline().split())
    if x > y:
        x, y = y, x
    road.append((w, x, y))

road.sort()
parent = [i for i in range(N+1)]
child = [[] for _ in range(N+1)]

for i in range(len(road)):
    w, x, y = road[i]
    if x > y:
        x, y = y, x
    if check(x) != check(y):
        parent[check(y)] = check(x)
        child[x].append(y)

for i in range(N-1):
    for j in range(i, N):


print(child)