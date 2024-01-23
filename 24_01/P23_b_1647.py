import sys, heapq
sys.stdin = open("../temp/input.txt")

# 현재 노드의 부모 탐색
def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

# 두 노드의 부모 연결
def union(n, m):
    if n > m:
        n, m = m, n
    parent[m] = n
    return


N, M = list(map(int, sys.stdin.readline().split()))
parent = [i for i in range(N + 1)]
queue = []

for _ in range(M):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    # 유지비가 작은 순서대로 저장
    heapq.heappush(queue, [c, a, b])

# 총 유지비
result = 0

# 끊을 길 유지비
last = 0

while queue:
    add, x, y = heapq.heappop(queue)
    # 두 노드의 부모가 연결되어 있지 않다면
    # 연결 후 총 유지비에 해당 길의 유지비 합산
    # 마지막 길의 정보 저장
    if find(x) != find(y):
        union(find(x), find(y))
        result += add
        last = add

# 전체 유지비 - 마지막 길 유지비 출력
print(result - last)