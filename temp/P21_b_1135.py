import sys
from collections import deque
sys.stdin = open('input.txt')

def check(n):
    global temp, depth
    depth += 1
    temp += parnet.count(n)
    for m in tree[n]:
        check(m[0])
    return

N = int(sys.stdin.readline().strip())
tree = [[] for _ in range(N)]
parnet = list(map(int, sys.stdin.readline().split()))
child = [0] * N

for i in range(1, N):
    tree[parnet[i]].append([i])

# 재귀를 활용해 총 자식 수, 깊이 세기
for i in range(N):
    temp = 0
    depth = 0
    check(i)
    # depth 기준 정렬 후 자식 수 기준 정렬 추가하기
    child[i] = temp + depth

# 총 자식의 수를 트리 구조에 추가해주기
for i in tree:
    for j in i:
        j.append(child[j[0]])

visited = [0] * N
visited[0] = 0
queue = deque()
queue.append(0)

while queue:
    i = queue.popleft()
    order = 0
    # 깊이 고려, 자식 수를 기준으로 정렬
    tree[i].sort(key=lambda x: x[1], reverse=True)
    print(tree)
    for j in tree[i]:
        if not visited[j[0]]:
            queue.append(j[0])
            visited[j[0]] = visited[i] + order + 1
            order += 1

print(max(visited))