import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(sys.stdin.readline().strip())
tree = [[] for _ in range(N)]
parent = list(map(int, sys.stdin.readline().split()))

for i in range(1, N):
    tree[parent[i]].append([i])

visited = [0] * N
queue = deque()
queue.append(0)
visited[0] = 0

while queue:
    i = queue.popleft()
    order = 0
    # 여기서 정렬
    for j in tree[i]:
        j.append(len(tree[j[0]]))
    tree[i].sort(key=lambda x: x[1], reverse=True)
    for j in tree[i]:
        if not visited[j[0]]:
            queue.append(j[0])
            visited[j[0]] = visited[i] + order + 1
            order += 1

print(max(visited))