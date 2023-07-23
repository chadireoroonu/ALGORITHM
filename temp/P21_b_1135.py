import sys
from collections import deque
sys.stdin = open('input.txt')

def check(n):
    global temp, depth
    if tree[n]:
        depth += 1
    temp += parent.count(n)
    for m in tree[n]:
        check(m[0])
    return

N = int(sys.stdin.readline().strip())
tree = [[] for _ in range(N)]
parent = list(map(int, sys.stdin.readline().split()))
child = [0] * N

for i in range(1, N):
    tree[parent[i]].append([i])

# 재귀를 활용해 총 자식 수, 깊이 세기
for i in range(N):
    temp = 0
    depth = 0
    check(i)
    child[i] = [temp, depth]

# child 정보 tree에 저장
for i in tree:
    for j in i:
        j.append(child[j[0]][0] + child[j[0]][1])
        j.append(child[j[0]][1])

visited = [0] * N
visited[0] = 0
queue = deque()
queue.append(0)

while queue:
    i = queue.popleft()
    order = 0
    # 총 자식 + 깊이 수가 같다면 깊이 우선 정렬
    tree[i].sort(key=lambda x: x[2], reverse=True)
    tree[i].sort(key=lambda x: x[1], reverse=True)
    for j in tree[i]:
        if not visited[j[0]]:
            queue.append(j[0])
            # 시간 기록
            visited[j[0]] = visited[i] + order + 1
            order += 1

print(max(visited))