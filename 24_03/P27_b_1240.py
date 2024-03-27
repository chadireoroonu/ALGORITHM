import sys
from collections import deque
sys.stdin = open("../temp/input.txt")


def sol(n, m):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        for nx, add in tree[x]:
            if nx == m:  # 도착했다면 거리 출력 반환
                return print(visited[x] + add)
            if not visited[nx]:  # 도착하지 못했다면 이동 기록
                visited[nx] = visited[x] + add
                queue.append(nx)
    return


N, M = list(map(int, sys.stdin.readline().split()))
tree = [[] for _ in range(N + 1)]  # 연결 정보 저장

for _ in range(N - 1):  # 양방향 연결 정보, 거리 기록
    u, v, c = list(map(int, sys.stdin.readline().split()))
    tree[u].append([v, c])
    tree[v].append([u, c])

for _ in range(M):  # 거리 구하기
    visited = [0] * (N + 1)  # 출발 노드부터의 거리
    s, e = list(map(int, sys.stdin.readline().split()))
    sol(s, e)
