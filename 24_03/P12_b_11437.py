import sys
from collections import deque
sys.stdin = open("../temp/input.txt")

# 공통 조상 찾기 함수
def find(n, m):
    # 깊이 맞추기
    while depth[n] != depth[m]:
        if depth[n] > depth[m]:
            n = parent[n]
        else:
            m = parent[m]
    # 깊이가 같다면 공통 조상까지 역행
    while n != m:
        n, m = parent[n], parent[m]

    return print(n)


N = int(sys.stdin.readline())
# 연결 정보 저장
tree = [[] for _ in range(N + 1)]
# 부모 노드 기록
parent = [0] * (N + 1)
# 깊이 기록
depth = [0] * (N + 1)

# 입력
for _ in range(N  - 1):
    a, b = list(map(int, sys.stdin.readline().split()))
    tree[a].append(b)
    tree[b].append(a)

# 트리 부모 정리
queue = deque([1])
while queue:
    x = queue.popleft()
    for nx in tree[x]:
        if nx != parent[x]:
            parent[nx] = x
            depth[nx] = depth[x] + 1
            queue.append(nx)

M = int(sys.stdin.readline())

# 공통조상 찾을 두 수
for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    find(a, b)